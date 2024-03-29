# -*- coding: utf-8 -*-
"""
    sphinx.util.nodes
    ~~~~~~~~~~~~~~~~~

    Docutils node-related utility functions for Sphinx.

    :copyright: Copyright 2007-2011 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from docutils import nodes

from sphinx import addnodes
from sphinx.locale import pairindextypes
from sphinx.util.pycompat import class_types


# \x00 means the "<" was backslash-escaped
explicit_title_re = re.compile(r'^(.+?)\s*(?<!\x00)<(.*?)>$', re.DOTALL)
caption_ref_re = explicit_title_re  # b/w compat alias


def extract_messages(doctree):
    """Extract translatable messages from a document tree."""
    for node in doctree.traverse(nodes.TextElement):
        if isinstance(node, (nodes.Invisible, nodes.Inline)):
            continue
        # <field_name>orphan</field_name>
        # XXX ignore all metadata (== docinfo)
        if isinstance(node, nodes.field_name) and node.children[0] == 'orphan':
            continue
        msg = node.rawsource.replace('\n', ' ').strip()
        # XXX nodes rendering empty are likely a bug in sphinx.addnodes
        if msg:
            yield node, msg


def nested_parse_with_titles(state, content, node):
    """Version of state.nested_parse() that allows titles and does not require
    titles to have the same decoration as the calling document.

    This is useful when the parsed content comes from a completely different
    context, such as docstrings.
    """
    # hack around title style bookkeeping
    surrounding_title_styles = state.memo.title_styles
    surrounding_section_level = state.memo.section_level
    state.memo.title_styles = []
    state.memo.section_level = 0
    try:
        return state.nested_parse(content, 0, node, match_titles=1)
    finally:
        state.memo.title_styles = surrounding_title_styles
        state.memo.section_level = surrounding_section_level


def clean_astext(node):
    """Like node.astext(), but ignore images."""
    node = node.deepcopy()
    for img in node.traverse(nodes.image):
        img['alt'] = ''
    return node.astext()


def split_explicit_title(text):
    """Split role content into title and target, if given."""
    match = explicit_title_re.match(text)
    if match:
        return True, match.group(1), match.group(2)
    return False, text, text


indextypes = [
    'single', 'pair', 'double', 'triple', 'see', 'seealso',
]

def process_index_entry(entry, targetid):
    indexentries = []
    entry = entry.strip()
    oentry = entry
    main = ''
    if entry.startswith('!'):
        main = 'main'
        entry = entry[1:].lstrip()
    for type in pairindextypes:
        if entry.startswith(type+':'):
            value = entry[len(type)+1:].strip()
            value = pairindextypes[type] + '; ' + value
            indexentries.append(('pair', value, targetid, main))
            break
    else:
        for type in indextypes:
            if entry.startswith(type+':'):
                value = entry[len(type)+1:].strip()
                if type == 'double':
                    type = 'pair'
                indexentries.append((type, value, targetid, main))
                break
        # shorthand notation for single entries
        else:
            for value in oentry.split(','):
                value = value.strip()
                main = ''
                if value.startswith('!'):
                    main = 'main'
                    value = value[1:].lstrip()
                if not value:
                    continue
                indexentries.append(('single', value, targetid, main))
    return indexentries


def inline_all_toctrees(builder, docnameset, docname, tree, colorfunc):
    """Inline all toctrees in the *tree*.

    Record all docnames in *docnameset*, and output docnames with *colorfunc*.
    """
    tree = tree.deepcopy()
    for toctreenode in tree.traverse(addnodes.toctree):
        newnodes = []
        includefiles = map(str, toctreenode['includefiles'])
        for includefile in includefiles:
            try:
                builder.info(colorfunc(includefile) + " ", nonl=1)
                subtree = inline_all_toctrees(builder, docnameset, includefile,
                    builder.env.get_doctree(includefile), colorfunc)
                docnameset.add(includefile)
            except Exception:
                builder.warn('toctree contains ref to nonexisting '
                             'file %r' % includefile,
                             builder.env.doc2path(docname))
            else:
                sof = addnodes.start_of_file(docname=includefile)
                sof.children = subtree.children
                newnodes.append(sof)
        toctreenode.parent.replace(toctreenode, newnodes)
    return tree


def make_refnode(builder, fromdocname, todocname, targetid, child, title=None):
    """Shortcut to create a reference node."""
    node = nodes.reference('', '', internal=True)
    if fromdocname == todocname:
        node['refid'] = targetid
    else:
        node['refuri'] = (builder.get_relative_uri(fromdocname, todocname)
                          + '#' + targetid)
    if title:
        node['reftitle'] = title
    node.append(child)
    return node

# monkey-patch Node.traverse to get more speed
# traverse() is called so many times during a build that it saves
# on average 20-25% overall build time!

def _all_traverse(self, result):
    """Version of Node.traverse() that doesn't need a condition."""
    result.append(self)
    for child in self.children:
        child._all_traverse(result)
    return result

def _fast_traverse(self, cls, result):
    """Version of Node.traverse() that only supports instance checks."""
    if isinstance(self, cls):
        result.append(self)
    for child in self.children:
        child._fast_traverse(cls, result)
    return result

def _new_traverse(self, condition=None,
                 include_self=1, descend=1, siblings=0, ascend=0):
    if include_self and descend and not siblings and not ascend:
        if condition is None:
            return self._all_traverse([])
        elif isinstance(condition, class_types):
            return self._fast_traverse(condition, [])
    return self._old_traverse(condition, include_self,
                              descend, siblings, ascend)

nodes.Node._old_traverse = nodes.Node.traverse
nodes.Node._all_traverse = _all_traverse
nodes.Node._fast_traverse = _fast_traverse
nodes.Node.traverse = _new_traverse

# monkey-patch Node.__contains__ to get consistent "in" operator behavior
# across docutils versions

def _new_contains(self, key):
    # support both membership test for children and attributes
    # (has_key is translated to "in" by 2to3)
    if isinstance(key, basestring):
        return key in self.attributes
    return key in self.children

nodes.Node.__contains__ = _new_contains

# monkey-patch Element.copy to copy the rawsource

def _new_copy(self):
    return self.__class__(self.rawsource, **self.attributes)

nodes.Element.copy = _new_copy

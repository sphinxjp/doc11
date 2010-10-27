# -*- coding: utf-8 -*-
"""
    sphinx.builders.intl
    ~~~~~~~~~~~~~~~~~~~~

    The MessageCatalogBuilder class.

    :copyright: Copyright 2007-2010 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from os import path
from codecs import open
from datetime import datetime
from collections import defaultdict

from docutils import nodes

from sphinx.builders import Builder
from sphinx.builders.versioning import VersioningBuilderMixin
from sphinx.util.nodes import extract_messages
from sphinx.util.osutil import SEP, copyfile
from sphinx.util.console import darkgreen
from sphinx.util.ordereddict import OrderedDict

POHEADER = ur"""
# SOME DESCRIPTIVE TITLE.
# Copyright (C) %(copyright)s
# This file is distributed under the same license as the %(project)s package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: %(version)s\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: %(ctime)s\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

"""[1:]


class I18nBuilder(Builder, VersioningBuilderMixin):
    """
    General i18n builder.
    """
    name = 'i18n'

    def init(self):
        Builder.init(self)
        VersioningBuilderMixin.init(self)
        self.catalogs = defaultdict(OrderedDict)
        self.last_source = None

    def get_target_uri(self, docname, typ=None):
        return ''

    def get_outdated_docs(self):
        return self.env.found_docs

    def prepare_writing(self, docnames):
        return

    def write_doc(self, docname, doctree):
        catalog = self.catalogs[docname.split(SEP, 1)[0]]

        self.handle_versioning(docname, doctree, nodes.TextElement)

        for node, msg in extract_messages(doctree):
            if node.source is None:
                if self.last_source is not None:
                    source = self.last_source
                else:
                    source = "(unknown)"
            else:
                source = self.last_source = path.basename(node.source)
            if node.line is None:
                line = 0
            else:
                line = node.line 
            catalog.setdefault(msg, []).append((source, line))

    def finish(self):
        Builder.finish(self)
        VersioningBuilderMixin.finish(self)


class MessageCatalogBuilder(I18nBuilder):
    """
    Builds gettext-style message catalogs (.pot files).
    """
    name = 'gettext'

    def finish(self):
        I18nBuilder.finish(self)
        data = dict(
            version = self.config.version,
            copyright = self.config.copyright,
            project = self.config.project,
            # XXX should supply tz
            ctime = datetime.now().strftime('%Y-%m-%d %H:%M%z'),
        )
        for section, messages in self.status_iterator(
                self.catalogs.iteritems(), "writing message catalogs... ",
                lambda (section, _):darkgreen(section), len(self.catalogs)):

            pofn = path.join(self.outdir, section + '.pot')
            pofile = open(pofn, 'w', encoding='utf-8')
            try:
                pofile.write(POHEADER % data)
                for message, poss in messages.iteritems():
                    # message contains *one* line of text ready for translation
                    pos = self._join(
                        ["%s(%d)" % (s, l) for s, l in poss])
                    message = message.replace(u'\\', ur'\\'). \
                                      replace(u'"', ur'\"')
                    pomsg = u'%s\nmsgid "%s"\nmsgstr ""\n\n' % (pos, message)
                    pofile.write(pomsg)
            finally:
                pofile.close()

    def _join(self, strings, prefix="# ", sep=", ", max_length=70):
        lines = [[prefix, strings[0]]]
        strings = strings[1:]
        length = max_length - len(prefix)
        while strings:
            next = strings[0]
            del strings[0]
            if length - len(next) - len(sep) < 0:
                length = max_length - len(next) - len(prefix)
                lines[-1] = "".join(lines[-1])
                lines.append([prefix, next])
            else:
                lines[-1].append(sep)
                lines[-1].append(next)
                length = length - len(sep) - len(next)
        lines[-1] = "".join(lines[-1])
        return "\n".join(lines)

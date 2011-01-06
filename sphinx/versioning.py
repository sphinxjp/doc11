# -*- coding: utf-8 -*-
"""
    sphinx.versioning
    ~~~~~~~~~~~~~~~~~

    Implements the low-level algorithms Sphinx uses for the versioning of
    doctrees.

    :copyright: Copyright 2007-2011 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
from uuid import uuid4
from operator import itemgetter
from collections import defaultdict

from sphinx.util.pycompat import product, zip_longest


# anything below that ratio is considered equal/changed
VERSIONING_RATIO = 65


def add_uids(doctree, condition):
    """Add a unique id to every node in the `doctree` which matches the
    condition and yield the nodes.

    :param doctree:
        A :class:`docutils.nodes.document` instance.

    :param condition:
        A callable which returns either ``True`` or ``False`` for a given node.
    """
    for node in doctree.traverse(condition):
        node.uid = uuid4().hex
        yield node


def merge_doctrees(old, new, condition):
    """Merge the `old` doctree with the `new` one while looking at nodes
    matching the `condition`.

    Each node which replaces another one or has been added to the `new` doctree
    will be yielded.

    :param condition:
        A callable which returns either ``True`` or ``False`` for a given node.
    """
    old_iter = old.traverse(condition)
    new_iter = new.traverse(condition)
    old_nodes = []
    new_nodes = []
    ratios = defaultdict(list)
    seen = set()
    # compare the nodes each doctree in order
    for old_node, new_node in zip_longest(old_iter, new_iter):
        if old_node is None:
            new_nodes.append(new_node)
            continue
        if new_node is None:
            old_nodes.append(old_node)
            continue
        ratio = get_ratio(old_node.rawsource, new_node.rawsource)
        if ratio == 0:
            new_node.uid = old_node.uid
            seen.add(new_node)
        else:
            ratios[old_node, new_node] = ratio
            old_nodes.append(old_node)
            new_nodes.append(new_node)
    # calculate the ratios for each unequal pair of nodes, should we stumble
    # on a pair which is equal we set the uid and add it to the seen ones
    for old_node, new_node in product(old_nodes, new_nodes):
        if new_node in seen or (old_node, new_node) in ratios:
            continue
        ratio = get_ratio(old_node.rawsource, new_node.rawsource)
        if ratio == 0:
            new_node.uid = old_node.uid
            seen.add(new_node)
        else:
            ratios[old_node, new_node] = ratio
    # choose the old node with the best ratio for each new node and set the uid
    # as long as the ratio is under a certain value, in which case we consider
    # them not changed but different
    ratios = sorted(ratios.iteritems(), key=itemgetter(1))
    for (old_node, new_node), ratio in ratios:
        if new_node in seen:
            continue
        else:
            seen.add(new_node)
        if ratio < VERSIONING_RATIO:
            new_node.uid = old_node.uid
        else:
            new_node.uid = uuid4().hex
            yield new_node
    # create new uuids for any new node we left out earlier, this happens
    # if one or more nodes are simply added.
    for new_node in set(new_nodes) - seen:
        new_node.uid = uuid4().hex
        yield new_node


def get_ratio(old, new):
    """Return a "similiarity ratio" (in percent) representing the similarity
    between the two strings where 0 is equal and anything above less than equal.
    """
    if not all([old, new]):
        return VERSIONING_RATIO
    return levenshtein_distance(old, new) / (len(old) / 100.0)


def levenshtein_distance(a, b):
    """Return the Levenshtein edit distance between two strings *a* and *b*."""
    if a == b:
        return 0
    if len(a) < len(b):
        a, b = b, a
    if not a:
        return len(b)
    previous_row = xrange(len(b) + 1)
    for i, column1 in enumerate(a):
        current_row = [i + 1]
        for j, column2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (column1 != column2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

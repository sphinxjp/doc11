# -*- coding: utf-8 -*-
"""
    test_websupport
    ~~~~~~~~~~~~~~~

    Test the Web Support Package

    :copyright: Copyright 2007-2010 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import os
from StringIO import StringIO

from sphinx.websupport import WebSupport
from sphinx.websupport.errors import *

try:
    from functools import wraps
except ImportError:
    # functools is new in 2.4
    wraps = lambda f: (lambda w: w)

from util import *


def teardown_module():
    (test_root / 'websupport').rmtree(True)


def with_support(*args, **kwargs):
    """Make a WebSupport object and pass it the test."""
    settings = {'outdir': os.path.join(test_root, 'websupport'),
                'status': StringIO(),
                'warning': StringIO()}
    settings.update(kwargs)

    def generator(func):
        @wraps(func)
        def new_func(*args2, **kwargs2):
            support = WebSupport(**settings)
            func(support, *args2, **kwargs2)
        return new_func
    return generator


@with_support()
def test_no_srcdir(support):
    """Make sure the correct exception is raised if srcdir is not given."""
    raises(SrcdirNotSpecifiedError, support.build)

@with_support(srcdir=test_root)
def test_build(support):
    support.build()

@with_support()
def test_get_document(support):
    raises(DocumentNotFoundError, support.get_document, 'nonexisting')
    
    contents = support.get_document('contents')
    assert contents['title'] and contents['body'] \
        and contents['sidebar'] and contents['relbar']

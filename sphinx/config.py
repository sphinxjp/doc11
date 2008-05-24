# -*- coding: utf-8 -*-
"""
    sphinx.config
    ~~~~~~~~~~~~~

    Build configuration file handling.

    :copyright: 2008 by Georg Brandl.
    :license: BSD license.
"""

import os
from os import path


class Config(object):
    """Configuration file abstraction."""

    # the values are: (default, needs fresh doctrees if changed)

    # If you add a value here, don't forget to include it in the
    # quickstart.py file template as well as in the docs!

    config_values = dict(
        # general substitutions
        project = ('Python', True),
        copyright = ('', False),
        version = ('', True),
        release = ('', True),
        today = ('', True),
        today_fmt = ('%B %d, %Y', True),

        # extensibility
        templates_path = ([], False),
        extensions = ([], True),

        # general reading options
        master_doc = ('contents', True),
        source_suffix = ('.rst', True),
        unused_docs = ([], True),
        exclude_dirs = ([], True),
        exclude_trees = ([], True),
        add_function_parentheses = (True, True),
        add_module_names = (True, True),
        show_authors = (False, True),
        pygments_style = ('sphinx', False),
        template_bridge = (None, False),

        # HTML options
        html_title = (lambda self: '%s v%s documentation' %
                                   (self.project, self.release),
                      False),
        html_short_title = (lambda self: self.html_title, False),
        html_style = ('default.css', False),
        html_logo = (None, False),
        html_static_path = ([], False),
        html_last_updated_fmt = ('%b %d, %Y', False),
        html_use_smartypants = (True, False),
        html_translator_class = (None, False),
        html_sidebars = ({}, False),
        html_additional_pages = ({}, False),
        html_use_modindex = (True, False),
        html_use_index = (True, False),
        html_copy_source = (True, False),
        html_use_opensearch = ('', False),
        html_file_suffix = (None, False),
        html_show_sphinx = (True, False),

        # HTML help only options
        htmlhelp_basename = ('pydoc', False),

        # LaTeX options
        latex_paper_size = ('letter', False),
        latex_font_size = ('10pt', False),
        latex_documents = ([], False),
        latex_logo = (None, False),
        latex_preamble = ('', False),
        latex_appendices = ([], False),
        latex_use_parts = (False, False),
        latex_use_modindex = (True, False),
    )

    def __init__(self, dirname, filename):
        self.valuenames = set(self.config_values.keys())
        config = {'__file__': path.join(dirname, filename)}
        olddir = os.getcwd()
        try:
            os.chdir(dirname)
            execfile(config['__file__'], config)
        finally:
            os.chdir(olddir)
        for name in config:
            if name in self.valuenames:
                self.__dict__[name] = config[name]
        self.setup = config.get('setup', None)

    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(name)
        if name not in self.valuenames:
            raise AttributeError('No such config value: %s' % name)
        default = self.config_values[name][0]
        if callable(default):
            return default(self)
        return default

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        setattr(self, name, value)

    def __delitem__(self, name):
        delattr(self, name)

    def __contains__(self, name):
        return name in self.valuenames

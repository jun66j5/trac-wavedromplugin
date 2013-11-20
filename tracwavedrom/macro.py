# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Jun Omae
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

import re
from genshi.builder import tag

from trac.core import implements
from trac.web.api import IRequestFilter
from trac.web.chrome import ITemplateProvider, add_script
from trac.wiki.macros import WikiMacroBase


class WaveDromMacro(WikiMacroBase):

    implements(IRequestFilter, ITemplateProvider)

    # IRequestFilter methods

    def pre_process_request(self, req, handler):
        return handler

    def post_process_request(self, req, template, data, content_type):
        if template:
            add_script(req, 'wavedrom/skins/default.js')
            add_script(req, 'wavedrom/WaveDrom.js')
            add_script(req, 'wavedrom/load.js')
        return template, data, content_type

    # ITemplateProvider methods

    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename
        return [('wavedrom', resource_filename(__name__, 'htdocs'))]

    def get_templates_dirs(self):
        return ()

    # IWikiMacroProvider

    def get_macro_description(self, name):
        return """\
!WaveDrom processor provides to render wavedrom drawings within a Trac
wiki page.

Example:
{{{
{{{
#!WaveDrom
{ "signal" : [{ "name": "Alfa", "wave": "01.zx=ud.23.45" }] }
}}}
}}}
"""

    _quote = dict(zip('&<>', map(lambda v: r'\x%02x' % ord(v), '&<>')))
    _quote_re = re.compile('[&<>]')

    def expand_macro(self, formatter, name, content):
        if content and content.strip():
            def repl(match):
                return self._quote[match.group(0)]
            return tag.script(self._quote_re.sub(repl, content),
                              type='WaveDrom')

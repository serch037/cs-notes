#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sergio Ugalde Marcano'
SITENAME = 'Computer Science Notes'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
STATIC_PATHS = ['images']
TYPOGRIFY = True
MD_EXTENSIONS =  ['toc','fenced_code', 'codehilite(css_class=highlight)','extra','tables','smartypants', 'pipe_tables']
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}
HIDE_DATE = True
THEME = "/usr/lib/python3.4/site-packages/pelican/themes/pelican-bootstrap3/"

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Robillard'
SITENAME = u'LV2'
SITELOGO = 'images/logo.svg'
SITELOGO_WIDTH = '75'
SITELOGO_HEIGHT = '48'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

THEME = 'themes/lv2'

FAVICON = 'images/favicon.png'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = ()

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = ()

MENUITEMS = [('Developing', '/pages/developing.html'),
             ('Git', 'http://lv2plug.in/git')]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_PAGINATION = False

GITHUB_URL = 'http://github.com/drobilla/lv2'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_SERIES_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False

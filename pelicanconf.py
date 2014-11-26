#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'David Robillard'
SITENAME = u'LV2'
SITELOGO = 'images/logo.svg'
SITELOGO_WIDTH = '75'
SITELOGO_HEIGHT = '48'
SITEURL = 'http://lv2plug.in'

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

PLUGIN_PATHS = ["extra_plugins"]
PLUGIN_PATH = "extra_plugins"
PLUGINS = ["gallery"]

GALLERY_FOLDER = "galleries"
GALLERY_SRC_PATH = "%s%s" % (PATH, "/images/screenshots")
GALLERY_OUTPUT_PATH = "%s%s" % ("output/", GALLERY_FOLDER)
GALLERY_REGENERATE_EXISTING = True
GALLERY_PRESETS = [
    {"name": "thumb",
     "actions": [{"type": "fit", "height": 100, "width": 100, "from": (0.5, 0.5)}]},
    {"name": "slider",
     "actions" : []},
    {"name": "large",
     "actions": [{"type": "resize", "height": 640, "width": 850, "from": (0.5, 0.5)}]},
    {"name": "thumb_greyscale",
     "actions": [{"type": "fit", "height": 100, "width": 100, "from": (0.5, 0.5)},
                 {"type": "greyscale"} ]}]

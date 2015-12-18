#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rok Roškar'
SITENAME = u'Data Blog'
SITEURL = 'http://rokroskar.github.io'
DISQUS_SITENAME = 'rokdatablog'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = ('#'),)

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {'status': 'draft', }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/Users/rok/pelican-themes/pelican-bootstrap3"

GOOGLE_ANALYTICS = 'UA-71475726-1'

TWITTER_USERNAME = 'rokstars'

STATIC_PATHS = ['images']

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False

SOCIAL = (('twitter', 'http://twitter.com/rokstars'),
          ('github', 'http://github.com/rokroskar'),)

CC_LICENSE = "CC-BY-NC"



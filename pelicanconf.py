#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = 'Miguel Hernandez'
SITENAME = "Miguel's Website"
# SITEURL = 'https://miguelhx.github.io/personal-website'
SITEURL = 'https://www.miguelhx.com'
# SITEURL = 'http://localhost:8000'
SITETITLE = "Miguel Hernandez"
SITESUBTITLE = "Software Engineer"
SITEDESCRIPTION = "Personal Website and Blog by Miguel Hernandez"
SITELOGO = SITEURL + "/images/miguel-pic.png"
# FAVICON = SITEURL + "/images/favicon.ico"
PYGMENTS_STYLE = "monokai"
BROWSER_COLOR = '#333'

ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

STATIC_PATHS = ['images', 'extra', 'extra/CNAME', 'static']

PAGE_PATHS = ['pages']

ARTICLE_PATHS = ['articles']


EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': 'CNAME'},
}

# CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

THEME = 'MinimalXY'

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
# MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2018
MINIMALXY_CURRENT_YEAR = datetime.datetime.now().year

# Theme settings
DISPLAY_PAGES_ON_MENU=True
DISPLAY_CATEGORIES_ON_MENU=False

# Author
AUTHOR_INTRO = 'Miguel Hernandez | Software Engineer'
AUTHOR_DESCRIPTION = 'See about me page for details :)'
AUTHOR_AVATAR = SITELOGO
AUTHOR_WEB = SITEURL

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('resume/cv', 'http://python.org/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/miguel-hernandez-535b05102/'),
          ('github', 'https://github.com/miguelhx'),
          ('twitter', 'https://twitter.com/miguel_hx'),)

MENUITEMS = (('Archives', SITEURL + '/archives.html'),
              ('Categories', SITEURL + '/categories.html'),
              ('Tags', SITEURL + '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

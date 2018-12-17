#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Miguel Hernandez'
SITENAME = ""
SITEURL = 'https://miguelhx.github.io/personal-website'
# SITEURL = 'http://localhost:8000'
SITETITLE = "Miguel Hernandez"
SITESUBTITLE = "Software Engineer"
SITEDESCRIPTION = "Personal Website and Blog by Miguel Hernandez"
SITELOGO = SITEURL + "/images/miguel-pic.jpg"
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

STATIC_PATHS = ['images']

PAGE_PATHS = ['pages']

ARTICLE_PATHS = ['articles']


# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'static/custom.css'},
# }
# CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True

THEME = 'Flex'

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
SOCIAL = (('linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
          ('github', 'https://github.com/miguelhx'),
          ('twitter', 'https://twitter.com/miguel_hx'),)

MENUITEMS = (('Archives', '/archives.html'),
              ('Categories', '/categories.html'),
              ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
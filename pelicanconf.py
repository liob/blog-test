# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hinrich B. Winther'
SITENAME = u'Blog'
SITEURL = ''
THEME = 'theme/pelican-bootstrap3'
CUSTOM_CSS = 'css/style.css'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Projects', '{filename}/pages/about.html'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

#MENUITEMS = (('Projects', '/pages/about.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

SOCIAL = (
    ('EMail', 'mailto:hbwinther@metalabs.de'),
    ('Twitter', 'http://twitter.com/hbwinther'),
    ('Github', 'http://github.com/liob/'),
    ('BitBucket', 'https://bitbucket.org/hbwinther'),
    ('Facebook', 'https://www.facebook.com/hbwinther'),
    ('Linkedin', 'http://www.linkedin.com/in/hbwinther'),
)

STATIC_PATHS = ['images', 'css/style.css']

# theme specific:
DISPLAY_CATEGORIES_ON_MENU = False
#ABOUT_ME = 'Hi'
#AVATAR = 'images/hbwinther.jpg'
#HIDE_SITENAME = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

PLUGIN_PATH = 'plugins'
PLUGINS = ['pandoc_reader', 'better_figures_and_images']
RESPONSIVE_IMAGES = True
PANDOC_ARGS = [ '--bibliography=bibliography.bib', ]

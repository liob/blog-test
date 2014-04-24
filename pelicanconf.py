# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hinrich B. Winther'
SITENAME = u'Proven Inconclusive'
SITEURL = 'http://proven-inconclusive.com'
THEME = 'theme/pelican-bootstrap3'
CUSTOM_CSS = 'css/style.css'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Projects', '{filename}/pages/about.html'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

#MENUITEMS = (('Projects', '/pages/about.html'),)

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

SOCIAL = (
    ('EMail', 'mailto:hbwinther@metalabs.de'),
    ('Twitter', 'http://twitter.com/hbwinther'),
    ('Github', 'http://github.com/liob/'),
    ('BitBucket', 'https://bitbucket.org/hbwinther'),
    ('Facebook', 'https://www.facebook.com/hbwinther'),
    ('Linkedin', 'http://www.linkedin.com/in/hbwinther'),
    ('RSS', 'http://proven-inconclusive.com/feeds/all.atom.xml'),
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
PANDOC_ARGS = [ 
    '--bibliography=./bibliography.bib',
    '--csl=./jmir.csl',
    '--mathml' ]

ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
#PAGE_URL = '{slug}.html'
#PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'

PIWIK_URL = 'http://tools.metalabs.de/piwik/piwik.php'
PIWIK_SITE_ID = '3'

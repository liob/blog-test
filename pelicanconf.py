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
TAG_FEED_ATOM = 'feeds/tag.%s.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category.%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Projects', '{filename}/pages/about.html'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS =  (
    ('R-bloggers', 'http://www.r-bloggers.com'),
    ('Christian Hundt', 'http://abstractnonsense.de'),
    ('Randy Olson', 'http://www.randalolson.com/blog/'),
)


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
#ABOUT_ME = 'Simplicity is the ultimate sophistication'
#AVATAR = 'images/hbwinther.jpg'
#HIDE_SITENAME = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
SHOW_ARTICLE_AUTHOR = True

PLUGIN_PATH = 'plugins'
PLUGINS = ['pandoc_reader']
RESPONSIVE_IMAGES = True
PANDOC_ARGS = [ 
    '--bibliography=./bibliography.bib',
    '--csl=./jmir.csl',
    '--mathml' ]

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
#PAGE_URL = '{slug}.html'
#PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'

TWITTER_USERNAME = 'hbwinther'
TWITTER_WIDGET_ID = 481049923681406977

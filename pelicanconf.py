#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'יודה רונן'
SITENAME = 'הוצאת פושישית'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'he'

SUMMARY_MAX_LENGTH = None

FEED_ALL_ATOM = 'abonrilato/atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

MENUITEMS = [('<i class="icon-home ikono"></i>עמוד ראשי', '/'),
             ('<i class="icon-bug ikono"></i>אודות', '/pri'),
             ('<i class="icon-book ikono"></i>קטלוג', '/katalogo'),
             ('<i class="icon-rss ikono"></i>חדשות', '/novajxoj.html'),
             ('<i class="icon-megaphone ikono"></i>איך להשתתף?',
              '/partopreni')]

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'novajxoj-{date:%Y}-{date:%m}-{date:%d}'
ARTICLE_SAVE_AS = 'novajxoj-{date:%Y}-{date:%m}-{date:%d}/index.html'

THEME = "themes/xpr"

DIRECT_TEMPLATES = ('index', 'novajxoj')

DEFAULT_DATE_FORMAT = '%-d ב%B, %Y'
LOCALE = ('he_IL.utf8')
FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)')

PAGE_PATHS = ['pagxoj']
STATIC_PATHS = ['senmova']
ARTICLE_EXCLUDES = ['pagxoj']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-page-hierarchy']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

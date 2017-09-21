#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ramón Darío Iglesias'
SITENAME = u'Ramón Darío Iglesias'
SITEURL = 'http://ramondario.com'

NOTEBOOK_DIR = 'notebooks'
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

FAVICON_URL = '/images/favicon.ico'


# article paths
INDEX_SAVE_AS = 'notes/index.html'
INDEX_URL = 'notes/'

# publications
PUBLICATIONS_SRC = 'bib/iglesias.bib'


PATH = 'content'
STATIC_PATHS = ['images','cv']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal','liquid_tags.youtube','render_math', 
           'pelican-bibtex']

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

THEME = 'pure-single'

#liquid tags says this is necessary
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
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
SOCIAL = (('github', 'https://github.com/huevosabio'),
          ('linkedin','https://www.linkedin.com/in/ram%C3%B3n-iglesias-00620227/'),
          ('envelope','mailto:rdit@stanford.edu')
          )

# navigation
MENUITEMS = [
	#('Projects','/projects/'),
	('Notes','/notes/'),
	('Publications','/publications.html'),
	('CV', '/cv/ramon_iglesias_cv.pdf')
	]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
COVER_IMG_URL = '/images/sunset.jpg'
PROFILE_IMG_URL = '/images/closeup.jpg'
#TAGLINE = 'Notes, thoughts, snippets, and more.'
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime
# need to update the copywright stuff
AUTHOR = 'Benjamin'
SITENAME = 'Bencraver.com'
SITEURL = "https://bensgithubaccount.github.io"
SITENAME = "bencraver.com" # Tab title
SITETITLE = "Welcome!"
SITESUBTITLE = ""
SITEDESCRIPTION = "bencraver.com - a personal website"
COPYRIGHT_NAME = 'Benjamin Craver'
COPYRIGHT_YEAR = datetime.date.today().year
SITELOGO = 'blank_pic.jpg'

PATH = 'content'
TIMEZONE = "America/New_York"
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', '/'),)

INDEX_SAVE_AS = 'posts/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

# Social widget
# SOCIAL = (('I don\'t use social media', '#'), )
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['files']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'Flex'
MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Tags", "/tags.html"),
    ("Posts", "/posts"),
    # ("Categories", "/categories.html"),
)

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

DISPLAY_PAGES_ON_MENU = True #The menu on the right/top of the screen
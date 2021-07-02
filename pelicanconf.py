AUTHOR = 'Pimoroni Ltd.'
SITENAME = "32Blit Tutorials"
SITESUBTITLE = 'Lua and C++ Tutorials for the 32Blit handheld.'
SITEURL = 'http://tutorials.32blit.com'
TIMEZONE = "Europe/London"


THEME = 'Flex'
THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
PYGMENTS_STYLE = 'vs'
PYGMENTS_STYLE_DARK = 'monokai'
MAIN_MENU = True

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = 'http://github.com/32blit/'
DISQUS_SITENAME = "blog-32blittutorials"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

LINKS = (('Pimoroni', 'https://shop.pimoroni.com'),
         ('32Blit', "https://32bilt.com"),)

SOCIAL = (('twitter', 'http://twitter.com/32blit'),
          ('github', 'http://github.com/32blit'),)

MENUITEMS = (
    ("Lua Tutorials", "/category/lua.html"),
    ("C++ Tutorials", "/category/c++.html"),
    ("Case Studies", "/category/case-studies.html"),
)

# global metadata to all the contents
DEFAULT_METADATA = {'32blit': 'tutorial'}

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = []

ARTICLE_PATHS = [
    'case-studies',
    'lua',
    'c++'
]

USE_FOLDER_AS_CATEGORY = True

# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# there is no other HTML content
READERS = {'html': None}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

MARKDOWN = {
    'tab_length': 2, # Fix nested lists with only two spaces
    'extension_configs': {
        'markdown.extensions.toc': {}, # Add "id" attributes to header tags
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {}, # Does... something... maybe
    }
}

# 
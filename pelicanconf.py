AUTHOR = 'חוויות מייקרס'
SITENAME = 'חוויות מייקרס'
SITEURL = ''

PATH = 'content'
THEME = 'themes/makers'
TIMEZONE = 'Asia/Jerusalem'
DEFAULT_LANG = 'he'

PLUGINS = ['i18n_subsites']

_SUBSITE_COMMON = {
    'INDEX_SAVE_AS': 'blog/index.html',
    'INDEX_URL': 'blog/',
    'DIRECT_TEMPLATES': ['index'],
}

I18N_SUBSITES = {
    'en': {
        **_SUBSITE_COMMON,
        'SITENAME': 'Havayot Makers',
        'MENUITEMS': [
            ('Activities', '/en/activities/'),
            ('Past Activities', '/en/blog/'),
            ('Contact', '/en/contact/'),
        ],
    },
    'ar': {
        **_SUBSITE_COMMON,
        'SITENAME': 'حوايوت مايكرز',
        'MENUITEMS': [
            ('الأنشطة', '/ar/activities/'),
            ('الأنشطة السابقة', '/ar/blog/'),
            ('اتصل بنا', '/ar/contact/'),
        ],
    },
    'ru': {
        **_SUBSITE_COMMON,
        'SITENAME': 'Хавайот Мейкерс',
        'MENUITEMS': [
            ('Занятия', '/ru/activities/'),
            ('Прошлые занятия', '/ru/blog/'),
            ('Контакты', '/ru/contact/'),
        ],
    },
}

# Feeds — disabled for MVP
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Content paths
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['images']

# Clean URLs
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

# Move article index to /blog/ so a page can own /
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'

# Navigation — Hebrew main site
MENUITEMS = [
    ('פעילויות', '/activities/'),
    ('פעילויות שעברו', '/blog/'),
    ('צור קשר', '/contact/'),
]

SPONSOR_URL = 'https://www.havayot.org.il/%D7%A1%D7%A4%D7%A8%D7%99%D7%95%D7%AA/'

# Disable auto-generated taxonomy pages
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

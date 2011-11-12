# -*- encoding: utf-8 -*-

import os
__path__ = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ABSOLUTE_URL_PREFIX = '/'

ADMINS = (
    # ('Ricardo Dani', 'ricardo.dani@gmail.com'),
)

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'partenon'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = 'p4ssw0rd!'         # Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

MANAGERS = ADMINS

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-BR'

SITE_ID = 1

USE_I18N = True

ADMIN_MEDIA_ROOT = os.path.join(__path__, 'admin_media')
MEDIA_ROOT = os.path.join(__path__, 'site_media')
RAIZ = __path__

MEDIA_URL = '/site_media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = '&q!!_c-&bse)0a+!jn#8xpya9s45ja066t(*jc2pclqk+0g%fd'

TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.load_template_source',
  'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'partenon.urls'

TEMPLATE_DIRS = (
    os.path.join(__path__, 'templates'),
)

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',

  'django.contrib.admin',
  
  'tinymce',
  'photologue',
  'treemenus',
  
  'paginas',
  'videos',
  'pessoas',
  'muralderecados',
  'noticias',
  
  'teste',
)

TINYMCE_DEFAULT_CONFIG = {
    'skin': "o2k7",
    'theme': "advanced",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'plugins': "spellchecker,directionality,paste,searchreplace",
    'dialog_type': "modal",
    'object_resizing': True,
    'cleanup_on_startup': True,
    'forced_root_block': "p",
    'remove_trailing_nbsp': True,
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "none",
    'theme_advanced_buttons1': "formatselect,styleselect,bold,italic,underline,bullist,numlist,undo,redo,link,unlink,image,code,template,visualchars,fullscreen,pasteword,media,search,replace,charmap",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'theme_advanced_path': False,
    'theme_advanced_blockformats': "p,h2,h3,h4,div,code,pre",
    'theme_advanced_styles': "[all] clearfix=clearfix;[p] summary=summary;[div] code=code;[img] img_left=img_left;[img] img_left_nospacetop=img_left_nospacetop;[img] img_right=img_right;[img] img_right_nospacetop=img_right_nospacetop;[img] img_block=img_block;[img] img_block_nospacetop=img_block_nospacetop;[div] column span-2=column span-2;[div] column span-4=column span-4;[div] column span-8=column span-8",
    'width': '700',
    'height': '200',
    'plugins': "advimage,advlink,fullscreen,visualchars,paste,media,template,searchreplace",
    'advimage_styles': "LinksbÃ¼ndig neben Text=img_left;RechtsbÃ¼ndig neben Text=img_right;Eigener Block=img_block",
    'advlink_styles': "internal (sehmaschine.net)=internal;external (link to an external site)=external",
    'advimage_update_dimensions_onchange': True,
    'file_browser_callback': "CustomFileBrowser",
    'relative_urls': False,
    'valid_elements ': "" +
    "-p," + 
    "a[href|target=_blank|class]," +
    "-strong/-b," +
    "-em/-i," +
    "-u," + 
    "-ol," + 
    "-ul," + 
    "-li," + 
    "br," + 
    "img[class|src|alt=|width|height]," + 
    "-h2,-h3,-h4," + 
    "-pre," +
    "-code," + 
    "-div",
    'extended_valid_elements': "" + 
    "a[name|class|href|target|title|onclick]," + 
    "img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name]," + 
    "br[clearfix]," + 
    "-p[class<clearfix?summary?code]," + 
    "h2[class<clearfix],h3[class<clearfix],h4[class<clearfix]," + 
    "ul[class<clearfix],ol[class<clearfix]," + 
    "div[class],"
}

UPLOAD_PATH = 'uploads'

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.core.context_processors.auth",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.request",
  'context_processors.portal',
  
)

try:
    from custom_settings import *
except:
    pass

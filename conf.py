import os

project = u'Thunderbird WebExtension APIs'
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store', 'overlay']
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Configure headers for non-stable versions
rtd_version = os.environ.get('READTHEDOCS_VERSION')
versionwarning_default_message = 'This version of the documentation is for to the discontinued Thunderbird ' + rtd_version + '. The API documentation for the current release of Thunderbird can be found <a href="/">here</a>.'
versionwarning_body_selector = 'div[itemprop="articleBody"]'
versionwarning_messages = {
    'latest': 'This documentation is for pre-release versions of Thunderbird. The API documentation for the current release of Thunderbird can be found <a href="/">here</a>.',
}

if rtd_version == 'latest':
    versionwarning_admonition_type = 'tip'
    versionwarning_banner_title = 'Tip'

versionwarning_body_selector = 'div[itemprop="articleBody"]'

extensions = [
     # ... other extensions here
     'versionwarning.extension',
]

def setup(app):
   #app.add_javascript("custom.js")
   app.add_stylesheet('theme_overrides.css')

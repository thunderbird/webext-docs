import sys, os

# local extension folder
sys.path.append(os.path.abspath('_extensions'))

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

# Configure headers
versionwarning_body_selector = 'div[itemprop="articleBody"]'

versionwarning_latest_type = 'tip'
versionwarning_latest_title = 'Note'   
versionwarning_latest_message = 'This is the API documentation for pre-release versions of Thunderbird. See version {newest} for the current ESR of Thunderbird.'

versionwarning_current_type = 'tip'
versionwarning_current_title = 'Note'   
versionwarning_current_message = 'This is the API documentation for Thunderbird {this}.'

versionwarning_older_type = 'warning'
versionwarning_older_title = 'Warning'   
versionwarning_older_message = 'This is the API documentation for Thunderbird {this}. See version {newest} for the current ESR of Thunderbird.'


extensions = [
    # ... other extensions here
    'versionwarning.extension',
    #'sphinx_toolbox.confval',
]

def setup(app):
   #app.add_javascript("custom.js")
   app.add_stylesheet('theme_overrides.css')

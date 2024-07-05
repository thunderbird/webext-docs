import sys, os

# local extension folder
sys.path.append(os.path.abspath('_extensions'))

project = u'WebExtension Documentation for Thunderbird Beta<br><br>Manifest V3'
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store', 'overlay']

extensions = [
    # ... other extensions here
    'versionwarning.extension',
    'apiheader',
    'apimember',
    'apisectionannotationhack',
    'sphinx_rtd_theme',
]

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False,
    'style_external_links': True,
    'prev_next_buttons_location': "None"
}

html_context = {
  'display_github': False
}

html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Configure headers
versionwarning_body_selector = 'div[itemprop="articleBody"] h1'

def setup(app):
   app.add_js_file("custom.js")
   app.add_css_file('theme_overrides.css')

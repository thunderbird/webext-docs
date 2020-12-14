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


versionwarning_messages = {
    'latest': 'This documentation is for pre-release versions of Thunderbird. See the “stable” version of this documentation for the current ESR release of Thunderbird.',
}
versionwarning_default_message = "This documentation is for Thunderbird READTHEDOCS_VERSION, which is no longer supported. See the “stable” version for the current ESR release of Thunderbird."
versionwarning_body_selector = 'div[itemprop="articleBody"]'

extensions = [
     # ... other extensions here
     'versionwarning.extension',
]

def setup(app):
   #app.add_javascript("custom.js")
   app.add_stylesheet("theme_overrides.css")

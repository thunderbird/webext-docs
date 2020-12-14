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

def setup(app):
   #app.add_javascript("custom.js")
   app.add_stylesheet("theme_overrides.css")

versionwarning_default_message = "This page is part of the API documentation of the no longer supported Thunderbird READTHEDOCS_VERSION. The current version of this documentation is for Thunderbird {newest}."

versionwarning_messages = {
    'latest': 'This is a custom message only for version "latest" of this documentation.',
}

extensions = [
     # ... other extensions here
     'versionwarning.extension',
]


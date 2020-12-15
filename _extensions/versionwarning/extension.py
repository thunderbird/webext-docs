# -*- coding: utf-8 -*-
import os
import sphinx
from versionwarning import version
from .signals import generate_versionwarning_data_json


def setup(app):
    default_message = 'You are not reading the most up to date version of this documentation. {newest} is the newest version.'

    banner_html = '''
    <div id="{id_div}" class="admonition {admonition_type}">
        <p class="first admonition-title">{banner_title}</p>
            <p class="last">
                {message}
            </p>
    </div>'''

    app.add_config_value('versionwarning_message_placeholder', 'newest', 'html')
    app.add_config_value('versionwarning_admonition_type', 'warning', 'html')
    app.add_config_value('versionwarning_older_message', default_message, 'html')
    app.add_config_value('versionwarning_current_message', '', 'html')
    app.add_config_value('versionwarning_latest_message', '', 'html')
    app.add_config_value('versionwarning_messages', {}, 'html')

    app.add_config_value('versionwarning_api_url', 'https://readthedocs.org/api/v2/', 'html')
    app.add_config_value('versionwarning_banner_html', banner_html, 'html')
    app.add_config_value('versionwarning_banner_id_div', 'version-warning-banner', 'html')
    app.add_config_value('versionwarning_banner_title', 'Warning', 'html')
    app.add_config_value('versionwarning_body_selector', 'div.body', 'html')
    app.add_config_value('versionwarning_project_slug', os.environ.get('READTHEDOCS_PROJECT', None), 'html')
    app.add_config_value('versionwarning_project_version', os.environ.get('READTHEDOCS_VERSION', None), 'html')

    if sphinx.version_info >= (1, 8):
        # ``config-initied`` requires Sphinx >= 1.8
        app.connect('config-inited', generate_versionwarning_data_json)

        # ``add_js_file`` requires Sphinx >= 1.8
        app.add_js_file('js/versionwarning.js')
    else:
        app.connect('builder-inited', generate_versionwarning_data_json)
        app.add_javascript('js/versionwarning.js')

    return {
        'version': version,
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

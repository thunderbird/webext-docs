# -*- coding: utf-8 -*-

import json
import os


STATIC_PATH = os.path.join(os.path.dirname(__file__), '_static')
JSON_DATA_FILENAME = 'versionwarning-data.json'


def generate_versionwarning_data_json(app, config=None, **kwargs):
    """
    Generate the ``versionwarning-data.json`` file.

    This file is included in the output and read by the AJAX request when
    accessing to the documentation and used to compare the live versions with
    the curent one.

    Besides, this file contains meta data about the project, the API to use and
    the banner itself.
    """

    # In Sphinx >= 1.8 we use ``config-initied`` signal which comes with the
    # ``config`` object and in Sphinx < 1.8 we use ``builder-initied`` signal
    # that doesn't have the ``config`` object and we take it from the ``app``
    config = config or kwargs.pop('config', None)
    if config is None:
        config = app.config

    if config.versionwarning_project_version in config.versionwarning_messages:
        custom = True
        message = config.versionwarning_messages.get(config.versionwarning_project_version)
    else:
        custom = False
        message = config.versionwarning_default_message

    banner_html = config.versionwarning_banner_html.format(
        id_div=config.versionwarning_banner_id_div,
        banner_title=config.versionwarning_banner_title,
        message=message.format(
            **{config.versionwarning_message_placeholder: '<a href="#"></a>'},
        ),
        admonition_type=config.versionwarning_admonition_type,
    )

    data = json.dumps({
        'meta': {
            'api_url': config.versionwarning_api_url,
        },
        'banner': {
            'html': banner_html,
            'id_div': config.versionwarning_banner_id_div,
            'body_selector': config.versionwarning_body_selector,
            'custom': custom,
        },
        'project': {
            'slug': config.versionwarning_project_slug,
        },
        'version': {
            'slug': config.versionwarning_project_version,
        },
    }, indent=4)

    data_path = os.path.join(STATIC_PATH, 'data')
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    with open(os.path.join(data_path, JSON_DATA_FILENAME), 'w') as f:
        f.write(data)

    # Add the path where ``versionwarning-data.json`` file and
    # ``versionwarning.js`` are saved
    config.html_static_path.append(STATIC_PATH)

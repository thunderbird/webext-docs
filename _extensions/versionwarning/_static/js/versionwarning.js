function injectVersionWarningBanner(running_version_slug, config, versions) {
    const running_version = versions.find(e => e.slug == running_version_slug);
    const highest_version = getHighestVersion(
        versions.filter(e => e.manifest_version == running_version.manifest_version)
    );

    console.debug("injectVersionWarningBanner");
    var current_url = window.location.pathname;
    var isIndex = current_url.endsWith(running_version.slug + "/") || current_url.endsWith(running_version.slug + "/index.html");

    var others = [];
    $.each(versions, function (i, version) {
        if (version.slug != running_version.slug && version.slug != highest_version.slug) {
            others.push("<a href='" + current_url.replace(running_version.slug, version.slug) + "'>" + version.title + "</a>");
        }
    });
    let other = others.pop();
    let first = others.join(", ");
    if (first) {
        other = first + " & " + other;
    }

    // Strings
    const versionwarning_latest_type = 'warning'
    const versionwarning_latest_title = 'Warning'
    const versionwarning_latest_message = 'This is the documentation for Thunderbird {this}. See version {newest} for the current ESR of Thunderbird.'
    
    const versionwarning_current_type = 'note'
    const versionwarning_current_title = 'Note'
    const versionwarning_current_message = 'This is the documentation for Thunderbird ESR {this}. Other available versions are: {other}'
    
    const versionwarning_older_type = 'warning'
    const versionwarning_older_title = 'Warning'
    const versionwarning_older_message = 'This is an outdated documentation for Thunderbird {this}. See version {newest} for the current ESR of Thunderbird.'
    

    let msg = versionwarning_older_message;
    let title = versionwarning_older_title;
    let type = versionwarning_older_type
    
    if (running_version.slug.startsWith("latest") || running_version.slug.startsWith("beta")) {
        msg = versionwarning_latest_message;
        title = versionwarning_latest_title;
        type = versionwarning_latest_type
    } else if (running_version.slug == "stable" || running_version.slug == highest_version.slug) {
        msg = isIndex ? versionwarning_current_message : "";
        title = versionwarning_current_title;
        type = versionwarning_current_type
    }

    if (msg) {
        var warning = $(
            config.banner.html
                .replace("{message}", msg)
                .replace("{id_div}", config.banner.id_div)
                .replace("{banner_title}", title)
                .replace("{admonition_type}", type)
                .replace("{newest}", '<a href="' + current_url.replace(running_version.slug, highest_version.slug) + '">' + highest_version.title + '</a>')
                .replace("{this}", running_version.title)
                .replace("{other}", other)
        );

        var body = $(config.banner.body_selector);
        body.after(warning);
    }
}

function getHighestVersion(results) {
    console.debug("getHighestVersion");
    var highest_version;

    $.each(results, function (i, result) {
        if (isNaN(result.slug)) {
            // Skip versions that are not numbers
        }
        else if (!highest_version) {
            highest_version = result;
        }
        else if (result.version > highest_version.version) {
            highest_version = result;
        }
    });
    return highest_version;
}


function checkVersion(config) {
    console.debug("checkVersion");
    var running_version_slug = config.version.slug;
    console.debug("Running version slug: " + running_version_slug);

    var get_data = {
        project__slug: config.project.slug,
        active: "true"
        // format: "jsonp",
    };

    $.ajax({
        // Access of API is broken by CORS
        // https://readthedocs.org/api/v2/version/?project__slug=thunderbird-webextension-apis&active=true
        //url: config.meta.api_url + "version/",
        url: "https://webextension-api.thunderbird.net/en/latest/_static/versions.json",
        // Used when working locally for development
        // crossDomain: true,
        // xhrFields: {
        //     withCredentials: true,
        // },
        // dataType: "jsonp",
        data: get_data,
        success: function (versions) {
            // TODO: fetch more versions if there are more pages (next)
            console.debug({running_version_slug, config, versions})
            injectVersionWarningBanner(running_version_slug, config, versions["results"]);
        },
        error: function () {
            console.error("Error loading Read the Docs active versions.");
        }
    });
}

function init() {
    console.debug("init");
    // get the base_url so we can get the versionwarning-data.json from
    // any page.
    var base_url = $('script[src*=versionwarning]').attr('src');
    base_url = base_url.replace('versionwarning.js', '');
    $.ajax({
        url: base_url + "../../_static/data/versionwarning-data.json",
        success: function (config) {
            // Check if there is already a banner added statically
            console.debug({config})
            var banner = document.getElementById(config.banner.id_div);
            if (banner) {
                console.debug("There is already a banner added. No checking versions.")
            } else {
                checkVersion(config);
            }
        },
        error: function () {
            console.error("Error loading versionwarning-data.json");
        },
    })
}


$(document).ready(function () {
    init();
});

function injectVersionWarningBanner(running_version, highest_version, config, versions) {
    console.debug("injectVersionWarningBanner");
    var current_url = window.location.pathname;
    var isIndex = current_url.endsWith(running_version.slug + "/") || current_url.endsWith(running_version.slug + "/index.html");
    
    var others = [];
    $.each(versions, function (i, version) {
        if (version.slug != running_version.slug && version.slug != highest_version.slug) {
            let label = version.slug;
            if (label == "latest") {
                label = "Latest"
            }
            others.push("<a href='" + current_url.replace(running_version.slug, version.slug) + "'>" +label + "</a>");
        }
    });
    let other = others.pop();
    let first = others.join(", ");
    if (first) {
        other = first + " & " + other;
    }
    
    let msg = (config.banner.older_indexmessage && isIndex) 
                        ? config.banner.older_indexmessage
                        : config.banner.older_message;
    let title =  config.banner.older_title;
    let type = config.banner.older_type
    if (running_version.slug == "latest") {
        msg = (config.banner.latest_indexmessage && isIndex) 
                        ? config.banner.latest_indexmessage
                        : config.banner.latest_message;
        title =  config.banner.latest_title;
        type = config.banner.latest_type
    } else if (running_version.slug == highest_version.slug) {
        msg = (config.banner.current_indexmessage && isIndex) 
                        ? config.banner.current_indexmessage
                        : config.banner.current_message;
        title =  config.banner.current_title;
        type = config.banner.current_type
    } 
    
    if (msg) {
        var warning = $(
            config.banner.html
                .replace("{message}", msg)
                .replace("{id_div}", config.banner.id_div)
                .replace("{banner_title}", title)
                .replace("{admonition_type}", type)
                .replace("{newest}",  '<a href="' + current_url.replace(running_version.slug, highest_version.slug) + '">' + highest_version.slug + '</a>')
                .replace("{this}", running_version.slug)
                .replace("{other}", other)
        );

        var body = $(config.banner.body_selector);
        body.prepend(warning);
    }
}

function getHighestVersion(versions) {
    console.debug("getHighestVersion");
    var highest_version;

    $.each(versions, function (i, version) {
        if (isNaN(version.slug)) {
            // Skip versions that are not numbers
        }
        else if (!highest_version) {
            highest_version = version;
        }
        else if (parseInt(version.slug, 10) > parseInt(highest_version.slug, 10)) {
            highest_version = version;
        }
    });
    return highest_version;
}


function checkVersion(config) {
    console.debug("checkVersion");
    var running_version = config.version;
    console.debug("Running version: " + running_version.slug);

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
            highest_version = getHighestVersion(versions["results"]);
            console.debug("Highest version: " + highest_version.slug);
            if (running_version.slug == "stable") {
                running_version = highest_version
            }
            injectVersionWarningBanner(running_version, highest_version, config, versions["results"]);
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
        success: function(config) {
            // Check if there is already a banner added statically
            var banner = document.getElementById(config.banner.id_div);
            if (banner) {
                console.debug("There is already a banner added. No checking versions.")
            } else {
                checkVersion(config);
            }
        },
        error: function() {
            console.error("Error loading versionwarning-data.json");
        },
    })
}


$(document).ready(function () {
    init();
});

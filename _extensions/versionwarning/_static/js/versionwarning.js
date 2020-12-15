function injectVersionWarningBanner(running_version, highest_version, config) {
    console.debug("injectVersionWarningBanner");
    var version_url = window.location.pathname.replace(running_version.slug, highest_version.slug);
    
    let msg = config.banner.older_message;
    let title =  config.banner.older_title;
    let type = config.banner.older_type
    if (running_version == "latest") {
        msg = config.banner.latest_message;
        title =  config.banner.latest_title;
        type = config.banner.latest_type
    } else if (running_version == highest_version) {
        msg = config.banner.current_message;
        title =  config.banner.current_title;
        type = config.banner.current_type
    } 
    
    var warning = $(
        config.banner.html
            .replace("{message}", msg)
            .replace("{id_div}", config.banner.id_div)
            .replace("{banner_title}", title)
            .replace("{admonition_type}", type)
            .replace("{newest}",  '<a href="#"></a>')
            .replace("{this}", running_version)
    );

    warning
      .find("a")
      .attr("href", version_url)
      .text(highest_version.slug);

    var body = $(config.banner.body_selector);
    body.prepend(warning);
}

function getHighestVersion(versions) {
    console.debug("getHighestVersion");
    var highest_version;

    $.each(versions, function (i, version) {
        if ( isNaN(version)) {
            // Skip versions that are not numbers
        }
        else if (!highest_version) {
            highest_version = version;
        }
        else if (version > highest_version) {
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
        url: config.meta.api_url + "version/",
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
            if (true
//                semver.valid(semver.coerce(running_version.slug)) && semver.valid(semver.coerce(highest_version.slug)) &&
//                semver.lt(semver.coerce(running_version.slug), semver.coerce(highest_version.slug))
            ) {
                console.debug("Highest version: " + highest_version.slug);
                injectVersionWarningBanner(running_version, highest_version, config);
            }
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

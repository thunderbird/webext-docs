//const semver = require('semver');

function injectVersionWarningBanner(running_version, version, config) {
    console.debug("injectVersionWarningBanner");
    var version_url = window.location.pathname.replace(running_version.slug, version.slug);
    var warning = $(config.banner.html);
    console.debug("" + config.banner.html);
    console.debug("" + config.banner.html.replace("{message}", config.banner.current)));

    warning
      .find("a")
      .attr("href", version_url)
      .text(version.slug);

    var body = $(config.banner.body_selector);
    body.prepend(warning);
}

function getHighestVersion(versions) {
    console.debug("getHighestVersion");
    var highest_version;

    $.each(versions, function (i, version) {
/*        if (!semver.valid(semver.coerce(version.slug))) {
            // Skip versions that are not valid
        }
        else */ if (!highest_version) {
            highest_version = version;
        }
        else if (true
//            semver.valid(semver.coerce(version.slug)) && semver.valid(semver.coerce(highest_version.slug)) &&
//            semver.gt(semver.coerce(version.slug), semver.coerce(highest_version.slug))
        ) {
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
    console.log(base_url);
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

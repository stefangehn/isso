var requirejs = {
    paths: {
        "text": "/usr/share/nodejs/requirejs/text/text",
        "jade": "lib/requirejs-jade/jade",
        "libjs-jade": "/usr/lib/nodejs/jade/lib/jade",
        "libjs-jade-runtime": "/usr/lib/nodejs/jade/lib/runtime"
    },

    config: {
        text: {
            useXhr: function (url, protocol, hostname, port) {
                return true;
            }
        }
    }
};

({
    baseUrl: ".",
    mainConfigFile: 'config.js',
    paths: {
        "app/text/svg": "app/text/dummy",
        "app/text/css": "app/text/dummy"
    },

    name: "/usr/share/nodejs/almond/almond.js",
    include: ['count'],
    out: "count.min.js",
    wrap: true
})

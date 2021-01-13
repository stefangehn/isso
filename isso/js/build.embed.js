({
    baseUrl: ".",
    mainConfigFile: 'config.js',
    stubModules: ['text', 'jade'],

    name: "/usr/share/nodejs/almond/almond.js",
    include: ['embed'],
    out: "embed.min.js",

    optimizeAllPluginResources: true,
    wrap: true
})

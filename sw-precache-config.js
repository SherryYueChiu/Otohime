module.exports = {
    staticFileGlobs: [
        './allSticker/**/**.*',
        './**.{html,css,js,json}'
    ],
    runtimeCaching: [{
        urlPattern: /.*/,
        handler: 'fastest'
    }],
    swFile: 'service-worker.js'
};
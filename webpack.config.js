const HtmlWebPackPlugin = require("html-webpack-plugin");
var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');
module.exports = {
    entry: './src/scripts/index.tsx',
    module: {
        rules: [
            {
                test: /\.(ts|tsx)?$/,
                include: path.resolve(__dirname, 'src'),
                use: [
                    {
                        loader: 'babel-loader'
                    }
                ]
            },
        ]
    },
    watch: true,
    resolve: {
        extensions: ['.tsx', '.ts', '.js']
    },
    output: {
        path: path.resolve('./assets/webpack_bundles/'),
        filename: "[name]-[hash].js"
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ]

};
const path = require('path')
const webpack = require('webpack')
const HtmlWebPackPlugin = require("html-webpack-plugin")
const MiniCssExtractPlugin = require('mini-css-extral-plugin');
const OptimizeCSSAssetPlugin = require('optimize-css-assets-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const workboxPlugin = require('workbox-webpack-plugin');

module.exports = {
    entry: './src/client/index.js',
    mode: 'production',
    optimization:{
      minimizer:[new TerserPlugin({}), new OptimizeCSSAssetPlugin({})],  
    },
    module: {
        rules: [
            {
                test: '/\.js$/',
                exclude: /node_modules/,
                loader: "babel-loader"
            },
            {
                test:/\.js$/,
                use:[MiniCssExtractPlugin.loader, 'css-loader','sass-loader']
            }
        ]
    },
    plugins: [
        new HtmlWebPackPlugin({
            template: "./src/client/views/index.html",
            filename: "./index.html",
        }),
        new MiniCssExtractPlugin({filename:'[name].css'}),
        new workboxPlugin.GenerateSW({
            clientsClaim:true,
            skipWaiting:true
        }),
    ]
}

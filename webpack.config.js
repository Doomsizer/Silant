const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: "./Silant/src/index.jsx",
    output: {
        path: path.join(__dirname, "Silant/dist"),
        filename: "bundle.js",
        publicPath: "/static/"
    },
    resolve: {
        extensions: [".jsx", ".js"]
    },
    module: {
        rules: [
            {
                test: /\.jsx$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            ['@babel/preset-env', {
                                "targets": {
                                    "browsers": ["last 2 versions"]
                                }
                            }],
                            ['@babel/preset-react']
                        ]
                    }
                }
            },
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            },
            {
                test: /\.(png|jpe?g|gif|svg)$/i,
                type: 'asset/resource',
            },
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: "./Silant/src/index.html"
        })
    ],
    devServer: {
        static: {
            directory: path.join(__dirname, "Silant/dist"),
        },
        compress: true,
        port: 8080,
        historyApiFallback: true,
        hot: true
    }
};
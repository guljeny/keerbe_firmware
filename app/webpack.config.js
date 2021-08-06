const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

const isDev = process.env.NODE_ENV === 'development'

module.exports = {
  entry: './src/index.tsx',
  target: 'electron-main',
  mode: isDev ? 'development' : 'production',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: [
          'ts-loader',
        ],
        exclude: /node_modules/,
      },
      {
        test: /\.svg$/,
        loader: 'svg-inline-loader',
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              modules: {
                ...(isDev ? {
                  localIdentName: '[name]_[local]_[local]',
                } : {
                }),
              },
            },
          },
          'sass-loader',
        ],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, 'src/template.html'),
    }),
    new MiniCssExtractPlugin(),
  ],
  resolve: {
    extensions: [".ts", ".tsx", ".js"],
    alias: {
      "actions": path.resolve(__dirname, 'src/actions/'),
      "modules": path.resolve(__dirname, 'src/modules/'),
      "components": path.resolve(__dirname, 'src/components/'),
      "images": path.resolve(__dirname, 'src/images/'),
      "constants": path.resolve(__dirname, 'src/constants/'),
      "utils": path.resolve(__dirname, 'src/utils/'),
      "reducers": path.resolve(__dirname, 'src/reducers/'),
      "types": path.resolve(__dirname, 'src/types/'),
      "styles": path.resolve(__dirname, 'src/styles/'),
      "sagas": path.resolve(__dirname, 'src/sagas/'),
      "hooks": path.resolve(__dirname, 'src/hooks/'),
      "api": path.resolve(__dirname, 'src/api/'),
      "root": path.resolve(__dirname, 'src/'),
    },
  },
  devServer: {
    historyApiFallback: true,
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 8080,
  },
}

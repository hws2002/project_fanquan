const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: {
    dashboard:"/src/components/dashboard/index.js", // src/index.js which imports the App component
    event_hall:"/src/components/event_hall/index.js",
    messages_contacts:"/src/components/messages_contacts/index.js",
    forum:"/src/components/forum/index.js",
  },
  output: {
    path: path.resolve(__dirname, "static"),
    filename: "[name]/bundle.js",
  },
  resolve: {
    extensions: ['.js', '.jsx'],
    modules: ['node_modules', './src'],
    alias:{
      "dash_board-components" : path.resolve(__dirname,"./src/components/dashboard"),
      "event_hall-components" : path.resolve(__dirname,"./src/components/event_hall"),
      "messages_contacts-components" : path.resolve(__dirname,"./src/components/messages_contacts"),
      "forum-components" : path.resolve(__dirname,"./src/components/forum"),
    },
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],
};
[![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)
[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

Usage
The easiest way to use JavaScript Semi-Standard Style to check your code is to install it globally as a Node command line program. To do so, simply run the following command in your terminal (flag -g installs semistandard globally on your system, omit it if you want to install in the current working directory):

npm install semistandard -g
After you've done that you should be able to use the semistandard program. The simplest use case would be checking the style of all JavaScript files in the current working directory:

$ semistandard
Error: Use JavaScript Semi-Standard Style
  lib/torrent.js:950:11: Expected '===' and instead saw '=='.


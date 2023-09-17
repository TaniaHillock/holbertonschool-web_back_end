# ES6 classes
## Resources
* Classes
* Metaprogramming
## Learning Objectives
* How to define a Class
* How to add methods to a class
* Why and how to add a static method to a class
* How to extend a class from another
* Metaprogramming and symbols
## Requirements
* All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
* Allowed editors: vi, vim, emacs, Visual Studio Code
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the js extension
* Your code will be tested using Jest and the command npm run test
* Your code will be verified against lint using ESLint
* Your code needs to pass all the tests and lint. You can verify the entire project running npm run full-test
## Setup
Install NodeJS 12.11.x
(in your home directory):

curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y

$ nodejs -v
v12.11.1
$ npm -v
6.11.3


## Install Jest, Babel, and ESLint in your project directory:

Install Jest using: npm install --save-dev jest
Install Babel using: npm install --save-dev babel-jest @babel/core @babel/preset-env
Install ESLint using: npm install --save-dev eslint

## Configuration files
* package.json
* babel.config.js
* eslintrc.js

and run

$ npm install when you have the package.json

## Files

| Name | Description |
|------|--------------
|0-classroom.js|Class named ClassRoom accepts one attribute and assigned to _maxStudentsSize|
|1-make_classrooms.js| Function initializeRooms returns an array of 3 ClassRoom objects with the sizes 19, 20, and 34|

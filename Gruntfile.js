'use strict';

module.exports = function (grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),


    // Cleaning annoying python bytecode files   
    clean: {
      src:["app/**/*.pyc","app/**/*.pyo"]
    }

  });

  grunt.loadNpmTasks('grunt-contrib-clean');
};

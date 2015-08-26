'use strict';

module.exports = function (grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),


    // Compiling sass
    sass: {
      dist: {
        files: {
          'app/static/css/main.css': 'app/static/scss/main.scss'
        }
      }
    },

    // Cleaning annoying python bytecode files
    clean: {
      src:["app/**/*.pyc","app/**/*.pyo"]
    },

    watch: {
      files: ['app/static/scss/**/*'],
      tasks: ['sass'],
    },

  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-sass');
};

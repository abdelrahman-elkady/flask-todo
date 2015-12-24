'use strict';

module.exports = function(grunt) {

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

    // Concatinating JS
    concat: {
      options: {
        separator: '\n\n',
      },
      dist: {
        src: ['app/static/js/src/init.js', 'app/static/js/src/*.js'],
        dest: 'app/static/js/main.js',
      },
    },

    // Cleaning annoying python bytecode files
    clean: {
      src: ["app/**/*.pyc", "app/**/*.pyo", "tests/**/*.pyc", "tests/**/*.pyo"]
    },

    watch: {
      sass: {
        files: ['app/static/scss/**/*'],
        tasks: ['sass'],
      },

      js: {
        files: ['app/static/js/src/*.js'],
        tasks: ['concat'],
      }
    },

    nose: {
      main: {},
      options: {
        virtualenv: 'venv',
      },
    },

  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-nose');
  grunt.loadNpmTasks('grunt-contrib-concat');

  grunt.registerTask('test', ['nose', 'clean']);
};

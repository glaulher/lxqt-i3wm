#!/usr/bin/python
# coding=UTF-8
# These glyphs, and the mapping of file extensions to glyphs
# has been copied from the vimscript code that is present in
# https://github.com/ryanoasis/vim-devicons
import re
import os
from getpass import getuser


# all those glyphs will show as weird squares if you don't have the correct patched font
# My advice is to use NerdFonts which can be found here:
# https://github.com/ryanoasis/nerd-fonts
file_node_extensions = {
          'styl'     : '',
          'sass'     : '',
          'scss'     : '',
          'htm'      : '',
          'html'     : '',
          'slim'     : '',
          'haml'     : '',
          'ejs'      : '',
          'css'      : '',
          'less'     : '',
          'md'       : '',
          'mdx'      : '',
          'markdown' : '',
          'rmd'      : '',
          'json'     : '',
          'webmanifest' : '',
          'js'       : '',
          'mjs'      : '',
          'jsx'      : '',
          'rb'       : '',
          'gemspec'  : '',
          'rake'     : '',
          'php'      : '',
          'py'       : '',
          'pyc'      : '',
          'pyo'      : '',
          'pyd'      : '',
          'coffee'   : '',
          'mustache' : '',
          'hbs'      : '',
          'conf'     : '',
          'ini'      : '',
          'yml'      : '',
          'yaml'     : '',
          'toml'     : '',
          'bat'      : '',
          'jpg'      : '',
          'jpeg'     : '',
          'bmp'      : '',
          'png'      : '',
          'webp'     : '',
          'gif'      : '',
          'ico'      : '',
          'twig'     : '',
          'cpp'      : '',
          'c++'      : '',
          'cxx'      : '',
          'cc'       : '',
          'cp'       : '',
          'c'        : '',
          'cs'       : '',
          'h'        : '',
          'hh'       : '',
          'hpp'      : '',
          'hxx'      : '',
          'hs'       : '',
          'lhs'      : '',
          'nix'      : '',
          'lua'      : '',
          'java'     : '',
          'sh'       : '',
          'fish'     : '',
          'bash'     : '',
          'zsh'      : '',
          'ksh'      : '',
          'csh'      : '',
          'awk'      : '',
          'ps1'      : '',
          'ml'       : 'λ',
          'mli'      : 'λ',
          'diff'     : '',
          'db'       : '',
          'sql'      : '',
          'dump'     : '',
          'clj'      : '',
          'cljc'     : '',
          'cljs'     : '',
          'edn'      : '',
          'scala'    : '',
          'go'       : '',
          'dart'     : '',
          'xul'      : '',
          'sln'      : '',
          'suo'      : '',
          'pl'       : '',
          'pm'       : '',
          't'        : '',
          'rss'      : '',
          'f#'       : '',
          'fsscript' : '',
          'fsx'      : '',
          'fs'       : '',
          'fsi'      : '',
          'rs'       : '',
          'rlib'     : '',
          'd'        : '',
          'erl'      : '',
          'hrl'      : '',
          'ex'       : '',
          'exs'      : '',
          'eex'      : '',
          'leex'     : '',
          'vim'      : '',
          'ai'       : '',
          'psd'      : '',
          'psb'      : '',
          'ts'       : '',
          'tsx'      : '',
          'jl'       : '',
          'pp'       : '',
          'vue'      : '﵂',
          'elm'      : '',
          'swift'    : '',
          'xcplayground' : '',
          'tex'      : 'ﭨ',
          'r'        : 'ﳒ',
          'rproj'    : '鉶'
}

dir_node_exact_matches = {
# GNU/linux standard home stuff
    '.git'                             : '',
    '.mozilla'                         : '',
    '.templates'                       : '',
    '.config'                          : '',
    '.ssh'                             : '',
    '.steam'                           : '',
    '.purple'                          : '',
    '.wine'                            : '',
    '.vim'                             : '',
    'dropbox'                          : '',
#    'gdrive'                           : '',
# English
    'Desktop'                          : '',
    'Documents'                        : '',
    'Downloads'                        : '',
    'Dropbox'                          : '',
    'Music'                            : '',
    'Pictures'                         : '',
    'Public'                           : '',
    'Templates'                        : '',
    'Videos'                           : '',
    'src'                              : '',
# French
    'Bureau'                           : '',
    'Documents'                        : '',
    'Téléchargements'                  : '',
    'Musique'                          : '',
    'Images'                           : '',
    'Publique'                         : '',
    'Vidéos'                           : '',
# Portuguese
    'Área de trabalho'                 : '',
    'Documentos'                       : '',
    'Música'                           : '',
    'Imagens'                          : '',
    'Público'                          : '',
    'Modelos'                          : '',
    'Vídeos'                           : '',
# Italian
    'Scrivania'                        : '',
    'Documenti'                        : '',
    'Scaricati'                        : '',
    'Musica'                           : '',
    'Immagini'                         : '',
    'Pubblici'                         : '',
    'Modelli'                          : '',
    'Video'                            : '',
# German
    'Schreibtisch'                     : '',
    'Dokumente'                        : '',
    'Musik'                            : '',
    'Bilder'                           : '',
    'Öffentlich'                       : '',
    'Vorlagen'                         : '',
}

file_node_exact_matches = {
    '.Xauthority'                      : '',
    '.Xdefaults'                       : '',
    '.Xresources'                      : '',
    '.bash_aliases'                    : '',
    '.bashprofile'                     : '',
    '.bash_profile'                    : '',
    '.bash_logout'                     : '',
    '.bash_history'                    : '',
    '.bashrc'                          : '',
    '.dmrc'                            : '',
    '.DS_Store'                        : '',
    '.fasd'                            : '',
    '.fehbg'                           : '',
    '.gitconfig'                       : '',
    '.gitattributes'                   : '',
    '.gitignore'                       : '',
    '.inputrc'                         : '',
    '.jack-settings'                   : '',
    '.mime.types'                      : '',
    '.nvidia-settings-rc'              : '',
    '.pam_environment'                 : '',
    '.profile'                         : '',
    '.recently-used'                   : '',
    '.selected_editor'                 : '',
    '.vim'                             : '',
    '.vimrc'                           : '',
    '.viminfo'                         : '',
    '.xinitrc'                         : '',
    '.xinputrc'                        : '',
    'config'                           : '',
    'Dockerfile'                       : '',
    'docker-compose.yml'               : '',
    'dropbox'                          : '',
    'exact-match-case-sensitive-1.txt' : 'X1',
    'exact-match-case-sensitive-2'     : 'X2',
    'favicon.ico'                      : '',
    'a.out'                            : '',
    'bspwmrc'                          : '',
    'sxhkdrc'                          : '',
    'Makefile'                         : '',
    'Makefile.in'                      : '',
    'Makefile.ac'                      : '',
    'config.mk'                        : '',
    'config.m4'                        : '',
    'config.ac'                        : '',
    'configure'                        : '',
    'Rakefile'                         : '',
    'gruntfile.coffee'                 : '',
    'gruntfile.js'                     : '',
    'gruntfile.ls'                     : '',
    'gulpfile.coffee'                  : '',
    'gulpfile.js'                      : '',
    'gulpfile.ls'                      : '',
    'ini'                              : '',
    'ledger'                           : '',
    'package.json'                     : '',
    'package-lock.json'                : '',
    '.ncmpcpp'                         : '',
    'playlists'                        : '',
    'known_hosts'                      : '',
    'authorized_keys'                  : '',
    'license'                          : '',
    'LICENSE.md'                       : '',
    'LICENSE'                          : '',
    'LICENSE.txt'                      : '',
    'mimeapps.list'                    : '',
    'node_modules'                     : '',
    'procfile'                         : '',
    'react.jsx'                        : '',
    'README.rst'                       : '',
    'README.md'                        : '',
    'README.markdown'                  : '',
    'README'                           : '',
    'README.txt'                       : '',
    'user-dirs.dirs'                   : '',
    'webpack.config.js'                : '',
}

def devicon(file):
  folder_ico = ''
  

  if file.is_link:
      if file.is_directory:
        folder_ico = ''
      else:
        folder_ico = ''
      return dir_node_exact_matches.get(file.relative_path, folder_ico)

  if file.is_directory: 
      if '/run/media/'+getuser() == file.dirname or '/mnt/' == file.dirname:
        folder_ico = '' 
      else:
        folder_ico = ''
      return dir_node_exact_matches.get(file.relative_path, folder_ico)

  return file_node_exact_matches.get(file.relative_path, file_node_extensions.get(file.extension, ''))

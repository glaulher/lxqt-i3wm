#!/usr/bin/python
# coding=UTF-8
# These glyphs, and the mapping of file extensions to glyphs
# has been copied from the vimscript code that is present in
# https://github.com/ryanoasis/vim-devicons
import re;
import os;

# all those glyphs will show as weird squares if you don't have the correct patched font
# My advice is to use NerdFonts which can be found here:
# https://github.com/ryanoasis/nerd-fonts
file_node_extensions = {
#video 
   'avi'      : '',
   'mkv'      : '',
   'mp4'      : '',
   'mpeg'     : '',
   'mpg'      : '',
   'flv'      : '',
   'mov'      : '',
#image
	'jpeg'     : '',
    'jpg'      : '',
    'gif'      : '',
    'png'      : '',
    'bmp'      : '',
    'ico'      : '',
#audio
	'ogg'      : '',
	'flac'     : '',	
	'mp3'      : '',
	'wav'      : '',
#text
	'pdf'      : '',
	'txt'      : '',
	'srt'      : '',
#package 
    'iso'      : '',
	'deb'      : '',
	'apk'      : '',	
	'rpm'      : '',
	'7z'       : '',
	'bz2'      : '',	
	'cab'      : '',
	'gz'       : '',
	'gzip'     : '',
	'gem'      : '',
	'zip'      : '',
	'tar'      : '',
    'tgz'      : '',
    'rar'      : '',
#dev
    'css'      : '',
    'xml'      : '',
	'htm'      : '',
    'html'     : '',
    'java'     : '',
    'jar'      : '',
    'js'       : '',
    'json'     : '',	
    'db'       : '⛃',
    'py'       : '',
    'sln'      : '',
    'suo'      : '',   
   
}

dir_node_exact_matches = {
# English
    '.git'                             : '',
    'Desktop'                          : '',
    'Documents'                        : '',
    'Downloads'                        : '',
    'Dropbox'                          : '',
    'Music'                            : '',
    'Pictures'                         : '',
    'Public'                           : '',
    'Templates'                        : '',
    'Videos'                           : '',
# French
    'Bureau'                           : '',
    'Documents'                        : '',
    'Images'                           : '',
    'Musique'                          : '',
    'Publique'                         : '',
    'Téléchargements'                  : '',
    'Vidéos'                           : '',
# Portuguese
    'Documentos'                       : '',
    'Imagens'                          : '',
    'Modelos'                          : '',
    'Música'                           : '',
    'Público'                          : '',
    'Vídeos'                           : '',
    'Área de trabalho'                 : '',
# Italian
    'Documenti'                        : '',
    'Immagini'                         : '',
    'Modelli'                          : '',
    'Musica'                           : '',
    'Pubblici'                         : '',
    'Scaricati'                        : '',
    'Scrivania'                        : '',
    'Video'                            : '',
# German
    'Bilder'                           : '',
    'Dokumente'                        : '',
    'Musik'                            : '',
    'Schreibtisch'                     : '',
    'Vorlagen'                         : '',
    'Öffentlich'                       : '',
}

file_node_exact_matches = {
    '.Xdefaults'                       : '',
    '.Xresources'                      : '',
    '.bashprofile'                     : '',
    '.bashrc'                          : '',
    '.dmrc'                            : '',
    '.ds_store'                        : '',
    '.fasd'                            : '',
    '.gitconfig'                       : '',
    '.gitignore'                       : '',
    '.jack-settings'                   : '',
    '.mime.types'                      : '',
    '.nvidia-settings-rc'              : '',
    '.pam_environment'                 : '',
    '.profile'                         : '',
    '.recently-used'                   : '',
    '.selected_editor'                 : '',
    '.vimrc'                           : '',
    '.xinputrc'                        : '',
    'config'                           : '',
    'dropbox'                          : '',
    'exact-match-case-sensitive-1.txt' : 'X1',
    'exact-match-case-sensitive-2'     : 'X2',
    'favicon.ico'                      : '',

}

def devicon(file):
  if file.is_directory: return dir_node_exact_matches.get(file.relative_path, '')
  return file_node_exact_matches.get(file.relative_path, file_node_extensions.get(file.extension, ''))

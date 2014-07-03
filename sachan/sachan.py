# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile
import hashlib
from sys import argv
import getopt

def gethashfile(path_to_file):
	f = open(path_to_file, 'rb')
	sha = hashlib.new('sha1')
	sha.update(f.read())
	f.close()
	return sha.hexdigest()

def savechanges(backupdir, sourcedir):
	pass

def main(argv):
	option, args = getopt.getopt(argv, "hb:s:")
	backupdir = ''
	sourcedir = ''
	for opt, arg in option:
		if opt == '-h':
			print 'sachan.py -b <backupdir> -s <sourcedir> '
		elif opt == '-b':
			backupdir = arg
		elif opt == '-s':
			sourcedir = arg
	savechanges(backupdir, sourcedir)
	
	#path_to_file = r'F:\dump\pruebas\sachan\file.txt'
	#print gethashfile(path_to_file)

if __name__ == '__main__':
	main(argv[1:])
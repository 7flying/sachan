# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile
import hashlib

def gethashfile(path_to_file):
	f = open(path_to_file, 'rb')
	sha = hashlib.new('sha1')
	sha.update(f.read())
	f.close()
	return sha.hexdigest()

def main():
	path_to_file = r'F:\dump\pruebas\sachan\file.txt'
	print gethashfile(path_to_file)

if __name__ == '__main__':
	main()
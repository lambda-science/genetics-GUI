#!/usr/bin/python
# -*- coding: utf-8 -*-

def countAcidNuc(seq):
	"""Function that count every letter in a string.
	Return a dictionnary with each letter and the number of occurence"""
	acidNucCount = {}
	for i in seq:
		acidNucCount[i] = acidNucCount.get(i, 0) +1
	return acidNucCount
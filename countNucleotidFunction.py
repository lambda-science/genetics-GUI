def countAcidNuc(seq):
	acidNucCount = {}
	for i in seq:
		acidNucCount[i] = acidNucCount.get(i, 0) +1
	return acidNucCount
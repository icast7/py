lex = {
	'north' : 'direction' ,
	'south' : 'direction',
	'east':'direction',
	'west':'direction',



	'bear':'noun',
	'cabinet':'noun',
	'door':'noun',
	'princess':'noun'
}



def scan(text):
	words = text.split()
	pairs = []

	for word in words:
		try:
			word2 = word[(-len(word)):-1]
			mynum = int(word2)
			tuples = ('number', mynum)
		except ValueError:
			if lex.has_key(word):
				w_type = lex[word]
				tuples = (w_type, word)
			else:
				tuples = ('error',word)
		pairs.append(tuples)

	return pairs


print lex
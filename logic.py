class KB:
	"""Do something here"""

def splitLiteral(sentence):

	#Tach bien dua vao OR
	literal = sentence.split(" OR ")
	return literal
	

def main():
	input = open("input.txt")
	
	#Cau alpha
	alpha = input.readline()
	alpha = alpha.rstrip()	#Xoa dau \n o cuoi
	
	#So menh de cua KB
	numClause = int(input.readline())
	
	#Cau cua KB
	sentence = []
	for i in range(numClause):
		s = input.readline()
		s = s.rstrip()
		sentence.append(s)
		
	print(alpha)
	
	list = []
	for i in sentence:
		list.append(splitLiteral(i))
		
	print(list)
	
main()
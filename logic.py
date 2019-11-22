class KnowledgeBase:
	#KB la mang cac Clause
	#clauses = []
	
	def __init__(self):
		#Mang cac doi tuong Literal
		self.clauses = []
	
	def getKB(self, KBString):
		
		for i in range(len(KBString)):
			clause = Clause()
			clause.getClauseFromSentence(KBString[i])
			self.clauses.append(clause)
			'''print(len(self.clauses[i].literals))'''
			
	def addClause(self, clause):
		#Dung de them not(alpha) vao KB
		self.clauses.append(clause)

		
def splitLiteral(sentence):
	#Ham tach cau thanh mang cac chuoi literal
	#A OR -B => ['A', '-B']
	#Tach bien dua vao OR
	literals = sentence.split(" OR ")
	return literals
	
class Clause:
	#In logic, a clause is an expression formed from a finite collection of literals (atoms or their negations) (Source: Wikipedia)
	#literals = []
	def __init__(self):
		#Mang cac doi tuong Literal
		self.literals = []
	
	
	def getClauseFromSentence(self, sentence):
		
		literalList = splitLiteral(sentence)
		for i in literalList:
			lit = Literal()
			lit.getLiteral(i)
			self.literals.append(lit)
	def negate(self):
		for i in self.literals:
			i.negate()
			
class Literal:
	def __init__(self, symbol = '', isNegative = 0):
		self.symbol = symbol
		
		#isNegative == 1 neu literal am, == 0 neu literal duong
		self.isNegative = isNegative
	def __del__(self): 
		self.symbol = ''
		self.isNegative = 0
	
	def isNegativeOf(self, l):
		return self.symbol == l.symbol and self.isNegative != l.isNegative
		
	def getLiteral(self, s):
		#Ham dua chuoi ve doi tuong Literal
		#Vi du: "-A" -> (symbol = 'A', isNegative = 0)
		
		if s[0] == '-':
			
			self.isNegative = 1
			self.symbol = s[1]
		else:
			
			self.isNegative = 0
			self.symbol = str(s[0])
			
	def negate(self):
		#Lay phu dinh 1 literal
		self.isNegative = int(not self.isNegative)
def main():
	input = open("input.txt")
	
	#Cau alpha
	alphaSentence = input.readline()
	alphaSentence = alphaSentence.rstrip()	#Xoa dau \n o cuoi
	
	alpha = Clause()
	alpha.getClauseFromSentence(alphaSentence)
	alpha.negate()
	
	
	#So menh de cua KB
	numClause = int(input.readline())
	
	#Cau cua KB
	sentences = []
	for i in range(numClause):
		s = input.readline()
		s = s.rstrip()
		sentences.append(s)
	print(sentences)
		
	KB = KnowledgeBase()
	KB.getKB(sentences)
	KB.addClause(alpha)
	
	'''KB.printKB()'''
	print(len(KB.clauses))
	
	for i in range(len(KB.clauses)):
		for j in range(len(KB.clauses[i].literals)):
			print("Clause ", i, vars(KB.clauses[i].literals[j]))
	'''
	print(vars(KB.clauses[0].literals[0]))
	print(vars(KB.clauses[0].literals[1]))
	print(vars(KB.clauses[1].literals[0]))
	print(vars(KB.clauses[1].literals[1]))
	print(vars(KB.clauses[2].literals[0]))
	print(vars(KB.clauses[2].literals[1]))
	print(vars(KB.clauses[2].literals[2]))
	print(vars(KB.clauses[3].literals[0]))
	'''
	
main()
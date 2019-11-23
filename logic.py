	
def splitLiteral(sentence):
	#Ham tach cau thanh mang cac chuoi literal
	#A OR -B => ['A', '-B']
	#Tach bien phu thuoc vao OR
	literals = sentence.split(" OR ")
	return literals


def setClausesFromKB(KB):
	setClauses = set()
	for i in range(len(KB)):
		clause = Clause()
		clause.setClauseFromSentence(KB[i])
		setClauses.add(clause)
	return setClauses
	

class Clause:
	#In logic, a clause is an expression formed from a finite collection of literals (atoms or their negations) (Source: Wikipedia)
	#literals = []
	def __init__(self):
		#Mang cac Literal
		self.literals = []
		self.numLiteral = 0
	
	def __key(self):
		return (tuple(self.literals), self.numLiteral)

	def __hash__(self):
		return hash(self.__key())
	
	def __eq__(self, other):
		if isinstance(other, Clause):
			return self.numLiteral == other.numLiteral and sorted(self.literals) == sorted(other.literals)
		return False 
		
	def setClauseFromSentence(self, sentence):
		
		literalList = splitLiteral(sentence)
		for i in literalList:
			lit = Literal()
			lit.setLiteral(i)
			self.addLiteral(lit)
		self.literals.sort()
			
	def addLiteral(self, literal):
		self.literals.append(literal)
		self.numLiteral += 1
			
	def negate(self):
		for i in self.literals:
			i.negate()
		
	def reduce(self):
	
		#Loai bo cac literal giong nhau trong cung  clause
		final_list = [] 
		for li in self.literals: 
			if li not in final_list: 
				final_list.append(li) 
		self.literals = final_list
		self.numLiteral = len(final_list) 
	
	def isTrue(self):
		#Ham xet chan tri cua clause co phai true khong
		#Vi clause chan tri true thi khong can thiet
		for li in self.literals:
			liNeg = Literal(li.symbol, li.isNegative)
			liNeg.negate()
			if liNeg in self.literals:
				return True
		return False
	'''
	def __contains__(self, item):
		for i in self.literals:
			if item.symbol == self.symbol and item.isNegative == self.isNegative:
				return True
		return False
	'''		

	def __str__(self):
		if self.numLiteral == 0:
			return "{}"
		s = str(self.literals[0])
		for i in range(1, self.numLiteral):
			s += " OR "
			s += str(self.literals[i])
		return s			
	
class Literal:
	def __init__(self, symbol = '', isNegative = 0):
		self.symbol = symbol
		
		#isNegative == 1 neu literal am, == 0 neu literal duong
		self.isNegative = isNegative
	def __key(self):
		return (self.symbol, self.isNegative)
	def __eq__(self, other): 
		if self.symbol == other.symbol and self.isNegative == other.isNegative: 
			return True
		else: 
			return False
	def __lt__(self, other): 
		if self.symbol < other.symbol: 
			return True
		else: 
			return False		
	def __hash__(self): 
		return hash(self.__key())
	
	def __str__(self):
		if self.isNegative == 1:
			return '-' + self.symbol
		else:
			return self.symbol
	
	def isNegativeOf(self, l):
		return self.symbol == l.symbol and self.isNegative != l.isNegative
		
	def setLiteral(self, s):
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
		
def resolve(Ci, Cj):
	
	resolvent = Clause()
	for li in Ci.literals:
		for lj in Cj.literals:
			#Neu co 2 Literal trong 2 Clause doi nghich nhau
			if li.isNegativeOf(lj):
				resolvent = Clause()
				
				#thi lay cac literal con lai cua 2 cau noi voi nhau
				for i in Ci.literals:
					if i != li:
						resolvent.addLiteral(i)
				for j in Cj.literals:
					if j != lj:
						resolvent.addLiteral(j)
						
				#Neu clause co chan tri la True thi khong can thiet
				if resolvent.isTrue():
					return False
				#Tra ve clause suy ra duoc
				resolvent.literals.sort()
				resolvent.reduce()
				return resolvent
			
	#Neu khong co literal nao doi nghich nhau
	return False
						
def PL_Resolution(KB, alphaSentence):
	#ref: PL_Resolution Pseudo code - Artificial Intelligence, A Modern Approach
	#clauses ←the set of clauses in the CNF representation of KB ∧¬α
	clauses = setClausesFromKB(KB)
	alpha = Clause()
	alpha.setClauseFromSentence(alphaSentence)
	alpha.negate()
	clauses.add(alpha)
	'''
	clauseList = list(clauses)
	
	for i in range(len(clauses)):
		
		for j in range(clauses[i].numLiteral):
			print("Clause ", i, ": ", vars(clauses[i].literals[j]))
			
	'''
	#new ←{}
	new = set()
	found = 0
	clauseList = list(clauses)
	
	while True:
		clauseResolve = set()
		clauseResolvePrev = set() #Luu lai cac menh de duoc suy ra o vong lap truoc
		clauseList = list(clauses)
		for i in range(len(clauseList)-1):
			for j in range(i+1, len(clauseList)):
				resolvent = resolve(clauseList[i], clauseList[j])
				
				#if resolvents contains the empty clause then return true
				if resolvent != False:
					
					if resolvent.numLiteral == 0:
						'''print("True roi nha may dua")'''
						found = 1
					#new ←new ∪ resolvents
					new.add(resolvent)
					clauseResolve.add(resolvent)
				
			
		#if new is subset of clauses then return false
		#Lay nhung clause chua xuat hien
		clauseResolve = clauseResolve.difference(clauseResolvePrev, clauses)
		
		print(len(clauseResolve))
		for c in list(clauseResolve):
			print(str(c))
		if found == 1:
			return True
		if new.issubset(clauses):
			return False
		clauses = clauses.union(new)
		clauseResolvePrev = clauseResolve
		'''print(clauses)
		'''
	
def main():
	input = open("input.txt")
	
	#Cau alpha
	alphaSentence = input.readline()
	alphaSentence = alphaSentence.rstrip()	#Xoa dau \n o cuoi
	
	'''
	alpha = Clause()
	alpha.setClauseFromSentence(alphaSentence)
	alpha.negate()
	'''
	
	#So menh de cua KB
	numClause = int(input.readline())
	
	#Cau cua KB
	KB = []
	for i in range(numClause):
		s = input.readline()
		s = s.rstrip()
		KB.append(s)
	
	print(KB)
	
	'''
	KB = KnowledgeBase()
	KB.setKB(sentences)
	KB.addClause(alpha)
	'''
	if PL_Resolution(KB, alphaSentence) == True:
		print("YES")
	else:
		print("NO")
	
	
	'''KB.printKB()'''
	
main()
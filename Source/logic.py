
def writeToFile(output, buffer):
	output.write(buffer)
	
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
		#return (self.numLiteral, dict(self.literals))
		return (self.numLiteral, tuple(self.literals))

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
						
def PL_Resolution(KB, alphaSentence, output):
	#ref: PL_Resolution Pseudo code - Artificial Intelligence, A Modern Approach
	#clauses ←the set of clauses in the CNF representation of KB ∧¬α
	clauses = setClausesFromKB(KB)
	alpha = Clause()
	alpha.setClauseFromSentence(alphaSentence)

	#add negative-alpha to clauses
	for i in range(alpha.numLiteral):
		c = Clause()
		l = alpha.literals[i]
		l.negate()
		c.addLiteral(l)
		clauses.add(c)
	
	#new ←{}
	new = set()
	found = 0
	clauseList = list(clauses)
	
	while True:
		clauseResolve = set()
		#clauseResolvePrev = set() #Luu lai cac menh de duoc suy ra o vong lap truoc
		clauseList = list(clauses)
		for i in range(len(clauseList)-1):
			for j in range(i+1, len(clauseList)):
				resolvent = resolve(clauseList[i], clauseList[j])
				
				if resolvent != False:	
					if resolvent.numLiteral == 0:
						found = 1
					#new ←new ∪ resolvents
					new.add(resolvent)
					clauseResolve.add(resolvent)
				
			
		#Lay nhung clause chua xuat hien
		clauseResolve = clauseResolve.difference(clauses)
		
		output.write(str(len(clauseResolve)) + '\n')
		for c in list(clauseResolve):
			output.write(str(c) + '\n')
			
		#if resolvents contains the empty clause then return true
		if found == 1:
			return True
			
		#if new is subset of clauses then return false
		if new.issubset(clauses):
			return False
		clauses = clauses.union(new)
		#clauseResolvePrev = clauseResolve
		
	
def main():
	input = open("input.txt")
	output = open("output.txt", "w")
	
	#Cau alpha
	alphaSentence = input.readline()
	alphaSentence = alphaSentence.rstrip()	#Xoa dau \n o cuoi
	
	
	#So menh de cua KB
	numClause = int(input.readline())
	
	#Cau cua KB
	KB = []
	for i in range(numClause):
		s = input.readline()
		s = s.rstrip()
		KB.append(s)
	
	if PL_Resolution(KB, alphaSentence, output) == True:
		output.write("YES\n")
	else:
		output.write("NO\n")
	input.close()
	output.close()
	
main()
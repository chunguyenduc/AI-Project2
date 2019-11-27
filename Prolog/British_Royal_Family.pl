:-discontiguous male/1,female/1,married/2,parent/2,divorced/2.

female('Queen Elizabeth II').
female('Princess Diana').
female('Duchess Camilla Parker Bowles').
female('Duchess Sarah Ferguson').
female('Princess Anne').
female('Countess Sophie Rhys-Jones').
female('Duchess Kate Middleton').
female('Duchess Meghan Markle').
female('Princess Eugenie').
female('Princess Beatrice').
female('Autumn Phillips').
female('Zara Tindall').
female('Lady Louise Windsor').
female('Princess Charlotte').

male('Prince Philip').
male('Prince Charles').
male('Prince Andrew').
male('Captain Mark Phillips').
male('Timothy Laurence').
male('Prince Edward').
male('Prince William').
male('Prince Harry').
male('Peter Phillips').
male('Mike Tindall').
male('Viscount James').
male('Prince George').
male('Prince Louis').
male('Archie Harrison Mountbatten-Windsor').

parent('Queen Elizabeth II','Prince Charles').
parent('Queen Elizabeth II','Prince Andrew').
parent('Queen Elizabeth II','Princess Anne').
parent('Queen Elizabeth II','Prince Edward').
parent('Prince Philip','Prince Charles').
parent('Prince Philip','Prince Andrew').
parent('Prince Philip','Princess Anne').
parent('Prince Philip','Prince Edward').
parent('Princess Diana','Prince William').
parent('Princess Diana','Prince Harry').
parent('Prince Charles','Prince William').
parent('Prince Charles','Prince Harry').
parent('Prince Andrew','Princess Eugenie').
parent('Prince Andrew','Princess Beatrice').
parent('Duchess Sarah Ferguson','Princess Eugenie').
parent('Duchess Sarah Ferguson','Princess Beatrice').
parent('Captain Mark Phillips','Peter Phillips').
parent('Captain Mark Phillips','Zara Tindall').
parent('Princess Anne','Peter Phillips').
parent('Princess Anne','Zara Tindall').
parent('Prince Edward','Lady Louise Windsor').
parent('Prince Edward','Viscount James').
parent('Countess Sophie Rhys-Jones','Lady Louise Windsor').
parent('Countess Sophie Rhys-Jones','Viscount James').
parent('Duchess Kate Middleton','Prince George').
parent('Duchess Kate Middleton','Princess Charlotte').
parent('Duchess Kate Middleton','Prince Louis').
parent('Prince William','Prince George').
parent('Prince William','Princess Charlotte').
parent('Prince William','Prince Louis').
parent('Prince Harry','Archie Harrison Mountbatten-Windsor').
parent('Duchess Meghan Markle','Archie Harrison Mountbatten-Windsor').

married('Queen Elizabeth II','Prince Philip').
married('Princess Diana','Prince Charles').
married('Prince Charles','Duchess Camilla Parker Bowles').
married('Prince Andrew','Duchess Sarah Ferguson').
married('Captain Mark Phillips','Princess Anne').
married('Princess Anne','Timothy Laurence').
married('Prince Edward','Countess Sophie Rhys-Jones').
married('Duchess Kate Middleton','Prince William').
married('Prince Harry','Duchess Meghan Markle').
married('Peter Phillips','Autumn Phillips').
married('Zara Tindall','Mike Tindall').


married('Prince Philip','Queen Elizabeth II').
married('Prince Charles','Princess Diana').
married('Duchess Camilla Parker Bowles','Prince Charles').
married('Duchess Sarah Ferguson','Prince Andrew').
married('Princess Anne','Captain Mark Phillips').
married('Timothy Laurence','Princess Anne').
married('Countess Sophie Rhys-Jones','Prince Edward').
married('Prince William','Duchess Kate Middleton').
married('Duchess Meghan Markle','Prince Harry').
married('Autumn Phillips','Peter Phillips').
married('Mike Tindall','Zara Tindall').

divorced('Prince Charles','Princess Diana').
divorced('Prince Andrew','Duchess Sarah Ferguson').
divorced(Person1,Person2) :-
	divorced(Person2,Person1).

husband(Person,Wife) :-
	male(Person), female(Wife), married(Person,Wife).
wife(Person,Husband) :-
	female(Person), male(Husband), married(Person,Husband).
father(Parent,Child) :-
	male(Parent), parent(Parent,Child).
mother(Parent,Child) :-
	female(Parent), parent(Parent,Child).
child(Child,Parent) :-
	parent(Parent,Child).
son(Child,Parent) :-
	male(Child), parent(Parent,Child).
daughter(Child,Parent) :-
	female(Child), parent(Parent,Child).

grandparent(GP,GC) :-
	parent(GP,U), parent(U,GC).
grandmother(GM,GC) :-
	parent(GM,U), parent(U,GC), female(U).
grandfather(GF,GC) :-
	parent(GF,U), parent(U,GC), male(U).
grandchild(GC,GP) :-
	parent(GP,U), parent(U,GC).
grandson(GS,GP) :-
	male(GS), parent(GP,U), parent(U,GS).
granddaughter(GD,GP) :-
	female(GD), parent(GP,U), parent(U,GD).

sibling(Person1,Person2) :-
	parent(Parent,Person1), parent(Parent,Person2), Person1\=Person2.
brother(Person,Sibling) :-
	sibling(Person,Sibling), male(Person).
sister(Person,Sibling) :-
	sibling(Person,Sibling), female(Person).
aunt(Person,NieceNephew) :-
	parent(Parent,NieceNephew), sister(Person,Parent).
uncle(Person,NieceNephew) :-
	parent(Parent,NieceNephew), brother(Person,Parent).
niece(Person,AuntUncle) :-
	male(Person), aunt(AuntUncle,Person); uncle(AuntUncle,Person).
nephew(Person,AuntUncle) :-
	female(Person), aunt(AuntUncle,Person); uncle(AuntUncle,Person).






/*female(A): A la nu gioi*/
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

/*male(A) : A la mot nam gioi*/
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

/*parent(A,B) : A la cha/me cua B*/
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

/*married(A,B) : A da ket hon voi B*/
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

/*divorced(A,B) : A da ly hon voi B*/
divorced('Prince Charles','Princess Diana').
divorced('Prince Andrew','Duchess Sarah Ferguson').
divorced('Princess Diana','Prince Charles').
divorced('Duchess Sarah Ferguson','Prince Andrew').

/*husband(Person,Wife) : Person la chong cua Wife*/
husband(Person,Wife) :-
	male(Person), female(Wife), married(Person,Wife).

/*wife(Person,Husband) : Person la vo cua Husband */
wife(Person,Husband) :-
	female(Person), male(Husband), married(Person,Husband).

/*father(Parent,Child) : Parent la cha cua Child*/
father(Parent,Child) :-
	male(Parent), parent(Parent,Child).

/*mother(Parent,Child) : Parent la me cua Child*/
mother(Parent,Child) :-
	female(Parent), parent(Parent,Child).

/*child(Child,Parent) : Child la con cua Parent*/
child(Child,Parent) :-
	parent(Parent,Child).

/*son(Child,Parent) : Child la con trai cua Parent*/
son(Child,Parent) :-
	male(Child), parent(Parent,Child).

/*daughter(Child,Parent) : Child la con gai cua Parent*/
daughter(Child,Parent) :-
	female(Child), parent(Parent,Child).

/*grandparent(GP,GC) : GP la ong ba cua GC*/
grandparent(GP,GC) :-
	parent(GP,U), parent(U,GC).

/*grandmother(GM,GC) : GM la ong/ba ngoai cua GC*/
grandmother(GM,GC) :-
	parent(GM,U), parent(U,GC), female(U).

/*grandfather(GF,GC) : GF la ong/ba noi cua GC*/
grandfather(GF,GC) :-
	parent(GF,U), parent(U,GC), male(U).

/*grandchild(GC,GP) : GC la chau cua GP*/
grandchild(GC,GP) :-
	parent(GP,U), parent(U,GC).

/*grandson(GS,GP) : GS la chau trai cua GP*/
grandson(GS,GP) :-
	male(GS), parent(GP,U), parent(U,GS).

/*granddaughter(GD,GP) : GD la chau gai cua GP*/
granddaughter(GD,GP) :-
	female(GD), parent(GP,U), parent(U,GD).

/*sibling(Person1,Person2) : Person1 la anh/chi/em cua Person2*/
sibling(Person1,Person2) :-
	parent(Parent,Person1), parent(Parent,Person2), Person1 \= Person2, male(Parent).

/*brother(Person,Sibling) : Person la anh/em trai cua Sibling*/
brother(Person,Sibling) :-
	sibling(Person,Sibling), male(Person), Person \= Sibling.

/*sister(Person,Sibling) : Person la chi/em gai cua Sibling*/
sister(Person,Sibling) :-
	sibling(Person,Sibling), female(Person), Person \= Sibling.

/*aunt(Person,NieceNephew) : Person la di/co/mo cua NieceNephew*/
aunt(Person,NieceNephew) :-
	parent(Parent,NieceNephew), parent(X,Parent), parent(X,Person), female(Person).

/*uncle(Person,NieceNephew) : Person la duong/chu/cau cua NieceNephew*/
uncle(Person,NieceNephew) :-
	parent(Parent,NieceNephew), parent(X,Parent), parent(X,Person), male(Person).

/*niece(Person,AuntUncle) : Person la chau gai cua AuntUncle*/
niece(Person,AuntUncle) :-
	female(Person), child(Person,Parent), parent(Parent1,Parent), parent(Parent1,AuntUncle), male(Parent1), AuntUncle \= Parent.

/*nephew(Person,AuntUncle) : Person la chau trai cua AuntUncle*/
nephew(Person,AuntUncle) :-
	male(Person), child(Person,Parent), parent(Parent1,Parent), parent(Parent1,AuntUncle), male(Parent1), AuntUncle \= Parent.






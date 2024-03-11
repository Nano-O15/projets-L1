evaluer_etat(Pot,Mise,Piece) :-
    Pot =< 0 -> halt;
    evaluer_etat2(Pot, Mise, Piece).

evaluer_etat(Pot,Mise,Piece) :-
    Piece > 0.5,
    write('La valeur de Piece est egale a '),
    write(Piece),
    nl,
    New_Pot is Pot + Mise,
    next_etat(New_Pot, Mise).

evaluer_etat(Pot,Mise,Piece) :-
    Piece < 0.5,
    write('La valeur de Piece est egale a '),
    write(Piece),
    nl,
    New_Pot is Pot - Mise,
    next_etat(New_Pot, Mise).

evaluer_etat2(Pot, Mise, Piece) :-
    Piece < 0.1,
    write('La valeur de Piece est egale a '),
    write(Piece),
    nl,
    write('Tu doubles la Mise !'),
    nl,
    New_Mise is Mise + Mise,
    next_etat(Pot, New_Mise).

next_etat(Pot, Mise) :-
    write('Le Pot est de '),
    write(Pot),
    nl,
    write('La Mise est de '),
    write(Mise).

next_etat(Pot, Mise) :-
    random(Piece),
    evaluer_etat(Pot, Mise, Piece).

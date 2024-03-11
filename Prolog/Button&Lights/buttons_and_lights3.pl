print_res([]):- !.
print_res([T|Q]) :- 
    write(T),
    write(' '), 
    print_res(Q).

action1(_,B,C,1,B,C).

action2(A,B,C,B,A,C).

action3(A,B,C,A,C,B).

next(0,0,0,A1,B1,C1,1):-
    action1(0,0,0,A1,B1,C1).


next(1,0,C,A1,B1,C1,2):-
    action2(1,0,C,A1,B1,C1).

next(0,1,0,A1,B1,C1,1):-
    action1(0,1,0,A1,B1,C1).

next(0,1,0,A1,B1,C1,3):-
    action3(0,1,0,A1,B1,C1).

next(1,1,0,A1,B1,C1,3):-
    action3(1,1,0,A1,B1,C1).

next(0,B,1,A1,B1,C1,1):-
    action1(0,B,1,A1,B1,C1).

endgame(1,1,1).

continuer(1,1,1,_,Res):-
    write("Success "),
    print_res(Res).
    
continuer(A,B,C,X,Res):-
    not(endgame(A,B,C)),
    X>0,
    next(A,B,C,A1,B1,C1,Action),
    append([Action],Res,Res2),
    Y is X-1,
    continuer(A1,B1,C1,Y,Res2).

jouer(A,B,C,X):-
    continuer(A,B,C,X,[]).

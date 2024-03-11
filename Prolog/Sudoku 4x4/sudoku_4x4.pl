different([]).
different([T|H]):-
    not(member(T,H)),
    different(H).

oneness([]).
oneness(List):-
    member(1, List), 
    member(2, List), 
    member(3, List),
    member(4, List),
    different(List).

nombre([A,B,C,D]):-
    member(A, [1,2,4,8]),
    member(B, [1,2,4,8]),
    member(C, [1,2,4,8]),
    member(D, [1,2,4,8]),
    Y is A + B + C + D,
    Y = 15.


sudoku([A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]):-
    oneness([A,B,C,D]),
    oneness([E,F,G,H]),
    oneness([I,J,K,L]),
    oneness([M,N,O,P]),
    oneness([A,E,I,M]),
    oneness([B,F,J,N]),
    oneness([C,G,K,O]),
    oneness([D,H,L,P]),
    oneness([A,B,E,F]),
    oneness([C,D,G,H]),
    oneness([I,J,M,N]),
    oneness([K,L,O,P]).

sudoku2([A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]):-
    nombre([A,B,C,D]),
    nombre([E,F,G,H]),
    nombre([I,J,K,L]),
    nombre([M,N,O,P]),
    nombre([A,E,I,M]),
    nombre([B,F,J,N]),
    nombre([C,G,K,O]),
    nombre([D,H,L,P]),
    nombre([A,B,E,F]),
    nombre([C,D,G,H]),
    nombre([I,J,M,N]),
    nombre([K,L,O,P]).

print_line_sudoku([]):- !.
print_line_sudoku([T|Q]) :- 
    write(T),
    write(' '), 
    print_line_sudoku(Q).

all_sol_sudoku2([A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]):-
    nombre([A,B,C,D]),
    nombre([E,F,G,H]),
    nombre([I,J,K,L]),
    nombre([M,N,O,P]),
    nombre([A,E,I,M]),
    nombre([B,F,J,N]),
    nombre([C,G,K,O]),
    nombre([D,H,L,P]),
    nombre([A,B,E,F]),
    nombre([C,D,G,H]),
    nombre([I,J,M,N]),
    nombre([K,L,O,P]),
    print_line_sudoku([A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]).
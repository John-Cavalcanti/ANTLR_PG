grammar Arithmetic;

// Regras do Parser e Novas Regras do Parser
expr: term ( (PLUS | MINUS) term )* ;
term: factor ( (MUL | DIV) factor )* ;
factor: INT | VAR | LPAREN expr RPAREN ;

program: statement+ ;
statement: assignment | expr ;
assignment: VAR ASSIGN expr ;

// Regras do Lexer e Novas Regras do Lexer
PLUS: '+' ;
MINUS: '-' ;
MUL: '*' ;
DIV: '/' ;
INT: [0-9]+ ;
LPAREN: '(' ;
RPAREN: ')' ;
WS: [ \t\r\n]+ -> skip ;

VAR: [a-zA-Z]+ ;
ASSIGN: '=' ;


   

grammar Expr;

program: statement+ EOF ;
// Keywords

WS : [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;

primitiveType
    : type=INT
    | type=FLOAT
    | type=STRING
    | type=BOOLEAN
    ;

BOOLEAN:    'bool';
FLOAT:      'float';
INT:        'int';
STRING:     'string';

READ:       'read' ;
WRITE:      'write' ;
IF:         'if';
WHILE:      'while';
ELSE:       'else';
FOR:        'for';

SEMI:       ';';
COMMA:      ',';
CON :       '.' ;
MUL :       '*' ; 
DIV :       '/' ;
MOD :       '%' ;
ADD :       '+' ;
SUB :       '-' ;
LES :       '<' ;
GRE :       '>' ;
NEG :       '!' ;
EQ  :       '==' ;
NEQ :       '!=' ;
AND :       '&&' ;
OR :        '||' ;


IDENTIFIER : [a-zA-Z] ([a-zA-Z0-9]*)? ; 

// Literals

DECIMAL_LITERAL:    [0-9]+;
FLOAT_LITERAL:      [0-9]+ CON [0-9]+;
BOOL_LITERAL:       'true'
            |       'false'
            ;
STRING_LITERAL:     '"' (~["\\\r\n] | EscapeSequence)* '"';

fragment EscapeSequence
    : '\\' [btnfr"'\\]
    | '\\' ([0-3]? [0-7])? [0-7]
    ;



// STATEMENTS-EXPRESSION

statement
    : '{' statement* '}'                                                    # blockOfStatements     
    | primitiveType IDENTIFIER ( COMMA IDENTIFIER)* SEMI                    # declaration          
    | FOR '(' init=expr SEMI cond=expr SEMI update=expr ')' loop=statement  # for 
    | IF '(' cond=expr ')' pos=statement (ELSE neg=statement)?              # ifElse                
    | WHILE '(' cond=expr ')' loop=statement                                # while
    | READ IDENTIFIER ( COMMA IDENTIFIER)* SEMI                             # readStatement 
    | WRITE expr ( COMMA expr)* SEMI                                        # writeStatement           
    | expr SEMI                                                             # printExpr              
    | SEMI                                                                  # emptyStatement        
    ;

expr: IDENTIFIER                            # id            
    | ('true'|'false')                      # bool
    | DECIMAL_LITERAL                       # int
    | FLOAT_LITERAL                         # float
    | STRING_LITERAL                        # string          
    | '(' expr ')'                          # parens
    | prefix=SUB right=expr                 # unaryMinus    
    | prefix=NEG right=expr                 # negation      
    | left=expr op=(MUL|DIV|MOD) right=expr # mulDivMod     
    | left=expr op=(ADD|SUB|CON) right=expr # addSubCon    
    | left=expr op=(LES|GRE) right=expr     # relation     
    | left=expr op=(EQ|NEQ) right=expr      # comparison
    | left=expr AND right=expr              # logicalAnd   
    | left=expr OR right= expr              # logicalOr     
    | <assoc=right> IDENTIFIER '=' expr     # assignment
    ;



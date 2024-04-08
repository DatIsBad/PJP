grammar Expr;

program: statement+ EOF ;
// Keywords

BOOLEAN:    'bool';
FLOAT:      'float';
INT:        'int';
STRING:     'string';

READ:       'read' ;
WRITE:      'write' ;
IF:         'if';
WHILE:      'while';
ELSE:       'else';

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

DECIMAL_LITERAL:    [1-9]+;
FLOAT_LITERAL:      [1-9]+ '.' [1-9]+;
BOOL_LITERAL:       'true'
            |       'false'
            ;
STRING_LITERAL:     '"' (~["\\\r\n] | EscapeSequence)* '"';

fragment EscapeSequence
    : '\\' [btnfr"'\\]
    | '\\' ([0-3]? [0-7])? [0-7]
    ;



// STATEMENTS


statement
    : '{' statement* '}'                                    # blockOfStatements     // YY
    | (BOOLEAN | INT | FLOAT | STRING) IDENTIFIER ( ',' IDENTIFIER)* ';'    # declaration           // YY
    | IF '(' expr ')' pos=statement (ELSE neg=statement)?   # ifElse                // YY
    | WHILE '(' expr ')' statement                          # while                 // Y
    | READ IDENTIFIER ( ',' IDENTIFIER)* ';'             # readStatement            // YY
    | WRITE expr ( ',' expr)* ';'                        # writeStatement           // YY
    | expr ';'                                             # printExpr              // YY
    | ';'                                                  # emptyStatement         // Y
    ;

expr: IDENTIFIER                            # id            // YY
    | ('true'|'false')                      # bool          // YY
    | '(' expr ')'                          # parens        // YY
    | INT                                   # int           // YY
    | FLOAT                                 # float         // YY
    | STRING                                # string        // YY
    | prefix=SUB expr                       # unaryMinus    // YY
    | prefix=NEG expr                       # negation      // YY
    | expr op=(MUL|DIV|MOD) expr            # mulDivMod     // YY
    | expr op=(ADD|SUB|CON) expr            # addSubCon     // YY
    | expr op=(LES|GRE) expr                # relation      // YY
    | expr op=(EQ|NEQ) expr                 # comparison    // YY
    | expr AND expr                         # logicalAnd    // YY
    | expr OR expr                          # logicalOr     // YY
    | <assoc=right> IDENTIFIER '=' expr     # assignment    // YY
    ;

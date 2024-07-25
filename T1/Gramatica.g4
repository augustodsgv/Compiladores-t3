lexer grammar Gramatica;

//palavras chave verificada inicialmente, para que não fossem classificadas como cadeias
PALAVRA_CHAVE 
	:	'algoritmo' | 'declare' | 'inteiro' | 'leia' | 'escreva' | 'fim_algoritmo' | 'real' | 'literal' 
	| 'logico' | 'fim_se' | 'senao' | 'entao' | 'se' | 'ou' | 'fim_caso' | 'para' | 'ate' | 'faca'
	| 'fim_enquanto' | 'fim_para' | 'seja' | 'caso' | 'enquanto' | 'registro' | 'fim_registro'
	| 'tipo' | 'fim_procedimento' | 'procedimento' | 'var' | 'funcao' | 'fim_funcao'
	| 'retorne' | 'constante' | 'falso' | 'verdadeiro'
	; 

//todos os elementos que deveriam ser repetidos na saída foram colocasos em uma só classe, por isso alguns são operadores e delimitadores
PONTUACAO : ',' | '(' | ')' | '/' | '+' | '<-' | '-' | '*' | 'e' | 'nao' | '=' | '<=' | '>=' | '..' | '<' 
	| '<>' | '>' | '%' | '^' | '&' | '.' | '[' | ']' | ':'
	;

//aceita casos em que a variavel possui "_" no meio
IDENT : ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9' | '_')*
	;

NUM_INT	: ('0'..'9')+
	;
NUM_REAL : ('0'..'9')+ ('.' ('0'..'9')+)?
	;

CADEIA 	: '"' ( ~('\n') )*? '"'
	;
fragment
ESC_SEQ	: '\\\'';


COMENTARIO
    :   '{' ~('\n'|'\r'|'}')* '}' ('\n' | ' ')
    ;

COMENTARIO_FECHADO_2
    :   '{' ~('\n'|'\r'|'}')* '}}' ('\n' | ' ')
    ;

//trata o erro do comentário sem chaves fechando
COMENTARIO_ABERTO:  '{' ~('\n'|'\r' | '}')* ('\n')
	;

WS  :   ( ' '
        | '\t'
        | '\r'	
        | '\n'
        ) {pass}
    ;

//trata o erro da cadeia sem aspas fechando
CADEIA_NAO_FECHADA: '"' ( ~('\n') )*? 
	;


//trata caracteres que não são reconhecidos
ERRO_CARACTER : ('~')+ | '$' | '}'
	;	
from antlr4 import Lexer

class Vocabulary:
    def __init__(self, grammar_file : str):
        self.tokens : dict = {}
        with open(grammar_file) as f:
            for line in f.readlines(): 
                line = line.replace("'", '')
                spplited_line = line.split('=')
                if len(spplited_line) > 2:
                    key = '='
                    value = spplited_line[-1]
                else:
                    key, value = spplited_line
                self.tokens[key] = int(value)
    
    def is_token(self, token : str) :
        return token in self.tokens.keys()
    

if __name__ == '__main__':
    v = Vocabulary('Gramatica.tokens')
    print(v.tokens)
                
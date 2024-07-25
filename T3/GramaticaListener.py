# Generated from Gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete listener for a parse tree produced by GramaticaParser.
class GramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaParser#var_personalizada.
    def enterVar_personalizada(self, ctx:GramaticaParser.Var_personalizadaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#var_personalizada.
    def exitVar_personalizada(self, ctx:GramaticaParser.Var_personalizadaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#var_registro.
    def enterVar_registro(self, ctx:GramaticaParser.Var_registroContext):
        pass

    # Exit a parse tree produced by GramaticaParser#var_registro.
    def exitVar_registro(self, ctx:GramaticaParser.Var_registroContext):
        pass


    # Enter a parse tree produced by GramaticaParser#ponteiro.
    def enterPonteiro(self, ctx:GramaticaParser.PonteiroContext):
        pass

    # Exit a parse tree produced by GramaticaParser#ponteiro.
    def exitPonteiro(self, ctx:GramaticaParser.PonteiroContext):
        pass


    # Enter a parse tree produced by GramaticaParser#endereco.
    def enterEndereco(self, ctx:GramaticaParser.EnderecoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#endereco.
    def exitEndereco(self, ctx:GramaticaParser.EnderecoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#op_bool.
    def enterOp_bool(self, ctx:GramaticaParser.Op_boolContext):
        pass

    # Exit a parse tree produced by GramaticaParser#op_bool.
    def exitOp_bool(self, ctx:GramaticaParser.Op_boolContext):
        pass


    # Enter a parse tree produced by GramaticaParser#programa.
    def enterPrograma(self, ctx:GramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#programa.
    def exitPrograma(self, ctx:GramaticaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#listaComandos.
    def enterListaComandos(self, ctx:GramaticaParser.ListaComandosContext):
        pass

    # Exit a parse tree produced by GramaticaParser#listaComandos.
    def exitListaComandos(self, ctx:GramaticaParser.ListaComandosContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comando.
    def enterComando(self, ctx:GramaticaParser.ComandoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comando.
    def exitComando(self, ctx:GramaticaParser.ComandoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comandoAtribuicao.
    def enterComandoAtribuicao(self, ctx:GramaticaParser.ComandoAtribuicaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comandoAtribuicao.
    def exitComandoAtribuicao(self, ctx:GramaticaParser.ComandoAtribuicaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracao.
    def enterDeclaracao(self, ctx:GramaticaParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracao.
    def exitDeclaracao(self, ctx:GramaticaParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracao_tipo.
    def enterDeclaracao_tipo(self, ctx:GramaticaParser.Declaracao_tipoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracao_tipo.
    def exitDeclaracao_tipo(self, ctx:GramaticaParser.Declaracao_tipoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracao_registro.
    def enterDeclaracao_registro(self, ctx:GramaticaParser.Declaracao_registroContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracao_registro.
    def exitDeclaracao_registro(self, ctx:GramaticaParser.Declaracao_registroContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracao_constante.
    def enterDeclaracao_constante(self, ctx:GramaticaParser.Declaracao_constanteContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracao_constante.
    def exitDeclaracao_constante(self, ctx:GramaticaParser.Declaracao_constanteContext):
        pass


    # Enter a parse tree produced by GramaticaParser#expressaoAritmetica.
    def enterExpressaoAritmetica(self, ctx:GramaticaParser.ExpressaoAritmeticaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#expressaoAritmetica.
    def exitExpressaoAritmetica(self, ctx:GramaticaParser.ExpressaoAritmeticaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#fatorAritmetico.
    def enterFatorAritmetico(self, ctx:GramaticaParser.FatorAritmeticoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#fatorAritmetico.
    def exitFatorAritmetico(self, ctx:GramaticaParser.FatorAritmeticoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#expressaoRelacional.
    def enterExpressaoRelacional(self, ctx:GramaticaParser.ExpressaoRelacionalContext):
        pass

    # Exit a parse tree produced by GramaticaParser#expressaoRelacional.
    def exitExpressaoRelacional(self, ctx:GramaticaParser.ExpressaoRelacionalContext):
        pass


    # Enter a parse tree produced by GramaticaParser#termoRelacional.
    def enterTermoRelacional(self, ctx:GramaticaParser.TermoRelacionalContext):
        pass

    # Exit a parse tree produced by GramaticaParser#termoRelacional.
    def exitTermoRelacional(self, ctx:GramaticaParser.TermoRelacionalContext):
        pass


    # Enter a parse tree produced by GramaticaParser#entrada.
    def enterEntrada(self, ctx:GramaticaParser.EntradaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#entrada.
    def exitEntrada(self, ctx:GramaticaParser.EntradaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comandoEntrada.
    def enterComandoEntrada(self, ctx:GramaticaParser.ComandoEntradaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comandoEntrada.
    def exitComandoEntrada(self, ctx:GramaticaParser.ComandoEntradaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#saida.
    def enterSaida(self, ctx:GramaticaParser.SaidaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#saida.
    def exitSaida(self, ctx:GramaticaParser.SaidaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comandoSaida.
    def enterComandoSaida(self, ctx:GramaticaParser.ComandoSaidaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comandoSaida.
    def exitComandoSaida(self, ctx:GramaticaParser.ComandoSaidaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comandoCondicao.
    def enterComandoCondicao(self, ctx:GramaticaParser.ComandoCondicaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comandoCondicao.
    def exitComandoCondicao(self, ctx:GramaticaParser.ComandoCondicaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#intervalo.
    def enterIntervalo(self, ctx:GramaticaParser.IntervaloContext):
        pass

    # Exit a parse tree produced by GramaticaParser#intervalo.
    def exitIntervalo(self, ctx:GramaticaParser.IntervaloContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comandoCaso.
    def enterComandoCaso(self, ctx:GramaticaParser.ComandoCasoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comandoCaso.
    def exitComandoCaso(self, ctx:GramaticaParser.ComandoCasoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comandoEnquanto.
    def enterComandoEnquanto(self, ctx:GramaticaParser.ComandoEnquantoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comandoEnquanto.
    def exitComandoEnquanto(self, ctx:GramaticaParser.ComandoEnquantoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comandoFaca.
    def enterComandoFaca(self, ctx:GramaticaParser.ComandoFacaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comandoFaca.
    def exitComandoFaca(self, ctx:GramaticaParser.ComandoFacaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#comandoPara.
    def enterComandoPara(self, ctx:GramaticaParser.ComandoParaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#comandoPara.
    def exitComandoPara(self, ctx:GramaticaParser.ComandoParaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#subAlgoritmo.
    def enterSubAlgoritmo(self, ctx:GramaticaParser.SubAlgoritmoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#subAlgoritmo.
    def exitSubAlgoritmo(self, ctx:GramaticaParser.SubAlgoritmoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#parametros_chamada_funcao.
    def enterParametros_chamada_funcao(self, ctx:GramaticaParser.Parametros_chamada_funcaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parametros_chamada_funcao.
    def exitParametros_chamada_funcao(self, ctx:GramaticaParser.Parametros_chamada_funcaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#chamada_funcao.
    def enterChamada_funcao(self, ctx:GramaticaParser.Chamada_funcaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#chamada_funcao.
    def exitChamada_funcao(self, ctx:GramaticaParser.Chamada_funcaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#parametros_declaracao_funcao.
    def enterParametros_declaracao_funcao(self, ctx:GramaticaParser.Parametros_declaracao_funcaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#parametros_declaracao_funcao.
    def exitParametros_declaracao_funcao(self, ctx:GramaticaParser.Parametros_declaracao_funcaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracao_funcao.
    def enterDeclaracao_funcao(self, ctx:GramaticaParser.Declaracao_funcaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracao_funcao.
    def exitDeclaracao_funcao(self, ctx:GramaticaParser.Declaracao_funcaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#retorno_funcao.
    def enterRetorno_funcao(self, ctx:GramaticaParser.Retorno_funcaoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#retorno_funcao.
    def exitRetorno_funcao(self, ctx:GramaticaParser.Retorno_funcaoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#procedimento.
    def enterProcedimento(self, ctx:GramaticaParser.ProcedimentoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#procedimento.
    def exitProcedimento(self, ctx:GramaticaParser.ProcedimentoContext):
        pass



del GramaticaParser
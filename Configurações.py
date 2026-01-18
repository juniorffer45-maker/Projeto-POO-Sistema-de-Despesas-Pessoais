class Configuracoes:
    def __init__(self, filename="settings.json"):
        self.filename = filename

        self.alerta_alto_gasto = 500.0               # valor em reais
        self.meses_comparativo = 3                   # quantidade de meses
        self.meta_economia_percentual = 10.0         # percentual (%)

        # Se existir arquivo, pode ser carregado futuramente
        self.validar_parametros()
   
    def validar_parametros(self):
        if not (0<= self.meta_economia_percentual <=1):
           print("Erro: Meta de economia percentual deve estar entre 0 e 1")
           return False 
        
        if self.alerta_alto_gasto <0:
           print("Erro: Alerta de alto gasto deve ser maior ou igual a 0")
           return False

        return True

    def atualizar_meta(self, nova_meta): # Adicionado nome da função
        valor_antigo = self.meta_economia_percentual
        self.meta_economia_percentual = nova_meta
        if self.validar_parametros():
            print(f"Meta alterada de {valor_antigo:.0%} para {nova_meta:.0%}")
        else:
            self.meta_economia_percentual = valor_antigo

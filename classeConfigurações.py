  class Configuracoes:
    def __init__(self, filename='settings.json'):
        self.filename = filename
        self.alerta_alto_gasto = 0.0
        self.meta_economia_percentual = 0.0
        self.carregar()

    def configurar_inicial(self):
        print("CONFIGURAÇÃO INICIAL")
        try:
            self.alerta_alto_gasto = float(input("Valor para alerta de gasto alto (Ex: 1000): "))
            self.meta_economia_percentual = float(input("Meta de economia % (Ex: 10): "))
            self.salvar()
        except ValueError:
            print("Valores inválidos. Usando padrões: 1000 e 10%.")
            self.alerta_alto_gasto, self.meta_economia_percentual = 1000.0, 10.0

    def salvar(self): # Salva os atributos atuais em um arquivo JSON separado
        with open(self.filename, 'w') as f:
            json.dump(self.__dict__, f, indent=4)

    def carregar(self): # Lê o arquivo de texto e atualiza os atributos da classe.
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                dados = json.load(f)
                self.alerta_alto_gasto = dados.get('alerta_alto_gasto', 1000.0)
                self.meta_economia_percentual = dados.get('meta_economia_percentual', 10.0)

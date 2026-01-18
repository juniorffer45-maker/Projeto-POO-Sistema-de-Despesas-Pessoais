class GerenciadorFinanças:
    def __init__(self):
        self.categorias = {}
        self.orcamentos = {}
        self.configuracoes = Configuracoes()
        self.arquivo_dados = "dados.json"
        self.carregar_dados()

    def carregar_dados(self):
        if not os.path.exists(self.arquivo_dados): return
        with open(self.arquivo_dados, "r") as f:
            dados = json.load(f)
            for n, c in dados.get("categorias", {}).items():
                self.categorias[n] = Categoria(c['nome'], c['tipo'], c['limite_mensal'], c['descricao'])
            for k, o in dados.get("orcamentos", {}).items():
                obj_orc = OrcamentoMensal(o['mes'], o['ano'])
                for l in o['lancamentos']:
                    cat = self.categorias[l['categoria']]
                    dt = date.fromisoformat(l['data'])
                    Classe = Receita if cat.tipo == "RECEITA" else Despesa
                    obj_orc.adicionar_lancamento(Classe(l['valor'], cat, dt, l['forma_de_pagamento'], l['status']))
                self.orcamentos[k] = obj_orc

    def salvar_dados(self):
        dados = {
            "categorias": {n: c.to_dict() for n, c in self.categorias.items()},
            "orcamentos": {k: o.to_dict() for k, o in self.orcamentos.items()}
        }
        with open(self.arquivo_dados, "w") as f:
            json.dump(dados, f, indent=4)

    def cadastrar_categoria(self, nome, tipo, limite=None):
        if nome not in self.categorias:
            self.categorias[nome] = Categoria(nome, tipo, limite)
            self.salvar_dados()

    def adicionar_lancamento(self, valor, nome_cat, data_str, forma, status, classe):
        dt = datetime.strptime(data_str, "%d/%m/%Y").date()
        chave = f"{dt.month:02d}-{dt.year}"
        if chave not in self.orcamentos: self.orcamentos[chave] = OrcamentoMensal(dt.month, dt.year)
        
        lanc = classe(valor, self.categorias[nome_cat], dt, forma, status)
        self.orcamentos[chave].adicionar_lancamento(lanc)
        
        # Lógica de Alerta de Gasto Alto
        if isinstance(lanc, Despesa) and valor >= self.configuracoes.alerta_alto_gasto:
            print(f"Erro: Alto gasto detectado: (R${valor:.2f})")
            
        self.salvar_dados()

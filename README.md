# Projeto-POO-Sistema-de-Despesas-Pessoais

## Equipe - Grupo de Programação UFCA

## Integrantes da Equipe
##### -- Beatriz Benigno de Vasconcelos(2025013076) - Construção das Classes GerenciadorFinanças e OrçamentoMensal 
##### -- Aldemir Ferreira da Silva Junior(2025012892) - Construção das Classes Categoria, Lançamento e Alerta
##### -- Ana Karla Pontes de Souza(2025012954) - Construção da Classe 
##### -- João Paulo Lima David(2025013441) - Construção da Classe Configuração
##### -- Maria Ivanilda Irineu de Lima(2025013610) - Construção da Classe Despesa

## Classes do Sistema
##### Class: Categoria
##### Atributos: id, nome, tipo, limite_mensal,  descricao
##### Metodos: __init__(self, nome, tipo, limite_mensal=None, descricao=""),  @property nome(self), @nome.setter(self, novo_nome), @property limite_mensal(self), @limite_mensal.setter(self, novo_limite), to_dict(self)  
-
##### Class: Lançamento
##### Atributos: valor, categoria, data, descrição, forma de pagamento
##### Metodos: __init__(self, valor, categoria, data, ...),  @property valor(self), @valor.setter(self, novo_valor), @property data(self), @data.setter(self, nova_data), __str__(self), __repr__(self), __eq__(self, outro), __lt__(self, outro), __add__(self, outro), to_dict(self) 
-
##### Class: Receita
##### Atributos: self
##### Metodos: __init__(self)
-
##### Class: Despesas
##### Atributos: self
##### Metodos: __init__(self, ...) ,@valor.setter(self, novo_valor), validar_limite(self), validar_alto_valor(self, limite_alto)
-
##### Class: GerenciadorFinanças
##### Atributos: categorias, orcamentos, configuracoes, alertas_log  
##### Metodos: carregar_dados(self), salvar_dados(self),  cadastrar_categoria(...), adicionar_lancamento(...), gerar_relatorio_comparativo(), identificar_mes_economico()
-
##### Class: OrçamentoMensal
##### Atributos: mes, ano, lançamentos
##### Metodos: __init__(self, mes, ano), adicionar_lancamento(self, lancamento), calcular_total_receitas(self), calcular_total_despesas(self), calcular_saldo(self), verificar_deficit(self), gerar_relatorio(self)
-
##### Class: Alerta
##### Atributos: tipo, mensagem, data, lancamento
##### Metodos: __init__(self, tipo, mensagem, data, lancamento=None), __str__(self)
-
##### Class: Configurações
##### Atributos: alerta_alto_gasto, meses_comparativo, meta_economia_percentual
##### Metodos:  __init__(self, filename='settings.json'), validar_parametros(self)


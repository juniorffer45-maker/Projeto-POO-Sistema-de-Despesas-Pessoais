# Projeto-POO-Sistema-de-Despesas-Pessoais

## Equipe - Grupo de Programação UFCA

## Integrantes da Equipe
##### -- Beatriz Benigno de Vasconcelos(2025013076) -  DevOps e Front-End
##### -- Aldemir Ferreira da Silva Junior(2025012892) - Back-end
##### -- Ana Karla Pontes de Souza(2025012954) - Design
##### -- João Paulo Lima David(2025013441) - Banco de Dados
##### -- Maria Ivanilda Irineu de Lima(2025013610) - Front-End

### Uma ferramenta simples e eficiente para gerenciar sua vida financeira, permitindo o acompanhamento detalhado de entradas e saídas com relatórios automáticos e alerta de gastos.

##### Classes: Gerenciador de Finanças, Cadastro de Categorias, Lançamento de Receitas e Despesas, Orçamento Mensal, Relatórios e Estatísticas, Configuracoes, Alertas.

-
##### Class: GerenciadorFinanças
##### Atributos: categorias, orcamentos, configuracoes, alertas 
##### Metodos: carregar_dados(self), salvar_dados(self), cadastrar_categoria(...), adicionar_lancamento(...), gerar_relatorio_comparativo(), identificar_mes_economico(), remover_categoria(id), excluir_lancamento(id)
-
##### Class: Categoria
##### Atributos: id, nome, tipo, limite_mensal,  descricao
##### Metodos: __init__(self, nome, tipo, limite_mensal=None, descricao=""), @property nome(self), @nome.setter(self, novo_nome), @property limite_mensal(self), @limite_mensal.setter(self, novo_limite), to_dict(self)  
-
##### Class: Lançamento
##### Atributos: valor, categoria, data, descrição, forma de pagamento, status
##### Metodos: __init__(self, valor, categoria, data, ...),  @property valor(self), @valor.setter(self, novo_valor), @property data(self), @data.setter(self, nova_data), __str__(self), __repr__(self), __eq__(self, outro), __lt__(self, outro), __add__(self, outro), to_dict(self), marcar_como_pago(self) , marcar_como_pendente(self), esta_pago(self)
-
##### Class: Receita
##### Atributos: self
##### Metodos: __init__(self)
-
##### Class: Despesas
##### Atributos: self
##### Metodos: __init__(self, ...), @valor.setter(self, novo_valor), validar_limite(self), validar_alto_valor(self, limite_alto)
-
##### Class: OrçamentoMensal
##### Atributos: mes, ano, lançamentos
##### Metodos: __init__(self, mes, ano), adicionar_lancamento(self, lancamento), calcular_total_receitas(self), calcular_total_despesas(self), calcular_saldo(self), verificar_deficit(self), gerar_relatorio(self)
-
##### Class: RelatoriosEstatisticas
##### Atributos: orcamentos, OrcamentoMensal
##### Metodos: __init__(self, lista_orcamentos), total_por_categoria(self, mes, ano), despesas_por_forma_pagamento(self, mes, ano), calcular_percentuais_categoria(self, mes, ano), mes_mais_economico(self), comparativo_ultimos_3_meses(self, mes_atual, ano_atual), _buscar_orcamento(self, mes, ano), _subtrair_meses(self, mes, ano, n)
-
##### Class: Alerta
##### Atributos: tipo, mensagem, data, lancamento
##### Metodos: __init__(self, tipo, mensagem, data, lancamento=None)
-
##### Class: Configurações
##### Atributos: alerta_alto_gasto, meses_comparativo, meta_economia_percentual
##### Metodos: __init__(self, filename='settings.json'), validar_parametros(self), alterar_meta_economia(self, nova_meta)



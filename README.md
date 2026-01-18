# Projeto-POO-Sistema-de-Despesas-Pessoais

## Equipe - Grupo de Programação UFCA

## Integrantes da Equipe
##### -- Beatriz Benigno de Vasconcelos(2025013076)
##### -- Aldemir Ferreira da Silva Junior(2025012892) 
##### -- Ana Karla Pontes de Souza(2025012954) 
##### -- João Paulo Lima David(2025013441) 
##### -- Maria Ivanilda Irineu de Lima(2025013610) 

### Uma ferramenta simples e eficiente para gerenciar sua vida financeira, permitindo o acompanhamento detalhado de entradas e saídas com relatórios automáticos e alerta de gastos.

##### PARA USAR O GERENCIADOR, VÁ EM SISTEMA.PY 

.
.
.
.
.
-
##### Class: GerenciadorFinanças
##### Atributos: categorias, orcamentos, configuracoes, alertas 
##### Metodos: carregar_dados, salvar_dados, cadastrar_categoria, adicionar_lancamento, gerar_relatorio_comparativo, identificar_mes_economico, remover_categoria, excluir_lancamento.

#### É o "chefe" do sistema. É ele quem salva os dados no arquivo JSON, carrega os dados quando o programa abre e decide para qual mês um novo gasto deve ir. Ele conecta todas as outras classes.
-
##### Class: Categoria
##### Atributos: id, nome, tipo, limite_mensal,  descricao
##### Metodos: __init__(self, nome, tipo, limite_mensal=None, descricao=""), @property nome(self), @nome.setter(self, novo_nome), @property limite_mensal(self), @limite_mensal.setter(self, novo_limite), to_dict(self)

#### É a etiqueta que você coloca no gasto (ex: "Saúde", "Lazer"). Ela guarda o nome e, no caso de despesas, o valor máximo que você pretende gastar nela por mês.

-
##### Class: Lançamento
##### Atributos: valor, categoria, data, descrição, forma de pagamento, status
##### Metodos: __init__(self, valor, categoria, data, ...),  @property valor(self), @valor.setter(self, novo_valor), @property data(self), @data.setter(self, nova_data), __str__(self), __repr__(self), __eq__(self, outro), __lt__(self, outro), __add__(self, outro), to_dict(self), marcar_como_pago(self) , marcar_como_pendente(self), esta_pago(self)

#### (Classe Mãe): É o modelo base para qualquer movimentação de dinheiro. Ela guarda o valor, a data e a descrição. Serve tambem para garantir que Receitas e Despesas tenham a mesma estrutura.
-
##### Class: Receita
##### Atributos: self
##### Metodos: __init__(self)

#### (Filha de Lancamento): Representa o dinheiro que entra (Salário, Pix recebido). Sua função é somar ao saldo.
-
##### Class: Despesas
##### Atributos: self
##### Metodos: __init__(self, ...), @valor.setter(self, novo_valor), validar_limite(self), validar_alto_valor(self, limite_alto)

#### (Filha de Lancamento): Representa o dinheiro que sai (Aluguel, Lanche). Ela verifica se o gasto está dentro do limite da categoria e avisa se for um valor muito alto.

-
##### Class: OrçamentoMensal
##### Atributos: mes, ano, lançamentos
##### Metodos: __init__(self, mes, ano), adicionar_lancamento(self, lancamento), calcular_total_receitas(self), calcular_total_despesas(self), calcular_saldo(self), verificar_deficit(self), gerar_relatorio(self)

#### É como uma "pasta" do mês. Ela junta todos os lançamentos de Janeiro, Fevereiro, etc. Ela sabe calcular sozinha: "Quanto ganhei esse mês?", "Quanto gastei?" e "Quanto sobrou?".

-
##### Class: RelatoriosEstatisticas
##### Atributos: orcamentos, OrcamentoMensal
##### Metodos: __init__(self, lista_orcamentos), total_por_categoria(self, mes, ano), despesas_por_forma_pagamento(self, mes, ano), calcular_percentuais_categoria(self, mes, ano), mes_mais_economico(self), comparativo_ultimos_3_meses(self, mes_atual, ano_atual), _buscar_orcamento(self, mes, ano), _subtrair_meses(self, mes, ano, n)

#### É o "analista". Ele olha para todos os dados e cria as estatísticas, como gráficos de pizza (gastos por categoria) ou comparativos de quanto você gastou nos últimos 3 meses.

-
##### Class: Alerta
##### Atributos: tipo, mensagem, data, lancamento
##### Metodos: __init__(self, tipo, mensagem, data, lancamento=None)

#### É uma mensagem de aviso. Ela é criada automaticamente quando algo sai do planejado (ex: você gastou mais do que ganhou ou ultrapassou o limite de uma categoria).
-
##### Class: Configurações
##### Atributos: alerta_alto_gasto, meses_comparativo, meta_economia_percentual
##### Metodos: __init__(self, filename='settings.json'), validar_parametros(self), alterar_meta_economia(self, nova_meta)

#### Guarda as regras e configurações do usuário, como: "Quero ser avisado sempre que um gasto passar de R$ 500" ou "Minha meta é economizar 10% do que ganho".
-

##### Class: InterfaceCLI
##### Atributos: gerenciador, usuario_logado, menu_ativo
##### Metodos: exibir_menu_principal(), limpar_tela(), solicitar_dados_categoria(), solicitar_dados_lancamento(), exibir_relatorio_mensal(), exibir_alertas_ativos(), configurar_sistema()

#### É a "ponte de comunicação". Ela não faz cálculos e não salva arquivos diretamente; ela apenas "pergunta ao usuário", "lê a resposta" e "pede ao Gerenciador para executar".



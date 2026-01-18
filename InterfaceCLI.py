import os
from datetime import date

class InterfaceCLI:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador
        self.usuario_logado = None
        self.menu_ativo = True

    # =========================
    # CONTROLE GERAL
    # =========================

    def configurar_sistema(self):
        self.limpar_tela()
        print("=== CONFIGURAÇÃO DO SISTEMA ===")
        self.usuario_logado = input("Informe o nome do usuário: ")
        self.gerenciador.configurar(self.usuario_logado)

    def exibir_menu_principal(self):
        while self.menu_ativo:
            self.limpar_tela()
            print(f"Usuário: {self.usuario_logado}")
            print("\n=== MENU PRINCIPAL ===")
            print("1 - Cadastrar Categoria")
            print("2 - Cadastrar Lançamento")
            print("3 - Relatório Mensal")
            print("4 - Alertas Ativos")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.solicitar_dados_categoria()
            elif opcao == "2":
                self.solicitar_dados_lancamento()
            elif opcao == "3":
                self.exibir_relatorio_mensal()
            elif opcao == "4":
                self.exibir_alertas_ativos()
            elif opcao == "0":
                self.menu_ativo = False
            else:
                input("Opção inválida. Pressione ENTER para continuar.")

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")

    # =========================
    # ENTRADA DE DADOS
    # =========================

    def solicitar_dados_categoria(self):
        self.limpar_tela()
        print("=== CADASTRO DE CATEGORIA ===")

        nome = input("Nome da categoria: ")
        tipo = input("Tipo (Receita/Despesa): ")
        limite = input("Limite mensal (opcional): ")

        limite = float(limite) if limite else None

        self.gerenciador.criar_categoria(
            nome=nome,
            tipo=tipo,
            limite_mensal=limite
        )

        input("Categoria cadastrada com sucesso! Pressione ENTER.")

    def solicitar_dados_lancamento(self):
        self.limpar_tela()
        print("=== CADASTRO DE LANÇAMENTO ===")

        valor = float(input("Valor: "))
        categoria = input("Categoria: ")
        forma_pagamento = input("Forma de pagamento: ")
        status = input("Status (PAGO/PENDENTE): ")

        print("Data do lançamento:")
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        data_lancamento = date(ano, mes, dia)

        self.gerenciador.criar_lancamento(
            valor=valor,
            categoria_nome=categoria,
            data=data_lancamento,
            forma_pagamento=forma_pagamento,
            status=status
        )

        input("Lançamento registrado! Pressione ENTER.")

    # =========================
    # SAÍDA DE DADOS
    # =========================

    def exibir_relatorio_mensal(self):
        self.limpar_tela()
        print("=== RELATÓRIO MENSAL ===")

        relatorio = self.gerenciador.obter_relatorio_mensal()

        for linha in relatorio:
            print(linha)

        input("\nPressione ENTER para voltar ao menu.")

    def exibir_alertas_ativos(self):
        self.limpar_tela()
        print("=== ALERTAS ATIVOS ===")

        alertas = self.gerenciador.obter_alertas()

        if not alertas:
            print("Nenhum alerta ativo.")
        else:
            for alerta in alertas:
                print(f"- {alerta}")

        input("\nPressione ENTER para voltar ao menu.")

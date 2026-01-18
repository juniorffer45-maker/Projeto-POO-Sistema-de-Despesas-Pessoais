#Caso se opte por usa-la em vez de API

class InterfaceCLI:
    def __init__(self, chefe):
        self.chefe = chefe

    def menu(self):
        if not os.path.exists('settings.json'): self.chefe.configuracoes.configurar_inicial()
        
        while True:
            print(f"\n=== SISTEMA FINANCEIRO | META: {self.chefe.configuracoes.meta_economia_percentual}% ===")
            print("1. Categoria | 2. Receita | 3. Despesa | 4. Resumo | 0. Sair")
            op = input("Opção: ")
            
            if op == '1':
                n = input("Nome: "); t = input("Tipo (Receita/Despesa): ")
                self.chefe.cadastrar_categoria(n, t)
            elif op in ['2', '3']:
                try:
                    v = float(input("Valor: "))
                    c = input("Categoria: ")
                    d = input("Data (DD/MM/AAAA): ")
                    f = input("Forma: ")
                    self.chefe.adicionar_lancamento(v, c, d, f, "PAGO", Receita if op == '2' else Despesa)
                except Exception as e: print(f"Erro: {e}")
            elif op == '4':
                ch = input("Mês/Ano (MM-AAAA): ")
                o = self.chefe.orcamentos.get(ch)
                if o:
                    print(f"\nReceitas: R${o.calcular_total_receitas():.2f}")
                    print(f"Despesas: R${o.calcular_total_despesas():.2f}")
                    print(f"Saldo: R${o.calcular_saldo():.2f}")
                else: print("Mês não encontrado.")
            elif op == '0': break



if __name__ == "__main__":
    app = InterfaceCLI(GerenciadorFinanças())
    app.menu()

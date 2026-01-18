import json
import os
from datetime import date, datetime

class GerenciadorFinanças:
    def __init__(self):
        self.categorias = {}
        self.orcamentos = []
        self.alertas = []
        self.arquivo_dados = "dados_financeiros.json"
        self.carregar_dados()
        self.relatorios = Relatorios(self.orcamentos)

    def cadastrar_categoria(self, nome, tipo, limite=None, desc=""):
        self.categorias[nome] = Categoria(nome, tipo, limite, desc)
        self.salvar_dados()

    def adicionar_lancamento(self, valor, nome_cat, data_str, forma, status, tipo_classe):
        dt = datetime.strptime(data_str, "%d/%m/%Y").date()
        cat = self.categorias.get(nome_cat)
        if not cat: raise ValueError("Categoria não existe!")

        novo = tipo_classe(valor, cat, dt, forma, status)
        
        orc = self.relatorios.buscar_orcamento(dt.month, dt.year)
        if not orc:
            orc = OrcamentoMensal(dt.month, dt.year)
            self.orcamentos.append(orc)
        
        orc.adicionar_lancamento(novo)
        
        # Lógica de Alerta de Saldo Negativo
        if orc.calcular_saldo() < 0:
            self.alertas.append(Alerta("CRÍTICO", f"Saldo negativo em {dt.month}/{dt.year}", date.today()))
            
        self.salvar_dados()

    def salvar_dados(self):
        # Simplificação para exemplo de salvamento JSON
        dados = {
            "categorias": {n: {"tipo": c.tipo, "limite": c.limite_mensal} for n, c in self.categorias.items()}
        }
        with open(self.arquivo_dados, 'w') as f:
            json.dump(dados, f)

    def carregar_dados(self):
        if os.path.exists(self.arquivo_dados):
            with open(self.arquivo_dados, 'r') as f:
                dados = json.load(f)
                for n, c in dados.get("categorias", {}).items():
                    self.categorias[n] = Categoria(n, c['tipo'], c['limite'])



#CLASSE ALDEMIR FERREIRA
class Lançamento:

  def __init__(self, valor, categoria, data, forma_de_pagamento, status):
    self.valor = valor
    self.categoria = categoria
    self.data = data
    self.forma_de_pagamento = forma_de_pagamento
    self.status = status
    
  @property # Getter para o valor
  def valor(self):
    return self._valor
  
  @valor.setter # Setter para o valor
  def valor(self, novo_valor):
    if novo_valor <= 0:
      raise ValueError("O valor deve ser maior que 0")
    self._valor = float(novo_valor)

  @property # Getter para a data
  def data(self):
    return self._data

  @data.setter # Setter para a data
  def data(self, nova_data):
    if not isinstance(nova_data, date):
      raise TypeError("Data está no formato errado")
    self._data = nova_data

  @property # Getter para a forma_de_pagamento
  def forma_de_pagamento(self):
     return self._forma_de_pagamento
  
  @forma_de_pagamento.setter # Setter para a forma_de_pagamento
  def forma_de_pagamento(self, nova_forma):
      if not isinstance(nova_forma, str):
          raise TypeError("Forma de pagamento deve ser um texto (Ex: Pix, Dinheiro, Boleto, Cartão)")
      self._forma_de_pagamento = nova_forma

      if not nova_forma.strip():
          raise ValueError("Forma de pagamento não pode estar vazia")
      self._forma_de_pagamento= nova_forma

  @property # Getter para o status
  def status(self):
    return self._status
  
  @status.setter # Setter para o status
  def status(self, novo_status):
      status_ajustado = novo_status.upper().strip()
      permitidos = ["PENDENTE", "PAGO"]
      if status_ajustado not in permitidos:
          raise ValueError(f"Status inválido. Escolha entre: {permitidos}")
      self._status = status_ajustado

  def marcar_como_pago(self):
    self.status = "PAGO"

  def marcar_como_pendente(self):
    self.status = "PENDENTE"

  def esta_pago(self):
    return self.status == "PAGO"
  
  def __str__(self):
     return f"{self.data} - {self.categoria.nome} - R$ {self.valor:.2f}"
  
  def __repr__(self):
      return f"Lançamento(valor={self.valor}, categoria={self.categoria.nome}, data={self.data}"
  
  def __eq__(self, other):
     if not isinstance(other, Lançamento):
        return False

     return (self.valor == other.valor and
              self.categoria.nome == other.categoria.nome and
              self.data == other.data)

  def __lt__(self, other):
     return self.data < other.data
  
#CLASSE BEATRIZ BENIGNO
  
class Receita(Lançamento):
    def __init__(self, valor, categoria, data, forma_de_pagamento, status):
        super().__init__(valor, categoria, data, forma_de_pagamento, status)

class Despesa(Lançamento):
    def __init__(self, valor, categoria, data, forma_de_pagamento, status):
        super().__init__(valor, categoria, data, forma_de_pagamento, status)


#CLASSE ALDEMIR FERREIRA
class Categoria:

  def __init__(self, nome, tipo, limite_mensal=None, descricao=""):
    
    self.nome = nome
    self.tipo = tipo
    self.limite_mensal = limite_mensal
    self.descricao = descricao

  @property # Getter para o nome
  def nome(self):
    return self._nome

  @nome.setter # Setter para o nome
  def nome(self, novo_nome):
    if not novo_nome:
      raise ValueError("O nome da categoria não pode estar vazio")
    self._nome = novo_nome

  @property # Getter para o limite_mensal
  def limite_mensal(self):
    return self._limite_mensal

  @limite_mensal.setter # Setter para o limite_mensal
  def limite_mensal(self, novo_limite):
    if novo_limite is not None and novo_limite < 0:
      raise ValueError ("O limite mensal não pode ser negativo")
    self._limite_mensal = novo_limite


  def __str__(self):
    return self.nome
    

#CLASSE BEATRIZ BENIGNO

class OrcamentoMensal:
    def __init__(self, mes, ano):
        self.mes = mes
        self.ano = ano
        self.lancamentos = []

    @property
    def mes(self):
        return self._mes
    
    @mes.setter
    def mes(self, novo_mes):
        if novo_mes <1 or novo_mes > 12:
            raise ValueError("Mês deve estar entre 1 e 12")
        self._mes = novo_mes

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, novo_ano):
        if novo_ano <1940 or novo_ano > 2100:
            raise ValueError("Ano deve estar entre 1940 e 2100")
        self._ano = novo_ano

    def adicionar_lancamento(self, lancamento):
        self.lancamentos.append(lancamento)
    
    def calcular_total_receitas(self):
        total = 0
        for lancamento in self.lancamentos:
           if isinstance (lancamento, Receita):
               total += lancamento.valor
        return total
    
    def calcular_total_despesas(self):
        total = 0
        for lancamento in self.lancamentos:
           if isinstance (lancamento, Despesa):
               total += lancamento.valor
        return total
    
    def calcular_saldo(self):
       return self.calcular_total_receitas() - self.calcular_total_despesas()
    
    def verificar_alerta_saldo(self):
        saldo_atual = self.calcular_saldo()
        if saldo_atual < 0:
           msg = f"Alerta: Saldo negativo de R$ {saldo_atual:.2f} no mês {self.mes}/{self.ano}"
       
           novo_alerta = Alerta("Crítico", msg, date.today())

           return novo_alerta
    #Se estiver tudo bem
        return None

    def imprimir_extrato(self):
        print(f"\n--- Extrato Mês {self.mes}/{self.ano} ---")
        
        # Se a lista estiver vazia, avisa o usuário
        if not self.lancamentos:
            print("(Nenhum lançamento registrado ainda)")
            return

        # Se tiver coisas, imprime uma por uma
        for item in self.lancamentos:
            print(f"{item.data} | {item.categoria.nome} | R$ {item.valor:.2f}")
        
        print("-" * 30)
      

#CLASSE JOÃO PAULO
class Relatorios:
   def __init__(self, lista_orcamentos):
        self.lista_orcamentos = lista_orcamentos
       
   def buscar_orcamento(self, mes, ano):
         for orcamento in self.lista_orcamentos:
              if orcamento.mes == mes and orcamento.ano == ano:
                return orcamento
         
         return None
   
   def total_categoria(self, mes, ano):
        #busca o orçamento do mês e ano especificados
        orcamento = self.buscar_orcamento(mes, ano)
        #se não achou o orçamento, retorna dicionário vazio
        if orcamento is None:
            return {}
      
        totais = {}

        for lancamento in orcamento.lancamentos:
             if isinstance(lancamento, Despesa):
            #Pega o nome para saber em qual "caixa" guardar
                 nome_categoria = lancamento.categoria.nome
                 valor =  lancamento.valor

                 if nome_categoria in totais:
                    totais[nome_categoria] += valor
                 else:
                    totais[nome_categoria] = valor

        return totais
   
   def despesas_formapagamento(self, mes, ano):
        orcamento = self.buscar_orcamento(mes, ano)
        if orcamento is None:
            return {}
        
        totais = {}

        for lancamento in orcamento.lancamentos:
             if isinstance(lancamento, Despesa):
                 forma = lancamento.forma_de_pagamento
                 valor = lancamento.valor

                 if forma in totais:
                    totais[forma] += valor
                 else:
                    totais[forma] = valor

        return totais
   
   def calcular_percentual_cat(self, mes, ano):
        orcamento = self.buscar_orcamento(mes, ano)

        totais = self.total_categoria(mes, ano)
        total_despesas = sum(totais.values())
        if total_despesas == 0:
           return {}

        percentuais = {}

        for categoria, valor in totais.items(): 
           calculo = (valor / total_despesas) * 100
           percentuais[categoria] = calculo

        return percentuais
     
   def mes_economico(self):
        melhor_mes = None
        menor_gasto = float('inf') #cria um número infinito para comparar
        #loop em todos os orçamentos
        for orcamento in self.lista_orcamentos:
                total_despesas = orcamento.calcular_total_despesas()
                if total_despesas < menor_gasto:
                    menor_gasto = total_despesas
                    melhor_mes = (orcamento.mes, orcamento.ano)

        return melhor_mes, menor_gasto

   def _subtrair_meses(self, mes, ano, quantidade_meses):
        # Transforma os meses em algo mutável
        novo_mes = mes
        novo_ano = ano
        
        # Loop para voltar 1 mês de cada vez
        for _ in range(quantidade_meses):
            novo_mes -= 1 # Diminui o mês
            
            if novo_mes == 0:
                novo_mes = 12 # Volta para Dezembro
                novo_ano -= 1 # Volta um ano
        
        return novo_mes, novo_ano

   def comparar_ultimos_3meses(self, mes_atual, ano_atual):
    
    resultados = []
   
    for i in range(3):
            mes_alvo, ano_alvo = self._subtrair_meses(mes_atual, ano_atual, i)
            orcamento = self.buscar_orcamento(mes_alvo, ano_alvo)

            if orcamento:
               total = orcamento.calcular_total_despesas()
            else:
               total = 0

            resultados.append((mes_alvo, ano_alvo, total))
        
    return resultados

#CLASSE ANA KARLA

class Alerta:
    def __init__(self, tipo, mensagem, data, lancamento=None):
        self.tipo = tipo
        self.mensagem = mensagem
        self.data = data
        self.lancamento = lancamento

    def __str__(self):
        return f"[{self.data}] {self.tipo.upper()}: {self.mensagem}"

#CLASSE MARIA IVANILDA

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
          


#CLASSE MARIA IVANILDA

class InterfaceCLI:
    def __init__(self):
        self.gerente = GerenciadorFinanças()

    def exibir_menu(self):
        while True:
            print("\n" + "="*30)
            print("   GERENCIADOR FINANCEIRO ")
            print("="*30)
            if self.gerente.alertas:
                print(self.gerente.alertas[-1])
            
            print("1. Cadastrar Categoria")
            print("2. Adicionar Receita")
            print("3. Adicionar Despesa")
            print("4. Ver Saldo do Mês")
            print("0. Sair")
            
            op = input("\nEscolha uma opção: ")

            if op == '1':
                nome = input("Nome: ")
                tipo = input("Tipo (Receita/Despesa): ")
                limite = input("Limite (opcional): ")
                self.gerente.cadastrar_categoria(nome, tipo, float(limite) if limite else None)
                print("Categoria cadastrada!")

            elif op in ['2', '3']:
                try:
                    v = float(input("Valor: R$ "))
                    c = input("Categoria: ")
                    d = input("Data (DD/MM/AAAA): ")
                    f = input("Forma de Pagamento: ")
                    tipo = Receita if op == '2' else Despesa
                    self.gerente.adicionar_lancamento(v, c, d, f, "PAGO", tipo)
                    print("Lançamento realizado!")
                except Exception as e:
                    print(f"❌ Erro: {e}")

            elif op == '4':
                m = int(input("Mês (1-12): "))
                a = int(input("Ano (AAAA): "))
                orc = self.gerente.relatorios.buscar_orcamento(m, a)
                if orc:
                    print(f"\nResumo {m}/{a}:")
                    print(f"Saldo: R$ {orc.calcular_saldo():.2f}")
                else:
                    print("Nenhum dado encontrado.")

            elif op == '0':
                print("Até logo!")
                break



if __name__ == "__main__":
    InterfaceCLI().exibir_menu()


import json
import os
from datetime import date, datetime

#CLASSE JUNIOR FERREIRA
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
     return self.forma_de_pagamento
  
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
    return self.status
  
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


#CLASSE JUNIOR FERREIRA
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
    
    def alerta_saldo_negativo(self):
       saldo_atual = self.calcular_saldo()
       if saldo_atual < 0:
          return "Alerta: Seu saldo está negativo!"
       else:
          return "Saldo está positivo."

#CLASSE JOÃO PAULO

class RelatoriosEstatisticas:
    def __init__(self, lista_orcamentos):
        """
        Inicializa com uma lista de objetos OrcamentoMensal.
        :param lista_orcamentos: list[OrcamentoMensal]
        """
        self.orcamentos = lista_orcamentos

    def _buscar_orcamento(self, mes, ano):
        """Método auxiliar para encontrar o orçamento de um mês/ano específico."""
        for orc in self.orcamentos:
            if orc.mes == mes and orc.ano == ano:
                return orc
        return None

    def _subtrair_meses(self, mes, ano, n):
        """Método auxiliar para calcular meses anteriores (ex: para comparativos)."""
        mes_result = mes
        ano_result = ano
        for _ in range(n):
            mes_result -= 1
            if mes_result == 0:
                mes_result = 12
                ano_result -= 1
        return mes_result, ano_result

    def total_por_categoria(self, mes, ano):
        """Calcula o total de despesas agrupadas por categoria (dados para gráfico de pizza)."""
        orcamento = self._buscar_orcamento(mes, ano)
        if not orcamento:
            return {}
        
        totais = {}
        for despesa in orcamento.despesas:
            cat = despesa.categoria
            totais[cat] = totais.get(cat, 0) + despesa.valor
        return totais

    def despesas_por_forma_pagamento(self, mes, ano):
        """Agrupa despesas por forma de pagamento (crédito, débito, pix)."""
        orcamento = self._buscar_orcamento(mes, ano)
        if not orcamento:
            return {}
        
        pagamentos = {}
        for despesa in orcamento.despesas:
            forma = despesa.forma_pagamento
            pagamentos[forma] = pagamentos.get(forma, 0) + despesa.valor
        return pagamentos

    def calcular_percentuais_categoria(self, mes, ano):
        """Calcula a porcentagem que cada categoria representa no total gasto."""
        totais = self.total_por_categoria(mes, ano)
        total_geral = sum(totais.values())
        
        if total_geral == 0:
            return {}
        
        percentuais = {cat: (valor / total_geral) * 100 for cat, valor in totais.items()}
        return percentuais

    def mes_mais_economico(self):
        """Identifica o mês com o menor total de despesas entre os orçamentos cadastrados."""
        if not self.orcamentos:
            return None
        
        # Encontra o orçamento com a menor soma de despesas
        melhor_orcamento = min(self.orcamentos, key=lambda o: sum(d.valor for d in o.despesas))
        return {"mes": melhor_melhor_orcamento.mes, "ano": melhor_orcamento.ano}

    def comparativo_ultimos_3_meses(self, mes_atual, ano_atual):
        """Cria um comparativo de gastos dos últimos 3 meses (incluindo o atual)."""
        comparativo = {}
        for i in range(3):
            m, a = self._subtrair_meses(mes_atual + 1, ano_atual, i + 1) # Ajuste lógico
            orcamento = self._buscar_orcamento(m, a)
            if orcamento:
                comparativo[f"{m}/{a}"] = sum(d.valor for d in orcamento.despesas)
            else:
                comparativo[f"{m}/{a}"] = 0
        return comparativo

#CLASSE MARIA IVANILDA

class Configuracoes:
    def __init__(self, filename="settings.json"):
        self.filename = filename

        # Configurações padrão
        self.alerta_alto_gasto = 500.0               # valor em reais
        self.meses_comparativo = 3                   # quantidade de meses
        self.meta_economia_percentual = 10.0         # percentual (%)

        # Se existir arquivo, pode ser carregado futuramente
        self.validar_parametros()
   
    def validar_parametros(self):
        if self.alerta_alto_gasto <= 0:
            raise ValueError("O alerta de alto gasto deve ser maior que zero.")

        if self.meses_comparativo <= 0:
            raise ValueError("Meses de comparativo deve ser maior que zero.")

        if not (0 <= self.meta_economia_percentual <= 100):
            raise ValueError("Meta de economia deve estar entre 0 e 100%.")

    def alterar_meta_economia(self, nova_meta):
        if not isinstance(nova_meta, (int, float)):
            raise TypeError("A meta de economia deve ser numérica.")

        if nova_meta < 0 or nova_meta > 100:
            raise ValueError("A meta de economia deve estar entre 0 e 100%.")

        self.meta_economia_percentual = float(nova_meta)



# ÁREA DE TESTES 

if __name__ == "__main__":
    print("\n INICIANDO SISTEMA FINANCEIRO")

    # 1. CRIANDO AS CATEGORIAS
    # Precisamos delas antes de criar os lançamentos
    cat_salario = Categoria("Salário Mensal", "Receita")
    cat_aluguel = Categoria("Aluguel/Moradia", "Despesa")
    cat_lazer = Categoria("Lazer e Cinema", "Despesa")

    # 2. CRIANDO O ORÇAMENTO DO MÊS
    # Vamos simular Janeiro de 2025
    meu_orcamento = OrcamentoMensal(1, 2025)
    print(f"\n Orçamento criado para: {meu_orcamento.mes}/{meu_orcamento.ano}")

    # 3. CRIANDO OS LANÇAMENTOS
    # Ordem: Valor, Categoria, Data, Forma Pagamento, Status

    # Uma Receita (Entrou dinheiro)
    salario = Receita(5000.00, cat_salario, date(2025, 1, 5), "PIX", "PAGO")

    # Uma Despesa (Saiu dinheiro - Aluguel)
    aluguel = Despesa(1200.00, cat_aluguel, date(2025, 1, 10), "Boleto", "PAGO")

    # Outra Despesa (Cinema - Ainda não pagou)
    cinema = Despesa(50.00, cat_lazer, date(2025, 1, 20), "Crédito", "PENDENTE")

    # 4. ADICIONANDO TUDO NA "CAIXA" DO ORÇAMENTO
    meu_orcamento.adicionar_lancamento(salario)
    meu_orcamento.adicionar_lancamento(aluguel)
    meu_orcamento.adicionar_lancamento(cinema)

    print(f"\n Lançamentos adicionados: {len(meu_orcamento.lancamentos)}")

    # 5. TESTANDO A VISUALIZAÇÃO (__str__)
    print("\n - Detalhe dos Lançamentos -")
    for item in meu_orcamento.lancamentos:
        print(item)

    # 6. RELATÓRIO FINAL (Cálculos)
    print("\n - RESUMO FINANCEIRO -")
    
    total_receitas = meu_orcamento.calcular_total_receitas()
    total_despesas = meu_orcamento.calcular_total_despesas()
    saldo_final = meu_orcamento.calcular_saldo()
    
    print(f"Total Receitas:  R$ {total_receitas:.2f}")
    print(f"Total Despesas:  R$ {total_despesas:.2f}")
    print(f"---------------------------")
    print(f"SALDO FINAL:     R$ {saldo_final:.2f}")
    
    # 7. VERIFICANDO O ALERTA
    print(f"Situação: {meu_orcamento.alerta_saldo_negativo()}")

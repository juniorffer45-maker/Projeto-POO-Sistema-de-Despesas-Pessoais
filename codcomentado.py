from datetime import date

#CLASSE JUNIOR FERREIRA

#ssa é a classe "Mãe". Ela define o que todo lançamento financeiro tem.
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
  
  # O @valor.setter define as regras para MODIFICAR o valor.
  # Quando alguém fizer 'objeto.valor = 50', este método roda.
  
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
      self.forma_de_pagamento = nova_forma

  @property # Getter para o status
  def status(self):
    return self.status
  
  @status.setter # Setter para o status
  def status(self, novo_status):
      status_ajustado = novo_status.upper().strip() #Padronização: Transforma tudo em maiúsculo e tira espaços laterais.

      permitidos = ["PENDENTE", "PAGO"] #Definição das regras: Só aceitamos estes dois status.
    
    # Validação: Se o status não estiver na lista de permitidos, dá erro.
      if status_ajustado not in permitidos:
          raise ValueError(f"Status inválido. Escolha entre: {permitidos}")
      self._status = status_ajustado

## Métodos simples para alterar o estado do objeto sem precisar digitar a string manualmente.
  def marcar_como_pago(self):
    self.status = "PAGO"

  def marcar_como_pendente(self):
    self.status = "PENDENTE"

  def esta_pago(self):
    return self.status == "PAGO"
  
#Como o objeto aparece para o USUÁRIO (ex: num print).
  def __str__(self): 
     return f"{self.data} - {self.categoria.nome} - R$ {self.valor:.2f}"

#Como o objeto aparece para o PROGRAMADOR (ex: numa lista de depuração).
  def __repr__(self):
      return f"Lançamento(valor={self.valor}, categoria={self.categoria.nome}, data={self.data}"

#Define como comparar se dois lançamentos são IGUAIS (usando ==).  
  def __eq__(self, other):
     # Primeiro checa se o "outro" é um Lançamento. Se não for, impossível ser igual.
     if not isinstance(other, Lançamento):
        return False
     
#Compara valor, nome da categoria e data. Se tudo bater, são iguais.
     return (self.valor == other.valor and
              self.categoria.nome == other.categoria.nome and
              self.data == other.data)

#Define quem é MENOR que o outro. Usado para ordenar (sort) por data.
  def __lt__(self, other):
     return self.data < other.data

  def __add__(self, other):
        # Verifica se são do mesmo tipo (Ex: Receita com Receita)
        # type(self) pega a classe exata (Receita ou Despesa)
        if type(self) != type(other):
            raise TypeError("Não é possível somar Receita com Despesa")
            
        #Retorna a soma dos valores (float)
        return self.valor + other.valor
  
#CLASSES FILHAS (Herança)
#A Receita e a Despesa herdam tudo de Lançamento. A vantagem disso é que se a gente precisar mudar como a 'Data' funciona, muda só na mãe e as filhas já aprendem automaticamente. 
#Isso é Reaproveitamento de Código
  
class Receita(Lançamento):
    def __init__(self, valor, categoria, data, forma_de_pagamento, status):
        super().__init__(valor, categoria, data, forma_de_pagamento, status)

class Despesa(Lançamento):
    def __init__(self, valor, categoria, data, forma_de_pagamento, status):
        super().__init__(valor, categoria, data, forma_de_pagamento, status)


#CLASSE JUNIOR FERREIRA
#Serve para rotular os lançamentos (Ex: Alimentação, Salário).

class Categoria:

  def __init__(self, nome, tipo, limite_mensal=None, descricao=""):
    #Inicializa variáveis internas como nulas primeiro
    self.nome = None
    self._limite_mensal = None
    
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
#Essa classe agrupa e calcula tudo. É a "Caixa" onde guardamos os lançamentos.

class OrcamentoMensal:
    def __init__(self, mes, ano):
        self.mes = mes
        self.ano = ano
        self.lancamentos = [] # Lista vazia para guardar os lançamentos

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

#Método para receber um lançamento e guardar na lista.
    def adicionar_lancamento(self, lancamento):
        self.lancamentos.append(lancamento)
    
    def calcular_total_receitas(self):
        total = 0
        for lancamento in self.lancamentos:
           #isinstance verifica: "Esse item da lista foi criado pelo obj Receita?"
           if isinstance (lancamento, Receita):
               total += lancamento.valor
        return total
    
    def calcular_total_despesas(self):
        total = 0
        for lancamento in self.lancamentos:
           if isinstance (lancamento, Despesa): #o mesmo que acima, mas para Despesa
               total += lancamento.valor
        return total
    
# Faz a matemática final: Ganhou - Gastou.
    def calcular_saldo(self):
       # Reaproveita os métodos que já criamos acima (self.metodo()).
       return self.calcular_total_receitas() - self.calcular_total_despesas()
    
# Método simples para dar feedback ao usuário sobre a situação financeira.
    def alerta_saldo_negativo(self):
       saldo_atual = self.calcular_saldo()
       if saldo_atual < 0:
          return "Alerta: Seu saldo está negativo!"
       else:
          return "Saldo está positivo."

'''
#COMENTARIOS EXPLICATIVOS

Usamos Herança para Receita e Despesa aproveitarem a estrutura de Lançamento. 
Usamos Encapsulamento com Setters para validar os dados e impedir erros bobos (como valor negativo). 
criamos uma classe Orçamento que gerencia tudo isso numa lista e calcula o saldo dinamicamente.

P: "Por que não colocou tudo numa classe só?"
R: "Porque ficaria bagunçado (baixa coesão). Se o sistema crescer, separar as coisas facilita a manutenção. Cada classe cuida do seu quadrado."

P: "O que é esse super()?"
R: "É a forma da classe filha chamar o __init__ da mãe. É como dizer: 'Mãe, faz o cadastro básico aí que eu assumo daqui'."

P: "Para que serve o isinstance?"
R: "Serve para checar o tipo do objeto. É assim que o Orçamento sabe se tem que somar (Receita) ou considerar como gasto (Despesa)."

P: Por que usar raise ValueError nos Setters em vez de só dar um print('Erro')?
R: Porque print só mostra texto na tela, mas o programa continua rodando errado. 
O raise interrompe o programa imediatamente (Fail Fast). 
É melhor o sistema parar e avisar o erro grave do que deixar passar um valor negativo que vai estragar todo o cálculo financeiro lá na frente.


'''

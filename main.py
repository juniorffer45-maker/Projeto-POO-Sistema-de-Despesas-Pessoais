class Categoria:

  def __init__(self, nome, tipo, limite_mensal=None, descricao="")
    self.nome = None
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
  def limite_mensal(self)
    return self._limite_mensal

  @limite_mensal.setter # Setter para o limite_mensal
  def limite_mensal(self, novo_limite):
    if novo_limite is not None and novo_limite < 0:
      raise ValueError ("O limite mensal não pode ser negativo")
    self._limite_mensal = novo_limite
    
  def __str__(self):
      return self.nome

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
    if not novo_valor and novo_valor < 0:
      raise ValueError("O valor não pode estar vazio ou ser menor que 0")
    self._valor = novo_valor

  @property # Getter para a data
  def data(self):
    return self._data

  @data.setter # Setter para a data
  def data(self, nova_data):
    if not isinstance(nova_data, date):
      raise TypeError("Data está no formato errado")
    self._data = nova_data

  def marcar_como_pago(self):
    self.status = "PAGO"

  def marcar_como_pendente(self):
    self.status = "PENDENTE"

  def esta_pago(self):
    return self.status == "PAGO"

  
  

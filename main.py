class Categoria:

  def __init__(self, nome, tipo, limite_mensal = None, descricao = "")
    self.nome = none
    self.tipo = tipo
    self.limite_mensal = limite_mensal
    self.descricao = descricao

  @property # Getter para o nome
  def nome(self):
    return self._nome

  @nome.setter # Setter para o nome
  def nome(self, novo_nome):
    if not novo_nome:
      print("O nome não pode estar vazio")
    self._nome = novo_nome

  @property # Getter para o limite_mensal
  def limite_mensal(self)
    return self._limite_mensal

  @limite_mensal.setter # Setter para o limite_mensal
  def limite_mensal(self, novo_limite)
    if limite_mensal_novo is not None and novo_limite < 0:
      print("O valor não pode ser negativo")
    self._limite_mensal = novo_limite

  def to_dict(self):
    pass


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
      print("O valor não pode estar vazio ou ser menor que 0")
    self._valor = novo_valor

  @property # Getter para a data
  def data(self):
    return self._data

  @data.setter # Setter para a data
  def data(self, nova_data):
    if not isinstance(nova_data, date):
      print("Data esta no formato errado")
    self._data = nova_data

  def __str__(self):
    pass

  def __repr__(self):
    pass
    
  def __eq__(self):
    pass

  def __it__(self):
    pass

  def add(self, outro):
    pass

  def to_dict(self):
    pass

  def marcar_como_pago(self):
    self.status = "PAGO"

  def marcar_como_pendente(self):
    self.status = "PENDENTE"

  def esta_pago(self):
    return self.status == "PAGO"

  
  

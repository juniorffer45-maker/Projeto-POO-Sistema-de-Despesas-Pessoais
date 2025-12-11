# Projeto-POO-Sistema-de-Despesas-Pessoais

## Equipe - Grupo de Programação UFCA

## Integrantes da Equipe
##### -- Beatriz Benigno de Vasconcelos(2025013076) -  
##### -- Aldemir Ferreira da Silva Junior(2025012892) -
##### -- Ana Karla Pontes de Souza(2025012954) -
##### -- João Paulo Lima David(2025013441) - 
##### -- Maria Ivanilda Irineu de Lima(2025013610) - 

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
##### Class: 
##### Atributos: 
##### Metodos:
-
##### Class: 
##### Atributos: 
##### Metodos:
-
##### Class: 
##### Atributos: 
##### Metodos:
-
##### Class: 
##### Atributos: 
##### Metodos:
-
##### Class: 
##### Atributos: 
##### Metodos:
-
##### Class: 
##### Atributos: 
##### Metodos:

class Configurações:
  def __init__(self, file_name = 'settings.json'):
    self.file_name = file_name
    self.alerta_alto_gasto = alerta_alto_gasto
    self.meses_comparativo = meses_comparativo
    self.meta_economia_percentual = meta_economia_percentual 

  def validar_parametros(self): # Garante que as configurações façam sentido matemático
    if self.meta_economia_percentual < 0 or self.meta_economia_percentual > 100:
            print("Erro: A meta de economia deve estar entre 0 e 100%.")
            return False
        if self.alerta_alto_gasto < 0:
            print("Erro: O valor de alerta não pode ser negativo.")
            return False
        return True    

  def alterar_meta_de_economia(self, nova_meta): # Método específico para atualizar a meta com validação
    valor_antigo = self.meta_economia_percentual
        self.meta_economia_percentual = float(nova_meta)
        
        if self.validar_parametros():
            self.salvar_configuracoes()
            print(f"Meta de economia atualizada: {valor_antigo}% -> {nova_meta}%")
        else:
            self.meta_economia_percentual = valor_antigo # Reverte em caso de erro
    

  def salvar_configuracoes(self): # Salva os atributos atuais em um arquivo JSON separado
    dados = {
            "alerta_alto_gasto": self.alerta_alto_gasto,
            "meses_comparativo": self.meses_comparativo,
            "meta_economia_percentual": self.meta_economia_percentual
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4)
          
  def carregar_configuracoes(self): # Lê o arquivo de texto e atualiza os atributos da classe.
    pass
      
  

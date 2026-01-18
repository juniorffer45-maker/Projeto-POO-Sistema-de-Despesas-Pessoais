class Configuracoes:
    def __init__(self, filename="settings.json"):
        self.filename = filename

        # Configurações padrão
        self.alerta_alto_gasto = 500.0               # valor em reais
        self.meses_comparativo = 3                   # quantidade de meses
        self.meta_economia_percentual = 10.0         # percentual (%)

        # Se existir arquivo, pode ser carregado futuramente
        self.validar_parametros()

    # =========================
    # VALIDAÇÕES
    # =========================

    def validar_parametros(self):
        if self.alerta_alto_gasto <= 0:
            raise ValueError("O alerta de alto gasto deve ser maior que zero.")

        if self.meses_comparativo <= 0:
            raise ValueError("Meses de comparativo deve ser maior que zero.")

        if not (0 <= self.meta_economia_percentual <= 100):
            raise ValueError("Meta de economia deve estar entre 0 e 100%.")

    # =========================
    # ALTERAÇÕES DE CONFIGURAÇÃO
    # =========================

    def alterar_meta_economia(self, nova_meta):
        if not isinstance(nova_meta, (int, float)):
            raise TypeError("A meta de economia deve ser numérica.")

        if nova_meta < 0 or nova_meta > 100:
            raise ValueError("A meta de economia deve estar entre 0 e 100%.")

        self.meta_economia_percentual = float(nova_meta)

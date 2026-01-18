class RelatoriosEstatisticas:
    def __init__(self, orcamentos):
        self.orcamentos = orcamentos

    def total_por_categoria(self, chave):
        orc = self.orcamentos.get(chave)
        if not orc: return {}
        res = {}
        for l in orc.lancamentos:
            if isinstance(l, Despesa):
                res[l.categoria.nome] = res.get(l.categoria.nome, 0) + l.valor
        return res

    def mes_mais_economico(self):
        if not self.orcamentos: return "N/A"
        melhor = min(self.orcamentos.values(), key=lambda o: o.calcular_total_despesas())
        return f"{melhor.mes:02d}/{melhor.ano}"

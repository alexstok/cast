# financeiro/financeiro.py
from datetime import datetime, timedelta

class Financeiro:
    def __init__(self, prazo_vencimento, servidor):
        self.prazo_vencimento = prazo_vencimento
        self.servidor = servidor
        self.calcular_data_vencimento()
        self.calcular_status()
        self.alerta_vencimento = self.calcular_alerta_vencimento()
        self.custo_total = self.calcular_custo()  # Renomeie para evitar conflitos
        self.valor_pago = 0

    def calcular_data_vencimento(self):
        self.data_vencimento = datetime.now() + timedelta(days=self.prazo_vencimento * 30)

    def calcular_status(self):
        hoje = datetime.now()
        self.dias_restantes = (self.data_vencimento - hoje).days
        if self.dias_restantes <= 0:
            self.status = "VENCIDO"
        elif self.dias_restantes < 5:
            self.status = "VENCER"
        elif self.dias_restantes <= 6:
            self.status = "ativo"
        else:
            self.status = "ativo"

    def calcular_alerta_vencimento(self):
        alerta_data = self.data_vencimento - timedelta(days=3)
        return alerta_data

    def calcular_custo(self):
        if self.servidor == "Blaze":
            return 10.00
        elif self.servidor == "Multz":
            return 5.00
        else:
            return 0.00

    def calcular_lucro(self):
        return self.valor_pago - self.custo


# cadastro/cadastro.py
from datetime import datetime, timedelta

class CadastroCliente:
    def __init__(self, nome, whatsapp, tipo, servidor, prazo_vencimento):
        self.nome = nome
        self.whatsapp = whatsapp
        self.tipo = tipo
        self.servidor = servidor
        self.data_criacao = datetime.now()
        self.prazo_vencimento = prazo_vencimento
        self.calcular_data_vencimento()
        self.calcular_dias_restantes()
        self.status = self.calcular_status()
        self.alerta_vencimento = self.calcular_alerta_vencimento()
        self.status_pagamento = "Teste"  # ou "PAGO"
        self.custo = self.calcular_custo()
        self.valor_pago = 0

    def calcular_data_vencimento(self):
        self.data_vencimento = self.data_criacao + timedelta(days=self.prazo_vencimento * 30)

    def calcular_dias_restantes(self):
        hoje = datetime.now()
        self.dias_restantes = (self.data_vencimento - hoje).days

    def calcular_status(self):
        if self.dias_restantes <= 0:
            return "VENCIDO"
        elif self.dias_restantes < 5:
            return "VENCER"
        elif self.dias_restantes <= 6:
            return "ativo"
        else:
            return "ativo"

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

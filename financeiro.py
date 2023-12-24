from datetime import datetime, timedelta

class Financeiro:
    def __init__(self, prazo_vencimento, custo):
        self.prazo_vencimento = prazo_vencimento
        self.alerta_vencimento = 3
        self.custo = custo
        self.valor_pago = 0.00

    def calcular_lucro(self):
        return self.valor_pago - self.custo

    def calcular_dias_restantes(self):
        data_vencimento = datetime.today() + timedelta(days=self.prazo_vencimento)
        dias_restantes = (data_vencimento - datetime.today()).days
        return dias_restantes

    def alerta_vencimento(self):
        dias_restantes = self.calcular_dias_restantes()
        if dias_restantes <= 0:
            return "Vencido"
        elif dias_restantes == 1:
            return "Vence amanhã"
        elif dias_restantes <= 5:
            return "Vencer"
        elif dias_restantes > 6:
            return "Ativo"

    def alerta_vencimento_3dias_antes(self):
        dias_restantes = self.calcular_dias_restantes()
        return dias_restantes == (self.alerta_vencimento - 3)

    def mostrar_informacoes(self):
        print(f"Prazo de Vencimento: {self.prazo_vencimento} dias")
        print(f"Dias Restantes: {self.calcular_dias_restantes()} dias")
        print(f"Status: {self.alerta_vencimento()}")
        print(f"Custo: R$ {self.custo}")
        print(f"Valor Pago: R$ {self.valor_pago}")
        print(f"Lucro: R$ {self.calcular_lucro()}")

# Exemplo de uso
financeiro1 = Financeiro(30, 10.00)
financeiro1.mostrar_informacoes()

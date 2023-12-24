from datetime import datetime, timedelta

class CadastroCliente:
    def __init__(self, nome, numero_whatsapp, tipo, servidor):
        self.nome = nome
        self.numero_whatsapp = numero_whatsapp
        self.tipo = tipo
        self.servidor = servidor
        self.data_criacao = datetime.today()
        self.prazo_vencimento = 30
        self.alerta_vencimento = 3
        self.status = "Ativo"
        self.custo = 10.00 if servidor == "Blaze" else 5.00
        self.valor_pago = 0.00

    def calcular_dias_restantes(self):
        data_vencimento = self.data_criacao + timedelta(days=self.prazo_vencimento)
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
        print(f"Nome: {self.nome}")
        print(f"Número do WhatsApp: {self.numero_whatsapp}")
        print(f"Tipo: {self.tipo}")
        print(f"Servidor: {self.servidor}")
        print(f"Data de Criação: {self.data_criacao.strftime('%d/%m/%Y')}")
        print(f"Prazo de Vencimento: {self.prazo_vencimento} dias")
        print(f"Dias Restantes: {self.calcular_dias_restantes()} dias")
        print(f"Status: {self.alerta_vencimento()}")
        print(f"Custo: R$ {self.custo}")
        print(f"Valor Pago: R$ {self.valor_pago}")

# Exemplo de uso
cliente1 = CadastroCliente("Cliente 1", "123456789", "IP", "Blaze")
cliente1.mostrar_informacoes()
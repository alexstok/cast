# main.py
from cadastro.cadastro import CadastroCliente
from financeiro.financeiro import Financeiro

# Exemplo de uso
cliente1 = CadastroCliente("Cliente1", "123456789", "IP", "Blaze", 3)
financeiro1 = Financeiro(3, cliente1.servidor)



print("Cadastro Cliente:")
print(f"Nome: {cliente1.nome}")
print(f"Número do WhatsApp: {cliente1.whatsapp}")
print(f"Tipo: {cliente1.tipo}")
print(f"Servidor: {cliente1.servidor}")
print(f"Data de Criação: {cliente1.data_criacao}")
print(f"Prazo de Vencimento (meses): {cliente1.prazo_vencimento}")
print(f"Data de Vencimento: {cliente1.data_vencimento}")
print(f"Dias Restantes: {cliente1.dias_restantes}")
print(f"Status: {cliente1.status}")
print(f"Alerta de Vencimento: {cliente1.alerta_vencimento}")
print(f"Status de Pagamento: {cliente1.status_pagamento}")
print(f"Custo: R${cliente1.custo}")
print(f"Valor Pago: R${cliente1.valor_pago}")

print("\nFinanceiro:")
print(f"Prazo de Vencimento (meses): {financeiro1.prazo_vencimento}")
print(f"Data de Vencimento: {financeiro1.data_vencimento}")
print(f"Dias Restantes: {financeiro1.dias_restantes}")
print(f"Status: {financeiro1.status}")
print(f"Alerta de Vencimento: {financeiro1.alerta_vencimento}")
print(f"Custo: R${financeiro1.custo_total}")  # Altere de custo para custo_total
print(f"Lucro: R${financeiro1.calcular_lucro()}")

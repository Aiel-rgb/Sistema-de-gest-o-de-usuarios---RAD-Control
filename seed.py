import random
from faker import Faker
from database import BancoRAD
from datetime import date, timedelta

fake = Faker('pt_BR')

tipos = ["Dúvida", "Entrega", "Correção", "Orientação", "Reisão", "Outro"]
prioridades = ["Baixa", "Média", "Alta"]
status_list = ["Aberto", "Em andamento", "Concluído", "Cancelado"]

banco = BancoRAD()
banco.conectar()

for i in range(20):
    nome = fake.name()
    matricula = fake.bothify("20######")
    tipo = random.choice(tipos)
    prioridade = random.choice(prioridades)
    status = random.choice(status_list)
    descricao = fake.sentence(nb_words=10)
    prazo = date.today() + timedelta(days=random.randint(1,30))

    banco.inserir(nome,matricula,tipo,prioridade,status,descricao,prazo)
    print(f"Inserindo: {nome}...")

print("Registros inseridos com sucesso")
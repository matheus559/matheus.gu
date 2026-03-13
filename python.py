# Duas listas separadas
alunos = ["Ana", "Bruno", "Carla", "Diego"]
notas = [8.5, 7.2, 9.8, 6.5]

print("--- Relatório de Notas ---")

# 1. zip() junta as duas listas em pares
# 2. enumerate() cria um índice para cada par
for i, (nome, nota) in enumerate(zip(alunos, notas), start=1):
    print(f"{i}. {nome}: {nota}")

# 3. max() encontra a maior nota
maior_nota = max(notas)

# 4. round() arredonda um cálculo (ex: média)
media = sum(notas) / len(notas)
media_formatada = round(media, 2)

print("-" * 25)
print(f"Média da turma: {media_formatada}")
print(f"A maior nota foi: {maior_nota}")

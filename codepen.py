nome = input("Qual é seu nome? ")

print("Olá, " + nome + "! Bem-vindo ao Python.")


numero1 = int(input("me fale um número"))

numero2 = int(input("me fale outro numero"))

resultado = (numero1 + numero2)

print(resultado)


# Programa 1 - Par ou Ímpar

def verificar_par_ou_impar():
    try:
        numero = int(input("Informe um número: "))
        if numero % 2 == 0:
            return True  # Número par
        else:
            return False  # Número ímpar
    except ValueError:
        return "Valor inválido! Por favor, informe um número inteiro."

# Executar a função
print(verificar_par_ou_impar())


# Programa 2 - Can You Drive?

def verificar_idade():
    try:
        idade = int(input("Informe sua idade: "))
        if idade < 0:
            return "Idade inválida! Informe um número positivo."
        elif idade < 18:
            return "Você é menor de idade."
        elif 18 <= idade <= 59:
            return "Você é adulto."
        else:
            return "Você é idoso."
    except ValueError:
        return "Valor inválido! Por favor, informe um número válido para a idade."

# Executar a função
print(verificar_idade())


#No caps please (pare de gritar!)
frase = input("Fale me uma frase")

frase_minuscula = frase.lower()

print(frase_minuscula)


#fale devagar
frase = input("Fale uma frase")

frase_com_reticencias = frase.replace(" ", "...")

print(frase_com_reticencias)


def dolares_para_float(d):
    # Remove o símbolo "$" e converte o valor restante para float
    return float(d.replace('$', ''))

def percentual_para_float(p):
    # Remove o símbolo "%" e converte o valor restante para float e divide por 100
    return float(p.replace('%', '')) / 100

dolares = dolares_para_float(input("Quanto custou a refeição? "))
percentual = percentual_para_float(input("Qual percentual você gostaria de deixar de gorjeta? "))
gorjeta = dolares * percentual
print(f"Deixe ${gorjeta:.2f}")



produto = input("Qual é o nome do produto? ")


slogan = input("Qual é o slogan? ")


palavra_chave = input("Qual é a palavra-chave? ")


if palavra_chave in slogan:
    print("Slogan adequado (palavra-chave está no slogan).")
else:
    print("Slogan inadequado (palavra-chave não está no slogan).")


palavras = slogan.split()
num_palavras = len(palavras)


if num_palavras >= 7 and num_palavras <= 10:
    print("Slogan adequado (número de palavras está bom).")
else:
    print("Slogan inadequado (número de palavras está errado).")


if slogan[0].isalpha() and slogan[-1].isalpha():
    print("Slogan adequado (começa e termina com letra).")
else:
    print("Slogan inadequado (não começa e termina com letra).")


if palavra_chave in slogan and num_palavras >= 7 and num_palavras <= 10 and slogan[0].isalpha() and slogan[-1].isalpha():
    print(f'O slogan "{slogan}" está bom para o produto "{produto}".')



produto = input("Digite o nome do produto: ")

valor_produto = float(input("Digite o valor do produto: R$ "))


valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))

troco = valor_pago - valor_produto


print("\n------------------------------------")
print("Comprovante de Venda")
print("------------------------------------")
print(f"Produto: {produto}")
print(f"Valor do Produto: R$ {valor_produto:.2f}")
print(f"Valor Pago: R$ {valor_pago:.2f}")
print(f"Troco: R$ {troco:.2f}")
print("------------------------------------")



temp_max = input("Digite a temperatura máxima do dia: ")
temp_min = input("Digite a temperatura mínima do dia: ")

try:
    temp_max = float(temp_max)
    temp_min = float(temp_min)
except:
  print("Erro você precisa digitar números válidos para as temperaturas.")

media = (temp_max + temp_min) / 2
print("A média das temperaturas é:", media)

variacao = temp_max - temp_min
print("A variação entre as temperaturas é:", variacao)




numero = input("Digite um número para somarmos seus dígitos: ")


if numero.isdigit():
    soma = 0

    for digito in numero:
        soma += int(digito)
    print("A soma dos dígitos é:", soma)
else:
    print("Erro você precisa digitar um número inteiro.")




def soma_dos_numeros():
  entrada = input("digite um número inteiro!")
  if not entrada.lstrip('-').isdigit():
    return print("este número não é válido, por favor digite um número inteiro!")
    numero = int(entrada)
    soma = sum(int(digito) for digito in str(abs(numero)))
    print(f"A soma dos digitos do numero {numero} é: {soma}")
    
    soma_dos_numeros()



# Programa - Notas da equipe

def notas_da_equipe():
    notas = []

    # Solicitar as 5 notas
    for i in range(1, 6):
        while True:
            try:
                nota = float(input(f"Digite a nota do aluno {i}: "))
                if 0 <= nota <= 10:  # Validar que a nota está no intervalo de 0 a 10
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! A nota deve ser entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")

    # Calcular o maior valor, menor valor e média
    maior_nota = max(notas)
    menor_nota = min(notas)
    media_notas = sum(notas) / len(notas)

    # Exibir os resultados
    print(f"\nMaior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Média das notas: {media_notas:.2f}")

# Executar a função
notas_da_equipe()



# Programa - Notas de Carnaval (Modo Antigo)

def notas_de_carnaval():
    notas = []

    # Solicitar as 5 notas
    for i in range(1, 6):
        while True:
            try:
                nota = float(input(f"Digite a nota {i}: "))
                if 0 <= nota <= 10:  # Validar que a nota está no intervalo de 0 a 10
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! A nota deve ser entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")

    # Descarta a maior e a menor nota
    maior_nota = max(notas)
    menor_nota = min(notas)
    notas.remove(maior_nota)
    notas.remove(menor_nota)

    # Calcular a média das 3 notas restantes
    media_notas = sum(notas) / len(notas)

    # Exibir o resultado
    print(f"\nMédia das notas (descontando a maior e a menor): {media_notas:.2f}")

# Executar a função
notas_de_carnaval()




# Programa - Lista de Convidados para a Festa

def lista_de_convidados():
    convidados = []

    # Solicitar nomes dos convidados
    while True:
        nome = input("Digite o nome de um convidado (ou digite 'fim' para encerrar): ")
        
        if nome.lower() == 'fim':
            break
        else:
            convidados.append(nome)

    # Remover duplicados (usando set) e ordenar os nomes
    convidados_unicos = sorted(set(convidados))

    # Exibir a lista final
    print("\nLista final de convidados (sem duplicatas e ordenada):")
    for convidado in convidados_unicos:
        print(convidado)

# Executar a função
lista_de_convidados()



import random

# Função para o jogo de adivinhação
def jogo_de_adivinhacao():
    numero_aleatorio = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas = 0
    acertou = False

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número gerado entre 1 e 100.")

    # Loop até o usuário acertar o número
    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < numero_aleatorio:
                print("O número é maior. Tente novamente.")
            elif palpite > numero_aleatorio:
                print("O número é menor. Tente novamente.")
            else:
                acertou = True
                print(f"Parabéns! Você acertou o número {numero_aleatorio}!")
                print(f"Você acertou em {tentativas} tentativas.")
        except ValueError:
            print("Por favor, insira um número válido.")

# Executar o jogo
jogo_de_adivinhacao()
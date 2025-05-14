# Importa argumentos da linha de comando e a função exit para encerrar o programa.
from sys import argv, exit

# Importa funções e exceções específicas da biblioteca de resolução DNS do dnspython.
from dns.resolver import resolve, NXDOMAIN, NoAnswer, Timeout

# Tenta obter os argumentos passados pelo usuário (domínio e wordlist).
try:
    domain = argv[1]
    wordlist = argv[2]

except IndexError:
    print("Usage: python3 dnsbrute.py dominio wordlist.txt")
    exit()

# Tenta abrir o arquivo de wordlist para leitura.
try:
    with open(wordlist, "r") as file:

        # Lê todas as linhas e remove quebras de linha (\n), criando uma lista.
        subdomains = file.read().splitlines()

except FileNotFoundError:

    # Se o arquivo não for encontrado, exibe erro e encerra.
    print(f"Arquivo '{wordlist}' não encontrado!")
    exit()

# Loop para cada subdomínio presente na lista
for i in subdomains:
    montagem_sub = f"{i}.{domain}"

    try:
        # Faz a resolução DNS do tipo A (endereço IPv4).
        resposta = resolve(montagem_sub, "MX")

        # Para cada IP retornado na resposta, imprime o IP e o subdomínio correspondente.
        for j in resposta:
            print(f"{j} -> {montagem_sub}")

    # Se o subdomínio não existir ou der erro na resposta (sem IP ou timeout), ignora.
    except (NXDOMAIN, NoAnswer, Timeout):
        pass

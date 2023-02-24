# Biblioteca para escolher numeros aleatorios
import random
# Biblioteca para manipular as strings
import string

# Definindo o numero de carcteres da senha 
tamanho = 16

# Vai receber a etrutura da senha com o modulo ascii_letters que 
# permite receber letras maiusculas e minusculas
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+_,.;:/?|'

# vai chamar a funçao para gerar numeros aleatorios a parti de fontes fornecida pelo S.O
rnd = random.SystemRandom()

# Vai pegar cada caracter randomico e criar uma senha
print('Sua senha é:',''.join(rnd.choice(chars) for i in range(tamanho)))
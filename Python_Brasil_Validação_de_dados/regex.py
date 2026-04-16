import re

padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "aaabbbcc rodrigo123@gmail.com.br 1923234747 ccbbbaaa"
resposta = re.findall(padrao, texto)

print(resposta)
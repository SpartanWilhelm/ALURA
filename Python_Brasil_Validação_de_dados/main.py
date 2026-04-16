from Cpf_Cnpj import Documento

from validate_docbr import CNPJ

exemplo_cnpj = "39800701000140"
exemplo_cpf = "69515630045"

documento = Documento.cria_documento(exemplo_cnpj)
documento2 = Documento.cria_documento(exemplo_cpf)

print(documento)
print(documento2)
import os
from generative_model import GenerativeModel

from dotenv import load_dotenv
from google import genai

load_dotenv()
CHAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
modelo = "gemini-3.5-flash"

def carrega(nome_do_arquivo):
  try:
    with open(nome_do_arquivo, "r") as arquivo:
      dados = arquivo.read()
      return dados
  except IOError as e:
    print(f"Erro: {e}")

prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega(os.path.join("dados", "lista_de_compras_100_clientes.csv"))

modelo_flash = GenerativeModel(
  client=client,
  model_name=modelo,
  system_instruction=prompt_sistema,
)
qtd_tokens = modelo_flash.count_tokens(prompt_usuario)

LIMITE_TOKENS = 3000

if qtd_tokens >= LIMITE_TOKENS:
  modelo = "gemini-3.1-pro-preview"

print(f"O modelo selecionado foi: {modelo}")

llm = GenerativeModel(
  client=client,
  model_name=modelo,
  system_instruction=prompt_sistema
)

resposta = llm.generate_content(prompt_usuario)
print(f"Resposta: {resposta.text}")

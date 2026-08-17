import os
from generative_model import GenerativeModel

from dotenv import load_dotenv
from google import genai

MODELO_FLASH = "gemini-3.5-flash"
MODELO_PRO = "gemini-3.1-pro-preview"

CUSTO_ENTRADA_FLASH = 0.075
CUSTO_SAIDA_FLASH = 0.30

CUSTO_ENTRADA_PRO = 3.5
CUSTO_SAIDA_PRO = 10.50

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


model_flash = client.models.get(model=MODELO_FLASH)
limites_modelo_flash = {
    "tokens_entrada" : model_flash.input_token_limit,
    "tokens_saida" : model_flash.output_token_limit,
}

print(f"Limites do modelo flash são: {limites_modelo_flash}")

model_pro = client.models.get(model=MODELO_PRO)
limites_modelo_pro = {
    "tokens_entrada" : model_pro.input_token_limit,
    "tokens_saida" : model_pro.output_token_limit,
}

print(f"Limites do modelo pro são: {limites_modelo_pro}")

llm_flash = GenerativeModel(
    client=client,
    model_name=MODELO_FLASH,
    system_instruction="",
)

quantidade_tokens = llm_flash.count_tokens("O que é uma calça de shopping?")
print(f"A quantidade de tokens é {quantidade_tokens}")

resposta = llm_flash.generate_content("O que é uma calça de shopping?")
tokens_prompt = resposta.usage_metadata.prompt_token_count
tokens_resposta = resposta.usage_metadata.candidates_token_count

custo_total = (tokens_prompt * CUSTO_ENTRADA_FLASH) / 1000000 + (tokens_resposta * CUSTO_SAIDA_FLASH) / 1000000
print(f"Custo Total U$ Flash: ", custo_total)

custo_total = (tokens_prompt * CUSTO_ENTRADA_PRO) / 1000000 + (tokens_resposta * CUSTO_SAIDA_PRO) / 100.000
print(f"Custo Total U$ Pro: ", custo_total)
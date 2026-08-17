import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from generative_model import GenerativeModel

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELO_ESCOLHIDO = "gemini-3.5-flash"

prompt_sistema = "Liste apenas os nomes dos produtos e ofereça uma breve descrição."

configurcao_modelo = {
    "temperature" : 0.1,
    "top_p" : 1.0,
    "top_k" : 64,
    "max_output_tokens" : 8192,
    "response_mime_type" : "text/plain"
}

llm = GenerativeModel(
    client=client,
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_sistema,
    generation_config=configurcao_modelo,
)

pergunta = "Liste três produtos de moda sustentável para ir ao shopping."
resposta = llm.generate_content(pergunta)

print(f"A resposta gerada para a pergunta é: {resposta.text}")
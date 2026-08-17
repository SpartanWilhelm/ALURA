from google.genai import types


class GenerativeModel:
    def __init__(self, client, model_name, system_instruction, generation_config=None):
        self.client = client
        self.model_name = model_name
        self.system_instruction = system_instruction
        self.generation_config = generation_config or {}

    def generate_content(self, pergunta):
        return self.client.models.generate_content(
            model=self.model_name,
            contents=pergunta,
            config=types.GenerateContentConfig(
                system_instruction=self.system_instruction,
                **self.generation_config,
            ),
        )

    def count_tokens(self, conteudo):
        resposta = self.client.models.count_tokens(
            model=self.model_name,
            contents=conteudo,
        )
        return resposta.total_tokens

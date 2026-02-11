import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

prompt_template = """
Você é um assistente jurídico especializado nas Regras do Jogo da IFAB 2023/24.

Use EXCLUSIVAMENTE os trechos abaixo para responder.

Se a informação estiver presente, responda de forma objetiva e normativa.
Se não estiver presente, diga exatamente:
"Essa informação não consta nas Regras do Jogo 2023/24."

Responda sempre em português do Brasil.

Trechos:
{context}

Pergunta:
{question}

Resposta:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
)

# 📄 Caminho do PDF com regras oficiais do futebol
CAMINHO_PDF = "regras_futebol.pdf"

# 1️⃣ Carregar documentos
loader = PyPDFLoader(CAMINHO_PDF)
documents = loader.load()
print(f"PDF carregado com {len(documents)} páginas.")

# 2️⃣ Dividir em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,
    chunk_overlap=250,
    separators=[
        "\nRegra ",
        "\n•",
        "\n",
        ". "
    ]
)

chunks = text_splitter.split_documents(documents)
print(f"Documentos divididos em {len(chunks)} pedaços.")

# 3️⃣ Criar embeddings e banco vetorial (offline)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_regras_futebol"
)
# print(f"Criar embeddings e banco vetorial (offline)")

# 4️⃣ Criar retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 8}
)
# print(f"Criar retriever")

# 5️⃣ Inicializar LLM local (exemplo com Ollama)
# Você pode trocar por outro modelo local ou até usar OpenAI se quiser
llm = ChatOllama(
    model="mistral",
    temperature=0.0
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
# print(f"Inicializar LLM local (Ollama)")

# 6️⃣ Loop interativo
print("\n🤖 Agente de Regras do Futebol iniciado (offline)!")
print("Digite sua pergunta ou 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando agente. Até mais!")
        break
    
    resposta = qa_chain.invoke({"query": pergunta})
    print("\nAgente:", resposta["result"])
    # print("\nTrechos usados como contexto:\n")
    # for i, doc in enumerate(resposta["source_documents"], start=1):
    #     print(f"--- Trecho {i} ---")
    #     print(f"Página: {doc.metadata.get('page', 'N/A')}")
    #     print(doc.page_content[:300], "...\n")

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama


def build_index():
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5",
        model_kwargs={"local_files_only": True}
    )

    documents = SimpleDirectoryReader("docs/").load_data()
    return VectorStoreIndex.from_documents(documents)


def build_query_engine(port):
    llm = Ollama(
        model="tinyllama",
        base_url=f"http://127.0.0.1:{port}",
        system_prompt="Tu ne dois utiliser que le contexte fourni.",
        temperature=0
    )

    index = build_index()
    return index.as_query_engine(llm=llm)
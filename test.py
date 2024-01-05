from mixedbread_ai import MixedbreadAiApi, ApiClient, Configuration

API_KEY = "..."

client = MixedbreadAiApi(
    ApiClient(
        Configuration(
            api_key=API_KEY,
            host="http://localhost:8080",
        )
    )
)
emb_req = {
    "texts": [
        "I love you",
    ],
    "model": "all-MiniLM-L6-v2",
}

embeddings = client.embeddings(emb_req)
print(embeddings)

client = MixedbreadAiApi()
embeddings = client.embeddings(emb_req)
from textblob import TextBlob
from elasticsearch import Elasticsearch
from datetime import datetime
from googletrans import Translator

# Instanciar tradutor
translator = Translator()

# Tweets em português
tweets = [
    "Esse curso foi excelente!",
    "O atendimento foi horrível.",
    "Mais ou menos, esperava mais.",
    "A palestra foi muito boa!",
    "Achei fraco e mal organizado."
]

# Função para traduzir e analisar sentimento
def analisar_sentimento(texto):
    try:
        traduzido = translator.translate(texto, dest='en').text
        analise = TextBlob(traduzido)
        polaridade = analise.sentiment.polarity
        if polaridade > 0:
            return "positivo"
        elif polaridade < 0:
            return "negativo"
        else:
            return "neutro"
    except Exception as e:
        print(f"Erro ao traduzir/analisar: {texto} → {e}")
        return "neutro"

# Conectar ao Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Enviar os tweets para o Elasticsearch
for i, tweet in enumerate(tweets):
    doc = {
        "id": i,
        "texto": tweet,
        "sentimento": analisar_sentimento(tweet),
        "data": datetime.now().isoformat()
    }

    es.index(index="tweets-sentimentos", document=doc)

print("Todos os tweets foram enviados com sucesso!")


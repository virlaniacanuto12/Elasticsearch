from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# Buscar por nome
# Buscar por nome
res = es.search(index="usuarios", query={"match": {"nome": "João"}})
print(res["hits"]["hits"])

# Atualizar idade
id_doc = res["hits"]["hits"][0]["_id"]
es.update(index="usuarios", id=id_doc, doc={"idade": 26})
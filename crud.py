from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# Criar o índice com mapeamento (tipo de cada campo)
if not es.indices.exists(index="usuarios"):
    es.indices.create(
        index="usuarios",
        body={
            "mappings": {
                "properties": {
                    "nome": {"type": "text"},
                    "idade": {"type": "integer"},
                    "email": {"type": "keyword"}
                }
            }
        }
    )
    print("Índice 'usuarios' criado com mapeamento.")

# Inserir documento
doc = {"nome": "João", "idade": 25, "email": "joao@email.com"}
es.index(index="usuarios", document=doc)

# Buscar por nome
res = es.search(index="usuarios", query={"match": {"nome": "João"}})
print(res["hits"]["hits"])

# Atualizar idade
id_doc = res["hits"]["hits"][0]["_id"]
es.update(index="usuarios", id=id_doc, doc={"idade": 26})

# Deletar documento
es.delete(index="usuarios", id=id_doc)
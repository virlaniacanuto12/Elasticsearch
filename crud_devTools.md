
# Comandos Elasticsearch para índice `usuarios` para serem executados no Kibana

## Inserir documento (POST)

```json
POST usuarios/_doc
{
  "nome": "Ana",
  "idade": 22,
  "email": "ana@email.com"
}
```

---

## Buscar documento pelo email (GET)

```json
GET usuarios/_search
{
  "query": {
    "term": {
      "email": {
        "value": "joao@email.com"
      }
    }
  }
}
```

---

## Atualizar documento por ID (POST)

```json
POST usuarios/_update/YkzpxYwB1qQIEmT0tgVd
{
  "doc": {
    "idade": 30,
    "nome": "João da Silva"
  }
}
```

---

## Deletar documento por ID (DELETE)

```http
DELETE usuarios/_doc/YkzpxYwB1qQIEmT0tgVd
```

---

## Atualizar documentos por query (POST)

```json
POST usuarios/_update_by_query
{
  "query": {
    "term": {
      "email": {
        "value": "joao@email.com"
      }
    }
  },
  "script": {
    "source": "ctx._source.idade = params.nova_idade; ctx._source.nome = params.novo_nome;",
    "params": {
      "nova_idade": 30,
      "novo_nome": "João da Silva"
    }
  }
}
```

---

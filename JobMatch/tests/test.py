from chalicelib.elastic_search import ElasticSearch

def test_es_connection():
    es = ElasticSearch()
    assert es.ping(), "Elasticsearch connection failed"
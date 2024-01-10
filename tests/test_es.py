from JobMatch.chalicelib.elastic_search import ElasticSearch

class TestElasticSearch():
    def test_es_connection():
        es = ElasticSearch()
        assert es.ping(), "Elasticsearch connection failed"

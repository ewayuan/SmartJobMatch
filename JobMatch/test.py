from chalicelib.elastic_search import ElasticSearch
from chalicelib.apify_scraper import JobScraper

class TestScraper():
    def test_run_scraper(self):
        job_tiles = ["Machine Learning Engineer"]
        locations = {"&uule=w+CAIQICIHVG9yb250bw==": "Toronto"}

        scrapper = JobScraper(job_tiles, locations)
        results_pd = scrapper.run_scraper()
        assert len(results_pd) > 0

class TestElasticSearch():
    def test_save_job_to_es(self):
        es = ElasticSearch()
        es.save_job_to_es()

def main():
    return
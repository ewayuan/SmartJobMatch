from chalice import Chalice, Cron
from chalicelib.elastic_search import ElasticSearch
from chalicelib.apify_scraper import JobScraper

import logging
import pandas as pd

app = Chalice(app_name='JobMatch')


@app.route('/')
def index():
    return {'hello': 'world'}


# Run at 08:00am (UTC) every 1st day of the month.
@app.schedule(Cron(0, 8, 1, '*', '?', '*'))
def scrapeJob():
    logging.info("Running Job Scraper")
    # job_tiles = ["Machine Learning Engineer", "Data Scientist", "Data Engineer", "Data Analyst", "Software Developer"]
    job_tiles = ["Machine Learning Engineer", "Data Scientist"]
    locations = {"&uule=w+CAIQICIHVG9yb250bw==": "Toronto", "&uule=w+CAIQICIJVmFuY291dmVy": "Vancouver"}

    scrapper = JobScraper(job_tiles, locations)
    results_pd = scrapper.run_scraper()
    logging.info("Finished Job Scraper")
    logging.info("Successfully scraped " + str(len(results_pd)) + " jobs")

    es = ElasticSearch()
    logging.info("Saving jobs to ElasticSearch")  
    es.save_job_to_es(results_pd)
    logging.info("Finished saving jobs to ElasticSearch")

    return 


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting JobMatch Lambda Function")
    scrapeJob()
    logging.info("Finished JobMatch Lambda Function")
    return

main()
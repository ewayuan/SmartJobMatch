import os
from apify_client import ApifyClient
from apify_client.consts import ActorJobStatus

import pandas as pd
import datetime
import logging

class JobScraper:
    def __init__(self, job_tiles, locations) -> None:
        self.APIFY_API_TOKEN = os.environ.get("APIFY_API_TOKEN")
        self.ACTOR_ID = os.environ.get("ACTOR_ID")
        
        self.client = ApifyClient(self.APIFY_API_TOKEN)
        self.job_tiles = job_tiles
        self.locations = locations
        self.results_pd = pd.DataFrame()
    
    def run_scraper (self):

        for location in self.locations:
            for job_title in self.job_tiles:

                logging.info("Scraping " + job_title + " in " + self.locations[location])
                
                run_input = {
                "queries": job_title,
                "locationUule": location,
                "maxPagesPerQuery": 1,
                "csvFriendlyOutput": True,
                "countryCode": "ca",
                "languageCode": "",
                "maxConcurrency": 10,
                "saveHtml": False,
                "saveHtmlToKeyValueStore": False,
                "includeUnfilteredResults": False
                }
            
                # Run the actor and wait for it to finish
                scraper_run = self.client.actor(self.ACTOR_ID).call(run_input=run_input)

                # Check if the scraper finished successfully, otherwise raise an error
                if scraper_run['status'] != ActorJobStatus.SUCCEEDED:
                    raise RuntimeError('The weather scraper run has failed')

                # Get the default dataset associated with the actor run
                job_dataset = self.client.dataset(scraper_run["defaultDatasetId"])

                # Get the data from the dataset as a Pandas DataFrame
                cur_scraped_job_pd = pd.DataFrame.from_dict(job_dataset.list_items().items)
                cur_scraped_job_pd["job_title"] = job_title
                cur_scraped_job_pd["location"] = self.locations[location]
                cur_scraped_job_pd["scraped_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                logging.info("Successfully scraped " + str(len(cur_scraped_job_pd)) + " jobs for " + job_title + " in " + self.locations[location])

                # Append the current scraped jobs to the results Pandas DataFrame
                self.results_pd = pd.concat([self.results_pd, cur_scraped_job_pd])

        return self.results_pd.fillna(value="None")



from opensearchpy import OpenSearch, helpers
import opensearch_py_ml as oml

import pandas as pd
import os
import logging

class ElasticSearch:
    def __init__(self) -> None:
        self.ELASTIC_HOST = os.environ.get("ELASTIC_HOST")
        self.PORT = os.environ.get("PORT")
        self.AUTH = ('swift', 'Hire123!')

        self.es_client = OpenSearch(
            hosts=[{'host': self.ELASTIC_HOST, 'port': self.PORT}],
            http_compress=True,  # enables gzip compression for request bodies
            http_auth=self.AUTH,
            use_ssl=True,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )
    
    def save_job_to_es (self, jobs_pd):
        
        index_name = "jobmatch_dev_wei"

        if not self.es_client.indices.exists(index_name):
            self.es_client.indices.create(index=index_name)
            logging.info("Created index: " + index_name)

        def df_to_opensearch(df, index_name):
            df_iter = df.iterrows()
            for _, document in df_iter:
                record =  {
                    "_index": index_name,
                    "_source": document.to_dict(),
                    }
                yield record 
  
        helpers.bulk(self.es_client, df_to_opensearch(jobs_pd, index_name))

    def get_job_from_es (self):
        pass

    def delete_job_from_es (self):
        pass

    def update_job_in_es (self):
        pass

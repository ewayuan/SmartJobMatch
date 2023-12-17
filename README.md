# SmartJobMatch

## Business Problem
In today's challenging job market, job seekers often encounter a low response rate. Our project is dedicated to developing a solution aimed at significantly improving the success rate of job searches. This solution is designed to enhance the efficiency of job seeking, saving valuable time for applicants while simultaneously increasing response rates. It achieves this by meticulously analyzing individual resumes and preferences to match job seekers with the best-suited opportunities.
## Metrics
### Business Metrics: 
Click-Through Rate: the percentage of users clicking on suggested job links
### Machine Learning-Based Metrics:
Precision: the percentage of the number of accurate positives the model predicted compared to the total number of positives it predicted.
Recall: the percentage of the number of positives the model predicted compared to the actual number of positives in the data.
Specificity: the percentage of the number of negatives the model predicted compared to the actual number of negatives in the data. 
Data
User Resume & Preference Data: User upload their resume and their preference, and the app will summary the resumr and store them along with user preference  in the database on AWS
Job Description Data: The app will scrape job information from job hunting websites daily, such as Linkedin, Indeed, Glassdoor, and it will store thos information into database on AWS



## Solution
### Architect diagram


The system initiates daily scans of fresh job descriptions from platforms like Linkedin, Indeed, and Glassdoor. These details are scraped to update the job database, seamlessly storing them in the AWS S3 bucket.
Upon a new user's arrival, they upload their resume on the frontend website triggering an interaction with the OpenAI API. This API summarizes the resume, preserving the summary in the AWS S3 bucket for reference.
Once the system has gathered preferences and key summarizations from the new user's resume, it employs a matching algorithm. This algorithm effectively sifts through available jobs, aiming to pinpoint the best-suited matches for the user. The top-matched jobs are then presented.
Following the filtration of top matches, the system adheres to a scheduled protocol, promptly sending an email notification to the user.



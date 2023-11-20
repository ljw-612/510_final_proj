# AIPI 510 Final Project
This project achieves a centralized Duke resource database, and provides a web interface for users to search for whatever resources they want. 10 results would be return for each search term with a brief description of the resource and a link to the resource's website. 

# Data Pipeline
## Data Collection/Scraping
 We scraped the data from the Duke websites using `selenium`. 
Websites we scraped:
- https://gpsg.duke.edu/
- https://dukegroups.com/events
- https://students.duke.edu/belonging/get-involved/student-organizations/

Data was well cleaned and organized, null values are filled to the best extent and duplicated values are droped. Finally we obtained a dataset containing xxx rows and each row contains information: `Tilte`, `Reference`, `Type`, and `Description`. Corresponding code can be found under the `data_scrape` folder.

## Data Embedding
We used OpenAI's api to do word embedding to the scraped data. The embedding was done on the combination of `Tilte`, `Reference`, `Type` columns. By doing so, we converted text data into vectors, which can be used for further analysis. 

## Data Storage
A sqlite database was created to store the data. The database contains one table named `embedded_groups` with 6 columns: `Name`, `Description`, `Type`, `Reference`, `Description_bfr_embeddings` and `ada_embedding`. The database is stored in the `database` folder.

# Search Engine Building
## Search Engine
We built a search engine using `streamlit`. We made a Web interface where users can simply input the search term and the system will return the top 10 related resources. Each resources' types are indicated by different colors. Links to the resources' websites and possible descriptions are also provided.

# Project Usage
Nevigate to the root folder of the project and type the following command in the terminal:
``` 
$ stremlit run app.py
```
Then the web interface will be launched in the browser.
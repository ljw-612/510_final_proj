# AIPI 510 Final Project
This project achieves a centralized Duke resource database, and provides a web interface for users to search for whatever resources they want. 10 results would be return for each search term with a brief description of the resource and a link to the resource's website. 

# Data Pipeline
## Data Collection/Scraping
 We scraped the data from the Duke websites using `selenium`. 
Websites we scraped:
- https://gpsg.duke.edu/
- https://dukegroups.com/events
- https://students.duke.edu/belonging/get-involved/student-organizations/

Data was well cleaned and organized, null values are filled to the best extent and duplicated values are droped. Finally we obtained a dataset containing 1000+ rows and each row contains information: `Tilte`, `Reference`, `Type`, and `Description`. Corresponding code can be found under the `data_scrape` folder. See these three files: `duke_events.py`, `duke_groups.py`, `others.py`.

## Data Labels
We wanted to performing classification on the data to create tags per row, so that in the search engine based on tags we can filter data. Hence, we started with `Sports` & `Spiritual or Religious` Tag. Manually created Data Labels for rows. 
Process: Removed stop words from Description of each row using nltk library. Then converted to Vectorized format using TfidfVectorizer. Then, used a Logistic Regression for classification of them into Sports or Not. Similarly if it is related to `Spiritual or Religious` Tag or not. Its part of Classification in dataScraping_Experimentation folder
Conclusion: 
1. There were about 50 rows related to Sports out of 1000+ rows, hence the classification was resulting in all '0'.
2. About 400 were about Spiritual or Religious, hence the classification of it was better.
3. However, realized it is not possible to manually create labels for every condition & create a model for Search Engine. Hence, went with embeddings method described below. 

## Data Embedding
We used OpenAI's api to do word embedding to the scraped data. The embedding was done on the combination of `Tilte`, `Reference`, `Type` columns. By doing so, we converted text data into vectors, which can be used for further analysis. Check out the embedding.py file under the `data_scrape` folder for more details.

## Data Storage
A sqlite database was created to store the data. The database contains one table named `embedded_groups` with 6 columns: `Name`, `Description`, `Type`, `Reference`, `Description_bfr_embeddings` and `ada_embedding`. The database is stored in the `database` folder.

# Search Engine Building
## Search Engine
We built a search engine using `streamlit`. We made a Web interface where users can simply input the search term and the system will return the top 10 related resources. Each resources' types are indicated by different colors. Links to the resources' websites and possible descriptions are also provided.

# Project Usage
We included a Makefile and a requirements.txt to install all of the dependencies and assist in formating the code.

      - Install: install dependencies

      - Format: formats the code using black
      
      - All: performs all


`make install` to install, `make format` to format, and `make all` to perform both

You should obtain a OpenAI API key before running the project. The key should be stored `.env` file under the root folder of the project. The `.env` file should look like this:
```
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
OPENAI_API_KEY=abc123
```
Nevigate to the root folder of the project and type the following command in the terminal:
``` 
$ stremlit run app.py
```
Then the web interface will be launched in the browser.

## Project structure:
```bash
├── Makefile
├── README.md
├── app.py
├── data_scrape
│   ├── classification.py
│   ├── duke_events.ipynb
│   ├── duke_events.py
│   ├── duke_groups.ipynb
│   ├── duke_groups.py
│   ├── embedding.ipynb
│   ├── embedding.py
│   ├── others.ipynb
│   └── others.py
├── database
│   ├── database.db
│   └── database_builder.py
├── output
│   ├── FullDF.csv
│   ├── data_events.csv
│   ├── data_groups.csv
│   ├── embedded_groups.csv
│   └── phonebook.xlsx
├── requirements.txt
├── tree.md
└── venv
```

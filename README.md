# Building Your Own Dataset: Web Scraping with Scrapy in Jupyter Notebooks

Training machine learning models require accurate datasets from the right sources. One way to procure, process and validate the data needed for a dataset is to do it yourself through web scraping.

Following this guide, we will be building a Scrapy spider to scrape data from a website, learn fundamentals of scrapy, and load the scraped JSON data into a Pandas dataframe all in a Jupyter notebook.

You can follow the guide using multiple ways, 

1. Google Colab: [https://colab.research.google.com/drive/1lbJLmFgbZWEvUdp0KbGKT0q75uneqxVf?usp=sharing](https://colab.research.google.com/drive/1lbJLmFgbZWEvUdp0KbGKT0q75uneqxVf?usp=sharing)
2. Jupyter Notebook: [validmind_scraper.ipynb](./validmind_scraper.ipynb)

OR, 

Run the Scrapy command in your virtual environment

```bash
cd tutorial
python3 -m venv scraper
source scraper/bin/activate
pip3 install -r requirements.txt

# Run the ValidMind spider
scrapy crawl valid --nolog
```


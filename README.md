# scraping-music
 A demo scraping project. It was used to create a database of songs and artists reported in spotify playlists. This data was extracted, processed and shipped. The scraped webpages where the following:

1. https://spotifycharts.com/viral/global/weekly/latest
2. https://spotifycharts.com/viral/us/daily/latest
3. https://spotifycharts.com/viral/gb/daily/latest
4. https://spotifycharts.com/regional/global/weekly/latest
5. https://spotifycharts.com/regional/us/daily/latest
6. https://spotifycharts.com/regional/gb/daily/latest

 ## Installing Scrapy
Open a command line. Using python 3.7.9 or above, use:

```python
pip install scrapy
```

## Crawling the webpages
Once scrapy is installed, open a command line and navigate to the ./scraping-music/ScrapingSpotifyCharts/ directory. Once there, run the following command:

```python
# Export as JSON
scrapy crawl spotify-charts -o results.json

# Export as CSV
scrapy crawl spotify-charts -o results.csv

# Export as HTML
scrapy crawl spotify-charts -o results.html
```

## Example results
The file named 2020-december-23-results.json is an example output file. This scraping job was run on the 2020-12-23. You can check it using a text editor.

## Scraping-hub
Scrapinghub.com is a service created by the same team that created the Scrapy library. You can use this service to run a scraping job automatically everytime you need. The data will be saved in their cloud for you to download and use whenever you want. 

Please feel free to ask any questions!

Author: Andres Sanchez

Email: andres.sanchez.liu@gmail.com

UpWork: Andres Sanchez

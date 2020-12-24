import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest
from ..items import ScrapingspotifychartsItem
import re

def remove_colaborators(song):
    '''
    Description:    
        Checks if the given song includes the words: FEAT, feat, Feat, Ft., ft.,  with, WITH, With to then process the song name correctly.  

    Args:
        song (str): a string that includes the artist name, the song name and the colab names.
    
    Returns:
        True > if it contains the given words.
        False > if it doesn't contain the given words.
    '''
    regex_match = r'([(]*\s*[Ff][Ee][Aa][Tt][.]*) | ([(]*\s*[Ff][Tt][.]*) | ([(]*\s*[Ff][Ee][Aa][Tt][Uu][Rr][Ii][Nn][Gg]) | ([(]\s*[Ww][Ii][Tt][Hh])'

    return re.search(regex_match, song)

def define_country(url):
    '''
    Description:
        Checks the url to see which country does the playlist come from.

    Args:
        url (str): the url that is being scraped.

    Returns:
        string: returns a string specified for the value in the python dictionary that is assigned to a given key.
    '''

    Lists = {
        'global':'Global',
        'us':'United States',
        'gb':'United Kingdom'
    }

    for key in Lists.keys():
        if re.search(key, url) is not None:
            List = Lists.get(key)
            break
        else:
            List = 'Unkwown'
    
    return List


class SpotifyChartsSpider(scrapy.Spider):
    name = 'spotify-charts'
    start_urls = [
        'https://spotifycharts.com/viral/global/weekly/latest',
        'https://spotifycharts.com/viral/us/daily/latest',
        'https://spotifycharts.com/viral/gb/daily/latest',
        'https://spotifycharts.com/regional/global/weekly/latest',
        'https://spotifycharts.com/regional/us/daily/latest',
        'https://spotifycharts.com/regional/gb/daily/latest'
    ]

    def parse(self, response):
        items = ScrapingspotifychartsItem()

        # Checks if the list is global, from US or the UK.
        List = define_country(response.url)
        
        # Cada fila de la pagina es una cancion con sus datos
        rows = response.css('tbody tr')

        for row in rows[0:50]:
            Author = row.css('td.chart-table-track span::text').extract_first()
            Author = re.sub(r'[b][y]\s','', Author)
            Ranking = row.css('td.chart-table-position::text').extract_first()
            Link = row.css('a::attr(href)').extract_first()
            
            # Separando y tratando canciones con colaboradores
            song_text_name = row.css('td.chart-table-track strong::text').extract_first()

            if remove_colaborators(song_text_name) is not None: 
                Song = song_text_name.split(remove_colaborators(song_text_name).group(),1)[0]
                Colaborators = song_text_name.split(remove_colaborators(song_text_name).group(),1)[1]
                Colaborators = re.sub('[()]','',Colaborators).lstrip()
                ConcatName = Author + ' ft ' + Colaborators + ' - ' + Song
            else:
                Colaborators = None
                Song = song_text_name
                ConcatName = Author + ' - ' + Song

            items['Author'] = Author
            items['Colaborators'] = Colaborators
            items['Song'] = Song
            items['ConcatName'] = ConcatName
            items['Ranking'] = Ranking
            items['List'] = List
            items['Link'] = Link

            yield items

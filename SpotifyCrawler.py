from SpotifyScraper.scraper import Scraper
from SpotifyScraper.request import Request
import os

if __name__ == "__main__":

    data_dir = 'C:\\Users\\16520\\Desktop\\GenrePrediction\\data'
    predata_dir = 'C:\\Users\\16520\\Desktop\\GenrePrediction\\pre-data'

    for dirpath, dirnames, filenames in os.walk(predata_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            genre_name = filename.split('.txt')[0]
            genre_data_dir = os.path.join(data_dir, genre_name)
            with open(filepath) as f:
                lines = f.readlines()
                for line in lines:
                    track_info = Scraper(session=Request().request()).get_track_url_info(url=line)
                    path = Scraper(session=Request().request()).download_preview_mp3(url=line, path=genre_data_dir, with_cover=False)
                    print(path)

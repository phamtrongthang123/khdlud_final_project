
# %%
from Crawler import Crawler
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()

url = args.url

crawler = Crawler(url)
dat = crawler.start_crawling()
crawler.finish_crawling()
print(dat)
import json
with open('demo/demo_crawl_result.json', 'w') as f:
    json.dump(dat, f)


        



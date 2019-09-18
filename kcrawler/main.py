from scrapy import cmdline
import os 

filename = 'response.json'
if os.path.exists(filename):
	os.remove(filename)
        
key = input("Enter keyword : ")
cmd="scrapy crawl mainspider -a keyword="+key+" -o response.json"
cmdline.execute(cmd.split())

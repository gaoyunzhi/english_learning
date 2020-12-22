#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import link_extractor
import time
import plain_db
from bs4 import BeautifulSoup
import cached_url
import export_to_telegraph

with open('token') as f:
	token = f.read().strip()

existing = plain_db.loadKeyOnlyDB('existing')
		
def run():
	links = link_extractor.getLinks('https://www.bbc.co.uk/learningenglish/chinese')
	print(links)
			
if __name__ == '__main__':
	run()
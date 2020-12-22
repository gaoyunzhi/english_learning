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

# with open('telegraph_token') as f:
# 	export_to_telegraph.token = f.read().strip()

site = 'https://www.bbc.co.uk/learningenglish/chinese'

existing = plain_db.loadKeyOnlyDB('existing')
		
def run():
	for link in link_extractor.getLinks(site):
		result = export_to_telegraph.export(link, force=True, throw_exception=True) 
		print(result)
		return
	
			
if __name__ == '__main__':
	run()
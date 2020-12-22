#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, MessageHandler, Filters
from telegram_util import log_on_fail
import link_extractor
import time
import plain_db
from bs4 import BeautifulSoup
import cached_url
import export_to_telegraph

with open('token') as f:
	tele = Updater(f.read().strip(), use_context=True)
debug_group = tele.bot.get_chat(420074357)
channel_en = tele.bot.get_chat(-1001414226421)

# with open('telegraph_token') as f:
# 	export_to_telegraph.token = f.read().strip()

site = 'https://www.bbc.co.uk/learningenglish/chinese'

existing = plain_db.loadKeyOnlyDB('existing')

def getFile(link):
	soup = BeautifulSoup(cached_url.get(link, force_cache=True), 'html.parser')
	for item in soup.find_all('a', class_='download'):
		if item.get('href', '').endswith('mp3'):
			return item.get('href', '')
		
def run():
	for link in link_extractor.getLinks(site):
		if existing.contain(link):
			continue
		# result = export_to_telegraph.export(link, force=True, throw_exception=True) 
		file = getFile(link)
		if not file:
			continue
		cached_url.get(file, mode='b', force_cache=True)

		
if __name__ == '__main__':
	run()
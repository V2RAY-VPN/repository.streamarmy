import requestsimport reimport xbmcimport xbmcguiimport timefrom random import randintdialog = xbmcgui.Dialog()from cloudscraper2 import CloudScraperCF = CloudScraper.create_scraper()ua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",      "Referer" : "https://www.limetorrents.info/"}class Scraper:	def __init__(self):		self.Base = 'https://www.limetorrents.info/'		self.Search = ('search/movies/%s')		self.SearchTv = ('search/tv/%s')		self.links = []	def Index(self,type, term,year,imdb,torrents):		if type == 'TV':			MovieName = term			#term = term.replace('TV|||','')			term = term.replace(' ','-')			link = CF.get(self.Base+self.SearchTv %term, headers=ua).content			match = re.findall('Torrent Name</span>(.*?)<div id="rightbar">',link,flags=re.DOTALL)[0]			pattern = r'''href=['"]([^'"]+)['"]'''			getlinks = re.findall(pattern,match)			if not getlinks: return False			for link in getlinks:				if self.Base not in link and '.html' in link:					link = self.Base+link					if 'uhd' in link.lower(): sort = '5' ; qual = '4K UHD'					elif '2160' in link.lower(): sort = '5'; qual = '4K UHD'					elif '1080' in link.lower(): sort = '6'; qual = 'FHD'					elif '720' in link.lower(): sort = '7'; qual = 'HD'					else : sort = '8'; qual = 'SD'					title = 'LimeTorrents ( Debrid ) | ' + qual + ' | ' +MovieName					self.links.append({'title': title, 'url': link, 'quality' : sort, 'Debrid' : True, 'Direct' : False})			return self.links		else:			MovieName = term			term = term.replace(' ','+')			link = CF.get(self.Base+self.Search %term, headers=ua).content			match = re.findall('Torrent Name</span>(.*?)<div id="rightbar">',link,flags=re.DOTALL)[0]			pattern = r'''href=['"]([^'"]+)['"]'''			getlinks = re.findall(pattern,match)			if not getlinks: return False			for link in getlinks:				if self.Base not in link and '.html' in link:					if year.strip() in link:						link = self.Base+link						if 'uhd' in link.lower(): sort = '5' ; qual = '4K UHD'						elif '2160' in link.lower(): sort = '5'; qual = '4K UHD'						elif '1080' in link.lower(): sort = '6'; qual = 'FHD'						elif '720' in link.lower(): sort = '7'; qual = 'HD'						else : sort = '8'; qual = 'SD'						title = '[COLOR yellow]LimeTorrents ( Debrid ) | [/COLOR]' + qual + ' | ' +MovieName						self.links.append({'title': title, 'url': link, 'quality' : sort, 'Debrid' : True, 'Direct' : False})			return self.links
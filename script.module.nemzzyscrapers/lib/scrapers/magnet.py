import requestsimport reimport xbmcimport xbmcguifrom cloudscraper2 import CloudScraperfrom bs4 import BeautifulSoupdialog = xbmcgui.Dialog()CF = CloudScraper.create_scraper()ua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}class Scraper:	def __init__(self):		self.Base = 'https://www.magnetdl.com/'		self.Search = ('')		self.links = []	def Index(self,type, term,year,imdb,torrents):		if type == 'TV':			MovieName = term			term = term.replace(' ','-')			t1 = term[0]			fulllink = (self.Base+'%s/%s' % (t1,term)).lower()			link = CF.get(fulllink,headers=ua).content			soup = BeautifulSoup(link,'html.parser')			data = soup.find('table', class_={'download'})			for i in data.select("a[href*=magnet]"):				link = i['href']				captacha = link.replace('+',' ').replace('.',' ')				if MovieName.lower() in captacha.lower():					if 'uhd' in link.lower(): sort = '5' ; qual = '4K UHD'					elif '2160' in link.lower(): sort = '5'; qual = '4K UHD'					elif '1080' in link.lower(): sort = '6'; qual = '1080'					elif '720' in link.lower(): sort = '7'; qual = '720'					else : sort = '8'; qual = 'SD'					title = ('[COLOR yellow]Magnet DL ( Real Debrid ) | %s | %s' % (qual,MovieName))					self.links.append({'title': title, 'url': link, 'quality' : sort})			return self.links		else:			MovieName = term			term = term.replace(' ','-')			t1 = term[0]			fulllink = (self.Base+'%s/%s' % (t1,term)).lower()			link = CF.get(fulllink,headers=ua).content			soup = BeautifulSoup(link,'html.parser')			data = soup.find('table', class_={'download'})			for i in data.select("a[href*=magnet]"):				link = i['href']				captacha = link.replace('+',' ').replace('.',' ')				if MovieName.lower() in captacha.lower() and year.strip() in captacha.lower():					if 'uhd' in link.lower(): sort = '5' ; qual = '4K UHD'					elif '2160' in link.lower(): sort = '5'; qual = '4K UHD'					elif '1080' in link.lower(): sort = '6'; qual = '1080'					elif '720' in link.lower(): sort = '7'; qual = '720'					else : sort = '8'; qual = 'SD'					title = ('[COLOR yellow]Magnet DL ( Real Debrid ) | %s | %s' % (qual,MovieName))					self.links.append({'title': title, 'url': link, 'quality' : sort})			return self.links
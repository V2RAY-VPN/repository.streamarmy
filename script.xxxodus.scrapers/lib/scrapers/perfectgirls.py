import xbmc,xbmcplugin,os,urlparse,re
import client
import kodi
import dom_parser2
import log_utils
import lover
from bs4 import BeautifulSoup
from resources.lib.modules import utils
from resources.lib.modules import helper
buildDirectory = utils.buildDir #CODE BY NEMZZY AND ECHO

filename     = os.path.basename(__file__).split('.')[0]
base_domain  = 'http://www.perfectgirls.net'
base_name    = base_domain.replace('www.',''); base_name = re.findall('(?:\/\/|\.)([^.]+)\.',base_name)[0].title()
type         = 'video'
menu_mode    = 216
content_mode = 217
player_mode  = 801

search_tag   = 1
search_base  = urlparse.urljoin(base_domain,'search/?q=%s')

@utils.url_dispatcher.register('%s' % menu_mode)
def menu():
    
    lover.checkupdates()
    
    try:
        url = base_domain
        c = client.request(url)
        r = dom_parser2.parse_dom(c, 'li', {'class': 'header-submenu__item'})
        r = dom_parser2.parse_dom(r, 'a', req='href')
        r = [(i.attrs['href'], \
            i.content)for i in r if i]
        r = [(urlparse.urljoin(base_domain,i[0]),i[1]) for i in r if i]
        if ( not r ):
            log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
            kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
            quit()
    except Exception as e:
        log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
        kodi.notify(msg='Fatal Error', duration=4000, sound=True)
        quit()

    dirlst = []
    
    for i in r:
        try:
            name = kodi.sortX(i[1].encode('utf-8')).title()
            icon = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/icon.png' % filename))
            fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
            dirlst.append({'name': name, 'url': i[0], 'mode': content_mode, 'icon': icon, 'fanart': fanarts, 'folder': True})
        except Exception as e:
            log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)
    
    if dirlst: buildDirectory(dirlst)    
    else:
        kodi.notify(msg='No Menu Items Found')
        quit()
        
@utils.url_dispatcher.register('%s' % content_mode,['url'],['searched'])
def content(url,searched=False):

	try:
		url = client.request(url, output='geturl')
		c = client.request(url)
		soup = BeautifulSoup(c,'html.parser')
		r = soup.find_all('div', class_={'list__item'})
		if ( not r ) and ( not searched ):
			log_utils.log('Scraping Error in %s:: Content of request: %s' % (base_name.title(),str(c)), log_utils.LOGERROR)
			kodi.notify(msg='Scraping Error: Info Added To Log File', duration=6000, sound=True)
	except Exception as e:
		if ( not searched ):
			log_utils.log('Fatal Error in %s:: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
			kodi.notify(msg='Fatal Error', duration=4000, sound=True)
			quit()    
		else: pass
		
	dirlst = []

	for i in r:
		try:
			name = i.img['alt']
			if searched: description = 'Result provided by %s' % base_name.title()
			else: description = name
			icon = i.img['data-original']
			if not 'http' in icon: icon='http:'+icon
			url2 = i.a['href']
			if not base_domain in url2: url2 = base_domain + url2
			fanarts = xbmc.translatePath(os.path.join('special://home/addons/script.xxxodus.artwork', 'resources/art/%s/fanart.jpg' % filename))
			dirlst.append({'name': name, 'url': url2, 'mode': player_mode, 'icon': icon, 'fanart': fanarts, 'description': description, 'folder': False})
		except Exception as e:
			log_utils.log('Error adding menu item %s in %s:: Error: %s' % (i[1].title(),base_name.title(),str(e)), log_utils.LOGERROR)

	if dirlst: buildDirectory(dirlst, stopend=True, isVideo = True, isDownloadable = True)
	else:
		if (not searched):
			kodi.notify(msg='No Content Found')
			quit()
		
	if searched: return str(len(r))

	if not searched:
		
		try:
			pattern = r'''((?:http|https)(?:\:\/\/)(?:www)(?:\/\/|\.)(perfectgirls.net)\/(category\/)([0-9+]\/)(.+?\/))([0-9]+)'''
			r = re.search(pattern,url)
			base = r.group(1)
			search_pattern = '''<a\s*class=['"]btn_wrapper__btn['"]\s*href=['"]([^'"]+)['"]>Next'''
			parse = base         
			helper.scraper().get_next_page(content_mode,url,search_pattern,filename,parse)
		except Exception as e: 
			log_utils.log('Error getting next page for %s :: Error: %s' % (base_name.title(),str(e)), log_utils.LOGERROR)
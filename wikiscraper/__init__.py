#┌----------------------------------------------┐#
#| Wikiscraper								    |#
#| Developed by Alexandre MEYER                 |#
#| License CC BY 4.0                            |#
#| https://github.com/Alexandre333/wikiscraper  |#
#| 2021                                         |#
#└----------------------------------------------┘#

import requests
from bs4 import BeautifulSoup
import bs4

# default language
LANG_ISO6391 = "en"

def lang(iso):
	global LANG_ISO6391
	LANG_ISO6391 = iso

class searchBySlug:

	def __init__(self, slug):
		self.slug = slug
		r = requests.get('https://'+LANG_ISO6391+'.wikipedia.org/wiki/'+self.slug)
		self.misoSoup = BeautifulSoup(r.text, 'html.parser')

		for s in self.misoSoup.select('sup'):
			s.extract()

	def getTitle(self):
		title = self.misoSoup.find(id="firstHeading")

		return title.text

	def getURL(self):
		url = 'https://'+LANG_ISO6391+'.wikipedia.org/wiki/'+self.slug

		return url

	def getAbstract(self, limit=1000):
		dataAbstract = []

		if self.misoSoup.find('div', attrs={'class': "noarticletext"}):
			dataAbstract.append("Unable to find the requested query: please check the spelling of the slug")
		else:
			if self.misoSoup.find(class_="infobox_v2"):
				info_class_name = "infobox_v2"
			else:
				info_class_name = "infobox"

			tag = self.misoSoup.find(class_=info_class_name).findNext('p')

			# Thanks salmanwahed
			# https://stackoverflow.com/questions/34585206/beautiful-soup-find-all-p-until-form
			for i in range(limit):
				if isinstance(tag, bs4.element.Tag):
					if tag.name == 'div':
						break
					else:
						dataAbstract.append(tag.text.replace(u'\n', u'').replace(u'\xa0', u' '))
						tag = tag.nextSibling
				else:
					tag = tag.nextSibling

		return dataAbstract

	def getSideInfo(self, label):
		value_label = []
		
		if self.misoSoup.find('div', attrs={'class': "noarticletext"}):
			value_label.append("Unable to find the requested query: please check the spelling of the slug")
		else:
			if self.misoSoup.find(class_="infobox_v2"):
				info_class_name = "infobox_v2"
			else:
				info_class_name = "infobox"

			all_tr = self.misoSoup.find(class_=info_class_name).findAll('tr')

			for tr in all_tr:
				if tr.find('th', attrs={'scope':'row'}):
					if tr.find('th').find('a'):
						row_label = tr.find('th').find('a').text
					else:
						row_label = tr.find('th').text
						
					if row_label == label:
						if tr.find('td').find('a', attrs={'class': None}):
							row_value = tr.find('td').find('a', attrs={'class': None}).text
						else:
							row_value = tr.find('td').text

						row_value = row_value.replace(u'\xa0', u' ').replace(u'\n', u'')
						value_label.append(row_value)

		return value_label

	def getImage(self):
		images = []

		if self.misoSoup.find('div', attrs={'class': "noarticletext"}):
			images.append("Unable to find the requested query: please check the spelling of the slug")
		else:
			thumbs = self.misoSoup.findAll('a', class_="image")

			for thumb in thumbs:
				image = "https:"+thumb.find('img').attrs['src']
				images.append(image)
		
		return images

	def getSection(self, h2_name=None, h3_name=None, h4_name=None, limit=1000):
		content = []

		if self.misoSoup.find('div', attrs={'class': "noarticletext"}):
			content.append("Unable to find the requested query: please check the spelling of the slug")
		else:

			if h2_name is None:
				sections = self.misoSoup.findAll("h2")
				for section in sections:
					h2_title = section.find(class_="mw-headline")
					if h2_title is not None:
						content.append(h2_title.text)
			else:
				
				if h4_name is not None:
					h4_name = h4_name.replace(" ", "_")				
					section = self.misoSoup.find(id=h4_name).findNext('p')
				elif h3_name is not None:
					h3_name = h3_name.replace(" ", "_")				
					section = self.misoSoup.find(id=h3_name).findNext('p')
				else:
					h2_name = h2_name.replace(" ", "_")				
					section = self.misoSoup.find(id=h2_name).findNext('p')

				for i in range(limit):
					if isinstance(section, bs4.element.Tag):
						if section.name == 'h2' or section.name == 'h3' or section.name == 'h4':
							break
						else:
							content.append(section.text)
							section = section.nextSibling
					else:
						section = section.nextSibling

		return content

	def getContentsTable(self, subcontents=False):
		if not subcontents:
			content = []
		else:
			content = {}

		if self.misoSoup.find('div', attrs={'class': "noarticletext"}):
			content.append("Unable to find the requested query: please check the spelling of the slug")
		else:
			all_li = self.misoSoup.find(class_="toctitle").findNext('ul')
			for li in all_li:
				if not li.find('a') == -1:
					li_value = li.find('a').find(class_="toctext").text
					
					if not subcontents:
						content.append(li_value)
					else:
						if li.find('ul'):
							all_li_of_ul = li.find('a').findNext('ul')
							list_li = []
							for li_of_ul in all_li_of_ul:
								if not li_of_ul.find('a') == -1:
									li_of_ul = li_of_ul.find('a').find(class_="toctext").text
									list_li.append(li_of_ul)
								
								content[li_value] = list_li
						else:
							content[li_value] = []
		return content

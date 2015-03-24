#!/usr/bin/python
from random import randint
import library.dateutil.parser as parse
from library.dateutil.relativedelta import *
from library.dateutil.tz import tzlocal
from datetime import *
from math import pow, log, log10, e

class Apartment(object):

	def __init__(self, title, link, description, created):

		self.description = description
		self.link = link
		self.created = created

		temp = title.split()
		self.size = temp.pop().split('<')[0].replace('ft', '')
		self.bedrooms = temp.pop()
		self.price = temp.pop().replace('&#x0024;', '')

		self.title = ' '.join(temp)

		self.ranking = self.__getRanking()

	def __str__(self):
		return self.title + "\r\nPrice: $" + self.price + "\r\nSize: " + self.size + "sqft\r\nBedrooms: " + self.bedrooms + "\r\nDescription: " + self.description + "\r\n" + self.link + "\r\nCreated: " + self.created

	def formatForEmail(self):
		return "<html><a href='" + self.link + "'><h1>" + self.title + """</h1></a>
				<b>Rating:</b> """ + str(self.ranking) + """<br/> 
				<b>Price:</b> $""" + str(self.price) + """<br/>
				<b>Size:</b> """ + str(self.size) + """sqft<br/>
				<b>Bedrooms:</b> """ + self.bedrooms + """<br/>
				<b>Description:</b> """ + self.description + """<br/>
				<b>Created:</b> """ + self.created + "</html>"

	def __getRanking(self):

		ranking = ((int(self.size) / 600) * 4) + (pow((1800 / int(self.price)), 2) * 6)

# 		print("""
# Printing Rating for """ + self.link)

# 		print("Now: ", datetime.now(tzlocal()).timestamp())
# 		print("Posted On: ", parse.parse(self.created).timestamp())

# 		print("Ranking from time: ", (1 / 2.592) * pow((14400 / (datetime.now(tzlocal()).timestamp() - parse.parse(self.created).timestamp())), 2) * 10)
# 		print("Ranking2 from time: ", log(14400 / (datetime.now(tzlocal()).timestamp() - parse.parse(self.created).timestamp())))
# 		print("Ranking3 from time: ", log(14400 / (datetime.now(tzlocal()).timestamp() - parse.parse(self.created).timestamp())))

# 		test = pow((14400 / (datetime.now(tzlocal()).timestamp() - parse.parse(self.created).timestamp())), 2)

# 		print("Ranking4 from time: ", pow(e, test) * 14)

		ranking +=  (10 / 2.592) * pow((14400 / (datetime.now(tzlocal()).timestamp() - parse.parse(self.created).timestamp())), 2)

		if "balcony" in self.description:
			ranking += 4

		if "sound" in self.description:
			ranking += 5

		if "water" in self.description:
			ranking += 5

		if "elliot" in self.description:
			ranking += 5

		if "nook" in self.description:
			ranking += 8
			
		if "island" in self.description:
			ranking += 8	

		return ranking
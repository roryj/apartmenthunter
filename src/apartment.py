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

		print (title)
		temp = title.split()
		self.size = temp.pop().split('<')[0].replace('ft', '')
		self.bedrooms = temp.pop()
		self.price = temp.pop().replace('&#x0024;', '')
		print (self.price)

		self.title = ' '.join(temp)

		self.ranking = self.__getRanking()

	def __str__(self):
		return self.title + "\r\nPrice: $" + self.price + "\r\nSize: " + self.size + "sqft\r\nBedrooms: " + self.bedrooms + "\r\nDescription: " + self.description + "\r\n" + self.link + "\r\nCreated: " + self.created

	def __getRanking(self):

		ranking = ((int(self.size) / 600) * 3) + ((1800 / int(self.price)) * 6)

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

		if "view" in self.description:
			ranking += 5

		return ranking
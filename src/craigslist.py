#!/usr/bin/python

from src.website import Website
from src.apartment import Apartment
import library.feedparser as parser

class Craigslist(Website):

	def getApartments(self, neighbourhood, pages):

		apartments = []

		print ("Searching ", pages, " pages of craigslist for apartments in ", neighbourhood, ".")

		for page in range(0, pages):

			queryString = self.__generateQueryString(neighbourhood, page)

			print(queryString)

			results = parser.parse(queryString)

			apartmentList = results["entries"]

			for apartmentListing in apartmentList:

				try:
					apartment = Apartment(apartmentListing["title"], apartmentListing["link"], apartmentListing["summary"], apartmentListing["published"])

					print ("Adding apartment ", apartment.title, " to list.")

					apartments.append(apartment)

				except ValueError as detail:
					print ("Apartment could not be loaded with this title: ", apartmentListing["title"].encode('utf-8'), detail)

		return apartments

	def __generateQueryString(self, neighbourhood, page):
		#http://seattle.craigslist.org/search/see/apa?minAsk=1400&maxAsk=2000&bedrooms=1&minSqft=500&query=capital+hill&format=rss
		
		query = "http://seattle.craigslist.org/search/see/apa?"

		#Get all properties in the website object that are not private or not methods
		searchProperties = [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self,a))]

		for objectProperty in searchProperties:

			propertyValue = getattr(self, objectProperty)

			if (propertyValue):
				query += objectProperty + "=" + str(propertyValue) + "&"

		if (neighbourhood):
			query += "query=" + neighbourhood.replace(" ", "+") + "&"

		query += "format=rss&s=" + str(page * 25)

		return query
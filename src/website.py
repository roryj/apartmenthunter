#!/usr/bin/python

class Website(object):

	def __init__(self, minPrice = 0, maxPrice = 0, bedrooms = 0, minSqft = 0, maxSqft = 0):
		self.minAsk = minPrice
		self.maxAsk = maxPrice
		self.bedrooms = bedrooms
		self.minSqft = minSqft
		self.maxSqft = maxSqft

	def getApartments(self, neighborhood):
		return []

	def __generateQueryString():
		return "Test"
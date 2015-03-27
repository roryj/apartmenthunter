#!/usr/bin/python
import json

class Configuration(object):

	def __init__(self, configPath = ''):

		if not configPath:
			configPath = "config.json"

		print ("Setting up the configuration from ", configPath, ".")

		with open(configPath) as data_file:
			data = json.load(data_file)

		self.email = data["email"]
		self.password = data["password"]
		self.phoneNumber = data["phoneNumber"]

		# Search criteria
		self.neighbourhoods = data["criteria"]["neighbourhoods"]
		self.minPrice = data["criteria"]["minPrice"]
		self.maxPrice = data["criteria"]["maxPrice"]
		self.minSqft = data["criteria"]["minSqft"]
		self.maxSqft = data["criteria"]["maxSqft"]
		self.bedrooms = data["criteria"]["bedrooms"]
		self.pages = data["criteria"]["pages"]


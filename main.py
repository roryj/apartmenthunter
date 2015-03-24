#!/usr/bin/python

import sys
from src.craigslist import Craigslist
from src.messenger import Messenger
from src.configuration import Configuration

def main():

	config = Configuration()
	craigsLister = Craigslist(config.minPrice, config.maxPrice, config.bedrooms, config.minSqft, config.maxSqft)

	apartments = []

	for neighbourhood in config.neighbourhoods:
		# Get the list of apartments from craigslist
		apartments.extend(craigsLister.getApartments(neighbourhood, config.pages))

	for apartment in apartments:
		print (apartment.ranking)

	# Sort the apartments based on ranking
	apartments.sort(key=lambda x: x.ranking, reverse=True)

	for apartment in apartments:
		print (apartment.ranking)

	messenger = Messenger(config.email, config.password)

	# Send the #1 ranked apartment as a text
	messenger.sendTextMessageTMobile(config.phoneNumber, str(apartments[0]))

	# Send the top 10 in email
	messenger.sendEmailMessage(('<br/><br/>'.join(apt.formatForEmail() for apt in apartments[:20])))

if __name__ == "__main__":
    main()
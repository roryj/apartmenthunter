#!/usr/bin/python

import sys
from src.craigslist import Craigslist
from src.messenger import Messenger
from src.configuration import Configuration

def main():

	config = Configuration()

	craigsLister = Craigslist(config.minPrice, config.maxPrice, config.minSqft, config.maxSqft)

	# Get the list of apartments from craigslist
	apartments = craigsLister.getApartments("Capital Hill", config.pages)

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
	messenger.sendEmailMessage('\r\n\r\n'.join(str(str(apt).encode('utf-8')) for apt in apartments[:10]))

if __name__ == "__main__":
    main()
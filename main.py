#!/usr/bin/python

import sys
from src.craigslist import Craigslist
from src.messenger import Messenger
from src.configuration import Configuration

def main():

	config = Configuration()
	craigsLister = Craigslist(config.minPrice, config.maxPrice, config.bedrooms, config.minSqft, config.maxSqft)

	apartments = []

	# For the list of neighbourhoods, append the list of apartments to the list
	for neighbourhood in config.neighbourhoods:
		apartments.extend(craigsLister.getApartments(neighbourhood, config.pages))

	# Sort the apartments based on ranking
	apartments.sort(key=lambda x: x.ranking, reverse=True)

	# Make the list unique
	temp = set(apartments)

	uniqueApartments = list(temp)

	messenger = Messenger(config.email, config.password)

	# Send the #1 ranked apartment as a text
	messenger.sendTextMessageTMobile(config.phoneNumber, str(uniqueApartments[0]))

	# Send the top 20 in email
	messenger.sendEmailMessage(('<br/><br/>'.join(apt.formatForEmail() for apt in uniqueApartments[:20])))

if __name__ == "__main__":
    main()
#!/usr/bin/python

import sys
from src.craigslist import Craigslist
from src.messenger import Messenger
from src.configuration import Configuration

def main():

	print ("""*********************************************
Starting the Apartment Hunter
*********************************************""")

	config = Configuration()
	craigsLister = Craigslist(config.minPrice, config.maxPrice, config.bedrooms, config.minSqft, config.maxSqft)

	apartments = []

	# For the list of neighbourhoods, append the list of apartments to the list
	for neighbourhood in config.neighbourhoods:
		apartments.extend(craigsLister.getApartments(neighbourhood, config.pages))

	# Make the list unique
	temp = set(apartments)

	uniqueApartments = list(temp)

	# Sort the apartments based on ranking
	uniqueApartments.sort(key=lambda x: x.ranking, reverse=True)

	print (len(apartments), " apartments found in total.")
	print (len(uniqueApartments), " unique apartments found in total.")

	messenger = Messenger(config.email, config.password)

	# Send the #1 ranked apartment as a text
	messenger.sendTextMessageTMobile(config.phoneNumber, str(uniqueApartments[0]))

	# Send the top 10 in email
	messenger.sendEmailMessage(('<br/><br/>'.join(apt.formatForEmail() for apt in uniqueApartments[:10])))

if __name__ == "__main__":
    main()

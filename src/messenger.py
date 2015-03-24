#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Messenger(object):

	def __init__(self, email, password):
		self.email = email
		self.password = password 

	def sendEmailMessage(self, message):

		msg = MIMEMultipart('alternative')
		msg['Subject'] = 'Apartment Results'
		msg['From'] = self.email
		msg['To'] = self.email

		htmlMessage = MIMEText(message, 'html')
		msg.attach(htmlMessage)

		self.__sendMessage(self.email, msg)

	def sendTextMessageTMobile(self, number, message):

		msg = MIMEText(message)

		self.__sendMessage(number + "@tmomail.net", msg)

	def __sendMessage(self, email, message):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(self.email,self.password)
		server.sendmail(self.email, email, message.as_string())
		server.quit()
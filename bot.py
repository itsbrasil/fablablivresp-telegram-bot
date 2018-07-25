#coding=UTF-8

import sys
import datetime
import requests
from time import sleep
from info import months, messages
from configreader import readConfigData

class BotHandler:

	def __init__(self, token):
		self.api_url = "https://api.telegram.org/bot{}/".format(token)

	def send_message(self, chat_id, text):
		parameters = {"chat_id": chat_id, "text": text}
		method = "sendMessage"
		response = requests.post(self.api_url + method, parameters)

		return response


config_file = "{}.cfg".format(sys.argv[1])
token = readConfigData(config_file, sys.argv[2], "token")
chat_id = readConfigData(config_file, sys.argv[2], "chat_id")

bot = BotHandler(token)

run_script = True
notified = False
last_notification = None


def main():

	global last_notification

	while run_script:

		now = datetime.datetime.now()
		today = now.day
		month = now.month
		hour = now.hour

		#SE O DIA MUDAR, ALTERA A VARIÁVEL QUE CHECA SE JÁ HOUVE NOTIFICAÇÃO
		if today != last_notification:
			notified = False

		if today == 10 and notified == False and hour > 11:
			bot.send_message(chat_id, messages[today].format(months[month+1 if month != 12 else 1], months[month+1 if month != 12 else 1]))
			notified = True
			last_notification = today

		elif today == 13 and notified == False and hour > 11:
			bot.send_message(chat_id, messages[today].format(months[month+1 if month != 12 else 1]))
			notified = True
			last_notification = today

		elif today == 15 and notified == False and hour > 11:
			bot.send_message(chat_id, messages[today].format(months[month+1 if month != 12 else 1]))
			notified = True
			last_notification = today

		elif today == 19 and notified == False and hour > 11:
			bot.send_message(chat_id, messages[today])
			notified = True
			last_notification = today

		elif today == 20 and notified == False and hour > 11:
			bot.send_message(chat_id, messages[today])
			notified = True
			last_notification = today

		elif today == 25 and notified == False and hour > 11:
			bot.send_message(chat_id, messages[today])
			notified = True
			last_notification = today

		elif today == 27 and notified == False and hour > 11:
			bot.send_message(chat_id, messages[today])
			notified = True
			last_notification = today

		elif today == 28 and notified == False and hour > 11:
			bot.send_message(chat_id, messages[today])
			notified = True
			last_notification = today

		elif today == 30 and notified == False and hour > 11:
			bot.send_message(chat_id, messages[today])
			notified = True
			last_notification = today

		sleep(7200)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

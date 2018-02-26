#coding=UTF-8

import datetime
from time import sleep
from info import months, messages

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

		today = 10

		#SE O DIA MUDAR, ALTERA A VARIÁVEL QUE CHECA SE JÁ HOUVE NOTIFICAÇÃO
		if today != last_notification:
			notified = False

		if today == 10 and notified == False and hour > 10:
			print messages[today].format(months[month+1 if month != 12 else 1])
			notified = True
			last_notification = today

		elif today == 13 and notified == False and hour > 10:
			print messages[today].format(months[month+1 if month != 12 else 1])
			notified = True
			last_notification = today

		elif today == 15 and notified == False and hour > 10:
			print messages[today].format(months[month+1 if month != 12 else 1])
			notified = True
			last_notification = today

		elif today == 19 and notified == False and hour > 10:
			print messages[today]
			notified = True
			last_notification = today

		elif today == 20 and notified == False and hour > 10:
			print messages[today]
			notified = True
			last_notification = today

		elif today == 25 and notified == False and hour > 10:
			print messages[today]
			notified = True
			last_notification = today

		elif today == 28 and notified == False and hour > 10:
			print messages[today]
			notified = True
			last_notification = today

		elif today == 30 and notified == False and hour > 10:
			print messages[today]
			notified = True
			last_notification = today

		else:
			print "Não publicar nada."

		sleep(3) #120

main()
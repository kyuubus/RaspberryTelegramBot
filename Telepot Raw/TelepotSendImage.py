#!/usr/bin/env python3
import telepot

chat_id = 54438947 #edit this with your own chat id
bot = telepot.Bot('7972098389:AAGyJnB1JJPkVI8QHd8_28tYCyrVdwMM') #edit tthis with yout own telegram bot token
def alert():  
        #bot.sendPhoto(chat_id, photo = open('/home/pi/4.png', 'rb'))
        bot.sendMessage(chat_id, 'start')
        return()

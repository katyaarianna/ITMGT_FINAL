#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd
import time
import requests
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

def get_data():
    #this accesses a website that supposedly updates the vaccination data daily
    df=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")
    #this part gets the current date and converts it into the format of the csv file
    result = time.localtime(time.time())
    today=str(result.tm_year)+"-"+str(result.tm_mon)+"-"+str(result.tm_mday)
    #basically just filtered the data so we have the # of people fully vaccinated today, and daily # of vaccinations
    ph=df["location"].str.contains("Philippines")
    date=df[ph].iloc[-1]
    fully_vaxxed=date["people_fully_vaccinated"]
    vax_rate=date["daily_vaccinations"]
    return (vax_rate,fully_vaxxed)


def bop(update: Update, context: CallbackContext):
    data=get_data()
    chat_id = update.message.chat_id
    context.bot.sendMessage(chat_id, data)

def main():
    updater = Updater('1906421584:AAHnIufgiPparqdD6kvYRtUjgvN5xdtwUu4')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()


# In[ ]:


import csv
import pandas as pd
import time
import requests
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

#this accesses a website that supposedly updates the vaccination data daily
df=pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")
#this part gets the current date and converts it into the format of the csv file
result = time.localtime(time.time())
today=str(result.tm_year)+"-"+str(result.tm_mon)+"-"+str(result.tm_mday)
#basically just filtered the data so we have the # of people fully vaccinated today, and daily # of vaccinations
ph=df["location"].str.contains("Philippines")
date=df[ph].iloc[-1]
latest['date']
fully_vaxxed=date["people_fully_vaccinated"]
vax_rate=date["daily_vaccinations"]
print(vax_rate,fully_vaxxed)


# In[ ]:





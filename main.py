import time
from importlib import reload
from pickle import NONE
from sqlite3 import Time
from bs4 import BeautifulSoup
import telebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import replace
import requests

# Por informações do seu bot.########
api_key = '5650157973:AAHoljPGgxNeyVmk-lGzE1-YiKVsaJ--45w'  # TOKEN DO SEU BOT
chat_id = '-1001829510303' # ID DO CANAL pladix
#####################################
bot = telebot.TeleBot(token=api_key)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)

nav.get('https://blaze.com/pt/games/double')



analisar_pandão1 = 0 
analisar_pandão2 = 0
analisar_pandão3 = 0 
analisar_pandão4 = 0
analisar_pandão5 = 0 
analisar_pandão6 = 0
analisar_pandão7 = 0 
analisar_pandão8 = 0
analisar_pandão9 = 0 
analisar_pandão10 = 0
analisar_pandão11 = 0 
analisar_pandão12 = 0
analisar_pandão13 = 0 
analisar_pandão14 = 0




analisar_open = 0
resultsDouble = []

mensage_ids = 0
mensage_delete = False


while True:

    def alert_olhar():
            global mensage_ids
            global mensage_delete

            message_id = bot.send_message(
            chat_id, text='''
⚠️ DE OLHO NA BLAZE ⚠️
            ''').message_id
            mensage_ids = message_id
            mensage_delete = True
            return  
    def delet_olhar():
        global mensage_ids
        global mensage_delete

        if  mensage_delete == True:
            bot.delete_message(chat_id=chat_id, message_id=mensage_ids)
            mensage_delete = False
        
    def alert_entra():
            global mensage_ids
            global mensage_delete

            message_id = bot.send_message(
            chat_id, text='''
PADRÃO DO BRANCO ⚪️ 🧨
ENTRADA AGORA 🔥
🎰
            ''').message_id
            mensage_ids = message_id
            mensage_delete = True
            return  
    def delet_entra():
        global mensage_ids
        global mensage_delete

        if  mensage_delete == True:
            bot.delete_message(chat_id=chat_id, message_id=mensage_ids)
            mensage_delete = False

    def qualnum(x):
        if x == '0':
            return '0'

        if x == '1':
            return '1'

        if x == '2':
            return '2'

        if x == '3':
            return '3'

        if x == '4':
            return '4'

        if x == '5':
            return '5'

        if x == '6':
            return '6'

        if x == '7':
            return '7'

        if x == '8':
            return '8'

        if x == '9':
            return '9'

        if x == '10':
            return '10'

        if x == '11':
            return '11'

        if x == '12':
            return '12'

        if x == '13':
            return '13'

        if x == '14':
            return '14'
    def qualcor(x):
        if x == '0':
            return 'b'

        if x == '1':
            return 'n'

        if x == '2':
            return 'n'

        if x == '3':
            return 'n'

        if x == '4':
            return 'n'

        if x == '5':
            return 'n'

        if x == '6':
            return 'n'

        if x == '7':
            return 'n'

        if x == '8':
            return 'n'

        if x == '9':
            return 'n'

        if x == '10':
            return 'n'

        if x == '11':
            return 'n'

        if x == '12':
            return 'n'

        if x == '13':
            return 'n'

        if x == '14':
            return 'n'
    def qualcor1(x):
        if x == '0':
            return 'B'

        if x == '1':
            return 'V'

        if x == '2':
            return 'V'

        if x == '3':
            return 'V'

        if x == '4':
            return 'V'

        if x == '5':
            return 'V'

        if x == '6':
            return 'V'

        if x == '7':
            return 'V'

        if x == '8':
            return 'P'

        if x == '9':
            return 'P'

        if x == '10':
            return 'P'

        if x == '11':
            return 'P'

        if x == '12':
            return 'P'

        if x == '13':
            return 'P'

        if x == '14':
            return 'P'

       
    try: 
        resulROOL = nav.find_element(
        By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    except NameError as erro:
        print
        print
    except Exception as erro:
        print

    if resulROOL == 'Girando...':
        analisar_open = 1 
        print('Analisando')
        time.sleep(13) 
        c = nav.page_source
        resultsDouble.clear()
        
        soup = BeautifulSoup(c, 'html.parser')
        go = soup.find('div', class_="entries main")
        for i in go:
            if i.getText():
                resultsDouble.append(i.getText())
            else:
                resultsDouble.append('0')
        
        resultsDouble = resultsDouble[:-1]
        
        if analisar_open == 1:

            default = resultsDouble[0:24]
            

            mapeando = map(qualnum, default)
            mapeando2 = map(qualcor, default)
            mapeando3 = map(qualcor1, default)
           
            finalnum = list(mapeando)
            finalcor = list(mapeando2) 
            finalcor3 = list(mapeando3) 
    
 
            print(finalcor[0:5])
            print(finalnum[0:5])
            
            

            def CHECK_VERSION(num):
                global analisar_pandão1
                 
                if analisar_pandão1 == 0:
                    if num[0:1] == ['n']:
                        global ns1, ns2
                        ns1 = finalnum[0:1]
                        ns2 = finalnum[0:1]
                        analisar_pandão1 = 1
                        bot.send_message(chat_id=chat_id, text=('{}'.format(ns1)))
                        print (ns1)
                        return 
                    
                elif analisar_pandão1 == 1:
                    if num[0:1] == ['n']:
                        analisar_pandão1 = 2
                        bot.send_message(chat_id=chat_id, text='passei aqui')
                        return
                    
                elif analisar_pandão1 == 2:    
                    if  finalnum[0:1] == ns2:
                        analisar_pandão1 = 0
                        bot.send_message(chat_id=chat_id, text='ola')
                        print ('{}'.format(ns1))
                        return    
                    else:
                        analisar_pandão1 = 1   
                        bot.send_message(chat_id=chat_id, text='Nuemro Em Analise {}'.format(ns1))
                        return
                    

            checkVersion = CHECK_VERSION(finalnum)
            checkVersion = CHECK_VERSION(finalcor)
            checkVersion = CHECK_VERSION(finalcor3)

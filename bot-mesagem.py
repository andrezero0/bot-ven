import telebot
import time
import openpyxl


api_key = '6032335278:AAHNq4jtnyNtUNpQP0SHHFRl2YPYH_1bEMY'

bot = telebot.TeleBot(token= api_key)

baak = openpyxl.load_workbook('uids.xlsx')
vall = baak['Sheet']

texto = '''
Fala Jogador! 

Trago boas noticias.

Atualizamos nossos vips, estamos com o catalogo de salas vips
maoir, para conferir basta usar /Catalogo para ter acesso.

Com o codigo: free05

Você tem disconto de 5 reias em qualquer sala vip, faça a 
compra do seu vip e desconte os 5 e envie o comprovante 
para t.me/BossAtendimento01 e fale que usou o 
codigo: free05.



não fique de fora dessa!  🔥🔥
'''

linha = 1

while True:

    uid = vall[f'A{linha}'].value
    print(f'Mensagem enviada para o id: {uid}')
    bot.send_message(chat_id=uid, text= texto)
    time.sleep(1)
    linha = linha +1

    if linha == 17:
        quit()

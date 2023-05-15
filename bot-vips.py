import telebot
import time



chave_api = '6032335278:AAHNq4jtnyNtUNpQP0SHHFRl2YPYH_1bEMY'

bot = telebot.TeleBot(chave_api)


@bot.message_handler(commands= ['ROBO_BLAZE_LIMBO'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 40 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')


@bot.message_handler(commands= ['ROBO_BLAZE_DICE'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 40 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')
    

@bot.message_handler(commands= ['BOT_BLAZE_DOUBLE'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 20 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')

    
@bot.message_handler(commands= ['BOT_BLAZE_BRANCO'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 30 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')

    
@bot.message_handler(commands= ['BOT_BLAZE_CRASH'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 20 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')
    
    
@bot.message_handler(commands= ['BOT_BLAZE_MINES'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 40 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')
    

@bot.message_handler(commands= ['BOT_ESTRELA_BET'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 30 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')
    

@bot.message_handler(commands= ['BOT_AVIATO'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 30 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')
    

@bot.message_handler(commands= ['BOT_ESTRELA_BET_SPACEMAN'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 40 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')
    

@bot.message_handler(commands= ['BOT_BRABET_DOUBLE'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 30 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')    
    

@bot.message_handler(commands= ['BOT_BRABET_CRASH'])
def info(mensagem):
    bot.reply_to(mensagem,'''
Faça sua assinatura vitalicia

Valor da Compra 30 reais:

PIX bossblazevip@gmail.com

Envie seu /Comprovante''')   
    

@bot.message_handler(commands= ['Comprovante'])
def info(mensagem):
    bot.reply_to(mensagem,'''SEUPORTE @Boss_Suport''')   




def verificar(mensagem):
    return True

@bot.message_handler(func= verificar)
def responder(mensagem):
    texto = f'''

Olá,  {mensagem.chat.first_name}

ESCOLA UM DOS VIP ABAIXO, PRA GANHA DINHEIRO! 🍀

🎰 /ROBO_BLAZE_LIMBO

🎰 /ROBO_BLAZE_DICE

🎰 /BOT_BLAZE_DOUBLE

🎰 /BOT_BLAZE_BRANCO

🎰 /BOT_BLAZE_CRASH

🎰 /BOT_BLAZE_MINES

🎰 /BOT_ESTRELA_BET

🎰 /BOT_AVIATO

🎰 /BOT_ESTRELA_BET_SPACEMAN

🎰 /BOT_BRABET_DOUBLE

🎰 /BOT_BRABET_CRASH

ESCOLHA SEU VIP AGORA!! 🔥🔥
'''

    bot.reply_to(mensagem, texto)

bot.polling(non_stop= True)
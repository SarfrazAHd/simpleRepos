import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

os.system('color 7f')  # coloring background of terminal

bot = ChatBot('Test')
conv = open("Data.txt", 'r').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)

while 1:
    msg = input("You: ")
    if msg.strip() != 'Bye':
        reply = bot.get_response(msg)
        print("Bot:", reply)

    if msg.strip() == 'Bye':
        print("Boat: Bye ")
        break

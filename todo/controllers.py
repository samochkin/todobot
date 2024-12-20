import telebot
from models import TaskModel

class Controller:
    def __init__(self, bot):
        self.bot:telebot = bot

    def register_handlers(self):
        @self.bot.messege_handler(commands = ['stars'])
        def send_welcome(messege):
            self.bot.reply_to(messege, "Это Todo-бот")

        @self.bot.messege_handler(commands = ['add'])
        def add_task(messege):
            msg = self.bot.reply_to(messege, "Введите текст задачи:")
            self.bot.register_next_step_handler(msg, self.add_task_handlerop)

from django.core.management.base import BaseCommand
from bot_tlg.handlers import bot
class Command(BaseCommand):
    help = 'Запустить телеграм-бот'

    def handle(self, *args, **options):
        bot.infinity_polling()
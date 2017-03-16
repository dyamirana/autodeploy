import random
from plugin_system import Plugin

# Инициализируем возможные ответы
greetings = ['Слава Украине!', '🌚 Кекеке', 'Запущен и готов служить!', 'У контакта ужасный флуд-контроль',
             'Хуяк-хуяк и в продакшн']

plugin = Plugin('Приветствие',
                usage="привет - поприветствовать пользователя")


@plugin.on_command('привет', 'приветствие', 'голос', 'ку')
async def call(msg, args):
    await msg.answer(random.choice(greetings))

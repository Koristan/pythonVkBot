from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle.user import User
from vkbottle.bot import Bot, Message
from vkbottle.api import API

import config
from helpers import Helpers

client = Bot(config.BOT_TOKEN)

is_review = False
is_rewrite = False
is_product = False
is_product_stage_2 = False
is_problem = False

# Общая клавиатура "Назад"
keyboard_back = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Назад"))
)

# Клавиатура для "Старт"
keyobard_start = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Оставить отзыв о товаре"))
    .row()
    .add(Text("Сотрудничество"))
    .row()
    .add(Text("Информация о товаре"))
    .row()
    .add(Text("Проблема"))
    .add(Text("Где купить"))
    .get_json()
)

# Клавиатура Продуктов
keyboard_product = (
    Keyboard(one_time=True, inline=False)
    .add(Text('Гель для стирки IDIALITI орхидея 5л'))
    .row()
    .add(Text("Другой товар"))
    .row()
    .add(Text("Назад"))
)

# Клавиатура маркетплейсов
keyboard_markets = (
    Keyboard(one_time=True, inline=False)
    .add(Text('Ozon'))
    .row()
    .add(Text("Wildberries"))
    .row()
    .add(Text("Назад"))
)

@client.on.private_message(text=["Начать", "начать", "старт", "Старт", "Назад"])
async def echo_start(ans: Message):
    helper = Helpers()
    name = await helper.get_user_name(ans)
    await ans.answer(
        message = f'{name}, добрый день! Укажите тему вопроса.',
        keyboard = keyobard_start
    )
  

@client.on.private_message(text=["Оставить отзыв о товаре"])
async def echo_reviews(ans: Message):
    
    await ans.answer(
        message = 'Отзыв о товаре Вы можете оставить по ссылке https://vk.com/reviews-227973529 или написать здесь',
        keyboard = keyboard_back
    )
    global is_review
    is_review = True


@client.on.private_message(text=["Сотрудничество"])
async def echo_both(ans: Message):
    helper = Helpers()
    name = await helper.get_user_name(ans)
    
    await ans.answer(
        message = f'{name}, напишите нам адрес своей электронной почты или аккаунт в телеграмм. Мы с Вами свяжемся в ближайшее рабочее время.',
        keyboard = keyboard_back
    )
    global is_rewrite
    is_rewrite = True
    

@client.on.private_message(text=["Информация о товаре"])
async def echo_about(ans: Message):
    global is_product
    await ans.answer(
        message = f'Какой товар Вас интересует?',
        keyboard = keyboard_product
    )
    is_product = True

  
@client.on.private_message(text=['Гель для стирки IDIALITI орхидея 5л', 'Другой товар'])
async def echo_products(ans: Message):
    global is_product
    await ans.answer(
        message = 'Опишите Ваш вопрос, и мы ответим Вам в ближайшее время.',
        keyboard = keyboard_back        
    )
    is_product = True
    
@client.on.private_message(text=["Проблема"])
async def echo_about(ans: Message):
    global is_problem
    await ans.answer(
        message = 'Опишите Вашу проблему, и мы решим ее в ближайшее время.',
        keyboard = keyboard_back        
    )
    is_problem = True

@client.on.private_message(text=["Где купить"])
async def echo_about(ans: Message):
    global is_problem
    await ans.answer(
        message = 'Укажите платформу, которая Вас интересует.',
        keyboard = keyboard_markets        
    )
    is_problem = True
    
@client.on.private_message(text=["Ozon"])
async def echo_about(ans: Message):
    await ans.answer(
        message = 'https://clck.ru/3EBKba',
        keyboard = keyboard_back        
    )
    
@client.on.private_message(text=["Wildberries"])
async def echo_about(ans: Message):
    await ans.answer(
        message = 'https://clck.ru/3EBK54',
        keyboard = keyboard_back        
    )
  
@client.on.private_message()
async def echo_all(ans: Message):
    
    global is_review    
    global is_rewrite
    global is_product
    global is_problem
    
    if (is_review and ans != 'Назад'):
        await ans.answer(
            message = 'Ваш отзыв сохранен. Он пройдет модерацию и будет выложен на сайт.',
            keyboard = keyboard_back
        )
    elif (is_rewrite and ans != "Назад"):
        await ans.answer(
            message = 'Ваше обращение сохранено. Мы свяжемся с Вами в ближайшее рабочее время.',
            keyboard = keyboard_back
        )
    elif (is_product and ans != "Назад"):
        await ans.answer(
            message = 'Ваш вопрос отправлен. Мы свяжемся с Вами в ближайшее время.',
            keyboard = keyboard_back
        )
    elif (is_problem and ans != "Назад"):
        await ans.answer(
            message = 'Мы увидели вашу проблему. Мы решим ее в ближайшее время.',
            keyboard = keyboard_back
        )
        
    is_review = False
    is_rewrite = False
    is_product = False
    is_problem = False
    
if __name__ == "__main__":
    client.run_forever()

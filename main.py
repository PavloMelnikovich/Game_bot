import logging
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters
from db import users_collection
import uuid

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# States
START = 1
QUESTION_1 = 2
QUESTION_2 = 3
QUESTION_3 = 4
QUESTION_4 = 5
QUESTION_5 = 6
END = 7

user_states = {}

updater = Updater(token="5708404670:AAEY6TyowFaRP7guPtAYbgb_cnSX1Az2HYE", use_context=True)
dispatcher = updater.dispatcher

def start_command_handler(update: Update, context: CallbackContext):
    global user_states
    
    user_id = update.effective_chat.id
    
    # If user not in states - add him / her
    if user_id not in user_states:
        user_states[user_id] = START
        
    print(f"[/start]: current user state: {user_states[user_id]}")
        
    # Check state of current user
    if user_states[user_id] == START:
        text = "Ви звичайний солдат в армії Короля Артура. Ви прокидаетесь в казармі від звуків битви, вставши з ліжка і підійшовши до вікна ви бачите битву яка відбувается прямо під стінами замка. Що ви будите робити?\n1: Йти спати дальше\n2: Швидко одягнути броню і відправитись в бій"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        user_states[user_id] += 1
    else:
        pass

def text_message_handler(update: Update, context: CallbackContext):
    message = update.message.text
    user_id = update.effective_chat.id
    
    global user_states
    
    print(f"[text]: current user state: {user_states[user_id]}")
    
    if user_states[user_id] == QUESTION_1:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Після огляду поля битви з вікна замка ви обернулись і сказавши -Не мої проблеми-, відпрвились назад в ліжко")
            user_states[user_id] = 1
            text = "Через те що ви ніяк не помогли в битві ваш замок було зруйновано. Гра закінчена. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif message == "2":
            text = "Швидко одягнувши броню, ви відправились на поле бою. Прийшовши ви побачили як армія мертвеців атакує ваших побратимім, також ви побачили як головний Некромант хоче убити найкращого воїна королівства. Які будуть ваші дії?\n1: Побігти до Некроманта і захистити найкращого воїна\n2: Кинутись помагати звичайним воякам"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
    elif user_states[user_id] == QUESTION_2:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Відбивши удар Некроманта ви врятували найкращого воїна, піднявшись на ноги він знову ринувся в бій. Після недовгої дуелі Некромант знову почав брати верх в битві, тому найкращий воїн прийняв рішення і крикнув -Відходим до воріт замка-.Що ви будите робити?\n1: Послухатися наказу і відійти до воріт \n2: Не послухати і побігти прямо на ворога")
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Ви почали битися разом з звичайними вояками. Найкращий воїн був вбитий і армія мервеців почала массивний наступ")
            user_states[user_id] = 1
            text = "Вас було вбито під час битви під стінами замка. Гра закінчена. Введіть /start, щоб почати знову."
    elif user_states[user_id] == QUESTION_3:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Після відходу до замка ви одразу закрили ворота і виграли собі трохи часу. Після чого ви швидко познайомились з воїном, він назвався Річард, одразу після знайомства ви почали роздумувати план дій. Який буде план?\n1: Послати декількох солдат щоби ті почали евакуацію мирного населення з міста, а самим оборонняти прохід і виграти максимум часу\n2: Наказати людям обороняти ворота, а самим побігти в троний зал и врятувати короля")
            user_states[user_id] += 1
    elif user_states[user_id] == QUESTION_4:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Відправивши людей ви почали оборону ворот, через декілька хвилин мертвецям все таки вдалось зламати ворота і вони почали атаку. Ви почали відбивати хвилі ворогів, але їх ставало все більше і більше. Ви змогли оборонятися 3 години, за цей час все населення міста було успішно врятованно, але помер король якого так і не змогли врятувати.")
            user_states[user_id] = 1
            text = "Ви померли як народний герой, в вашу честь люди складали багато казок і легенд. Але через смерть короля вас не признали героем королівства и почали ненавидіти серед дворянської знаті. Також свою ненавість до вас знать перенесла і на ваших потомків. Гра закінчена. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Після прибудтя в замок ви разом з Річардом побачили мертву сторожу короля. Увійшовши до троного залу ви побачили як ворожий ассасін намагается вбити короля. Які будут ваші дії?\n1: Відправитись самому в бій з ворогом\n2: Направитись до короля і допомогти йому залишивши ассасіна на Річарда")
            user_states[user_id] += 1
    elif user_states[user_id] == QUESTION_5:
        if message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Ви підбігли до короля і допомогли йому, за цей час Річард вступив в бій з ворогом. Під час битви Річарда сильно ранили і він не зміг продовжувати бій, тоді ви вхопилися за меч і вступили в бій з ассасіном. Після тяжкого поединку ви все таки взяли верх і вбили ворога, одразу після цього ви побігли до Річарда але вже було пізно. Тоді ви взяли короля і втекли разом з ним з замку")
            user_states[user_id] = 1
            context.bot.send_message(chat_id=update.effective_chat.id, text="Після втечі з замку вм відправились до найближчого міста і швидко зібрали армію для того щоб відбити замок. Коли ви разом з воїнами прибули до замка ви побачили лише розвалини, ви відправились блукати по вулицям в надії знайти хочаб якесь населення, але все що ви знаходили це трупи і ворогів. Замок було зруйноване")
            text = "Вас було нагородженно званням найкращого воїна королівства, але ця нагорода далась вам ціною тисячох життів. Серед дворянської знаті вас почали поважати, але народ вас ненавидів, до кінця свого життя ви прожили самотнім. Гра закінчена. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    else:
        pass

start_handler = CommandHandler('start', start_command_handler)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler)
dispatcher.add_handler(echo_handler)

# Start bot
updater.start_polling()
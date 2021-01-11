import pymongo
import requests
import json
import time
from mdb import parser_FEFU

###
client = pymongo.MongoClient('localhost', 27017)
db = client['FEFU_Bot']
coll = db['People']
###
token = '1591256992:AAEIlEOg7GfD443LJ3cEY0AZsRHMkdSEis8'
name = '@FEFU_T_Bot'
T_bot_url = 'https://api.telegram.org/bot' + token + '/'
global offset
global change_id


###
def KB():
    result = coll.find()
    keyboard = {'one_time_keyboard': True,
                'selective': True}
    list_but = []
    for ddict in result:
        for key, value in ddict.items():
            if key == 'Должность':
                position = value
                but = [{'text': position}]
                list_but.append(but)
    keyboard['keyboard'] = list_but
    kb = json.dumps(keyboard)
    return kb


def KB_pos(position):
    result = coll.find_one({'Должность': position})
    keyboard = {'one_time_keyboard': True}
    list_but = []
    for key, value in result.items():
        if key == '_id':
            global change_id
            change_id = value
        elif key == 'Должность':
            continue
        else:
            t = key + ':' + value
            but = [{'text': key}]
            list_but.append(but)
    keyboard['keyboard'] = list_but
    kb = json.dumps(keyboard)
    return kb


###
global last_text
last_text = ''

global last_upd_id
last_upd_id = 0

global current_admin
current_admin = ''

global flag
flag = False


def getUpdate(offset):
    url = T_bot_url + 'getupdates?offset={}'.format(offset)
    req = requests.get(url)
    return req.json()


def get_msg(ddict):
    update_result = ddict['result'][-1]
    update_id = update_result['update_id']
    global offset
    if ddict['ok']:
        for message in ddict['result']:
            offset = message['update_id']
    # print(offset)
    global last_upd_id
    if last_upd_id != update_id:
        last_upd_id = update_id
        try:
            msg = {
                'Chat_id': update_result['message']['chat']['id'],
                'Text': update_result['message']['text'],
                'User': update_result['message']['from']['username'],
                'user_id': update_result['message']['message_id']

            }
        except KeyError:
            return None
        print(msg['user_id'])
        return msg
    else:
        return None


def url_k(chat_id, answer, user_id, keyboard):
    URL = T_bot_url + 'sendMessage?chat_id={}&text={}&reply_to_message_id={}&reply_markup={}'.format(chat_id, answer,
                                                                                                     user_id, keyboard)
    requests.get(URL)


def get_administrator(chat_id, username):
    URL = T_bot_url + 'getChatAdministrators?chat_id={}'.format(chat_id)
    r = requests.get(URL)
    # print(r.json())
    list_user_data = r.json()['result']
    admin_l = []
    for i in list_user_data:
        user = i['user']['username']
        admin_l.append(user)
    if username in admin_l:
        return True
    else:
        return False


def url_wk(chat_id, answer):
    URL = T_bot_url + 'sendmessage?chat_id={}&text={}'.format(chat_id, answer)
    requests.get(URL)


def find_people(position):
    ddict = coll.find_one({'Должность': position})
    answer = "Должность:{}\nФамилия:{}\nИмя:{}\nОчество:{}\nКабинет:{}\nТелефон:{}\nПочта:{}".format(
        ddict['Должность'], ddict['Фамилия'], ddict['Имя'], ddict['Очесство'], ddict['Кабинет'],
        ddict['Телефон'], ddict['Почта'])
    return answer


def delete_people(position):
    coll.delete_one({'Должность': position})


def inserOne(list):
    print(len(list))
    if len(list) < 7:
        for i in range(7 - len(list)):
            list.append('None')
    ddict = {'Должность': list[0],
             'Фамилия': list[1],
             'Имя': list[2],
             'Очесство': list[3],
             'Кабинет': list[4],
             'Телефон': list[5],
             'Почта': list[6]}
    coll.insert_one(ddict)


def updateOne(data):
    global change_id
    coll.update_one({'_id': change_id}, {'$set': data})


def chek_admin(admin):
    global current_admin
    global flag
    if admin == current_admin:
        flag = True
    else:
        flag = False


def Answer(chat_id, users_msg, user_name, user_id):
    is_admin = get_administrator(chat_id, user_name)
    print(users_msg)
    global last_text
    global current_admin
    change_list = ['Фамилия', 'Имя', 'Очесство', 'Кабинет', 'Телефон', 'Почта']
    if users_msg == '/info' or users_msg == '/info@FEFU_T_Bot':
        last_text = users_msg
        url_k(chat_id, "Choose position.", user_id, KB())
    elif users_msg == '/edit' or users_msg == '/edit@FEFU_T_Bot':
        if is_admin:
            answer = 'Выбирете'
            keyboard = json.dumps({'one_time_keyboard': True,
                                   'selective': True,
                                   'keyboard': [
                                       [{'text': 'Изменить'}],
                                       [{'text': 'Добавить'}],
                                       [{'text': 'Удалить'}]
                                   ]
                                   })
            url_k(chat_id, answer, user_id, keyboard)
            current_admin = user_name
        else:
            answer = 'You dont have permition!'
            url_wk(chat_id, answer)
    elif users_msg == 'Изменить' and current_admin == user_name:
        last_text = users_msg
        url_k(chat_id, 'Выбирете должность которую хотите измениьть', user_id, KB())
    elif users_msg == 'Добавить' and current_admin == user_name:
        last_text = users_msg
        url_wk(chat_id, 'Введите данные:\nДолжность\nФамилия\nИмя\nОчетсво\nКабинет\nТелефон\nПочта')
    elif users_msg == 'Удалить' and current_admin == user_name:
        last_text = users_msg
        url_k(chat_id, 'Выбирете то что необходимо удалить.', user_id, KB())
    elif last_text == '/info' or last_text == '/info@FEFU_T_Bot' and current_admin == user_name:
        try:
            url_wk(chat_id, find_people(users_msg))
        except TypeError:
            return 0
    elif last_text == 'Изменить' and current_admin == user_name:
        last_text = 'change'
        url_wk(chat_id, 'Введите данные по типу - Изменяемое поле:данные')
        r = coll.find_one({'Должность': users_msg})
        global change_id
        change_id = r['_id']
        print(change_id)
    elif last_text == 'change' and current_admin == user_name:
        text = users_msg.split(':')
        if text[0] in change_list and len(text) == 2:
            data = {text[0]: text[1]}
            updateOne(data)
            answer = 'Данные обновленны'
        else:
            answer = 'Невверный ввод данных'
        url_wk(chat_id, answer)
    elif last_text == 'Добавить' and current_admin == user_name:
        data_list = users_msg.split('\n')
        inserOne(data_list)
        url_wk(chat_id, 'Данные добавленны')
    elif last_text == 'Удалить' and current_admin == user_name:
        delete_people(users_msg)
        url_wk(chat_id, 'Данные удаленны')
    else:
        return 0
        print(users_msg)
        answer = "Unknown commands"
        url_wk(chat_id, answer)


if __name__ == '__main__':
    url = T_bot_url + 'getupdates'
    req = requests.get(url)
    m = req.json()
    global offset
    offset = m['result'][-1]['update_id']
    if m['ok']:
        for message in m['result']:
            offset = message['update_id']
            # print(offset)
    time_start = time.time()
    # parser_FEFU()
    while True:
        if (time.time() - time_start) > 86400:
            parser_FEFU()
            time_start = time.time()
        # print(getUpdate())
        msg = get_msg(getUpdate(offset))
        # get_administrator(msg['Chat_id'])
        # print(msg)
        if msg != None:
            Answer(msg['Chat_id'], msg['Text'], msg['User'], msg['user_id'])
        time.sleep(3)

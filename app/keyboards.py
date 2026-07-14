from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)
from time import strftime
import os

month, month_1 = strftime('%y'), str(int(strftime('%y')) - 1)
year, year_1, year_2 = strftime('%Y'), str(int(strftime('%Y')) - 1), str(int(strftime('%Y')) - 2)
year_3, year_4, year_5 = str(int(strftime('%Y')) - 3), str(int(strftime('%Y')) - 4), str(int(strftime('%Y')) - 5)

pochta = KeyboardButton(text='📨 Почта')
email = KeyboardButton(text='📨 Бимгор', style='success')
otchet = KeyboardButton(text="📝 Отчет")
dolgi = KeyboardButton(text='📕 Долги')
serdyuch = KeyboardButton(text='🚻 Сердюченко')
forma_fasad = KeyboardButton(text='🚪 Фасады', style='success')
zarplata = KeyboardButton(text='💰 Зарплата')
klient = KeyboardButton(text='👨‍💼 Клиенты')
info_zakaza = KeyboardButton(text='❗Инфо по заказу')
obnovit = KeyboardButton(text=f"🔄 Обновить", style='success')
kursi_valyut = KeyboardButton(text='💵 Курсы валют', style='success')
zametki = KeyboardButton(text='📝Заметки', style='success')
raskroy = KeyboardButton(text='🪚 Раскрой')
frezer = KeyboardButton(text='🕹 Фрезер')
press = KeyboardButton(text='⚙️ Пресс')
price = KeyboardButton(text='💷 Стоимость', style='primary')
plenka = KeyboardButton(text='🟧 Пленки', style='danger')
st_plenka = KeyboardButton(text='📊 Статистика')
raskroy_ostatok = KeyboardButton(text='🪚 Раскрой/ост.')
raskroy_zarplata = KeyboardButton(text='🪚 Раскрой/зар.')
client_all = KeyboardButton(text='⚙️ Мои заказы')
client_credit = KeyboardButton(text='⚙️ Мои долги')

bot_kb = [
    [KeyboardButton(text=f"Обновить {year}", style='success'),
     KeyboardButton(text=f"Обновить {year_1}", style='danger'),
     KeyboardButton(text='Доп. кнопки', style='primary')],
    [zametki, KeyboardButton(text='Срочность', style='danger'), KeyboardButton(text='Заказы', style='primary')],
    [dolgi, pochta, otchet],
    [klient, email, zarplata],
    [raskroy, frezer, press],
    [forma_fasad, plenka, price],
    [st_plenka, info_zakaza, raskroy_ostatok]
]
vova_kb = [[obnovit, pochta, otchet],
           [klient, dolgi, zarplata],
           [raskroy, frezer, press],
           [st_plenka, info_zakaza, raskroy_ostatok],
           [forma_fasad, plenka, price],
           [raskroy_zarplata, email],
           ]

serdyuch_kb = [[KeyboardButton(text=f"Обновить {year}", style='success'),
                KeyboardButton(text=f"Обновить {year_1}", style='danger')],
               [forma_fasad, plenka, price]]

shef_kb = [[obnovit, pochta, otchet],
           [klient, dolgi, zarplata],
           [serdyuch, info_zakaza, st_plenka],
           [raskroy, frezer, press],
           [forma_fasad, plenka, price],
           ]

all_user = [[forma_fasad, plenka, price]]

client_kb = [[forma_fasad, plenka, price], [client_all, client_credit]]

ellion_kb = [[forma_fasad, plenka, price]]

admin_kb = [[KeyboardButton(text='Объявление'), KeyboardButton(text='Картинка'), KeyboardButton(text='Аккаунты')],
            [KeyboardButton(text='Добавить'), KeyboardButton(text='Обновить'), KeyboardButton(text='Удалить')],
            [KeyboardButton(text='Рестарт ПК'), KeyboardButton(text='✖ Отмена'), KeyboardButton(text='🔄 Рестарт')],
            [KeyboardButton(text='🔙 Назад'), KeyboardButton(text='Переписать'), KeyboardButton(text='Акции')]]

frezer_kb = [[forma_fasad, price, frezer],
             [KeyboardButton(text='ss_станок'), KeyboardButton(text='nc_станок'), KeyboardButton(text='it_станок')],
             [KeyboardButton(text='✖ Отмена'), KeyboardButton(text='Архив'), KeyboardButton(text='+132 фреза')]]

frezer_nc = [[KeyboardButton(text='Подклад'), KeyboardButton(text='Подача')],
             [KeyboardButton(text='↩️ Назад'), KeyboardButton(text='✖ Отмена')]]

frezer_it = [[KeyboardButton(text='№ фрезы'), KeyboardButton(text='Толщина МДФ')],
             [KeyboardButton(text='↩️ Назад'), KeyboardButton(text='✖ Отмена')]]

kb_bot = ReplyKeyboardMarkup(keyboard=bot_kb, resize_keyboard=True)
kb_vova = ReplyKeyboardMarkup(keyboard=vova_kb, resize_keyboard=True)
kb_serdyuch = ReplyKeyboardMarkup(keyboard=serdyuch_kb, resize_keyboard=True)
kb_shef = ReplyKeyboardMarkup(keyboard=shef_kb, resize_keyboard=True)
kb_all_user = ReplyKeyboardMarkup(keyboard=all_user, resize_keyboard=True)
kb_admin = ReplyKeyboardMarkup(keyboard=admin_kb, resize_keyboard=True)
kb_frezer = ReplyKeyboardMarkup(keyboard=frezer_kb, resize_keyboard=True)
kb_frezer_nc = ReplyKeyboardMarkup(keyboard=frezer_nc, resize_keyboard=True)
kb_frezer_it = ReplyKeyboardMarkup(keyboard=frezer_it, resize_keyboard=True)
kb_clent = ReplyKeyboardMarkup(keyboard=client_kb, resize_keyboard=True)
kb_ellion = ReplyKeyboardMarkup(keyboard=ellion_kb, resize_keyboard=True)

kb_in = [[InlineKeyboardButton(text='156', callback_data="value_156"),
          InlineKeyboardButton(text='144_1', callback_data="value_144_1"),
          InlineKeyboardButton(text='144_2', callback_data="value_144_2"),
          InlineKeyboardButton(text='144_3', callback_data="value_144_3")],
         [InlineKeyboardButton(text='под 45', callback_data="value_45"),
          InlineKeyboardButton(text='136_1', callback_data="value_136_1"),
          InlineKeyboardButton(text='136_2', callback_data="value_136_2"),
          InlineKeyboardButton(text='136_3', callback_data="value_136_3")],
         [InlineKeyboardButton(text='Без хдф', callback_data="value_bez_xdf"),
          InlineKeyboardButton(text='RY=44.5', callback_data="value_ramy_45"),
          InlineKeyboardButton(text='под 92', callback_data="value_92"), ]
         ]

dop_knopki = [[InlineKeyboardButton(text="Del", callback_data="del_value", style='danger'),
               InlineKeyboardButton(text="Copy_it", callback_data="copyit_value_it", style='success'),
               InlineKeyboardButton(text="Copy_ss", callback_data="copyss_value_ss", style='success'),
               InlineKeyboardButton(text="Copy_nc", callback_data="copync_value_nc", style='success')],
              [InlineKeyboardButton(text="Папки", callback_data="papki_value"),
               InlineKeyboardButton(text="Copy", callback_data="copy_value"),
               InlineKeyboardButton(text="zk_Del", callback_data="zk_Del_value"),
               InlineKeyboardButton(text="Temp", callback_data="temp_value")],
              [InlineKeyboardButton(text="Файл", callback_data="fail_value"),
               InlineKeyboardButton(text="Скрин", callback_data="skrin_value"),
               InlineKeyboardButton(text="Процесс", callback_data="proc_value"),
               InlineKeyboardButton(text="Отметка", callback_data="otmetka_value")],
              [InlineKeyboardButton(text="Процесс + Отметка", callback_data="proc_otmetka_value"),
               InlineKeyboardButton(text='Удалить', callback_data="dir_delete", style='danger'),
               InlineKeyboardButton(text='Фасад', callback_data="do_facade")], ]

change_order = [[InlineKeyboardButton(text='Заказ №', callback_data="zakaz_value"),
                 InlineKeyboardButton(text='Добавить', callback_data="change_value")],]

static_plenka = [[InlineKeyboardButton(text="По номеру пленки", callback_data="static_plenki")],
                 [InlineKeyboardButton(text="По форме фасада", callback_data="static_fasad")],
                 [InlineKeyboardButton(text="По толщине МДФ", callback_data="static_mdf")]]

actions = [[InlineKeyboardButton(text="Просмотр", callback_data="view_actions", style='success')],
                 [InlineKeyboardButton(text="Редоктировать", callback_data="view_add_actions", style='primary')],
                 [InlineKeyboardButton(text="Финансы", callback_data="view_add_finance", style='danger')],]

number_fasad = [str(j) for j in sorted([int(i) for i in os.listdir('images')])]

mesyac = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
          'Декабрь']

letter = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
          'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Э', 'Ю', 'Я']

group = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

dolgi_year = [year, year_1, year_2]
client_year = [year, year_1, year_2, year_3, year_4, year_5]


def vivod_inlinekey(lst, number, call_txt):
    result, lst_temp = [], []
    for i in range(0, len(lst), number):
        for j in lst[i:i + number]:
            lst_temp.append(InlineKeyboardButton(text=j, callback_data=f'{call_txt}{j}'))
        result.append(lst_temp)
        lst_temp = []
    return result


dop_kn = InlineKeyboardMarkup(inline_keyboard=dop_knopki)
in_kn = InlineKeyboardMarkup(inline_keyboard=kb_in)
in_risunok = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(number_fasad, 7, '$'))
in_ris_facade = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(number_fasad, 7, 'facade'))
in_mesyac = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(mesyac, 4, '!!!'))
in_letter = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(letter, 8, '%%%'))
in_ris_price = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(number_fasad, 7, 'fasad'))
in_group_pl = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(group, 6, 'group'))
in_group_sort = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(group, 6, 'sort'))
in_dolgi_year = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(client_year, 3, 'year'))
in_my_dolgi_year = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(client_year, 3, 'my_year'))
in_zarplata_year = InlineKeyboardMarkup(inline_keyboard=vivod_inlinekey(dolgi_year, 3, 'zar_year'))
in_static_plenka = InlineKeyboardMarkup(inline_keyboard=static_plenka)
in_actions = InlineKeyboardMarkup(inline_keyboard=actions)

vid_facade = [[InlineKeyboardButton(text="Фасад", callback_data="Фасад_Ris"),
               InlineKeyboardButton(text="СТЕКЛО", callback_data="СТЕКЛО_Ris"),
               InlineKeyboardButton(text="ПСЯ", callback_data="ПСЯ_Ris")],
              [InlineKeyboardButton(text="Бутыл.", callback_data="Бутыл._Ris"),
               InlineKeyboardButton(text="Планка", callback_data="Планка_Ris"),
               InlineKeyboardButton(text="ПЕРЕПЛЕТ", callback_data="ПЕРЕПЛЕТ_Ris")],
              ]
in_vid_facade = InlineKeyboardMarkup(inline_keyboard=vid_facade)
in_change_order = InlineKeyboardMarkup(inline_keyboard=change_order)

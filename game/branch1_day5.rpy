label branch1_day5_conspiracy_room_boys:

    scene boy_room_day with dissolve

    play music "music/Runaway_08 (Pre_Loop).ogg"

    queue music "music/Runaway_08 (Loop).ogg"

    "Я проснулся от лучей солнца." with dissolve

    "Начинался новый день." with dissolve

    "Сегодня по плану я должен помочь Алие сделать новый паспорт." with dissolve

    "Я открыл телефон." with dissolve

    show day5_time1053 as cg_screen_phone with dissolve:
        xalign 1.0

    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    "Есть новые сообщения." with dissolve

    hide cg_screen_phone_new_message

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_messenger_cover_above_boy_room as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    $ phoneSayCoachWithTitle(__("Семён, мы с Яриком поехали в центр Москвы по делам."))

    $ phoneSayCoachWithTitle(__("Сделай сегодня Алие паспорт!"))

    $ phoneSayCoachWithTitle(__("Зайди на сайт Ночлежки и прочитай как это сделать!"))

    $ phoneSayCoachWithTitle(__("После обеда возможно пересечемся. Чао!"), True)

    coach "Семён, мы с Яриком поехали в центр Москвы по делам." with dissolve

    coach "Сделай сегодня Алие паспорт!" with dissolve

    coach "Зайди на сайт Ночлежки и прочитай как это сделать!" with dissolve

    coach "После обеда возможно пересечемся. Чао!" with dissolve

    "Хороший план на день." with dissolve

    $ clearMessages()

    hide cg_messenger_cover_above

    hide cg_messenger_title

    show cg_screen_phone_browser1 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я открыл браузер." with dissolve


    "Милана посоветовала открыть сайт Ночлежки, хмм, сейчас посмотрим." with dissolve

    show cg_screen_phone_browser2 as cg_screen_phone with dissolve:
        xalign 1.0

    "Адрес homeless.ru, очень легко запомнить." with dissolve

    show cg_screen_phone_browser3 as cg_screen_phone with dissolve:
        xalign 1.0

    "Ага, вот, Пошаговые инструкции для решения правовых проблем." with dissolve

    "Нажимаю 'Получить паспорт'" with dissolve

    show cg_screen_phone_browser4 as cg_screen_phone with dissolve:
        xalign 1.0

    "Ну здесь довольно легко." with dissolve

    "Сделать фото на паспорт - это можно сделать по пути." with dissolve

    "Оплатить пошлину - это можно сделать через платежный терминал или даже онлайн." with dissolve

    "Заполнить анкету в отделе по вопросам миграции - легко." with dissolve

    "... И это все?" with dissolve

    "Готовый паспорт можно будет забрать там же через 5 дней?" with dissolve

    "Отлично! Тогда можно прямо сейчас идти делать!" with dissolve

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    "Что же, я думаю пора идти умываться..." with dissolve

    jump branch1_day5_conspiracy_hall_morning


label branch1_day5_conspiracy_hall_morning:

    scene corridor_day_open with dissolve

    "Я вышел в коридор." with dissolve

    "Вот ванная комната, справа." with dissolve

    "Я подошел к двери..." with dissolve

    aliya "Эй!" with dissolve

    scene girl_room_day with dissolve

    show Aliya half_turn_hand_side_tshirt_happy1_1 at any_center_pos with dissolve

    "Я обернулся и увидел Алию в дверях комнаты." with dissolve

    show Aliya half_turn_hand_side_tshirt_happy1_2 at any_center_pos with dissolve

    aliya "Я первая пойду умываться!" with dissolve

    show Aliya half_turn_hand_side_tshirt_happy1_1 at any_center_pos with dissolve

    "Я улыбнулся." with dissolve

    "Глядя на меня, Алия тоже улыбалась." with dissolve

    show Aliya half_turn_hand_side_tshirt_happy1_2 at any_center_pos with dissolve

    aliya "У тебя классные друзья, где ты только их находишь?" with dissolve

    show Aliya half_turn_hand_side_tshirt_happy1_1 at any_center_pos with dissolve

    me "По правде говоря, я этих ребят знаю совсем недавно." with dissolve

    me "Я с ними познакомился в интернете." with dissolve

    show Aliya half_turn_hand_side_tshirt_happy1_2 at any_center_pos with dissolve

    aliya "Каждый из них как будто пришел из своего мира!" with dissolve

    aliya "Ярик водит спортивный автомобиль." with dissolve

    aliya "Николай вообще имеет свой самолет и летает куда хочет." with dissolve

    aliya "Костя путешествует с одним рюкзаком по всему миру." with dissolve

    aliya "Даже Милана, она такая классная!" with dissolve

    aliya "Я раньше не очень хорошо относилась к нефоркам." with dissolve

    aliya "Но теперь она моя лучшая подруга!" with dissolve

    show Aliya half_turn_hand_side_tshirt_happy1_1 at any_center_pos with dissolve

    "Если так подумать, то у меня тоже не очень-то и много друзей." with dissolve

    "Да и то, в последнее время все старые \"друзья\" как будто пропали из моей жизни." with dissolve

    "А настоящие друзья в моей жизни появились только сейчас, когда мне потребовалась помощь." with dissolve

    show Aliya half_turn_hand_down_tshirt_worried1_2 at any_center_pos with dissolve
    
    aliya "О чем задумался?" with dissolve

    show Aliya half_turn_hand_down_tshirt_worried1_1 at any_center_pos with dissolve

    me "Да так..." with dissolve

    show Aliya half_turn_hand_down_tshirt_happy1_1 at any_center_pos with dissolve

    aliya "Пропусти меня, я пойду умываться!" with dissolve

    show Aliya half_turn_hand_down_tshirt_happy1_2 at any_center_pos with dissolve

    me "А, да, конечно..." with dissolve

    scene black with dissolve

    "Я пропустил Алию вперед, а после нее и сам тоже умылся." with dissolve

    jump branch1_day5_conspiracy_kitchen


label branch1_day5_conspiracy_kitchen:

    scene kitchen_day with dissolve

    show Aliya half_turn_hand_down_tshirt_happy1_2 at any_right_pos with dissolve

    "После того как я умылся, я пришел на кухню." with dissolve

    "Алия уже была там." with dissolve

    show Aliya half_turn_hand_down_tshirt_happy1_1 at any_right_pos with dissolve

    aliya "Нам в холодильнике оставили завтрак, так мило!" with dissolve

    show Aliya half_turn_hand_down_tshirt_happy1_2 at any_right_pos with dissolve

    me "Да, это очень мило." with dissolve

    show Aliya straight_tshirt_neutral2 at any_right_pos with dissolve

    aliya "Какие планы на сегодня?" with dissolve

    show Aliya straight_tshirt_neutral1 at any_right_pos with dissolve

    me "Сейчас мы поедем с тобой оформлять тебе паспорт." with dissolve

    me "Я уже нашел инструкцию." with dissolve

    me "Нам нужно будет сделать фотографию тебе, оплатить пошлину." with dissolve

    me "И потом найти МФЦ и прийти туда." with dissolve

    me "Там ты заполнишь анкету и все на этом." with dissolve

    show Aliya straight_tshirt_happy2_2 at any_right_pos with dissolve

    aliya "Отлично!" with dissolve

    aliya "Я уже поела." with dissolve

    show Aliya straight_tshirt_happy1 at any_right_pos with dissolve

    aliya "Доедай свой завтрак и пойдем!" with dissolve

    show Aliya straight_tshirt_happy1_2 at any_right_pos with dissolve

    "Действительно, мне не помешало бы подкрепиться!" with dissolve

    scene black with dissolve

    "И я приступил к еде..." with dissolve

    jump branch1_day5_conspiracy_hall_morning_exit

label branch1_day5_conspiracy_hall_morning_exit:

    scene corridor_day_open with dissolve

    show Aliya half_turn_hoodie_neutral1 at any_center_pos with dissolve

    "Позавтракав, мы вышли в коридор." with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_2 at any_center_pos with dissolve

    aliya "Я вот думаю, на улице вроде бы тепло." with dissolve

    aliya "Мне стоило надевать свою толстовку?" with dissolve

    aliya "Или лучше снять ее?" with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_1 at any_center_pos with dissolve

    me "Я думаю, что надо ее надеть." with dissolve

    me "Вдруг вечером погода изменится." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 at any_center_pos with dissolve

    "Алия задумалась." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 at any_center_pos with dissolve

    aliya "После того как мы оформим паспорт, мне нужно будет купить сменную одежду." with dissolve

    aliya "Мне нужно будет переодеться в чистую одежду." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 at any_center_pos with dissolve

    me "Хорошо, я придумаю что можно сделать!" with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_1 at any_center_pos with dissolve

    "Алия улыбнулась." with dissolve

    show Aliya half_turn_hand_down_hoodie_happy2_1 at any_center_pos with dissolve

    aliya "Договорились!" with dissolve

    scene black with dissolve

    "И мы вышли из квартиры..." with dissolve

    jump branch1_day5_conspiracy_exterior2


label branch1_day5_conspiracy_exterior2:

    scene entrance_day with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_1 at any_left_pos with dissolve

    play music "music/Runaway_09 (Pre_Loop).ogg"

    queue music "music/Runaway_09 (Loop).ogg"

    "Мы вышли из подъезда." with dissolve

    "Солнце уже прогрело улицы города, но легкий ветер приносил прохладу." with dissolve

    show cg_screen_phone_map1 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я достал телефон, чтобы проверить маршрут." with dissolve

    me "Удобнее всего добраться до МФЦ, который находится на Автозаводской." with dissolve

    me "Там мы сможем сразу заполнить анкету и заказать тебе новый паспорт." with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_2 at any_left_pos with dissolve

    aliya "Отлично! А как мы туда доберемся?" with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_1 at any_left_pos with dissolve

    show cg_screen_phone_metro1 as cg_screen_phone with dissolve:
        xalign 1.0
    
    "Я открыл карту метро." with dissolve

    me "Можно сесть на станцию Новокосино, Калининская линия." with dissolve
    
    me "И без пересадок доехать до Автозаводской." with dissolve

    show Aliya half_turn_hand_down_hoodie_worried1_2 at any_left_pos with dissolve

    aliya "Тогда пойдем к метро?" with dissolve

    show Aliya half_turn_hand_down_hoodie_worried1_1 at any_left_pos with dissolve

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    me "Пойдем!" with dissolve

    jump branch1_day5_mcdonalds_exterior


label branch1_day5_mcdonalds_exterior:

    scene mcd_parking33 with dissolve

    show Aliya turn_around_hand_down_hoodie_happy1_1 at any_left_pos with dissolve

    "Мы дошли до Макдоналдса." with dissolve

    "Именно здесь мы вчера встретились с Напарником." with dissolve

    show cg_screen_phone_map2 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я достал телефон." with dissolve

    me "Судя по карте, вход в метро должен быть где-то слева от нас." with dissolve

    hide cg_screen_phone with dissolve

    me "Так, я вижу продуктовый магазин, офис Нотариуса... А где метро?" with dissolve

    me "Ладно, давай пойдем дальше." with dissolve

    show Aliya turn_around_hand_down_hoodie_happy1_2 at any_left_pos with dissolve

    aliya "Идем!" with dissolve

    jump branch1_day5_metro_novokosino_exterior

label branch1_day5_metro_novokosino_exterior:

    scene metro_novokosino_ext_day1 with dissolve

    show Aliya turn_around_hand_down_hoodie_happy1_1 at any_left_pos with dissolve

    "Наконец, мы пришли к входу в метро." with dissolve

    "Вокруг ходили люди, занятые своими делами." with dissolve

    me "Я помню, как мы с тобой впервые прокатились на метро." with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_2 at any_left_pos with dissolve

    aliya "Да, я помню." with dissolve

    aliya "Мы покупали карту Тройка в автомате." with dissolve

    aliya "Милана мне одолжила свою карту, поэтому сейчас ничего покупать не нужно." with dissolve

    aliya "Мы можем сразу спускаться к поездам." with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_1 at any_left_pos with dissolve

    me "Хорошо, тогда пойдем!" with dissolve

    jump branch1_day5_metro_novokosino_interior

label branch1_day5_metro_novokosino_interior:

    scene black

    show metro_novokosino_int_empty as metro_int

    show metro_novokosino_int_people1

    show black

    hide black with dissolve

    show Aliya half_turn_hoodie_happy1_1 at any_right_pos zorder 5 with dissolve

    stop music

    play music "ambience/novokosino_loop.ogg" fadein 1.0

    queue music "ambience/novokosino_loop.ogg"

    "Пройдя через турникеты и спустившись на эскалаторе, мы оказались в метро." with dissolve

    "Сейчас пассажиров было не очень много." with dissolve

    "Мы встали на перроне и стали ждать поезд." with dissolve
    
    "Шум метро наполнял мои уши." with dissolve

    show metro_novokosino_int_train as metro_int with dissolve

    "Вскоре подъехал поезд в сторону центра." with dissolve

    show metro_novokosino_int_train_open as metro_int with dissolve

    "Двери поезда открылись." with dissolve

    me "А вот и наш поезд!" with dissolve

    me "Пойдем!" with dissolve

    jump branch1_day5_metro_train_car

label branch1_day5_metro_train_car:

    scene black

    show metro_novokosino_front as metro_front zorder 1:
        xpos 0.0

    show m_train_center_door_open as m_train zorder 2

    show m_train_center_people2 as people zorder 2.5

    show Aliya straight_hoodie_neutral1 at any_left_pos zorder 3

    show black as black_front zorder 5

    hide black_front with dissolve

    play music_crossfade "ambience/novokosino_train1.ogg" fadein 2.0 noloop

    queue music_crossfade "ambience/novokosino_train2_loop.ogg"

    stop music fadeout 2.0

    announcement "Осторожно, двери закрываются! Следующая станция - Новогиреево!" with dissolve

    announcement "Для вашей безопасности, держитесь за поручни!" with dissolve

    show m_train_center_door_closed as m_train zorder 2

    "И сразу же двери закрылись." with dissolve

    stop music_crossfade fadeout 2.0

    play music "ambience/novokosino_train3.ogg" noloop

    queue music "ambience/novokosino_train3_loop.ogg"

    show metro_novokosino_front as metro_front zorder 1:
        xpos 0.0
        easeout 15.0 xpos -3.0

    show tonnel2 as metro_front_tonnel zorder 0.5:
        xpos 1.0 + (3000.0/1920.0-1)
        easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1)


    show tonnel1 as metro_front_tonnel2 zorder 0.5:
        xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel3 zorder 1:
        xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel4 zorder 1:
        xpos 5000
        pause 15.0
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat


    "И поезд поехал." with dissolve

    "Разогнавшись, поезд заехал в тоннель." with dissolve

    "Внутри вагона было не так уж и шумно." with dissolve

    "Можно было разговаривать голосом." with dissolve

    stop music fadeout 2.0

    jump branch1_day5_metro_train_car_again

label branch1_day5_metro_train_car_again:

    scene black

    show tonnel1 as metro_front_tonnel2 zorder 0.5:
        #xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        #easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel3 zorder 1:
        #xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        #easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel4 zorder 1:
        #xpos 5000
        #pause 15.0
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show metro_avia_front1 as metro_front zorder 1:
        xpos 3.0
        easein 8.0 xpos -0.5

    show m_train_center_door_closed as m_train zorder 2

    show m_train_center_people2 as people zorder 2.5

    show Aliya straight_hoodie_neutral1 at any_left_pos zorder 3

    show black as black_front zorder 5

    hide black_front with dissolve

    play music_crossfade "ambience/train_aviamotornaya_before_loop.ogg" fadein 2.0 noloop

    queue music_crossfade "ambience/train_aviamotornaya_loop.ogg"

    announcement "Станция Авиамоторная!" with dissolve

    announcement "Надземный переход на Некрасовскую линию!" with dissolve

    announcement "Выход к железнодорожной платформе Авиамоторная!" with dissolve

    announcement "Внимание! Временно не ходят поезда на участке Автозаводская - Орехово Замоскворецкой линии." with dissolve

    announcement "Пользуйтесь другими линиями, МЦД, автобусами КМ и наземным транспортом." with dissolve

    "Вагон плавно остановился у станции." with dissolve

    show metro_avia_front1 as metro_front zorder 1:
        xpos -0.5

    show m_train_center_door_open as m_train zorder 2 with dissolve

    "Двери шумно открылись." with dissolve

    show Aliya straight_hoodie_happy1 at any_left_pos zorder 3

    aliya "Пойдем?" with dissolve

    show Aliya straight_hoodie_happy1_2 at any_left_pos zorder 3

    me "Пойдем!" with dissolve

    show black as black_front zorder 5 with dissolve

    stop music_crossfade fadeout 2.0

    "И мы вышли из метро..." with dissolve

    jump branch1_day5_aviamotornaya_exterior

label branch1_day5_aviamotornaya_exterior:

    scene metro_avia_ext_day2_people with dissolve

    show Aliya half_turn_hoodie_happy1_1 at any_left_pos zorder 3 with dissolve
    
    play music "music/Runaway_09 (Pre_Loop).ogg"

    queue music "music/Runaway_09 (Loop).ogg"

    "Город встретил нас жарким дыханием летнего воздуха." with dissolve

    "Здесь уже чувствовалась суета, привычная для Москвы." with dissolve

    "Мимо ехали автомобили, и ходили пешеходы." with dissolve

    show Aliya straight_hoodie_happy1 at any_left_pos zorder 3 with dissolve

    aliya "Мы сейчас отсюда пойдем в МФЦ?" with dissolve

    show Aliya straight_hoodie_happy1_2 at any_left_pos zorder 3 with dissolve

    me "Не совсем. Нам еще нужно сначала сделать фотографию на паспорт." with dissolve

    show Aliya half_turn_hand_down_hoodie_worried1_2 at any_left_pos zorder 3 with dissolve

    aliya "Где это можно сделать?" with dissolve

    show Aliya half_turn_hand_down_hoodie_worried1_1 at any_left_pos zorder 3 with dissolve

    me "В любом фотосалоне." with dissolve

    show Aliya_back back2 as Aliya zorder 3 with dissolve

    "Я осмотрелся." with dissolve

    me "Вот кстати совсем рядом подходящий фотосалон." with dissolve

    show Aliya turn_around_hand_down_hoodie_neutral2 at any_left_pos zorder 3 with dissolve

    aliya "Пойдем туда?" with dissolve

    show Aliya turn_around_hand_down_hoodie_neutral1 at any_left_pos zorder 3 with dissolve

    me "Пойдем!" with dissolve

    scene black with dissolve

    "И мы спустились в помещение фотосалона..." with dissolve

    jump branch1_day5_aviamotornaya_photo


label branch1_day5_aviamotornaya_photo:

    scene photo_background

    show photoman sit1 zorder 3

    show photo_foreground zorder 2

    show black zorder 10

    show Aliya straight_hoodie_happy1_2 zorder 3 at any_left_pos with dissolve

    hide black with dissolve

    "Это было небольшое помещение, в котором было все что должно быть в фотосалоне." with dissolve

    "Принтеры, плоттеры, сканеры, ламинаторы, белая простыня, стул и фотоаппарат." with dissolve
    
    "Стену украшали портреты и различные арты." with dissolve

    hide photoman with dissolve

    show photoman neutral zorder 3 with dissolve

    "К нам сразу же подошел молодой человек, работник фотосалона." with dissolve

    show Aliya_back back2 as Aliya zorder 3 with dissolve

    show photoman neutral_speak zorder 3 with dissolve

    photoman "Приветствую, что для вас?" with dissolve

    show Aliya turn_around_hand_down_hoodie_neutral1 zorder 3 at any_left_pos with dissolve

    show photoman neutral zorder 3 with dissolve

    me "Нужно сделать фотографию на паспорт для девушки." with dissolve

    show photoman neutral_speak zorder 3 with dissolve

    photoman "Сделаем! Это будет стоить 500 рублей." with dissolve

    photoman "А вы молодая девушка проходите, садитесь сюда!" with dissolve

    show photoman neutral zorder 3 with dissolve

    hide Aliya with dissolve

    show photo_aliya zorder 1 with dissolve

    "Алия села на стул и слегка поправила волосы." with dissolve

    show photoman shoot zorder 3 with dissolve

    "Фотограф настроил свет и сделал фотографию." with dissolve

    hide photoman with dissolve

    hide photo_aliya with dissolve

    show Aliya straight_hoodie_neutral1 zorder 2 at any_left_pos with dissolve

    show photoman sit2 zorder 3 with dissolve

    "После чего сел за стол и начал обрабатывать фото." with dissolve

    show cg_screen_phone_browser5 as cg_screen_phone zorder 7 with dissolve:
        xalign 1.0
        xpos 1.1

    "Я открыл телефон и посмотрел список документов для паспорта." with dissolve

    me "Нужно оплатить пошлину за оформление нового паспорта." with dissolve

    show Aliya straight_hoodie_neutral2 zorder 2 at any_left_pos with dissolve

    aliya "Где это можно сделать?" with dissolve

    show Aliya straight_hoodie_neutral1 zorder 2 at any_left_pos with dissolve

    me "Это можно сделать в терминале оплаты в отделении банка." with dissolve

    me "Но намного проще это сделать онлайн." with dissolve

    me "Сейчас я оплачу через свою карту, а потом мы распечатаем квитанцию." with dissolve

    show cg_screen_phone_bank1 as cg_screen_phone zorder 7 with dissolve:
        xalign 1.0
        xpos 1.1

    "Я открыл сайт банка и начал заполнять платежку." with dissolve

    show cg_screen_phone_bank2 as cg_screen_phone zorder 7 with dissolve:
        xalign 1.0
        xpos 1.1

    "Платеж проведен! Теперь нужно лишь распечатать квитанцию." with dissolve

    me "Молодой человек, мне нужно распечатать документ. Куда мне его отправлять?" with dissolve

    show photoman sit3 zorder 3 with dissolve

    photoman "50 рублей за страницу. Присылайте вот по QR-коду или на почту." with dissolve

    show photoman sit2 zorder 3 with dissolve

    hide cg_screen_phone with dissolve

    "Я отправил квитанцию фотографу и убрал телефон." with dissolve

    hide cg_screen_phone with dissolve

    show photoman sit3 zorder 3 with dissolve

    photoman "Получил, сейчас распечатаю!" with dissolve

    show photoman neutral_docs zorder 3 with dissolve

    "Зашумел принтер, а затем фотограф взял распечатанные документы и подошел к нам." with dissolve

    show photoman neutral_docs_speak zorder 3 with dissolve

    photoman "Вот ваши фотографии и вот ваш документ. С вас 550 рублей за все вместе!" with dissolve

    show photoman neutral_docs zorder 3 with dissolve

    "Я достал и отсчитал ему пачку наличных." with dissolve

    show photoman neutral_speak zorder 3 with dissolve

    photoman "Благодарю, приходите еще!" with dissolve

    show photoman neutral zorder 3 with dissolve

    me "Спасибо, до свидания!" with dissolve

    jump branch1_day5_aviamotornaya_exterior_after_photo

label branch1_day5_aviamotornaya_exterior_after_photo:

    scene metro_avia_ext_day_people with dissolve

    show Aliya turn_around_hand_down_hoodie_neutral1 zorder 3 at any_left_pos with dissolve

    "И мы вышли на улицу, на свежий воздух." with dissolve

    show cg_screen_phone_browser5 as cg_screen_phone zorder 7 with dissolve:
        xalign 1.0
        xpos 1.1

    "Я открыл телефон и посмотрел список документов для паспорта." with dissolve

    me "У нас все готово, теперь нужно идти в МФЦ." with dissolve

    hide cg_screen_phone with dissolve

    show Aliya turn_around_hand_down_hoodie_neutral2 zorder 3 at any_left_pos with dissolve

    aliya "Ты знаешь куда идти?" with dissolve

    show Aliya turn_around_hand_down_hoodie_neutral1 zorder 3 at any_left_pos with dissolve

    me "Нужно будет повернуть налево на Красноказарменную улицу." with dissolve

    me "А потом еще раз налево, на Красноказарменный проезд." with dissolve

    me "Там будет центр госуслуг района Лефортово." with dissolve

    show Aliya turn_around_hand_down_hoodie_neutral2 zorder 3 at any_left_pos with dissolve

    aliya "Пойдем?" with dissolve

    show Aliya turn_around_hand_down_hoodie_neutral1 zorder 3 at any_left_pos with dissolve

    me "Пойдем!" with dissolve

    jump branch1_day5_guvm_exterior

label branch1_day5_guvm_exterior:

    scene mvd1 with dissolve

    show Aliya_back back2 as Aliya at any_left_pos with dissolve

    "Достаточно скоро мы подошли к МФЦ." with dissolve

    "Это был новый район, активно застраиваемый жильем комфорт-класса." with dissolve

    "Здание МФЦ также выглядело очень респектабельно, свежо и чисто." with dissolve

    me "Нам сюда! Пошли!" with dissolve

    jump branch1_day5_guvm_interior

label branch1_day5_guvm_interior:

    scene mvd_int2 with dissolve

    show Aliya straight_hoodie_neutral1 at any_left_pos zorder 3 with dissolve

    "Мы зашли внутрь." with dissolve

    "Отделение миграции выглядело скромно." with dissolve

    "Возле кабинетов были стулья, где можно было подождать своей очереди." with dissolve

    "Почти никого не было. Видимо, сюда редко кто ходит." with dissolve

    "На стене висели примеры заполнения анкет." with dissolve

    "А рядом находился столик, где можно было взять анкеты и заполнить их." with dissolve

    me "Теперь тебе нужно взять вот эту анкету." with dissolve

    me "Заполнить ее." with dissolve

    me "И вместе с фото и квитанцией отдать этому сотруднику." with dissolve

    me "Понятно?" with dissolve

    show Aliya straight_hoodie_neutral2 at any_left_pos zorder 3 with dissolve

    aliya "Да." with dissolve

    hide Aliya with dissolve

    "Алия взяла анкету, и ушла заполнять ее." with dissolve

    "А когда анкета была заполнена, Алия зашла в кабинет." with dissolve

    messenger "Новое сообщение" with dissolve

    show day5_time1352 as cg_screen_phone with dissolve:
        xalign 1.0

    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    "Я достал телефон." with dissolve

    hide cg_screen_phone_new_message
    
    show cg_messenger_cover_above_mfc as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    $ phoneSayCoachWithTitle(__("Привет Семён! Как у вас дела?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Мы уже в МФЦ, подаем документы на паспорт."))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Отлично!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Есть предложение,"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Как насчет погулять втроем в Замоскворечье?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Хотите присоединиться?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Покажешь Алие Москву еще раз."))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошая идея!"))
    me "[lastPhoneMsg!t]" with dissolve
    
    $ phoneSayCoachWithTitle(__("Тогда как закончишь, садитесь на метро,"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("И езжайте до Третьяковской."))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Договорились!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    show Aliya straight_hoodie_happy1_2 zorder 3 at any_left_pos with dissolve

    "Скоро Алия вышла из кабинета." with dissolve

    show Aliya straight_hoodie_happy1 zorder 3 at any_left_pos with dissolve

    aliya "Все?" with dissolve

    show Aliya straight_hoodie_happy1_2 zorder 3 at any_left_pos with dissolve

    me "Да, все." with dissolve

    show Aliya straight_hoodie_happy1 zorder 3 at any_left_pos with dissolve

    aliya "Мне дали бумажку, и сказали приходить 20 июля, с 10 до 12!" with dissolve

    aliya "Так быстро, просто, и совсем не страшно!" with dissolve

    show Aliya straight_hoodie_happy1_2 zorder 3 at any_left_pos with dissolve

    me "А теперь пойдем!" with dissolve

    jump branch1_day5_guvm_exterior2


label branch1_day5_guvm_exterior2:

    scene mvd2 with dissolve

    show Aliya straight_hoodie_neutral1 at any_left_pos with dissolve

    "Мы вышли на улицу." with dissolve

    show Aliya straight_hoodie_neutral2 at any_left_pos with dissolve

    aliya "Что будем делать теперь?" with dissolve

    show Aliya straight_hoodie_neutral1 at any_left_pos with dissolve

    me "Милана предлагает поехать гулять в Замоскворечье." with dissolve

    me "Как ты на это смотришь?" with dissolve

    show Aliya half_turn_hoodie_happy1_1 at any_left_pos with dissolve

    "Алия улыбнулась." with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_2 at any_left_pos with dissolve


    aliya "Отлично, я буду рада!" with dissolve

    aliya "Это куда нужно идти?" with dissolve

    show Aliya half_turn_hand_down_hoodie_happy1_1 at any_left_pos with dissolve

    me "Это нужно сесть на метро и поехать до станции Третьяковская." with dissolve

    me "Ты уже запомнила как дойти до метро?" with dissolve

    aliya "Да, я помню дорогу!" with dissolve

    me "Тогда веди!" with dissolve

    show Aliya_back back2 as Aliya with dissolve

    "Алия уверенно развернулась и пошла вдоль Красноказарменного проезда." with dissolve

    scene black with dissolve

    stop music fadeout 2.0

    "И я пошел за ней к метро..." with dissolve

    jump branch1_day5_metro_train_car2

label branch1_day5_metro_train_car2:

    play music_crossfade "ambience/tretyakovskaya_train_loop.ogg"

    show tonnel1 as metro_front_tonnel2 zorder 0.5:
        #xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        #easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel3 zorder 1:
        #xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        #easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel4 zorder 1:
        #xpos 5000
        #pause 15.0
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show m_train_center_door_closed as m_train zorder 3

    show m_train_center_people3 as people zorder 3.5

    show Aliya straight_hoodie_sad2 as Aliya at any_left_pos zorder 4

    show black as black_front zorder 10

    hide black_front with dissolve

    "И вот мы уже едем в метро в сторону Третьяковской." with dissolve

    "Алия смотрела на меня." with dissolve

    "Мне было немножко неловко." with dissolve

    "Я не привык к тому, что меня так внимательно рассматривают." with dissolve

    "Ну ладно, я сделаю вид что ничего не заметил." with dissolve

    "Хотя может лучше, сказать что-нибудь?" with dissolve

    me "Мы уже почти приехали!" with dissolve

    show metro_tret_front_people as metro_front zorder 2:
        xpos 3.0 + 2.5
        easein 8.0 * 2 xpos -0.5

    stop music_crossfade fadeout 2.0

    play music "ambience/tretyakovskaya_arrive2.ogg" fadein 2.0 noloop

    queue music "ambience/tret_before_open_door_loop.ogg"

    announcement "Станция Третьяковская!" with dissolve

    announcement "Переход на станцию Новокузнецкая и Калужско-Рижскую линию!" with dissolve

    announcement "Поезд дальше не идет!" with dissolve

    announcement "Пожалуйста, выйдите из вагонов!" with dissolve

    announcement "О подозрительных предметах сообщайте машинисту!" with dissolve

    stop music fadeout 2.0

    play music_crossfade "ambience/tret_door_open_pre_loop.ogg" noloop

    queue music_crossfade "ambience/tretyakovskaya_standby_loop.ogg"

    show metro_tret_front_people as metro_front zorder 2:
        xpos -0.5

    show m_train_center_door_open as m_train zorder 3 with dissolve

    "Двери открылись." with dissolve

    me "Идем!" with dissolve

    aliya "Идем..." with dissolve

    jump branch1_day5_tretyakovskaya_exterior1

label branch1_day5_tretyakovskaya_exterior1:

    stop music_crossfade fadeout 2.0

    stop music fadeout 2.0

    play music "music/Runaway_09 (Pre_Loop).ogg"

    queue music "music/Runaway_09 (Loop).ogg"

    scene kliment with dissolve

    show Aliya_back back2 as Aliya at any_left_pos with dissolve

    "Мы вышли из метро." with dissolve

    "Стояла ясная летняя погода, дул легкий ветер." with dissolve

    "Это была пешеходная зона, здесь не было машин." with dissolve

    "Зато пешеходы ходили толпами, через всю улицу." with dissolve

    "Москвичи и приезжие, старики и школьники - казалось, здесь можно было встретить кого угодно!" with dissolve

    show Aliya turn_around_hoodie_happy1_2 at any_left_pos with dissolve

    aliya "А здесь даже красивее чем на Таганской!" with dissolve

    show Aliya turn_around_hand_down_hoodie_happy1_1 at any_left_pos with dissolve

    me "Да, это точно!" with dissolve

    me "Здесь много кафешек и ресторанов, в которых можно посидеть и поесть." with dissolve

    me "Здесь много летних террас." with dissolve

    show Aliya half_turn_hand_down_jacket_happy1_2 at any_left_pos with dissolve

    aliya "Мне здесь нравится!" with dissolve

    aliya "Я бы здесь каждый день гуляла!" with dissolve

    show Aliya half_turn_hand_down_jacket_happy1_1 at any_left_pos with dissolve

    "Питаться в кафешках на Третьяковской каждый день никаких денег не хватит." with dissolve

    me "Да, конечно!" with dissolve

    messenger "Новое сообщение" with dissolve

    show day5_time1439 as cg_screen_phone with dissolve:
        xalign 1.0

    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    "Я достал телефон." with dissolve

    hide cg_screen_phone_new_message
    
    show cg_messenger_cover_above_kliment as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0 

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    $ phoneSayCoachWithTitle(__("Ну где вы там?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Мы уже приехали."))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Отлично!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я уже заняла место в кафе!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("От метро прямо - и увидишь летнюю веранду. Иди туда!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Да, я вижу!"))
    me "[lastPhoneMsg!t]" with dissolve
    
    $ phoneSayCoachWithTitle(__("Жду вас!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    me "Нас уже ждут! Пойдем!" with dissolve

    show Aliya half_turn_hand_down_jacket_happy1_2 at any_left_pos with dissolve

    aliya "Идем!" with dissolve

    scene black with dissolve

    "И мы пошли к кафе." with dissolve

    jump branch1_day5_tretyakovskaya_cafe

label branch1_day5_tretyakovskaya_cafe:

    scene kliment_cafe1

    show milana_table table1 as Milana zorder 1:
        xpos -0.2
        ypos 0.2
        zoom 0.9

    show AliyaSitTableLeft hoodie_hands_down_neutral1 zorder 2:
        ypos 0.2
        xpos -0.03
        zoom 0.9

    show kliment_cafe_table_food_down zorder 3

    show kliment_cafe_table_food_up zorder 4

    show black zorder 10

    hide black with dissolve

    "Мы заказали еду и сели за стол." with dissolve

    show milana_table table2 as Milana zorder 1 with dissolve

    milana "Алия, как тебе первый день в Москве?" with dissolve

    show milana_table table1 as Milana zorder 1 with dissolve

    show AliyaSitTableLeft hoodie_hands_down_happy2 zorder 2 with dissolve

    aliya "Очень круто! Мне нравится!" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 2 with dissolve

    aliya "Хотя я уже была в Москве раньше." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 2 with dissolve

    show milana_table table2 as Milana zorder 1 with dissolve

    milana "А, ну да, это уже не первый твой побег, конечно!" with dissolve

    milana "Мне здесь тоже нравится." with dissolve

    milana "Хотя первое время мне было нелегко." with dissolve

    show milana_table table1 as Milana zorder 1 with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 2 with dissolve

    aliya "Ты тоже сбежала из дома?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 2 with dissolve

    show milana_table table2 as Milana zorder 1 with dissolve

    milana "Да, но у меня не такой сложный случай, как у тебя." with dissolve

    milana "Когда я получила диплом, я собрала вещи и уехала из дома." with dissolve

    milana "Меня по сути и не искали. Родители махнули рукой на меня, живи как хочешь." with dissolve

    milana "Для меня было сложным найти жилье и работу в Москве." with dissolve

    milana "Но как видишь, я встала на ноги, и все у меня в жизни более-менее спокойно." with dissolve

    show milana_table table1 as Milana zorder 1 with dissolve

    "Алия вздохнула." with dissolve

    show milana_table table2 as Milana zorder 1 with dissolve

    milana "У тебя тоже все будет хорошо!" with dissolve

    show milana_table table1 as Milana zorder 1 with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 2 with dissolve

    aliya "Я надеюсь." with dissolve

    aliya "Когда вы все рядом, мне спокойно." with dissolve

    aliya "Но когда я остаюсь одна, мне иногда бывает страшно." with dissolve

    aliya "Мне кажется, что меня поймают и найдут." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 2 with dissolve

    show milana_table table2 as Milana zorder 1 with dissolve

    milana "Давай будем с тобой оптимистами." with dissolve

    milana "Твои родители не знают что ты уехала в Москву." with dissolve

    milana "Ты можешь здесь жить спокойно, ждать пока будет готов твой паспорт." with dissolve

    milana "А потом можно будет уехать из России." with dissolve

    milana "Так что держи выше нос! Все будет хорошо!" with dissolve

    show milana_table table1 as Milana zorder 1 with dissolve

    show AliyaSitTableLeft hoodie_hands_down_happy2 zorder 2 with dissolve

    aliya "Спасибо!" with dissolve

    aliya "Спасибо вам что помогаете мне!" with dissolve

    aliya "И тебе спасибо, Семён!" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_happy1 zorder 2 with dissolve

    show milana_table table2 as Milana zorder 1 with dissolve

    milana "А теперь предлагаю приступить к еде!" with dissolve

    jump branch1_day5_metro_train_car3

label branch1_day5_metro_train_car3:

    scene black with dissolve

    "Только приступив к еде, я понял насколько был голоден." with dissolve

    "Мы хорошо поели," with dissolve

    "А после еды мы попрощались и поехали по домам..." with dissolve

    scene black

    show tonnel1 as metro_front_tonnel2 zorder 0.5:
        #xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        #easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel3 zorder 1:
        #xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        #easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel4 zorder 1:
        #xpos 5000
        #pause 15.0
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show metro_novogireevo_front as metro_front zorder 1:
        xpos 3.0
        easein 8.0 xpos -0.5

    show metro_police1 as metro_police1 zorder 1.7:
        xpos 3.0+0.94
        easein 8.0 xpos -0.5+0.94

    show metro_police2 as metro_police2 zorder 1.6:
        xpos 3.0+0.90
        easein 8.0 xpos -0.5+0.90
    
    show metro_police3 as metro_police3 zorder 1.5:
        xpos 3.0+0.79
        easein 8.0 xpos -0.5+0.79

    show m_train_center_door_closed as m_train zorder 2

    show m_train_center_people1 as people zorder 2.5

    show Aliya turn_around_hand_down_hoodie_neutral1 at any_left_pos zorder 3

    show black as black_front zorder 5

    hide black_front with dissolve

    stop music

    play music_crossfade "ambience/novogireevo1x_pre_loop.ogg" noloop

    queue music_crossfade "ambience/novogireevo1x_loop.ogg"

    "Поезд метро подъезжает к станции Новогиреево." with dissolve

    show Aliya_back back2 as Aliya at any_left_pos zorder 3

    announcement "Станция Новогиреево!" with dissolve

    announcement "Выход к железнодорожной платформе Новогиреево!" with dissolve

    stop music_crossfade fadeout 2.0

    play music "ambience/novogireevo1_pre_loop.ogg" noloop

    queue music "ambience/novogireevo_standby_loop.ogg"

    show metro_novogireevo_front as metro_front zorder 1:
        xpos -0.5

    show metro_police1 as metro_police1 zorder 1.7:
        xpos -0.5+0.94

    show metro_police2 as metro_police2 zorder 1.6:
        xpos -0.5+0.90
    
    show metro_police3 as metro_police3 zorder 1.5:
        xpos -0.5+0.79

    show m_train_center_door_open as m_train zorder 2 with dissolve

    "Двери открылись." with dissolve

    "Я заметил несколько сотрудников полиции на станции." with dissolve

    "Интересно, я редко видел сразу столько полицейских одновременно." with dissolve

    "Я посмотрел на них. И заметил что один из них смотрит на меня." with dissolve

    show metro_police1_step2 as metro_police1 zorder 1.7 with dissolve:
        xpos -0.5+0.97

    "Он направился прямо ко мне. У меня внутри похолодело." with dissolve

    stop music fadeout 2.0

    play music_crossfade "ambience/novogireevo2_pre_loop.ogg" noloop

    queue music_crossfade "ambience/novogireevo2_loop.ogg"

    show m_train_center_door_closed as m_train zorder 2 with dissolve
    
    announcement "Осторожно, двери закрываются! Следующая станция Новокосино!" with dissolve

    "По счастью, он не успел дойти. Двери метро закрылись." with dissolve

    show metro_police1_step3 as metro_police1 zorder 1.7 with dissolve:
        xpos -0.5+0.97

    play sound "sound/686358__rangerrich68__walkie-talkie.ogg"

    "Я увидел как он что-то передал по рации." with dissolve

    show metro_novogireevo_front as metro_front zorder 1:
        xpos 0.0 - 0.5
        easeout 10.0 xpos -2.0 - 0.5

    show metro_police2 as metro_police2 zorder 1.6:
        xpos -0.5+0.90
        easeout 10.0 xpos -2.0 - 0.5+0.90

    show metro_police3 as metro_police3 zorder 1.5:
        xpos -0.5+0.79
        easeout 10.0 xpos -2.0 - 0.5+0.79

    
    show metro_police1_step3 as metro_police1 zorder 1.7:
        xpos -0.5+0.97
        easeout 10.0 xpos -2.0 - 0.5+0.97


    "И поезд поехал." with dissolve

    me "Ты видела его?" with dissolve

    me "Он явно шел к тебе!" with dissolve

    show Aliya straight_hoodie_fright2 at any_left_pos zorder 3

    aliya "Да!" with dissolve

    aliya "Что же делать?" with dissolve

    show Aliya straight_hoodie_sad2 at any_left_pos zorder 3

    "Надо было думать быстро." with dissolve

    me "Неужели московская полиция тоже тебя ищет?" with dissolve

    me "Полицейские как-то узнали что мы сейчас в метро." with dissolve

    me "Возможно они вычислили это по камерам." with dissolve

    show Aliya straight_hoodie_fright2 at any_left_pos zorder 3

    aliya "Что же делать? Меня поймают!" with dissolve

    aliya "Тот мент по рации говорил!" with dissolve
    
    aliya "Он наверняка передал чтобы на следющей станции нас задержали!" with dissolve

    aliya "Я не хочу домой!" with dissolve

    show Aliya straight_hoodie_sad2 at any_left_pos zorder 3

    "Я начал думать." with dissolve

    "Нас вычислили по камерам?" with dissolve

    "Значит, нужно сделать так чтобы камеры нас не нашли." with dissolve

    "Решение пришло само собой." with dissolve

    me "Идем в начало вагона." with dissolve

    scene black with dissolve

    "Я взял Алию за руку и мы пошли вдоль поезда." with dissolve

    scene black

    show tonnel1 as metro_front_tonnel2 zorder 0.5:
        #xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        #easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel3 zorder 1:
        #xpos 1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        #easeout 15.0 xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0)+ (1620.0/1920.0)
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show tonnel1 as metro_front_tonnel4 zorder 1:
        #xpos 5000
        #pause 15.0
        block:
            xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0)
            linear 2.0*(1620.0/1920.0) xpos -1.0 + -1.0 + (3000.0/1920.0-1) + (1620.0/1920.0) + (1620.0/1920.0) + (1620.0/1920.0) - (1620.0/1920.0)
            repeat

    show m_train_base_door_closed as m_train zorder 2

    show homeless1 as homeless zorder 2.5

    show Aliya straight_hoodie_sad2 as Aliya at any_left_pos zorder 3

    show black as black_front zorder 5

    hide black_front with dissolve

    me "Снимай толстовку, и клади в мой пакет!" with dissolve

    aliya "Что?" with dissolve

    me "Снимай быстро! Чтобы тебя не узнали!" with dissolve

    aliya "Хорошо..." with dissolve

    show AliyaMetroScene scene1 as Aliya at any_left_pos zorder 3

    "Алия быстро начала снимать толстовку." with dissolve

    show AliyaMetroScene scene2 as Aliya at any_left_pos zorder 3

    "Сбросив верхнюю одежду, Алия осталась в футболке." with dissolve

    show Aliya straight_tshirt_sad2 as Aliya at any_left_pos zorder 3

    "Я залез в карман, и нашел там..." with dissolve

    "Старую потрепанную маску!" with dissolve

    "То что надо!" with dissolve

    me "Надевай!" with dissolve

    show AliyaMetroScene scene3 as Aliya at any_left_pos zorder 3

    aliya "Ладно..." with dissolve

    show AliyaMetroScene scene4 as Aliya at any_left_pos zorder 3

    "Алия послушно надела маску." with dissolve

    show AliyaMetroScene scene5 as Aliya at any_left_pos zorder 3

    "Хорошо, теперь Алию не узнают. А как же я?" with dissolve

    "Что же мне делать?" with dissolve

    "Я оглянулся вокруг и увидел бомжеватого вида мужчину." with dissolve

    "Мне сразу вспомнилась сцена из одного старого фильма." with dissolve

    me "Мужчина! Хотите заработать пять тысяч рублей?" with dissolve

    show homeless2 as homeless zorder 2.5

    hobo "Что?" with dissolve

    me "Хотите пять тысяч рублей?" with dissolve

    hobo "Давай!" with dissolve

    me "Продайте мне свою куртку!" with dissolve

    hobo "Мою куртку?" with dissolve

    me "Да!" with dissolve

    hobo "За пять тысяч рублей?" with dissolve

    me "Да!" with dissolve

    show homeless3 as homeless zorder 2.5

    hobo "Давайте!" with dissolve

    show homeless4 as homeless zorder 2.5

    "Мужчина быстро снял с себя куртку и отдал мне." with dissolve

    show homeless5 as homeless zorder 2.5
    
    "Я быстро натянул ее на себя." with dissolve

    "Куртка пахла не очень приятно, но мне было уже наплевать." with dissolve

    show metro_novokosino_front_people as metro_front zorder 1:
        xpos 3.0
        easein 8.0 xpos -0.5

    stop music_crossfade fadeout 2.0

    play music "ambience/novokosino2_pre_loop.ogg" fadein 2.0 noloop

    queue music "ambience/novokosino2_loop.ogg"

    announcement "Станция Новокосино!" with dissolve

    announcement "Выход к железнодорожной платформе Реутово!" with dissolve

    announcement "Конечная! Поезд дальше не идет!" with dissolve

    announcement "Пожалуйста, выйдите из вагонов!" with dissolve

    show metro_novokosino_front_people as metro_front zorder 1:
        xpos -0.5

    show m_train_base_door_open as m_train zorder 2 with dissolve

    "Вот мы и приехали. Ментов снаружи нет." with dissolve

    me "Идем!" with dissolve

    aliya "Идем..." with dissolve

    jump branch1_day5_metro_train_car2_head

label branch1_day5_metro_train_car2_head:

    scene black

    show metro_novokosino_int_train_open as metro_int

    show metro_novokosino_int_people2

    show black

    hide black with dissolve

    show AliyaMetroScene scene5 as Aliya at any_left_pos zorder 5 with dissolve

    stop music fadeout 2.0

    play music_crossfade "ambience/novokosino_loop.ogg" fadein 1.0

    queue music_crossfade "ambience/novokosino_loop.ogg"

    "Мы выскользнули из вагона втихую." with dissolve

    "На станции действительно были менты, но они не обратили на нас внимания." with dissolve

    me "Быстрее, валим отсюда!" with dissolve

    scene black with dissolve

    "Я взял Алию за руку и мы побежали по эскалатору наверх..." with dissolve

    jump branch1_day5_metro_novokosino_exterior2


label branch1_day5_metro_novokosino_exterior2:

    scene metro_novokosino_ext_night with dissolve

    stop music_crossfade fadeout 2.0

    show Aliya half_turn_hand_down_tshirt_sad3 at any_left_pos zorder 3
    
    play music "music/Runaway_10 (Pre_Loop).ogg"

    queue music "music/Runaway_10 (Loop).ogg"

    "И вот мы уже стоим на улице." with dissolve

    "Полицейских здесь не было, только люди, спешащие по своим делам." with dissolve

    "Алия тяжело дышала." with dissolve

    show Aliya half_turn_hand_down_tshirt_sad2 at any_left_pos zorder 3

    aliya "Я чуть не сдохла там..." with dissolve

    show Aliya half_turn_hand_down_tshirt_sad4 at any_left_pos zorder 3

    me "Наверное, нас вычислили по камерам в метро." with dissolve

    me "Я думаю, нам лучше пока не пользоваться общественным транспортом." with dissolve

    show Aliya half_turn_hand_down_tshirt_sad2 at any_left_pos zorder 3

    aliya "Да, ты прав." with dissolve

    aliya "Давай пойдем отсюда..." with dissolve

    jump branch1_day5_mcdonalds_exterior2

label branch1_day5_mcdonalds_exterior2:

    scene mcd_parking32 with dissolve

    show Aliya straight_tshirt_sad2 at any_left_pos zorder 3 with dissolve

    "Мы отошли подальше от входа в метро." with dissolve

    "Я думаю, стоит предупредить остальных." with dissolve

    show cg_messenger_cover_above_mcd_night as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_screen_phone_night_dialog as cg_screen_phone:
        xalign 1.0 

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    "Я достал телефон." with dissolve

    $ phoneSayMe(__("У нас ЧП"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Когда мы подъезжали к Новогиреево, за нами увязалась транспортная полиция"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Мы еле еле как смогли от них скрыться"))
    me "[lastPhoneMsg!t]" with dissolve
    
    $ phoneSayCoachWithTitle(__("Менты, реально? Зачем?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я не знаю"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Мне кажется, они нас вычислили по камерам"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Как будто мы в розыске или что-то типа такого"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я сейчас напишу своему знакомому адвокату"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Надо его тоже добавить в этот чат"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Тут действительно что-то нечисто"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("С чего бы московская полиция ищет беглянок с Дагестана?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Что нам делать?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Идите домой, сидите там"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Мы с Яриком скоро подъедем"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошо"))
    me "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    show Aliya straight_tshirt_sad1 at any_left_pos zorder 3 with dissolve

    aliya "Что будем делать?" with dissolve

    show Aliya straight_tshirt_sad2 at any_left_pos zorder 3 with dissolve

    me "Милана советует нам идти домой." with dissolve

    me "Она посоветуется с адвокатом, мы попробуем выяснить почему тебя ищет полиция." with dissolve

    show Aliya straight_tshirt_sad1 at any_left_pos zorder 3 with dissolve

    aliya "Хорошо..." with dissolve

    show Aliya straight_tshirt_sad2 at any_left_pos zorder 3 with dissolve

    me "Пойдем!" with dissolve

    jump branch1_day5_conspiracy_exterior3




label branch1_day5_conspiracy_exterior3:

    scene entrance_night with dissolve

    show Aliya half_turn_hand_down_tshirt_sad3 at any_left_pos zorder 3 with dissolve

    "Мы подошли к подъезду." with dissolve

    "Мне было немножко страшно." with dissolve

    "Казалось, вот вот из-за темноты выйдет сотрудник полиции и арестует меня." with dissolve

    "Но у подъезда не было никого." with dissolve

    scene black with dissolve

    "И мы зашли внутрь..." with dissolve

    jump branch1_day5_conspiracy_hall1


label branch1_day5_conspiracy_hall1:

    play music "music/conversation.ogg"

    queue music "music/conversation.ogg"

    scene corridor_night_open with dissolve

    show Aliya straight_tshirt_worried2_2 at any_left_pos with dissolve:
        ypos 1.1

    show kostya neutral as Kostya with dissolve:
        xpos 0.05

    "Нас встретил Костя." with dissolve

    show kostya neutral_speak as Kostya with dissolve

    costya "Намасте!" with dissolve

    costya "Что случилось? Вы выглядите взволнованно!" with dissolve

    show kostya neutral as Kostya with dissolve

    show Aliya straight_tshirt_worried2 with dissolve 

    aliya "Здравствуйте!" with dissolve

    aliya "Нас чуть не поймала полиция в метро!" with dissolve

    show Aliya straight_tshirt_worried2_2 with dissolve 

    show kostya neutral_speak as Kostya with dissolve

    costya "Это ужасно!" with dissolve

    costya "Полиция все время что-то выясняет, лезет не в свои дела." with dissolve

    costya "Если совсем никак не избавиться от полицейских," with dissolve

    costya "То я советую вам езжать в глушь, подальше." with dissolve
    
    costya "Там нет ни камер ни стукачей." with dissolve

    costya "Россия большая. Никто вас найти не сможет, ни полиция, ни дагестанцы." with dissolve

    costya "Ладно, желаю вам удачи! Чувствуйте себя как дома!" with dissolve

    costya "Я буду собирать свои вещи. Я уже завтра улетаю в Непал!" with dissolve

    hide Kostya with dissolve

    "С этими словами Костя ушел в комнату." with dissolve

    show Aliya straight_tshirt_worried2 with dissolve 

    aliya "Я только-только за эти дни успела почувствовать себя в безопасности." with dissolve

    aliya "И вдруг снова - полиция, меня ищут." with dissolve

    aliya "Мне немного не по себе." with dissolve

    aliya "Если мои родственники меня найдут, они же убьют меня!" with dissolve

    show Aliya straight_tshirt_worried2_2 with dissolve 

    me "Они не найдут тебя." with dissolve

    show Aliya straight_tshirt_worried2 with dissolve 

    aliya "Правда?" with dissolve

    show Aliya straight_tshirt_worried2_2 with dissolve 

    me "Я буду защищать тебя. И все мои друзья тоже." with dissolve

    show Aliya straight_tshirt_sad3 with dissolve 

    "Алия улыбнулась." with dissolve

    show Aliya straight_tshirt_worried2 with dissolve 

    aliya "Спасибо..." with dissolve

    show Aliya straight_tshirt_worried2_2 with dissolve 

    "В этот момент я услышал звуки поворота ключа у входной двери." with dissolve

    show milana_jacket neutral1 as Milana with dissolve:
        xpos -0.35

    "В квартиру вошла Милана." with dissolve

    show milana_jacket neutral2 as Milana with dissolve

    milana "Ребята, как же я рада вас видеть!" with dissolve

    milana "Хорошо, что вы смогли скрыться от ментов!" with dissolve

    milana "Я это так не оставлю! Я уже написала знакомому адвокату!" with dissolve

    milana "И я добавила его в наш чат." with dissolve

    milana "Он скоро приедет, и мы будем решать этот вопрос!" with dissolve

    show milana_jacket neutral1 as Milana with dissolve

    show Aliya straight_tshirt_worried2 with dissolve 

    aliya "Спасибо..." with dissolve

    show Aliya straight_tshirt_worried2_2 with dissolve 

    show milana_jacket neutral2 as Milana with dissolve

    milana "Пойдем пока на кухню?" with dissolve

    jump branch1_day5_conspiracy_kitchen1


label branch1_day5_conspiracy_kitchen1:

    scene kitchen_table_back_night

    show AliyaSitTableKitchen aliya_sit_kitchen zorder 1

    show kitchen_table_front_night2 as kitchen_table_front_night zorder 2

    show milana_kitchen milana_kitchen as milana

    show black zorder 3

    hide black with dissolve

    "Мы уютно расположились на кухне." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "Говоришь, у тебя отец работал в полиции?" with dissolve

    show milana_kitchen milana_kitchen as milana

    aliya "Да, он бывший следователь." with dissolve

    aliya "Я не знаю, какие у него могут быть связи." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "А как он нашел тебя в первый раз?" with dissolve

    show milana_kitchen milana_kitchen as milana

    "Алия задумалась." with dissolve

    aliya "В сущности, ему даже не пришлось искать меня." with dissolve
    
    aliya "Мы с Семёном по глупости сами сказали ему, где я живу." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "В прошлый раз, получается, он даже не успел в полицию заявить?" with dissolve

    show milana_kitchen milana_kitchen as milana

    aliya "Ну он пришел в отдел полиции в Пятигорске." with dissolve

    aliya "И успел написать заявление." with dissolve
    
    aliya "Но полиция в Пятигорске еще не начала поиски." with dissolve

    "Алия задумалась." with dissolve

    aliya "По сути, он даже не знал что я сбежала в Москву." with dissolve

    aliya "Он думал что я прячусь в Пятигорске." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "В этот раз, наверное, он всерьез начал тебя искать." with dissolve

    milana "Я знаю некоторых беглянок, вроде тебя." with dissolve

    milana "Некоторые сбегали и жили без проблем." with dissolve

    milana "Меня например, полиция не искала." with dissolve

    milana "Хотя меня за мой побег все родственники прокляли." with dissolve

    show milana_kitchen milana_kitchen as milana

    "Милана усмехнулась." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "Но у одной моей подруги вайнашки после побега начались проблемы." with dissolve

    milana "Как раз как у тебя, где-то на третий день побега." with dissolve

    milana "Ее тоже задержала полиция, но мы нашли адвоката и смогли ее отбить." with dissolve

    milana "С этим адвокатом я тебя сейчас и познакомлю." with dissolve

    show milana_kitchen milana_kitchen as milana
    messenger "Новое сообщение" with dissolve

    show day5_time1352 as cg_screen_phone with dissolve:
        xalign 1.0

    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    "Я достал телефон." with dissolve

    hide cg_screen_phone_new_message
    
    show cg_messenger_cover_above_kitchen_night as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    $ phoneSayLawyerWithTitle(__("Всем привет!"))
    lawyer "[lastPhoneMsg!t]" with dissolve

    $ phoneSayLawyerWithTitle(__("Я уже выхожу из метро."))
    lawyer "[lastPhoneMsg!t]" with dissolve

    $ phoneSayLawyerWithTitle(__("Спускайтесь, встретимся в Макдоналдсе."))
    lawyer "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    me "Адвокат только что написал!" with dissolve

    me "Он уже приехал и выходит из метро." with dissolve

    me "Он говорит, чтобы мы встретили его у Макдоналдса." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "Тогда пойдем его встречать!" with dissolve

    show milana_kitchen milana_kitchen as milana

    me "Пошли!" with dissolve

    jump branch1_day5_mcdonalds_exterior5


label branch1_day5_mcdonalds_exterior5:

    stop music fadeout 1.0

    scene mcd_parking32 with dissolve
    
    show Aliya straight_hoodie_worried2_2 at any_left_pos with dissolve:
        ypos 1.1

    show milana_jacket neutral1 as Milana with dissolve:
        xpos -0.35

    play music "music/Runaway_10 (Pre_Loop).ogg"

    queue music "music/Runaway_10 (Loop).ogg"

    "Мы вышли на парковку." with dissolve

    show milana_jacket neutral2 as Milana with dissolve

    milana "Посмотри, что там говорит адвокат?" with dissolve

    show milana_jacket neutral1 as Milana with dissolve

    show cg_messenger_cover_above_mcd_night2 as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_screen_phone_night_dialog as cg_screen_phone:
        xalign 1.0 

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    "Я достал телефон." with dissolve

    $ phoneSayMe(__("Привет, где вы?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayLawyerWithTitle(__("Я уже на месте"))
    lawyer "[lastPhoneMsg!t]" with dissolve

    $ phoneSayLawyerWithTitle(__("Жду вас на летней веранде!"))
    lawyer "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошо"))
    me "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    me "Он говорит, что уже ждет нас на веранде!" with dissolve

    show milana_jacket neutral2 as Milana with dissolve

    milana "Тогда поспешим туда!" with dissolve

    scene black with dissolve

    "И мы пришли на летнюю террасу в Макдоналдсе." with dissolve

    jump branch1_day5_mcdonalds_exterior3_lawyer


label branch1_day5_mcdonalds_exterior3_lawyer:

    scene m_table_evening_bkg

    show AliyaSitTableLeft hoodie_hands_down_worried4 at any_left_pos zorder 1

    show milana_table table1 as Milana zorder 1

    show lawyer neutral as Lawyer zorder 2

    show m_table_evening_table zorder 3

    show black zorder 4

    hide black with dissolve

    "Мы сидели за столиком в Макдоналдсе." with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Итак, меня зовут Александр, я адвокат." with dissolve
    
    lawyer "Расскажите про вашу ситуацию." with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve

    aliya "Меня зовут Алия, я из Дагестана." with dissolve

    aliya "Я сбежала из дома." with dissolve

    aliya "С помощью Семёна." with dissolve

    aliya "Потому что меня дома хотели насильно выдать замуж." with dissolve

    aliya "Родители заперли меня дома, и никуда не выпускали." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Вам есть 18 лет?" with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve

    aliya "Да." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "По закону, вы можете жить где угодно, и никто вас не может ограничивать." with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve

    aliya "Тогда почему меня ищет полиция?" with dissolve
    
    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "У меня до этого были доверительницы с Кавказа." with dissolve

    lawyer "И у них была похожая история." with dissolve

    lawyer "Возможно, ваши родители объявили вас как пропавшую без вести." with dissolve

    lawyer "Например, ваш отец пришел в отдел полиции в Дагестане и сказал, что потерял свою дочь." with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve
    
    aliya "Что мне в таком случае делать?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Если вас объявили как потеряшку, то все не так уж и страшно." with dissolve

    lawyer "Вам нужно будет прийти в любое отделение полиции и написать заявление о снятии с розыска." with dissolve
    
    lawyer "Но я это не рекомендую пока что делать." with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve
    
    aliya "Почему?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    "Адвокат вздохнул." with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Когда вы напишете такое заявление, его отправят в Дагестан." with dissolve

    lawyer "И скорее всего, оно попадет в руки ваших родителей. Они будут знать где вы находитесь." with dissolve
    
    lawyer "Но это не единственная причина." with dissolve

    lawyer "Скажите пожалуйста, вы когда сбегали из дома, вы не брали с собой никаких денег и драгоценностей?" with dissolve
    
    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve
    
    aliya "Нет." with dissolve

    aliya "Я сбежала вот как есть." with dissolve

    aliya "Я не взяла с собой ни паспорта, ни телефона, ни денег, ни драгоценностей." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "В некоторых случаях, родственники пишут на свою дочь заявление о преступлении в полицию." with dissolve

    lawyer "Они говорят полицейским, что дочь украла у них драгоценности." with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve

    aliya "Но я же ничего не крала!" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Если ваши родители написали на вас такое заявление, это уже не важно." with dissolve

    lawyer "Полиция в Дагестане возбудит уголовное дело." with dissolve
    
    lawyer "А когда московские полицейские поймают вас, они уже не будут разбираться." with dissolve
    
    lawyer "Они отправят вас в Дагестан, а там вас уже поймают родители." with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve
    
    aliya "Дело плохо." with dissolve

    aliya "А как можно узнать, на меня написали заявление или нет?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Можно поискать информацию на сайте МВД Розыск." with dissolve

    lawyer "Если вы там есть, то у вас проблемы." with dissolve
    
    lawyer "Но если вас там нет, то это еще не означает, что вас не ищут." with dissolve
    
    lawyer "Я могу сделать адвокатский запрос в отдел МВД, куда скорее всего подали заявление ваши родители." with dissolve
    
    lawyer "Где вы жили до побега?" with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve

    aliya "Дагестан, село Караюрт." with dissolve

    aliya "Недалеко от Хунзаха." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Я тогда сделаю запрос в ваше районное ОВД." with dissolve

    lawyer "Получается, у вас нет паспорта?" with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve

    aliya "Да." with dissolve

    aliya "Я сегодня написала заявление об утере паспорта." with dissolve

    aliya "И мне написали дату и время, когда можно приходить за готовым." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Да, придется подождать." with dissolve

    lawyer "А пока что сидите тихо, пореже выходите на улицу." with dissolve

    lawyer "Про метро тоже можете забыть пока что." with dissolve

    lawyer "Я сделаю запрос в дагестанский ОВД и узнаю почему вас ищут." with dissolve
    
    lawyer "И заодно попробую пробить вас по базе через своих знакомых полицейских." with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve

    aliya "Хорошо..." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Есть еще один способ узнать, заведено ли на вас уголовное дело, или нет." with dissolve

    lawyer "Алия может попробовать получить справку о несудимости." with dissolve

    lawyer "Если есть какие-то уголовные дела, то в этой справке возможно будет эта информация." with dissolve

    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve
    
    aliya "Но если я пойду в полицию просить справку о несудимости, меня могут задержать прямо там?" with dissolve
    
    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve
    
    show lawyer neutral_speak as Lawyer with dissolve
    
    lawyer "Да." with dissolve

    lawyer "Но вы можете написать доверенность на другого человека." with dissolve

    lawyer "Тогда другой человек получит за вас эту справку." with dissolve

    show lawyer neutral as Lawyer with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Алия, давай я это сделаю." with dissolve

    milana "Завтра сходим к нотариусу, сделаем доверенность." with dissolve
    
    milana "И я получу за тебя справку о несудимости." with dissolve

    show milana_table table1 as Milana with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve

    aliya "Спасибо..." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Мне больше нечего сказать по вашему кейсу." with dissolve
    
    lawyer "Еще раз напомню - избегайте метро и оживленных улиц, там будут камеры." with dissolve

    lawyer "Будь начеку. Если вдруг вас задержит полиция - сообщай мне, я приеду." with dissolve
    
    show lawyer neutral as Lawyer with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 with dissolve

    aliya "Спасибо..." with dissolve

    milana "Спасибо большое, Александр! Тогда будем на связи?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 with dissolve

    show lawyer neutral_speak as Lawyer with dissolve

    lawyer "Да, хорошо, удачи вам! До связи!" with dissolve

    scene black with dissolve

    "И мы пошли домой..." with dissolve

    jump branch1_day5_mcdonalds_exterior4


label branch1_day5_mcdonalds_exterior4:

    scene mcd_parking32 with dissolve

    show Aliya straight_hoodie_worried2_2 at any_left_pos with dissolve:
        ypos 1.1

    show milana_jacket neutral1 as Milana with dissolve:
        xpos -0.35

    "Мы вышли на парковку." with dissolve

    show milana_jacket neutral2 as Milana with dissolve

    milana "Алия, давай завтра утром проснемся пораньше." with dissolve

    milana "И сделаем все дела." with dissolve

    milana "Вот здесь как раз недалеко отсюда Нотариус есть, сделаем доверенность." with dissolve

    milana "Заодно сходим на рынок, купим тебе новую одежду. Как тебе идея?" with dissolve

    show milana_jacket neutral1 as Milana with dissolve

    show Aliya straight_hoodie_worried2 with dissolve

    aliya "Да, хорошо." with dissolve

    show Aliya straight_hoodie_worried2_2 with dissolve

    show milana_jacket neutral2 as Milana with dissolve

    milana "Отлично, договорились." with dissolve

    milana "Ну ладно, пойдем домой?" with dissolve

    show milana_jacket neutral1 as Milana with dissolve

    show Aliya straight_hoodie_worried2 with dissolve

    aliya "Идем!" with dissolve

    scene black with dissolve

    "И мы пошли домой..." with dissolve

    jump branch1_day5_conspiracy_room_boys1


label branch1_day5_conspiracy_room_boys1:

    scene boy_room_night with dissolve

    "Я вернулся в спальню." with dissolve

    "Я сильно устал, но я попробовал вспомнить весь прожитый день снова." with dissolve

    "Начало дня было солнечным, и все шло хорошо." with dissolve

    "Алия подала заявку на оформление паспорта, а потом мы гуляли по Москве." with dissolve

    "Но потом нас чуть не задержала полиция в метро." with dissolve

    "Я вспомнил лицо полицейского и вздрогнул." with dissolve

    "Только благодаря счастливому случаю, нам удалось скрыться." with dissolve

    "И теперь мне было не по себе." with dissolve

    "Побег Алии оказался чуть более серьезным делом, чем я ожидал..." with dissolve

    "Надеюсь нам удасться избежать излишнего внимания полиции..." with dissolve

    scene black with dissolve

    "Я закрыл глаза и попробовал уснуть..." with dissolve

    "Со временем мои мысли успокоились, и я задремал..." with dissolve

    jump branch1_day6_conspiracy_room_boys


## ============================

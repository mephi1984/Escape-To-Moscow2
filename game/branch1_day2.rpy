label branch1_day2_start:

    scene semen_room_day_nophone with dissolve

    play music "music/naprtyag_loop.ogg" fadein 1.0

    queue music "music/naprtyag_loop.ogg"

    "Начался новый день." with dissolve

    show day2_time1012 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я вспомнил про вчерашний день и достал телефон." with dissolve

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0

    show cg_messenger_title_noname at cg_messenger_title_pos as cg_messenger_title zorder 20

    $ switchChatToNoName()

    $ phoneSayNoName(__("Привет, это снова я"))

    $ phoneSayNoName(__("В Караюрте адресов нет. Но ты найди на спутниковой карте мечеть"))

    $ phoneSayNoName(__("Слева от мечети дом с красной крышей - это наш дом. Я там"))

    $ phoneSayNoName(__("Если поедешь ко мне, то бери джип"))

    $ phoneSayNoName(__("Я удаляю сообщения у себя, но оставлю у тебя. Пока!"), True)

    "Ага, вижу, мне уже пришли несколько сообщений от Алии." with dissolve

    noName "Привет, это снова я." with dissolve

    noName "В Караюрте адресов нет. Но ты найди на спутниковой карте мечеть." with dissolve

    noName "Слева от мечети дом с красной крышей - это наш дом. Я там." with dissolve

    noName "Если поедешь ко мне, то бери джип." with dissolve

    noName "Я удаляю сообщения у себя, но оставлю у тебя. Пока!" with dissolve

    "Неплохо." with dissolve

    "Меня радует что Алия настроена решительно." with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    "Пора вставать. У меня сегодня будет нелегкий день." with dissolve

    show black with dissolve

    "Я встал, оделся, умылся и сел за компьютер." with dissolve

    show semen_room_table_day

    show cg_screen_youtube

    show black as black2 zorder 10

    hide black2 with dissolve

    "Я открыл свой ноутбук." with dissolve

    show cg_messenger_cover_above_desk as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    "Первым делом я открыл мессенджер и чат нашей группы." with dissolve

    $ phoneSayMe(__("Всем доброе утро, мне написала Алия"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Привет! Что она пишет?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoNameForwardedRight(__("Привет, это снова я"))

    $ phoneSayNoNameForwardedRight(__("В Караюрте адресов нет. Но ты найди на карте спутниковой мечеть"))

    $ phoneSayNoNameForwardedRight(__("Слева от мечети дом с красной крышей - это наш дом. Я там"))

    $ phoneSayNoNameForwardedRight(__("Если поедешь ко мне, то бери джип"))

    $ phoneSayNoNameForwardedRight(__("Я удаляю сообщения у себя, но оставлю у тебя. Пока!"), True)

    "Я переслал все сообщения от Алии." with dissolve

    $ phoneSayYarikWithTitle(__("Абы на чем не поедет, ей джип подавай)"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("В этом есть смысл"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("В Дагестане есть аулы, куда на легковушке не доедешь"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("И где мы возьмем джип?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("У меня есть знакомые в Оффроад Алерт"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Это сообщество автоволонтеров на джипах"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Обычно они занимаются поиском пропавших людей или вытаскиванием застрявших машин"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Но я им сейчас напишу, вдруг кто-то из них в Дагестане и готов помочь в таком щекотливом деле"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Отлично!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("У меня тоже есть новости"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Алия может покинуть Дагестан на самолете, без паспорта"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Через своих друзей я нашел пилота, который согласен помочь нам"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Он сказал что может взять тебя и Алию до Ростова-на-Дону"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Это хорошо! А дальше?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Можно сделать так - я приеду в Ростов, встречу вас там"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("И по трассе М4 Дон довезу до Москвы"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Отлично!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Получается, мы все соберемся в Москве"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Тогда я начну смотреть билеты для Семёна в Махачкалу"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я считаю, самое лучшее время для побега - это утро"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Предварительно план такой: Семён прилетает в Махачкалу ранним утром"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Затем на внедорожнике добирается до села Алии"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Подъезжаете к ее дому, встаете на видное место"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("В назначенное время Алия будет смотреть в окно"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Когда она увидит ваш джип, она выбегает из дома и прыгает внутрь"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Затем вы уезжаете, а потом и улетаете"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Хэппи энд!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("А что будет если нас догонят?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Ну значит - не повезло))"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__(")))"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Мда уж"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошо, я готов"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("О, мне как раз с Оффроад Алерта один чел написал"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Его зовут Рома, он живет в Махачкале"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("У него есть большой джип, и он заинтересовался твоей историей"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я его добавлю в чат?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Да, давай"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Добавляю"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Всем привет!"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Семён, я слышал про твои приключения"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("И я очень впечатлен"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Спасибо!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Я помогу тебе и Алие"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Я знаю Караюрт и дорогу до него"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Я могу привезти тебя туда, а затем увезти вас вдвоем куда надо"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Мой автомобиль - японский внедорожник. Проедет везде!"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaPhoto()

    "Рома выложил в чат фотографию своего автомобиля." with dissolve

    show cg_screen_phone_day_car_roma as cg_screen_phone2 zorder 21 with dissolve:
        xalign 1.0

    "Я открыл фото." with dissolve
    
    "Надо запомнить номер на всякий случай." with dissolve

    hide cg_screen_phone2 with dissolve

    $ phoneSayMe(__("О, отлично! Спасибо большое!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Семён, вот тут как раз есть билеты в Махачкалу в ночь"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("В Махачкалу ты прилетишь завтра, в 9 утра. Как тебе?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Да, норм. А сколько ехать до Караюрта?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Там где-то полторы сотни километров, 3 часа будем ехать"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Ничего себе"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Это Ингушетию ты можешь от края до края за полчаса проехать"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("А наш Дагестан большой!"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Тогда Семён, покупай билеты"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Если Алия с тобой свяжется, сообщи ей, чтобы ждала тебя завтра в полдень"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Я тогда свяжусь с пилотом, он вас будет ждать!"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Отлично!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я тогда начну собирать вещи"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Давай! Увидимся завтра!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Я тоже буду собираться. Мне нужно будет сейчас ехать в Ростов"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("И я тоже"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("А я буду ждать вас уже в Москве"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошо!"))
    me "[lastPhoneMsg!t]" with dissolve

    "И снова все складывается просто идеально." with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я немного нервничаю, потому что снова нужно бросать все и отправляться в путешествие." with dissolve

    "Но все же, решимость переполняет меня." with dissolve

    scene black with dissolve

    "Я купил авиабилеты и начал собираться..." with dissolve

    scene semen_room_night with dissolve

    "Почти все готово для поездки." with dissolve

    "Пора выключать ноутбук и паковать его в сумку." with dissolve

    "Алия вышла со мной на связь вчера примерно в это же время." with dissolve

    "Я все поглядываю на телефон, думая - будет ли у нее возможность написать сегодня?" with dissolve

    "Очень надеюсь, что скоро она мне напишет, иначе весь план придется менять." with dissolve

    scene black with dissolve

    "Прошло некоторое время..." with dissolve

    scene semen_room_night_empty with dissolve

    show day2_time0047 as cg_screen_phone with dissolve:
        xalign 1.0
    
    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    messenger "Новое сообщение." with dissolve

    hide cg_screen_phone_new_message

    show cg_messenger_cover_above_room at cg_messenger_cover_above_room_pos zorder 20

    show cg_screen_phone_night_dialog as cg_screen_phone:
        xalign 1.0

    show cg_messenger_title_noname at cg_messenger_title_pos zorder 20

    $ switchChatToNoName()

    $ phoneSayNoName(__("Привет, это я опять"))
    noName "[lastPhoneMsg!t]" with dissolve

    "Надо проверить, это действительно Алия?" with dissolve

    $ phoneSayMe(__("Какого цвета платье?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Синее"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Привет Алия!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Ты нашел мой дом на карте?"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Да."))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("У меня есть план как спасти тебя"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Рассказывай"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Завтра примерно в 12 часов, тебе нужно смотреть в окно"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("К твоему дому подъедет белый японский внедорожник, я буду тебя там ждать"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Тебе нужно будет добежать до машины и сесть в нее"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Из моего окна видно дорогу"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Когда я увижу машину, я смогу добежать до нее за пару минут"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Хорошо"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Предупреждаю, у моего отца много связей"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Как только он поймет что я сбежала, он сделает все чтобы найти меня"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Меня могут остановить и в аэропорту, и на блокпостах на дороге"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("А еще за нами может быть погоня"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я уже нашел выход"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я знаю как вывезти тебя из Дагестана"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Отлично"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Я постараюсь к утру найти и собрать свои документы"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Я доверяю тебе"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Пожалуйста, не подведи меня"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Если меня поймают, меня может быть убьют, да и тебя тоже"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я не боюсь твоего отца"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Спасибо"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Сестра идет"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Я удаляю переписку"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    $ var_dialog_stack['chatWithNoName'] = []

    "И все сообщения мгновенно пропали." with dissolve

    hide cg_messenger_title_noname

    hide cg_messenger_cover_above_room

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    "Пора садится в такси и ехать в аэропорт." with dissolve

    jump branch1_day2_taxi


label branch1_day2_taxi:

    scene black with dissolve

    "Я вышел из квартиры и сел в такси..." with dissolve

    stop music fadeout 2.0

    scene taxi_start with dissolve

    play music "ambience/237374__squareal__car-driving-interior.ogg" fadein 1.0 fadeout 1.0

    "И вот я еду в аэропорт." with dissolve

    "В прошлый раз меня вез Ярик." with dissolve

    "В этот раз я еду на такси, потому что времени достаточно." with dissolve

    "А Ярик сейчас едет в Ростов." with dissolve

    "Надо кстати спросить у них, как дела." with dissolve

    show cg_screen_phone_night_dialog as cg_screen_phone:
        xalign 1.0

    show cg_messenger_cover_above_taxi_day2 at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20


    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    "Я открыл мессенджер и чат нашей группы." with dissolve

    $ phoneSayMe(__("Всем доброй ночи, как у вас дела?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Мои новости - со мной связалась Алия, я сообщил ей план и она готова"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я сейчас еду в аэропорт, и улетаю в Махачкалу"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("У меня все отлично! Я жду вас в Москве"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Скоро встречу вас, надеюсь!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Я заправил полный бак в свой джип. Завтра утром еду в аэропорт, забирать Семёна!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Я связался с пилотом, он будет вас ждать в 12:30"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Он сказал, завтра скинет точные координаты, где его найти"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("А я на пути в Ростов"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Не смотри в телефон за рулем!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__(")))"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("У меня остановка на заправке"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я сейчас еду в аэропорт, и улетаю в Махачкалу"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Семён, тебе пора выключать телефон."))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Выключай режим радиомолчания!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошо. Всем пока!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above_taxi_day2

    hide cg_screen_phone with dissolve

    "Я перевел телефон в авиарежим, а затем достал симкарту." with dissolve

    "Симкарту я скотчем приклеил к задней крышке телефона." with dissolve

    "Что же, боюсь что теперь до меня навряд ли кто-то дозвонится!" with dissolve

    "Радиостанция прервалась на новости." with dissolve

    radio "Двадцать два часа, в эфире новости." with dissolve

    radio "В Китае зафиксирована вспышка нового, раннее не известного вируса." with dissolve

    radio "Национальная комиссия здравоохранения Китая начала расследование..." with dissolve

    play music_crossfade "music/synthwave_final_radio_room.ogg" fadein 1.0

    queue music_crossfade "music/synthwave_final_radio_room.ogg"

    "Таксист переключил на другую радиостанцию." with dissolve

    "Вспышка нового вируса, надо же." with dissolve

    "Пять лет назад была вспышка ближневосточного респираторного синдрома в Южной Корее." with dissolve

    "Еще раньше были свиной грипп, птичий грипп." with dissolve

    "Совсем олды вспомнят выспышку атипичной пневмонии." with dissolve

    "А в СМИ только панику разводят." with dissolve

    "Интересно, как назовут вирус в этот раз? Бычий грипп?" with dissolve

    "Впрочем, неважно." with dissolve

    "Мне нужно сосредоточиться на спасении Алии." with dissolve

    scene black with dissolve

    stop music_crossfade fadeout 2.0

    stop music fadeout 2.0

    "Прошло немного времени, и мы приехали в аэропорт." with dissolve

    "Я зарегистрировался, сел на рейс и улетел в Махачкалу..." with dissolve

    jump branch1_day3_airplane

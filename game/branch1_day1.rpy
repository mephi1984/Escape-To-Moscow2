label branch1_day1_start:

    scene black

    show branch1_semyon_room_bedside_table1 with dissolve

    play music "music/Runaway_01 (Pre_Loop).ogg"

    queue music "music/Runaway_01 (Loop).ogg"

    "Я лежу в постели и пытаюсь заснуть." with dissolve

    "Я уже почти уснул, но вдруг..." with dissolve

    play sound "sound/555154__nomerodin1__vibrating-message.ogg"

    show branch1_semyon_room_bedside_table2 with dissolve

    hide branch1_semyon_room_bedside_table1

    stop music fadeout 3.0

    messenger "Новое сообщение" with dissolve

    show branch1_semyon_room_bedside_table3 with dissolve

    hide branch1_semyon_room_bedside_table2

    show day1_time2237 as cg_screen_phone with dissolve:
        xalign 1.0

    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    "На экране блокировки не написано, от кого сообщение." with dissolve

    "Это означает только одно - сообщение отправлено через секретный чат." with dissolve

    play music "music/moscow_napryag.ogg" fadein 1.0

    queue music "music/moscow_napryag.ogg"

    "Мое сердце забилось быстрее..." with dissolve

    hide cg_screen_phone_new_message

    show cg_messenger_cover_above_bed at cg_messenger_cover_above_room_pos zorder 20

    show cg_screen_phone_night_dialog as cg_screen_phone:
        xalign 1.0

    show cg_messenger_title_noname at cg_messenger_title_pos zorder 20

    $ switchChatToNoName()

    $ phoneSayNoName(__("Привет"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Это я"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Алия?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Да"))
    noName "[lastPhoneMsg!t]" with dissolve

    "Стоп, а вдруг это не Алия? Вдруг кто-то разыгрывает меня?" with dissolve

    $ phoneSayMe(__("Как я могу проверить что это действительно ты?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Я читала тебе стихи в самолете"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Мы купили синее платье"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Достаточно, я верю тебе"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Как ты?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("У меня мало времени"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Родители меня обманули"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("У меня отобрали паспорт и телефон"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Меня привезли в Дагестан и не выпускают из дома"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Сестра вышла ненадолго, я пишу с ее телефона"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Свадьба будет через неделю"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Я хочу сбежать, но я не знаю как"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Это просто жесть"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я тебя не брошу, я постараюсь тебя вытащить оттуда"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Сестра возвращается"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Я напишу тебе потом"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ phoneSayNoName(__("Я удаляю нашу переписку"))
    noName "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    $ var_dialog_stack['chatWithNoName'] = []

    "И все сообщения мгновенно пропали." with dissolve

    hide cg_messenger_title_noname

    hide cg_messenger_cover_above_bed

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    scene black with dissolve

    "Похоже, в эту ночь я не смогу поспать..." with dissolve

    scene semen_room_night with dissolve

    "Я не так давно вернулся в свой родной город." with dissolve

    "Немножко разгреб долги по заказам, немножко погасил долги на своей кредитке." with dissolve

    "Днем я забивал себе голову работой, заказами и ежедневной рутиной." with dissolve

    "Но каждый раз когда я завершал работу и ложился спать," with dissolve

    "я снова вспоминал Алию и думал о ней." with dissolve

    "Как она там? Замужем она или еще нет?" with dissolve

    "Да что там замужем - жива ли она или еще нет?" with dissolve

    "Почему она не отвечает на мои сообщения?" with dissolve

    "Зачем она отправила меня в ЧС?" with dissolve

    "Все эти вопросы не давали мне уснуть каждую ночь." with dissolve

    "Но вот сейчас неожиданно Алия дала о себе знать." with dissolve

    show black with dissolve

    "Что же, пора действовать." with dissolve

    show semen_room_table_night

    show cg_screen_youtube

    show black as black2 zorder 10

    hide black2 with dissolve

    "Включаю ноутбук, запускаю браузер." with dissolve

    "Пока компьютер открывается, запускаю чат с Напарником." with dissolve

    show cg_screen_phone_night_dialog as cg_screen_phone:
        xalign 1.0

    show cg_messenger_title_coach at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_messenger_cover_above_desk_night at cg_messenger_cover_above_room_pos zorder 20

    $ switchChatToCoach()

    $ phoneSayMe(__("Привет"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Мне написала Алия"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("Таак"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("У меня аж кофе чуть из рук не выпал"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("Ты серьезно?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Да."))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("У нее отобрали телефон и заперли ее дома"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("Как она тогда тебе написала?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Она написала мне с телефона сестры"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("Откуда ты знаешь что это точно она?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("Вдруг это ее брат развлекается"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Она мне сказала детали которые знает только она"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Про стихи и платье"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("Очень умно"))
    coach "[lastPhoneMsg!t]" with dissolve

    "Наступило неловкое молчание. Я не знал как продолжить диалог." with dissolve

    $ phoneSayCoach(__("Она написала тебе, потому что ей больше не на кого надеятся, кроме тебя"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("Хочешь спасти ее снова?"))
    coach "[lastPhoneMsg!t]" with dissolve

    # !!! Поставить развилку - возможность слиться

    menu:

        "Что сделать?"

        "Спасать Алию.":

            jump branch1_day1_start2

        "Нет, я больше в этом не участвую.":

            jump branch1_day1_start_fail

label branch1_day1_start_fail:
    
    $ phoneSayMe(__("Нет, с меня достаточно."))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я не хочу больше рисковать своей жизнью."))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("В таком случае забей на нее, и возвращайся к работе."))
    coach "[lastPhoneMsg!t]" with dissolve

    "Разум подсказывал мне, что не стоит ввязываться в эту историю снова." with dissolve

    scene black with dissolve

    stop music fadeout 1.0

    "И лучший способ избежать проблем - никогда не участвовать в приключениях..." with dissolve

    return




label branch1_day1_start2:
    "Остатки сомнений растворились. Я почувствовал решимость." with dissolve

    $ phoneSayMe(__("Да."))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я начинаю операцию Побег 2.0"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Присоединишься?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("Ах ты сукин сын, я в деле"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoach(__("Думаю, Ярик тоже захочет в команду"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Да, собираем всех!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    $ switchChatToEscapeRoom()

    $ renpy.pause(0.5)

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20 with dissolve

    "Я создал групповой чат, и добавил туда Напарника и Ярика." with dissolve

    $ phoneSayMe(__("Всем привет, это Семён. Все здесь?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я тут"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Я тоже здесь!"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("В двух словах, какие новости?"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошие новости: Алия жива"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Плохие новости: она сейчас в Дагестане, в своем родном селе"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Родители заперли ее дома, а также отобрали у нее паспорт и телефон"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Алия хочет сбежать, но не знает как"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Я может не очень разбираюсь, но может ей просто сбежать через окно например?"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Ярик, в Дагестане это так не работает"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Там села небольшие, все друг друга знают"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("И расстояния между селами значительные"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Через село обычно проходит только одна дорога"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Она не успеет дойти до другого села, ее хватяться и будут искать"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Возможно она не успеет даже выйти из села, ее заметят перехватят на полпути"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("А может она поймает попутку?"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Там трафик маленький - хорошо если хотя бы одна машина в час будет проезжать через село"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Надо что-то придумать"))
    me "[lastPhoneMsg!t]" with dissolve

    jump branch1_day1_step1_choice

label branch1_day1_step1_choice:

    if (branch1_day1_step1_taxi_asked == True) and (branch1_day1_step1_offroad_asked == True):
        jump branch1_day1_step1_come

    menu:

        "Что предложить?"

        "Предложить взять такси." if branch1_day1_step1_taxi_asked == False:

            jump branch1_day1_step1_taxi

        "Предложить пойти пешком по бездорожью." if branch1_day1_step1_offroad_asked == False:

            jump branch1_day1_step1_offroad

        "Предложить приехать к Алие.":

            jump branch1_day1_step1_come


label branch1_day1_step1_taxi:

    $ branch1_day1_step1_taxi_asked = True

    $ phoneSayMe(__("Может быть Алия закажет такси?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Нет, Семён, это не просто"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Там в селе нет агрегаторов такси, как ты привык"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("В Дагестане \"вызвать такси\" означает позвонить таксисту лично"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("А там наверняка все местные таксисты знают эту семью"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Они однозначно не будут увозить Алию и сольют ее родокам"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Да уж"))
    me "[lastPhoneMsg!t]" with dissolve

    jump branch1_day1_step1_choice

label branch1_day1_step1_offroad:

    $ branch1_day1_step1_offroad_asked = True

    $ phoneSayMe(__("Может быть Алия сойдет с дороги и пойдет пешком по земле?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("По какой земле? Семён, Дагестан это не равнина, это горы"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("В Дагестане аулы находятся в ущельях между горами"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Там же в ущелье обычно проходит единственная дорога через село"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Свернуть с дороги - это значит подниматься в горы"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Да, там есть места где можно пройти: перевалы всякие, тропы"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Но бывает и так что идешь по дороге, слева - обрыв, а справа - крутой склон"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я еще посмотрю какая там местность вокруг ее села, но скорее всего - это не вариант"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я понял"))
    me "[lastPhoneMsg!t]" with dissolve

    jump branch1_day1_step1_choice


label branch1_day1_step1_come:

    $ phoneSayMe(__("Тогда как насчет того чтобы приехать к Алие и забрать ее?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Да, похоже что это единственный способ вытащить ее оттуда"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Семён, тебе нужно отправиться в путешествие в Дагестан"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Мне?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Алия знает тебя и доверяет только тебе"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Тебе нужно будет приехать в ее село и забрать ее оттуда"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("А как я доберусь до ее села?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Может меня кто-нибудь подбросит?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Ярик, среди нас ты единственный, у кого есть машина"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("У меня заниженный корч для дрифта"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Я боюсь, моя машина плохо приспособлена к дорогам в Дагестане"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Ладно. Семён, тогда тебе нужно будет прилететь в Дагестан"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("И дальше наземным транспортом приехать к Алие"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("И забрать ее оттуда"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Но тут есть другая проблема"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Какая?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Как ты говорил, ее отец - бывший следователь"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("У него полно связей в Дагестане среди ментов"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Когда он узнает что Алия пропала, он немедленно объявит ее в розыск"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("И скорее всего, вас будут ловить на постах ДПС на границе Дагестана"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("И как же нам тогда выбраться?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("На самолете не вариант?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Алия сбежит без паспорта"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Она не сможет сесть в самолет без документов"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Семён, план с самолетом мне нравится"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("И у меня есть идея, как можно улететь без паспорта"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Я сейчас спишусь с одним знакомым челом, надо кое-что уточнить"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Ярик, если у тебя получится, то это было бы идеально!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Спасибо Ярик!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("А что Алия будет делать после того как сбежит?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("У нее же нет паспорта"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("В первую очередь ей нужно будет выехать в безопасное место"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("За пределы Дагестана"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Как раз сейчас я нахожусь в Москве, по своим делам"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я предлагаю Алие приехать в Москву, как в прошлый раз"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("В Москве мы заселим ее на конспиративную квартиру"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("А потом она должна объявить паспорт утерянным и начать делать новый"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Отличный план!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Итак, мы определились"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я подумаю как тебе добраться до Алии"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("А я уточню насчет того, как Алии улететь из Дагестана"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Отлично"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Семён, я еще одну вещь хочу уточнить"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Если у родителей Алии есть связи в полиции"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("То они могут тебя отследить по твоему телефону"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Отец Алии сможет отследить твое местоположение"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("И они смогут через тебя найти Алию!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Да, точно!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Что же делать?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Может дадим Семёну новый чистый телефон с чистой симкой?"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Я могу через своих друзей попробовать пробить симки"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Отличная идея!"))
    me "[lastPhoneMsg!t]" with dissolve
    
    $ phoneSayMe(__("Давайте сразу два телефона"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Один мне, и второй Алие!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Хорошо, сделаем!"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Семён, тогда перед поездкой тебе нужно будет выключить телефон"))
    coach "[lastPhoneMsg!t]" with dissolve
    
    $ phoneSayCoachWithTitle(__("Или перевести его в авиарежим"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("И вытащить сим-карту"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Тогда менты не смогут отследить твое местоположение по триангуляции"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошо, я сделаю это когда буду ехать в аэропорт!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Когда Алия свяжется с тобой в следующий раз?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я не знаю"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я не могу написать ей"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Она сама выходит на связь когда у нее есть возможность"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Будем надеятся, она напишет тебе, и не раз"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Что же, предлагаю на сегодня закончить"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Завтра будет очень сложный день"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Семён, готовься к тому что в течение пары дней тебе нужно будет лететь в Махачкалу"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошо!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Всем пока, до завтра! Пишите если что"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Пока-пока!"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Спасибо, пока!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above_desk_night

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    "Спать мне совершенно не хотелось." with dissolve

    "Обычно свежий воздух помогает мне уснуть." with dissolve

    scene black with dissolve

    "Поэтому я оделся и вышел на балкон." with dissolve

    show branch1_balcony_bkg_1 zorder 1:
        xpos -0.4

    show branch1_balcony_layer1_1 zorder 11:
        xpos -0.4

    show black

    hide black with dissolve

    "Ночь сегодня была особенно свежа." with dissolve

    "Я смотрел на ночной город." with dissolve

    "Тысячи людей живут своей жизнью, учатся, работают, женятся, заводят детей, умирают." with dissolve

    "Обычная жизнь обычных обывателей, чья мечта - квадратные метры и иномарка." with dissolve

    "Иногда я задумывался - что заставляет сделать подвиг? Что заставляет человека стать героем?" with dissolve

    "Герои есть в книгах, в фильмах, в компьютерных играх. Герои преодолевают свой страх и бросаются совершать подвиги." with dissolve

    "Подвиги можно совершать и в обычной жизни." with dissolve

    "Иногда можно прочитать про героев, которые спасали детей из огня или вытаскивали тонущих людей из реки." with dissolve

    "Но я никогда не примеривал на себя роль героя. Это звучало... странно." with dissolve

    "Мы привыкли равнодушно проходить мимо зла, делая вид что это нас не касается." with dissolve

    "Если мы видим как гопники пристают к девушке в подземном переходе - мы стыдливо отводим глаза и уходим прочь." with dissolve

    "Чтобы остановить хулиганов, иногда достаточно лишь остановиться, обратить внимание и громко сказать \"Эй! Руки прочь!\"." with dissolve

    "Но из десятков прохожих, никто так и не остановится, чтобы произнести это \"Руки прочь!\"." with dissolve

    "Каждый ждет что это сделает кто-то другой." with dissolve

    "Это называется эффект свидетеля." with dissolve

    "И вот ты оглядываешься по сторонам, и понимаешь, что никого, кроме тебя и нет." with dissolve

    "Никто не защитит девушку, если это не сделаешь ты." with dissolve

    "Никто, кроме тебя." with dissolve

    "И если ты струсишь, то у тебя больше не будет оправданий своей трусости." with dissolve

    "И тогда я встаю, и твердым голосом говорю: \"Эй! Прекратите!\"." with dissolve

    "Да, я не качок, я не занимаюсь единоборствами." with dissolve

    "Да, мое тело слегка дрожит, когда я бросаю вызов гопникам." with dissolve

    "Но гопники ничего этого не знают. Мое тело скрыто одеждой, под которой не видно что я не качок." with dissolve

    "Гопники думают, что если кто-то посмел бросить им вызов - значит, его следует опасаться." with dissolve

    "Один лишь только факт что кто-то из безразличной толпы обратил внимание на их дела, может радикально изменить ситуацию." with dissolve

    "Нужно лишь только назвать зло - злом, нужно лишь только произнести вслух \"Руки прочь от девушки, негодяи!\"." with dissolve

    "Это может привлечь других людей в толпе, которые боялись выступить первыми." with dissolve

    "И гопники, оценив ситуацию, могут отступить и оставить девушку в покое." with dissolve

    "Это и есть героизм." with dissolve

    "Да, в наш век цинизма принято говорить что все не так однозначно." with dissolve

    "Можно наверняка найти сто оправданий, почему зло называется добром, а добро называется злом." with dissolve

    "Можно это все объявить традициями, можно сказать что так тут заведено." with dissolve

    "Выдавать замуж девушку против ее воли - наверное, это тоже определенная традиция, определенных народов." with dissolve

    "Но вот я встал и объявляю вслух - свадьба по принуждению это зло, этого не должно быть в современном мире." with dissolve

    "И у меня достаточно смелости, чтобы попытаться остановить зло." with dissolve

    "Да, я не знаю, хватит ли у меня сил и способности." with dissolve

    "Возможно все закончится уголовным делом, или чем-то похуже." with dissolve

    "Но если Алие не помогу я - ей не поможет больше никто." with dissolve

    "Всем людям вокруг наплевать на ее судьбу, всем наплевать на творимое ее родственниками зло." with dissolve

    "Только я один могу спасти ее." with dissolve

    "И кто знает, может быть этого окажется достаточно." with dissolve

    "У меня есть шанс на успех." with dissolve

    "Ночь сегодня была особенно свежа." with dissolve

    show branch1_balcony_bkg_2 zorder 2:
        xpos -0.4
        alpha 0.0
        linear 2.0 alpha 1.0


    show branch1_balcony_layer1_2 zorder 12:
        xpos -0.4
        alpha 0.0
        linear 2.0 alpha 1.0

    "Свет в домах напротив потихоньку исчезал." with dissolve

    "Время уже позднее." with dissolve

    "Теперь уже точно пора идти спать." with dissolve

    scene black with dissolve

    "Я вернулся в комнату и лег спать." with dissolve

    show perlin at credits_perlin_pos zorder 2 with dissolve:
        alpha 0.5
        xpos 0.0
        linear 120.0 xpos -2.0

    "Уснуть было тяжело." with dissolve

    show perlin as perlin2 at credits_perlin_pos zorder 4 with dissolve:
        alpha 0.5
        xpos -1.0
        linear 80.0 xpos -2.0

    "Мысли все крутились в моей голове." with dissolve

    show Aliya turn_around_hand_down_jacket_worried1_1 at any_center_pos zorder 3 with dissolve:
        alpha 0.5


    "Передо мной возник образ." with dissolve

    "Знакомый образ девушки, которую я знал всего один день." with dissolve

    "Но которая теперь навсегда впечалась в мою память." with dissolve

    show Aliya turn_around_hand_down_jacket_worried1_3 at any_center_pos zorder 3 with dissolve:
        alpha 0.5

    aliya "Это твой последний шанс." with dissolve

    aliya "В этот раз ты не имеешь права на ошибку." with dissolve

    show Aliya turn_around_hand_down_jacket_sad4 at any_center_pos zorder 3 with dissolve:
        alpha 0.5

    "Я попытался что-то ответить, но не смог." with dissolve

    show Aliya turn_around_hand_down_jacket_sad4 at any_center_pos zorder 3 with dissolve:
        alpha 0.2

    "Знакомый силуэт плавно начал исчезать прямо на моих глазах." with dissolve

    hide Aliya with dissolve

    hide perlin2 with dissolve

    "А потом и вовсе исчез." with dissolve

    hide perlin with dissolve

    "Все поглотила тьма..." with dissolve

    jump branch1_day2_start

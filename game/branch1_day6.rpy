label branch1_day6_conspiracy_room_boys:

    play music "music/Runaway_08 (Pre_Loop).ogg"

    queue music "music/Runaway_08 (Loop).ogg"

    scene boy_room_day with dissolve

    "Наступило утро." with dissolve


    show day6_time1134 as cg_screen_phone with dissolve:
        xalign 1.0

    "Часы на телефоне показывали 11:34." with dissolve

    "Я сегодня очень долго поспал." with dissolve

    "Было чувство, что я проспал все на свете." with dissolve

    "Самое время вставать." with dissolve

    scene black with dissolve

    "Я встал и вышел в коридор." with dissolve

    jump branch1_day6_conspiracy_hall_morning



label branch1_day6_conspiracy_hall_morning:

    scene corridor_day_open with dissolve

    "В коридоре было тихо." with dissolve

    me "Алия, ты здесь?" with dissolve

    me "Кто дома?" with dissolve

    "Тишина была мне ответом." with dissolve

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_messenger_cover_above_corridor as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    "Я открыл телефон и написал в чат." with dissolve

    $ phoneSayMe(__("Всем доброе утро, где вы?"))
    me "[lastPhoneMsg!t]" with dissolve

    "В ответ молчание." with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    "Милана говорила вчера, что пойдет с Алией заниматься делами." with dissolve

    "Доверенность оформить, вещи купить и так далее." with dissolve

    "Наверное, они сейчас идут где-то по улице." with dissolve

    "Немного непривычно, что Алия сейчас далеко." with dissolve

    "Все это время я плотно общался с ней." with dissolve

    "Она была все время рядом, можно было спросить у нее, как она себя чувствует." with dissolve
    
    "А сейчас ее нет рядом." with dissolve

    "На меня напали воспоминания о нашем первом побеге." with dissolve

    "Я целый день провел с ней, а потом она пропала." with dissolve

    "Я уже думал, что она пропала навсегда." with dissolve

    "Но сейчас же все по-другому!" with dissolve

    "Она просто ушла гулять с Миланой..." with dissolve

    "Ведь так?.." with dissolve

    "А что если полиция выследила их?" with dissolve

    "Что если родственники уже нашли Алию и вернули домой?" with dissolve

    "А я все проспал!" with dissolve

    "Мне стало страшно..." with dissolve

    messenger "Новое сообщение" with dissolve

    show day6_time1146 as cg_screen_phone with dissolve:
        xalign 1.0

    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    "Я достал телефон." with dissolve

    hide cg_screen_phone_new_message
    
    show cg_messenger_cover_above_corridor as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    $ phoneSayCoachWithTitle(__("У нас все хорошо, мы идем домой"))
    coach "[lastPhoneMsg!t]" with dissolve

    "Я почувствовал облегчение." with dissolve

    $ phoneSayCoachWithTitle(__("Мы сходили с Алией в оружейный магазин"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я купила ей газовый пистолет Добрыня"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Теперь никакие дагестанцы ей не страшны!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Отлично!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("А вы купили ей сменную одежду?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Ой, нет, не успели"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Кстати, Семён, ты можешь сходить с Алией в супермаркет?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Мне нужно бежать по делам уже"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Конечно!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Тогда одевайся и выходи!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Мы будем ждать тебя возле Макдоналдса!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Иду!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    "Зря я беспокоюсь и паникую, все хорошо." with dissolve

    scene black with dissolve

    play music "music/Runaway_09 (Pre_Loop).ogg"

    queue music "music/Runaway_09 (Loop).ogg"

    "С этими мыслями я оделся и пошел на улицу." with dissolve

    jump branch1_day6_mcdonalds_exterior1


label branch1_day6_mcdonalds_exterior1:

    scene mcd_parking33 with dissolve

    show Aliya half_turn_hand_down_hoodie_sad3 at any_left_pos with dissolve:
        ypos 1.1

    show milana_jacket neutral1 as Milana with dissolve:
        xpos -0.35

    "Я подошел к Макдоналдсу. Алия и Милана уже были тут." with dissolve

    show milana_jacket neutral2 as Milana with dissolve

    milana "О, Семён, привет!" with dissolve

    milana "Все, я вас оставляю тут вдвоем." with dissolve

    milana "Давай, удачи вам!" with dissolve

    hide Milana with dissolve

    me "Привет! Как ты?" with dissolve

    show Aliya half_turn_hand_down_hoodie_sad1 with dissolve

    aliya "Не очень." with dissolve

    aliya "Я плохо спала, мне снились кошмары." with dissolve

    aliya "Я все время убегала от своих родственников, а они все время меня преследовали." with dissolve

    aliya "Это ужасные сны, а я просто хочу спать спокойно." with dissolve

    show Aliya half_turn_hand_down_hoodie_sad3 with dissolve

    me "Эх сочуствую." with dissolve

    show Aliya half_turn_hoodie_neutral2 with dissolve

    aliya "Милана купила мне пистолет Добрыня." with dissolve
    
    aliya "Сказала, если дагестаны будут меня доставать - нужно стрелять в них." with dissolve

    show Aliya half_turn_hoodie_neutral1 with dissolve

    "Да, это очень хорошая идея." with dissolve

    me "Правильно! Стреляй, не жалей их!" with dissolve

    show Aliya half_turn_hoodie_happy1_1 with dissolve

    "Алия улыбнулась." with dissolve

    show Aliya half_turn_hoodie_happy1_2 with dissolve
    
    aliya "Еще мне нужно купить средства гигиены." with dissolve
    
    aliya "Пойдешь со мной в магазин?" with dissolve

    show Aliya half_turn_hoodie_happy1_1 with dissolve

    me "Конечно!" with dissolve

    me "Пойдем!" with dissolve

    scene black with dissolve

    "И мы пошли в супермаркет." with dissolve

    jump branch1_day6_supermarket


label branch1_day6_supermarket:

    scene shop5_view2_ver1 with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 at any_left_pos zorder 3 with dissolve:
        ypos 1.1

    "Это был обычный супермаркет, такие всегда появляются возле крупных станций метро." with dissolve
    
    "Здесь можно было купить еду, алкоголь, бытовую химию и многое другое." with dissolve

    me "Хочешь чипсы?" with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 with dissolve

    aliya "Давай!" with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 with dissolve

    "Я взял с полки пачку." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 with dissolve

    aliya "Я тоже кое-что возьму." with dissolve

    aliya "Но не ходи за мной." with dissolve

    hide Aliya with dissolve

    "Алия отошла к полке с прокладками." with dissolve

    "Взяла оттуда пачку," with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 at any_left_pos zorder 3 with dissolve:
        ypos 1.1

    "И вернулась ко мне." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 with dissolve

    aliya "Все можем идти к кассе." with dissolve
    
    aliya "Ты иди первый." with dissolve

    aliya "Я за тобой." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 with dissolve
    
    "Алия стесняется покупать прокладки, это так мило." with dissolve

    me "Ладно пойдем!" with dissolve

    scene black with dissolve

    "Мы рассчитались на кассе и вышли из супермаркета." with dissolve

    jump branch1_day6_mcdonalds_exterior2


label branch1_day6_mcdonalds_exterior2:

    scene mcd_parking33 with dissolve

    show Aliya straight_hoodie_neutral1 at any_left_pos zorder 3 with dissolve:
        ypos 1.1

    "Мы вышли на парковку у Макдоналдса." with dissolve

    show Aliya straight_hoodie_neutral2 with dissolve

    aliya "Мне осталось купить сменную одежду." with dissolve

    aliya "Но это можно сделать вечером." with dissolve

    aliya "Давай пойдем домой сейчас?" with dissolve

    show Aliya straight_hoodie_neutral1 with dissolve

    me "Конечно, идем!" with dissolve

    jump branch1_day6_conspiracy_exterior2


label branch1_day6_conspiracy_exterior2:

    play music "music/Runaway_12 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_12 (Loop).ogg"

    scene entrance_fight_bkg with dissolve

    show Aliya half_turn_hand_down_hoodie_sad3 at any_left_pos zorder 3

    "Мы подошли к подъезду." with dissolve

    "Я сразу увидел странных людей, которые стояли у подъезда." with dissolve

    me "Смотри, там кто-то есть!" with dissolve

    show Aliya_back back2 as Aliya at any_left_pos zorder 3 with dissolve

    "Алия обернулась и забеспокоилась." with dissolve

    me "Доставай пистолет!" with dissolve

    hide Aliya with dissolve

    show entrance_fight1 as entrance_fight with dissolve

    "Алия достала Добрыню и спряталась за трансформаторной будкой." with dissolve

    "Пока они нас не видят, я решил сфотографировать их." with dissolve

    show cg_screen_phone_day6_photo1 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я достал телефон и навел камеру..." with dissolve

    show cg_screen_phone_day6_photo3 as cg_screen_phone:
        xalign 1.0

    show cg_screen_phone_day3_photo2 as cg_screen_phone2:
        xalign 1.0
        alpha 0.0
        linear 0.3 alpha 1.0
        linear 0.3 alpha 0.0

    "И сфотографировал их." with dissolve

    hide cg_screen_phone2

    hide cg_screen_phone with dissolve

    show entrance_fight2 as entrance_fight with dissolve

    "Дагестанцы заметили нас." with dissolve

    "У нас не оставалось выбора." with dissolve

    play music "music/Runaway_15 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_15 (Loop).ogg"

    me "Стреляй быстрее, прямо в лицо!" with dissolve
    
    show entrance_fight3 as entrance_fight with dissolve

    "Алия прицелилась." with dissolve
    
    "Дагестанцы бежали прямо на нас!" with dissolve
    
    show entrance_fight4 as entrance_fight with dissolve

    play sound "sound/324473__150237_matthys__airsoft-gun-firing.ogg"

    "Я услышал легкий хлопок." with dissolve
    
    show entrance_fight5 as entrance_fight with dissolve

    "Один из дагестанцев остановился, закрывая лицо руками." with dissolve
    
    show entrance_fight6 as entrance_fight with dissolve

    play sound "sound/324473__150237_matthys__airsoft-gun-firing.ogg"

    "Я услышал второй хлопок." with dissolve
    
    show entrance_fight7 as entrance_fight with dissolve

    "Второй дагестанец тоже остановился и упал на колени." with dissolve
    
    show entrance_fight8 as entrance_fight with dissolve

    play sound "sound/324473__150237_matthys__airsoft-gun-firing.ogg"

    "Еще один хлопок и третий дагестанец тоже получил заряд." with dissolve

    show entrance_fight9 as entrance_fight with dissolve

    "Он остановился и начал тереть глаза." with dissolve
    
    me "Все, хватит бежим!" with dissolve

    show entrance_fight10 as entrance_fight with dissolve

    "Алия побежала прочь." with dissolve
    
    scene black with dissolve

    "И я побежал за ней." with dissolve

    jump branch1_day6_mcdonalds_exterior3


label branch1_day6_mcdonalds_exterior3:

    scene mcd_parking33 with dissolve

    show Aliya straight_hoodie_fright2 at any_left_pos zorder 3 with dissolve:
        ypos 1.1

    # Давай разделимся!!!

    "Алия тяжело дышала." with dissolve

    "Я чувствовал, что далеко убежать она не сможет." with dissolve

    me "Давай сделаем так!" with dissolve

    me "Беги в супермаркет и прячься там!" with dissolve

    me "А я отвлеку дагестанцев на себя!" with dissolve

    "Алия кивнула." with dissolve

    me "Беги быстро!" with dissolve

    hide Aliya with dissolve

    "Алия убежала прочь." with dissolve

    show mcd_parking33_dag with dissolve

    "И едва она скрылась, я увидел дагестанцев справа от Макдоналдса." with dissolve
    
    me "Эй, вы не меня ищете случайно?" with dissolve

    "Двое дагестанцев заметили меня и побежали за мной." with dissolve

    "Кажется, у меня хорошо получается агрить их на себя." with dissolve

    scene black with dissolve

    "И я убежал подальше." with dissolve

    jump branch1_day6_metro_novokosino_exterior



label branch1_day6_metro_novokosino_exterior:

    scene metro_novokosino_ext_day2 with dissolve

    "Когда я подбежал ко входу в метро, дагестанцы уже сильно отстали от меня." with dissolve

    "Здесь я замедлил темп и отдышался." with dissolve

    "Заходя в метро, я постарался аккуратно слиться с толпой." with dissolve

    jump branch1_day6_metro_novokosino_interior


label branch1_day6_metro_novokosino_interior:

    scene black with dissolve

    show metro_novokosino_int_train_open as metro_int

    show metro_novokosino_int_people1

    show black as black_front zorder 10

    hide black_front with dissolve

    stop music

    play music "ambience/novokosino_loop.ogg" fadein 1.0

    queue music "ambience/novokosino_loop.ogg"

    "И вот я здесь, в метро." with dissolve

    "Мне повезло - поезд как раз ждет меня с открытыми дверями." with dissolve


    scene black with dissolve

    show metro_novokosino_front as metro_front zorder 1:
        xpos 0.0

    show m_train_center_door_open as m_train zorder 2

    show m_train_center_people4 as people zorder 2.5

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

    "Теперь можно расслабиться." with dissolve

    "Да уж, я горжусь собой." with dissolve

    "Уже в который раз я, рискуя своей жизнью, спасаю Алию от дагестанцев." with dissolve

    "Я достал телефон." with dissolve

    show day6_time1221 as cg_screen_phone zorder 10:
        xalign 1.0

    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos zorder 11 with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    messenger "Новое сообщение" with dissolve

    "О, новые сообщения от Алии!" with dissolve

    stop music fadeout 1.0

    play music "music/Runaway_16 (Pre_Loop).ogg"

    queue music "music/Runaway_16 (Loop).ogg"

    hide cg_screen_phone_new_message

    show cg_screen_phone_day_dialog as cg_screen_phone zorder 10:
        xalign 1.0

    show cg_messenger_cover_above_metro as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_aliya at cg_messenger_title_pos as cg_messenger_title zorder 20

    $ switchChatToAliya()

    $ phoneSayAliya(__("Чтобы не подвергать вас и себя опасности, я решила покинуть вашу съемную квартиру"))

    $ phoneSayAliya(__("Я спрячусь в каком-нибудь шелтере, так мне будет спокойнее"))

    $ phoneSayAliya(__("Не ищите меня, дальше я буду жить сама"))

    $ phoneSayAliya(__("Этот телефон я выключаю, симку выкидываю. Больше сюда не пиши"))

    $ phoneSayAliya(__("Спасибо за все!"), True)

    aliya "Чтобы не подвергать вас и себя опасности, я решила покинуть вашу съемную квартиру." with dissolve

    aliya "Я спрячусь в каком-нибудь шелтере, так мне будет спокойнее." with dissolve

    aliya "Не ищите меня, дальше я буду жить сама." with dissolve

    aliya "Этот телефон я выключаю, симку выкидываю. Больше сюда не пиши." with dissolve

    aliya "Спасибо за все!" with dissolve

    "У меня аж помутнело в глазах." with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Все рухнуло, все разрушилось." with dissolve

    "Алия снова исчезла." with dissolve

    "Я снова потерял с ней связь." with dissolve

    "И если она попадет в беду, я не могу больше ей помочь..." with dissolve

    "У меня аж руки затряслись..." with dissolve

    jump branch1_day6_metro_tretyakovskaya_interior


label branch1_day6_metro_tretyakovskaya_interior:

    scene black with dissolve

    announcement "Станция Третьяковская. Поезд дальше не идет. Просьба освободить вагоны!" with dissolve

    "Громкий голос объявления вернул меня в реальность." with dissolve

    "Мне пришлось встать и пойти на выход..." with dissolve

    jump branch1_day6_metro_tretyakovskaya_exterior

label branch1_day6_metro_tretyakovskaya_exterior:

    scene kliment with dissolve

    "Я был на пешеходной дорожке." with dissolve

    "Вчера я гулял здесь с Алией." with dissolve

    "Она радовалась своей свободе." with dissolve

    "А сегодня - ее уже нет рядом со мной." with dissolve

    "Казалось бы, мы живем в век соцсетей, у каждого есть телефон и куча мессенджеров." with dissolve

    "Я думал, что в современном мире невозможно полностью потерять контакт с кем-то." with dissolve

    "Но увы, сейчас я потерял связь с Алией." with dissolve

    "Я не знаю где она находится, и где она теперь собирается жить." with dissolve

    "Тот телефонный номер, который я знал - уже больше недоступен." with dissolve

    "В социальных сетях Алии нет, а те аккаунты которые были - с момента побега заброшены." with dissolve

    "От родителей она сбежала, от полиции она успешно скрывается." with dissolve

    "И было бы лучше, если бы ни родители ни полиция не могли бы ее найти и дальше." with dissolve

    "От этой мысли мне немножко стало легче." with dissolve

    "Да, мне обидно что Алия так просто взяла и сбежала от меня." with dissolve

    "От чувства несправедливости мне хочется кричать." with dissolve

    "Но все не так уж и плохо." with dissolve

    "Все что я сделал - было не зря." with dissolve

    "Алия на свободе." with dissolve

    "У нее есть вещи, деньги, и ей есть где переночевать." with dissolve

    "У нее есть мои контактные данные." with dissolve

    "И я уверен, что когда мы снова свяжемся - я поговорю с ней." with dissolve

    "Я объясню ей, что мне очень неприятно, когда от меня так сбегают." with dissolve

    "Мы поговорим, она поймет, и больше не будет так делать." with dissolve

    scene black with dissolve

    "Эх, жаль что я не могу с ней поговорить сейчас..." with dissolve

    play music "music/ETM_Titles_track.ogg"
    queue music "music/ETM_Titles_track.ogg"

    scene kliment with dissolve

    "... ладно, надо взять себя в руки." with dissolve

    "Я достал телефон и открыл чат побега." with dissolve

    show cg_screen_phone_day_dialog as cg_screen_phone zorder 10:
        xalign 1.0

    show cg_messenger_cover_above_kliment as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    $ phoneSayMe(__("Возле конспиративной квартиры на нас напали дагестанцы"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMePhoto()
    "Я отправил фотографию с дагестанцами в чат." with dissolve

    $ phoneSayYarikWithTitle(__("Вот жесть"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Я аж чуть чаем не подавилась"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Семён ты в порядке?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я то да"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Но Алия убежала, выключила телефон и выкинула симку"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Вот последнее что она мне написала"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayAliyaForwardedRight(__("Чтобы не подвергать вас и себя опасности, я решила покинуть вашу съемную квартиру"))

    $ phoneSayAliyaForwardedRight(__("Я спрячусь в каком-нибудь шелтере, так мне будет спокойнее"))

    $ phoneSayAliyaForwardedRight(__("Не ищите меня, дальше я буду жить сама"))

    $ phoneSayAliyaForwardedRight(__("Этот телефон я выключаю, симку выкидываю. Больше сюда не пиши"))

    $ phoneSayAliyaForwardedRight(__("Спасибо за все!"), True)

    "Я переслал все сообщения от Алии." with dissolve

    $ phoneSayCoachWithTitle(__("Отчаянная засранка"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Дагестанцы все еще там?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я не знаю"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("А где ты сейчас?"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я у метро Третьяковская"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Не возвращайся на квартиру, они могут поджидать тебя"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Предлагаю объявить общий сбор"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayYarikWithTitle(__("Я за!"))
    yarik "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Семён, оставайся там, мы скоро приедем к тебе"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Держись там!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Спасибо"))
    me "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    show cg_screen_phone_day as cg_screen_phone with dissolve

    "Я выключил телефон." with dissolve

    show cg_screen_phone_call_arstan1 as cg_screen_phone with dissolve

    "Но не успел я убрать телефон, как мне позвонили." with dissolve

    show cg_screen_phone_call_arstan2 as cg_screen_phone with dissolve

    "Я поднял трубку." with dissolve

    dag "Семён привет, меня зовут Арстан, я двоюродный брат Алии." with dissolve

    dag "Что ты убегаешь постоянно, как не мужчина. Нам надо встретиться и поговорить." with dissolve

    me "Мне не о чем с вами говорить." with dissolve

    dag "Вот скажи мне, что ты вообще делаешь с Алией?" with dissolve

    dag "Я знаю что ты прилетал в Дагестан." with dissolve

    dag "Я знаю что ты со своим другом ездил в наше село и забрал ее оттуда." with dissolve

    dag "Я видел по записям с камер, как вы вдвоем гуляете в Москве." with dissolve

    dag "Вацок, у вас с ней любовь что ли?" with dissolve

    me "Я не буду разговаривать с вами." with dissolve

    dag "Семён, расслабься." with dissolve

    dag "Уже весь Дагестан знает, что она сбежала с тобой." with dissolve

    dag "Я могу поговорить с ее родителями." with dissolve

    dag "Сделаем все по красоте, организуем вашу свадьбу." with dissolve

    dag "И она будет твоей, без базара." with dissolve

    dag "Ты уже так далеко зашел, давай уже просто решим этот вопрос, брат." with dissolve

    "На секунду я задумался, но потом тотчас же выбросил эту мысль из головы." with dissolve

    "Родственникам Алии нельзя верить, я уже убедился в этом на собственном опыте." with dissolve

    me "Я не буду разговаривать с вами. До свидания." with dissolve

    dag "Ну хорошо, брат, как знаешь." with dissolve

    dag "Еще увидимся!" with dissolve

    show cg_screen_phone_call_arstan4 as cg_screen_phone with dissolve

    "Арстан положил трубку." with dissolve

    hide cg_screen_phone with dissolve

    "Что же, как минимум, Алию они до сих пор не нашли." with dissolve

    "Может быть и правда, ей сейчас безопаснее держаться подальше от меня?" with dissolve

    scene black with dissolve

    "Ладно, делать нечего, скоро ко мне приедут Милана и Ярик..." with dissolve

    jump branch1_day6_metro_tretyakovskaya_cafe1



label branch1_day6_metro_tretyakovskaya_cafe1:

    scene kliment_cafe1 with dissolve

    show milana_table table1 as Milana zorder 1:
        xpos -0.2
        ypos 0.2
        zoom 0.9

    show Yarik_notable neutral2 as Yarik zorder 2:
        xpos -0.25
        ypos 0.2
        zoom 0.9

    show kliment_cafe_table_food_down zorder 3

    show kliment_cafe_table_food_up zorder 4

    "Ярик и Милана пришли довольно быстро." with dissolve

    show Yarik_notable neutral1 as Yarik with dissolve

    yarik "Привет!" with dissolve

    show Yarik_notable neutral2 as Yarik with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Привет! Ну что, рассказывай." with dissolve

    show milana_table table1 as Milana with dissolve

    me "Когда ты уехала, я с Алией пошли домой." with dissolve

    me "И у подъезда мы увидели дагестанцев, словно поджидающих нас." with dissolve

    me "Я их сфоткал, они нас заметили, и один из них бросился в погоню за нами." with dissolve

    me "Мы сбежали." with dissolve

    me "Дальше мы с Алией разделились. Я отвлек на себя дагестанцев." with dissolve

    me "Я увел дагестанцев за собой до метро, и там он остал от меня." with dissolve

    me "А когда проверил телефон, увидел эти сообщения от Алии." with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Костя писал, что когда он выходил, то у подъезда было пусто. Дагестанцы уже ушли." with dissolve

    show milana_table table1 as Milana with dissolve

    me "Почему дагестанцы ждали у подъезда, но не зашли в квартиру?" with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Мне кажется, это потому что они не знают точного адреса." with dissolve

    milana "Смотри. Возможно, менты каким-то образом узнали твой номер телефона." with dissolve

    milana "Зная твой номер, менты вычислили твое примерное местоположение менты узнали по симке." with dissolve

    milana "Эту информацию менты слили дагестанцам, и они приехали тебя встречать." with dissolve

    show milana_table table1 as Milana with dissolve
    
    me "Звучит логично." with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Если они знают твой номер, скорее всего они знают и номер Алии." with dissolve

    milana "Она правильно сделала что выкинула свою симку." with dissolve

    milana "Как ты думаешь, Алие удалось успешно сбежать незамеченной?" with dissolve

    show milana_table table1 as Milana with dissolve

    me "Думаю да." with dissolve

    me "Полчаса назад мне позвонил Арстан, двоюродный брат Алии." with dissolve

    me "И начал меня убеждать, типа, давай поговорим и т.д." with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Не верь ему, дагестанцы обманывают жестко." with dissolve

    show milana_table table1 as Milana with dissolve

    me "Да, конечно. Но я подумал о другом." with dissolve

    me "Если бы они поймали Алию, они бы не стали мне звонить." with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Это значит, что ей удалось скрыться. Это радует." with dissolve

    show milana_table table1 as Milana with dissolve

    me "Где сейчас может быть Алия?" with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Вчера вечером я дала Алие листовку со списком телефонов правозащитных организации и шелтеров." with dissolve

    milana "Я уверена, что она связалась с кем-то из них, и сейчас заселяется в шелтер." with dissolve

    show milana_table table1 as Milana with dissolve

    me "Мы можем объездить все шелтеры и найти Алию?" with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Ну во-первых, никто тебя не пустит в шелтер." with dissolve

    milana "Во-вторых, тебе же звонил Арстан?" with dissolve

    milana "Это значит, что менты вычислили твой новый телефонный номер." with dissolve

    milana "А затем координаты всех твоих перемещений будут сначала на столе у ментов, а потом попадут в руки отцу Алии." with dissolve

    milana "Если ты будешь ездить по адресам шелтеров, ты так просто спалишь вероятное местоположение Алии." with dissolve

    show milana_table table1 as Milana with dissolve

    me "Да, было бы неловко." with dissolve

    me "Но что же делать? Мне нужно связаться с ней и поговорить." with dissolve

    me "Я даже не попрощался с нею толком." with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Я не знаю, что и посоветовать." with dissolve

    milana "У Алии очень сильный характер горянки." with dissolve

    milana "Ей палец в рот не клади, она кого хочешь уделает." with dissolve

    milana "Не ты решаешь когда с ней поговорить. Она сама решит, когда захочет с тобой связаться." with dissolve

    show milana_table table1 as Milana with dissolve
    
    me "Это же несправедливо! Я столько для нее сделал." with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Ее жизнь тебе не принадлежит." with dissolve

    milana "То что ты ей помог, не дает тебе никаких прав принимать решения за нее." with dissolve

    milana "Она может делать что хочет." with dissolve

    show milana_table table1 as Milana with dissolve

    "Это звучит жестоко, но справедливо." with dissolve

    "Действительно, она мне ничего не обещала." with dissolve

    show Yarik_notable neutral1 as Yarik with dissolve

    yarik "Позвольте мне вмешаться." with dissolve

    yarik "Мы не знаем где сейчас Алия, и как с ней связаться." with dissolve

    yarik "Но мы все-таки знаем где она будет в будущем." with dissolve

    yarik "Семён, ты же ездил с ней в МФЦ Лефортовского района, делать паспорт." with dissolve

    yarik "Вам сказали, когда можно будет забирать готовый паспорт?" with dissolve

    show Yarik_notable neutral2 as Yarik with dissolve

    me "Да... нам сказали приходить 20 июля с 10 до 12." with dissolve

    show Yarik_notable neutral1 as Yarik with dissolve

    yarik "Ставлю свою машину, что она приедет туда в этот день и в это время." with dissolve

    show Yarik_notable neutral2 as Yarik with dissolve

    show milana_table table2 as Milana with dissolve

    milana "А я ставлю свой мотик на то, что дагестанцы тоже будут ждать ее там." with dissolve

    show milana_table table1 as Milana with dissolve

    "Мне стало немного не по себе." with dissolve

    "Алия может снова попасть в ловушку!" with dissolve

    me "Ох черт, мы должны что-то сделать!" with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Семён, проверь пожалуйста, находится ли Алия в розыске." with dissolve

    milana "Я вчера проверяла, там было пусто." with dissolve

    milana "Но может сегодня что-то поменялось." with dissolve

    show milana_table table1 as Milana with dissolve

    show cg_screen_phone_wanted1 as cg_screen_phone zorder 10 with dissolve:
        xalign 1.0

    "Я достал телефон и открыл сайт МВД Розыск." with dissolve

    show cg_screen_phone_wanted2 as cg_screen_phone zorder 10 with dissolve:
        xalign 1.0

    "Затем я ввел данные Алии..." with dissolve

    show cg_screen_phone_wanted3 as cg_screen_phone zorder 10 with dissolve:
        xalign 1.0

    "По запросу было написано \"Разыскивается по статье УК\"." with dissolve

    me "Плохие новости! Здесь написано, что ее разыскивают по статье уголовного кодекса." with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Черт, это очень плохо." with dissolve

    hide cg_screen_phone with dissolve

    milana "Это значит, что ее родственники действительно написали на нее заявление в полицию." with dissolve

    milana "И ее ищут как преступницу." with dissolve

    milana "Все как и сказал адвокат Александр." with dissolve

    milana "Когда полицейские в Москве поймают Алию, они задержат ее." with dissolve

    milana "И будут держать до прибытия коллег из Дагестана." with dissolve

    milana "Дагестанские менты заберут ее и отвезут в Дагестан." with dissolve

    milana "Дальше с ней может случиться все что угодно." with dissolve

    show milana_table table1 as Milana with dissolve

    me "Это ужасно!" with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Наш адвокат теперь должен сделать запрос в отдел полиции в Дагестане." with dissolve
    
    milana "Узнаем хотя бы, в чем ее обвиняют." with dissolve

    milana "Ярик, поехали к адвокату, и попробуем с ним это обсудить." with dissolve

    milana "Семён, оставайся здесь. Не возвращайся в квартиру, это опасно." with dissolve

    show milana_table table1 as Milana with dissolve

    show Yarik_notable neutral1 as Yarik with dissolve

    yarik "Да, оставайся здесь. Мы вернемся и попробуем придумать, где тебе спрятаться." with dissolve

    show Yarik_notable neutral2 as Yarik with dissolve

    hide Milana with dissolve

    hide Yarik with dissolve

    "Милана и Ярик встали из-за стола и ушли." with dissolve

    "Мысли крутились у меня в голове." with dissolve

    stop music fadeout 1.0

    scene black with dissolve

    "Неужели это конец?" with dissolve

    "Неужели Алию поймают, и я не успею ей помочь?" with dissolve

    "Нам же так везло почти все время, неужели сейчас удача отвернулась от нас..." with dissolve

    "Из транса меня вывел телефонный звонок." with dissolve

    scene kliment_cafe1 with dissolve

    show cg_screen_phone_call_mega1 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я достал телефон." with dissolve

    "На экране было написано Мега Химки Справочная." with dissolve

    show cg_screen_phone_call_mega2 as cg_screen_phone with dissolve:
        xalign 1.0

    me "Да, слушаю." with dissolve

    play music "music/Runaway_11 (Pre_Loop).ogg" fadein 1.5

    queue music "music/Runaway_11 (Loop).ogg"


    aliya "Это я." with dissolve

    me "Алия? Ты где?" with dissolve

    aliya "У меня мало времени." with dissolve

    aliya "Приезжай в Мега Химки прямо сейчас." with dissolve

    aliya "Выключи телефон, за тобой могут следить." with dissolve

    aliya "Я буду ждать тебя." with dissolve

    show cg_screen_phone_call_arstan4 as cg_screen_phone with dissolve

    "Звонок прервался." with dissolve

    hide cg_screen_phone with dissolve

    "У меня внутри все перевернулось." with dissolve
    
    "Как будто у меня появился второй шанс." with dissolve
    
    "Нет, какой второй шанс? Третий уже." with dissolve

    show cg_messenger_cover_above_kliment_cafe as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0 

    $ switchChatToEscapeRoom()

    $ drawCurrentMessageStack(True)

    "Я достал телефон и открыл чат побега." with dissolve


    $ phoneSayMe(__("Алия вышла на связь"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Мне нужно добраться до Мега Химки прямо сейчас"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Отличные новости!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Семён, к сожалению мы сейчас не можем тебя подбросить"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Нас с Яриком стопанули дпс"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Ого! На вас тоже вышла полиция?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Навряд ли"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Документы проверяют"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("И как мне теперь добраться до Мега? Заказать такси?"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Да, но не заказывай со своего телефона"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Давай я лучше тебе закажу машину со своего аккаунта"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Давай"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Минуточку"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Выходи к метро, тебя будет ждать машина"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Серая камри, номер 755"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Отлично, спасибо!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Выключи телефон и вытащи сим-карту!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayCoachWithTitle(__("Чтобы менты не смогли вслед за тобой найти Алию!"))
    coach "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Хорошо!"))
    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Я отключаюсь"))
    me "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я выключил телефон и вытащил сим-карту." with dissolve

    "Мне стало немного беспокойно." with dissolve

    "Сначала менты пришли к Роме, а теперь вот остановили Ярика." with dissolve

    "Алию объявили в федеральный розыск по уголовной статье." with dissolve

    "Нужно срочно найти ее и спрятаться." with dissolve

    scene black with dissolve

    stop music fadeout 1.0

    "Время не ждет! Надо срочно ехать к Алие!" with dissolve


label branch1_day6_taxi_ride:

    scene taxi_moscow with dissolve

    play music_crossfade "ambience/237374__squareal__car-driving-interior.ogg" fadein 1.0 fadeout 1.0

    "Я ехал в такси и думал о ситуации." with dissolve

    "Если Алия отмечена как разыскиваемая по статье УК." with dissolve

    "Это значит что на нее заведено уголовное дело." with dissolve

    "Это значит, что она не сможет найти ни паспорт, ни загранпаспорт." with dissolve

    "И это также значит, что ее будет искать полиция." with dissolve

    "Учитывая, что ее отец начальник где-то в МВД, так просто она не отделается." with dissolve

    "В России ей теперь небезопасно." with dissolve

    "Но и зарубеж теперь не выехать." with dissolve

    "Но должен же быть способ." with dissolve

    "Должен быть!" with dissolve

    "Меня отвлекло радио." with dissolve

    radio "К другим новостям: аналитики предсказывают миграционный кризис в Евросоюзе." with dissolve

    radio "Многочисленные мигранты из Сирии и Сомали штурмуют границы Европы." with dissolve

    radio "Перейдя границу, они специально рвут паспорта и подают на убежище." with dissolve

    play music "music/synthwave_final_radio_room.ogg" fadein 1.0

    queue music "music/synthwave_final_radio_room.ogg"

    "Таксист переключил на другую радиостанцию." with dissolve

    taxiDriver "Давно их не было так много, иншалла все получится у них." with dissolve

    me "Что?" with dissolve

    taxiDriver "У этих ребят дома разбомблены войной, их семьи голодают." with dissolve

    taxiDriver "Единственный шанс - добраться до Европы и осесть там." with dissolve

    "Я задумался." with dissolve

    me "А как они добираются в Европу?" with dissolve

    taxiDriver "По разному. Пешком через Турцию, или на лодках из Африки." with dissolve

    me "А как они переходят через границу? Там же охрана!" with dissolve

    taxiDriver "Там граница большая, везде охрану не поставишь." with dissolve

    taxiDriver "Некоторых ловят конечно." with dissolve

    taxiDriver "Но большинство находят лазейки." with dissolve

    me "И что они потом делают в Европе? У них же ни визы, ни разрешения на работу." with dissolve

    taxiDriver "Они сдаются в полицию и просят убежище, как беженцы." with dissolve

    taxiDriver "Обратно их не депортируешь, потому что там откуда они родом, идет война." with dissolve

    taxiDriver "Вот они и живут в лагере для беженцев." with dissolve

    taxiDriver "Со временем они получают разрешение на работу, а потом и гражданство." with dissolve

    "Интересные мысли закрались у меня в голове." with dissolve

    "Обычные сомалийцы и сирийцы находят способ добраться до Европы и получить лучшую жизнь." with dissolve

    "В то время как Алия обречена быть запертой здесь, в России." with dissolve

    "Может, стоит чему-то поучиться у сомалийцев?" with dissolve

    "Россия граничит с Норвегией, Финляндией, Эстонией и Латвией." with dissolve

    me "Где лучше подавать на беженство? Норвегия, Финляндия, Эстония или Латвия?" with dissolve

    taxiDriver "Эстония и Латвия хуже всех выдают убежища, и оттуда часто депортируют." with dissolve

    taxiDriver "Финляндия или Норвегия лучше." with dissolve

    taxiDriver "Германия лучше всего! Они столько сирийцев приняли у себя." with dissolve

    me "Понятно." with dissolve

    taxiDriver "А зачем ты интересуешься?" with dissolve

    me "Так, просто. " with dissolve

    taxiDriver "У меня если что, двоюродный брат так в Америку уехал." with dissolve

    taxiDriver "Добрался до Мексики, и потом попросил политическое убежище." with dissolve

    taxiDriver "Сейчас он в Чикаго, возит грузы на фурах." with dissolve

    me "Рад за него." with dissolve

    scene black with dissolve

    stop music_crossfade fadeout 2.0

    "Мы подъехали к Меге." with dissolve

    "Я расчитался с таксистом и побежал в Мегу." with dissolve

    jump branch1_day6_mega_interior


label branch1_day6_mega_interior:

    play music "music/Runaway_11 (Pre_Loop).ogg" fadein 1.5

    queue music "music/Runaway_11 (Loop).ogg"


    scene mega_part1

    show black_screen zorder 10:
        alpha 1.0
        linear 1.0 alpha 0.0

    show mega_people1:
        xalign 0.5
        yalign 0.5
        alpha 1.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0

    show mega_people2:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0

    show mega_people3:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0

    show mega_people4:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0

    $ renpy.pause(8.0)

    hide mega_people1
    hide mega_people2
    hide mega_people3
    hide mega_people4

    "Вокруг ходили люди, а я старался найти глазами Алию." with dissolve

    show black zorder 3 with dissolve

    "Кто-то закрыл мои глаза руками." with dissolve

    aliya "Угадай кто!"  with dissolve

    me "Алия!" with dissolve

    show Aliya straight_hoodie_happy1_2 at any_center_pos

    hide black with dissolve

    aliya "Дааа, это яяяяя!"  with dissolve

    me "Как ты здесь оказалась?" with dissolve

    show Aliya straight_hoodie_sad1_2 at any_center_pos

    aliya "Прости меня пожалуйста, за то что я сбежала."  with dissolve

    aliya "Я очень сильно испугалась тех дагестанцев."  with dissolve

    aliya "А в метро я спускаться боялась, потому что там были менты."  with dissolve

    aliya "Я проверила через сайт МВД. Я в федеральном розыске."  with dissolve

    show Aliya straight_hoodie_worried1_2 at any_center_pos

    aliya "Я выключила телефон, и просто поехала на маршрутке куда глаза глядят."  with dissolve

    aliya "Потом я поехала искать шелтер, мне Милана дала листовки."  with dissolve

    aliya "Потом я вспомнила как Костя рассказывал про свой Дом Для Всех в Ленинградской области."  with dissolve

    aliya "И я решила поехать туда и спрятаться там."  with dissolve

    show Aliya straight_hoodie_sad1_2 at any_center_pos

    aliya "Но потом я вспомнила про тебя."  with dissolve

    show Aliya straight_hoodie_sad2 at any_center_pos

    "От этих слов я почувствовал тепло в груди." with dissolve

    show Aliya straight_hoodie_worried1_2 at any_center_pos

    aliya "Скажу честно, я немного начала скучать."  with dissolve

    aliya "У меня не было телефона, чтобы тебе позвонить."  with dissolve

    aliya "Но я помнила твой номер телефона, и поэтому решила просто..."  with dissolve

    aliya "Подойти к стойке информации и позвонить оттуда."  with dissolve
    
    aliya "Они мне разрешили! Они наверное подумали что я потерялась или типа того."  with dissolve

    show Aliya straight_hoodie_worried1 at any_center_pos

    me "И я рад что я нашел тебя." with dissolve

    show Aliya straight_hoodie_sad3_2 at any_center_pos

    "Алия улыбнулась." with dissolve

    show Aliya straight_hoodie_sad1_2 at any_center_pos

    aliya "И я тоже рада, что я нашла тебя снова."  with dissolve

    show Aliya straight_hoodie_sad3_2 at any_center_pos

    "Мы посмотрели друг на друга внимательно." with dissolve

    show Aliya straight_hoodie_sad1_2 at any_center_pos

    aliya "Я в жизни не ожидала что моя судьба повернется вот так."  with dissolve

    aliya "Я познакомилась с тобой в интернете, наша встреча это чистая случайность."  with dissolve

    aliya "Но ты помог мне даже когда все отвернулись от меня."  with dissolve

    aliya "Рискуя своей жизнью ты вытащил меня из этого ада."  with dissolve

    show Aliya straight_hoodie_sad3_2 at any_center_pos

    me "Я никогда не брошу тебя и не оставлю тебя." with dissolve

    me "И тебя и меня ищут менты, но это меня не остановит." with dissolve

    me "Даже если весь мир будет против нас, я буду защищать тебя."  with dissolve

    "Алия улыбнулась снова." with dissolve

    aliya "Давай никогда в жизни больше не расставаться."  with dissolve

    me "Давай." with dissolve

    show black zorder 3 with dissolve

    "Я наклонился к ней." with dissolve

    scene scene_final1 with dissolve

    "Алия была очень близко." with dissolve

    "Я чувствовал что она совершенно не боялась меня." with dissolve

    "Я знал, что я сейчас должен сделать." with dissolve

    "И Алия тоже знала." with dissolve

    scene scene_final2 with dissolve

    "Наши губы соприкоснулись." with dissolve

    "Губы Алии были мягкими и податливыми." with dissolve

    "Слова нам были больше не нужны." with dissolve

    "Все границы между нами исчезли, все барьеры сняты." with dissolve

    "И весь мир вокруг нас как будто исчез." with dissolve

    "Остались только мы вдвоем." with dissolve

    "А время словно бы остановилось..." with dissolve

    scene black with dissolve

    "Я рад что наша история пришла к этому моменту." with dissolve

    "Но я понимаю, что это еще не финал нашего путешествия." with dissolve

    scene mega_part1 with dissolve

    show Aliya straight_hoodie_sad3_2 at any_center_pos with dissolve

    "Алия стояла прямо передо мной, смотря мне в глаза, словно ожидая моих дальнейших действий." with dissolve

    me "У тебя нет телефона." with dissolve

    aliya "Да."  with dissolve

    me "У меня есть телефон, но включать его нельзя." with dissolve

    aliya "Верно."  with dissolve

    me "Мой паспорт остался в съемной квартире." with dissolve

    me "Твой паспорт еще не готов." with dissolve

    aliya "Да."  with dissolve

    me "По сути все что у нас есть - это немного наличных денег." with dissolve

    aliya "У меня есть несколько сотенных купюр."  with dissolve

    me "У меня чуть побольше." with dissolve

    aliya "И как мы уедем в Петебург?"  with dissolve

    aliya "Я знаю что отсюда ходят автобусы, но я не знаю как их найти."  with dissolve

    me "Костя говорил, что возле меги часто паркуются маршруточники." with dissolve

    me "Он сказал, нужно ждать где-то возле главного входа." with dissolve

    aliya "Тогда пойдем туда?"  with dissolve
    
    me "Пойдем!" with dissolve

    scene black with dissolve

    jump branch1_day6_mega_exterior


label branch1_day6_mega_exterior:

    scene mega_ver1 with dissolve

    
    play music "music/moscow_guitar.ogg"

    queue music "music/moscow_guitar.ogg"


    show Aliya half_turn_hand_down_hoodie_happy1_1 zorder 2 at any_right_pos with dissolve

    "И вот мы стоим снаружи." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 zorder 2 at any_right_pos with dissolve

    aliya "Когда мы приедем в Петербург, что мы будем делать дальше?"  with dissolve

    aliya "Мы будем искать тот самый Дом Для Всех?"  with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 zorder 2 at any_right_pos with dissolve

    me "Сначала да." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 zorder 2 at any_right_pos with dissolve

    aliya "А потом?"  with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 zorder 2 at any_right_pos with dissolve

    me "У меня есть план." with dissolve

    me "В России тебе не дадут покоя ни отец, ни менты." with dissolve

    me "Тебе нужно уехать зарубеж." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 zorder 2 at any_right_pos with dissolve

    aliya "Но как мы выедем, если у меня нет паспорта?"  with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 zorder 2 at any_right_pos with dissolve

    me "Я уже все продумал." with dissolve

    me "Доверься мне." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 zorder 2 at any_right_pos with dissolve

    aliya "Хорошо."  with dissolve

    aliya "Спасибо."  with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 zorder 2 at any_right_pos with dissolve

    show mega_ver1_driver as mega_ver1_bus zorder 1 with dissolve

    show Aliya_back back2 as Aliya zorder 3 with dissolve:
        xzoom -1.0

    "В этот момент на парковку приехал автобус." with dissolve

    show mega_ver1_bus_door as mega_ver1_bus zorder 1 with dissolve

    show mega_driver1 zorder 2 with dissolve

    show mega_ver1_bus as mega_ver1_bus zorder 1 with dissolve

    "Водитель вышел наружу и открыл дверь, ожидая пассажиров." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 zorder 3 at any_right_pos with dissolve

    aliya "Ты заплатишь водителю?"  with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 zorder 3 at any_right_pos with dissolve

    me "Конечно." with dissolve

    me "Пойдем внутрь..." with dissolve

    scene black with dissolve

    stop music fadeout 3.0

    jump branch1_day6_bus_exterior




label branch1_day6_bus_exterior:

    scene merc_int1 with dissolve

    show AliyaSitSide turned_hoodie_worried2 as aliya with dissolve

    "Мы сидим с Алией в автобусе." with dissolve

    "Наверное, менты сейчас обыскивают квартиру Кости." with dissolve

    "Мне грозит уголовное дело." with dissolve

    "Но меня это нисколько не волнует." with dissolve

    me "Хочешь снова послушать музыку с моего телефона?" with dissolve

    show AliyaSitSide turned_hoodie_happy1 as aliya with dissolve

    "Алия улыбнулась." with dissolve

    show AliyaSitSide turned_hoodie_happy2 as aliya with dissolve

    aliya "Давай!"  with dissolve

    show AliyaSitSide turned_hoodie_happy1 as aliya with dissolve

    play music "music/ETM_Night_Run (MIX) - 02.ogg"

    queue music "music/ETM_Night_Run (MIX) - 02.ogg"

    scene black with dissolve

    "Я протянул ей наушник, и включил музыку." with dissolve

    "Так заканчиваются наши приключения в Москве." with dissolve

    "Но впереди нас ждут и другие приключения!" with dissolve

    jump credits



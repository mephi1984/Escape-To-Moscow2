
label branch1_day4_accessible_sky_interior_room:

    scene black with dissolve

    play sound "sound/403449__anez__alarm_clo.ogg"

    "Я проснулся от звонка будильника." with dissolve

    show hotelroom3_2a as hotelroom with dissolve

    "Я открыл глаза и вспомнил где я." with dissolve

    show hotelroom3_2 as hotelroom2:
        alpha 0.0
        linear 1.0 alpha 1.0

    stop sound

    show day4_time0641 as cg_screen_phone:
        xalign 1.0
        alpha 0.0
        linear 1.0 alpha 1.0

    "Я посмотрел телефон." with dissolve

    "Было еще очень рано, но все-таки мне уже не хотелось спать." with dissolve

    show hotelroom3_2 as hotelroom2:
        alpha 1.0
        linear 1.0 alpha 0.0

    show day4_time0641 as cg_screen_phone:
        xalign 1.0
        alpha 1.0
        linear 1.0 alpha 0.0


    "Поэтому я решил выйти прогуляться." with dissolve

    scene black with dissolve

    "Я вышел на улицу..." with dissolve

    jump branch1_day4_accessible_sky_exterior_parking


label branch1_day4_accessible_sky_exterior_parking:

    scene accessible_sky_ext3n1 with dissolve 

    play music "music/guitar night fadein.ogg"

    queue music "music/guitar night.ogg"


    "На улице была ночь, было очень свежо." with dissolve

    "Все было на своих местах, как и вчера - самолет, столики, скамейка." with dissolve

    "Не было лишь людей." with dissolve

    "И от этого, было странное ощущение нереальности происходящего." with dissolve

    "Лишь в траве скрипели кузнечики, нарушая тишину ночи." with dissolve

    "Я мог бы сейчас быть у себя дома, в своей постели." with dissolve

    "А сейчас нахожусь за сотни километров, где-то в чистом поле." with dissolve

    "Точнее, в поле, в котором там и сям припаркованы легкомоторные самолеты." with dissolve

    "Я вообще не ожидал, что когда-либо окажусь в подобном месте." with dissolve

    "Я мог бы проводить ночи за ноутбуком, работая над заказами." with dissolve

    "Но вот жизнь позвала меня на новые приключения." with dissolve

    "И в результате я провожу ночь где-то на юге России, рядом с самолетами." with dissolve

    "В какие еще места меня закинет судьба, интересно?" with dissolve

    "Где суждено оказаться мне, и где суждено оказаться Алие?" with dissolve

    "О, и вот, словно подслушав мои мысли, Алия тоже вышла на улицу." with dissolve

    show Aliya straight_hoodie_happy1_2 at any_center_pos with dissolve

    "Алия увидела меня, улыбнулась и подошла поближе." with dissolve

    show Aliya straight_hoodie_neutral2 at any_center_pos with dissolve

    aliya "Я проснулась, и теперь не могу уснуть." with dissolve

    show Aliya straight_hoodie_neutral1 at any_center_pos with dissolve

    me "Ну и ладно. Все равно скоро уже утро." with dissolve

    "Наступила неловкая пауза." with dissolve

    show Aliya straight_hoodie_worried1_2 at any_center_pos with dissolve

    aliya "Здесь так тихо и спокойно." with dissolve

    aliya "До вчерашнего дня я постоянно нервничала." with dissolve

    aliya "Мне приходилось украдкой брать телефон у сестры, я постоянно боялась спалиться." with dissolve

    aliya "Я не знала что мне делать дальше, я даже не знала, приедешь ли ты." with dissolve

    aliya "И когда мы ехали на джипе от моего дома, мне было очень страшно." with dissolve

    show Aliya straight_hoodie_sad2 at any_center_pos with dissolve

    me "Да, я заметил." with dissolve

    show Aliya straight_hoodie_sad1 at any_center_pos with dissolve

    aliya "Но в тот момент, когда мы сели на самолет и взлетели, все поменялось." with dissolve

    aliya "Я словно почувствовала свою неуязвимость." with dissolve

    aliya "Как будто никто больше не может причинить мне вреда." with dissolve

    aliya "И как будто я стала сама по себе." with dissolve

    show Aliya straight_hoodie_happy1 at any_center_pos with dissolve

    aliya "И это было так здорово!" with dissolve

    show Aliya straight_hoodie_happy2 at any_center_pos with dissolve

    "Алия улыбнулась, вспоминая день нашего первого знакомства." with dissolve

    show Aliya straight_hoodie_worried2 at any_center_pos with dissolve

    aliya "Знаешь, я вроде бы не очень боюсь своего отца." with dissolve

    aliya "Но все равно, когда его вижу, у меня возникает какое-то оцепенение." with dissolve

    aliya "Я как будто хочу убежать, но не могу." with dissolve

    aliya "Да и не только отца." with dissolve

    aliya "С Имраном тоже такое было." with dissolve

    show Aliya straight_hoodie_worried1_2 at any_center_pos with dissolve

    aliya "Вообще мне кажется, если любой дагестанец меня окрикнет, я не смогу ничего сделать." with dissolve

    aliya "Это что-то такое, глубоко психологическое." with dissolve

    show Aliya straight_hoodie_worried1 at any_center_pos with dissolve

    me "Да, понимаю." with dissolve

    "Это многое объясняет." with dissolve

    me "Я постараюсь сделать так, чтобы ни один дагестанец тебя не нашел." with dissolve

    show Aliya straight_hoodie_happy2 at any_center_pos with dissolve

    aliya "Спасибо!" with dissolve

    show Aliya straight_hoodie_happy1 at any_center_pos with dissolve

    me "Но ты же все-таки пересилила себя, и сбежала из дома." with dissolve

    show Aliya straight_hoodie_worried2 at any_center_pos with dissolve

    aliya "Да, но мне это стоило огромных усилий!" with dissolve

    show Aliya straight_hoodie_worried2_2 at any_center_pos with dissolve

    me "Дальше будет легче." with dissolve

    me "Чем дольше ты будешь вдали от родителей, тем сильнее в тебе будет эта \"самость\"." with dissolve

    show Aliya straight_hoodie_happy1 at any_center_pos with dissolve

    "Алия улыбнулась." with dissolve

    stop music fadeout 3.0

    show Aliya straight_hoodie_happy1 at any_center_pos with dissolve

    aliya "Надеюсь, что так и будет." with dissolve

    
    show Aliya straight_hoodie_happy1_2 at any_center_pos with dissolve

    play sound "sound/720379__fer_lobo__vehcar_car-by-fl-carby-9_fernando-lobo_fl.ogg"

    "В тишине можно было слышать, как где-то вдалеке ехал автомобиль." with dissolve

    "Шум автомобиля был где-то рядом." with dissolve

    show Aliya straight_hoodie_neutral1 at any_center_pos with dissolve

    "Алия насторожилась." with dissolve

    show Aliya straight_hoodie_neutral2 at any_center_pos with dissolve

    aliya "Что это?" with dissolve

    show Aliya straight_hoodie_neutral1 at any_center_pos with dissolve

    show day4_time0703 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я достал телефон, чтобы проверить время." with dissolve

    me "Судя по часам, как раз сейчас к нам приехал Ярик." with dissolve

    me "Пойдем на парковку, встречать его?" with dissolve

    show Aliya straight_hoodie_happy1 at any_center_pos with dissolve

    aliya "Хорошо!" with dissolve

    show Aliya straight_hoodie_happy1_2 at any_center_pos with dissolve

    hide cg_screen_phone

    "Я убрал телефон и мы пошли на парковку." with dissolve

    scene parking3_4 with dissolve

    show parking3_4 as parking3 with dissolve

    show Aliya_back back2 as Aliya at any_left_pos with dissolve

    "Здесь все было так же, как и вчера вечером." with dissolve

    show parking_in as parking3 with dissolve

    play music "ambience/235507__ceberation__car-engine.ogg" fadein 3.0 fadeout 3.0

    "Едва мы подошли, как на парковку заехал знакомый автомобиль, и встал прямо рядом с нами." with dissolve

    show parking_out as parking3 with dissolve

    "Дверь автомобиля открылась, и к нам вышел Ярик." with dissolve

    show parking3_5 as parking3 with dissolve

    show Yarik smile_speak at any_right_pos with dissolve

    yarik "Здорово путешественники!" with dissolve

    show Yarik smile at any_right_pos with dissolve

    me "Ярик это Алия, Алия это Ярик." with dissolve

    show Yarik smile_speak at any_right_pos with dissolve

    yarik "Приятно познакомиться!" with dissolve

    show Yarik smile at any_right_pos with dissolve

    aliya "Спасибо, мне тоже очень приятно!" with dissolve

    yarik "Да, кстати..." with dissolve

    hide Yarik with dissolve

    hide Aliya with dissolve

    show Yarik_phone neutral with dissolve:
        xpos -0.35

    "Ярик сунул руку в карман, и достал оттуда два новеньких смартфона на Андроиде." with dissolve

    yarik "Вот вам новые телефоны!" with dissolve

    hide Yarik_phone with dissolve

    show Yarik smile at any_right_pos with dissolve

    show Aliya_phone new_phone as Aliya with dissolve 

    show day4_time0715 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я взял телефон в руки." with dissolve

    show Yarik smile_speak at any_right_pos with dissolve

    yarik "Пинкод - дата рождения наоборот." with dissolve

    yarik "В телефоне - незасвеченная симка на чужое имя." with dissolve

    yarik "И там уже установлены мессенджер и прочие приложения." with dissolve

    yarik "Семён, старый телефон теперь лучше выключи, он тебе в близжайшее время не понадобится." with dissolve

    hide cg_screen_phone with dissolve

    yarik "Алия, я так понимаю, твой телефон дома остался?" with dissolve

    show Yarik smile at any_right_pos with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral2 at any_far_left_pos with dissolve

    aliya "Да, я без телефона." with dissolve

    show Aliya half_turn_hand_down_hoodie_neutral1 at any_far_left_pos with dissolve

    show Yarik smile_speak at any_right_pos with dissolve

    yarik "Теперь у тебя есть телефон! Пользуйся им на здоровье!" with dissolve

    yarik "Предлагаю время не терять, и сразу в путь!" with dissolve

    show Aliya straight_hoodie_happy1 at any_far_left_pos with dissolve

    aliya "Хорошо!" with dissolve

    show Aliya straight_hoodie_happy1_2 at any_far_left_pos with dissolve

    show Yarik smile_speak at any_right_pos with dissolve

    yarik "У меня машина не рассчитана на много пассажиров." with dissolve

    yarik "Но все же сзади есть небольшая скамейка. Я думаю, Алия, ты туда поместишься." with dissolve

    yarik "А ты Семён, садись спереди!" with dissolve

    show Yarik smile at any_right_pos with dissolve

    me "Хорошо." with dissolve

    show Yarik smile_speak at any_right_pos with dissolve

    yarik "От винта!" with dissolve

    scene black with dissolve

    stop music fadeout 3.0

    "Мы сели в машину и поехали." with dissolve

    jump branch1_day4_yarik_car_interior1


label branch1_day4_yarik_car_interior1:


    scene m4_morning with dissolve

    play music "music/synthwave_final_radio_room.ogg" fadein 1.0

    queue music "music/synthwave_final_radio_room.ogg"

    "Достаточно скоро мы вырулили на федеральную трассу М4 Дон и ехали по ней." with dissolve

    "На улице уже светало." with dissolve

    "Я сидел спереди, Алия расположилась на заднем ряду." with dissolve

    "Алия увлеченно изучала свой новый телефон." with dissolve

    aliya "Семён, я написала тебе в мессенджере, добавь меня пожалуйста в свои чаты" with dissolve

    show day4_time0727 as cg_screen_phone with dissolve:
        xalign 1.0
    
    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    "Я достал телефон." with dissolve

    show cg_messenger_title_aliya at cg_messenger_title_pos as cg_messenger_title zorder 20

    hide cg_screen_phone_new_message

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0

    $ switchChatToAliya()

    $ drawCurrentMessageStack(True)

    $ phoneSayAliya(__("Приветик"))
    aliya "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Привет, сейчас добавлю"))
    me "[lastPhoneMsg!t]" with dissolve

    show cg_messenger_cover_above_car as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    $ switchChatToEscapeRoom()

    $ phoneSayRomaWithTitle(__("Я успешно привез Семёна и Алию на условное место!"))

    $ phoneSayYarikWithTitle(__("Меня что-то рубит, я переночую в Ростове"))

    $ phoneSayYarikWithTitle(__("Приеду забирать Алию и Семёна завтра в 7:00"))

    $ phoneSayCoachWithTitle(__("Я передам Николаю, чтобы он предупредил Семёна!"))

    $ phoneSayYarikWithTitle(__("Я уже проснулся и еду за нашими беглецами!"), True)

    $ drawCurrentMessageStack(True)

    "Я открыл чат нашей группы." with dissolve

    "Оказывается, мой новый аккаунт уже сюда добавили." with dissolve

    "И здесь уже есть новые сообщения." with dissolve

    $ phoneSayMe(__("Всем снова привет!"))

    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayMe(__("Представляю всем Алию! Прошу любить и жаловать!"))

    me "[lastPhoneMsg!t]" with dissolve

    $ phoneSayAliyaWithTitle(__("Привеет!"))

    aliya "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Салям снова!"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayRomaWithTitle(__("Я рад что у тебя все хорошо!"))
    roma "[lastPhoneMsg!t]" with dissolve

    $ phoneSayAliyaWithTitle(__("Спасииибо!"))

    aliya "[lastPhoneMsg!t]" with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve
    
    "Я убрал телефон." with dissolve

    aliya "А почему у меня в мессенджере номер такой странный, плюс сорок четыре?" with dissolve

    yarik "А да, это твой виртуальный мобильный номер." with dissolve

    yarik "Видишь ли, если полиция узнает твой номер настоящий телефона в мессенджере, то они могут вычислить твою геолокацию." with dissolve

    yarik "Чтобы этого избежать, мы заказали виртуальный номер, и зарегистрировали тебя в соцсетях на него." with dissolve

    yarik "Плюс сорок четыре это номер Великобритании." with dissolve

    aliya "А что такое виртуальный номер?" with dissolve

    yarik "В-общем есть приложение специальное." with dissolve

    yarik "И в этом приложении можно заказать виртуальные номера разных стран, за определенную плату." with dissolve

    yarik "Если ты закажешь номер, то можно будет на него звонить, присылать СМС." with dissolve

    yarik "Все это делается через приложение." with dissolve

    yarik "Получается, симки у тебя нет, а номер есть." with dissolve

    aliya "Интересно!" with dissolve

    aliya "Блин, я не знала про виртуальные номера." with dissolve

    me "Да, я тоже не знал." with dissolve

    me "Наверное, если бы знал, то может быть Имран нас не поймал бы в первый же день побега." with dissolve

    yarik "Ничего страшного!" with dissolve

    yarik "Как говориться, одна голова хорошо, а две - лучше!" with dissolve

    yarik "Когда мы соберемся все вместе, мы обсудим дальнейший план в мельчайших деталях." with dissolve

    aliya "Кстати, куда мы поедем?" with dissolve

    yarik "Мы нашли вам конспиративную квартиру в Реутове, это Подмосковье." with dissolve

    yarik "Хозяин квартиры - Костя, это друг пилота Николая." with dissolve

    yarik "Костя увлекается гитарой, походами и автостопом." with dissolve

    yarik "Квартира большая, места хватит нам всем." with dissolve

    yarik "А через несколько дней Костя улетает в Непал, так что квартира будет полностью в нашем распоряжении." with dissolve

    aliya "Круто!" with dissolve

    yarik "Костя много стран объездил автостопом. Может он даст какие-нибудь советы по путешествиям." with dissolve

    aliya "Да, это было бы здорово!" with dissolve

    "Наступила тишина." with dissolve

    yarik "Семён, Алия, а вы завтракали сегодня?" with dissolve

    aliya "Нет." with dissolve

    me "Я тоже нет." with dissolve

    yarik "Непорядок!" with dissolve

    yarik "Скоро будет заправка по пути." with dissolve

    yarik "После того как я заправлю машину, можно будет съесть хот-дог или типа того." with dissolve

    yarik "Выпить кофе, опять же." with dissolve

    yarik "Как вы на это смотрите?" with dissolve

    aliya "Я за!" with dissolve

    me "Я тоже! Отличная идея!" with dissolve

    yarik "Скоро будем!" with dissolve

    stop music fadeout 1.0

    scene black with dissolve

    "Мы приехали на заправку." with dissolve

    jump branch1_day4_lukoil


label branch1_day4_lukoil:

    scene lukoil_side with dissolve

    show lukoil_sprite2 as lukoil_sprite with dissolve

    play music "music/Runaway_08 (Pre_Loop).ogg"

    queue music "music/Runaway_08 (Loop).ogg"

    "Алия улыбалась." with dissolve

    aliya "Обычно мне не нравится путешествовать на автомобиле." with dissolve

    aliya "Раньше я ездила на машине только между Дагестаном и Пятигорском." with dissolve

    aliya "За рулем был мой отец, а я сидела сзади и играла в телефоне во что-нибудь." with dissolve

    me "Да, могу себе представить." with dissolve


    messenger "Новое сообщение" with dissolve

    show day4_time1023 as cg_screen_phone with dissolve:
        xalign 1.0

    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    "Я достал телефон." with dissolve

    hide cg_screen_phone_new_message
    
    show cg_messenger_cover_above_lukoil as cg_messenger_cover_above at cg_messenger_cover_above_room_pos zorder 20

    show cg_messenger_title_escape_group at cg_messenger_title_pos as cg_messenger_title zorder 20

    show cg_screen_phone_day_dialog as cg_screen_phone:
        xalign 1.0

    $ switchChatToEscapeRoom()

    $ phoneSayRomaVoice()

    me "Это голосовое сообщение от Ромы, который нас возил в Дагестане." with dissolve

    stop music

    aliya "Включи громкую связь пожалуйста." with dissolve

    play music "music/Runaway_12 (Pre_Loop).ogg"

    queue music "music/Runaway_12 (Loop).ogg"

    roma "Семён привет!" with dissolve

    roma "Сегодня к нам домой приходили менты, опрашивали меня." with dissolve

    roma "Но я им ничего не сказал!" with dissolve

    roma "Они как-то вычислили автомобиль моего отца." with dissolve

    roma "Из того что я понял - менты проследили путь автомобиля от аэропорта до села Алии, а потом потеряли след." with dissolve

    roma "Если они смогут посмотреть запись камеры в аэропорту Махачкалы, то они могут выйти на тебя." with dissolve

    roma "Но я им ничего не сказал!" with dissolve

    roma "Полицейские злились, злились." with dissolve

    roma "В итоге выписали мне повестку на завтра, и ушли." with dissolve

    roma "Буду сейчас искать адвоката себе на завтра." with dissolve

    me "Жесть." with dissolve

    $ clearMessages()

    hide cg_messenger_title

    hide cg_messenger_cover_above

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    aliya "Что-то мне страшновато." with dissolve

    aliya "Что если полицейские выйдут на тебя?" with dissolve

    "По идее я должен был чувствовать страх. Но страха не было." with dissolve

    me "Я не боюсь полицейских." with dissolve

    me "Не знаю почему, но сейчас мне не страшно." with dissolve

    me "Я буду защищать тебя до конца." with dissolve

    show Yarik_gas_station neutral3 at any_center_pos with dissolve

    "К нам подошел Ярик." with dissolve

    show Yarik_gas_station neutral1 at any_center_pos with dissolve

    yarik "Что-то случилось?" with dissolve

    show Yarik_gas_station neutral3 at any_center_pos with dissolve

    me "На Рому вышли менты." with dissolve

    me "Возможно, скоро выйдут и на меня." with dissolve

    show Yarik_gas_station neutral1 at any_center_pos with dissolve

    yarik "Как раз поэтому вы и получили новые телефоны." with dissolve

    yarik "Не заходите в соцсети, не звоните никому из старых знакомых." with dissolve

    yarik "И тогда вас будет невозможно вычислить." with dissolve

    show Yarik_gas_station neutral3 at any_center_pos with dissolve

    aliya "Хорошо." with dissolve

    scene black with dissolve

    stop music fadeout 1.0

    play music_crossfade "ambience/237374__squareal__car-driving-interior.ogg" fadein 1.0 fadeout 1.0

    "И мы сели в автомобиль и поехали дальше." with dissolve

    jump branch1_day4_yarik_car_interior2


label branch1_day4_yarik_car_interior2:

    scene m4_day with dissolve

    "Мы продолжили движение по трассе M4 Дон." with dissolve

    "Радиостанция прервалась на новости." with dissolve

    radio "В Москве три часа дня, в эфире новости." with dissolve

    radio "В связи с эпидемией нового вируса в Китае, власти приняли решение закрыть город Ухань на карантин." with dissolve

    radio "С сегодняшнего дня китайцы не могут ни въехать в Ухань, ни покинуть его." with dissolve

    radio "К другим новостям..." with dissolve

    play music "music/synthwave_final_radio_room.ogg" fadein 1.0

    queue music "music/synthwave_final_radio_room.ogg"

    "Ярик переключил радио на музыку..." with dissolve

    yarik "Алия, а у вас в Дагестане же много национальностей живут, да?" with dissolve

    aliya "Да." with dissolve

    yarik "А как вы друг друга различаете?" with dissolve

    "Алия усмехнулась." with dissolve

    aliya "Обычно спрашиваем!" with dissolve

    yarik "А это как вообще, не считается невежливым?" with dissolve

    aliya "Я не люблю когда меня спрашивают." with dissolve

    aliya "Меня спросят, я отвечу - я аварка, ну и что? Это что-то меняет?" with dissolve

    yarik "А можно ли как-нибудь узнать национальность, не спрашивая?" with dissolve

    yarik "По фамилии, например?" with dissolve

    aliya "По фамилии нет. Особенно если взять популярную фамилию - Гаджиев, Магомедов." with dissolve

    aliya "Если ты знаешь откуда человек родом, то можно догадаться." with dissolve

    aliya "Есть аварские села, лакские, даргинские." with dissolve

    aliya "Если дагестанец из даргинского села, значит скорее всего он даргинец." with dissolve

    aliya "Еще можно по хинкалу догадаться." with dissolve

    yarik "По хинкалу?" with dissolve

    aliya "Хинкал это национальное блюдо Дагестана." with dissolve

    aliya "Каждый народ его готовит по-своему." with dissolve

    aliya "Я увижу фотку хинкала в соцсетях, например, и пойму - это аварский хинкал, или лезгинский например." with dissolve

    aliya "Так я по фотке хинкала узнаю национальность дагестанца, который ведет эту страничку." with dissolve

    yarik "Интересно!" with dissolve

    yarik "А по речи, по языку можете узнать?" with dissolve

    aliya "Ну это сложно." with dissolve

    aliya "У нас языки очень непохожие, поэтому ты можешь просто не понять на каком языке дагестанец говорит." with dissolve

    aliya "Я знаю аварский язык, а также немного понимаю даргинский и лезгинский." with dissolve

    aliya "Но если со мной заговорят на кумыкском, я не пойму даже что это кумыкский язык." with dissolve

    yarik "Да уж, загадка." with dissolve

    yarik "А аварский язык сложный?" with dissolve

    yarik "Скажи что-нибудь по-аварски? А я попробую повторить." with dissolve

    "Алия посмеялась." with dissolve

    aliya "Ну попробуй повторить это!" with dissolve

    "Алия набрала воздуха, и приготовилась говорить." with dissolve

    aliya "Микьазаралда микьнусиЯлда ункъоялда микьо къеркъ къвакъвадила бук1ана кьода гъоркь!" with dissolve

    yarik "Миказаялда, микунысялда кырк кырк..." with dissolve

    yarik "Язык сломать можно!" with dissolve

    yarik "Ладно я проиграл." with dissolve

    aliya "Ахах, то то же!" with dissolve

    aliya "Это скороговорка у нас такая." with dissolve

    aliya "Восемь тысяч восемьсот восемьдесят восемь лягушек квакало под корягой." with dissolve

    yarik "Да, сложно!" with dissolve

    yarik "Я думал ты скажешь что-то типа жи есть." with dissolve

    aliya "Так говорят только плохо воспитанные абушки." with dissolve

    aliya "Не нужно судить о Дагестане по этим парням." with dissolve

    aliya "На самом деле у нас красивый язык, да и сам Дагестан очень красивый!" with dissolve

    yarik "Хорошо!" with dissolve

    yarik "Возможно, мне представится шанс когда-нибудь приехать и посмотреть Дагестан вживую." with dissolve

    aliya "Да, было бы здорово! Я думаю, ты не пожалеешь." with dissolve

    aliya "Эх, ладно." with dissolve

    aliya "Что-то меня после еды клонит в сон." with dissolve

    aliya "Я пожалуй посплю..." with dissolve

    yarik "Ладно. А ты, Семён?" with dissolve

    "Мне тоже немного хотелось поспать." with dissolve

    "Я сегодня проснулся очень рано, и после еды меня немного разморило." with dissolve

    scene black with dissolve

    "Глаза сами собой закрылись и я уснул." with dissolve

    "Я чувствовал сквозь сон как мы ехали." with dissolve

    "По ощущениям, мы ехали долго." with dissolve

    "Я периодически просыпался, но потом засыпал заново." with dissolve

    stop music_crossfade fadeout 1.0

    stop music fadeout 1.0

    "И в конце концов, мне удалось заснуть на достаточно длительное время..." with dissolve

    jump branch1_day4_yarik_car_interior3


label branch1_day4_yarik_car_interior3:

    scene mcd_parking31 with dissolve


    play music "music/ETM_Night_Run (MIX) - 02.ogg"

    queue music "music/ETM_Night_Run (MIX) - 02.ogg"

    "Мы приехали на парковку возле Макдоналдса." with dissolve

    yarik "Добро пожаловать в Москву!" with dissolve

    yarik "На самом деле это не совсем Москва, это Подмосковье." with dissolve

    yarik "А точнее, это город Реутов." with dissolve

    yarik "Скоро сюда приедет Напарник." with dissolve

    scene mcd_parking32 with dissolve

    show Aliya_back back2 as Aliya at any_left_pos with dissolve:
        ypos 1.1

    "Мы вышли из машины." with dissolve

    play music_crossfade "audio/49329__heigh-hoo__hayabusa4_start.ogg"

    queue music_crossfade "audio/49329__heigh-hoo__hayabusa4_loop.ogg"

    "Раздался рев двигателя." with dissolve

    show milana_driving bike1 with dissolve

    "И на парковку возле ресторана заехал байк." with dissolve

    play music_crossfade "audio/49329__heigh-hoo__hayabusa4_end.ogg"

    stop music_crossfade fadeout 1.0

    show milana_driving bike2 with dissolve

    "Это и есть Напарник? Я себе его представлял не таким." with dissolve

    show milana_driving bike3 with dissolve

    "Байкер слез с мотоцикла..." with dissolve

    show milana_driving bike4 with dissolve

    "Затем снял с себя шлем..." with dissolve

    show milana_driving bike5 with dissolve

    "Из-под шлема появились густые волосы." with dissolve

    "Так это не байкер, а байкерша!" with dissolve

    show milana_driving bike6 with dissolve

    show milana_jacket happy1 as Milana at any_left_pos with dissolve

    "Девушка подошла к нам." with dissolve

    show milana_jacket happy2 as Milana at any_left_pos with dissolve

    coach "Привет, Семён! Ну вот мы и познакомились вживую." with dissolve

    show milana_jacket happy1 as Milana at any_left_pos with dissolve

    "У меня аж челюсть упала." with dissolve

    show milana_jacket happy2 as Milana at any_left_pos with dissolve

    milana "Меня зовут Милана, приятно познакомиться." with dissolve

    show milana_jacket happy1 as Milana at any_left_pos with dissolve

    me "Я и понятия не имел, что ты женщина." with dissolve

    show milana_jacket half_turn_happy2 as Milana with dissolve:
        xpos 0.0

    milana "Ничего удивительного, я не люблю рассказывать о себе." with dissolve

    milana "И я не люблю фотографироваться." with dissolve

    show milana_jacket half_turn_happy1 as Milana with dissolve:
        xpos 0.0

    me "Но как так? Ты разбираешься в психологии, водишь мотоцикл, еще и столько всего знаешь про Дагестан!" with dissolve

    show milana_jacket happy2 as Milana at any_left_pos with dissolve

    milana "Ааа, ну да, ты же не знаешь." with dissolve

    milana "Я тоже из Дагестана." with dissolve

    show milana_jacket happy1 as Milana at any_left_pos with dissolve

    aliya "Ты тоже?" with dissolve

    show milana_jacket half_turn_happy2 as Milana with dissolve:
        xpos 0.0

    milana "Да, я лачка." with dissolve

    milana "Ну мы лакцы вообще такие, в Дагестане, самые неформальные, современные что ли." with dissolve

    milana "Ты нигде не встретишь лакца, агрессивного ахишку." with dissolve

    milana "Так что не бойся, я тебя не сдам родокам, и постараюсь помочь тебе чем смогу." with dissolve

    show milana_jacket half_turn_happy1 as Milana with dissolve:
        xpos 0.0

    aliya "Спасибо!" with dissolve

    yarik "Простите, что вмешиваюсь." with dissolve

    yarik "Предлагаю взять бургеры, картошку, колу, и продолжить общение уже за столом!" with dissolve

    show milana_jacket happy2 as Milana at any_left_pos with dissolve

    milana "Отличная идея!" with dissolve
    scene black with dissolve

    "Мы сели за стол, хорошо поели." with dissolve

    "А когда с едой было завершено, мы начали обсуждать дела." with dissolve

    jump branch1_day4_mcd_exterior2

label branch1_day4_mcd_exterior2:

    scene m_table_evening_bkg

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1

    show milana_table table1 as Milana zorder 1

    show Yarik_table neutral2 as Yarik zorder 2

    show mtable_coffee zorder 3

    show black zorder 4

    hide black with dissolve

    "Мы сидели за столиком в Макдоналдсе, снаружи." with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Итак, Алия, думаю, можно переходить к делу." with dissolve

    milana "Так уж получилось, что я хорошо знаю про твою ситуацию." with dissolve

    milana "Потому что я консультировала Семёна и помогала ему советами." with dissolve

    show milana_table table1 as Milana with dissolve

    "Алия покосилась на меня." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve

    aliya "Так вот с кем ты все время переписывался." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    me "Да, прости, я не думал что это было так заметно." with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Я знаю что ты решила вернуться домой." with dissolve

    milana "Потому что такое часто бывает - сложно сразу уйти из дома." with dissolve

    milana "И некоторые из моей родни тоже убегали из дома, а потом мирились с родителями и возвращались." with dissolve

    milana "Но потом Семён сказал мне, что ты ему написала через телефон сестры, что у тебя проблемы." with dissolve

    show milana_table table1 as Milana with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve
    
    aliya "Да. Когда я вернулась домой, меня сразу же повезли в мое родное село." with dissolve

    aliya "Там родители собрали семейный совет, и решали что со мной делать." with dissolve

    aliya "Мне говорили, что я их всех опозорила, говорили что убьют и закопают меня прямо там же." with dissolve

    aliya "Все свои обещания родители сразу же забыли - ну это не в первый раз." with dissolve

    aliya "В итоге, они решили меня все-таки выдать замуж." with dissolve

    aliya "Чтобы я не сбежала, они отобрали у меня паспорт, телефон, и запретили выходить из дома." with dissolve

    aliya "Я поняла, что попала в ловушку." with dissolve

    aliya "Единственная моя надежда была - это Семён. Я помнила его ник в мессенджере." with dissolve

    aliya "Я взяла телефон сестры, пока она мылась. И написала Семёну." with dissolve

    aliya "И вот теперь я здесь." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Жесть, сочуствую и обнимаю." with dissolve

    show milana_table table1 as Milana with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve

    aliya "Спасибо." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Я так понимаю, у тебя нет с собой паспорта?" with dissolve

    show milana_table table1 as Milana with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve

    aliya "Да, я сбежала без ничего, вот как есть. Все документы остались дома." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Ох ты бедняжка!" with dissolve

    milana "Теперь слушай меня внимательно." with dissolve

    milana "Теперь ты с нами, и ты в безопасности. Мы будем вместе, и мы тебя никому не отдадим." with dissolve

    milana "Здесь в Реутове, есть конспиративная квартира, где мы останемся на ночь." with dissolve

    milana "А потом мы с тобой поедем в отдел полиции." with dissolve

    show milana_table table1 as Milana with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve

    aliya "Зачем в отдел полиции?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Я думаю ты уже знаешь, что твой отец начал тебя искать." with dissolve

    milana "Пока вы ехали в Москву, Рома отправил в наш чат голосовое сообщение." with dissolve

    milana "Рома сказал что к нему пришли полицейские." with dissolve

    milana "Это означает, что по заявлению твоего отца, полиция объявила тебя в розыск." with dissolve

    milana "Тебе нужно будет сняться с розыска. Для этого нужно будет прийти в любое отделение полиции и написать заявление." with dissolve

    show milana_table table1 as Milana with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve
    
    aliya "А это не опасно? А если мой отец узнает?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Ну вот представь, придешь ты в отдел МВД города Москвы." with dissolve

    milana "Тебя встретят московские менты, которым абсолютно насрать на твоего папашу." with dissolve

    milana "Напишешь заявление и уйдешь." with dissolve

    milana "Конечно, когда это заявление дойдет до Дагестана, то твой отец узнает об этом." with dissolve

    milana "Но все что он узнает - это то, что ты была там, написала заявление и ушла." with dissolve

    show milana_table table1 as Milana with dissolve
    
    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve

    aliya "Я же в полиции буду оставлять свой адрес, свой телефон?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Напиши ненастоящий адрес, укажи левый телефон." with dissolve

    show milana_table table1 as Milana with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve

    aliya "Но ведь мой отец узнает что я в Москве! Он найдет знакомых в полиции, и меня будут искать тут!" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Да, тебе придется все это время скрываться." with dissolve

    milana "Когда ты будешь восстанавливать паспорт, тебе нужно будет ждать несколько дней." with dissolve

    milana "Все это время тебе нужно будет прятаться где-нибудь и стараться не попадаться на глаза полицейским." with dissolve

    milana "А потом ты заберешь свой паспорт и будешь полностью свободна!" with dissolve

    show milana_table table1 as Milana with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve

    aliya "Когда у меня будет паспорт, что я буду делать дальше?" with dissolve

    aliya "Отец же не успокоится, он будет дальше меня искать!" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Как ты смотришь на то, чтобы уехать из России?" with dissolve
    
    show milana_table table1 as Milana with dissolve

    "Алия задумалась." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve

    aliya "Я хотела бы уехать жить в Корею." with dissolve

    aliya "Но сейчас я просто хочу чувствовать себя в безопасности." with dissolve

    aliya "Если я увижу хоть какого-нибудь кавказца, то меня начнет трясти от страха." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show milana_table table2 as Milana with dissolve

    milana "Когда ты получишь паспорт, у тебя есть два варианта." with dissolve

    milana "Вариант первый - подать документы на загранпаспорт и прятаться от отца, пока ты его не получишь." with dissolve

    milana "Вариант второй - уехать в одну из четырех стран: Белоруссию, Армению, Казахстан, Кыргызстан." with dissolve

    milana "Туда можно въехать по российскому паспорту, и остаться там жить." with dissolve

    milana "Когда ты получишь вид на жительство там, то ты сможешь затем получить загранпаспорт через российское консульство." with dissolve

    milana "Там в другой стране, твои родственники тебя не достанут." with dissolve

    milana "А когда ты получишь загранпаспорт, то ты сможешь уехать куда угодно, в том числе в Южную Корею." with dissolve

    show milana_table table1 as Milana with dissolve
    
    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 1 with dissolve

    aliya "Хорошо, понятно." with dissolve

    aliya "Ладно, сначала я восстановлю паспорт, а потом уже решу." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 1 with dissolve

    show Yarik_table neutral1 as Yarik zorder 2

    yarik "В таком случае, предлагаю проследовать на нашу конспиративную квартиру!" with dissolve

    scene black with dissolve

    "И мы пошли к квартире..." with dissolve

    jump conspiracy_exterior


label conspiracy_exterior:

    scene entrance_night with dissolve

    show Aliya_back back2 as Aliya at any_far_left_pos with dissolve:
        ypos 1.1

    show milana_jacket neutral1 as Milana with dissolve

    show Yarik neutral as Yarik with dissolve

    "Мы подошли к подъезду." with dissolve

    "Отсюда действительно было очень близко до Макдоналдса и до метро." with dissolve

    show milana_jacket neutral2 as Milana with dissolve

    milana "Мы пришли! Запомните этот подъезд, не перепутайте." with dissolve

    milana "Код домофона 777, подходите, набирайте - и дверь откроется." with dissolve

    milana "Если домофон, не работает, иногда можно докричаться в окно." with dissolve

    milana "У Кости всегда окна в доме открыты, поэтому он услышит." with dissolve

    scene black with dissolve

    "Милана открыла дверь, и мы зашли." with dissolve

    jump conspiracy_hall

label conspiracy_hall:

    play music "music/conversation.ogg"

    queue music "music/conversation.ogg"

    scene corridor_night_closed with dissolve

    show kostya neutral as Kostya with dissolve:
        xpos 0.15

    "Дверь нам открыл сам хозяин квартиры." with dissolve

    "Квартира Кости была очень... своеобразной." with dissolve

    "Как впрочем, и Костя." with dissolve

    "Сразу было видно, что в квартире живет любитель туристических походов и восхождений на горы." with dissolve

    show kostya neutral_speak as Kostya with dissolve

    costya "Намасте!" with dissolve

    costya "Добро пожаловать! Мой дом - это ваш дом!" with dissolve

    show kostya neutral as Kostya with dissolve

    show Aliya straight_hoodie_worried2 with dissolve:
        xpos 0.45
        ypos 0.1

    aliya "Здравствуйте!" with dissolve

    show Aliya straight_hoodie_worried2_2 with dissolve:
        xpos 0.45
        ypos 0.1

    show milana_jacket neutral2 as Milana with dissolve:
        xpos -0.7

    milana "Приветствую!" with dissolve

    show milana_jacket neutral1 as Milana with dissolve:
        xpos -0.7

    show Yarik smile_speak as Yarik with dissolve:
        xpos -0.6


    yarik "Костя красавчик как обычно!" with dissolve

    yarik "Извини что снова с пустыми руками!" with dissolve

    show Yarik neutral as Yarik with dissolve:
        xpos -0.6

    show kostya neutral_speak as Kostya with dissolve

    costya "Не надо переживать, на кухне есть чай и печенье!" with dissolve

    costya "И вообще, можете брать все что есть в холодильнике!" with dissolve

    costya "Первая дверь - комната для парней." with dissolve

    costya "Следующая дверь - комната для девушек." with dissolve

    costya "Ванная там. Не забывайте закрывать на защелку." with dissolve

    show kostya neutral as Kostya with dissolve

    show Yarik smile_speak as Yarik with dissolve:
        xpos -0.6

    yarik "А какой тут пароль от вайфая?" with dissolve

    show Yarik smile as Yarik with dissolve:
        xpos -0.6

    show kostya neutral_speak as Kostya with dissolve

    costya "Пароль от вайфая вот тут, на стикере на стене." with dissolve

    costya "И кстати если что, в комнате парней есть компьютер, можете его использовать." with dissolve

    show kostya neutral as Kostya with dissolve

    show Yarik smile_speak as Yarik with dissolve:
        xpos -0.6

    yarik "Оу, отлично!" with dissolve

    yarik "Ладно, ребята, меня что-то после дороги рубит немного." with dissolve

    yarik "Я пойду завалюсь спать. До завтра!" with dissolve

    show Yarik smile as Yarik with dissolve:
        xpos -0.6

    show Aliya straight_hoodie_worried2 with dissolve:
        xpos 0.45
        ypos 0.1

    aliya "До завтра!" with dissolve

    show Aliya straight_hoodie_worried2_2 with dissolve:
        xpos 0.45
        ypos 0.1
    
    hide Yarik with dissolve

    "Ярик ушел в комнату парней, и закрыл за собой дверь." with dissolve

    show kostya neutral_speak as Kostya with dissolve

    costya "Предлагаю пойти на кухню и попить чаю! Алия? Семён?" with dissolve

    show kostya neutral as Kostya with dissolve

    me "Да, с удовольствием!" with dissolve

    show Aliya straight_hoodie_worried2 with dissolve:
        xpos 0.45
        ypos 0.1

    aliya "Конечно!" with dissolve

    show Aliya straight_hoodie_worried2_2 with dissolve:
        xpos 0.45
        ypos 0.1

    show milana_jacket neutral2 as Milana with dissolve:
        xpos -0.7

    milana "Ребята, я тоже скоро присоединюсь, только схожу в уборную!" with dissolve

    jump conspiracy_kitchen


label conspiracy_kitchen:

    scene kitchen_night with dissolve

    show kostya neutral as Kostya with dissolve:
        xpos 0.0

    show Aliya straight_hoodie_worried2_2 with dissolve:
        xpos 0.1
        ypos 0.1

    "Из коридора мы сразу же прошли на кухню." with dissolve

    scene kitchen_table_back_night

    show AliyaSitTableKitchen aliya_sit_kitchen zorder 1

    show kitchen_table_front_night as kitchen_table_front_night zorder 2

    show black zorder 4

    hide black with dissolve

    show kostya kitchen with dissolve

    "Костя налил нам чай и подошел к окну." with dissolve

    show kostya kitchen_speak with dissolve

    costya "Алия, я бы хотел помочь еще чем-то тебе." with dissolve

    costya "Если что, у нас открыты Дома Для Всех." with dissolve

    costya "Один точно есть на Алтае, и еще мой знакомый открывает Дом Для Всех в Ленинградской области." with dissolve

    show kostya kitchen with dissolve

    me "Дом Для Всех?" with dissolve

    show kostya kitchen_speak with dissolve

    costya "Это такой социальный проект." with dissolve

    costya "Кто хочет сделать добро для Вселенной - открывает Дом Для Всех, скажем, на один сезон." with dissolve

    costya "В этом доме путешественник можете бесплатно остановится на любой срок, разделяя дом с другими путешественниками." with dissolve

    costya "Вот там вас точно никакие дагестанцы не достанут!" with dissolve

    show kostya kitchen with dissolve

    aliya "Спасибо, мне очень приятно." with dissolve

    aliya "Но все же, мне не нравится идея жить где-то на Алтае или... где вы сказали?" with dissolve

    show kostya kitchen_speak with dissolve

    costya "Второй Дом находится в Приозерске, это Ленинградская область, на границе с Карелией." with dissolve

    costya "Его открывает мой друг Антон." with dissolve

    costya "Добраться туда легко, сначала нужно поехать на маршрутке в Питер." with dissolve
    
    costya "Возле Меги каждый день собираются маршруточники до Петербурга." with dissolve
    
    costya "Стоит 1500 рублей с человека, вечером уже будете там." with dissolve

    costya "А из Петербурга можно добраться автостопом до Приозерска." with dissolve

    show kostya kitchen with dissolve

    aliya "Не обижайтесь, Костя, но я достаточно пожила в селе." with dissolve

    aliya "Город мне нравится больше." with dissolve

    show kostya kitchen_speak with dissolve

    costya "Да, конечно." with dissolve

    costya "Но кто знает как повернется Вселенная." with dissolve

    costya "В любом случае, я желаю вам удачи на вашем пути!" with dissolve

    costya "Я пойду чистить зубы." with dissolve

    hide kostya with dissolve

    "И Костя ушел из кухни." with dissolve

    show kitchen_table_front_night2 as kitchen_table_front_night zorder 2

    aliya "Я, наверное, обидела Костю." with dissolve

    aliya "Мне кажется, он добрый человек. Может мне извинится перед ним?" with dissolve

    show milana_kitchen milana_kitchen as milana with dissolve

    "На кухню зашла Милана." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "Костя - один из самых понимающих людей, которых я встречала." with dissolve

    milana "Не беспокойся, он прекрасно понимает, что ты не хотела его обидеть." with dissolve

    milana "У Кости есть свойство характера, он объединяет самых разных людей." with dissolve

    milana "Среди его друзей есть разные люди, от вице-президентов до бомжа с Курского вокзала." with dissolve

    milana "Мне даже немного жаль, что он улетает в Непал." with dissolve

    show milana_kitchen milana_kitchen2 as milana with dissolve

    "Милана слегка вздохнула." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "Ладно, достаточно о нем." with dissolve

    milana "Давайте поговорим о планах на завтра." with dissolve

    milana "Я предлагаю вам не откладывать восстановление паспорта в долгий ящик." with dissolve

    milana "Семён, узнай как восстановить паспорт." with dissolve

    show milana_kitchen milana_kitchen2 as milana with dissolve

    me "Что?" with dissolve

    me "Я думал ты знаешь." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "Я знаю, но не в деталях." with dissolve

    milana "Смотри. Есть благотворительная организация Ночлежка, которая помогает бездомным." with dissolve

    milana "У них есть сайт, найдешь потом в поисковике." with dissolve

    milana "На сайте там очень много интересных инструкций на все случаи жизни." with dissolve

    milana "И среди этих инструкций есть инструкция о том как восстановить утерянный паспорт." with dissolve

    milana "Изучи эту инструкцию внимательно." with dissolve

    show milana_kitchen milana_kitchen2 as milana with dissolve

    me "Хорошо, я займусь этим завтра." with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "Чтобы завтра утром вы сразу поехали восстанавливать паспорт!" with dissolve

    show milana_kitchen milana_kitchen2 as milana with dissolve
    
    me "Конечно, все будет сделано идеально!" with dissolve

    show milana_kitchen milana_kitchen2_speak as milana with dissolve

    milana "Ну а теперь, не буду отвлекать." with dissolve

    milana "Нам всем пора ложиться спать." with dissolve

    milana "Алия, пойдем, я покажу тебе комнату." with dissolve

    hide milana with dissolve

    hide AliyaSitTableKitchen with dissolve

    show kitchen_table_front_night3 as kitchen_table_front_night zorder 2

    "Алия встала из-за стола и ушла с Миланой." with dissolve

    "Что же, мне тоже пора идти спать." with dissolve

    scene black with dissolve

    "Я пошел в комнату для парней..." with dissolve

    jump conspiracy_room_boys

label conspiracy_room_boys:

    scene boy_room_ver2 with dissolve

    "Я пришел в комнату и расположился в своем углу." with dissolve

    "Конечно, спальный мешок - не самое удобное место для сна." with dissolve

    "Но мне нравилось находиться в этой квартире." with dissolve

    "Словно какая-то позитивная энергетика тут была..." with dissolve

    "Ярик уже храпел." with dissolve

    "Костя еще чистил зубы, но скоро должен был прийти в комнату." with dissolve

    "Ладно, утро вечера мудренее, пора идти спать." with dissolve

    scene black with dissolve

    "Я залез в спальный мешок и закрыл глаза..." with dissolve
    
    "Сегодня почти весь день был потрачен на путешествие из Ростова-на-Дону в Москву." with dissolve
    
    "Получается, мы с Алией добирались до Москвы почти два дня." with dissolve

    "Конечно, это не так просто, как при первом побеге." with dissolve

    "Но тем не менее, я доволен собой." with dissolve

    "Завтра предстоит долгий день, и мне нужно подготовиться." with dissolve

    stop music fadeout 2.0

    "С этими мыслями я уснул..." with dissolve

    jump branch1_day5_conspiracy_room_boys


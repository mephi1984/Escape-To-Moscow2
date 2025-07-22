label branch1_day3_airplane:

    scene black with dissolve

    play music "ambience/airplane_1ambience_before_landing_loop.ogg" fadein 1.0 fadeout 1.0

    "В ушах звенит гул летящего самолёта." with dissolve

    "И я опять был словно наполовину во сне, наполовину осознавая, что происходит вокруг." with dissolve

    play sound "sound/seatbelt.ogg"

    "Прозвучал звуковой сигнал \"пристегните ремни безопасности\"." with dissolve

    announcement "Уважаемые дамы и господа, наш самолёт приступил к снижению. Мы готовимся к посадке в аэропорту Махачкалы." with dissolve

    announcement "Просим вас пристегнуть ремни, привести спинки кресел в вертикальное положение, закрыть раскладные столики и открыть шторки на иллюминаторах." with dissolve

    show airplane_night at airplane_scene_pos with dissolve:
        ypos 0.525
        zoom 1.05

    "Я открыл глаза." with dissolve

    show airplane_night at airplane_scene_pos:
        ypos 0.525
        zoom 1.05
        easein 4.0 ypos 0.475

    "Я почувствовал как самолёт, снижаясь, задрал нос вверх." with dissolve

    "От этого движения я окончательно проснулся." with dissolve

    show day2_time0841 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я проверил время на телефоне - 8:41." with dissolve

    "Телефон по-прежнему был без сим-карты и в авиарежиме." with dissolve

    hide cg_screen_phone with dissolve

    "Я убрал телефон." with dissolve

    "Сегодня день будет очень долгим." with dissolve

    "У меня есть план, но все равно я волновался." with dissolve

    "Все что угодно могло пойти не по плану." with dissolve

    "Неизвестно, удасться ли мне вообще вытащить Алию из дома." with dissolve

    "А может быть, меня заметят и задержат." with dissolve

    "Ведь ее родители уже знаю как я выгляжу, и они могут устроить мне проблемы." with dissolve
    
    "Но я все равно уверен в себе." with dissolve

    "Я должен спасти Алию, чего бы мне это и ни стоило!" with dissolve

    play music "ambience/airplane_2landed_shortened.ogg"

    queue music "ambience/airplane_3after_landing_loop.ogg"

    show airplane_night:
        ypos 0.475
        zoom 1.05
        linear 2.0 ypos 0.5
        linear 5.0 zoom 1.075

    "Бум! Самолёт коснулся посадочной полосы и дёрнулся." with hpunch

    "Посадка была чуть более жестковатой, чем я ожидал." with dissolve

    "На крыльях поднялись спойлеры и шум торможения наполнил мои уши." with dissolve

    "Самолет снизил скорость и шум тоже заметно снизился." with dissolve

    announcement "Уважаемые дамы и господа, добро пожаловать в международный аэропорт Махачкалы." with dissolve

    announcement "Температура воздуха в Махачкале плюс девятнадцать градусов." with dissolve

    announcement "Местное время восемь часов тридцать минут." with dissolve

    announcement "Для вашей безопасности мы рекомендуем вам оставаться на местах с пристегнутыми ремнями безопасности до выключения светового табло \"пристегните ремни\"." with dissolve

    announcement "От имени авиакомпании благодарим вас за полёт и будем рады новой встрече!" with dissolve

    scene black with dissolve

    stop music fadeout 1.0

    "Мы прилетели." with dissolve

    "Я мысленно приготовился к своей первой встрече с Дагестаном..." with dissolve

    jump branch1_day3_airport_mcx


label branch1_day3_airport_mcx:

    scene airport_mcx_bkg

    show airport_mcx_layer1 as airport_mcx_layer zorder 1

    show airport_mcx_layer_top zorder 2

    show black as fg_black zorder 10

    hide fg_black with dissolve

    play music "music/whilemusic2.ogg" fadein 1.0

    "Свежий воздух ударил мне в лицо, когда я вышел наружу." with dissolve

    "Здесь было довольно тепло, теплее чем я ожидал." with dissolve

    "Возле аэропорта стояли таксисты, приветствующие путешественников." with dissolve

    "Где-то рядом кто-то шумно встречал родственников, прилетевших, судя по всему, домой." with dissolve

    "Рома должен ждать меня где-то здесь." with dissolve

    show cg_screen_phone_day_car_roma as cg_screen_phone with dissolve:
        xalign 1.0

    "Я достал телефон и открыл фотографию автомобиля, которую он мне прислал." with dissolve

    "Да, вот же он, белый внедорожник Ромы!" with dissolve

    hide cg_screen_phone with dissolve

    show airport_mcx_layer2 as airport_mcx_layer zorder 1 with dissolve

    "Я уже собрался подойти к внедорожнику, но тут его дверь открылась." with dissolve

    show airport_mcx_layer1 as airport_mcx_layer zorder 1 with dissolve

    show roma neutral as roma zorder 2 with dissolve:
        xpos 0.3

    "Из машины вышел парень и подошел ко мне." with dissolve

    show roma neutral_speak as roma zorder 2 with dissolve:
        xpos 0.3

    roma "Привет, так это ты Семён?" with dissolve

    show roma neutral as roma zorder 2 with dissolve:
        xpos 0.3

    me "Да, это я." with dissolve

    show roma neutral_speak as roma zorder 2 with dissolve:
        xpos 0.3

    roma "Я Рома, приятно познакомиться." with dissolve

    roma "Добро пожаловать в Дагестан!" with dissolve

    show roma neutral as roma zorder 2 with dissolve:
        xpos 0.3

    "Я чувствую себя очень неловко." with dissolve

    "Из-за того что мой первый визит в Дагестан связан с тем, что мне нужно спасать свою подругу." with dissolve

    me "Хотелось бы прилететь сюда как турист, но увы..." with dissolve

    "Рома усмехнулся." with dissolve

    show roma neutral_speak as roma zorder 2 with dissolve:
        xpos 0.3

    roma "Не переживай ты так!" with dissolve

    roma "В следующий раз приедешь сюда, и уже нормально отдохнешь, горы посмотришь!" with dissolve

    show roma neutral as roma zorder 2 with dissolve:
        xpos 0.3

    me "Надеюсь..." with dissolve

    show day3_time0910 as cg_screen_phone zorder 3 with dissolve:
        xalign 1.0

    "Я достал телефон чтобы проверить время." with dissolve

    me "Уже 9:10, нам пора!" with dissolve

    hide cg_screen_phone with dissolve

    show roma hand_up_speak as roma zorder 2 with dissolve:
        xpos 0.3

    roma "Точно! Садись, поехали!" with dissolve

    hide roma with dissolve

    "Рома подошел к автомобилю и сел за руль." with dissolve

    scene black with dissolve

    "Я проследовал за ним, сев на заднее сиденье, и мы поехали..." with dissolve

    jump branch1_day3_car_way1


label branch1_day3_car_way1:

    scene black

    show cruiser_bkg_loop as cruiser_bkg_loop1:
        xpos 0.0
        linear 36.0 xpos -1.0
        repeat

    show cruiser_bkg_loop as cruiser_bkg_loop2:
        xpos 1.0
        linear 36.0 xpos 0.0
        repeat

    show cruiser_ver3

    show cruiser_ver5

    show roma drive4

    show black as fg_black zorder 10

    hide fg_black with dissolve

    "Мы ехали по горным дорогам." with dissolve

    "В машине играла какая-то дагестанская музыка." with dissolve

    show roma drive2

    roma "Ну как тебе? Не укачивает?" with dissolve

    show roma drive3

    me "Нет, пока вроде норм" with dissolve

    show roma drive4

    show roma drive2

    roma "Конечно, кайфуй братан! Тачка просто высший класс." with dissolve

    roma "Это крузак моего пахана." with dissolve

    show roma drive4

    me "Пахана?" with dissolve

    show roma drive2

    roma "Ну отец мой." with dissolve

    roma "Когда-нибудь я поднимусь, и тоже куплю себе крузак." with dissolve

    roma "Хочу себе, знаешь, трехсотый, черного цвета, взорванный чтоб был." with dissolve

    roma "Его бы потом еще чуть-чуть приопустить, затонировать вкруг и поставить хорошую оптику." with dissolve

    show roma drive4
    
    "Разговор о машинах меня немного приободрил." with dissolve

    me "Тут, я вижу, такие машины в почете." with dissolve

    show roma drive2

    roma "Конечно. Кто может - покупает." with dissolve

    roma "Кто не может - хасанит на приорах." with dissolve

    roma "Или на маршрутках, хе-хе." with dissolve

    show roma drive4

    "Рома пустился в рассуждения о машинах, а я смотрел в окно на горы." with dissolve

    "Величественные горы Кавказа вызывали у меня ощущение нереальности происходящего." with dissolve

    "В который раз ловлю себя на мысли - если бы я не встретил Алию, я бы столько упустил в своей жизни..." with dissolve

    scene black with dissolve

    play music_crossfade "ambience/594541__arnoventer__car-idle-owi.ogg" fadein 1.0 fadeout 1.0

    stop music fadeout 1.0

    "И вот наконец мы заехали в село, и подъехали к нужному дому." with dissolve

    show black as fg_black zorder 10

    show karaurt_bkg1

    show cruiser_ver3 zorder 1

    show cruiser_ver5 as cruiser_doors zorder 0

    show roma drive4 zorder 3

    hide fg_black with dissolve

    show roma drive2 zorder 3 with dissolve

    roma "Семён, мы приехали." with dissolve

    roma "Я пока не буду глушить двигатель." with dissolve

    show roma drive3 zorder 3 with dissolve

    me "Это точно тот адрес?" with dissolve

    show roma drive2 zorder 3 with dissolve

    roma "Ну все как Алия написала - дом с красной крышей, мечеть." with dissolve

    show roma drive1 zorder 3 with dissolve

    roma "Дом кстати основательный. Сразу видно - не бедная семья." with dissolve

    show cruiser_ver4 as cruiser_doors zorder 0

    "Я открыл дверь и стал ждать." with dissolve

    "У меня прямо рука чесалась достать телефон, отключить авиарежим." with dissolve

    "Мне так хотелось посмотреть сообщения, я буквально страдал от информационного вакуума." with dissolve

    "Но если моя симка засветится здесь, это будет серьезное палево." with dissolve

    "Поэтому я просто рассматривал дом, сгорая внутри от нетерпения." with dissolve

    "Ну же, Алия, ну же!" with dissolve

    "Надеюсь с тобой все хорошо." with dissolve

    "Надеюсь ты сумеешь выскользнуть от внимания родителей, и сбежать из дома." with dissolve

    show aliya_escape0 as aliya_escape zorder 2 with dissolve

    play music "music/Runaway_15 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_15 (Loop).ogg"

    stop music_crossfade fadeout 2.0

    show aliya_escape1 as aliya_escape zorder 2 with dissolve

    "И тут я увидел на заборе знакомый силуэт..." with dissolve

    show aliya_escape2 as aliya_escape zorder 2 with dissolve

    show aliya_escape3 as aliya_escape zorder 2 with dissolve

    "Алия ловким движением спрыгнула на землю." with dissolve

    show aliya_escape4 as aliya_escape zorder 2 with dissolve

    "И Алия пулей залетает в машину." with dissolve

    hide aliya_escape with dissolve

    show cruiser_shadow zorder 2

    show AliyaSitSide turned_hoodie_angry4 as aliya zorder 3 with dissolve

    show cruiser_ver5 as cruiser_doors zorder 0 with dissolve

    aliya "Что стоишь поехали!" with dissolve

    show roma drive4 zorder 3 with dissolve

    me "Поехали быстро!" with dissolve

    scene black with dissolve

    "Рома втопил педаль в пол, и машина с ревом помчалась прочь от дома." with dissolve

    scene black

    show cruiser_bkg_loop as cruiser_bkg_loop1:
        xpos 0.0
        linear 36.0 xpos -1.0
        repeat

    show cruiser_bkg_loop as cruiser_bkg_loop2:
        xpos 1.0
        linear 36.0 xpos 0.0
        repeat

    show cruiser_ver3

    show cruiser_ver5

    show cruiser_shadow

    show AliyaSitSide straight_hoodie as aliya

    show roma drive4 zorder 3

    show black as fg_black zorder 10

    hide fg_black with dissolve

    "Мы ехали в обратную сторону, Алия сидела на боковом сиденье и чуть ли не ревела." with dissolve

    show AliyaSitSide turned_hoodie_fright2 as aliya with dissolve

    aliya "Ужас! Какой ужас! Какой позор!" with dissolve

    aliya "Что я сделала! Что я наделала!" with dissolve

    show AliyaSitSide turned_hoodie_fright1 as aliya with dissolve

    aliya "Что со мной теперь будет! Что со мной сделают!" with dissolve

    show AliyaSitSide turned_hoodie_sad1 as aliya with dissolve

    "Я постарался сделать свой голос максимально спокойным." with dissolve

    me "Успокойся! Все самое страшное уже позади!" with dissolve

    me "Ты теперь в безопасности." with dissolve

    me "Я тут, с тобой, и буду тебя защищать." with dissolve

    show AliyaSitSide turned_hoodie_worried4 as aliya with dissolve

    aliya "Мне страшно, мне очень страшно!" with dissolve

    aliya "Нас найдут, нас сейчас догонят!" with dissolve

    show AliyaSitSide turned_hoodie_worried1 as aliya with dissolve

    me "За нами нет погони." with dissolve

    me "Я предпринял все возможные меры безопасности." with dissolve

    "Алия вздохнула несколько раз." with dissolve

    show AliyaSitSide turned_hoodie_worried4 as aliya with dissolve

    aliya "А кто нас везет? Чья эта машина?" with dissolve

    show roma drive2 zorder 3

    roma "Салям алейкум, меня зовут Рома." with dissolve

    show roma drive4 zorder 3

    show AliyaSitSide turned_hoodie_fright2 as aliya with dissolve

    "Алия испуганно вздрогнула, так что мне пришлось вмешаться..." with dissolve

    me "Алия не бойся, Рома - он из наших." with dissolve

    aliya "Каких ваших? Что вы там задумали?" with dissolve

    show AliyaSitSide turned_hoodie_fright2_2 as aliya with dissolve

    me "Ну по-правде говоря, я сейчас не один тебя спасаю." with dissolve

    me "Я рассказал своим друзьям про твою ситуацию." with dissolve

    me "Кое-кто откликнулся, и теперь твоим спасением занимается целая команда." with dissolve

    show AliyaSitSide turned_hoodie_sad2_2 as aliya with dissolve

    "Алия слабо улыбнулась." with dissolve

    aliya "Ой, это так неожиданно..." with dissolve

    aliya "А я-то думаю, откуда у тебя внедорожник." with dissolve

    aliya "Я даже сначала подумала, что ты на самом деле тайный миллиардер под прикрытием, или типа того..." with dissolve

    "Теперь уже я улыбнулся." with dissolve

    me "Ох да, хотел бы я быть миллиардером." with dissolve

    me "Пока что я влез в большой долг по кредитке, чтобы вытащить тебя." with dissolve

    me "Но это все ерунда, для меня главное - что с тобой все в порядке." with dissolve

    show AliyaSitSide straight_hoodie as aliya with dissolve

    "Алия посмотрела в окно." with dissolve

    aliya "А куда мы едем? Я что-то не узнаю эти места." with dissolve

    me "Рома нас довезет до условной точки где-то возле Хунзаха." with dissolve

    me "Там нас должен встретить пилот, а Рома поедет домой." with dissolve

    aliya "Понятно..." with dissolve

    "Алия начала смотреть в окно..." with dissolve

    scene black with dissolve

    "Прошло некоторое время..." with dissolve

    stop music fadeout 3.0

    "Наконец, мы подъехали на поле к разрушенному зданию, и вышли из машины." with dissolve

    jump branch1_day3_khunzakh1

label branch1_day3_khunzakh1:

    play music_crossfade "ambience/396175__jayrope__mountain-meadow-near-almaty.ogg" fadein 1.0 fadeout 1.0


    scene khunzakh1 with dissolve

    show Aliya straight_hoodie_worried2_2 at any_left_pos with dissolve:
        ypos 1.05

    show roma neutral as roma with dissolve:
        xpos 0.5

    me "Нас должны встретить здесь..." with dissolve

    me "Но здесь никого нет!" with dissolve

    show roma neutral_speak as roma with dissolve:
        xpos 0.5

    roma "Мы приехали вот прямо по тем координатам, которые вы скинули." with dissolve

    show roma neutral as roma with dissolve:
        xpos 0.5

    "Я оглянулся." with dissolve

    "Впереди было здание, однако оно было давно заброшено." with dissolve

    show roma hand_up_speak as roma with dissolve:
        xpos 0.5

    roma "Ладно ребята, мне пора ехать. Я оставлю вас тут." with dissolve

    hide roma with dissolve

    "Рома быстро сел в автомобиль и уехал." with dissolve

    "Я остался наедине с Алией." with dissolve

    "И она явно была обеспокоена." with dissolve

    show Aliya straight_hoodie_sad1_2 at any_left_pos with dissolve:
        ypos 1.05

    aliya "Что же делать?" with dissolve

    aliya "Мы же здесь на виду, нас за десять километров увидят!" with dissolve

    show Aliya straight_hoodie_worried1 at any_left_pos with dissolve:
        ypos 1.05

    "Алия по виду, очень волновалась." with dissolve

    show Aliya straight_hoodie_worried2 at any_left_pos with dissolve:
        ypos 1.05

    aliya "Чего ты стоишь? Напиши пилоту, спроси где он?" with dissolve

    show Aliya straight_hoodie_worried2_2 at any_left_pos with dissolve:
        ypos 1.05

    me "Мой телефон сейчас без симки и в авиарежиме." with dissolve

    me "Если я сейчас выйду в интернет, то спалю свое местоположение." with dissolve

    show Aliya straight_hoodie_fright1 at any_left_pos with dissolve:
        ypos 1.05

    aliya "О боже, что же делать?" with dissolve

    aliya "А что если пилот опоздает? А что если он передумал?" with dissolve

    me "Не бойся, он надежный человек." with dissolve

    me "Давай просто посмотрим внимательнее, он уже должен быть где-то рядом." with dissolve

    show Aliya_back back2 as Aliya with dissolve

    "Алия оглянулась несколько раз по сторонам." with dissolve

    "Затем она замерла, словно заметив что-то." with dissolve

    show Aliya_point point2 as Aliya with dissolve

    "Алия прищурилась, а потом внезапно указала пальцем в небо." with dissolve

    show Aliya_point point1 as Aliya with dissolve

    aliya "Смотри! Что это?" with dissolve

    me "Где?" with dissolve

    "Я присмотрелся получше..." with dissolve

    stop music_crossfade fadeout 2.0

    play music "music/Runaway_14 (Pre_Loop).ogg"

    queue music "music/Runaway_14 (Loop).ogg"

    scene khunzakh1

    show movie_plane_landing

    pause 41.0

    jump branch1_day3_khunzakh2


label branch1_day3_khunzakh2:

    scene black

    show khunzakh3 as khunzakh


    show Aliya turn_around_hand_down_hoodie_happy1_1 at any_far_right_pos with dissolve:
        ypos 1.1

    "Перед нами стоял легкомоторный самолет." with dissolve

    "Алия восхищенно смотрела на него." with dissolve

    show Aliya turn_around_hand_down_hoodie_happy1_2 at any_far_right_pos with dissolve:
        ypos 1.1

    aliya "Это было шикарно!" with dissolve

    show Aliya_back back2 as Aliya at any_far_right_pos with dissolve:
        ypos 1.1

    me "Да, я тоже не ожидал." with dissolve

    show khunzakh2 as khunzakh with dissolve

    show pilot neutral as pilot at any_left_pos with dissolve

    show Aliya straight_hoodie_happy1_2 at any_far_right_pos with dissolve:
        ypos 1.1

    "Дверь самолета открылась, и оттуда вышел пилот." with dissolve

    show pilot neutral_speak as pilot at any_left_pos with dissolve

    pilot "Семён и Алия, все верно?" with dissolve

    pilot "Надеюсь вы не из тех, кого укачивает в полете." with dissolve

    pilot "Садитесь!" with dissolve

    show pilot neutral as pilot at any_left_pos with dissolve

    me "Мы полетим на ЭТОМ? Прямо сейчас?" with dissolve

    show pilot neutral_speak as pilot at any_left_pos with dissolve

    pilot "Конечно!" with dissolve

    pilot "Залезайте первыми, постарайтесь не наступать на закрылки." with dissolve

    pilot "Садитесь сзади." with dissolve

    pilot "Поспешите! Раньше сядете - раньше взлетим!" with dissolve

    scene black with dissolve

    "И мы сели в самолет..." with dissolve

    jump branch1_day3_piper_cherokee0



label branch1_day3_piper_cherokee0:

    show plane_ver1_loop2 as plane_bkg_loop1

    show plane_ver1_loop3 as plane_bkg_mountains_loop1

    show plane_ver1

    show plane_shadow

    show black as fg_black zorder 10

    show AliyaSitSide straight_hoodie as aliya with dissolve

    show pilot drive1

    hide fg_black with dissolve

    "Николай взял в руки тяжеленные наушники." with dissolve

    show pilot drive2 with dissolve

    "И ловким движением надел на себя." with dissolve

    show pilot drive5 with dissolve

    pilot "У вас там рядом гарнитура лежит." with dissolve

    pilot "Наденьте, иначе ничего не услышите." with dissolve

    show pilot drive4 with dissolve

    "Прямо на сиденье подо мной лежали наушники, как у Николая." with dissolve

    "Я надел гарнитуру и подвинул микрофон поближе." with dissolve

    show AliyaSitSide headphones_wear1 as aliya with dissolve

    "Алия тоже взяла в руки гарнитуру." with dissolve

    show AliyaSitSide headphones_wear2 as aliya with dissolve

    "И надела на голову." with dissolve

    show pilot drive5 with dissolve

    pilot "{i}Меня слышно?{/i}" with dissolve

    show pilot drive4 with dissolve

    me "{i}Да, слышу отлично.{/i}" with dissolve

    show AliyaSitSide headphones_neutral2 as aliya with dissolve

    aliya "{i}Да, я тоже слышу.{/i}" with dissolve

    show AliyaSitSide headphones_neutral1 as aliya with dissolve

    show pilot drive5 with dissolve

    pilot "{i}Очень хорошо.{/i}" with dissolve

    show pilot drive2 with dissolve

    pilot "{i}Пристегните ремни.{/i}" with dissolve

    pilot "{i}Ну что, все готовы?{/i}" with dissolve

    show pilot drive3 with dissolve

    pilot "{i}Следующая остановка - Ростов-на-Дону!{/i}" with dissolve

    scene black with dissolve

    pilot "{i}От винта!{/i}" with dissolve

    scene black
    show movie_plane
    pause 20.0

    jump branch1_day3_piper_cherokee1



label branch1_day3_piper_cherokee1:

    stop music fadeout 1.0

    play music "audio/440163__mozfoo__prop-plane.ogg" fadein 3.0

    queue music "audio/440163__mozfoo__prop-plane.ogg"


    scene black

    show plane_ver1_loop2 as plane_bkg_loop1:
        xpos 0.0
        linear 96.0 xpos -1.0
        repeat

    show plane_ver1_loop2 as plane_bkg_loop2:
        xpos 1.0
        linear 96.0 xpos 0.0
        repeat

    show plane_ver1_loop3 as plane_bkg_mountains_loop1:
        parallel:
            xpos 0.0
            linear 96.0 xpos -1.0
            repeat
        parallel:
            linear 320.0 ypos 1.0

    show plane_ver1_loop3 as plane_bkg_mountains_loop2:
        parallel:
            xpos 1.0
            linear 96.0 xpos 0.0
            repeat
        parallel:
            linear 320.0 ypos 1.0

    show plane_ver1

    show plane_shadow

    show black as fg_black zorder 10

    show AliyaSitSide headphones_straight as aliya with dissolve

    show pilot drive3 with dissolve

    hide fg_black with dissolve

    "Самолет плавно набирал высоту над горами Дагестана." with dissolve

    "Рев мотора перекрывал все прочие звуки." with dissolve

    show pilot drive5 with dissolve

    pilot "{i}Мы сейчас летим на высоте пять тысяч километров, со скоростью сто восемьдесят километров в час.{/i}" with dissolve

    pilot "{i}Через несколько часов мы прилетим на аэродром под Ростовом-на-Дону.{/i}" with dissolve

    show pilot drive3 with dissolve

    show AliyaSitSide headphones_fright2 as aliya with dissolve

    aliya "{i}Нас не остановят по пути нигде?{/i}" with dissolve

    show AliyaSitSide headphones_fright2_2 as aliya with dissolve

    pilot "{i}Хах, кто нас остановит в небе?{/i}" with dissolve

    pilot "{i}Маршрут полета согласован заранее. Бензина хватит до Ростова.{/i}" with dissolve

    pilot "{i}На этом эшелоне почти никто не летает, никому до нас нет дела.{/i}" with dissolve

    show AliyaSitSide headphones_fright2 as aliya with dissolve

    aliya "{i}Какое облегчение...{/i}" with dissolve

    show AliyaSitSide headphones_sad3 as aliya with dissolve

    "Алия посмотрела мне в глаза." with dissolve

    show AliyaSitSide headphones_neutral2 as aliya with dissolve

    aliya "{i}Семён, спасибо тебе большое! Я до сих пор поверить не могу, что я на свободе.{/i}" with dissolve

    aliya "{i}И вам тоже спасибо... как вас зовут?{/i}" with dissolve

    show AliyaSitSide headphones_sad3 as aliya with dissolve

    show pilot drive5 with dissolve

    pilot "{i}Николай.{/i}" with dissolve

    show pilot drive3 with dissolve

    show AliyaSitSide headphones_neutral2 as aliya with dissolve

    aliya "{i}Спасибо, Николай!{/i}" with dissolve

    show AliyaSitSide headphones_neutral1 as aliya with dissolve

    pilot "{i}Да не за что! Хаха, обычно я беру за полет от пятнадцати тысяч рублей.{/i}" with dissolve

    pilot "{i}Но я в курсе вашей ситуации, Алия. И поэтому я решил помочь бесплатно.{/i}" with dissolve

    show AliyaSitSide headphones_neutral2 as aliya with dissolve

    aliya "{i}Спасибо большое.{/i}" with dissolve

    aliya "{i}Я выбралась из дома, но у меня нет с собой ни денег, ни паспорта, ни телефона.{/i}" with dissolve

    show AliyaSitSide headphones_neutral1 as aliya with dissolve

    pilot "{i}Ну это вам нужно в МВД обращаться. Я могу только привезти вас в Ростов.{/i}" with dissolve

    me "{i}Этот вопрос решаемый. Обсудим, когда выберемся в безопасное место.{/i}" with dissolve

    show AliyaSitSide headphones_neutral2 as aliya with dissolve

    aliya "{i}Хорошо...{/i}" with dissolve

    show AliyaSitSide headphones_sad3 as aliya with dissolve

    "Неожиданно, самолет слегка тряхнуло." with dissolve

    show AliyaSitSide headphones_neutral2 as aliya with dissolve

    aliya "Ой!" with dissolve

    aliya "{i}А мы не упадем?{/i}" with dissolve

    show AliyaSitSide headphones_neutral1 as aliya with dissolve

    show pilot drive5 with dissolve

    pilot "{i}Нет. Когда самолет трясет - это называется турбулентность.{/i}" with dissolve

    pilot "{i}Это неприятно и может вызвать тошноту.{/i}" with dissolve

    pilot "{i}Но есть и хорошие новости - от турбулентности еще ни один самолет в мире не упал.{/i}" with dissolve

    show pilot drive3 with dissolve

    show AliyaSitSide headphones_neutral2 as aliya with dissolve

    aliya "{i}Хорошо...{/i}" with dissolve

    aliya "{i}А это нормально что в самолете пахнет бензином?{/i}" with dissolve

    show AliyaSitSide headphones_neutral1 as aliya with dissolve

    pilot "{i}Хах, да, это тебе не бизнес-класс от Эмирейтс.{/i}" with dissolve

    show AliyaSitSide headphones_neutral2 as aliya with dissolve

    aliya "{i}Да, конечно, понимаю.{/i}" with dissolve

    show AliyaSitSide headphones_straight as aliya with dissolve

    "Наступила неловкая тишина..." with dissolve

    me "{i}А вот у меня вопрос. Легко ли стать пилотом, как вы?{/i}" with dissolve

    show pilot drive5 with dissolve

    pilot "{i}Чуть сложнее, чем получить водительские права, конечно.{/i}" with dissolve

    pilot "{i}Чтобы получить лицензию PPL, нужно налетать 40 часов и сдать экзамен по теории.{/i}" with dissolve

    pilot "{i}Обычно все упирается в деньги, так как нужно арендовать самолет, чтобы налетать эти 40 часов.{/i}" with dissolve

    show pilot drive3 with dissolve

    me "{i}А вы арендовали самолет?{/i}" with dissolve

    pilot "{i}Хаха, нет, у меня свой. Я сам сдаю в аренду и обучаю пилотов-любителей.{/i}" with dissolve

    me "{i}Интересно! А сколько стоит самолет?{/i}" with dissolve

    show pilot drive5 with dissolve

    pilot "{i}Ну в среднем, как очень хороший внедорожник.{/i}" with dissolve

    pilot "{i}Мне мой обошелся в тридцать тысяч евро.{/i}" with dissolve

    pilot "{i}Но я просто в своем сообществе общаюсь, и мы все друг друга так или иначе знаем.{/i}" with dissolve

    pilot "{i}Кто продает самолет, кто хочет купить - у нас это быстро становится известно.{/i}" with dissolve

    show pilot drive3 with dissolve
    
    me "{i}Тридцать тысяч евро, это немаленькие деньги.{/i}" with dissolve

    me "{i}А побюджетнее никак?{/i}" with dissolve

    pilot "{i}Если не можете себе позволить самолет, можете летать на автожире.{/i}" with dissolve

    me "{i}Автожире?{/i}" with dissolve

    pilot "{i}Автожир, гирокоптер, гироплан.{/i}" with dissolve

    pilot "{i}Что-то среднее между самолетом и вертолетом.{/i}" with dissolve

    pilot "{i}Он проще в управлении, и на него проще получить лицензию.{/i}" with dissolve

    pilot "{i}И стоит дешевле.{/i}" with dissolve

    pilot "{i}Посмотри в интернете видео про автожиры, чтобы получить представление.{/i}" with dissolve

    pilot "{i}Там в двух словах не объяснить.{/i}" with dissolve

    me "{i}Хорошо, я посмотрю потом.{/i}" with dissolve

    "Наступила тишина." with dissolve

    "Равномерный шум двигателя действовал на меня усыпляюще." with dissolve

    "Я заметил, что Алия тоже прислонилась к стеклу и закрыла глаза." with dissolve

    "Что же, раз нам предстоит долгий полет, почему бы и не поспать немного..." with dissolve

    scene black with dissolve

    "И я тоже закрыл глаза..." with dissolve

    "Мне удалось ненадолго уснуть." with dissolve

    "Из-за равномерного гула мотора я немного потерял ход времени." with dissolve

    "И я просыпался несколько раз, а потом снова засыпал." with dissolve
    
    "Я уже не знал сколько времени прошло пока я спал..." with dissolve

    jump branch1_day3_piper_cherokee2

label branch1_day3_piper_cherokee2:

    "Во сне я почувствовал как самолет коснулся земли." with dissolve

    "Затем я почувствовал торможение, меня слегка потянуло вперед." with dissolve

    stop music fadeout 5.0

    pilot "Мы прилетели! Можете выходить из самолета!" with dissolve

    jump branch1_day3_accessible_sky_exterior1


label branch1_day3_accessible_sky_exterior1:


    play music "music/nighty.ogg"

    queue music "music/nighty.ogg"

    scene black

    show accessible_sky_ext3d2 as accessible_sky_ext with dissolve

    show Aliya straight_hoodie_happy1_2 at any_right_pos with dissolve:
        ypos 1.1

    "Мы вышли из самолета на свежий воздух." with dissolve

    show pilot out as pilot with dissolve

    "После нас вышел пилот, и закрыл дверь самолета." with dissolve

    hide pilot with dissolve

    show accessible_sky_ext3d1 as accessible_sky_ext with dissolve

    show pilot neutral_speak as pilot at any_left_pos with dissolve

    pilot "Ну как вам перелет?" with dissolve

    show pilot neutral as pilot at any_left_pos with dissolve

    me "Было круто!" with dissolve

    show Aliya straight_hoodie_happy1 at any_right_pos with dissolve:
        ypos 1.1

    aliya "Мне тоже понравилось!" with dissolve

    show Aliya straight_hoodie_happy1_2 at any_right_pos with dissolve:
        ypos 1.1

    show pilot neutral_speak as pilot at any_left_pos with dissolve

    pilot "Добро пожаловать в наш Ростовский аэроклуб!" with dissolve

    pilot "Здесь собираются все кто неравнодушен к небу." with dissolve

    pilot "Кстати, можете сфоткаться на фоне самолета!" with dissolve

    show pilot neutral as pilot at any_left_pos with dissolve

    me "Эээ, нет спасибо, мне сейчас не до этого..." with dissolve

    show Aliya half_turn_hoodie_happy1_2 at any_right_pos with dissolve:
        ypos 1.1

    aliya "А я - с удовольствием!" with dissolve

    aliya "Семён, сфоткаешь меня?" with dissolve

    show Aliya half_turn_hoodie_happy1_1 at any_right_pos with dissolve:
        ypos 1.1

    hide pilot with dissolve

    hide Aliya with dissolve

    show Aliya_airclub neutral as Aliya with dissolve

    show pilot look as pilot at any_right_pos with dissolve

    "Алия подбежала к самолету и встала прямо возле него." with dissolve

    show day3_time1748 as cg_screen_phone with dissolve:
        xalign 1.0

    "Что же, делать нечего, я достал телефон." with dissolve

    show cg_screen_phone_day3_photo1 as cg_screen_phone with dissolve:
        xalign 1.0
    
    "Затем я навел камеру на Алию..." with dissolve

    show cg_screen_phone_day3_photo3 as cg_screen_phone:
        xalign 1.0

    show cg_screen_phone_day3_photo2 as cg_screen_phone2:
        xalign 1.0
        alpha 0.0
        linear 0.3 alpha 1.0
        linear 0.3 alpha 0.0


    "И сфотографировал ее." with dissolve

    hide cg_screen_phone with dissolve

    hide cg_screen_phone2

    hide Aliya with dissolve

    show Aliya straight_hoodie_happy1 at any_left_pos with dissolve:
        ypos 1.1

    show pilot neutral as pilot at any_far_right_pos with dissolve

    "Алия снова подошла ко мне." with dissolve
    
    show Aliya_phone semoyn_phone1 as Aliya at any_left_pos with dissolve:
        ypos 1.1
    
    aliya "Покажи фотографию?" with dissolve

    show cg_screen_phone_day3_photo3 as cg_screen_phone with dissolve:
        xalign 1.0

    me "Вот..." with dissolve

    hide cg_screen_phone with dissolve

    show Aliya_phone semoyn_phone2 as Aliya at any_left_pos with dissolve:
        ypos 1.1

    aliya "Хорошо получилось!" with dissolve

    show Aliya_phone semoyn_phone3 as Aliya at any_left_pos with dissolve:
        ypos 1.1

    aliya "Отправишь кому-нибудь - убью!" with dissolve

    show Aliya straight_hoodie_neutral1 at any_left_pos with dissolve:
        ypos 1.1

    me "Хорошо..." with dissolve

    show pilot neutral_speak as pilot at any_far_right_pos with dissolve

    pilot "Надеюсь вам у нас понравится." with dissolve

    pilot "Мне нужно будет заправить самолет." with dissolve

    me "А где мы?" with dissolve

    pilot "Мы сейчас в Ростовской области!" with dissolve

    pilot "Это аэроклуб Чистое Небо!" with dissolve

    pilot "Многие мои друзья пилоты здесь собираются." with dissolve

    pilot "Здесь мы учим летать. Уже не одно поколение пилотов налетало здесь свои летные часы!" with dissolve

    pilot "Также мы катаем на самолетах всех желающих." with dissolve

    pilot "Я могу вам многое рассказать про наш аэроклуб." with dissolve

    pilot "Но сначала предлагаю перекусить!" with dissolve

    show pilot neutral as pilot at any_far_right_pos with dissolve

    "Я почувствовал голод - я же с утра ничего не ел." with dissolve

    me "А где мы можем поесть?" with dissolve

    show pilot neutral_speak as pilot at any_far_right_pos with dissolve

    pilot "У нас тут есть кафе, вот прямо перед летным полем." with dissolve

    pilot "Предлагаю пройти туда!" with dissolve

    show pilot neutral as pilot at any_far_right_pos with dissolve

    scene black with dissolve

    "И мы пошли к кафе..." with dissolve

    jump branch1_day3_accessible_sky_exterior_cafe


label branch1_day3_accessible_sky_exterior_cafe:

    show black zorder 10

    show accessible_sky_cafe1 zorder 1

    show accessible_sky_cafe2 zorder 2

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 3 with dissolve

    show pilot sit_neutral zorder 3 with dissolve

    show accessible_sky_cafe3 zorder 4

    hide black with dissolve

    "Мы сели за столик, и заказали себе еду." with dissolve

    show pilot sit_neutral_speak zorder 3 with dissolve

    pilot "Семён, я так понимаю, тебе еще рано выключать авиарежим в телефоне." with dissolve

    pilot "Я написал в ваш чатик, что вы успешно выбрались из Дагестана и находитесь в Ростове." with dissolve

    show pilot sit_neutral zorder 3 with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 3 with dissolve

    aliya "Чатик? Какой еще чатик?" with dissolve
    
    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 3 with dissolve

    me "Ну помнишь, я же рассказал своим друзьям про твою ситуацию." with dissolve

    me "У нас уже целая группа по спасению тебя." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_happy1 zorder 3 with dissolve

    "Алия опять смущенно улыбнулась." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_happy2 zorder 3 with dissolve

    aliya "Я уже знаю Романа, и вас, Николай." with dissolve

    aliya "А кто еще?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 3 with dissolve

    me "Ну, скоро за нами приедет Ярик, и мы поедем в Москву!" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 3 with dissolve

    aliya "В Москву? Снова? И что мы там будем делать?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 3 with dissolve

    me "Вот как раз там мы все вместе соберемся и решим, что делать дальше." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried4 zorder 3 with dissolve

    "Алия вздохнула." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried3 zorder 3 with dissolve

    aliya "Я рада что я на свободе, но что делать дальше, не представляю." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 3 with dissolve

    aliya "Сейчас мне еще сложнее, чем когда я бежала в первый раз." with dissolve

    aliya "У меня нет ни паспорта, ни телефона, ни денег." with dissolve

    aliya "Родители меня будут искать сразу же." with dissolve

    aliya "Еще и отец подключит своих родственников из ФСБ." with dissolve

    aliya "А если они меня найдут - скорее всего убьют и закопают где-нибудь." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 3 with dissolve

    me "Что ты думаешь насчет того, чтобы уехать из России?." with dissolve

    me "Там тебя не достанут." with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried2 zorder 3 with dissolve

    aliya "Но как я поеду заграницу без паспорта?" with dissolve

    aliya "Николай, вы можете меня увезти на самолете в другую страну?" with dissolve

    show AliyaSitTableLeft hoodie_hands_down_worried1 zorder 3 with dissolve

    "Николай задумался." with dissolve

    show pilot sit_neutral_speak zorder 3 with dissolve

    pilot "Хмм..." with dissolve

    pilot "По правилам, я все равно должен вылетать из международного аэропорта," with dissolve

    pilot "Я должен согласовывать пассажиров и маршрут полета с Росавиацией." with dissolve

    pilot "Если я так просто возьму и улечу на самолете в другую страну, то нарушу кучу законов." with dissolve

    show pilot sit_neutral zorder 3 with dissolve

    me "А что может случится? ПВО собъет ваш самолет?" with dissolve

    show pilot sit_neutral_speak zorder 3 with dissolve

    pilot "Думаю нет. Если самолет маленький и низко летит, то не собьют." with dissolve

    pilot "В 1987 году Матиас Руст на Цесне пересек границу Финляндии с СССР и успешно приземлился на Красной Площади." with dissolve

    pilot "И это был 87 год, СССР. Сейчас, в наше время, тем более никто никого сбивать не будет." with dissolve

    pilot "Но как только вы сядете, вас арестует местная полиция." with dissolve

    show pilot sit_neutral zorder 3 with dissolve

    "Николай вздохнул." with dissolve

    show pilot sit_neutral_speak zorder 3 with dissolve

    pilot "Теоретически, можно сбежать на самолете в другую страну, а потом на месте попросить политическое убежище." with dissolve

    pilot "Но я не знаю, сможете ли вы выиграть кейс в миграционном суде." with dissolve

    pilot "Может быть вам не поверят и вас депортируют." with dissolve

    pilot "Так что я бы десять раз подумал бы, прежде чем пробовать." with dissolve

    show pilot sit_neutral zorder 3 with dissolve

    "Наступила тишина." with dissolve

    show pilot sit_neutral_speak zorder 3 with dissolve

    pilot "Кстати, Ярик пишет, что он устал с дороги, и переночует под Ростовом." with dissolve

    pilot "За вами он заедет завтра, в 7 утра." with dissolve

    show pilot sit_neutral zorder 3 with dissolve

    aliya "А где мы будем ночевать?" with dissolve

    show pilot sit_neutral_speak zorder 3 with dissolve

    pilot "Здесь в авиаклубе есть гостиница." with dissolve

    show pilot sit_neutral zorder 3 with dissolve

    me "Но нам нельзя светить свои паспорта!" with dissolve

    "Николай еле заметно улыбнулся." with dissolve

    show pilot sit_neutral_speak zorder 3 with dissolve

    pilot "Я могу решить этот вопрос..." with dissolve

    show pilot sit_neutral zorder 3 with dissolve

    me "Правда? Это было бы здорово!" with dissolve

    show pilot sit_neutral_speak zorder 3 with dissolve

    pilot "Да, мне не трудно. Меня тут знают!" with dissolve

    pilot "Давайте тогда заканчивать ужин. Пойдем бронировать комнаты, а потом я поеду домой." with dissolve

    pilot "Сегодня я неплохо полетал, пора бы уже и отдохнуть." with dissolve

    show pilot sit_neutral zorder 3 with dissolve

    me "Хорошо!" with dissolve

    scene black with dissolve

    "Мы поели и встали из-за стола..." with dissolve

    jump branch1_day3_accessible_sky_exterior_parking

label branch1_day3_accessible_sky_exterior_parking:

    scene black with dissolve

    show parking3_0 as parking_overlay with dissolve

    show pilot neutral as pilot at any_right_pos with dissolve

    show Aliya straight_hoodie_sad3 at any_left_pos with dissolve:
        ypos 1.1

    "Николай забронировал нам номера в гостинице, а затем мы вышли на парковку." with dissolve

    show pilot neutral_speak as pilot at any_right_pos with dissolve

    pilot "Что же, пора прощаться." with dissolve

    pilot "Семён, Алия! Было приятно познакомиться с вами." with dissolve

    show pilot neutral as pilot at any_right_pos with dissolve

    me "Мне тоже приятно. Спасибо за все!" with dissolve

    show Aliya straight_hoodie_happy1 at any_left_pos with dissolve:
        ypos 1.1

    aliya "Я тоже очень рада, что познакомилась с вами!" with dissolve

    show Aliya straight_hoodie_happy1_2 at any_left_pos with dissolve:
        ypos 1.1

    show pilot neutral_speak as pilot at any_right_pos with dissolve

    pilot "Желаю удачи в вашем путешествии! Надеюсь, все у вас получится." with dissolve

    pilot "Не знаю, будет ли возможность в будущем, но приезжайте в наш аэроклуб еще!" with dissolve

    pilot "Здесь вы можете полетать на самолетах, или прыгать с парашютом." with dissolve

    pilot "Буду рад вас видеть у нас в Ростове снова!" with dissolve

    pilot "Пока, удачи!" with dissolve

    show pilot neutral as pilot at any_right_pos with dissolve

    me "Пока!" with dissolve

    show Aliya straight_hoodie_happy2_2 at any_left_pos with dissolve:
        ypos 1.1

    aliya "До свидания!" with dissolve

    show Aliya straight_hoodie_sad3 at any_left_pos with dissolve:
        ypos 1.1

    hide pilot with dissolve

    show parking3_1 as parking_overlay with dissolve

    show Aliya_back back2 as Aliya with dissolve:
        ypos 1.1

    "Николай сел в автомобиль," with dissolve

    show parking3_2 as parking_overlay with dissolve

    "Затем завел двигатель," with dissolve

    show parking3_3 as parking_overlay with dissolve

    "И уехал." with dissolve

    show Aliya straight_hoodie_sad3 at any_left_pos with dissolve:
        ypos 1.1

    "Я остался наедине с Алией." with dissolve

    play music "music/Runaway_11 (Pre_Loop).ogg"

    queue music "music/Runaway_11 (Loop).ogg"

    me "Мне столько всего надо сказать тебе." with dissolve

    "Алия смутилась." with dissolve

    show Aliya straight_hoodie_sad1 at any_left_pos with dissolve:
        ypos 1.1

    aliya "Я понимаю..." with dissolve

    show Aliya straight_hoodie_sad2 at any_left_pos with dissolve:
        ypos 1.1

    me "Может присядем на скамейку?" with dissolve

    show Aliya straight_hoodie_sad1 at any_left_pos with dissolve:
        ypos 1.1

    aliya "Хорошо." with dissolve

    hide Aliya with dissolve

    show black zorder 10 with dissolve

    show swing3_shadow

    show AliyaSitSide turned_hoodie_fright2_2 as Aliya zorder 2

    hide black with dissolve

    "Мы присели на скамейку." with dissolve

    me "С того момента как ты исчезла, я места себе не находил." with dissolve

    me "Ты просто добавила меня в ЧС и удалила все сообщения." with dissolve

    show AliyaSitSide turned_hoodie_fright1 as Aliya zorder 2

    aliya "Да, это было в тот вечер, когда мы уехали из Москвы." with dissolve

    aliya "Еще в автобусе мой отец увидел что я получаю сообщения." with dissolve

    aliya "Он потребовал чтобы я прекратила с тобой общаться." with dissolve

    aliya "Мне пришлось удалить переписку, и заблокировать тебя." with dissolve

    aliya "Потом он забрал у меня телефон." with dissolve

    show AliyaSitSide turned_hoodie_sad2 as Aliya zorder 2

    me "Что было дальше?" with dissolve

    "Алия вздохнула." with dissolve

    show AliyaSitSide turned_hoodie_sad1 as Aliya zorder 2

    aliya "Неприятно вспоминать, на самом деле." with dissolve

    aliya "Из Пятигорска родители сразу же повезли меня в аул." with dissolve

    aliya "Там они собрали семейный совет, решать что дальше делать со мной." with dissolve

    aliya "Говорили что я всех опозорила, что счастье что никто об этом не узнал." with dissolve

    aliya "Тетя, сестра отца, говорила что для таких как я есть кладбище специальное." with dissolve

    show AliyaSitSide turned_hoodie_sad2 as Aliya zorder 2

    me "Это ужасно." with dissolve

    show AliyaSitSide turned_hoodie_sad1_2 as Aliya zorder 2

    aliya "Ну я всю жизнь такое выслушивала." with dissolve

    aliya "И я догадывалась, что так и будет." with dissolve

    aliya "Мать плакала, спрашивала меня, зачем я так поступила." with dissolve

    aliya "Отец угрожал, что если хоть кто-нибудь узнает, мне конец." with dissolve

    aliya "Сестра спрашивала, почему я все скрыла от нее." with dissolve

    aliya "Было очень тяжело." with dissolve
    
    show AliyaSitSide turned_hoodie_sad2_2 as Aliya zorder 2

    me "И чем закончился семейный совет?" with dissolve

    show AliyaSitSide turned_hoodie_sad1_3 as Aliya zorder 2

    aliya "Моя родня решила скрыть факт побега от жениха, и все-таки выдать меня замуж." with dissolve

    show AliyaSitSide turned_hoodie_sad2_3 as Aliya zorder 2

    me "Получается, они обманули тебя?" with dissolve

    show AliyaSitSide turned_hoodie_sad1_3 as Aliya zorder 2

    aliya "Да." with dissolve

    aliya "Меня заперли дома, запретили выходить даже в магазин за продуктами." with dissolve

    aliya "Я могла гулять только во дворе дома." with dissolve

    aliya "Со мной постоянно кто-то был - мама, либо тетя, либо сестра." with dissolve

    aliya "Я думала о том чтобы сбежать или совершить самоубийство." with dissolve

    show AliyaSitSide turned_hoodie_sad1_2 as Aliya zorder 2

    aliya "Но из моего села сложно уехать." with dissolve

    aliya "У моего отца родственник - начальник МВД Дагестана." with dissolve

    aliya "И отец мне постоянно говорил, что если я сбегу, то меня поймают на любом блокпосту или в аэропорту." with dissolve

    show AliyaSitSide turned_hoodie_sad3_2 as Aliya zorder 2

    "Алия улыбнулась." with dissolve

    show AliyaSitSide turned_hoodie_sad1_2 as Aliya zorder 2

    aliya "Но ты сделал невозможное." with dissolve

    aliya "Прислать за мной самолетик, который сядет в чистом поле - это же надо было додуматься!" with dissolve

    show AliyaSitSide turned_hoodie_sad3_2 as Aliya zorder 2

    me "Спасибо! Хотя это была не моя идея." with dissolve

    show AliyaSitSide turned_hoodie_sad1 as Aliya zorder 2

    aliya "Все равно ты смог меня вытащить." with dissolve

    aliya "Я рада что доверилась тебе." with dissolve

    aliya "Скажу честно, там в Москве я не доверяла тебе на сто процентов." with dissolve

    show AliyaSitSide turned_hoodie_sad3_2 as Aliya zorder 2

    me "Не доверяла мне? Почему?" with dissolve

    show AliyaSitSide turned_hoodie_sad1 as Aliya zorder 2

    aliya "Ну ты вел себя странно." with dissolve

    aliya "Переписывался с кем-то." with dissolve

    aliya "Говорил странные вещи." with dissolve

    aliya "Когда родители сказали мне, что свадьбы не будет, я им поверила. А тебе - нет." with dissolve

    aliya "Я сейчас понимаю, что доверяться родителям было глупо." with dissolve

    aliya "Еще там, в Москве, мать обещала что приедет одна, если мы скажем адрес." with dissolve

    aliya "Но в итоге приехал мой дядя." with dissolve

    aliya "Если так подумать, то и в прошлом, мои родители тоже часто обманывали меня." with dissolve

    aliya "Ну ничего, больше я им на слово не поверю." with dissolve

    aliya "Еще раз спасибо тебе!" with dissolve

    aliya "Хотя я тебе пока еще не до конца доверяю." with dissolve

    show AliyaSitSide turned_hoodie_sad2 as Aliya zorder 2

    me "Почему?" with dissolve

    show AliyaSitSide turned_hoodie_sad1 as Aliya zorder 2

    aliya "Ну..." with dissolve

    aliya "Ты много для меня сделал, честно," with dissolve

    aliya "Но мы знакомы всего несколько дней." with dissolve

    aliya "Я не знаю какие у тебя намерения." with dissolve

    aliya "Если ты не предашь меня и не сделаешь мне ничего плохого - я буду доверять тебе больше." with dissolve
    
    show AliyaSitSide turned_hoodie_sad2 as Aliya zorder 2

    me "Хорошо..." with dissolve

    show AliyaSitSide turned_hoodie_sad1 as Aliya zorder 2

    aliya "Ладно, я чувствую что я очень устала." with dissolve

    aliya "Нам завтра вставать рано." with dissolve

    show AliyaSitSide turned_hoodie_sad2 as Aliya zorder 2

    me "Хорошо, конечно!" with dissolve

    me "Ты не проспишь?" with dissolve

    show AliyaSitSide turned_hoodie_sad3_2 as Aliya zorder 2

    "Алия улыбнулась." with dissolve

    show AliyaSitSide turned_hoodie_sad1 as Aliya zorder 2

    aliya "Если я не проснусь, стучи в дверь моей комнаты." with dissolve
    
    show AliyaSitSide turned_hoodie_sad3_2 as Aliya zorder 2

    me "Хорошо!" with dissolve

    scene black with dissolve

    "Мы зашли внутрь и разошлись по комнатам..." with dissolve

    scene black with dissolve

    "И я поднялся в свою комнату в гостинице." with dissolve

    jump branch1_day3_accessible_sky_interior_room


label branch1_day3_accessible_sky_interior_room:

    scene black

    show hotelroom3_1a as hotelroom with dissolve

    "Это был обычный номер в гостинице." with dissolve

    "Я прилег на кровать и погрузился в свои мысли." with dissolve

    "Второй побег Алии прошел успешно." with dissolve

    "Алия была в соседней комнате, и мирно спала." with dissolve

    "И я теперь чувствую себя намного спокойнее." with dissolve

    "Да, у Алии сейчас нет документов, и очень скоро ее начнет искать полиция и родственники." with dissolve

    "Но по крайней мере сейчас инициатива на нашей стороне." with dissolve

    show hotelroom3_1 as hotelroom with dissolve

    show day3_time1825 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я достал свой телефон." with dissolve

    "Телефон по-прежнему в авиарежиме, однако часы показывают правильное время." with dissolve

    "В целях безопасности я не должен использовать вайфай или мобильную сеть." with dissolve

    show cg_screen_phone_day3_photo3 as cg_screen_phone with dissolve:
        xalign 1.0

    "Я открыл фотографию Алии, которую сделал у самолета." with dissolve

    "Она выглядела очень мило." with dissolve

    "И я снова задумался о судьбе." with dissolve

    "Несколько дней назад я был в растерянности - я не знал, где Алия и что она делает сейчас." with dissolve

    "Сутки назад я летел в Дагестан чтобы помочь сбежать, не зная при этом, получится у меня или нет." with dissolve

    "И вот сейчас Алия спит в соседней комнате, в полной безопасности." with dissolve

    "Я постарался предусмотреть все, чтобы нас не нашли." with dissolve

    "Однако я все равно сильно рискую, спасая Алию." with dissolve

    "Интересно все-таки посмотреть, насколько далеко нам удасться зайти?" with dissolve

    "Алия рассказывала мне что хочет уехать в Корею - быть может, именно этим и закончится наше приключение?" with dissolve

    "Что же, посмотрим." with dissolve

    "Завтра утром приедет Ярик, и мы поедем в Москву." with dissolve

    "И уже в Москве будем решать, что делать дальше..." with dissolve

    "Что же, пора спать." with dissolve

    show hotelroom3_1a as hotelroom with dissolve

    hide cg_screen_phone with dissolve

    "Я поставил телефон на зарядку." with dissolve

    scene black with dissolve

    stop music fadeout 5.0

    "Мои глаза закрылись..." with dissolve

    "И я уснул..." with dissolve

    jump branch1_day4_accessible_sky_interior_room

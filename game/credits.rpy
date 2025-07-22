
define player_skipped_credits = False

screen credits_helper():

    key "dismiss" action [ SetVariable("player_skipped_credits", True), Jump("after_credits")]
    key 'button_select' action [ SetVariable("player_skipped_credits", True), Jump("after_credits")]
    key 'input_enter' action [ SetVariable("player_skipped_credits", True), Jump("after_credits")]
    key 'bar_activate' action [ SetVariable("player_skipped_credits", True), Jump("after_credits")]
    key 'bar_deactivate' action  [ SetVariable("player_skipped_credits", True), Jump("after_credits")]


label credits:
    $ renpy.pause(0.5)

    $ quick_menu = False
    $ show_say_menu = False

    show screen credits_helper

    scene black

    show credits_bkg1 with dissolve

    show credits_sprite1 at any_left_pos with dissolve

    show text Text(_("{color=#CC0000}Продюсер:{/color}\nВладислав Хорев"), size=int(50)) as credits_text1_line1 at credits_text1_line1_pos zorder 10 with dissolve:
        xpos 0.55
        linear 5.0 xpos 0.52

    $ renpy.pause(0.2)

    show text Text(__("{color=#CC0000}Разработчик:{/color}\nВладислав Хорев"), size=int(50)) as credits_text1_line2 at credits_text1_line2_pos zorder 10 with dissolve:
        xpos 0.55
        linear 5.0 xpos 0.52

    $ renpy.pause(3)

    hide credits_sprite1 with dissolve

    hide credits_text1_line1 with dissolve

    hide credits_text1_line2 with dissolve

    show credits_bkg2 with dissolve

    hide credits_bkg1

    show credits_sprite2 with dissolve

    show text Text(__("{color=#CC0000}Автор сценария:{/color}\nВладислав Хорев"), size=int(50)) as credits_text1_line3 at credits_text1_line3_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.15

    $ renpy.pause(0.2)

    show text Text(__("{color=#CC0000}Тексты:{/color}\nВладислав Хорев"), size=int(50)) as credits_text1_line4 at credits_text1_line4_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.15

    $ renpy.pause(3)

    hide credits_sprite2 with dissolve

    hide credits_text1_line3 with dissolve

    hide credits_text1_line4 with dissolve

    show hotelroom3_2a with dissolve

    hide credits_bkg2

    $ renpy.pause(0.2)

    show text Text(_("{color=#CC0000}Спрайты персонажей:{/color}\nОксана Дмитриева\nMarys (Маша Свиридова)\nТатьяна \"Akinago\" Аверина\nMaggie Tem\nAlan Klaver"), size=int(50)) as credits_text1_line5 at credits_text1_line5_pos zorder 10 with dissolve:
        xpos 0.45
        linear 5.0 xpos 0.52

    show hotelroom3_2 with dissolve

    $ renpy.pause(3)

    hide credits_text1_line5 with dissolve

    hide hotelroom3_2 with dissolve

    show credits_bkg4 with dissolve

    hide hotelroom3_2a

    $ renpy.pause(0.2)

    show credits_sprite4 with dissolve

    show text Text(_("{color=#CC0000}Фоны:{/color}\nLaynesis Ling\nshumoi\nQuandial\nВлад HEHUDOJNIK\nАнонимный художник"), size=int(50)) as credits_text1_line61 at credits_text1_line61_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.12

    show text Text(_("{color=#CC0000}Прочие изображения:{/color}\nАнна Агеева\nТатьяна \"Akinago\" Аверина"), size=int(50)) as credits_text1_line62 at credits_text1_line62_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.12

    $ renpy.pause(3)

    hide credits_text1_line61 with dissolve

    hide credits_text1_line62 with dissolve

    hide credits_sprite4 with dissolve

    show credits_bkg5 with dissolve

    hide credits_bkg4

    $ renpy.pause(0.2)

    show credits_sprite5 with dissolve:
        xzoom -1

    $ renpy.pause(0.2)

    show text Text(_("{color=#CC0000}Музыка:{/color}\nRomull\nPazetic Ocean"), size=int(50)) as credits_text1_line7 at credits_text1_line7_pos zorder 10 with dissolve:
        xpos 0.47
        linear 5.0 xpos 0.44

    show text Text(_("{color=#CC0000}Звуки и амбиент:{/color}\nВладислав Хорев\nFreeSound.org"), size=int(50)) as credits_text1_line8 at credits_text1_line8_pos zorder 10 with dissolve:
        xpos 0.47
        linear 5.0 xpos 0.44

    $ renpy.pause(3)

    hide credits_sprite5 with dissolve

    hide credits_text1_line7 with dissolve

    hide credits_text1_line8 with dissolve

    show credits_bkg6 with dissolve

    hide credits_bkg5

    show credits_sprite6 at any_right_pos with dissolve

    $ renpy.pause(0.2)

    show text Text(_("{color=#CC0000}Моушн-дизайн:{/color}\nВлад HEHUDOJNIK"), size=int(50)) as credits_text1_line9 at credits_text1_line9_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.12

    $ renpy.pause(2)

    hide credits_sprite6 with dissolve

    hide credits_text1_line9 with dissolve

    show credits_bkg7 with dissolve

    hide credits_bkg6

    $ renpy.pause(0.2)


    show text Text(_("Все персонажи и произошедшие в игре события вымышлены."), size=int(36)) as credits_text10_line1 at credits_text10_line1_pos zorder 10 with dissolve

    $ renpy.pause(2)

    show text Text(_("Любые совпадения с реальными личностями и событиями случайны."), size=int(36)) as credits_text10_line2 at credits_text10_line2_pos zorder 10 with dissolve
    $ renpy.pause(4)



    if _preferences.language == None:

        hide credits_text10_line1 with dissolve

        hide credits_text10_line2 with dissolve

        hide credits_text10_line3 with dissolve

        show text Text("Если ваша знакомая окажется в похожей затруднительной ситуации,", size=int(36)) as credits_text11_line1 at credits_text11_line1_pos zorder 10 with dissolve

        $ renpy.pause(2)

        show text Text("Сообщите ей мои контактные данные:", size=int(36)) as credits_text11_line2 at credits_text11_line2_pos zorder 10 with dissolve

        $ renpy.pause(2)

        show text Text("VK: ", size=int(36)) as credits_text11_line311 at credits_text11_line311_pos zorder 10 with dissolve

        show text Text("{b}vk.com/id677718{/b}", size=int(36)) as credits_text11_line312 at credits_text11_line312_pos zorder 10 with dissolve

        show text Text("Telegram: ", size=int(36)) as credits_text11_line321 at credits_text11_line321_pos zorder 10 with dissolve

        show text Text("{b}mephi1984{/b}", size=int(36)) as credits_text11_line322 at credits_text11_line322_pos zorder 10 with dissolve

        show text Text("Телефон: ", size=int(36)) as credits_text11_line331 at credits_text11_line331_pos zorder 10 with dissolve

        show text Text("{b}+7 925 014 8281{/b}", size=int(36)) as credits_text11_line332 at credits_text11_line332_pos zorder 10 with dissolve

        $ renpy.pause(2)

        show text Text("Я постараюсь ей помочь или найду того, кто сможет это сделать.", size=int(36)) as credits_text11_line4 at credits_text11_line4_pos zorder 10 with dissolve


        $ renpy.pause(2)

        show text Text("Помните!", size=int(36)) as credits_text11_line5 at credits_text11_line5_pos zorder 10 with dissolve

        $ renpy.pause(0.5)

        show text Text("Лишнее самоубийство не нужно никому!", size=int(36)) as credits_text11_line6 at credits_text11_line6_pos zorder 10 with dissolve

        $ renpy.pause(10)

    jump after_credits

label after_credits:



    if player_skipped_credits:

        stop music_crossfade fadeout 1.0

        hide credits_bkg1
        hide credits_sprite1

        hide credits_bkg2
        hide credits_sprite2

        hide hotelroom3_2
        hide hotelroom3_2a

        hide credits_bkg4
        hide credits_sprite4

        hide credits_bkg5
        hide credits_sprite5

        hide credits_bkg6
        hide credits_sprite6

        hide credits_bkg7
        

        hide credits_text1_line1

        hide credits_text1_line2

        hide credits_text1_line3

        hide credits_text1_line4

        hide credits_text1_line5

        hide credits_text1_line7

        hide credits_text10_line1

        hide credits_text10_line2

        hide credits_text10_line3


        hide credits_text11_line1

        hide credits_text11_line2

        hide credits_text11_line311
        hide credits_text11_line312
        hide credits_text11_line321
        hide credits_text11_line322
        hide credits_text11_line331
        hide credits_text11_line332

        hide credits_text11_line4

        hide credits_text11_line5

        hide credits_text11_line6


        $ player_skipped_credits = False # return the original value back



    else:


        if _preferences.language == None:

            stop music_crossfade fadeout 5.0

            hide credits_text11_line1 with dissolve

            hide credits_text11_line2 with dissolve

            hide credits_text11_line311 with dissolve
            hide credits_text11_line312 with dissolve
            hide credits_text11_line321 with dissolve
            hide credits_text11_line322 with dissolve
            hide credits_text11_line331 with dissolve
            hide credits_text11_line332 with dissolve

            hide credits_text11_line4 with dissolve

            hide credits_text11_line5 with dissolve

            hide credits_text11_line6 with dissolve

        else:
            stop music_crossfade fadeout 3.0

            hide credits_text10_line1 with dissolve

            hide credits_text10_line2 with dissolve

            hide credits_text10_line3 with dissolve


    hide credits_bkg7 with dissolve

    $ quick_menu = True
    $ show_say_menu = True

    return

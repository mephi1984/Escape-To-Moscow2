
define msg_vertical_spacing = 4

default var_dialog_stack = {'chatWithNoName' : [], 'chatWithCoach' : [], 'chatRoomEscape' : [], 'chatWithAliya': []}

default var_current_dialog = 'chatWithNoName'

transform phoneTransitionAppearLeft(new_ypos):
    yanchor 0.0
    xanchor 0.0
    xpos 1296
    ypos new_ypos
    zoom 0.0
    linear 0.2 zoom 1.0

transform phoneTransitionNoneLeft(new_ypos):
    yanchor 0.0
    xanchor 0.0
    xpos 1296
    ypos new_ypos

transform phoneTransitionAppearRight(new_ypos):
    xpos 1296 + 240
    yanchor 0.0
    xanchor 1.0
    ypos new_ypos
    zoom 0.0
    linear 0.2 zoom 1.0

transform phoneTransitionNoneRight(new_ypos):
    xpos 1296 + 240
    yanchor 0.0
    xanchor 1.0
    ypos new_ypos

transform phoneTransitionBottomAppearLeft(new_ypos, h):
    xpos 1296
    xanchor 0.0
    yanchor 0.0
    ypos new_ypos - h
    zoom 0.0
    linear 0.2 zoom 1.0

transform phoneTransitionBottomNoneLeft(new_ypos, h):
    xpos 1296
    xanchor 0.0
    yanchor 1.0
    ypos new_ypos

transform phoneTransitionBottomMoveUpLeft(new_ypos, h):
    xpos 1296
    xanchor 0.0
    yanchor 1.0
    ypos new_ypos + h
    linear 0.2 ypos new_ypos

transform phoneTransitionBottomAppearRight(new_ypos, h):
    xpos 1296 + 240
    xanchor 1.0
    yanchor 0.0
    ypos new_ypos - h
    zoom 0.0
    linear 0.2 zoom 1.0

transform phoneTransitionBottomNoneRight(new_ypos, h):
    xpos 1296 + 240
    xanchor 1.0
    yanchor 1.0
    ypos new_ypos


transform phoneTransitionBottomMoveUpRight(new_ypos, h):
    xpos 1296 + 240
    xanchor 1.0
    yanchor 1.0
    ypos new_ypos + h
    linear 0.2 ypos new_ypos

init python:

    #global lang
    global var_message_bubbles



    var_message_bubbles = {
            'ru' : {'noName' : [], 'noName_promo' : [], 'noName_forwarded_right' : [], 'aliya_forwarded_right' : [], 'me' : [], 'coach' : [], 'me_with_title_photo' : [], 'coach_with_title' : [], 'yarik_with_title' : [], 'lawyer_with_title' : [], 'roma_with_title' : [], 'roma_with_title_photo' : [], 'roma_with_title_voice' : [], 'aliya' : [], 'aliya_with_title' : []},
            'en' : {'noName' : [], 'noName_promo' : [], 'noName_forwarded_right' : [], 'aliya_forwarded_right' : [], 'me' : [], 'coach' : [], 'me_with_title_photo' : [], 'coach_with_title' : [], 'yarik_with_title' : [], 'lawyer_with_title' : [], 'roma_with_title' : [], 'roma_with_title_photo' : [], 'roma_with_title_voice' : [], 'aliya' : [], 'aliya_with_title' : []}
        }
    #global msg_vertical_spacing

    #msg_vertical_spacing = 16
    #msg_vertical_spacing = 0

    global msg_margin
    #msg_margin = 6
    msg_margin = 9

    global msg_frame_size
    msg_frame_size = 6

    global msg_area_start_x
    msg_area_start_x = 1298.0

    global msg_area_start_y
    msg_area_start_y = 316

    global msg_area_width
    msg_area_width = 236.0

    global msg_area_height
    msg_area_height = 360

    global msg_xmaximum
    msg_xmaximum = 190

    # 1296 316 start new

    # 364 - total height
    # 240 - total width


    # side: 0 is left, 1 is right

    # Quick hack:
    order = ['en', 'en']

    if _preferences.language != 'english':
        order = ['ru', 'ru']

    for lg in order:

        for i in range(len(var_character_messages[lg]['aliya'])):
            t = Text(var_character_messages[lg]['aliya'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_left.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['aliya'].append(phonebubble)
            renpy.image("aliya_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['noName'])):
            t = Text(var_character_messages[lg]['noName'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_left.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['noName'].append(phonebubble)
            renpy.image("noName_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['coach'])):
            t = Text(var_character_messages[lg]['coach'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_left.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['coach'].append(phonebubble)
            renpy.image("coach_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['me'])):
            t = Text(var_character_messages[lg]['me'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_right.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['me'].append(phonebubble)
            renpy.image("me_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['me_with_title_photo'])):
            phonebubble = Composite(
                (200, 227),  # Размер изображения
                (0, 0), "messenger/me_photo.png",  # Фоновое изображение
            )
            var_message_bubbles[lg]['me_with_title_photo'].append(phonebubble)
            renpy.image("me_with_title_photo_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['noName_forwarded_right'])):
            title = "{color=#45A32D}Пересланное сообщение от: No Name:{/color}\n"
            if lg == 'en':
                title = "{color=#45A32D}Forwarded message from: No Name:{/color}\n"

            t = Text(title + var_character_messages[lg]['noName_forwarded_right'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_right.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['noName_forwarded_right'].append(phonebubble)
            renpy.image("noName_forwarded_right_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['aliya_forwarded_right'])):
            title = "{color=#856F5D}Пересланное сообщение от: А.Г.:{/color}\n"
            if lg == 'en':
                title = "{color=#856F5D}Forwarded message from: A.G.:{/color}\n"

            t = Text(title + var_character_messages[lg]['aliya_forwarded_right'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_right.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['aliya_forwarded_right'].append(phonebubble)
            renpy.image("aliya_forwarded_right_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['coach_with_title'])):
            title = "{color=#007F46}Напарник:{/color}\n"
            if lg == 'en':
                title = "{color=#007F46}Mate:{/color}\n"

            t = Text(title + var_character_messages[lg]['coach_with_title'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_left.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['coach_with_title'].append(phonebubble)
            renpy.image("coach_with_title_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['yarik_with_title'])):
            title = "{color=#687DC9}Ярик:{/color}\n"
            if lg == 'en':
                title = "{color=#687DC9}Yarik:{/color}\n"

            t = Text(title + var_character_messages[lg]['yarik_with_title'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_left.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['yarik_with_title'].append(phonebubble)
            renpy.image("yarik_with_title_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['aliya_with_title'])):
            title = "{color=#856F5D}А.Г.:{/color}\n"
            if lg == 'en':
                title = "{color=#856F5D}A.G.:{/color}\n"
                
            t = Text(title + var_character_messages[lg]['aliya_with_title'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_left.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['aliya_with_title'].append(phonebubble)
            renpy.image("aliya_with_title_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['lawyer_with_title'])):
            t = Text("{color=#0094FF}Alex Law:{/color}\n" + var_character_messages[lg]['lawyer_with_title'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_left.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['lawyer_with_title'].append(phonebubble)
            renpy.image("lawyer_with_title_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['noName_promo'])):
            t = Text(var_character_messages[lg]['noName_promo'][i], size=28, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_left.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['noName_promo'].append(phonebubble)
            renpy.image("noName_promo_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['roma_with_title'])):
            title = "{color=#C03D33}Рома:{/color}\n"
            if lg == 'en':
                title = "{color=#C03D33}Roma:{/color}\n"
            t = Text(title + var_character_messages[lg]['roma_with_title'][i], size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Fixed(g, Frame("msg_left.png", msg_frame_size, msg_frame_size), g, xmaximum=msg_xmaximum, fit_first=True, xfit=True, yfit=True)
            var_message_bubbles[lg]['roma_with_title'].append(phonebubble)
            renpy.image("roma_with_title_bubble" + str(i), phonebubble)

        for i in range(len(var_character_messages[lg]['roma_with_title_photo'])):
            title = "{color=#C03D33}Рома:{/color}\n"
            if lg == 'en':
                title = "{color=#C03D33}Roma:{/color}\n"
            
            t = Text(title, size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Composite(
                (200, 227),  # Размер изображения
                (0, 0), "messenger/roma_photo.png",  # Фоновое изображение
                (msg_margin, msg_margin), t
            )
            var_message_bubbles[lg]['roma_with_title_photo'].append(phonebubble)
            renpy.image("roma_with_title_photo_bubble" + str(i), phonebubble)
        
        for i in range(len(var_character_messages[lg]['roma_with_title_voice'])):
            title = "{color=#C03D33}Рома:{/color}\n"
            if lg == 'en':
                title = "{color=#C03D33}Roma:{/color}\n"
            
            t = Text(title, size=16, color="#000000", layout="subtitle")
            g = Grid(1, 1, t, xmargin=msg_margin, ymargin=msg_margin)
            phonebubble = Composite(
                (200, 66),  # Размер изображения
                (0, 0), "messenger/voice_message.png",  # Фоновое изображение
                (msg_margin, msg_margin), t
            )
            var_message_bubbles[lg]['roma_with_title_voice'].append(phonebubble)
            renpy.image("roma_with_title_voice_bubble" + str(i), phonebubble)


    def addMessage(chr, msg):

        var_current_dialog_stack = var_dialog_stack[var_current_dialog]

        lxg = 'ru'

        if _preferences.language == 'english':
            lxg = 'en'

        msgIndex = -1
        try:
            msgIndex = var_character_messages[lxg][chr].index(msg)

            h = 0

            if chr == 'roma_with_title_photo':
                h = 227
            elif chr == 'me_with_title_photo':
                h = 227
            elif chr == 'roma_with_title_voice':
                h = 66
            else: 
                h = renpy.render(var_message_bubbles[lxg][chr][msgIndex], 1920, 1080, 0, 0).get_size()[1]

            totalHeight = 0

            for i in range(len(var_dialog_stack[var_current_dialog])):
                totalHeight = totalHeight + var_dialog_stack[var_current_dialog][i]['height']

            var_dialog_stack[var_current_dialog].append({'character' : chr, 'index' : msgIndex, 'height' : h + msg_vertical_spacing})

            #del var_dialog_stack[var_current_dialog][var_message_count_chatWithNoName+1:]

            totalHeight = totalHeight + h

            if totalHeight > msg_area_height + 300: # height of screen plus some extra
                dialogMessage = var_dialog_stack[var_current_dialog][0]
                renpy.hide(dialogMessage['character'] + "_bubble" + str(dialogMessage['index']))
                renpy.with_statement(None)
                var_dialog_stack[var_current_dialog].pop(0)
        except ValueError:
            msgIndex = -1
            return


    def drawCurrentMessageStack(force_no_transition=False):
        totalHeight = 0

        rangeLen = len(var_dialog_stack[var_current_dialog])

        for i in range(rangeLen):
            totalHeight = totalHeight + var_dialog_stack[var_current_dialog][i]['height']

        totalHeightExceptLast = 0

        if rangeLen > 0:
            for i in range(rangeLen-1):
                totalHeightExceptLast = totalHeightExceptLast + var_dialog_stack[var_current_dialog][i]['height']



        if totalHeight < msg_area_height: # start rendering from top
            ypos = msg_area_start_y

            for i in range(rangeLen):
                dialogMessage = var_dialog_stack[var_current_dialog][i]



                if (dialogMessage['character'] == 'me') or (dialogMessage['character'] == 'me_with_title') or (dialogMessage['character'] == 'me_with_title_photo') or (dialogMessage['character'] == 'noName_forwarded_right') or (dialogMessage['character'] == 'aliya_forwarded_right'):

                    if renpy.in_rollback():
                        transitionFunc = phoneTransitionNoneRight
                    elif renpy.get_skipping():
                        transitionFunc = phoneTransitionNoneRight
                    elif force_no_transition:
                        transitionFunc = phoneTransitionNoneRight
                    else:
                        if i == rangeLen-1:
                            transitionFunc = phoneTransitionAppearRight
                        else:
                            transitionFunc = phoneTransitionNoneRight
                else:
                    if renpy.in_rollback():
                        transitionFunc = phoneTransitionNoneLeft
                    elif renpy.get_skipping():
                        transitionFunc = phoneTransitionNoneLeft
                    elif force_no_transition:
                        transitionFunc = phoneTransitionNoneLeft
                    else:
                        if i == rangeLen-1:
                            transitionFunc = phoneTransitionAppearLeft
                        else:
                            transitionFunc = phoneTransitionNoneLeft

                pos = Position(xpos=(msg_area_start_x/1920.0), xanchor=0.0, ypos=ypos/1080.0, yanchor=0.0)
                renpy.show(dialogMessage['character'] + "_bubble" + str(dialogMessage['index']), tag="chat_bubble" + str(i), at_list=[transitionFunc(int(ypos))], zorder=15)
                renpy.with_statement(None)

                ypos = ypos + dialogMessage['height']
        else:
            ypos = msg_area_start_y + msg_area_height

            littleSpaceDiff = 0

            if totalHeightExceptLast < msg_area_height:
                littleSpaceDiff = msg_area_height - totalHeightExceptLast + msg_vertical_spacing
            else:
                littleSpaceDiff = 0

            lastBoxHeight = var_dialog_stack[var_current_dialog][rangeLen-1]['height']

            for i in reversed(range(rangeLen)):
                dialogMessage = var_dialog_stack[var_current_dialog][i]

                dh = 0

                if i == rangeLen-1:
                    dh = lastBoxHeight - msg_vertical_spacing
                else:
                    dh = lastBoxHeight - littleSpaceDiff

                if (dialogMessage['character'] == 'me') or (dialogMessage['character'] == 'me_with_title') or (dialogMessage['character'] == 'me_with_title_photo') or (dialogMessage['character'] == 'noName_forwarded_right') or (dialogMessage['character'] == 'aliya_forwarded_right'):

                    if renpy.in_rollback():
                        transitionBottomFunc = phoneTransitionBottomNoneRight
                    elif renpy.get_skipping():
                        transitionBottomFunc = phoneTransitionBottomNoneRight
                    elif force_no_transition:
                        transitionBottomFunc = phoneTransitionBottomNoneRight
                    else:
                        if i == rangeLen-1:
                            transitionBottomFunc = phoneTransitionBottomAppearRight
                            #dh = lastBoxHeight - msg_vertical_spacing
                        else:
                            transitionBottomFunc = phoneTransitionBottomMoveUpRight
                            #dh = lastBoxHeight - littleSpaceDiff
                else:
                    if renpy.in_rollback():
                        transitionBottomFunc = phoneTransitionBottomNoneLeft
                    elif renpy.get_skipping():
                        transitionBottomFunc = phoneTransitionBottomNoneLeft
                    elif force_no_transition:
                        transitionBottomFunc = phoneTransitionBottomNoneLeft
                    else:
                        if i == rangeLen-1:
                            transitionBottomFunc = phoneTransitionBottomAppearLeft
                            #dh = lastBoxHeight - msg_vertical_spacing
                        else:
                            transitionBottomFunc = phoneTransitionBottomMoveUpLeft
                            #dh = lastBoxHeight - littleSpaceDiff

                pos = Position(xpos = (msg_area_start_x/1920.0), xanchor=0.0, ypos=ypos/1080.0, yanchor=1.0)
                renpy.show(dialogMessage['character'] + "_bubble" + str(dialogMessage['index']), tag="chat_bubble" + str(i), at_list=[transitionBottomFunc(int(ypos), int(dh))], zorder=15)
                renpy.with_statement(None)

                ypos = ypos - dialogMessage['height']

    def clearMessages():
        for i in range(100):
            renpy.hide("chat_bubble" + str(i))
            renpy.with_statement(None)

    def phoneSayAliya(message, force_no_transition=False):
        addMessage('aliya', message)
        clearMessages()
        drawCurrentMessageStack(force_no_transition)
        global lastPhoneMsg
        lastPhoneMsg = message

    def phoneSayNoName(message, force_no_transition=False):
        addMessage('noName', message)
        clearMessages()
        drawCurrentMessageStack(force_no_transition)
        global lastPhoneMsg
        lastPhoneMsg = message


    def phoneSayNoNamePromo(message):
        renpy.transition(None)
        addMessage('noName_promo', message)
        clearMessages()
        drawCurrentMessageStack()


    def phoneSayNoNameForwardedRight(message, force_no_transition=False):
        addMessage('noName_forwarded_right', message)
        clearMessages()
        drawCurrentMessageStack(force_no_transition)
        global lastPhoneMsg
        lastPhoneMsg = message


    def phoneSayAliyaForwardedRight(message, force_no_transition=False):
        addMessage('aliya_forwarded_right', message)
        clearMessages()
        drawCurrentMessageStack(force_no_transition)
        global lastPhoneMsg
        lastPhoneMsg = message


    def phoneSayCoach(message):
        renpy.transition(None)
        addMessage('coach', message)
        clearMessages()
        drawCurrentMessageStack()
        global lastPhoneMsg
        lastPhoneMsg = message
        #renpy.say(noName, message)
        #renpy.with_statement(dissolve)
        #renpy.transition(None)
        #noName(message)
        #renpy.with_statement(dissolve)

    def phoneSayMe(message):
        #renpy.transition(None)

        addMessage('me', message)
        drawCurrentMessageStack()
        global lastPhoneMsg
        lastPhoneMsg = message
        #renpy.say(me, message)
        #renpy.with_statement(dissolve)

    def phoneSayMePhoto():
        renpy.transition(None)
        addMessage('me_with_title_photo', "")
        clearMessages()
        drawCurrentMessageStack()

    def phoneSayCoachWithTitle(message, force_no_transition=False):
        #renpy.transition(None)
        addMessage('coach_with_title', message)
        clearMessages()
        drawCurrentMessageStack(force_no_transition)
        global lastPhoneMsg
        lastPhoneMsg = message

    def phoneSayYarikWithTitle(message, force_no_transition=False):
        #renpy.transition(None)
        addMessage('yarik_with_title', message)
        clearMessages()
        drawCurrentMessageStack(force_no_transition)
        global lastPhoneMsg
        lastPhoneMsg = message

        #addMessage('noName_forwarded_right', message)
        #clearMessages()
        #drawCurrentMessageStack(force_no_transition)
        #global lastPhoneMsg
        #lastPhoneMsg = message

    
    def phoneSayAliyaWithTitle(message, force_no_transition=False):
        renpy.transition(None)
        addMessage('aliya_with_title', message)
        drawCurrentMessageStack(force_no_transition)
        global lastPhoneMsg
        lastPhoneMsg = message

    def phoneSayLawyerWithTitle(message, force_no_transition=False):
        #renpy.transition(None)
        addMessage('lawyer_with_title', message)
        clearMessages()
        drawCurrentMessageStack(force_no_transition)
        global lastPhoneMsg
        lastPhoneMsg = message

    def phoneSayRomaWithTitle(message):
        renpy.transition(None)
        addMessage('roma_with_title', message)
        drawCurrentMessageStack()
        global lastPhoneMsg
        lastPhoneMsg = message
        
    def phoneSayRomaPhoto():
        renpy.transition(None)
        addMessage('roma_with_title_photo', "")
        clearMessages()
        drawCurrentMessageStack()

    def phoneSayRomaVoice():
        renpy.transition(None)
        addMessage('roma_with_title_voice', "")
        clearMessages()
        drawCurrentMessageStack()


    def switchChatToCoach():
        global var_current_dialog

        var_current_dialog = 'chatWithCoach'

    def switchChatToEscapeRoom():
        global var_current_dialog

        var_current_dialog = 'chatRoomEscape'

    def switchChatToNoName():
        global var_current_dialog

        var_current_dialog = 'chatWithNoName'

    def switchChatToAliya():
        global var_current_dialog
        var_current_dialog = 'chatWithAliya'


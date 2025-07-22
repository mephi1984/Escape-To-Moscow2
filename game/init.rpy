
define any_center_pos = Position(xpos = 0.5, xanchor=0.5, ypos=1.0, yanchor=1.0)

define any_left_pos = Position(xpos = 0.33, xanchor=0.5, ypos=1.0, yanchor=1.0)

define any_right_pos = Position(xpos = 0.66, xanchor=0.5, ypos=1.0, yanchor=1.0)

define any_far_left_pos = Position(xpos = 0.2, xanchor=0.5, ypos=1.0, yanchor=1.0)

define any_far_right_pos = Position(xpos = 0.8, xanchor=0.5, ypos=1.0, yanchor=1.0)

define me = Character(_('Семён'), color="#f0f0f0")

define messenger = Character(_('Messenger'), color="#40A7E3")

define coach = Character(_('Напарник'), color="#007F46")

define milana = Character(_('Милана'), color="#007F46")

define aliya = Character(_('Алия'), color="#856F5D")

define noName = Character(_('No Name'), color="#E17076")

define yarik = Character(_('Ярик'), color="#687DC9")

define taxiDriver = Character(_('Таксист'), color="#F0F080")

define roma = Character(_('Рома'), color="#A59E8C")

define announcement = Character(_('Объявление'), color="#ff4040")

define radio = Character(_('Радио'), color="#ff4040")

define pilot = Character(_('Николай'), color="#40A7E3")

define police_arstan = Character(_('Арстан'), color="#0094FF")

define costya = Character(_('Костя'), color="#FE4E0D")

define dag = Character(_('Дагестанец'), color="#adadad")

define hobo = Character(_('Бездомный'), color="#9e7317")

define photoman = Character(_('Фотограф'), color="#ff4040")

define lawyer = Character(_('Адвокат'), color="#0094FF")


define cg_screen_phone_pos = Position(xalign=1.0, yalign=0.5)

default branch1_day1_step1_taxi_asked = False
default branch1_day1_step1_offroad_asked = False

define isMobileWeb = True

image movie_plane = Movie(stop_music=False, loop = False, play = "video/output_vp9_2.webm")

image movie_plane_landing = Movie(stop_music=False, loop = False, play = "video/output_vp9.webm")


image splash = "splash.png"

label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)


    if not persistent.lang_chosen:
            $ persistent.lang_chosen = True
            call screen language_and_difficulty_menu_first_time

    return

init python:
    renpy.music.register_channel("music_crossfade","music",loop=True,tight=True)
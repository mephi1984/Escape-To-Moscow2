import glob, os

import re

output = """# This file is auto generated. Do not modify!
# See script generateMessengerMessages.py for details

init -1 python:

    global var_character_messages

    var_character_messages = {
        'ru' : {'noName' : [], 'noName_promo' : [], 'noName_forwarded_right' : [], 'aliya_forwarded_right' : [], 'me' : [], 'coach' : [], 'me_with_title_photo' : [], 'coach_with_title' : [], 'yarik_with_title' : [], 'lawyer_with_title' : [], 'roma_with_title' : [], 'roma_with_title_photo' : [], 'roma_with_title_voice' : [], 'aliya' : [], 'aliya_with_title' : []},
        'en' : {'noName' : [], 'noName_promo' : [], 'noName_forwarded_right' : [], 'aliya_forwarded_right' : [], 'me' : [], 'coach' : [], 'me_with_title_photo' : [], 'coach_with_title' : [], 'yarik_with_title' : [], 'lawyer_with_title' : [], 'roma_with_title' : [], 'roma_with_title_photo' : [], 'roma_with_title_voice' : [], 'aliya' : [], 'aliya_with_title' : []}
    }
"""


def create_translation_dict(file_path):
    """
    Читает файл .rpy и создает словарь из пар old/new,
    корректно обрабатывая экранированные кавычки (\").

    Args:
        file_path (str): Путь к файлу.

    Returns:
        dict: Словарь, где ключи - это значения 'old',
              а значения - соответствующие 'new'.
    """
    translations = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Обновленное выражение для обработки экранированных кавычек
            # Оно ищет последовательность символов, которая либо не является кавычкой,
            # либо является экранированной кавычкой.
            pattern = re.compile(r'old\s+"((?:\\"|[^"])*)"\s+new\s+"((?:\\"|[^"])*)"', re.DOTALL)
            matches = pattern.findall(content)
            
            for old_text, new_text in matches:
                translations[old_text] = new_text
                
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {file_path}")
        return None
        
    return translations




os.chdir("game")


translationDict = create_translation_dict('tl/english/messenger_messages2.rpy')

# Some workaround:
translationDict['Да'] = 'Yes'

print("count is")
print(len(translationDict))

for file in glob.glob("*.rpy"):
    print(file)

    textfile = open(file, 'r', encoding="utf8")
    filetext = textfile.read()
    textfile.close()


    phoneSayMeMatches = re.findall("\$ phoneSayMe\(__\(\"(.+)\"\)\)", filetext)

    for match in phoneSayMeMatches:
        print(match)
        output += ("    var_character_messages['ru']['me'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['me'].append(\"" + translationDict[match] + "\")\n\n")

    phoneSayAliyaMatches = re.findall("\$ phoneSayAliya\(__\(\"(.+?)\".*\)\)", filetext)

    for match in phoneSayAliyaMatches:
        print(match)
        output += ("    var_character_messages['ru']['aliya'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['aliya'].append(\"" + translationDict[match] + "\")\n\n")

    phoneSayNoNameMatches = re.findall("\$ phoneSayNoName\(__\(\"(.+?)\".*\)\)", filetext)

    for match in phoneSayNoNameMatches:
        print(match)
        output += ("    var_character_messages['ru']['noName'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['noName'].append(\"" + translationDict[match] + "\")\n\n")

    phoneSayNoNamePromoMatches = re.findall("\$ phoneSayNoNamePromo\(\"(.+)\"\)", filetext)

    for match in phoneSayNoNamePromoMatches:
        print(match)
        output += ("    var_character_messages['ru']['noName_promo'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['noName_promo'].append(\"" + translationDict[match] + "\")\n\n")



    phoneSayNoNameForwardedRightMatches = re.findall("\$ phoneSayNoNameForwardedRight\(__\(\"(.+?)\".*\)\)", filetext)

    for match in phoneSayNoNameForwardedRightMatches:
        print(match)
        output += ("    var_character_messages['ru']['noName_forwarded_right'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['noName_forwarded_right'].append(\"" + translationDict[match] + "\")\n\n")


    phoneSayAliyaForwardedRightMatches = re.findall("\$ phoneSayAliyaForwardedRight\(__\(\"(.+?)\".*\)\)", filetext)

    for match in phoneSayAliyaForwardedRightMatches:
        print(match)
        output += ("    var_character_messages['ru']['aliya_forwarded_right'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['aliya_forwarded_right'].append(\"" + translationDict[match] + "\")\n\n")



    phoneSayCoachMatches = re.findall("\$ phoneSayCoach\(__\(\"(.+?)\".*\)\)", filetext)

    for match in phoneSayCoachMatches:
        print(match)
        output += ("    var_character_messages['ru']['coach'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['coach'].append(\"" + translationDict[match] + "\")\n\n")


    phoneSayMePhotoMatches = re.findall("\$ phoneSayMePhoto\(\)", filetext)

    for match in phoneSayMePhotoMatches:
        print("????"+match)
        output += ("    var_character_messages['ru']['me_with_title_photo'].append(_(\"\"))\n\n")
        output += ("    var_character_messages['en']['me_with_title_photo'].append(\"\")\n\n")


    phoneSayCoachWithTitleMatches = re.findall("\$ phoneSayCoachWithTitle\(__\(\"(.+)\".*\)\)", filetext)

    for match in phoneSayCoachWithTitleMatches:
        print(match)
        output += ("    var_character_messages['ru']['coach_with_title'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['coach_with_title'].append(\"" + translationDict[match] + "\")\n\n")



    phoneSayYarikWithTitleMatches = re.findall("\$ phoneSayYarikWithTitle\(__\(\"(.+)\".*\)\)", filetext)

    for match in phoneSayYarikWithTitleMatches:
        print(match)
        output += ("    var_character_messages['ru']['yarik_with_title'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['yarik_with_title'].append(\"" + translationDict[match] + "\")\n\n")

    phoneSayAliyaWithTitleMatches = re.findall("\$ phoneSayAliyaWithTitle\(__\(\"(.+)\"\)\)", filetext)

    for match in phoneSayAliyaWithTitleMatches:
        print(match)
        output += ("    var_character_messages['ru']['aliya_with_title'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['aliya_with_title'].append(\"" + translationDict[match] + "\")\n\n")


    phoneSayLawyerWithTitleMatches = re.findall("\$ phoneSayLawyerWithTitle\(__\(\"(.+)\"\)\)", filetext)

    for match in phoneSayLawyerWithTitleMatches:
        print(match)
        output += ("    var_character_messages['ru']['lawyer_with_title'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['lawyer_with_title'].append(\"" + translationDict[match] + "\")\n\n")


    phoneSayRomaWithTitleMatches = re.findall("\$ phoneSayRomaWithTitle\(__\(\"(.+)\"\)\)", filetext)

    for match in phoneSayRomaWithTitleMatches:
        print(match)
        output += ("    var_character_messages['ru']['roma_with_title'].append(_(\"" + match + "\"))\n\n")
        output += ("    var_character_messages['en']['roma_with_title'].append(\"" + translationDict[match] + "\")\n\n")

    phoneSayRomaPhotoMatches = re.findall("\$ phoneSayRomaPhoto\(\)", filetext)

    for match in phoneSayRomaPhotoMatches:
        print("!!!!!"+match)
        output += ("    var_character_messages['ru']['roma_with_title_photo'].append(_(\"\"))\n\n")
        output += ("    var_character_messages['en']['roma_with_title_photo'].append(\"\")\n\n")

    phoneSayRomaVoiceMatches = re.findall("\$ phoneSayRomaVoice\(\)", filetext)

    for match in phoneSayRomaVoiceMatches:
        print("!!!!!"+match)
        output += ("    var_character_messages['ru']['roma_with_title_voice'].append(_(\"\"))\n\n")
        output += ("    var_character_messages['en']['roma_with_title_voice'].append(\"\")\n\n")




text_file = open("messenger_messages2.rpy", "w", encoding="utf8")
text_file.write(output)
text_file.close()


os.system('pause')

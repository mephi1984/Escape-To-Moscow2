import re
import os
import argparse

def swap_translation_lines(input_file_path):
    """
    Считывает rpy-файл, меняет местами текст в кавычках
    в последовательных строках 'old' и 'new' и записывает
    результат в новый файл в той же директории.

    Args:
        input_file_path (str): Путь к исходному файлу.
    """
    # Проверяем, существует ли файл
    if not os.path.isfile(input_file_path):
        print(f"❌ Ошибка: Файл '{input_file_path}' не найден или не является файлом.")
        return

    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        return

    processed_lines = []
    i = 0
    # Регулярное выражение для поиска текста внутри кавычек
    pattern = re.compile(r'"(.*?)"')

    while i < len(lines):
        current_line = lines[i]
        
        # Ищем строку, начинающуюся с 'old' (с учетом отступов)
        if current_line.strip().startswith('old '):
            # Проверяем, есть ли следующая строка и начинается ли она с 'new'
            if (i + 1) < len(lines) and lines[i + 1].strip().startswith('new '):
                next_line = lines[i + 1]

                # Извлекаем текст из кавычек
                old_text_match = pattern.search(current_line)
                new_text_match = pattern.search(next_line)

                if old_text_match and new_text_match:
                    old_text = old_text_match.group(1)
                    new_text = new_text_match.group(1)

                    # Создаем новые строки, меняя текст местами
                    swapped_old_line = current_line.replace(f'"{old_text}"', f'"{new_text}"')
                    swapped_new_line = next_line.replace(f'"{new_text}"', f'"{old_text}"')

                    processed_lines.append(swapped_old_line)
                    processed_lines.append(swapped_new_line)

                    i += 2
                    continue

        processed_lines.append(current_line)
        i += 1

    # === Логика создания выходного файла в той же директории ===
    try:
        # Получаем директорию и имя файла из исходного пути
        directory = os.path.dirname(input_file_path)
        filename = os.path.basename(input_file_path)
        
        # Создаем новое имя файла
        name_part, extension = os.path.splitext(filename)
        output_filename = f"{name_part}_swapped{extension}"
        
        # Собираем полный путь к выходному файлу
        output_file_path = os.path.join(directory, output_filename)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)
        print(f"✅ Обработка завершена. Результат сохранен в: {output_file_path}")

    except Exception as e:
        print(f"❌ Ошибка при записи файла: {e}")


def main():
    """
    Основная функция для парсинга аргументов командной строки.
    """
    parser = argparse.ArgumentParser(
        description="Меняет местами строки перевода 'old' и 'new' в .rpy файле Ren'Py.",
        epilog="Пример использования: python swap_translator.py game/tl/russian/screens.rpy"
    )
    
    parser.add_argument(
        'filepath',
        type=str,
        help='Путь к исходному .rpy файлу.'
    )
    
    args = parser.parse_args()
    swap_translation_lines(args.filepath)


if __name__ == '__main__':
    main()
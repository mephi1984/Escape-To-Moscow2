import re
import os
import argparse

def copy_old_to_new(input_file_path: str):
    """
    Считывает rpy-файл, находит пары строк 'old' и 'new' и копирует
    текст из кавычек строки 'old' в строку 'new', заменяя её содержимое.
    Результат сохраняется в новый файл.

    Args:
        input_file_path (str): Путь к исходному файлу.
    """
    # Проверка на существование файла
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
    pattern = re.compile(r'"(.*?)"')

    while i < len(lines):
        current_line = lines[i]
        
        # Поиск пары строк old/new
        if current_line.strip().startswith('old '):
            if (i + 1) < len(lines) and lines[i + 1].strip().startswith('new '):
                next_line = lines[i + 1]

                old_text_match = pattern.search(current_line)
                new_text_match = pattern.search(next_line)

                if old_text_match and new_text_match:
                    old_text = old_text_match.group(1)
                    new_text = new_text_match.group(1)

                    # === Основное изменение логики ===
                    # Строка 'old' остаётся без изменений.
                    # В строке 'new' заменяем её текст на текст из 'old'.
                    copied_new_line = next_line.replace(f'"{new_text}"', f'"{old_text}"')

                    processed_lines.append(current_line) # Добавляем неизменённую 'old' строку
                    processed_lines.append(copied_new_line)  # Добавляем изменённую 'new' строку

                    i += 2
                    continue

        # Если пара не найдена, просто добавляем текущую строку
        processed_lines.append(current_line)
        i += 1
    
    # --- Сохранение результата ---
    try:
        directory = os.path.dirname(input_file_path)
        filename = os.path.basename(input_file_path)
        
        name_part, extension = os.path.splitext(filename)
        # Меняем суффикс выходного файла на _copied
        output_filename = f"{name_part}_copied{extension}"
        
        output_file_path = os.path.join(directory, output_filename)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)
        print(f"✅ Обработка завершена. Результат сохранен в: {output_file_path}")

    except Exception as e:
        print(f"❌ Ошибка при записи файла: {e}")


def main():
    """
    Парсинг аргументов командной строки.
    """
    parser = argparse.ArgumentParser(
        description="Копирует текст из строк 'old' в строки 'new' в .rpy файле Ren'Py.",
        epilog="Пример: python copy_translator.py game/tl/russian/screens.rpy"
    )
    
    parser.add_argument(
        'filepath',
        type=str,
        help='Путь к исходному .rpy файлу.'
    )
    
    args = parser.parse_args()
    copy_old_to_new(args.filepath)


if __name__ == '__main__':
    main()
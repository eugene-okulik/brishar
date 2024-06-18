import os
import argparse


def find_text_in_file(file_path, text):
    results = []
    with open(file_path, 'r', encoding='utf-8') as file:
        # Проходим по строкам файла, начиная нумерацию с 1
        for line_number, line in enumerate(file, 1):
            if text in line:
                words = line.split()
                # Находим индекс необходимого слова
                word_idx = next(
                    i for i, word in enumerate(words) if text in word)

                # Определяем радиус контекста и находим индексы слов для среза
                context_radius = 5
                start_index = max(0, word_idx - context_radius)
                end_index = min(len(words), word_idx + context_radius + 1)

                # Объединяем слова
                context = ' '.join(words[start_index:end_index])

                # Добавляем результат в список
                results.append((file_path, line_number, context))
    return results


def search_logs(directory, text):
    all_results = []
    # Проходим по всем подкаталогам и файлам в указанной директории
    for root, _, files in os.walk(directory):
        for file in files:  # Проходим по каждому файлу в текущем каталоге
            file_path = os.path.join(root, file)  # Формируем путь к файлу

            # Ищем текст в текущем файле и добавляем найденное в общий список
            all_results.extend(find_text_in_file(file_path, text))
    return all_results


def main():
    # Создаем парсер аргументов командной строки с описанием
    parser = argparse.ArgumentParser(
        description='Log analyzer for searching text in log files.')
    parser.add_argument('directory',
                        help='The directory containing log files')
    parser.add_argument('--text', required=True,
                        help='The text to search for in the log files')
    # Парсим аргументы командной строки
    args = parser.parse_args()

    directory = args.directory  # Получаем значение директории из аргументов
    text = args.text  # Получаем значение текста для поиска из аргументов

    # Проверяем, существует ли указанная директория
    if not os.path.isdir(directory):
        print(
            f"The specified directory {directory} does not exist.")
        return

    results = search_logs(directory, text)  # Выполняем поиск текста в логах

    if results:
        for file_path, line_number, context in results:
            print(f'Found in {file_path} on line {line_number}: {context}')
    else:
        print("No matches found.")


if __name__ == '__main__':  # Проверяем, запущен ли скрипт напрямую
    main()

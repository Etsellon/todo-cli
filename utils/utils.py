import json
import os

path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tasks.json')


def load_tasks(filename=path_to_json) -> list[dict] | list:
    if not os.path.exists(filename):
        open(filename, 'w').close()
    return json_to_dict_list() or []


def save_tasks(tasks: list[dict] | list) -> None:
    dict_list_to_json(tasks)


def dict_list_to_json(dict_list, filename=path_to_json):
    """
        Преобразует список словарей в JSON-строку и сохраняет её в файл.

        :param dict_list: Список словарей
        :param filename: Имя файла для сохранения JSON-строки
        :return: JSON-строка или None в случае ошибки
        """
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"error: {e}")


def json_to_dict_list(filename=path_to_json):
    """
        Преобразует JSON-строку из файла в список словарей.

        :param filename: Имя файла с JSON-строкой
        :return: Список словарей или None в случае ошибки
        """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            json_str = f.read()
            dict_list = json.loads(json_str)
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(f"error: {e}")

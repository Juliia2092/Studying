import json
"""Есть некоторый словарь, который хранит названия
стран и столиц. Название страны используется в качестве
ключа, название столицы в качестве значения. Необходимо
реализовать: добавление данных, удаление данных, поиск
данных, редактирование данных, сохранение и загрузку
данных (используя упаковку и распаковку)."""


countries = {
    'Гватемала': 'Гватемала',
    'Куба': 'Гавана',
    'Аргентина': 'Буенос-Айрес',
    'Бельгія': 'Брюссель'}


def add_new_item(storage: dict, **kwargs):
    key = kwargs.get('key')
    value = kwargs.get('value')
    storage[key] = value


def del_item(storage: dict, **kwargs):
    key = kwargs.get('key')
    storage.pop(key)
    return storage


def find(storage: dict, **kwargs):
    key = kwargs.get('key')
    return storage.get(key)


def change_item(storage: dict, **kwargs):
    key = kwargs.get('key')
    value = kwargs.get('value')
    storage[key] = value


def save_storage(**kwargs):
    file_name = kwargs.get('file_name')
    storage = kwargs.get('storage')
    if file_name and storage:
        with open(file_name, 'w', encoding='utf-8') as fw:
            fw.write(json.dumps(storage, ensure_ascii=False, indent=2))
            return 'Storage written successfully'
    else:
        return f'There is no argument {"file_name" if not kwargs.get("file_name") else None}'\
               f'{"storage" if not kwargs.get("storage") else None }'


def get_data(file_name):
    with open(file_name, 'r') as fr:
        data = fr.read()
        return json.loads(data)


print(countries)
print(add_new_item(countries, key="Франция", value='Париж'))
print(del_item(countries, key='Куба'))
print(find(countries, key='Аргентина'))
change_item(countries, key='Украина', value='Киев')
print(countries)
save_storage(file_name='test.json', storage=countries)
countries = get_data('test.json')


"""Есть некоторый словарь, который хранит названия
музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
альбомов в качестве значения. Необходимо реализовать:
добавление данных, удаление данных, поиск данных,
редактирование данных, сохранение и загрузку данных
(используя упаковку и распаковку)."""
musical_library = {'Queen': 'A night in the Opera',
                   'Scorpions': 'Unbreakable',
                   'Poets of the Fall': 'Carnival of Rust',
                   'System of a Down': 'Toxicity',
                   'In this Moment': 'Black Widow'}


def add_group(storage: dict, **kwargs):
    key = kwargs.get('key')
    value = kwargs.get('value')
    storage[key] = value


def delete_group(storage: dict, **kwargs):
    key = kwargs.get('key')
    storage.pop(key)
    return storage


def find_group(storage: dict, **kwargs):
    key = kwargs.get('key')
    return storage.get(key)


def change_group(storage: dict, **kwargs):
    key = kwargs.get('key')
    value = kwargs.get('value')
    storage[key] = value


def save_storage(**kwargs):
    file_name = kwargs.get('file_name')
    storage = kwargs.get('storage')
    if file_name and storage:
        with open(file_name, 'w', encoding='utf-8') as fw:
            fw.write(json.dumps(storage, ensure_ascii=False, indent=2))
            return 'Storage written successfully'
    else:
        return f'There is no argument {"file_name" if not kwargs.get("file_name") else None}'\
               f'{"storage" if not kwargs.get("storage") else None }'


def get_data(file_name):
    with open(file_name, 'r') as fr:
        data = fr.read()
        return json.loads(data)


print(musical_library)
print(add_group(musical_library, key='Blondie', value='The Curse of Blondie'))
print(delete_group(musical_library, key='In this Moment'))
print(find_group(musical_library, key='Poets of the Fall'))
change_group(musical_library, key='Guano Apes', value=' Walking on a Thin Line')
save_storage(file_name='groups.json', storage=musical_library)
musical_library = get_data('groups.json')

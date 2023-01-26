import json


def load_data():
    content = ""
    with open('categories.json', 'r', encoding='utf-8') as f:
        content = f.read()
    # print(content)
    categories = json.loads(content)
    content = ""
    with open('sub_categories.json', 'r', encoding='utf-8') as f:
        content = f.read()
    # print(content)
    sub_categories = json.loads(content)
    return categories, sub_categories


def get_sub_categories(sub_categories, parent_id=1):
    str1 = "Выберите тему для общения: \n"
    num = 1
    for sub_category in sub_categories:
        if sub_category['parent_id'] == parent_id:
            str1 = str1 + f"{sub_category['id']} - {sub_category['name']} \n"

    return str1

def get_categories(categories):
    str1 = "Выберите категорию тем для общения: \n"
    for category in categories:
        str1 = str1 + f"{category['id']} {category['name']} - {category['desc']} \n"
    return str1

def get_desc(sub_categories, id):
    for sub_category in sub_categories:
        if sub_category['id'] == id:
            return sub_category['desc']
    


if __name__ == "__main__":
    categories, sub_categories = load_data()
    str1 = get_categories(categories)
    print(str1)
    parent_id  = int(input("Введите номер катергории: "))
    str1 = get_sub_categories(sub_categories, parent_id)
    print(str1)
    id  = int(input("Введите номер темы для общения: "))
    data = get_desc(sub_categories, id)
    print(data)
    for item in data:
        desc = item[0]
        img = item[1]
        print(f"{desc} - {img}")
        
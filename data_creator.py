categories = []
item_cat1={}
item_cat1["id"]= 1
item_cat1["name"]= "Хобби"
item_cat1["desc"]= "Ваши увлечения"
categories.append(item_cat1)
item_cat2={}
item_cat2["id"]= 2
item_cat2["name"]= "Домашние животные"
item_cat2["desc"]= "Увлечения с вашими любимцами"
categories.append(item_cat2)
import json
jsonstring = json.dumps(categories, ensure_ascii=False)
with open('categories.json', 'w+', encoding='utf-8') as f:
    f.write(jsonstring)
    
sub_categories = []
item_sub_cat1={}
item_sub_cat1["id"]= 1
item_sub_cat1["parent_id"]= 1
item_sub_cat1["name"]= "Коллекционирование марок"
item_sub_cat1["desc"]= "История и оценки марок"
sub_categories.append(item_sub_cat1)
item_sub_cat2={}
item_sub_cat2["id"]= 2
item_sub_cat2["parent_id"]= 1
item_sub_cat2["name"]= "Философия"
item_sub_cat2["desc"]= "Обсуждают материалы по философии"
sub_categories.append(item_sub_cat2)
import json
jsonstring = json.dumps(sub_categories, ensure_ascii=False)
with open('sub_categories.json', 'w+', encoding='utf-8') as f:
    f.write(jsonstring)

import wikipediaapi

user_agent = 'Beasts Parser'
wiki_wiki = wikipediaapi.Wikipedia(user_agent, 'ru')
page = wiki_wiki.page('Категория:Животные_по_алфавиту')

output_dict = {
    'А': 0, 'Б': 0, 'В': 0, 'Г': 0, 'Д': 0, 'Е': 0, 'Ж': 0, 'З': 0, 'И': 0,
    'К': 0, 'Л': 0, 'М': 0, 'Н': 0, 'О': 0, 'П': 0, 'Р': 0, 'С': 0, 'Т': 0,
    'У': 0, 'Ф': 0, 'Х': 0, 'Ц': 0, 'Ч': 0, 'Ш': 0, 'Щ': 0, 'Э': 0, 'Ю': 0,
    'Я': 0
}

for value in page.categorymembers.values():
    if value.namespace == wikipediaapi.Namespace.MAIN:
        first_letter = str(value)[0]
        if first_letter in output_dict:
            output_dict[first_letter] += 1

with open('beasts.csv', 'w') as file:
    for key, value in output_dict.items():
        file.writelines(f'{key},{value}\n')

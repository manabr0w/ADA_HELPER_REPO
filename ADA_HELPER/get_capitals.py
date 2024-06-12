import json

def get_capital():
    with open('countries_and_capitals.json', 'r', encoding='utf-8') as file:
        countries_and_capitals = json.load(file)

    while True:
        country = input("Введіть назву країни: ")
        capital = countries_and_capitals.get(country)

        if capital:
            print(f"Столиця {country} — {capital}.")
            break
        else:
            print(f"Вибачте, інформація про столицю країни {country} відсутня. Будь ласка, спробуйте ще раз.")


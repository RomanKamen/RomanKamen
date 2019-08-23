import random

from GameEngine.settings import CARD_RACES
from GameEngine.database import CardModel, session

pres = {
    'Обычный': 0,
    'Уверенный': 1,
    'Злой': 2,
    'Бешенный': 3
}

races = CARD_RACES

posts = [
    {

        'name': 'Лесник',
        'hp': 4,
        'dmg': 3
    },
    {
        'name':'Охотник',
        'hp': 3,
        'dmg': 4
    },
    {
        'name':'Воин',
        'hp': 4,
        'dmg': 5
    }
]

for pre_k, pre_v in pres.items():
    for race_k, race_v in races.items():
        for post in posts:
            dmg = pre_v + post['dmg']
            hp = pre_v + post['hp']
            manacost = hp
            name = f"{pre_k} {race_v} {post['name']}"
            card = CardModel(name=name, race=race_k,
                             hp=hp, damage=dmg,
                             armor=random.randint(0, hp),
                             manacost=manacost)
            session.add(card)
            session.commit()

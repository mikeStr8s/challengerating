import json


def extract_monster_json():
    with open('C:\\Users\\stratimh\\Documents\\docker\\challengerating\\app\\api\\5e_monsters.json', 'r') as f:
        return json.load(f)

def extract_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def parse_monsters():
    monsters = extract_monster_json()
    unique_attrs = set()
    all_values = dict()
    for monster in monsters:
        for key, value in monster.items():
            unique_attrs.add(key)
            try:
                values = all_values[key]
                values.append(value)
                values = list(set(values))
                all_values[key] = values
            except KeyError:
                all_values[key] = [ value ]
    
    for key, values in all_values.items():
        with open('app\\api\\json\\{0}.json'.format(key), 'w') as f:
            json.dump(values, f)
    with open('monster_attrs.json', 'w') as monster_attrs_file:
        json.dump(list(unique_attrs), monster_attrs_file)


def parse_armor_class():
    armor_class = extract_json('app\\api\\json\\Armor Class.json')
    for ac in armor_class:
        value = ac.strip()  # Remove leading and trailing whitespace
        try:
            int(value)
        except ValueError:
            print(value)
        




if __name__ == "__main__":
    parse_armor_class()

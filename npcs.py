import random

class Creature:
    def __init__(self, name, hp, max_hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack

class Player(Creature):
    def __init__(self, name="чел"):
        self.name = name
        self.hp = 20
        self.max_hp = 20
        self.attack = 10
        self.lv = 19
        self.gold = 0
        self.inventory = ["легендарный гирой", "стейк-лицо", "кусок пирага"]
        self.is_pacifist = False

    def show_stats(self):
        print("\n--- " + self.name + " левел " + str(self.lv) + " ---")
        print("хп: " + str(self.hp) + "/" + str(self.max_hp))
        if self.inventory:
            print("рюкзак: " + ", ".join(self.inventory))
        else:
            print("рюкзак: пуста!")
        print("--------------------")

    def heal(self, amount, item_name):
        self.hp = self.hp + amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print("\n ты сьел " + item_name + " и востановил " + str(amount) + " хп!!!")
        print("щас хп: " + str(self.hp) + "/" + str(self.max_hp))

    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "lv": self.lv,
            "inventory": self.inventory
        }

    def load_dict(self, data):
        self.name = data["name"]
        self.hp = data["hp"]
        self.max_hp = data["max_hp"]
        self.lv = data["lv"]
        self.inventory = data["inventory"]


class Sans(Creature):
    def __init__(self):
        self.name = "санс"
        self.hp = 1
        self.max_hp = 1
        self.attack = 6
        self.dodges_left = 5
        self.betrayal_phase = False

    def get_attack_phrase(self):
        phrases = [
            "санс пускает бластеры!!! пиу пиу лазеры везде!!",
            "санс зделал синию гравитацию и ты летиш на кости!",
            "летять синие и оранживые кости уворачивайся давай"
        ]
        return random.choice(phrases)

    def talk(self):
        if self.dodges_left > 3:
            return "санс говорит: поют птички цвитут цветы... кароче крутой день"
        elif self.dodges_left > 1:
            return "санс говорит: в такие дни дети как ты... ДОЛЖНЫ ГОРЕТЬ В АДУ!!!"
        else:
            return "санс говорит: ппц ты упрямый мелкий"
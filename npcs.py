import random

class Player:
    def __init__(self):
        self.name = "Фриск"
        self.hp = 20
        self.max_hp = 20
        self.inventory = ["кусок пирога", "легендарный герой", "тягучий ирис"]

    def show_stats(self):
        print(f"\n--- {self.name} | HP: {self.hp}/{self.max_hp} ---")

    def heal(self, amount, item_name):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"Ты съел {item_name} и восстановил {amount} HP!")

    def to_dict(self):
        return {"name": self.name, "hp": self.hp, "inventory": self.inventory}

    def load_dict(self, data):
        self.name = data.get("name", self.name)
        self.hp = data.get("hp", self.hp)
        self.inventory = data.get("inventory", self.inventory)


class Sans:
    def __init__(self):
        self.hp = 1
        self.attack = 5
        self.dodges_left = 4

    def talk(self):
        return "говорит: 'какой прекрасный день на улице... птички поют, цветы благоухают...'"

    def get_attack_phrase(self):
        phrases = [
            "Санс включает гастер-бластеры! *ВЖУУУХ*",
            "Синие кости летят в твою сторону! Замри!",
            "Санс швыряет твою душу об стену коридора!"
        ]
        return random.choice(phrases)
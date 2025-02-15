
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"
    



# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        self.health=health
        self.strength=strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

    def attack(self):
        return super().attack()


def attack(self):
    return super().attack() 


# War

class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def addViking(self, viking):
        self.viking_army.append(viking)

    def addSaxon(self, saxon):
        self.saxon_army.append(saxon)

    # Resto del código del método vikingAttack, saxonAttack y showStatus

import random

    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = viking.attack()
        result = saxon.receiveDamage(damage)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = saxon.attack()
        result = viking.receiveDamage(damage)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


# esta útlima de war no me sale, pero no me da la cabeza para resolverlo. Prometo resolverlo!!!
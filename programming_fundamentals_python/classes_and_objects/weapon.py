class Weapon:

    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            output = "shooting..."
        else:
            output = f"no bullets left"

        return output
    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)

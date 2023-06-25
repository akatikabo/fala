class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def display_info(self):
        print(f"Ems: {self.name}")
        print(f"Level: {self.level}")


class Player(Character):
    def __init__(self, name, level, profession):
        super().__init__(name, level)
        self.profession = profession
    
    def display_info(self):
        super().display_info()
        print(f"Profession: {self.profession}")


class NonPlayer(Character):
    def __init__(self, name, level, role):
        super().__init__(name, level)
        self.role = role
    
    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")


# Create player and non-player characters
player = Player("The Chosen One", 20, "Vault Dweller")
npc = NonPlayer("Marcus", 15, "Super Mutant")

# Display information about the characters
print("Player Character:")
player.display_info()
print("\nNon-Player Character:")
npc.display_info()

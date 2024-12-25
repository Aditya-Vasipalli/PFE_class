import random
from character_creation import create_character
from combat_system import win_or_loss
from enemies import select_enemy, display_enemy_details, adjust_enemy_stats
from Menu import main_menu

def main():
    print("Welcome to the RPG Game!")
    character = create_character()
    
    # Main storyline logic
    start_quest(character, main_menu)

def start_quest(character, main_menu_callback, current_position=(0, 0)):
    while True:
        if character.hp <= 0:
            game_over(character)
            break
        print("You are summoned by the king.")
        print("King: Our kingdom is in grave danger. An ancient dragon has awakened and threatens our land.")
        print("King: Brave hero, will you accept the quest to defeat the dragon and save our kingdom?")
        choice = input("Do you accept the quest? (yes/no/menu): ")
        
        if choice.lower() == "yes":
            print("King: Thank you, brave hero. Your journey begins now.")
            traverse_paths(character, main_menu_callback, current_position)
        elif choice.lower() == "no":
            print("King: I understand. The kingdom's fate is uncertain without your help.")
            break
        elif choice.lower() == "menu":
            main_menu_callback(character, current_position)
        else:
            print("Invalid choice. Please select again.")

def traverse_paths(character, main_menu_callback, current_position):
    # Define the matrix representing the paths
    paths = [
        ["village", "market", "forest", "cave", "mountain"],
        ["hidden_treasure", "wise_old_man", "deeper_forest", "river", "abandoned_castle"],
        ["return_to_king", "swamp", "dragon_lair", "dark_forest", "haunted_village"],
        ["desert", "oasis", "ancient_ruins", "volcano", "ice_cave"],
        ["plains", "fortress", "enchanted_forest", "wizard_tower", "final_battle"]
    ]
    
    descriptions = {
        "village": "A peaceful village with friendly villagers.",
        "market": "A bustling market with various items for sale.",
        "forest": "A dense forest filled with wild creatures.",
        "hidden_treasure": "A hidden treasure rumored to be nearby.",
        "wise_old_man": "A wise old man who offers guidance.",
        "deeper_forest": "A deeper part of the forest with more dangers.",
        "return_to_king": "Return to the king to report your progress.",
        "dragon_lair": "The lair of the ancient dragon.",
        "cave": "A dark cave with unknown dangers.",
        "mountain": "A tall mountain with treacherous paths.",
        "river": "A flowing river with hidden secrets.",
        "abandoned_castle": "An abandoned castle with eerie silence.",
        "swamp": "A murky swamp with hidden creatures.",
        "dark_forest": "A dark forest with unknown dangers.",
        "haunted_village": "A village haunted by spirits.",
        "desert": "A vast desert with scorching heat.",
        "oasis": "A refreshing oasis in the desert.",
        "ancient_ruins": "Ruins of an ancient civilization.",
        "volcano": "An active volcano with molten lava.",
        "ice_cave": "A cold ice cave with slippery paths.",
        "plains": "Wide open plains with tall grass.",
        "fortress": "A heavily guarded fortress.",
        "enchanted_forest": "A magical forest with enchanted creatures.",
        "wizard_tower": "A tall tower where a powerful wizard resides.",
        "final_battle": "The final battle against the ancient dragon."
    }
    
    while True:
        if character.hp <= 0:
            game_over(character)
            break
        x, y = current_position
        location = paths[x][y]
        
        if location == "village":
            village_path(character)
        elif location == "market":
            visit_market(character)
        elif location == "forest":
            explore_forest(character)
        elif location == "hidden_treasure":
            find_hidden_treasure(character)
        elif location == "wise_old_man":
            visit_wise_old_man(character)
        elif location == "deeper_forest":
            deeper_forest(character)
        elif location == "return_to_king":
            return_to_king(character)
        elif location == "dragon_lair":
            dragon_lair(character)
        elif location == "cave":
            explore_cave(character)
        elif location == "mountain":
            climb_mountain(character)
        elif location == "river":
            explore_river(character)
        elif location == "abandoned_castle":
            explore_castle(character)
        elif location == "swamp":
            explore_swamp(character)
        elif location == "dark_forest":
            explore_dark_forest(character)
        elif location == "haunted_village":
            explore_haunted_village(character)
        elif location == "desert":
            explore_desert(character)
        elif location == "oasis":
            explore_oasis(character)
        elif location == "ancient_ruins":
            explore_ruins(character)
        elif location == "volcano":
            explore_volcano(character)
        elif location == "ice_cave":
            explore_ice_cave(character)
        elif location == "plains":
            explore_plains(character)
        elif location == "fortress":
            explore_fortress(character)
        elif location == "enchanted_forest":
            explore_enchanted_forest(character)
        elif location == "wizard_tower":
            explore_wizard_tower(character)
        elif location == "final_battle":
            final_battle(character)
        
        print("\nWhat would you like to do next?")
        if y < len(paths[0]) - 1 and paths[x][y + 1] is not None:
            print(f"1. Move Right to {paths[x][y + 1]}: {descriptions[paths[x][y + 1]]}")
        if x < len(paths) - 1 and paths[x + 1][y] is not None:
            print(f"2. Move Down to {paths[x + 1][y]}: {descriptions[paths[x + 1][y]]}")
        if y > 0 and paths[x][y - 1] is not None:
            print(f"3. Move Left to {paths[x][y - 1]}: {descriptions[paths[x][y - 1]]}")
        if x > 0 and paths[x - 1][y] is not None:
            print(f"4. Move Up to {paths[x - 1][y]}: {descriptions[paths[x - 1][y]]}")
        print("5. Exit to Main Menu")
        print("6. Manage Inventory")
        choice = input("Select an option: ")

        if choice == '1' and y < len(paths[0]) - 1 and paths[x][y + 1] is not None:
            current_position = (x, y + 1)
        elif choice == '2' and x < len(paths) - 1 and paths[x + 1][y] is not None:
            current_position = (x + 1, y)
        elif choice == '3' and y > 0 and paths[x][y - 1] is not None:
            current_position = (x, y - 1)
        elif choice == '4' and x > 0 and paths[x - 1][y] is not None:
            current_position = (x - 1, y)
        elif choice == '5':
            main_menu_callback(character, current_position)
        elif choice == '6':
            manage_inventory(character)
        else:
            print("Invalid choice or move out of bounds. Please select again.")

def manage_inventory(character):
    while True:
        character.inventory.show_inventory()
        print("1. Equip Item")
        print("2. Use Item")
        print("3. Back to Game")
        choice = input("Select an option: ")

        if choice == '1':
            try:
                index = int(input("Enter the index of the item you want to equip: "))
                character.inventory.equip_item(index)
            except ValueError:
                print("Invalid input. Please enter a valid index.")
        elif choice == '2':
            try:
                index = int(input("Enter the index of the item you want to use: "))
                character.inventory.use_item(index, character)
            except ValueError:
                print("Invalid input. Please enter a valid index.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select again.")

def village_path(character):
    print("You arrive at the village. The villagers tell you about a hidden treasure and a wise old man in the forest.")
    random_encounter(character)

def visit_market(character):
    print("You find various items for sale in the market.")
    print(f"Merchant: Welcome, traveler! Take a look at my wares. You have {character.money} gold.")
    while True:
        print("\nItems for sale:")
        print("1. Health Potion - 50 gold")
        print("2. Mana Potion - 50 gold")
        print("3. Sword - 100 gold")
        print("4. Shield - 100 gold")
        print("5. Return to the village")
        choice = input("Select an option: ")

        if choice == '1' and character.money >= 50:
            print("You bought a Health Potion.")
            character.money -= 50
            character.inventory.add_item("Health Potion")
        elif choice == '2' and character.money >= 50:
            print("You bought a Mana Potion.")
            character.money -= 50
            character.inventory.add_item("Mana Potion")
        elif choice == '3' and character.money >= 100:
            print("You bought a Sword.")
            character.money -= 100
            character.inventory.add_item("Sword")
        elif choice == '4' and character.money >= 100:
            print("You bought a Shield.")
            character.money -= 100
            character.inventory.add_item("Shield")
        elif choice == '5':
            break
        else:
            print("Invalid choice or insufficient funds. Please select again.")

def explore_forest(character):
    print("You venture into the forest.")
    random_encounter(character)

def find_hidden_treasure(character):
    print("You search for the hidden treasure.")
    print("After a long search, you find a chest hidden in the ground.")
    print("You open the chest and find a powerful weapon.")
    character.inventory.add_item("Powerful Weapon")

def visit_wise_old_man(character):
    print("Wise Old Man: Greetings, traveler. I have been expecting you.")
    print("Wise Old Man: I can offer you guidance and a powerful artifact to aid you in your quest.")
    print("You receive a magical amulet from the wise old man.")
    character.inventory.add_item("Magical Amulet")
    print("Wise Old Man: I will also teach you a new skill.")
    new_skill = random.choice(["Fireball", "Heal", "Lightning Strike"])
    character.skills.append(new_skill)
    print(f"You have learned a new skill: {new_skill}")

def deeper_forest(character):
    print("You follow the path deeper into the forest.")
    random_encounter(character)

def return_to_king(character):
    print("You return to the king and report your progress.")

def dragon_lair(character):
    print("You enter the dragon's lair and prepare for the final battle.")
    enemy_name = "Dragon"
    enemy = select_enemy(enemy_name)
    if enemy:
        level = character.level  # Match enemy level to character level
        adjust_enemy_stats(enemy, level)
        display_enemy_details(enemy)
        result = win_or_loss(character, enemy)
        print(result)
        if character.hp > 0:
            character.check_level_up()  # Check for level up immediately after the battle
    else:
        print("Enemy not found.")

def random_encounter(character):
    enemies = ["Goblin", "Orc", "Wolf", "Troll", "Bandit", "Skeleton", "Zombie", "Vampire", "Werewolf", "Giant Spider"]
    enemy_name = random.choice(enemies)
    enemy = select_enemy(enemy_name)
    if enemy:
        level = character.level  # Match enemy level to character level
        adjust_enemy_stats(enemy, level)
        display_enemy_details(enemy)
        result = win_or_loss(character, enemy)
        print(result)
        if character.hp > 0:
            character.money += random.randint(10, 50)  # Reward money for defeating the enemy
            print(f"You have earned some gold. Current gold: {character.money}")
            character.check_level_up()  # Check for level up immediately after the battle
    else:
        print("Enemy not found.")

def game_over(character):
    print(f"{character.name} has died. Game Over.")
    exit()

# Additional exploration functions for new locations
def explore_cave(character):
    print("You explore the dark cave.")
    random_encounter(character)

def climb_mountain(character):
    print("You climb the treacherous mountain.")
    random_encounter(character)

def explore_river(character):
    print("You explore the flowing river.")
    random_encounter(character)

def explore_castle(character):
    print("You explore the abandoned castle.")
    random_encounter(character)

def explore_swamp(character):
    print("You explore the murky swamp.")
    random_encounter(character)

def explore_dark_forest(character):
    print("You explore the dark forest.")
    random_encounter(character)

def explore_haunted_village(character):
    print("You explore the haunted village.")
    random_encounter(character)

def explore_desert(character):
    print("You explore the vast desert.")
    random_encounter(character)

def explore_oasis(character):
    print("You explore the refreshing oasis.")
    random_encounter(character)

def explore_ruins(character):
    print("You explore the ancient ruins.")
    random_encounter(character)

def explore_volcano(character):
    print("You explore the active volcano.")
    random_encounter(character)

def explore_ice_cave(character):
    print("You explore the cold ice cave.")
    random_encounter(character)

def explore_plains(character):
    print("You explore the wide open plains.")
    random_encounter(character)

def explore_fortress(character):
    print("You explore the heavily guarded fortress.")
    random_encounter(character)

def explore_enchanted_forest(character):
    print("You explore the magical enchanted forest.")
    random_encounter(character)

def explore_wizard_tower(character):
    print("You explore the tall wizard tower.")
    random_encounter(character)

def final_battle(character):
    print("You prepare for the final battle against the ancient dragon.")
    dragon_lair(character)

if __name__ == "__main__":
    main()
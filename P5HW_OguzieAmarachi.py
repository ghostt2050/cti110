# Oguzie Amarachi
# Date:4-20-2025
# Assignment: Character Creation Game
# This program simulates a character creation game using functions, dictionaries, and user interaction.

import random

# Value-returning function to create a character
def create_character():
    name = input("Enter character name: ")
    health = int(input("Enter health points: "))
    attack = int(input("Enter attack points: "))
    defense = int(input("Enter defense points: "))

    character = {
        "Name": name,
        "Health": health,
        "Attack": attack,
        "Defense": defense
    }
    return character

# Non-value returning function to display a character
def display_character(character):
    print("\nCharacter Details:")
    for key, value in character.items():
        print(f"{key}: {value}")

# Value-returning function: battle simulation
def battle(character1, character2):
    print(f"\n⚔️ {character1['Name']} is attacking {character2['Name']}!")
    damage = character1["Attack"] - character2["Defense"]
    damage = damage if damage > 0 else 0
    character2["Health"] -= damage
    print(f"{character2['Name']} took {damage} damage! Remaining Health: {character2['Health']}")

# Value-returning function: healing event
def find_potion(character):
    heal = random.randint(5, 15)
    character["Health"] += heal
    print(f"\n🧪 {character['Name']} found a healing potion and gained {heal} HP! New Health: {character['Health']}")

# Main function - does not return or take any parameters
def main():
    characters = []
    while True:
        print("\n=== Character Creation Game Menu ===")
        print("1. Create new character")
        print("2. Display all characters")
        print("3. Simulate battle between 2 characters")
        print("4. Random event (find potion)")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            new_char = create_character()
            characters.append(new_char)
        elif choice == '2':
            for char in characters:
                display_character(char)
        elif choice == '3':
            if len(characters) >= 2:
                display_character(characters[0])
                display_character(characters[1])
                battle(characters[0], characters[1])
            else:
                print("⚠️ Need at least 2 characters to simulate a battle.")
        elif choice == '4':
            if characters:
                find_potion(random.choice(characters))
            else:
                print("⚠️ No characters available.")
        elif choice == '5':
            print("👋 Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Run the main function
main()

input()

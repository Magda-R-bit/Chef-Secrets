import json

with open("recipes.json", "r") as file:
    recipes = json.load(file)


def add_new_secret():
    """
    Adds new recipe to the recipe book
    """
    name = input("Enter the recipe name: ").strip()
    ingredients = [ingredient.strip() for ingredient in input("Enter ingredients separated by comas: ").split(",")]
    instructions = [instructions.strip() for instruction in input("Enter instructions: ").split(",")]

    # Add new recipe to the dictionary
    recipes[name] = {"Ingredients": ingredients, "Instructions": instructions}

    #Write updated dictionary back to json file
    with open("recipes.json", "w") as file:
        json.dump(recipes, file, indent=4)
    print(f"Recipe '{name}' added successfully.")



def search_secret_recipe():
    """
    Searching for a recipe
    """

    
    name = input("Enter the recipe name to search: ").strip()
    if name in recipes:
        print(f"\nRecipe for {name}:")
        print("Ingredients:", ", ".join(recipes[name]["Ingredients"]))
        print("Instructions:", ", ".join(recipes[name]["Instructions"]))
    else:
        print(f"'{name}' not found.")


def display_all_recipes():
    """
    Displays all recipes stored in recipe book
    """

    if recipes:
        print("\nAvailable recipes:")
        for recipe_name in recipes:
            print(f"- {recipe_name}")
    else:
        print("No recipes available.")




def main():
    """
    Main function to display options and handle user choices
    """

    while True:
        print("\nOptions:")
        print("1. Add a new secret recipe")
        print("2. Search for a secret recipe")
        print("3. Display all recipes")
        print("4. Exit")

        choice = input("Choose one option: ")
        if choice == "1":
            add_new_secret()
        elif choice == "2":
            search_secret_recipe()
        elif choice == "3":
            display_all_recipes()#

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Call the main function

if __name__ == "__main__":
    main()

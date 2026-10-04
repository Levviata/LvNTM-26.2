import json
from pathlib import Path

# Folder containing this Python script
folder = Path(__file__).parent

empty_recipe = {
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
        "minecraft:structure_void"
    ],
    "result": {
        "id": "minecraft:barrier"
    }
}

total_recipes = 0
empty_recipes = 0

for file in folder.glob("*.json"):
    try:
        with file.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if data == empty_recipe:
            empty_recipes += 1
            continue

        total_recipes += 1

    except (json.JSONDecodeError, OSError) as e:
        print(f"Skipped {file.name}: {e}")

print(f"Recipes found: {total_recipes}")
print(f"Empty recipes ignored: {empty_recipes}")
print(f"Total JSON files: {total_recipes + empty_recipes}")

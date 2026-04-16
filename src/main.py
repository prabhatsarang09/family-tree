import sys
from src.services.family_tree import FamilyTree
from src.models.person import Person
from src.utils.parser import parse_line


def initialize_family(tree):
    # King Arthur family base (minimal setup)

    king = Person("KingArthur", "Male")
    queen = Person("QueenMargaret", "Female")

    king.spouse = queen
    queen.spouse = king

    tree.add_person(king)
    tree.add_person(queen)

    # Children of King Arthur
    tree.add_child("QueenMargaret", "Bill", "Male")
    tree.add_child("QueenMargaret", "Charlie", "Male")
    tree.add_child("QueenMargaret", "Percy", "Male")
    tree.add_child("QueenMargaret", "Ronald", "Male")
    tree.add_child("QueenMargaret", "Ginerva", "Female")

    # Add spouses
    tree.add_spouse("Bill", "Flora", "Female")
    tree.add_spouse("Charlie", "Audrey", "Female")
    tree.add_spouse("Percy", "Alice", "Female")
    tree.add_spouse("Ronald", "Helen", "Female")
    tree.add_spouse("Ginerva", "Harry", "Male")

    # Next generation
    tree.add_child("Flora", "Victoire", "Female")
    tree.add_child("Flora", "Dominique", "Female")

    tree.add_child("Audrey", "Molly", "Female")
    tree.add_child("Audrey", "Lucy", "Female")

    tree.add_child("Alice", "Hugo", "Male")
    tree.add_child("Alice", "Rose", "Female")

    tree.add_child("Helen", "James", "Male")
    tree.add_child("Helen", "Albus", "Male")
    tree.add_child("Helen", "Lily", "Female")


def process_input(file_path):
    tree = FamilyTree()
    initialize_family(tree)

    with open(file_path) as f:
        for line in f:
            parts = parse_line(line)

            if not parts:
                continue

            if parts[0] == "ADD_CHILD":
                _, mother, child, gender = parts
                print(tree.add_child(mother, child, gender))

            elif parts[0] == "GET_RELATIONSHIP":
                _, name, relation = parts
                result = tree.get_relationship(name, relation)
                print(" ".join(result))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
    else:
        process_input(sys.argv[1])
        
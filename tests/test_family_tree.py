from src.services.family_tree import FamilyTree
from src.models.person import Person


def test_add_child_success():
    tree = FamilyTree()

    mother = Person("Jane", "Female")
    tree.add_person(mother)

    result = tree.add_child("Jane", "Tom", "Male")

    assert result == "CHILD_ADDED"


def test_add_child_person_not_found():
    tree = FamilyTree()

    result = tree.add_child("Unknown", "Tom", "Male")

    assert result == "PERSON_NOT_FOUND"


def test_get_relationship_none():
    tree = FamilyTree()

    person = Person("John", "Male")
    tree.add_person(person)

    result = tree.get_relationship("John", "Siblings")

    assert result == ["NONE"]
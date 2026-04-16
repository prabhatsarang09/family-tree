from src.models.person import Person


class FamilyTree:
    def __init__(self):
        self.members = {}

    def add_person(self, person):
        self.members[person.name] = person

    def get_person(self, name):
        return self.members.get(name)

    def add_spouse(self, person1_name, person2_name, gender):
        person1 = self.get_person(person1_name)
        if not person1:
            return

        person2 = Person(person2_name, gender)
        person1.spouse = person2
        person2.spouse = person1

        self.add_person(person2)

    # -----------------------
    # ADD CHILD
    # -----------------------
    def add_child(self, mother_name, child_name, gender):
        mother = self.get_person(mother_name)

        if not mother:
            return "PERSON_NOT_FOUND"

        if mother.gender != "Female":
            return "CHILD_ADDITION_FAILED"

        child = Person(child_name, gender)
        father = mother.spouse

        child.mother = mother
        child.father = father

        mother.children.append(child)

        if father:
            father.children.append(child)

        self.add_person(child)

        return "CHILD_ADDED"

    # -----------------------
    # RELATIONSHIPS
    # -----------------------

    def get_siblings(self, person):
        if not person.mother:
            return []

        return [
            child.name
            for child in person.mother.children
            if child.name != person.name
        ]

    def get_sisters(self, person):
        return [
            name for name in self.get_siblings(person)
            if self.get_person(name).gender == "Female"
        ]

    def get_brothers(self, person):
        return [
            name for name in self.get_siblings(person)
            if self.get_person(name).gender == "Male"
        ]

    def get_sons(self, person):
        return [c.name for c in person.children if c.gender == "Male"]

    def get_daughters(self, person):
        return [c.name for c in person.children if c.gender == "Female"]

    def get_maternal_uncle(self, person):
        if not person.mother:
            return []
        return self.get_brothers(person.mother)

    def get_maternal_aunt(self, person):
        if not person.mother:
            return []
        return self.get_sisters(person.mother)

    def get_paternal_uncle(self, person):
        if not person.father:
            return []
        return self.get_brothers(person.father)

    def get_paternal_aunt(self, person):
        if not person.father:
            return []
        return self.get_sisters(person.father)

    # -----------------------
    # DISPATCHER
    # -----------------------
    def get_relationship(self, name, relation):
        person = self.get_person(name)

        if not person:
            return ["PERSON_NOT_FOUND"]

        relation_map = {
            "Siblings": self.get_siblings,
            "Sister": self.get_sisters,
            "Brother": self.get_brothers,
            "Son": self.get_sons,
            "Daughter": self.get_daughters,
            "Maternal-Uncle": self.get_maternal_uncle,
            "Maternal-Aunt": self.get_maternal_aunt,
            "Paternal-Uncle": self.get_paternal_uncle,
            "Paternal-Aunt": self.get_paternal_aunt,
        }

        if relation not in relation_map:
            return ["NONE"]

        result = relation_map[relation](person)

        return result if result else ["NONE"]
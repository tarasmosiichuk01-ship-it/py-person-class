class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]
    for person_dict in people:
        person_name = person_dict["name"]
        current_person = Person.people[person_name]
        if person_dict.get("wife") is not None:
            partner = Person.people[person_dict["wife"]]
            current_person.wife = partner
            partner.husband = current_person
        if person_dict.get("husband") is not None:
            partner = Person.people[person_dict["husband"]]
            current_person.husband = partner
            partner.wife = current_person

    return result

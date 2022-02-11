import dataclasses

from pipelined import *


person = ProxyObject()

Male = True
Female = False


@dataclasses.dataclass(frozen=True)
class Person:
    first_name: str
    last_name: str
    age: int
    sex: bool


people = [
    Person("John", "Doe", 23, Male),
    Person("Alex", "Black", 45, Male),
    Person("Judy", "Doe", 18, Female),
    Person("Katelyn", "Doe", 12, Female),
    Person("Marta", "White", 16, Female),
    Person("John", "Black", 87, Male),
    Person("Katelyn", "Doe", 32, Female),
]


adult_does = (
    people
    | where((person.age >= 18) & (person.last_name == "Doe"))
    | order_by(person.age)
)

print(*adult_does, sep='\n')

oldest_doe: Person = (
    people
    | where(person.last_name == "Doe")
    | max_by(person.age)
)

print(oldest_doe)

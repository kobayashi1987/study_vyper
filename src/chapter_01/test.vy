# pragma version 0.4.1
# SPDX-License-Identifier: MIT

my_number: public(uint256)
is_happy: public(bool)
is_sad: public(bool)

my_name: public(String[100])
my_favorite_number: public(uint256)

owner: public(address)
name: public(String[100])
expiresAt: public(uint256)


struct Shibainu:
    name: String[100]
    code: uint256


list_of_shibainus: public(Shibainu[10])
name_to_shibainu: public(HashMap[String[100],uint256])

struct Person:
    name: String[100]
    favorite_number: uint256


list_of_numbers: public(uint256[10])
index: public(uint256)
list_of_people: public(Person[10]) # (2, jack) (7, peter) etc


name_to_favorite_number: public(HashMap[String[100], uint256])


@deploy
def __init__():
    self.my_number = 10
    self.my_favorite_number = 77
    self.owner = msg.sender
    self.name = "jack"
    self.expiresAt = block.timestamp + 1000
    self.index = 0
    self.my_name = "jack"

@external
def set_happy(new_happy: bool):
    self.is_happy = new_happy


@external
@view
def retreive() -> uint256:
    return self.my_favorite_number


@external
@pure
def multilpy(x: uint256, y : uint256) -> uint256:
    return x * y

@external
@pure
def divide(x : uint256, y :uint256) -> uint256:
    return x // y

@external
def todo():
    pass

@external
@pure
def return_many() -> (uint256, bool):
    return (1, True)



@external
def add(number: uint256):
    self.list_of_numbers[self.index] = number
    self.index += 1

@external
def add_person(name: String[100], favorite_number: uint256):
    # add favorite number to list of numbers
    self.list_of_numbers[self.index] = favorite_number

    # add person to Person's list
    new_person: Person = Person(name=name, favorite_number=favorite_number)
    self.list_of_people[self.index] = new_person

    # add the person to the hashmap
    self.name_to_favorite_number[name] = favorite_number
    

    self.index += 1


@external
@pure
def add_number(x: uint256, y: uint256) -> uint256:
    return x + y

@external
@view
def add_number_a(x: uint256, y: uint256) -> uint256:
    return x + y + block.timestamp
    
@external
@pure
def if_else(x: uint256) -> uint256:
    if x <= 10:
        return 1
    elif x <= 20:
        return 2
    else:
        return 3

@external
@view
def add_one(x: uint256) -> uint256:
    result: uint256 = x + self.my_number
    return result + 1

@external
@view
def check_fav_number(x: uint256) -> bool:
    if x == self.my_favorite_number:
        return True
    else:
        return False
    


@external
def add_shibainu(name: String[100], code: uint256):
    new_shibainu: Shibainu = Shibainu(name=name, code=code)
    self.list_of_shibainus[self.index] = new_shibainu
    self.name_to_shibainu[name] = code
    self.index += 1










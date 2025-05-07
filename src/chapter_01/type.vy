# pragama version 0.4.1
# @licence MIT

# @author jack

# Reference data types
# - Fixed size list

nums: public(uint256[10])



# - Dynamic arrays




# - Mappings
myMap: public(HashMap[address, uint256])


# - Structs
struct Person:
    name: String[10]
    age: uint256

person: public(Person)



@deploy
def __init__():
    self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    self.nums[0] = 100
    self.nums[1] = 200
    self.nums[2] = 300
    self.nums[3] = 400
    self.nums[4] = 500
    self.nums[5] = 600
    self.nums[6] = 700
    self.nums[7] = 800
    self.nums[8] = 900
    self.nums[9] = 1000

    self.myMap[msg.sender] = 100
    self.myMap[msg.sender] = 200

    self.person.name = "jack"
    self.person.age = 38

    p: Person = self.person
    p.name = "solidity"
    p.age = 100

    self.person = p



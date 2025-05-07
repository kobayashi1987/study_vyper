# pragma version 0.4.1
# SPDX-License-Identifier: MIT

storedData: public(uint256)

@deploy
def __init__(_initValue: uint256):
    self.storedData = _initValue

@external
def set(_x: uint256):
    self.storedData = _x

@external
def get() -> uint256:
    return self.storedData

@external
def increment():
    """
    Increments the stored data by 1
    """
    self.storedData += 1

@external
def decrement():
    """
    Decrements the stored data by 1
    """
    self.storedData -= 1

@external
def multiply(_factor: uint256):
    """@param _factor The number to multiply the stored data by"""
    self.storedData *= _factor

@external
def reset():
    """
    Resets the stored data to 0
    """
    self.storedData = 0
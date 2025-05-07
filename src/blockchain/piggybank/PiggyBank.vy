# @version 0.4.1

event Deposit:
    depositor: indexed(address)
    amount: uint256

event Withdrawal:
    to: indexed(address)
    amount: uint256

beneficiary: public(address)
unlock_time: public(uint256)

@deploy
def __init__(_beneficiary: address, _unlock_time: uint256):
    assert _unlock_time > block.timestamp, "Unlock time must be in future"
    self.beneficiary = _beneficiary
    self.unlock_time = _unlock_time

@payable
@external
def deposit():
    log Deposit(depositor=msg.sender, amount=msg.value)

@external
def withdraw():
    assert msg.sender == self.beneficiary, "Not beneficiary"
    assert block.timestamp >= self.unlock_time, "Still locked"
    amount: uint256 = self.balance
    assert amount > 0, "Nothing to withdraw"
    log Withdrawal(to=msg.sender, amount=amount)
    send(msg.sender, amount)
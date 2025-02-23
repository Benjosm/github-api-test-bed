import pytest
from bank_account.bank_account import BankAccount

def test_withdrawal_broken():
    account = BankAccount("12345")
    account.deposit(100)
    account.withdraw(50)
    assert account.balance == 50
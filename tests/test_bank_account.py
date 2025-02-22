import pytest
from bank_account.bank_account import BankAccount

def test_deposit():
    account = BankAccount("12345")
    account.deposit(100)
    assert account.balance == 100


def test_withdraw_sufficient_funds():
    account = BankAccount("12345", 100)
    account.withdraw(50)
    assert account.balance == 50


def test_withdraw_insufficient_funds():
    account = BankAccount("12345", 100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(150)
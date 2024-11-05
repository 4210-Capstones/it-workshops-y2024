# Installation guide
# -----------------------
# python version <= 3.8
# pip install -U pytest
# pip install fastapi
# pip install httpx

import pytest
from fastapi.testclient import TestClient
import httpx

# Instruction
#-------------
# You can test from:
# Account
# Bank
# API

from account import Account
from bank import Bank
from bank_api import app

# Write code here
class BankTester:
    def test_withdrawal(self, account):
        amount = account.deposit(self, 1001)
        assert amount < 1000

    def test_create_account(self, bank):
        account_id = bank.create_account(self, "-1000")
        assert account_id > "0"

# To run:
# pytest -v test_assignment.py
from account import Account
from client import Client

client = Client("leticia")
bank_account = Account(123, "leticia", 44.5, 2000.0)
bank_account2 = Account(245, "marco", 567.34, 2000.0)

bank_account.bank_statement()
bank_account2.bank_statement()

bank_account.cash_deposit(47)

bank_account.withdraw_money(50.23)


bank_account2.bank_transfer(10, bank_account)
bank_account.bank_statement()
bank_account2.bank_statement()

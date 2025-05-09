from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.customer_addresses = {}  # key: customer, value: address
        self.customer_phone_numbers = {}  # key: customer, value: phone number
        self.branches = []
        self.payroll = None

    def setup_branch(self, location, opening_time, staff):
        self.branches.append(Branch(location, opening_time, staff))

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        branch.close(transfer_branch)
        self.branches.remove(branch)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)
            self.customer_addresses[customer] = "NO ADDRESS"  # default address
            self.customer_phone_numbers[customer] = "NO PHONE NUMBER"  # default phone number

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def add_interest(self, account: Account):
        balance = account.get_balance()
        interest_rate = account.get_interest_rate()
        interest = balance * interest_rate
        account.set_balance(balance + interest)

    def add_funds(self, account: Account, amount: float):
        balance = account.get_balance()
        account.set_balance(balance + amount)

    def close_account(self, account: Account):
        account.set_customer(None)
        account.set_balance(0)
        self.accounts.remove(account)

    def add_staff_member(self, branch: Branch, staff: Staff):
        branch.get_staff().append(staff)

    def change_opening_time(self, branch: Branch, time: str):
        self.branch_opening_times[branch] = time

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        self.payroll = payroll
        self.payroll.get_staff_category_pay_schedule(staff_category).set_pay_date(date)

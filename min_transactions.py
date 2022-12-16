from collections import Counter, deque
import heapq
import unittest

# sripley@plaid.com

def central_bank_processing(transactions):
    b_counter = Counter()
    res = []
    for element in transactions:
        from_bank = element[0]
        to_bank = element[1]
        amt = int(element[2:])
        b_counter[to_bank] += amt
        b_counter[from_bank] -= amt
    
    for bank, amt in b_counter.items():
        if bank == 'A':
            continue
        else:
             if amt < 0:
                 res.append(bank + 'A' + str(abs(amt)))
             elif amt > 0:
                res.append('A' + bank + str(amt))
    return res


def settle_debts(transactions):
    b_counter = Counter()
    b_counter_arr = []
    res = []
    for element in transactions:
        from_bank = element[0]
        to_bank = element[1]
        amt = int(element[2:])
        


    def dfs(start, transactions, path):
        if start == len(transactions):
            print(path)
            res.append(path[:])
            return
        curr_start = transactions[start]

        curr_bank = curr_start[0]
        curr_amt = int(curr_start[1:])

        if curr_amt == 0:
            dfs(start + 1, transactions, path)

        for i in range(start + 1, len(transactions)):
            next_bank, next_amt = transactions[i][0], int(transactions[i][1:])
            if next_amt * curr_amt < 0:
                next_amt += curr_amt
                transactions[i] = next_bank + str(next_amt)
                single_transaction = curr_bank + next_bank + str(abs(next_amt + curr_amt))
                path.append(single_transaction)
                dfs(start, transactions, path)
                next_amt -= curr_amt
                transactions[i] = next_bank + str(next_amt)

    dfs(0, b_counter_arr, [])
    min_trans = 0
    min_element = []
    for element in res:
        if len(element) < min_trans:
            min_element = element
    return element
        

def get_amount_owed(transactions):
    amt_owed = Counter()
    for element in transactions:
        from_bank, to_bank, amt = element[0], element[1], element[2:]
        amt_owed[from_bank] -= amt
        amt_owed[to_bank] += amt
    for element in amt_owed:
        if amt_owed[element] == 0:
            del amt_owed[element]
    return amt_owed

def settle_debts(transactions):
    amt_owed = get_amount_owed(transactions)
    res = []
    def dfs(start, path, amt_owed):
        if start == len(amt_owed):
            res.append(path[:])
            return
        if amt_owed[start]

# python3 -m unittest plaid_interview.py
class PlaidInterviewUnitTests(unittest.TestCase):

    def test_plaid_empty(self):
        self.assertEqual(True, True)

bank_trans = ['AB10', 'BC2', 'BC1', 'CA5']


print(settle_debts(bank_trans))

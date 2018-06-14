import pprint as pp

mempool = []
transaction1 = {"sender": "sender",
                "receiver": "receiver",
                "amount": 11}

transaction2 = {"sender": "sender",
                "receiver": "receiver",
                "amount": 12}

transaction3 = {"sender": "sender",
                "receiver": "receiver",
                "amount": 13}

transaction4 = {"sender": "sender",
                "receiver": "receiver",
                "amount": 14}

mempool.append(transaction1)
mempool.append(transaction2)
mempool.append(transaction3)
mempool.append(transaction4)
transactions = []
transactions.append(transaction1)
transactions.append(transaction2)

mempool = mempool + transactions

pp.pprint(mempool)



pp.pprint(mempool)
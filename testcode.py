import json

block = {'index': 11,
         'time_stamp': '11/11/11',
         'proof': 11,
         'previous_hash': '0000',
         'hash_operation': '0000',
         'data': {}}

strblock = json.dumps(block, sort_keys=True)

print(strblock)

print(type(strblock))

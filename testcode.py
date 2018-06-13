import xlsxwriter as xl

block = {'index': 11,
         'time_stamp': '11/11/11',
         'proof': 11,
         'previous_hash': '0000',
         'hash_operation': '0000',
         'data': {}}

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
wb.save('chain.xls')

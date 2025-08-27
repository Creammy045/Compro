with open('sales.txt', 'r') as sales_file:
    #Read all the lines to a float.
    for line in sales_file:
        #Convert line to a float.
        amount = float(line)
        #Format and display the amount.
        print(format(amount, '.2f'))
        
#taotal_sale = 0
#with open('sales.txt', 'r') as sales_file:
#     for line in sales_file:
#         amount = float(line.strip())
#         total_sales += amount
#         print(f'Sales total: {total_sales:.2f}')
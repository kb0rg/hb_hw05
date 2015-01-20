"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

"""

"""
hw: add commentary
find what's broken and note how to fix it
but also
comment what each part of code does
"""

# initialiaze empty lists
salespeople = []
melons_sold = []

# process data in sales report
f = open("sales_report.csv")
for line in f: # iterate through each line in file
    line = line.rstrip() # remove newlines and whitespace
    entries = line.split(",") # split data into list, separated by commas (thus csv)
    # split list into its respective parts, bind these to variables 
    salesperson = entries[0]
    melons = int(entries[2])

    #   check to see if current salesperson is already in the list of salepeople
    if salesperson in salespeople: # if so, record index in the salespeople list
        position = salespeople.index(salesperson) 
        melons_sold[position] += melons # and add melons from this transation to existing tally
    else: # if not, append name and melon tally to both lists
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)): # iterate through salespeople and melons sold lists
    print "%s sold %d melons" % (salespeople[i], melons_sold[i]) # print how much each has sold

"""
this assumes that the corresponding salesperson/ melons sold occupy same position in each list. 
at current read, this seems like a reasonable assumption, and I can't imagine a case that would break it.
however.
it would be safer to explicitly pair these values in anothe data structure, like a dictionary.
(would tuples work? immutable... I guess not)

"""
# This program will write a table from 2 to 20 and will save it in folder named table.
# these small projects are making my coding learning journey fun..

def table(n):  
    tables = ""
    for i in range(1,11):
        tables += f"{n} X {i} = {n*i} \n"
    with open (f"table/tables_{n}","w" ) as f:
        f.write(tables)


for i in range(2,21):
    table(i)
    
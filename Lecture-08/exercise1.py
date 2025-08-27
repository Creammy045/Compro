with open('emplyees.txt') as emp_file:
    read = emp_file.readlines()
    store = []
    emp = []
    for i in read:
        store.append(i)
        while len(store) == 3:
            emp.append(store)
            store = []
for data in emp:
    print(f'Name: {data[0]}'.strip())
    print(f'ID: {data[1]}'.strip())
    print(f'Dept: {data[2]}'.strip())
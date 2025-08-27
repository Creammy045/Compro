import struct

with open('records.bin', 'rb') as file:
    record_size = struct.calcsize('i20sif')
    while True:
        record = file.read(record_size)
        if not record:
            break
        id_num, name, age, gpa = struct.unpack('i20sif', record)
        name = name.decode().rstrip('\x00')
        print(f'ID: {id_num}, Name: {name}, Age: {age}, GPA: {gpa:.2f}')
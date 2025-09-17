import json

data = {"name": "Alice", "age": 25, "city": "New York"}
json_str = json.dumps(data)
print(f'JSON string: {json_str}')
print(f'length of JSON string: {len(json_str)}') 

parsed_data = json.loads(json_str)
print(f'Type of parsed data): {type(parsed_data)}')
print(f'Parsed data: {parsed_data}') 
print(f'Name: {parsed_data["name"]}') 
print(f'Age: {parsed_data["age"]}') 
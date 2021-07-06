import json

sample_dict = {"name": "Nigar", "surname": "Movsumova"}
with open('users', 'a+') as f:
    f.write(json.dumps(sample_dict) + '\n')

with open('users', 'r') as f:
    sample_dict_str = f.readline()
    print(type(sample_dict_str))
    print(sample_dict_str)
    converted_dict = json.loads(sample_dict_str)
    print(converted_dict)
    print(type(converted_dict))
    print(converted_dict['name'])
    print(converted_dict['surname'])
    # print(f.readline())

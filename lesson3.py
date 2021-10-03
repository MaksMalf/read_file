from pprint import pprint

data = {}


def files(file_list):
    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()

        with open(file_name, 'r', encoding='utf-8') as file:
            count = 0
            for line in file:
                count += 1
            d = {file_name: [count, text]}
            data.update(d)


files(['1.txt', '2.txt', '3.txt'])


sorted_data = {}
sorted_keys = sorted(data, key=data.get)

for w in sorted_keys:
    sorted_data[w] = data[w]


def data_f(name):
    x = open('finally_file.txt', 'a', encoding='utf-8')
    for key in name.keys():
        x.write(f'{key}\n')
        for lin in name[key]:
            x.write(f'{str(lin)}\n')


data_f(sorted_data)





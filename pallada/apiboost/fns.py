import requests
import json



def find_info(q, k, p=1):
    # try:
    #     x = requests.get(
    #         f'https://api-fns.ru/api/search?q={q}&key={k}&page={p}'
    #     ).json()
    # except json.JSONDecodeError as e:
    #     print(e)
    #     return {'items': [], "Count": 0, "Error": e}
    # print(x)
    # return x
    req = requests.get(f'https://api-fns.ru/api/search?q={q}&key={k}&page={p}')
    if req.status_code == 200:
        data = req.json()
        return data


def check_presone(q, k, p=1):
    # try:
    #     return requests.get(
    #         f'https://api-fns.ru/api/check?q={q}&key={k}&page={p}'
    #     ).json()
    # except json.JSONDecodeError as e:
    #     print(e)
    #     return {'items': [], "Count": 0, "Error": e}
    # try:
    req = requests.get(f'https://api-fns.ru/api/check?q={q}&key={k}&page={p}')
    if req.status_code == 200:
        data = req.json()
        return data

def fetch_all(func, q, k):
    i = 1
    data = {"items": [], "Count": 0}
    while i < 5:
        ret = func(q, k, i)
        if ret["Count"] == 0:
            break
        data['items'] += ret['items']
        data['Count'] += ret['Count']
        i += 1
    return data


# print(find_info('Лейкин+Григорий+Алексеевич', 'c4ae32a9960cad2dd051a3e075cab4de19cf0459'))
# print(check_presone('772748402568', 'c4ae32a9960cad2dd051a3e075cab4de19cf0459'))

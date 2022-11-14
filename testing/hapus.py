import json

def getDataFromJsonFile(file):
    with open(file, "r") as connect:
        return json.load(connect)

data = getDataFromJsonFile('db.json')

def deleteByID(db, id):
    for i in range(len(db)):
        if db[i]["id"] == id:
            db['karyawan'].pop(i)

def delProductbyName():
    _id = input("ID daxil edin: ")
    finder = False
    for karyawan in data['karyawan']:
        print(karyawan)
        if karyawan['id'] == _id:
            data['karyawan'].pop(data['karyawan'].index(karyawan))
            finder = True
            print(f"{_id} -Nömrəli ID databaseden silindi")
            break
    with open("db.json", "w") as connect:
        json.dump(data, connect)
    if finder == False:
        print(f"{_id} -Nömrəli ID tapılmadi")

db = getDataFromJsonFile('db.json')
kr = db['karyawan']


delProductbyName()


# deleteByID(kr, 3)

# print(db['karyawan'][0]['id'], end=" - "); print(db['karyawan'][0]['name'], end=" - "), print(db['karyawan'][0]['role'])
# print(db['karyawan'][1]['id'], end=" - "); print(db['karyawan'][1]['name'], end=" - "); print(db['karyawan'][1]['role'])
# for i in range(len(kr)):
#     if kr[i]["id"] == 1
    # print(db['karyawan'][i]['id'], end=" - "); print(db['karyawan'][i]['name'], end=" - "), print(db['karyawan'][i]['role'])
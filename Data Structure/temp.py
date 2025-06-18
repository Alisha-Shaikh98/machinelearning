dict_1 = {
    'Name' : 'Alisha Shaikh',
    'Subject': 'Python Advanced'
}
dict_1['fruits']= 'Apple'
print(f'{dict_1.keys()} \n {dict_1.values()} \n {dict_1.items()}')
print({**dict_1,**{'cool':True}})
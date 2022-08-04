base={}

flag=True


def delete(db):
    print('Input key to element that you want to change')
    key = input()
    db.pop(key)
    print('This human was deleted!')
    
def add(db):
    print('name')
    name =input()
    print('second name')
    fam = input()
    print('status')
    status = input()
    print('salary')
    salary = input()
    db[name + fam] = {'name': name,
                      'fam' : fam,
                      'status' : status,
                      'salary': salary}


def change(db):
    print('Input key to element that you want to change')
    key = input()
    db.pop(key)
    add(db)
    print('DONE!')


def show(db):
    print('_____________________________')
    for key in db.keys():
        print('key: ' + key)
        print('data: ', db[key])



while flag:
    print('_____________________________')
    print('Choose action')
    print('1. delete \n2. add \n3. change \n4. show \n anything else to end')
    action = input('>>')
    if action== 'delete':
        delete(base)
        
    elif action== 'add':
        add(base)
        
    elif action== 'change':
        change(base)    
 
    elif action == 'show':
        show(base)        

num_login = 5
num_exit = 5
good_login = 'Dzezhyts'
good_password = 12267
with open('Autorization.txt','w',encoding='utf-8') as f:
    f.write(f'Login for autorization:{good_login}\n')
    f.write(f'password for autorization:{good_password}\n')
with open('Autorization.txt','r',encoding='utf-8') as f:
    data = f.read()
    print(data)    
for i in range(5):
    login = input('Write login:')
    try:
        password = int(input('Write password:'))
    except ValueError:
        print('Error password must be a number')    
    if login == good_login and password == good_password:
        print('Autorization successfully')
        break
    else:
        num_login -= 1
        num_exit -= 1
        if num_login == 0 and num_login == 0:
            print('Your account is blocked')
            break
        print('Login or password wrong:')    
try :
    user = int(input('Write number:'))
    if user < 18:
        print('You are still a minor')
    elif 18 <= user <= 65:
        print('You are an adult')
    elif user > 65:
        print('You are old')
    else:
        print('Error')
except ValueError:
    print('Conversion error')
except Exception:
    print('General error')
finally:
    print('finally completed successfully') 
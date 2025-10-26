## Technologies Used
- Python 3
- file handing ('open', read / write)
- loops and conditions
- Exception handling ('try / except')
- Basic input validation

### Author 
Yauheni Dzezhyts 
//////////////////
Описание на русском:
Проект демонстрирует простую систему авторизации с ограничением попыток. 
После успешного входа проверяется возраст и выводится категория пользователя.
Все действия записываются в 'Autorazation.txt'.

# Authorization Project (Python)
This is a simple Python project that simulates a login  and authorization system.
The program gives the user 5 attempts to enter the correct login  and password.
If all attempts fail, the account becomes blocked.
After a successfull login, the program asks for the users age and classifies them as:
- Under 18 -> 'Minor'
- 18-65 -> 'Adult'
- Over 65 -> 'Senior'
All actions (login attempts, errors, results,) are recorded in a log file ('Autorization.txt').

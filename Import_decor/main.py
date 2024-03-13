from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

log_file = 'main.log'

def logger(old_function):
    def new_function(*args, **kwargs):
        print(f"Имя функции {old_function.__name__}")
        result = old_function(*args, **kwargs)
        print(f"Аргументы {args} {kwargs}")
        log = f'{datetime.now()} {old_function.__name__} {args} {kwargs} {result}\n'
        with open(log_file, 'a') as f:
            f.write(log)

        return result

    return new_function

@logger
def date():
    return datetime.today()


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date())
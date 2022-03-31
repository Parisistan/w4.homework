def validate_pin(correct_pin):
    pin_input = input('PLEASE ENTER YOUR 4-DIGIT PIN: ')
    if pin_input.isnumeric() is True and int(pin_input) == correct_pin:
        return True
    return False


def calculate_balance(current_balance):
    withdraw_amount = input("Please enter the amount you would like to withdraw: ")
    if withdraw_amount.isnumeric() is not True:
        raise TypeError
    new_balance = current_balance - int(withdraw_amount)
    if new_balance < 0:
        raise Exception
    return new_balance


def withdraw_money():
    correct_pin = 1223
    attempts = 3
    balance = 100

    while attempts != 0:
        pin_validity = validate_pin(correct_pin)

        if pin_validity is True:
            print('PIN is correct.')
            try:
                new_balance = calculate_balance(balance)
            except TypeError:
                print("Please enter numbers only!")
            except Exception:
                print("You have put an unaccepted amount! Try again later.")
            else:
                print("You have £{} remaining in your account.".format(new_balance))
            finally:
                print("☻☻☻ THANK YOU FOR USING THIS ATM. HAVE A GOOD DAY! ☻☻☻")
            break

        else:
            attempts -= 1
            print("Wrong pin, try again! You only have {} attempts remaining.".format(attempts))


withdraw_money()
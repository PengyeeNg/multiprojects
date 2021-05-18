import random, string

class UserData:
    announcement_transfer_amount = "1"
    withdrawal_area_withdrawal_amount = "100"
    actual_name = "wendy8888"
    acc_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    acc_number = ''.join(random.choices(string.digits, k=10))
    old_password = "wendy8888"
    new_password = "wendy8888"
    confirm_password = "wendy8888"


from src.enums.user_enums import Statuses


class Player:

    def __init__(self):
        self.result = {
            'localize': {
                'en': ....,
                'ru': ....
            }
        }

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar="https://google.com/"):
        self.result['avatar'] = avatar

    def build(self):
        return self.result

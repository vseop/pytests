from src.enums.user_enums import Statuses

from src.generators.player_localization import PlayerLocalization
from src.baseclasses.builder import BuilderBaseClass


class Player(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar="https://google.com/"):
        self.result['avatar'] = avatar

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
            "en": PlayerLocalization('en_US').build(),
            "ru": PlayerLocalization('ru_RU').build()
        }
        return self

    # def update_inner_value(self, keys, value):
    #     if not isinstance(keys, list):
    #         self.result[keys] = value
    #     else:
    #         temp = self.result
    #         for item in keys[:-1]:
    #             if item not in temp.keys():
    #                 temp[item] = {}
    #             temp = temp[item]
    #         temp[keys[-1]] = value
    #     return self

    # def build(self):
    #     return self.result

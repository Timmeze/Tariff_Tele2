
def is_archived(tariff):
    return tariff.archived

def is_actual(tariff):
    return not not tariff.archived

def my_filter(func, items):
    result = []
    for item in items:
        if func(item):
            result.append(item)
    return result

class Tariff():
    def __init__(self,
                 name,
                 *,
                 price=0, # 0 - без абонентской платы
                 price_period='mounth',
                 gb=0, # -1 - безлимит
                 minutes=0,
                 sms=0,
                 hit=False,
                 gb_unlim=False,
                 minutes_inlim_tele2=True,
                 archived=False
                 ):
        self.name = name
        self.price = price
        self.price_period = price_period
        self.gb = gb
        self.minutes = minutes
        self.sms = sms
        self.hit = hit
        self.gb_unlim = gb_unlim
        self.minutes_unlim_tele2 = minutes_inlim_tele2
        self.archived = archived
        pass

class TariffManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def create_dic(self, item):
        return {'name': item.name,
                'price': item.price,
                'price period': item.price_period,
                'gb': item.gb,
                'minutes': item.minutes,
                'sms': item.sms,
                'hit': item.hit,
                'gb_unlim': item.gb_unlim,
                'minutes_unlim_tele2': item.minutes_unlim_tele2,
                'archived': item.archived
        }

    def actual(self):
        return list(filter(lambda tariff: not tariff.archived, self.items))

    def archived(self):
        return list(filter(is_archived, self.items))

if __name__ == '__main__':
    manager = TariffManager()
    my_online = Tariff('Мой Онлайн', hit=True, gb=15, minutes=400, gb_unlim=['vk', 'fb'], price=290)
    my_tele2 = Tariff('Мой Теле2', price=7,price_period='day', gb=6)
    univer = Tariff('Универ', archived=True)

    manager.add(my_online)
    manager.add(my_tele2)
    manager.add(univer)

    print(manager.archived()[0].name)

    actual = manager.actual()
    for item in actual:
        print(manager.create_dic(item))

    print('_________')


    arctual = manager.actual()
    for item in actual:
        print(manager.create_dic(item))




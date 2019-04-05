from flask import app, render_template, Flask
from app.main import Tariff, TariffManager


def main():
    app = Flask(__name__)
    manager = TariffManager()
    my_online = Tariff('Мой Онлайн', hit=True, gb=15, minutes=400, gb_unlim=['vk', 'fb'], price=290)
    my_tele2 = Tariff('Мой Теле2', price=7, price_period='day', gb=6)
    univer = Tariff('Универ', archived=True)

    manager.add(my_online)
    manager.add(my_tele2)
    manager.add(univer)


    @app.route('/', methods=['GET','POST'])
    def actual():
        actual_tariff = manager.actual()
        result = []
        for item in actual_tariff:
            result.append(manager.create_dic(item))
        return render_template('ind.html', result=result)

    @app.route('/archive')
    def archive():
        archive_tariff = manager.archived()
        result = []
        for item in archive_tariff:
            result.append(manager.create_dic(item))
        return render_template('arch.html', result=result)


    app.run(port=9876, debug=True)


if __name__ == '__main__':
        main()
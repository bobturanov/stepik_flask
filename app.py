from flask import Flask, render_template  # подключаем render_template, который включает функции для Jinja
from data import title, subtitle, description, departures, tours

app = Flask(__name__)  # объявим экземпляр фласка


@app.route('/')
def main():
    print(tours)
    return render_template('index.html', title=title, subtitle=subtitle, description=description, departures=departures,
                           tours=tours)


@app.route('/departures/<departure>')
def render_departures(departure):
    return render_template('departure.html', title=title, subtitle=subtitle, description=description,
                           departures=departures, tours=tours)


@app.route('/tours/<id>')
def render_tours(id):
    return render_template("tour.html", title=title, departures=departures)


@app.errorhandler(404)
def render_not_found(error):
    print(error)
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим:\n{}".format(error.original_exception), 500


app.run()  # запустим сервер

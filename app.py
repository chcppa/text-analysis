import joblib
from flask import Flask, render_template, request

model = joblib.load("model.pkl")  # Загрузка обученной модели

app = Flask(__name__)  # Инициация приложения


def predict(text):
    """Функция анализа текста по настроению, возвращает True/False"""
    return model.predict([text])[0]


@app.route("/", methods=['GET', 'POST'])
def analyse_text():
    """Эндпоинт генерирующий главную страницу и возвращающий результат анализа при наличии текста"""
    flag = False
    type_res = ""
    name = ""
    if request.method == 'POST':
        flag = True
        if request.form["submit_button"]:
            text = request.form['text_tonal']
            if len(text) != 0:
                name = text
            res = predict(name)
            if res == 0:
                type_res = "Негативное сообщение"
            else:
                type_res = "Позитивное сообщение"

    return render_template('main.html', flag=flag, type_of_tonal=type_res, text=name)


if __name__ == "__main__":
    """Запуск приложения"""
    app.run()




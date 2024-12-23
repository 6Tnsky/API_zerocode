from flask import Flask, render_template
import requests

app = Flask(__name__)

# Функция для получения случайной шутки
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"setup": "Не удалось получить шутку.", "punchline": ""}
    except Exception as e:
        return {"setup": "Ошибка соединения.", "punchline": str(e)}

@app.route('/')
def index():
    joke = get_random_joke()
    return render_template('index.html', joke=joke)

if __name__ == '__main__':
    app.run(debug=True)
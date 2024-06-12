from flask import render_template, request, redirect, url_for
from app import app

posts =[]

@app.route("/", methods=["GET", "POST"])

def index():
#использует метод POST, так как информация будет отправляться. Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
    #функция request.form извлекает значение из соответствующих полей
        title = request.form.get('title')
        content = request.form.get('content')
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')



        if title and content:
            posts.append({'title': title, 'content': content, 'name': name, 'age': age, 'city': city, 'hobby': hobby })
            return redirect(url_for('index'))
        #возвращает отрендеренный шаблон с переданными данными постов
    return render_template('blog.html', posts=posts)
from django.http import HttpResponse


menu = """
<a href="/">Головна</a><br>
<a href="/about/">Про нас</a><br>
<a href="/contacts/">Контакти</a><br>
<a href="/products/">Товари</a><br>
<a href="/students/">Студенти</a><br>
<a href="/profile/">Профіль</a><br>
<a href="/sales/">Знижки</a><br><br>
"""


def home(request):
    return HttpResponse(f"""
        {menu}

        <h1>Головна</h1>
        <p>Ласкаво просимо на наш сайт!</p>
    """)


def about(request):
    return HttpResponse(f"""
        {menu}

        <h1>Про нас</h1>
        <p>Ми вивчаємо Django.</p>
    """)


def contacts(request):
    return HttpResponse(f"""
        {menu}

        <h1>Контакти</h1>
        <p>Email: test@gmail.com</p>
        <p>Телефон: +380000000000</p>
    """)


def products(request):
    return HttpResponse(f"""
        {menu}

        <h1>Наші товари</h1>

        <ul>
            <li>Ноутбук - 25000 грн</li>
            <li>Мишка - 700 грн</li>
            <li>Клавіатура - 1200 грн</li>
        </ul>
    """)


def students(request):
    return HttpResponse(f"""
        {menu}

        <h1>Студенти</h1>

        <table border="1">
            <tr>
                <th>Ім’я</th>
                <th>Вік</th>
                <th>Курс</th>
            </tr>

            <tr>
                <td>Іван</td>
                <td>18</td>
                <td>Python</td>
            </tr>

            <tr>
                <td>Марія</td>
                <td>20</td>
                <td>Django</td>
            </tr>
        </table>
    """)


def profile(request):
    name = "Іван"
    age = 18
    city = "Київ"

    return HttpResponse(f"""
        {menu}

        <h1>Профіль користувача</h1>

        <p>Ім'я: {name}</p>
        <p>Вік: {age}</p>
        <p>Місто: {city}</p>
    """)


def sales(request):
    return HttpResponse(f"""
        <style>
            body {{
                background: lightblue;
                font-family: Arial;
            }}
        </style>

        {menu}

        <h1>Знижки</h1>

        <ul>
            <li>Ноутбук - 20%</li>
            <li>Мишка - 10%</li>
            <li>Клавіатура - 15%</li>
        </ul>
    """)
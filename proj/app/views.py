from django.shortcuts import render

JOBS = [
    {
        'id': 1,
        'title': 'Python Developer',
        'company': 'SoftServe',
        'salary': '$2500',
        'description': 'Розробка backend на Django. Робота з REST API, PostgreSQL, Docker.',
    },
    {
        'id': 2,
        'title': 'Frontend Developer',
        'company': 'EPAM Ukraine',
        'salary': '$2200',
        'description': 'Розробка інтерфейсів на React. Верстка адаптивних сторінок.',
    },
    {
        'id': 3,
        'title': 'DevOps Engineer',
        'company': 'GlobalLogic',
        'salary': '$3000',
        'description': 'Налаштування CI/CD, адміністрування Kubernetes кластерів.',
    },
]


def index(request):
    context = {
        'jobs': JOBS,
    }
    return render(request, 'index.html', context)


def detail(request, job_id):
    job = next((j for j in JOBS if j['id'] == job_id), None)
    context = {
        'job': job,
    }
    return render(request, 'detail.html', context)
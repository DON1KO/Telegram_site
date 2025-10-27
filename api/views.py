from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import requests
from django.conf import settings

TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN
CHAT_ID = settings.CHAT_ID


@api_view(['POST'])
def send_message(request):
    email = request.data.get('email', 'не указан')
    phone = request.data.get('phone', 'не указан')

    message = (
        f'Зарегистрировался новый пользователь!\n'
        f'Email: {email}\n'
        f'Телефон: {phone}'
    )

    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return Response({'status': 'success', 'message': 'Отправлено в Telegram'})
    else:
        return Response({'status': 'error', 'details': response.text})


@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_about(request):
    about = About.objects.all()
    serializer = AboutSerializer(about, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_consultation(request):
    serializer = ConsultationSerializer(data=request.data)
    if serializer.is_valid():
        consultation = serializer.save()

        message = (
            f'Новая заявка на консультацию!\n'
            f'Имя: {consultation.name}\n'
            f'Телефон: {consultation.phone}\n'
            f'Сообщение: {consultation.message}'
        )

        url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
        payload = {'chat_id': CHAT_ID, 'text': message}
        requests.post(url, data=payload)

        return Response({'status': 'success', 'message': 'Заявка создана и отправлена в Telegram'})
    else:
        return Response({'status': 'error', 'errors': serializer.errors})


@api_view(['GET'])
def get_tools(request):
    tools = Tool.objects.all()
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_design(request):
    reviews = Design.objects.all()
    serializer = DesignSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_vacancy(request):
    vacancy = Vacancy.objects.first()
    if vacancy:
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    return Response({'message': 'Нет активных вакансий'}, status=404)


@api_view(['POST'])
def send_vacancy_application(request):
    serializer = VacancyApplicationSerializer(data=request.data)
    if serializer.is_valid():
        app = serializer.save()

        message = (
            f'Новый отклик на вакансию!\n'
            f'Имя: {app.name}\n'
            f'Email: {app.email}\n'
            f'Телефон: {app.phone}\n'
            f'Linkedin: {app.linkedin or "Не указана"}'
        )

        requests.post(
            f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage',
            data={'chat_id': CHAT_ID, 'text': message}
        )

        return Response({'status': 'success', 'message': 'Заявка успешно отправлена!'})
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def send_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        contact = serializer.save()

        message = (
            f'Новая заявка с сайта!\n'
            f'Имя: {contact.name}\n'
            f'Телефон: {contact.phone}\n'
            f'Интересует: {contact.message}'
        )

        url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
        payload = {'chat_id': CHAT_ID, 'text': message}
        requests.post(url, data=payload)

        return Response({'status': 'success', 'message': 'Заявка отправлена ✅'})
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_contact_info(request):
    info = ContactInfo.objects.first()
    if info:
        serializer = ContactInfoSerializer(info)
        return Response(serializer.data)
    return Response({'message': 'Информация не найдена'}, status=404)


@api_view(['GET'])
def get_viewjob(request):
    vacancy = ViewJob.objects.all()
    serializer = ViewJobSerializer(vacancy, many=True)
    return Response(serializer.data)

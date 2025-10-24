from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import requests


# 🔐 Токен и чат айди Telegram
Token = '8287861784:AAEQWmQkQesRGlH4cg-zG59saTBD8NukkDA'
Chat_id = '-1003087039414'


# 📩 Отправка сообщения в Telegram
@api_view(['POST'])
def send_message(request):
    email = request.data.get('email', 'не указан')
    phone = request.data.get('phone', 'не указан')

    message = (
        f'📩 Зарегистрировался новый пользователь!\n'
        f'📧 Email: {email}\n'
        f'📱 Телефон: {phone}'
    )

    url = f'https://api.telegram.org/bot{Token}/sendMessage'
    payload = {'chat_id': Chat_id, 'text': message}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return Response({'status': 'success', 'message': 'Отправлено в Telegram ✅'})
    else:
        return Response({'status': 'error', 'details': response.text})


# 📰 Получение всех постов (например, новости или проекты)
@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


# 💡 Получение инструментов ("О нас" — технологии)
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

        # Сообщение в Telegram
        message = (
            f'📬 Новая заявка на консультацию!\n'
            f'👤 Имя: {consultation.name}\n'
            f'📞 Телефон: {consultation.phone}\n'
            f'💬 Сообщение: {consultation.message}'
        )

        url = f'https://api.telegram.org/bot{Token}/sendMessage'
        payload = {'chat_id': Chat_id, 'text': message}
        requests.post(url, data=payload)

        return Response({'status': 'success', 'message': 'Заявка создана и отправлена в Telegram ✅'})
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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import CustomUser
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class UserInfoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token_str = request.data.get('token')
        if not token_str:
            return Response({'error': 'Токен не предоставлен'}, status=400)

        try:
            token = UntypedToken(token_str)
            user_id = token['user_id']
            user = CustomUser.objects.get(id=user_id)
            return Response({
                'is_authenticated': True,
                'username': user.username,
                'groups': list(user.groups.values_list('name', flat=True)),
            })
        except (InvalidToken, TokenError):
            return Response({'error': 'Неверный токен'}, status=401)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=404)
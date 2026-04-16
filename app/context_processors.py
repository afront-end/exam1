from .models import UserModel

def get_current_user(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = UserModel.objects.filter(id=user_id).first()
        return {'user': user}
    return {'user': None}
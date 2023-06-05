# from django.core.cache import cache

from .models import Player


# def validate_user(user_id):
#     if cache.get(user_id) is None:
#         try:
#             User.objects.get(user_id=user_id)
#             cache.set(user_id, 1, 5)
#             return True
#         except Player.DoesNotExist:
#             return False
#     else:
#         cache.set(user_id, 1, 5)
#         return True

def validate_user(user_id):
    try:
        Player.objects.get(userId=user_id)
        return True
    except Player.DoesNotExist:
        return False


def get_user_by_uid(user_id):
    try:
        player = Player.objects.get(userId=user_id)
        return player
    except Player.DoesNotExist:
        return None


def get_user_by_soid(social_id):
    try:
        player = Player.objects.get(socialId=social_id)
        return player
    except Player.DoesNotExist:
        return None

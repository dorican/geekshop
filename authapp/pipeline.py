from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse, urlparse
import requests
from django.core.files.base import ContentFile
from django.utils import timezone
from social_core.exceptions import AuthForbidden
from authapp.models import ShopUserProfile
import json


def save_user_profile(backend, user, response, *args, **kwargs):

    if backend.name != 'vk-oauth2':
        return
    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(
                              fields=','.join(('bdate', 'sex', 'city', 'country', 'lang',)),
                              access_token=response['access_token'], v='5.92')), None
                              ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]


    if data['sex'] and not user.shopuserprofile.gender:
        if data['sex'] == 2:
            user.shopuserprofile.gender = 'М'
        else:
            user.shopuserprofile.gender = 'Ж'

    # if data['bdate']:
    #     bdate = datetime.strptime(data['bdate'],'%d.%m.%Y').date()
    #     user.age = timezone.now().date().year - bdate.year
    #     if user.age < 18:
    #         user.delete()
    #         raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    if data['city']:
        user.shopuserprofile.city = data['city']['title']

    if data['country']:
        user.shopuserprofile.country = data['country']['title']
    print(data['language'])
    if data['language'] and not user.shopuserprofile.language:
        if data['language'] == '0':
            user.shopuserprofile.language = 'русский'

    user.save()

from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlparse, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https', 'api.vk.com', '/method/users.get', None,
                            urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'country', 'photo_50', 'online', 'domain', 'site')),
                            access_token=response['access_token'], v='5.131')),
                          None))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE

    if data['about']:
        user.shopuserprofile.about_me = data['about']

    # if data['country']:
    #     user.shopuserprofile.country = data['country']

    # if data['photo_50']:
    #     user.shopuserprofile.photo = data['photo_50']
    #
    # if data['online']:
    #     user.shopuserprofile.online = data['online']
    #
    # if data['domain']:
    #     user.shopuserprofile.domain = data['domain']
    #
    # if data['site']:
    #     user.shopuserprofile.site = data['site']

    user.save()

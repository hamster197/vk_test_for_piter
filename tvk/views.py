from social_django.models import UserSocialAuth
from django.shortcuts import render
import vk
import random
import time
# Create your views here.
def LogMainView(request):
    if request.user.is_authenticated:
        access_token = UserSocialAuth.objects.filter(user_id__username=request.user.username) \
                .last().extra_data['access_token']
        session = vk.Session(access_token=access_token)
        api = vk.API(session, v='5.4', lang='ru', timeout=10)
        name = api.users.get(user_ids=request.user.username.replace('id', ""))[0]['first_name'] + ' ' + \
                api.users.get(user_ids=request.user.username.replace('id', ""))[0]['last_name']
        all_frends = api.friends.get(user_ids=request.user.username.replace('id', ""))['items']

        frends = []
        for i in range(5):
            fr = random.choice(all_frends)
            frn = api.users.get(user_ids=fr)[0]['first_name']
            time.sleep(0.8)
            frn = frn + ' '+ api.users.get(user_ids=fr)[0]['last_name']
            frends.append(frn)
        return render(request, 'tvc/login.html', {'name': name, 'frends':frends})
    return render(request, 'tvc/login.html')
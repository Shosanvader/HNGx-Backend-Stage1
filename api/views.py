import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_GET

Github_File_Url = 'https://github.com/Shosanvader/HNGx-Stage1-Backend/blob/master/manage.py'
Github_Repo_Url = 'https://github.com/Shosanvader/HNGx-Stage1-Backend'

@require_GET
def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    current_day = datetime.datetime.now().strftime('%A')
    current_utc_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_utc_time,
        'track': track,
        'github_file_url': Github_File_Url,
        'github_repo_url': Github_Repo_Url,
        'status_code': 200
    }

    return JsonResponse(response)


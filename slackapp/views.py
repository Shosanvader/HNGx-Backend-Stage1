from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.utils import timezone
import datetime

@require_GET
def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    current_day = datetime.datetime.now().strftime('%A')
    current_utc_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    github_file_url = 'https://github.com/username/repo/blob/main/file_name.ext'
    github_repo_url = 'https://github.com/username/repo'

    response = {
        'slack_name': 'Praise Okediadi',
        'current_day': current_day,
        'utc_time': current_utc_time,
        'track': 'backend',
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return JsonResponse(response)


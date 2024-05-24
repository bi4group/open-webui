import requests

from enum import Enum


class MeetingType(str, Enum):
    FIREFLIES = 'fireflies'
    MICROSOFT_TEAMS = 'microsoft_teams'
    GOOGLE_MEET = 'google_meet'


class MeetingService:
    @staticmethod
    def get_meetings(meeting_type: MeetingType, user):
        meeting_methods = {
            MeetingType.FIREFLIES: MeetingService.get_fireflies_meetings,
            MeetingType.MICROSOFT_TEAMS: MeetingService.get_microsoft_teams_meetings,
            MeetingType.GOOGLE_MEET: MeetingService.get_google_meet_meetings
        }

        return meeting_methods[meeting_type](user)

    @staticmethod
    def get_fireflies_meetings(user):
        API_URL = 'https://api.fireflies.ai/graphql'
        auth_header = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {user.fireflies_api_key}'
        }

        data = ('{"query": "query Transcripts($userId: String) { transcripts(user_id: $userId) { title id dateString '
                'duration summary { action_items overview shorthand_bullet  } participants } }"}')

        response = requests.post(API_URL, headers=auth_header, data=data)

        return response.json()

    @staticmethod
    def get_microsoft_teams_meetings(user):
        # Implement the logic to get Microsoft Teams meetings
        pass

    @staticmethod
    def get_google_meet_meetings(user):
        # Implement the logic to get Google Meet meetings
        pass
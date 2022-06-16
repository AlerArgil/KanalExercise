import uuid

from django.conf import settings
from django.core.management.base import BaseCommand
from googleapiclient.discovery import build


class Command(BaseCommand):
    help = 'get info from file'

    def handle(self, *args, **options):
        service = build('sheets', 'v4', credentials=settings.GOOGLE_CREDS)
        sheet = service.spreadsheets()

        result = sheet.values().get(spreadsheetId=settings.GOOGLE_SHEET_ID, range='A:D').execute()
        rows = result.get('values', [])
        body = {
            'id': str(uuid.uuid4()),
            'type': 'webhook',
            'address': 'https://888a-91-195-136-125.ngrok.io/test/'
        }
        service_drive = build('drive', 'v3', credentials=settings.GOOGLE_CREDS)
        # watch = service_drive.files().watch(fileId=settings.GOOGLE_SHEET_ID, supportsAllDrives=True, body=body)
        watch = service_drive.files().watch(fileId=settings.GOOGLE_SHEET_ID, supportsAllDrives=True, body=body)

        print(watch.execute())
        # print(rows)
        print('do_staff')

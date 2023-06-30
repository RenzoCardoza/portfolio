from __future__ import print_function

import datetime
import os.path
from PyPDF2 import PdfReader
import requests, PyPDF2, io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import json

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    #Reading PDF
    
    reader = PdfReader("escala.pdf")
    page = reader.pages[0]
    text = page.extract_text()
    print(text)    
    # close reading


    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
       
        def events_reader(filename):
            """reads json to obtain the data"""
            #read the file
            with open(filename, "rt") as events_file:
                #manage the file
                events_arr = json.load(events_file)
            return events_arr
        #call the function
        event_dict = events_reader("events_test.json")

        event_arr = event_dict['events']
        print(event_arr)

        # for event in event_arr:
        #     new_event = service.events().insert(calendarId='primary', body=event).execute()
        #     print('event created: %s' % (event.get('htmlLink')))

    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    main()
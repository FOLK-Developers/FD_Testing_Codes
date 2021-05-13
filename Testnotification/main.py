import firebase_admin
import flask
import pyfcm
from firebase_admin import credentials, messaging
from firebase_admin import firestore
from flask import jsonify
from datetime import date
from datetime import datetime
from flask import request, jsonify
from pyfcm import FCMNotification

# firebase_admin.initialize_app()

cred = credentials.Certificate(
   'serviceAccountKey.json')

firebase_admin.initialize_app(cred, {
   'databaseURL': 'https://folk-bf69e.firebaseio.com/'
})

db = firestore.client()
# fcm_id = "epMqXIUVDUY5ppguW5Rwnz:APA91bFWpJu3BLZriZhXdHsoG4qUaFI_2tI2TtDBN9scdqofe_Zu8-dyhzWMtdWY2lFbPGcUuvS-dwd29NX_SbNPDh_LHJJCH1T_V9nMnNQWkqv0gGJhZwFkVojtFxuWzdgF9-M4bdXE";
#fcm_id = "eHIbPKguQMuePA9NGnM9Aq:APA91bEKS3FeMujxwWquY9zD3MdXAqjokY50pBoe18ItsV2HCNEAnYuyMGzFj3Tg09vC9nVEAqRe_SgiKatinllBD4XacrRyRmm91nGi2m3iNoTKPc1v0RaZx1tAS5gvrYv6xvMyL5NC";
fcm_id = "c7Q9N7mfQYOC7kI842pW2S:APA91bHl3CASGyMm4ffUEDzSV-G9ZJEOGajzfxUugtcyY7odHl96bdxXPZAvvD8_o70yTvWG0RTmkefw0HNE78kuMaksRX33aNOQp56VPyoTDKMjKEjPt8TCD6xIG1jVs97FOT0KFg8K";
# recdata = flask.request.json



recdata = {
   "fcm_id": fcm_id,
   "event_id": "Xnqm5j6Srd45m4jumUPC",
   "notification_type": "Feed",
   "FOLK_guide": "SRRD",
   "user_name": "Shresta Rupa Dasa",
   "user_zone": "ISKCON Bangalore",
   "user_phone": "9342336283",
   "title": "FOLK EVENT",
   "body": "Starting at 8:15 PM",
   "gender": "All"
}



def hello_world(recdata):
   fcm_id = recdata['fcm_id']
   event_id = recdata['event_id']
   typ = recdata['notification_type']
   title = recdata['title']
   body = recdata['body']

   docs = db.collection(u'Events').document(event_id)
   docs = docs.get()
   docs = docs.to_dict()
   # print(docs)
   zone = docs['zone']
   program = docs['program']
   program_title = docs['category']
   event_link = docs['venue']
   session = docs['session']

   data_message = {
       "feedDocumentId": event_id,
       "type": typ,
       "title": title,
       "image": "https://storage.googleapis.com/media.helloumi.com/customers/15878504/GX05AHZIY34S55SDEYSHMJPWGXVOPMYK.jpg",
       "icon": "notificationbar",
       "sound": "text_notification",
       "android_channel_id": "Krishna_Channel",
       "body": body,
       "click_action": "FLUTTER_NOTIFICATION_CLICK",
       "zone": zone,
       "program": program,
       "program_title": program_title,
       "event_link": event_link,
       "session": session,
       # "sound": "default",
       # "meetup_type": "Individual"

   }

   print("Data : ", data_message)
   if fcm_id is not None:
       push_service = FCMNotification(
           api_key="AAAAjMoPwj8:APA91bFQEyT-OKJu_Huw6nygF_vYm6NFiTzeZccfXFaKY7jrEt7lJQkB-zYYl4O3V9jUFYfd3ANyIW6l9gNFAWJqo2Jr4v7PtUD4_W49vyijLlH0atePaQEogLoWjB0W0Ap494PRYUtL",
           proxy_dict=None)
       message_title = title
       badge = "https://images.ctfassets.net/3prze68gbwl1/asset-17suaysk1qa1jpm/e2aae2e93b3f213fa8a3b05c1cfa849b/notification-badge-icon-badge.jpg"
       #message_body = "Hey, EVENT STARTED"
       # result = push_service.notify_single_device(registration_id=fcm_id, message_title=title,
       #                                            message_body=body)
       extra_notification_kwargs = {
           # 'android_channel_id': 2,
           "image": "https://storage.googleapis.com/media.helloumi.com/customers/15878504/GX05AHZIY34S55SDEYSHMJPWGXVOPMYK.jpg",

       }
       result = push_service.notify_single_device(registration_id=fcm_id, message_title=message_title, message_body= body, badge= badge,
                                                  data_message=data_message, extra_notification_kwargs=extra_notification_kwargs)

       print("result", result)
   else:
       result = {
           "Status": False,
           "output": "No FCM ID"
       }

   return result


resp = hello_world(recdata)
print(resp)
# 1. IN WHICH ANDROID app we are using this notification functionality
# 2. AndroidManifest.xml of that app

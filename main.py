import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials


def send_to_topic():
    # [START send_to_topic]
    # The topic name can be optionally prefixed with "/topics/".
    topic = 'TOPIC ID'

    # See documentation on defining a message payload.
    message = messaging.Message(
        apns=messaging.APNSConfig(
            headers={'apns-priority': '10'},
            payload=messaging.APNSPayload(
                aps=messaging.Aps(
                    alert=messaging.ApsAlert(
                        title='You are in huge risk!!!',
                        body='Please go away!!! Go away!!!',
                    ),
                    sound=messaging.CriticalSound(name='default', critical=True, volume=1.0),
                    badge=42,
                ),
            ),
        ),

        topic=topic,
    )

    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_topic]


cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)

send_to_topic()

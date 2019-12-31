from twilio.rest import Client

client = Client(
    "TWILIO_ACCOUNT_SID", 
    "AUTH_TOKEN"
    );

for msg in client.messages.list():
    print(f"Deleting {msg.body}");
    msg.delete();
#msg = client.messages.create(
#    to="YOUR_PHONE_NUMBER",
#    from_="TWILIO_PHONE_NUMBER",
#    body="Hello from Python!"
#);
#
#print(f"Created a new message: {msg.sid}");
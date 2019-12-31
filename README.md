# Twilio-Messaging-Python

> This assumes that you know how to use the cli/terminal in GNU/Linux

> This also assumes you have created an account on Twilio and obtained your twilio number

- Install python3.8 via cli in Linux or vis wsl
```
sudo apt install python3.8 
```
- Install python3.8-venv via Linux or wsl cli
```
sudo apt install python3.8-venv
```
- Create a folder for the python vitural environment 
```
mkdir folder name
```
- Add the example.py file into the folder
```
mv example.py /your/folder/directory
```
- CD into that folder name
```
cd folder name
```
- Create the python vitural envrionment
```
python -m venv .venv
```
- Open up your IDE via the command line
```
code .
```
- Then run the command in the vscode terminal
```
source ./.venv/bin/activate
```
- Make sure to input your account_sid and auth_token in the explore.py file
```
client = Client(
    "TWILIO_ACCOUNT_SID", 
    "AUTH_TOKEN"
    );

```
- Uncomment these lines of code to send messages to a phone number from your twilio number
- Change the body of the message if you want
```
#msg = client.messages.create(
#    to="YOUR_PHONE_NUMBER",
#    from_="TWILIO_PHONE_NUMBER",
#    body="Hello from Python!"
#);
#
#print(f"Created a new message: {msg.sid}");
```
- Make sure to comment out
```
#for msg in client.messages.list():
#    print(f"Deleting {msg.body}");
#    msg.delete();
```
- Finally run the code
```
python example.py
```

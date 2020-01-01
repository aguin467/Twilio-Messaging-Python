# Twilio-Messaging-Python <sup><sub>🐍
> <i> This assumes that you know how to use the cli/terminal in GNU/Linux </i> 

> <i> This also assumes you have created an account on Twilio and obtained your twilio number </i> 

----------------------------------------------------------------------------------------------------------------------------------------

- Install python3.8 via cli in Linux or vis wsl 
```
sudo apt install python3.8 
```
<p>&nbsp;

- Install python3.8-venv via Linux or wsl cli
```
sudo apt install python3.8-venv
```

<p>&nbsp;

- Create a folder for the python vitural environment 
```
mkdir folder name
```

<p>&nbsp;

- Add the example.py file into the folder
```
mv example.py /your/folder/directory
```

<p>&nbsp;

- CD into that folder name
```
cd folder name
```

<p>&nbsp;

- Create the python vitural envrionment
```
python -m venv .venv
```

<p>&nbsp;

- Install the vitural environment

```
source ./.venv/bin/activate
```

<p>&nbsp;

- Install twillio via pip in the venv from above

```
pip install twilio
```

<p>&nbsp;

- Open up your IDE via the command line
```
code .
```

<p>&nbsp;

- Then run the command in the vscode terminal
```
source ./.venv/bin/activate
```

<p>&nbsp;

- Make sure to input your account_sid and auth_token in the explore.py file
```
client = Client(
    "TWILIO_ACCOUNT_SID", 
    "AUTH_TOKEN"
    );

```

<p>&nbsp;

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

<p>&nbsp;

- Make sure to comment out
```
#for msg in client.messages.list():
#    print(f"Deleting {msg.body}");
#    msg.delete();
```

<p>&nbsp;

- Finally run the code :shipit:
```
python explore.py
```

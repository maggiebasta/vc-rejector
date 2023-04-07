# vc-rejector
An AI enabled extension for Gmail to reject annoying venture capitalists

## Set up:

**Installation:**

```
python -m venv env
source env/bin/activate
pip install -e .
pip install -r requirements.txt
```

**Upload the Chrome extension:**
- In Chrome, go to settings -> Extensions
- Toggle developer mode to ON in the upper right corner
- In the top left, select "Load unpacked" and upload the projects extension folder 

**Start your local server:**
```
source env/bin/activate
python app.py
```

**Reject**:

Go to Gmail, open the email you want to reply to, click the 3 vertical dots in the bottom right of the message box, select "Reject This VC"
![alt text](https://github.com/maggiebasta/vc-rejector/blob/main/assets/email.png)

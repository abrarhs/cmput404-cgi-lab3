# CMPUT404 CGI Experiments

Experimenting with CGI server stuff!

Lab 3 

1. import os and specify type to html

2. query_string  

3. type in the key in print statement. HTTP_USER_AGENT

4. cgi forms 
s= cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

5. HTTP header 'Set Cookie' for username and password

6. HTTP_COOKIE

7. for storing user data

8. https://github.com/abrarhs/cmput404-cgi-lab3
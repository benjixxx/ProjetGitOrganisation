#!/usr/bin/python
# coding: utf-8

import cgi 
import construct
#import cgitb; cgitb.enable()

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")


html_head= '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"/>
    <title>Mon programme</title>
    
    <style>
    
    {
    margin: auto;
    width: 50%;
    border: 3px solid green;
    padding: 10px;
    }
    
    table {  
    border: medium solid #000000;
    width: 100%;
    }
    
    td, th {
    border: thin solid #6495ed;
    width: 10%;
    } 
    </style>
</head>'''

html_body= '''<body>
    <h1>Tableau Récapitulatif Git</h1>
    
    <table>
    
    <tr>
    <th>Nom</th>
    <th>Chemin</th>
    <th>Date-Modif</th>
    <th>Dernier Pusher</th>
    </tr>'''
	
html_git =""
contenu_git = construct.main()

for file in contenu_git:
	html_git += "<tr><td>"+ file[0]+ "</td><td>"+ file[1]+ "</td><td>"+ file[2]+ "</td><td>"+ file[3]+"</td></tr>"

html_foot = '''
    </table>
</body>
</html>'''

html = html_head + html_body + html_git + html_foot

print(html)



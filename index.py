#!/usr/bin/python
# coding: utf-8

import cgi 
#import cgitb; cgitb.enable()

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")


html= """<!DOCTYPE html>
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
    width: 50%;
    }
    
    td, th {
    border: thin solid #6495ed;
    width: 10%;
    }
    </style>
</head>

<body>
    <h1>Tableau Récapitulatif Git</h1>
    
    <table>
    
    <tr>
    <th>Nom</th>
    <th>Chemin</th>
    <th>Date-Modif</th>
    <th>Dernier Pusher</th>
    </tr>
    
    <tr>
    <td>cellule A1</td>
    <td>cellule B1</td>
    <td>cellule C1</td>
    <td>cellule D1</td>
    </tr>
    
    <tr>
    <td>cellule A2</td>
    <td>cellule B2</td>
    <td>cellule C2</td>
    <td>cellule D2</td>
    </tr>
    
    <tr>
    <td>cellule A3</td>
    <td>cellule B3</td>
    <td>celulle C3</td>
    <td>celulle D3</td>
    </tr>

    </table>
</body>
</html>
"""
print(html)



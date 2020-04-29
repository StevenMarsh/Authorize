#!/usr/bin/env python3

###########################################################################
print('Content-Type:text/html') #HTML is following
print("")                          #Leave a blank line

import mysql.connector
from mysql.connector import Error
import cgi
import cgitb
cgitb.enable()

conn = None
try:
  conn = mysql.connector.connect(host='localhost',
                                     database='authorize',
                                     user='root',
                                     password='adam')

  if conn.is_connected:
    input_data=cgi.FieldStorage()
    cursor = conn.cursor()
    try:
      email = input_data["email"].value
      
      sql_command = """SELECT email FROM users WHERE email = %s"""

      var = (email, )

      cursor.execute(sql_command, var)

      data = cursor.fetchall()

      if not data:
        #need alert
        print('Email not associated with subscription')
      else:
        #need alert
        try:

          sql = """UPDATE users SET sub = %s WHERE email = %s"""
          varr = (0, email)
          cursor.execute(sql, varr)
          conn.commit()
        except Error as e:
          print('<p>',e,'</p>')

        print('Subscription cancelled')

    except Error as e:
      print('<p>',e,'</p>')
      
    finally:
      print('<p>Done!</p>')
      cursor.close()

except Error as e:
  print('<p>',e,'</p>')

finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print('<p>Connection closed</p>')

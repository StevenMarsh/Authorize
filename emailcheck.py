#!/usr/bin/env python3

###########################################################################
print('Content-Type:text/html') #HTML is following
print("")                          #Leave a blank line

###########################################################################
#
#import mysql.connector
#from mysql.connector import Error
#
#conn = None
#try:
#    conn = mysql.connector.connect(host='localhost',
#                                   database='autorize',
#                                   user='root',
#                                   password='adam')
#    if conn.is_connected():
#        print('<p>Connected to MySQL database</p>')
#########
#        try:
#            cursor = conn.cursor()
#            cursor.execute("SELECT * FROM users")
#            row = cursor.fetchone()
#            while row is not None:
#                print('<p>',row,'</p>')
#                row = cursor.fetchone()
#        except Error as e:
#            print('<p>',e,'</p>')
#        finally:
#            cursor.close()
#            print('<p>Cursor closed</p>')
#########
#    else:
#        print('<p>Unable to connect to MySQL database</p>')
#
#except Error as e:
#        print('<p>',e,'</p>')
#
#finally:
#    if conn is not None and conn.is_connected():
#        conn.close()
#        print('<p>Connection closed</p>')

###########################################################################

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

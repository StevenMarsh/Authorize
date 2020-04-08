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
      zipcode=int(input_data["zip"].value)
      fullname= input_data["fname"].value
      email = input_data["email"].value
      address = input_data["address"].value
      city = input_data["city"].value
      state = input_data["state"].value
      cardname = input_data["cardname"].value
      cardnum = int(input_data["cardnum"].value)
      expmonth = int(input_data["expmonth"].value)
      expyear = int(input_data["expyear"].value)
      cvv = int(input_data["cvv"].value)
      
      sql_command = """INSERT INTO users (fullname, email, address, city, state, zip, name, card, month, year, cvv) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
      
      recordTuple = (fullname, email, address, city, state, zipcode, cardname, cardnum, expmonth, expyear, cvv)
      
      cursor.execute(sql_command, recordTuple)
      
      conn.commit()

    except Error as e:
      print('<p>',e,'</p>')
      print('<p>Sorry, some forms are either incomplete or wrong format.</p>')

    finally:
      print('<p>Done!</p>')
      cursor.close()

except Error as e:
  print('<p>',e,'</p>')

finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print('<p>Connection closed</p>')



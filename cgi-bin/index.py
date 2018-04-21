#!/usr/bin/python3

#Import modules for CGI handling 
import cgi, cgitb 
# import pickle
# cache = pickle.load( open( "cache.p", "rb" ) )
#Create instance of FieldStorage 
form = cgi.FieldStorage() 

#Get data from fields
query_value = form.getvalue('query')

import MySQLdb
db = MySQLdb.connect("localhost","root","Ilovemylife@541236","tpcds")
#cursor = db.cursor()
# f = open('./working_queries/extract13.tpl','r')
# query_value = str(f.read())
# # print(query_value)
# f.close()
result = ""
try:
    # if query_value in cache:
    #     r = cache[query_value]
    
    #cursor.execute(query_value)
    # else:
        db.query(query_value)
        #result = str(cursor.fetchone())
        r = db.store_result()
        # cache[query_value] = r
except:
    result = 'error'

print("""content-type: text/html

    <html><head><title>MySQL and Python on the Web</title></head>
      <body bgcolor=#F0F8FF><h1>Mysql Query Results:</h1>
    """)
for row in r.fetch_row(10):
    row = list(row)
    new = ""
    result = ""
    for r in row:
        r = str(r)
        r = r.replace("&", "&amp;")
        r = r.replace("<", "&lt;")
        r = r.replace(">", "&gt;")
        new += cgi.escape(r) + str(" ")
    result += cgi.escape(new) + "<br>\n"
    # history += cgi.escape(row[0]) + "<br>\n"
    # break

    print(result)

    print("""
    <hr>
        """)
    # pickle.dump(cache, open( "cache.p", "wb" ))

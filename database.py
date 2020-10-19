import psycopg2
from config import DB_PASS
con = psycopg2.connect(
  database="db",
  user="postgres",
  password="%s" % DB_PASS,
  host="localhost",
  port="5432"
)
con.autocommit = True
cursor = con.cursor()
# sql = '''CREATE database db''';
# cursor.execute(sql)
# print('XALUYPS')
cursor.execute('DROP TABLE sometesttable')
print('smth')
con.close()

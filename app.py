from flask import Flask
import pandas as pd
import sqlite3
from config import Configuration

con = sqlite3.connect("/Users/david/flask/app/pharma")
cur = con.cursor()

'''
for row in cur.execute('SELECT * FROM pharma;'):
	print(row)
'''

df = pd.read_sql_query("SELECT * from pharma order by 'PAC-GENBeginDate'", con, parse_dates=['OffMarketDate', 'OnMarketDate', 'AWPBeginDate', 'WACBeginDate', 'DPBeginDate', 'C-AWP-25BeginDate', 'C-CMS-FULBeginDate', 'CMS-FULBeginDate', 'C-AWP-20BeginDate', 'NoneBeginDate', 'FSSBeginDate', 'Big4BeginDate', 'PAC-GENBeginDate', 'PAC-LowGENBeginDate', 'PAC-HiGENBeginDate', 'PAC-RTLGENBeginDate', 'PAC-BrandBeginDate', 'PAC-LowBRBeginDate', 'PAC-HiBRBeginDate', 'PAC-RTLBRBeginDate', 'NADAC-MonBeginDate', 'NADAC-WKBeginDate'])

print(df[['PAC-GENBeginDate']].head(50))

con.close()

app = Flask(__name__)
app.config.from_object(Configuration)

'''
@app.route('/')
def index():
	return 'Hello, Flask!'

@app.route('/hello/<name>')
def hello(name):
	return 'Hello, %s' % name
'''




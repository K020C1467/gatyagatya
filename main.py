#Jinja2を使う場合のテンプレート、myapp.py
from flask import Flask, render_template
import random

# Faskのインスタンスを作成
app = Flask(__name__)

# ルーティングの指定
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/gatya01')
def gatya01():

  num = random.randint(1,100)
  if num <=33:
    card_type = "N"
  elif num <=33+25:
    card_type = "N+"
  elif num <=33+25+20:
    card_type = "R"
  elif num <=33+25+20+15:
    card_type = "R+"
  elif num <=33+25+20+15+5:
    card_type = "SR"    
  else:
    card_type = "SR+"

  return render_template("gatya01.html",card_type=card_type)    

@app.route('/11rengatya01')
def gatya11():
  #変数card_type_listに入れる
  card_type_list =  []

  for i in range(10):
    num = random.randint(1,100)

    if num <=57:
      card_type = "R"
    elif num <=57+30:
      card_type = "R+"
    elif num <=57+30+10:
      card_type = "SR"
    else:
      card_type = "SR+"
    card_type_list.append(card_type)  
  select_num = random.randint(1,10)
  if select_num<11:
    card='SR'

  card_type_list.append(card)
  return render_template('11rengatya01.html',card_type_list = card_type_list)

# デバッグモードでサーバを起動させる
app.run(debug=True, host='0.0.0.0')

# ここまでファイル名をmyapp.py

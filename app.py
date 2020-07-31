# -*- coding:utf-8 -*-
# 引入flask框架，jsonify格式转换，网络请求request库，jieba库，数据库连接pymysql，flask_cors跨域处理
from flask import Flask, jsonify,request
import jieba
import csv
import pymysql
from flask_cors import *
# 初始化flask
app = Flask(__name__)
# 设置全局跨域处理
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# 统计高频词函数
def count_words(s, n):
    w = {}
    sp = s.split()
    for i in sp:
        if i not in w:
            w[i] = 1
        else:
            w[i] += 1
    top = sorted(w.items(), key=lambda item: (-item[1], item[0]))
    top_n = top[:n]
    return top_n
# 测试函数
@app.route('/hello_world')
def hello_world():
    jieba.add_word("51")
    f = open('paperlist.csv', 'r')
    reader = csv.reader(f)
    txt = []
    for row in reader:  # 获取行re
        txt.append(row[6])
    txt.remove("题目")
    txt = ' '.join(txt)  # 连接成字符串
    txt = jieba.lcut(txt)
    excludes = {"基于", "的", "设计", "与", "实现", "及", "和"}
    for word in excludes:  # 此功能可用WordCloud中的stopwords参数来排除词,但有时该参数不起作用，why？I don't know
        while word in txt:
            txt.remove(word)
    txt = ' '.join(txt)
    return txt
# 获取优秀论文函数接口
@app.route('/getlw',methods=['get'])
def getlw():
    # 数据库连接
    db = pymysql.connect(host='121.36.46.96',
                         port=3306,
                         user='root',
                         password='151874DZlw',
                         db='dzlw')
    # SQL语句
    sql1 = "SELECT * FROM stu where excellent=1"
    try:
        # 建立游标
        cur = db.cursor()
        # 执行SQL
        cur.execute(sql1)
        # 获取数据库返回接口
        data=cur.fetchall()
        # 关闭数据库
        db.close()
        # 将数据转换为json格式
        result = jsonify(data)
    # 异常捕获处理
    except Exception as e:
        result=e
    return result
# 获取论文成绩前十
@app.route('/getlw_10',methods=['get'])
def getlw_10():
    db = pymysql.connect(host='121.36.46.96',
                         port=3306,
                         user='root',
                         password='151874DZlw',
                         db='dzlw')
    sql1 = "select * from stu order by scor desc limit 20"
    try:
        cur = db.cursor()
        cur.execute(sql1)
        data=cur.fetchall()
        db.close()
        result = jsonify(data)
    except Exception as e:
        result=e
    return result
# 获取论文总数核优秀论文总数接口
@app.route('/getlw_sum',methods=['get'])
def getlw_sum():
    db = pymysql.connect(host='121.36.46.96',
                         port=3306,
                         user='root',
                         password='151874DZlw',
                         db='dzlw')
    sql = "select count(*) from stu"
    sql1 = "select count(*) from stu where excellent=1"
    try:
        cur = db.cursor()
        cur_1 = db.cursor()
        cur.execute(sql)
        cur_1.execute(sql1)
        t=cur.fetchall()
        t2=cur_1.fetchall()
        temp=[]
        temp.append(t)
        temp.append(t2)
        data=temp
        db.close()
        result = jsonify(data)
    except Exception as e:
        result=e
    return result
# 获取词云高频词接口
@app.route('/get_wordcloud',methods=['get'])
def get_wordcloud():
    db = pymysql.connect(host='121.36.46.96',
                              port=3306,
                              user='root',
                              password='151874DZlw',
                              db='dzlw')
    sql1="SELECT * FROM stu"
    cur = db.cursor()
    if (cur.execute(sql1)):
        reader = cur.fetchall()
        txt=[]
        for row in reader:  # 获取行re
            txt.append(row[2])
        txt = ' '.join(txt)  # 连接成字符串
        txt = jieba.lcut(txt)
        excludes = {"基于", "的", "设计", "与", "实现", "及", "和"}
        for word in excludes:  # 此功能可用WordCloud中的stopwords参数来排除词,但有时该参数不起作用，why？I don't know
            while word in txt:
                txt.remove(word)
        txt = ' '.join(txt)
        db.close()
    data=count_words(txt,70)
    result = jsonify(data)
    return result
# 搜索接口，返回论文相关数据相关
@app.route('/search',methods=['POST'])
def search():
    title=request.form.get('title')
    major=request.form.get('major')
    category=request.form.get('category')
    print(title,major,category)
    db = pymysql.connect(host='121.36.46.96',
                         port=3306,
                         user='root',
                         password='151874DZlw',
                         db='dzlw')
    sql1 = "select * from stu order by scor desc limit 20"
    try:
        # cur = db.cursor()
        # cur.execute(sql1)
        # data = cur.fetchall()
        # db.close()
        data={'status':200,'msg':'ok'}
        result = jsonify(data)
    except Exception as e:
        data={'status':404,'msg':'fail'}
        result = jsonify(data)
    return result
#项目启动入口
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

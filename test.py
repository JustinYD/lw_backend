# -*- coding:utf-8 -*-
import csv
import pymysql
f=open('list.csv', 'r')
reader = csv.reader(f)
txt=[]
for row in reader:#获取行re
    txt.append(row[0])
db = pymysql.connect(host='121.36.46.96',
                              port=3306,
                              user='root',
                              password='151874DZlw',
                              db='dzlw')
cur = db.cursor()
for i in txt:
    sql="update stu set excellent=1 where title='%s'"%i
    cur.execute(sql)
    db.commit()
# def count_words(s, n):
#     """Return the n most frequently occuring words in s."""
#     w = {}
#     sp = s.split()
#     # TODO: Count the number of occurences of each word in s
#     for i in sp:
#         if i not in w:
#             w[i] = 1
#         else:
#             w[i] += 1
#
#     # TODO: Sort the occurences in descending order (alphabetically in case of ties)
#     top = sorted(w.items(), key=lambda item: (-item[1], item[0]))
#     top_n = top[:n]
#     # TODO: Return the top n most frequent words.
#     return top_n
#
# data=count_words("压力 传感器 水库 防洪 报警 系统 树木 年轮 自动 提取 全景 图像 拼接 软件设计 单片机 智能 台灯 智能 除 地膜 机 Django 框架 旅游 网站 STC89C52 单片机 太阳能 路灯 单片机 酒精 浓度 测试仪 Python 飞机票 分析 助手 软件 “ Enjoytime ” 时间 管理 APP 单片机 智能 晾衣架 51 单片机 WIFI 智能家居 stm32 单片机 重量 分拣机 单片机 智能 垃圾 分类 装置 垃圾桶 单片机 智能 浇花 器 智能 高空 清洁 机器人 控制系统 51 单片机 指纹 密码锁 STC89C52 单片机 心率 仪 单片机 智能 健康秤 音乐 喷泉 系统 MYSQL 学生 管理系统 机器 视觉 实验室 人员 闯入 监控 系统 单片机 导盲助 行器 控制系统 出租车 计价器 Matlab 语音 信号处理 孤立 词 识别系统 51 单片机 电子 密码锁 单片机 语音 控制 智能 台灯 STM32 湿度 检测 自动 浇花 系统 Java 进销存 管理系统 大棚 智能 远程 监控 系统 单片机 报警 温度 调控 设备 51 单片机 电梯 控制系统 java swing mysql 企业 进销存 管理系统 canny 算法 图片 视频 边缘 检测 matlab 处理 指纹识别 研究 OLED 时钟 显示 系统",30)
# print(data)
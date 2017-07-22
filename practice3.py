#_*_ coding: utf-8 _*_
import turtle
import time
def main():
    #设置窗口信息
    turtle.title('数据绘制动态路径')
    turtle.setup(800,600,0,0)
    #设置画笔
    pen = turtle.Turtle()
    pen.color("red")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(5)
    #读取文件
    #data=r"D/github/base/data.pub"
    result=[]
    #如果要打开其他位置的本地文件则将第19行替换成如下代码
    #file = open('F:/github/data','r')
    file = open('data','r')
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)
    #新建的txt文件出现编码问题乱码时在settings/editor/cold style/file ecodings/GBK
     #动态绘制
    for i in range(len(result)):
        pen.color((result[i][3],result[i][4],result[i][5]))
        pen.fd(result[i][0])
        if result[i][1]:
            pen.rt(result[i][2])
        else:
            pen.lt(result[i][2])
    pen.goto(0,0)
    time.sleep(2)
if __name__== '__main__':
    main()









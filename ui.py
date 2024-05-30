#本文件用来为main.py提供输入输出的窗口
#在第一阶段的开发中，本文件使用控制台输入输出
#在main.py研发并确认无误后，本文件将会交由Yaoqx进行UI设计
import time as t
import main
import sys

def input_name():
    while True:
        #try:  
        if 1==1:
            names=[]
            names.append(input("请输入主角名："))
            if names[len(names)-1]=="9" or names[len(names)-1]=="2" or names[len(names)-1]=="20230609" or names[len(names)-1]=="20230602" or names[len(names)-1]==names[len(names)-1]=="yqx" or names[len(names)-1]=="mzy" or names[len(names)-1]=="YQX" or names[len(names)-1]=="MZY" or names[len(names)-1]=="yaoqixuan" or names[len(names)-1]=="Maoziyu" or names[len(names)-1]=="Yaoqixuan" or names[len(names)-1]=="Maoziyu" or names[len(names)-1]=="YaoQiXuan" or names[len(names)-1]=="MaoZiYu" or names[len(names)-1]=="YAOQIXUAN" or names[len(names)-1]=="MAOZIYU" or names[len(names)-1]=="姚祁轩" or names[len(names)-1]=="毛子煜":
                print("滚")
                sys.exit()
                
            
            print("请输入配角名，输入end以结束输入")
            while True:
                names.append(input())
                #print(names[len(names)-1]) #debug
                if names[len(names)-1]=="9" or names[len(names)-1]=="2" or names[len(names)-1]=="20230609" or names[len(names)-1]=="20230602" or names[len(names)-1]==names[len(names)-1]=="yqx" or names[len(names)-1]=="mzy" or names[len(names)-1]=="YQX" or names[len(names)-1]=="MZY" or names[len(names)-1]=="yaoqixuan" or names[len(names)-1]=="Maoziyu" or names[len(names)-1]=="Yaoqixuan" or names[len(names)-1]=="Maoziyu" or names[len(names)-1]=="YaoQiXuan" or names[len(names)-1]=="MaoZiYu" or names[len(names)-1]=="YAOQIXUAN" or names[len(names)-1]=="MAOZIYU" or names[len(names)-1]=="姚祁轩" or names[len(names)-1]=="毛子煜":
                    names.pop()
                    raise ValueError("yqx and mzy cannot in this game")

                if names[len(names)-1]=="end":
                    if len(names)<=2:
                        print("人数不足")
                    else:
                        print("选定成功")
                        names.pop()
                        return names


def output(text={"玩原神玩的","原神害了你","不玩原神，你只能过一个相对失败的人生","原神，启动！"}):
    for i in text:
        print(i)


if __name__ == "__main__":
    main.main()

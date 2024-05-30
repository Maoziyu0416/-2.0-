"""
版权声明：
本代码依照mpl2.0协议（https://mozillachina.github.io/MPL/）进行开源，原作者保留代码所有权利
mpl协议规定：

"""


import random as r
import ui
import os

def random(a,b):#随机数，输入a,b，表示希望得到true的概率为：b分之a
    if r.randint(0,b-1)<a:
        return True
    else:
        return False



def main():
    names=ui.input_name()
    state=[]#定义一个套了字典的列表标记当前状态，并且列表love栏是一个数组

    alive_player=[]

    ord=0#用来在循环中表示第几个人
    for i in names:
        state.append({"name":i,"order":ord,"love":[],"be_loved":[],"marry":-1,"hate":[],"alive":True,"no_sex":True})
        alive_player.append(ord)
        ord+=1

    num_player=ord

    event=[]#数组+字典 记录每一个玩家的死因


    #第一轮
    print(names[0]+"从小暗恋"+names[r.randint(1,len(names)-1)])
    print(names[0]+"的白月光是"+names[r.randint(1,len(names)-1)])
    print(names[0]+"的初恋是"+names[r.randint(1,len(names)-1)])
    print(names[0]+"和"+names[r.randint(1,len(names)-1)]+"是青梅竹马")
    print(names[0]+"的第一次给了"+names[r.randint(1,len(names)-1)])





    def update():#更新state数据，删除死人
        for wsq in state:
            if not wsq["alive"]:
                continue #死人 不用管

            for j in wsq["love"]:
                if not state[j]["alive"]:
                    wsq["love"].remove(j)

            for j in wsq["be_loved"]:
                if not state[j]["alive"]:
                    wsq["be_loved"].remove(j)



    def end():
        event.append(names[alive_player[0]]+"是最后的赢家!")
        ui.output(event)
        os.system("cls")



    def create_event():

        print("正片开始：")#debug

        def death_chain(reason_people,reason_num):#先空着，每个人死后，和他结婚的人和爱他的人都有三分之一的概率自杀，因为会产生连锁反应，所以是death_chain
            #reason_num: 0:reason_people死了 1:reason_people结婚了
            reason_text=["死了","结婚了"]

            for i in state[reason_people]["be_loved"]:
                if random(1,3) and state[i]["alive"]:
                    event.append("由于"+names[reason_people]+reason_text[reason_num]+","+names[i]+"自杀了")
                    #rint(event) #debug
                    alive_player.remove(i)
                    state[i]["alive"]=False
                    if(len(alive_player)<=1):
                        end()
                    death_chain(i,0)


        def divorce(a,b,reason):#离婚
            event.append("由于"+names[b]+reason+"，"+names[a]+"和"+names[b]+"离婚了")

            state[a]["marry"]=-1
            state[b]["marry"]=-1

            if not(r.randint(0,5)):
                try:
                    next_a_marriage = r.choice(state[a]["be_loved"])
                    if state[next_a_marriage]["marry"] == -1:
                        # 此人未婚
                        A(a, next_a_marriage)

                    else:
                        # 此人已婚
                        C(next_a_marriage, a)
                    #立刻有人趁虚而入
                except:
                    pass






        #由于事件较为复杂 每个事件定义一个函数
        def A(sub,ob):#大事件： 结婚
            event.append(names[sub]+"和"+names[ob]+"结婚了")

            #更新state
            state[sub]["marry"]=ob
            state[ob]["marry"]=sub

            come_to_marriage_party=""
            for i in alive_player:#遍历幸存玩家
                if r.randint(0,2) and i!=sub and i!=ob:#随机取其他玩家来婚礼现场
                    come_to_marriage_party=come_to_marriage_party+names[i]+","
            come_to_marriage_party.strip(",")
            if len(come_to_marriage_party) <=0:
                come_to_marriage_party+="没人"
            event.append(come_to_marriage_party+"来到了婚礼现场")

            event.append("婚礼现场，一片幸福的气息，然而当晚：")
            before_alive=alive_player
            death_chain(sub,1)
            death_chain(ob,1)
            if before_alive==alive_player:
                event.pop()
                event.append("婚礼美满地结束了")
            else:
                event.append("今晚一共死了"+str(before_alive-alive_player)+"人")



        def B(sub,ob,ComeFromAnotherRootEvent):
            event.append(names[sub]+"爱上了"+names[ob])

            state[sub]["love"].append(ob)
            state[ob]["be_loved"].append(sub)

            if (sub in state[ob]["love"]):
                event.append("因为"+names[ob]+"本就喜欢"+names[sub]+"两人很快就开始谈恋爱")

                if r.randint(0,1):
                    A(sub,ob)

                else:
                    event.append("可惜后来，"+names[sub]+"和"+names[ob]+"分手了")

            elif r.randint(0,2)==0 or ComeFromAnotherRootEvent==1:#双向明恋
                event.append(names[ob]+"也喜欢"+names[sub])

                state[ob]["love"].append(sub)
                state[sub]["be_loved"].append(ob)

                event.append(names[sub]+"和"+names[ob]+"很快就开始谈恋爱")

                if r.randint(0,1):
                    A(sub,ob)

                else:
                    event.append("可惜后来，"+names[sub]+"和"+names[ob]+"分手了")


            elif r.randint(0,2)==1:#单向明恋
                event.append("然而"+names[ob]+"不喜欢"+names[sub])
                if r.randint(0,3)==0:
                    event.append("因此,"+names[sub]+"自杀了")
                    alive_player.remove(sub)
                    if len(alive_player)<=1:
                        end()
                    state[sub]["alive"]=False
                    death_chain(sub,0)

                else:
                    event.append(names[sub]+"得知"+names[ob]+"不喜欢他,很快从阴影中走出来了")
                    state[sub]["love"].remove(ob)
                    state[ob]["be_loved"].remove(sub)

            else:#单向暗恋
                event.append(names[sub]+"为了有朝一日能和"+names[ob]+"在一起，决定将这个秘密藏在心底")



        def C(sub,ob):#sub和ob偷情

            if state[sub]["marry"]==-1 and state[ob]["marry"]==-1:#其实就是谈恋爱
                B(sub,ob,1)
                return

            if state[sub]["marry"]==-1 and state[ob]["marry"]!=-1:
                sub,ob=ob,sub#交换sub,ob

            event.append(names[sub]+"喜欢上"+names[ob]+"，绿了"+names[state[sub]["marry"]])

            if random(1,2):
                D(sub,ob)

            if not(r.randint(0,2)):
                event.append(names[state[sub]["marry"]]+"发现"+names[sub]+"绿了他，开始犹豫是否要和"+names[sub]+"离婚")
                choose_an_event()
                divorce(state[sub]["marry"],sub,"绿了"+names[state[sub]["marry"]])




        def D(sub,ob):#X关系
            event.append(names[sub] + "和" + names[ob] + "发生了X关系")
            if state[sub]["no_sex"]:
                state[sub]["no_sex"] = False
                event.append(names[sub] + "的第一次给了" + names[ob])

            if state[ob]["no_sex"]:
                state[ob]["no_sex"] = False
                event.append(names[ob] + "的第一次给了" + names[sub])



        def choose_an_event():
            choose = r.randint(0, 7)
            sub = 0
            ob = 0
            while sub == ob:
                sub = r.choice(alive_player)
                ob = r.choice(alive_player)

            # 维护起来比较复杂，希望Yaoqx能想出更好的维护方式
            if choose == 0:
                A(sub, ob)
            elif choose == 1:
                B(sub, ob, 0)
            elif choose == 2:
                C(sub, ob)
            elif choose == 3:
                D(sub, ob)



        while len(alive_player)>=2:
            choose_an_event()


    create_event()



    #print(event) #debug


if __name__ == "__main__":
    main()


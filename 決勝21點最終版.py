import tkinter as tk #之後都可以簡稱tk就好
import random



win=tk.Tk() #建立主視窗叫win
win.title("決勝21點")#標題
img=[]
green=tk.PhotoImage(file="green.png")
for i in range(52):
   img.append(tk.PhotoImage(file='img'+str(i)+'.png'))
   
   
#遊戲初始數值


list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51] #原始牌共52張
card=list
number=['K','A','2','3','4','5','6','7','8','9','10','J','Q'] #數字
color=['梅花','方塊','紅心','黑桃'] #花色
Round=int(0)
Apoint1=0 #用於A當作11或1
Apoint2=0 #用於A當作11或1
number_what1=int(0)#讓第"幾"張牌正確顯示
number_what2=int(0)#莊家的第幾張牌
player1_point=int(0)
player2_point=int(0)
True_player1_point=int(0) 
True_player2_point=int(0)      
record1=int(0)
record2=int(0)
record3=int(0)    
record1a=int(0) #莊家紀錄
record2a=int(0)
chips=int(0)
#background
win.geometry("800x600+400+100")#寬*高+固定出現的地方
win.minsize(width=300,height=200)#設定最小視窗
win.maxsize(width=1200,height=800)#設定最大視窗
#win.resizable(0,0) 不讓玩家控制視窗大小

#win.iconbitmap("001.ico") #icon 最左上角的小撲克牌

win.config(bg="green")#顏色

#win.attributes("-alpha",0.657) 透明度

#win.attributes("-topmost",1) 永遠置頂

#image
#img=tk.PhotoImage(file="image1.png") #導入圖片



money=int(10000)
money0=str(money)
money_reply=int(0)
check_add=int(0)
check_start=int(0)
check_reset=int(0)
#function1 籌碼與發前兩張牌

def start_game():
    
    global chips,number_what1,card,color,number,Apoint1,player1_point,number_what2,Apoint2,player2_point,True_player1_point,True_player2_point,money,money_reply,check_add,check_start
    if check_start==1:
        return
    money_reply=int(en.get())
    while True:#籌碼
        try:  
            if money_reply>money:#輸入金額超過財產
                check_money.config(bg="skyblue",text="您的籌碼不足",fg="red")
                return
            if money_reply<=0:#輸入小於0的數字
                check_money.config(bg="skyblue",text="請輸入大於0的整數",fg="red")
                return
            if money_reply>0 and  money_reply<=money:#紀錄輸入金額，先把財產扣掉輸入的錢，最後再結算
                money=money-money_reply
                chips=int(money_reply)
                print(money)
                check_add+=1
                check_start+=1
                break
        except ValueError:#除錯
            check_money.config(bg="skyblue",text="請不要輸入非數字的字元",fg="red")
            return
    point.config(text="%s"%(money),fg="red")
    while True:
    #莊家加前兩張牌
        number_what2+=1#數莊家現在是第幾張牌
        b=random.choice(card) #隨機抽取一張牌當作b
        card.remove(b) #抽到的卡刪掉，避免重複抽到一樣的卡
        pre_card_number2=int(b%13) #讓1~52能有對照的數字

    

        
                
        if number_what2==1: #紀錄莊家的牌，並回報給閒家
            p2c1.config(image=img[b])
        if number_what2==2: #紀錄莊家的牌，並回報給閒家
            p2c2.config(image=img[b])
    
        if pre_card_number2==1:
            Apoint2+=1 #用於A當作11或1
        if pre_card_number2==11 or pre_card_number2==12 or pre_card_number2==0:#JQK計10點
            player2_score=10
        else:
            player2_score=pre_card_number2#紀錄當下卡片數字
        player2_point=player2_point+player2_score#加當下卡片數字到總和
        if Apoint2!=0 and player2_point<=11:#如果有A的存在，可能要多+10
            True_player2_point=player2_point+10
        else:#沒有A的存在或點數超過11了，照常
            True_player2_point=player2_point
        if number_what2==1:#讓玩家一開始就拿到兩張牌
            continue
        elif number_what2==2:
            break
   
    
    while True: 
        #閒家家前兩張牌
        number_what1+=1#數現在是第幾張牌
        a=random.choice(card) #隨機抽取一張牌當作a
        card.remove(a) #抽到的卡刪掉，避免重複抽到一樣的卡
        pre_card_number1=int(a%13) #讓1~52能有對照的數字
        
        
        if number_what1==1: #紀錄玩家的牌
            p1c1.config(image=img[a])
        if number_what1==2: #紀錄莊家的牌，並回報給閒家
            p1c2.config(image=img[a])
    
        if pre_card_number1==1:
            Apoint1+=1 #用於A當作11或1
        if pre_card_number1==11 or pre_card_number1==12 or pre_card_number1==0:#JQK計10點
            player1_score=10
        else:
            player1_score=pre_card_number1#紀錄當下卡片數字
        player1_point=player1_point+player1_score#加當下卡片數字到總和
        if Apoint1!=0 and player1_point<=11:#如果有A的存在，可能要多+10
            True_player1_point=player1_point+10
        else:#沒有A的存在或點數超過11了，照常
            True_player1_point=player1_point
        if number_what1==1:#記錄前三張牌的數字，可能有特殊牌
            record1=player1_score
        elif number_what1==2:
            record2=player1_score
        if number_what1==1:#讓玩家一開始就拿到兩張牌
            continue
        elif number_what1==2:
            break
        
        
    return chips,player2_point,number_what2,Apoint2,player1_point,number_what1,Apoint1,record1,record2,card,True_player1_point,True_player2_point,money,money_reply,check_add,check_start

#function2加牌
def add_card():
    global chips,number_what1,card,color,number,Apoint1,player1_point,record3,True_player1_point,True_player2_point,money_reply,check_add
    if check_add==0:
        return
    if True_player1_point<21:
        number_what1+=1#數現在是第幾張牌
        a=random.choice(card) #隨機抽取一張牌當作a
        card.remove(a) #抽到的卡刪掉，避免重複抽到一樣的卡
        pre_card_number1=int(a%13) #讓1~52能有對照的數字
        pre_card_color1=int((a-pre_card_number1)/13) #讓1~52能有對照的花色
                
        P1C=(color[pre_card_color1]+number[pre_card_number1])
                
        if number_what1==3: #紀錄玩家的牌
            p1c3.config(image=img[a])
        if number_what1==4: #紀錄玩家的牌
            p1c4.config(image=img[a])
        if number_what1==5: #紀錄玩家的牌
            p1c5.config(image=img[a])
                
        if pre_card_number1==1:
            Apoint1+=1 #用於A當作11或1
        if pre_card_number1==11 or pre_card_number1==12 or pre_card_number1==0:#JQK計10點
            player1_score=10
        else:
            player1_score=pre_card_number1#紀錄當下卡片數字
        player1_point=player1_point+player1_score#加當下卡片數字到總和
        if Apoint1!=0 and player1_point<=11:#如果有A的存在，可能要多+10
            True_player1_point=player1_point+10
        else:#沒有A的存在或點數超過11了，照常
            True_player1_point=player1_point
        if number_what1==3:#記錄前三張牌的數字，可能有特殊牌
            record3=player1_score
        if True_player1_point>21:
            money_reply=0
            con.config(bg="skyblue",text="你爆牌了QQ"+'\n'+'莊家獲勝',fg="red")
            con_money.config(bg="skyblue",text='您在這局遊戲共輸了%s元'%(chips),fg="red")
            
            
            
        return number_what1,card,color,number,Apoint1,player1_point,record3,True_player1_point,True_player2_point,chips,money_reply,money
#fuction3結算
def conclusion():
    global chips,money,money_reply,number_what1,record1,record2,record3,True_player1_point,True_player2_point,number_what2,player2_point,Apoint2,check_reset
    check_reset+=1
    if money_reply==0:
        return
    if check_add==0:
        return
    while True_player2_point<=True_player1_point and True_player1_point<=20 and number_what1!=5:           #輪莊家取第三第四張牌
        if True_player2_point==True_player1_point and True_player2_point>13:
            break
        number_what2+=1#數莊家現在是第幾張牌
        b=random.choice(card) #隨機抽取一張牌當作b
        card.remove(b) #抽到的卡刪掉，避免重複抽到一樣的卡
        pre_card_number2=int(b%13) #讓1~52能有對照的數字
        pre_card_color2=int((b-pre_card_number2)/13) #讓1~52能有對照的花色
    
        P2C=(color[pre_card_color2]+number[pre_card_number2])
        
        if number_what2==3:
            p2c3.config(image=img[b])
        if number_what2==4:
            p2c4.config(image=img[b])
        if number_what2==5:
            p2c5.config(image=img[b])
            
        if pre_card_number2==1:
                Apoint2+=1 #用於A當作11或1
        if pre_card_number2==11 or pre_card_number2==12 or pre_card_number2==0:#JQK計10點
                player2_score=10
        else:
            player2_score=pre_card_number2#紀錄當下卡片數字
        player2_point=player2_point+player2_score#加當下卡片數字到總和
        if Apoint2!=0 and player2_point<=11:#如果有A的存在，可能要多+10
            True_player2_point=player2_point+10
        else:#沒有A的存在或點數超過11了，照常
            True_player2_point=player2_point
        
        if True_player2_point>21:
            con.config(bg="skyblue",text="莊家爆牌!",fg="red")
            money_reply=money_reply*2
            break
            

                
        if number_what2==5 and True_player2_point<=21:#過五關
            con.config(bg="skyblue",text="莊家過五關!",fg="red")
            money_reply=0
            break
        if True_player2_point==21:#莊家得到21點
            con.config(bg="skyblue",text="莊家21點!",fg="red")
            money_reply=0
            break
    
    
    
    
    if number_what1==5 and True_player1_point<=21:
        con.config(bg="skyblue",text="過五關,獎金三倍",fg="red")
        money_reply=money_reply*4
    elif True_player1_point==21:#玩家得到21點後，可能有下面三種情況   
        if record1==7 and record2==7 and record3==7:
            con.config(bg="skyblue",text="恭喜您得到三條7!獎金25倍!",fg="red")
            money_reply=money_reply*26
        elif record1==6 or record1==7 or record1==8:
            if record2==6 or record2==7 or record2==8:
                if record3==6 or record3==7 or record3==8:
                    con.config(bg="skyblue",text="恭喜您得到順子678!獎金十倍!",fg="red")
                    money_reply=money_reply*11
                else:
                    con.config(bg="skyblue",text="恭喜您剛好有21點!獎金加倍!",fg="red")
                    money_reply=money_reply*3
            else:
                con.config(bg="skyblue",text="恭喜您剛好有21點!獎金加倍!",fg="red")
                money_reply=money_reply*3
        else:
            con.config(bg="skyblue",text="恭喜您剛好有21點!獎金加倍!",fg="red")
            money_reply=money_reply*3
    
    elif True_player2_point==True_player1_point and True_player1_point!=21 and number_what2!=5 and True_player2_point!=21:
         con.config(bg="skyblue",text="和局!",fg="red")
    elif True_player2_point>True_player1_point and True_player2_point<21:
         con.config(bg="skyblue",text="莊家獲勝",fg="red")
         money_reply=0
    money=money+money_reply
    if money_reply==0:
        print('您在這局遊戲共輸了%s元'%(chips))
        con_money.config(bg="skyblue",text='您在這局遊戲共輸了%s元'%(chips),fg="red")
    else:
        print('您在這局共獲得了%d元'%(money_reply-chips))
        con_money.config(bg="skyblue",text='您在這局共獲得了%d元'%(money_reply-chips),fg="red")
    if money==0:#破產
        print('您已破產QQ')
        con_money.config(bg="skyblue",text="您已破產QQ",fg="red")
    point.config(text="%s"%(money),fg="red")
    money_reply=0
    return chips,money,money_reply,number_what1,record1,record2,record3,True_player1_point,True_player2_point,number_what2,player2_point,Apoint2,check_reset

#fuction4再來一局
def reset():
    global Round,Apoint1,Apoint2,number_what1,number_what2,player1_point,player2_point,True_player1_point,True_player2_point,record1,record2,record3,chips,money_reply,card,list,check_start,check_add,check_reset
    if check_reset==0:
        return
    list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
    p1c1.config(image=green)
    p1c2.config(image=green)
    p1c3.config(image=green)
    p1c4.config(image=green)
    p1c5.config(image=green)
    p2c1.config(image=green)
    p2c2.config(image=green)
    p2c3.config(image=green)
    p2c4.config(image=green)
    p2c5.config(image=green)
    con_money.config(bg="green",fg="green")
    con.config(bg="green",fg="green")
    check_money.config(bg='green',text='')
    Round=int(0)
    Apoint1=0 #用於A當作11或1
    Apoint2=0 #用於A當作11或1
    number_what1=int(0)#讓第"幾"張牌正確顯示
    number_what2=int(0)#莊家的第幾張牌
    player1_point=int(0)
    player2_point=int(0)
    True_player1_point=int(0) 
    True_player2_point=int(0)      
    record1=int(0)
    record2=int(0)
    record3=int(0)    
    chips=int(0)
    money_reply=int(0)
    card=list
    check_start=int(0)
    check_add=int(0)
    check_reset=int(0)
    return Round,Apoint1,Apoint2,number_what1,number_what2,player1_point,player2_point,True_player1_point,True_player2_point,record1,record2,record3,chips,money_reply,card,check_start,check_add,check_reset
    
#label(放字在介面上)
#lb=tk.Label(bg="lightgreen",text="你贏囉",fg="red")
#lb.config(font="微軟正黑體 22")#字型 大小
point=tk.Label(bg="green",fg="red")
#lb.pack()
point.pack()
  #莊家前兩張
p2c1=tk.Label(width=100,height=150)
p2c1.config(bg='green')

p2c1.place(x=50,y=100)

p2c2=tk.Label(width=100,height=150)
p2c2.config(bg='green')

p2c2.place(x=150,y=100)

    #莊家加牌
p2c3=tk.Label(width=100,height=150)
p2c3.config(bg='green')

p2c3.place(x=250,y=100)

p2c4=tk.Label(width=100,height=150)
p2c4.config(bg='green')

p2c4.place(x=350,y=100)

p2c5=tk.Label(width=100,height=150)
p2c5.config(bg='green')

p2c5.place(x=450,y=100)
  #閒家前兩張
p1c1=tk.Label(width=100,height=150)
p1c1.config(bg='green')

p1c1.place(x=50,y=300)

p1c2=tk.Label(width=100,height=150)
p1c2.config(bg='green')

p1c2.place(x=150,y=300)

    #閒家加牌
p1c3=tk.Label(width=100,height=150)
p1c3.config(bg='green')

p1c3.place(x=250,y=300)

p1c4=tk.Label(width=100,height=150)
p1c4.config(bg='green')

p1c4.place(x=350,y=300)

p1c5=tk.Label(width=100,height=150)
p1c5.config(bg='green')
p1c5.place(x=450,y=300)
    #結算
con=tk.Label(width=25,height=3)
con.config(bg='green')
con.place(x=550,y=20)

con_money=tk.Label(width=25,height=3)
con_money.config(bg='green')
con_money.place(x=550,y=60)
    #除錯
check_money=tk.Label(width=25,height=3)
check_money.place(x=100,y=30)
check_money.config(bg='green')
#entry(讓玩家可以輸入籌碼)
en = tk.Entry()
en.pack()



#button2 開始遊戲的按鈕
start_btn=tk.Button(text="下注",font="微軟正黑體 22")
start_btn.config(command=start_game)
start_btn.place(anchor="s",x=600,y=300,width=100,height=50)
#button3加牌按鈕
add_btn=tk.Button(text="加牌",font="微軟正黑體 22")
add_btn.config(command=add_card)
add_btn.place(anchor="s",x=710,y=300,width=100,height=50)
#button4 結算
conclu_btn=tk.Button(text="結算",font="微軟正黑體 22")
#conclu_btn.config(command=add_card2)
conclu_btn.config(command=conclusion)
conclu_btn.place(anchor="s",x=655,y=350,width=210,height=50)
#button5 reset

reset_btn=tk.Button(text="再來一局",font="微軟正黑體 22")
reset_btn.config(command=reset)
reset_btn.place(anchor="s",x=655,y=400,width=210,height=50)

#btn2 = tk.Button(text="加牌")#設置按鈕
#btn2.config(bg="") 可以調整按鈕顏色
#btn2.config(width=200,height=500) #可以調整按鈕大小
#btn2.config(image=img)#把button變成圖片
#btn2.config(command= add_card)
#btn2.pack()#放置

#scale可能可以加入籌碼功能
point.config(text="%s"%(money),fg="red")
win.mainloop()#常駐主視窗



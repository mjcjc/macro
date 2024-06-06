from tkinter import *
from src import reservation
import tkinter.ttk as ttk




#티켓 화면
def ticket_frame():
    frame3.lift()
    prev_frame = Frame(root, relief='solid')
    prev_frame.place(x=0, y=100, width=400, height=350)
    Button(prev_frame, text='메인으로 가기', command= main_frame).pack(side='right')

times = ['12:00','2:00','3:00','4:00','5:00','6:00']
getimes = None
getdays = None
getid = None
getpw = None
getpw2 = None
#헤어숍 화면
#여기에다가 아이디 비밀번호 2차 비밀번호 넣는거 해야함.
#일단 성공 했는데 
def hair_frame():
    frame2.lift()
    prev_frame = Frame(root, relief='solid')
    prev_frame.place(x=0, y=100, width=400, height=350)
    Button(prev_frame, text='메인으로 가기', command= main_frame).pack(side='right')
    comboboxday = ttk.Combobox(root, height=5, values=reservation.dates)
    comboboxday.place(x=100, y=80)  
    comboboxday.set("날짜 클릭")
    comboboxtime = ttk.Combobox(root, height=6, values=times)
    comboboxtime.place(x=100, y=100)
    getdays = comboboxtime.get()
    comboboxtime.set("시간 클릭")
    getimes = comboboxtime.get()
    

    #수정 끝났고 이제 값 받아서 payment에 넘겨서 결제하는거 해야함.
    # idText = Entry(root, width=10)
    # idText.place(x=100, y=140)  # place 메서드를 사용하여 위치 지정
    # idText.insert(0,"아이디")
    # getid = idText.get()
    # pwText = Entry(root, width=10)
    # pwText.place(x=100, y=160)
    # pwText.insert(0,"비밀번호")
    # getpw = pwText.get()
    # pw2Text = Entry(root,width=10)
    # pw2Text.place(x=100, y=180)
    # pw2Text.insert(0,"2차 비밀번호")
    # getpw2 = pw2Text.get()

    #이거 참고하면서 내 코드 수정하면 될 듯 show기능 좋은 거 같다.
    label = ttk.Label(root, text="Login :")
    label.place(x=90, y=160)

    idText = ttk.Entry(root)
    idText.place(x=100, y=160)

    label = ttk.Label(root, text="Password :")
    label.place(x=90, y=180)

    pwText = ttk.Entry(root, show="*")
    pwText.place(x=100, y=180)

    label = ttk.Label(root, text="2차 비밀번호 :")
    label.place(x=90, y=200)

    pw2Text = ttk.Entry(root, show="*")
    pw2Text.place(x=100, y=200)
    
# 메인화면
def main_frame():
    frame1.lift()
    btn_frame = Frame(root, relief='solid')
    btn_frame.place(x=0, y=100, width=400, height=350)
    Button(btn_frame,text='헤어숍', command=hair_frame).pack()
    Button(btn_frame,text='티켓 예매', command=ticket_frame).pack()

root = Tk()
root.title("예약 매크로")
root.geometry("400x300+300+300")

frame3 = Frame(root, relief='solid' )
frame2 = Frame(root, relief='solid')
frame1 = Frame(root, relief='solid')

btn_frame = Frame(root, relief='solid')

frame3.place(x=0, y=0, width=400, height=250)
frame2.place(x=0, y=0, width=400, height=250)
frame1.place(x=0, y=0, width=400, height=250)  # 이 프레임이 가장 먼저 나타남
btn_frame.place(x=0, y=100, width=400, height=350)  # 밑 바닥에 이전과 다음이 있을 버튼 영역

#Label(frame3, text="티켓예매", font=('consolas', 20)).pack()
Label(frame2, text="헤어숍", font=('consolas', 20)).pack()
Label(frame1, text="메인", font=('consolas', 20)).pack()

Button(btn_frame, text='헤어숍', command=hair_frame).pack()
Button(btn_frame, text='티켓 예매', command=ticket_frame).pack()

root.mainloop()




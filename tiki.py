from tkinter import *
from src import reservation
import tkinter.ttk as ttk


times = []
getimes = None
getid = None
getpw = None
getpw2 = None
comboboxday = None
combotimes = None

def hair_frame():
    global comboboxday
    global getid
    global getpw
    global getpw2
    frame2.lift()
    prev_frame = Frame(root, relief='solid')
    prev_frame.place(x=0, y=100, width=400, height=350)
    Button(prev_frame, text='메인으로 가기', command= main_frame).pack(side='right')
    comboboxday = ttk.Combobox(root, height=5, values=reservation.getDays())
    comboboxday.place(x=100, y=80)  
    comboboxday.set("날짜 클릭")
    day_select = Frame(root, relief='solid')
    day_select.place(x=200, y=100, width= 100, height= 100)
    Button(day_select,text='날짜 선택', command= abletime).pack(side='right')
    final_select =Frame(root, relief='solid')
    final_select.place(x=300, y=120, width= 50, height=50)
    Button(final_select,text='제출', command=final_frame).pack(side='right')
    
    label = ttk.Label(root, text="Login :")
    label.place(x=90, y=160)
    # 이거 여기 다시 생각해야해 그냥 이 함수에서 받아오면 getid나 그런 값들이 paymentF에서 분명 None으로 들어갈거임
    #구조를 생각해보자, 먼저 클릭하고 날짜를 클릭한 뒤 날짜 확인을 하면 reservation으로 이동을 하고 거기서 시간값을 다시 받아오고
    #그 시간값 을 받아서 다시 reservation times를 가져오고 그 시간을 선택함.
    #그리고 아이디 비밀번호를 입력을 
    idText = ttk.Entry(root)
    idText.place(x=140, y=160)
    getid = idText.get()

    label = ttk.Label(root, text="Password :")
    #x값 수정 필요
    label.place(x=60, y=180)

    pwText = ttk.Entry(root, show="*")
    pwText.place(x=140, y=180)
    getpw = pwText.get()

    label = ttk.Label(root, text="2차 비밀번호 :")
    #x값 수정 필요
    label.place(x=60, y=200)

    pw2Text = ttk.Entry(root, show="*")
    pw2Text.place(x=140, y=200)
    getpw2 = pw2Text.get()

def abletime(): 
    global combotimes
    combotimes = ttk.Combobox(root, height=6, values=reservation.getTimes())
    combotimes.place(x=100, y=100)
    combotimes.set("시간 클릭")

def res_day():
    return comboboxday.get()


def res_times():
    #쓰레기값 들어감 ㅋㅋ시바
    return combotimes.get()
#티켓 화면
def ticket_frame():
    frame3.lift()
    prev_frame = Frame(root, relief='solid')
    prev_frame.place(x=0, y=100, width=400, height=350)
    Button(prev_frame, text='메인으로 가기', command= main_frame).pack(side='right')
# 메인화면
def main_frame():
    frame1.lift()
    btn_frame = Frame(root, relief='solid')
    btn_frame.place(x=0, y=100, width=400, height=350)
    Button(btn_frame,text='헤어숍', command=hair_frame).pack()
    Button(btn_frame,text='티켓 예매', command=ticket_frame).pack()
def identyF():
    #여기서 정보를 리턴해주는 값을 해야할 듯
    pass
def final_frame():
    reservation.paymentF()

root = Tk()
root.title("예약 매크로")
root.geometry("400x300+300+300")

frame4 = Frame(root, relief='solid')
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
#Button(btn_frame, text='티켓 예매', command=ticket_frame).pack()

root.mainloop()




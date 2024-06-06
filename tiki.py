from tkinter import *
from src import reservation
import tkinter.ttk as ttk





times = []
getimes = None
getid = None
getpw = None
getpw2 = None
comboboxday = None
#버튼으로 값을 넣어줬다고 얘기를 안 줬음.

def hair_frame():
    global comboboxday
    frame2.lift()
    prev_frame = Frame(root, relief='solid')
    prev_frame.place(x=0, y=100, width=400, height=350)
    Button(prev_frame, text='메인으로 가기', command= main_frame).pack(side='right')
    comboboxday = ttk.Combobox(root, height=5, values=reservation.getDays())
    comboboxday.place(x=100, y=80)  
    comboboxday.set("날짜 클릭")
    prev_frame2 = Frame(root, relief='solid')
    prev_frame2.place(x=200, y=100, width= 100, height= 100)
    Button(prev_frame2,text='날짜 선택', command= abletime).pack(side='right')
    
    #getdays를 하고 버튼으로 확인을 한 뒤에 콤보박스를 또 띄워줘야함. 그걸 안해줘서 지금 값이 안 넘어간 거 같음.
    #Button(prev_frame,text='날짜 확인',).pack
    
    
    #이거 참고하면서 내 코드 수정하면 될 듯 show기능 좋은 거 같다.
    label = ttk.Label(root, text="Login :")
    label.place(x=90, y=160)

    idText = ttk.Entry(root)
    idText.place(x=140, y=160)

    label = ttk.Label(root, text="Password :")
    #x값 수정 필요
    label.place(x=60, y=180)

    pwText = ttk.Entry(root, show="*")
    pwText.place(x=140, y=180)

    label = ttk.Label(root, text="2차 비밀번호 :")
    #x값 수정 필요
    label.place(x=60, y=200)

    pw2Text = ttk.Entry(root, show="*")
    pw2Text.place(x=140, y=200)
def res_day():
    return comboboxday.get()

def abletime():
    
    comboboxtime = ttk.Combobox(root, height=6, values=reservation.getTimes())
    comboboxtime.place(x=100, y=100)
    comboboxtime.set("시간 클릭")
    getimes = comboboxtime.get()
    
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
#Button(btn_frame, text='티켓 예매', command=ticket_frame).pack()

root.mainloop()




from tkinter import *
from src import reservation
import tkinter.ttk as ttk
def ticket_frame():
    frame3.lift()
    prev_frame = Frame(root, relief='solid')
    prev_frame.place(x=0, y=100, width=400, height=350)
    Button(prev_frame, text='메인으로 가기', command= main_frame).pack(side='right')
    combobox = ttk.Combobox(root, height=5, values=reservation.dates)
    combobox.set("날짜 클릭")
    combobox.pack()

def hair_frame():
    frame2.lift()
    prev_frame = Frame(root, relief='solid')
    prev_frame.place(x=0, y=100, width=400, height=350)
    Button(prev_frame, text='메인으로 가기', command= main_frame).pack(side='right')

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

Label(frame3, text="티켓예매", font=('consolas', 20)).pack()
Label(frame2, text="헤어숍", font=('consolas', 20)).pack()
Label(frame1, text="메인", font=('consolas', 20)).pack()

Button(btn_frame, text='헤어숍', command=hair_frame).pack()
Button(btn_frame, text='티켓 예매', command=ticket_frame).pack()

root.mainloop()




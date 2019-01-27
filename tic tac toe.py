import tkinter as tk
import tkinter.messagebox


def resetboard():
	global turn
	turn=0
	button1["text"]=button2["text"]=button3["text"]=button4["text"]=button5["text"]=button6["text"]=button7["text"]=button8["text"]=button9["text"]=""
	button1["bg"]=button2["bg"]=button3["bg"]=button4["bg"]=button5["bg"]=button6["bg"]=button7["bg"]=button8["bg"]=button9["bg"]="white"
def mark(num):
	global turn
	turn += 1
	if turn%2==0:
		marker="O"
	else:
		marker="X"
	if num==1:
		button1["text"]=marker
	elif num==2:
		button2["text"]=marker
	elif num==3:
		button3["text"]=marker
	elif num==4:
		button4["text"]=marker
	elif num==5:
		button5["text"]=marker
	elif num==6:
		button6["text"]=marker
	elif num==7:
		button7["text"]=marker
	elif num==8:
		button8["text"]=marker
	else:
		button9["text"]=marker
	# print(turn)
	if check()=="player 1 wins":
		tk.messagebox.showinfo("Winner", "Player 1 won")
		resetboard()
	if check()=="player 2 wins":
		tk.messagebox.showinfo("Winner", "Player 2 won")
		resetboard()
	if check()=="" and turn==9:
		tk.messagebox.showinfo("Draw", "it was a draw")
		resetboard()
def check():
	if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
		button1["bg"]="green"
		button2["bg"]="green"
		button3["bg"]="green"
		return "player 1 wins"
	elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
		button4["bg"]="green"
		button5["bg"]="green"
		button6["bg"]="green"
		return "player 1 wins"
	elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
		button7["bg"]="green"
		button8["bg"]="green"
		button9["bg"]="green"
		return "player 1 wins"
	elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
		button1["bg"]="green"
		button4["bg"]="green"
		button7["bg"]="green"
		return "player 1 wins"
	elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
		button2["bg"]="green"
		button5["bg"]="green"
		button8["bg"]="green"
		return "player 1 wins"
	elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
		button3["bg"]="green"
		button6["bg"]="green"
		button9["bg"]="green"
		return "player 1 wins"
	elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
		button1["bg"]="green"
		button5["bg"]="green"
		button9["bg"]="green"
		return "player 1 wins"
	elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
		button3["bg"]="green"
		button5["bg"]="green"
		button7["bg"]="green"
		return "player 1 wins"
	elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
		button1["bg"]="green"
		button2["bg"]="green"
		button3["bg"]="green"
		return "player 2 wins"
	elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
		button4["bg"]="green"
		button5["bg"]="green"
		button6["bg"]="green"
		return "player 2 wins"
	elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
		button7["bg"]="green"
		button8["bg"]="green"
		button9["bg"]="green"
		return "player 2 wins"
	elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
		button1["bg"]="green"
		button4["bg"]="green"
		button7["bg"]="green"
		return "player 2 wins"
	elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
		button2["bg"]="green"
		button5["bg"]="green"
		button8["bg"]="green"
		return "player 2 wins"
	elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
		button3["bg"]="green"
		button6["bg"]="green"
		button9["bg"]="green"
		return "player 2 wins"
	elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
		button1["bg"]="green"
		button5["bg"]="green"
		button9["bg"]="green"
		return "player 2 wins"
	elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
		button3["bg"]="green"
		button5["bg"]="green"
		button7["bg"]="green"
		return "player 2 wins"
	else:
		return ""
turn=0
window =tk.Tk()
window.title("Tic Tok")
window.geometry("319x313")
button1=tk.Button(text="", height=2,width=5,fg="red",padx=5, pady=5,command=lambda: mark(1),bg="white",font=('Helvetica', '15'))
button1.grid(column=0, row=1,padx= (50,0),pady= (50,0))
button2=tk.Button(text="",height=2,width=5,padx=5, pady=5,fg="red",command=lambda: mark(2),bg="white",font=('Helvetica', '15'))
button2.grid(column=0, row=2,padx= (50,0))
button3=tk.Button(text="",height=2,width=5,fg="red",command=lambda: mark(3),padx=5, pady=5,bg="white",font=('Helvetica', '15'))
button3.grid(column=0, row=3,padx= (50,0))
button4=tk.Button(text="",height=2,width=5,command=lambda: mark(4),fg="red",padx=5, pady=5,bg="white",font=('Helvetica', '15'))
button4.grid(column=1, row=1,pady= (50,0))
button5=tk.Button(text="",height=2,width=5,command=lambda: mark(5),fg="red",padx=5, pady=5,bg="white",font=('Helvetica', '15'))
button5.grid(column=1, row=2)
button6=tk.Button(text="",height=2,width=5,command=lambda: mark(6),fg="red",padx=5, pady=5,bg="white",font=('Helvetica', '15'))
button6.grid(column=1, row=3)
button7=tk.Button(text="",height=2,width=5,command=lambda: mark(7),fg="red",padx=5, pady=5,bg="white",font=('Helvetica', '15'))
button7.grid(column=2, row=1,pady= (50,0))
button8=tk.Button(text="",height=2,width=5,command=lambda: mark(8),fg="red",padx=5, pady=5,bg="white",font=('Helvetica', '15'))
button8.grid(column=2, row=2)
button9=tk.Button(text="",height=2,width=5,command=lambda: mark(9),fg="red",padx=5, pady=5,bg="white",font=('Helvetica', '15'))
button9.grid(column=2, row=3)

window.mainloop()
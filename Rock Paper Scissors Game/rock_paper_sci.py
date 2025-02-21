from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Stone Paper Scissor Game")
root.configure(background = "black")

stone_img = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor_user.png"))
stone_comp_img = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_comp_img = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_comp_img = ImageTk.PhotoImage(Image.open("scissor_user.png"))


user_label = Label(root, image=scissor_img, bg="black")
comp_label = Label(root, image=scissor_comp_img, bg="black")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)


playerScore = Label(root, text=0, font=100, bg="black", fg="aqua")
computerScore = Label(root, text=0, font=100, bg="black", fg="aqua")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)


user_indicator = Label(root, font=50, text="USER", bg="black", fg="deeppink")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="black", fg="deeppink")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)


msg = Label(root, font=50, bg="black", fg="white")
msg.grid(row=3, column=2)

def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score =int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score =int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)


def checkWinner(player, computer):
    if player == computer:
        updateMessage("It's a tie !!!")
    elif player == "stone":
        if computer == "paper":
            updateMessage("You loose!!")
            updateCompScore()
        else:
            updateMessage("You Won!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose!!")
            updateCompScore()
        else:
            updateMessage("You Won!!")
            updateUserScore()
    elif player == "scissor":
        if computer == "stone":
            updateMessage("You loose!!")
            updateCompScore()
        else:
            updateMessage("You Won!!")
            updateUserScore()
    else:
        pass




stone = Button(root, width=20, height=2, text="STONE", bg="#FF3E4D", fg="white", command= lambda:updateChoice("stone")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#0ABDE3", fg="white", command= lambda:updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#FAD02E", fg="white", command= lambda:updateChoice("scissor")).grid(row=2, column=3)

choices = ["stone", "paper", "scissor"]
def updateChoice(x):
 #for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "stone":
        comp_label.configure(image=stone_comp_img)
    elif compChoice == "paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissor_comp_img)



 #for users   
    if x=="stone":
        user_label.configure(image=stone_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWinner(x, compChoice)



root.mainloop()
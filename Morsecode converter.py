from tkinter import * 
code = {"A":".-",
"B":"-...",
"C":"-.-.",
"D":"-..",
"E":".",
"F":"..-.",
"G":"--.",
"H":"....",
"I":"..",
"J":".---",
"K":"-.-",
"L":".-..",
"M":"--",
"N":"-.",
"O":"---",
"P":".--.",
"Q":"--.-",
"R":".-.",
"S":"...",
"T":"-",
"U":"..-",
"V":"...-",
"W":".--",
"X":"-..-",
"Y":"-.--",
"Z":"--..",
".-":"A",
"-...":"B",
"-.-.":"C",
"-..":"D",
".":"E",
"..-.":"F",
"--.":"G",
"....":"H",
"..":"I",
".---":"J",
"-.-":"K",
".-..":"L",
"--":"M",
"-.":"N",
"---":"O",
".--.":"P",
"--.-":"Q",
".-.":"R",
"...":"S",
"-":"T",
"..-":"U",
"...-":"V",
".--":"W",
"-..-":"X",
"-.--":"Y",
"--..":"Z"
}

def Convert():
    sentence = ""
    command = E1.get()
    if(var.get()):
        words = command.split("/")
        for word in words:
            for letter in word.split(" "):
                sentence = sentence + str(code[letter])
            sentence = sentence + " "
    else:
        words = command.split(" ")
        for word in words:
            for letter in word:
                sentence = sentence + str(code[letter.upper()]) + " "
            sentence = sentence + "/"
    print(sentence)
    L2.configure(text= sentence)




root = Tk()             
root.geometry('400x400')

L1 = Label(root, text="Enter your text here: \nSeperate sentence with slash")
L1.grid(row = 0, column = 0, sticky = W, pady = 1)

E1 = Entry(root, bd =5)
E1.grid(row = 0, column = 1, sticky = W, pady = 2)


var = IntVar()
chk = Checkbutton(root, text='Check if conversion is from code to text', variable=var)
chk.grid(row = 5, column = 0, sticky = W, pady = 4)

B1 = Button(root, text = 'Convert', bd = '5', command = Convert)
B1.grid(row = 6, column = 1, sticky = W, pady = 3)


L2 = Label(root, text = "Converted text")
L2.grid(row = 7, column = 0, sticky = W, pady = 5)





root.mainloop()

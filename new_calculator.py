"""This is a project on calculator.
"""

from tkinter import *
import math
import time


class gui():

    # class variables (i.e same as static variables in other programming languages).
    initialval=-1
    sum,sub,mul,div,pow='a','b','c','d','e'

    def __init__(self):
        self.win=Tk()
        self.win.resizable(0,0)           # this is inorder to avoid resizable.
        self.win.configure(bg="pink")     #this is for background as pink

        # my calculator name
        self.calculator_text=Label(self.win,text="SHIVA-CALCULATOR",bg='brown',fg="white",height="2",width="62");
        self.calculator_text.grid(row=0,columnspan=5,padx=0,pady=0,sticky=W)

        #this block is for result box, button from 7 to 9 with off and multiply button
        self.result_box=Label(self.win,text="Start the Calculator",bg="white",fg="black",height="3",width="61");
        self.result_box.grid(row=1,columnspan=5,padx=5,pady=2,sticky=W)
        self.but_7=Button(self.win,text="7",width=11,height=2,command=lambda : self.btnclick(7));
        self.but_8=Button(self.win,text="8",width=11,height=2,command=lambda : self.btnclick(8));
        self.but_9=Button(self.win,text="9",width=11,height=2,command=lambda : self.btnclick(9));
        self.but_x=Button(self.win,text="x",width=10,height=2,command=self.pressmul);
        self.but_off=Button(self.win,text="Off",width=10,height=2,command=self.pressoff)
        self.but_7.grid(row=2,column=0,padx=2,pady=2,sticky=W);
        self.but_8.grid(row=2,column=1,pady=2,padx=0,sticky=W);
        self.but_9.grid(row=2,column=2,pady=2,padx=0,sticky=W);
        self.but_x.grid(row=2,column=3,pady=2,padx=0,sticky=W);
        self.but_off.grid(row=2,column=4,pady=2,padx=0,sticky=W);

        #for button 4 to 6 with divide, on button
        self.but_4=Button(self.win,text="4",width=11,height=2,command= lambda : self.btnclick(4));
        self.but_5=Button(self.win,text="5",width=11,height=2,command=lambda : self.btnclick(5));
        self.but_6=Button(self.win,text="6",width=11,height=2,command=lambda : self.btnclick(6));
        self.but_div=Button(self.win,text="\u00F7",width=10,height=2,command=self.pressdiv);
        self.but_on=Button(self.win,text="On",width=10,height=2,command=self.presson)
        self.but_4.grid(row=3,column=0,padx=2,pady=2,sticky=W);
        self.but_5.grid(row=3,column=1,pady=2,padx=0,sticky=W);
        self.but_6.grid(row=3,column=2,pady=2,padx=0,sticky=W);
        self.but_div.grid(row=3,column=3,pady=2,padx=0,sticky=W);
        self.but_on.grid(row=3,column=4,pady=2,padx=0,sticky=W);

        #for button 1 to 3 with add and subtract sign
        self.but_1=Button(self.win,text="1",width=11,height=2,command=lambda : self.btnclick(1));
        self.but_2=Button(self.win,text="2",width=11,height=2,command=lambda : self.btnclick(2));
        self.but_3=Button(self.win,text="3",width=11,height=2,command=lambda : self.btnclick(3));
        self.but_add=Button(self.win,text="+",width=10,height=2,command=self.pressadd);
        self.but_sub=Button(self.win,text="-",width=10,height=2,command=self.presssub);
        self.but_1.grid(row=4,column=0,padx=2,pady=2,sticky=W);
        self.but_2.grid(row=4,column=1,pady=2,padx=0,sticky=W);
        self.but_3.grid(row=4,column=2,pady=2,padx=0,sticky=W);
        self.but_add.grid(row=4,column=3,pady=2,padx=0,sticky=W);
        self.but_sub.grid(row=4,column=4,pady=2,padx=0,sticky=W);

        #for button 0,00, point with power and equal sign
        self.but_0=Button(self.win,text="0",width=11,height=2,command=lambda : self.btnclick(0));
        self.but_pt=Button(self.win,text=".",width=11,height=2,command=lambda : self.btnclick('.'));
        self.but_00=Button(self.win,text="00",width=11,height=2,command=lambda: self.btnclick('00'));
        self.but_pow=Button(self.win,text="^",width=10,height=2,command=self.presspow);
        self.but_eq=Button(self.win,text="=",width=10,height=2,command=self.presseq);
        self.but_0.grid(row=5,column=0,padx=2,pady=2,sticky=W);
        self.but_pt.grid(row=5,column=1,pady=2,padx=0,sticky=W);
        self.but_00.grid(row=5,column=2,pady=2,padx=0,sticky=W);
        self.but_pow.grid(row=5,column=3,pady=2,padx=0,sticky=W);
        self.but_eq.grid(row=5,column=4,pady=2,padx=0,sticky=W)

        #for button like absolute value, for showing time, for 000, squareroot and cancel sign 
        self.but_abs=Button(self.win,text="abs",width=11,height=2,command=self.pressabs);
        self.but_time=Button(self.win,text="time",width=11,height=2,command=self.presstime);
        self.but_000=Button(self.win,text="000",width=11,height=2,command=lambda : self.btnclick('000'));
        self.but_sqrt=Button(self.win,text="\u221A",width=10,height=2,command=self.presssqrt);
        self.but_cut=Button(self.win,text="del",width=10,height=2,command=self.presscut);
        self.but_abs.grid(row=6,column=0,padx=2,pady=2,sticky=W);
        self.but_time.grid(row=6,column=1,pady=2,padx=0,sticky=W);
        self.but_000.grid(row=6,column=2,pady=2,padx=0,sticky=W);
        self.but_sqrt.grid(row=6,column=3,pady=2,padx=0,sticky=W);
        self.but_cut.grid(row=6,column=4,pady=2,padx=0,sticky=W)

      
        self.win.mainloop();

    #let's create a common function that will work on numbers(0-9 and .)
    #this is for display purpose . how they should be concated and display on a display screen
    def btnclick(self,number):
        if(gui.initialval==-1):
            self.result_box['text']="on it first!!!"
        else:
            self.result_box['text']=str(self.result_box['text']) + str(number)
    
    #for action related to but_time
    def presstime(self):
        localtime = time.asctime( time.localtime(time.time()) )
        self.calculator_text['text']=str(localtime);


    #for action related to but_cut  
    def presscut(self):
        if(gui.initialval==-1):
            self.result_box['text']="on it first!!!"
        else:
            s=str(self.result_box['text'])
            se=s[0:len(s)-1]
            if(se==''):
                self.result_box['text']='0'
            else:
                self.result_box['text']=se;

    #for action related to but_sqrt
    def presssqrt(self):
        if(gui.initialval==-1):
            self.result_box['text']="On it first"
        else:
            if '.' in str(self.result_box["text"]):
                s=float(self.result_box["text"])
            else:
                s=int(self.result_box['text'])
            self.result_box['text']= gui.initialval=math.sqrt(s)

    #for action related to but_abs
    def pressabs(self):
        if(gui.initialval==-1):
            self.result_box['text']="On it first"
        else:
            if '.' in str(self.result_box["text"]):
                s=float(self.result_box["text"])
            else:
                s=int(self.result_box['text'])
            self.result_box['text'] = self.initialval=abs(s);            

    #for action related to but_off
    def pressoff(self):
        gui.initialval=-1 
        self.result_box['bg']="Grey";
        self.result_box['fg']="White";
        self.result_box['text']="ON TO CONTINUE"

    #for action related to but_on  
    def presson(self):
        if(gui.initialval==-1):
            self.result_box['text']=0
            gui.initialval=0;
            
        self.result_box['bg']="White";
        self.result_box['fg']="blue";
        self.result_box.config(font=("Arial",9))
    
    #for action related to but_add
    def pressadd(self):
        if(gui.initialval==-1):
            self.result_box['text']="On it first"
        else:
            if '.' in str(self.result_box["text"]):
                s=float(self.result_box["text"])
            else:
                s=int(self.result_box["text"])
            if(gui.sum=="sum"):
                gui.initialval+=s
            else:
                gui.sum="sum";
                gui.initialval=s
            self.result_box["text"]="0";                
    
    #for action related to but_sub
    def presssub(self):
        if(gui.initialval==-1):
            self.result_box['text']="On it first"
        else:
            if '.' in str(self.result_box["text"]):
                s=float(self.result_box["text"])                
            else:
                s=int(self.result_box["text"])
            if(gui.sub=="sub"):
                gui.initialval-=s
            else:
                gui.sub="sub";
                gui.initialval=s
            self.result_box["text"]="0";            
    
    #for action related to but_mul
    def pressmul(self):
        if(gui.initialval==-1):
            self.result_box['text']="On it first"
        else:
            if '.' in str(self.result_box["text"]):
                s=float(self.result_box["text"])
            else:
                s=int(self.result_box["text"])
            if(gui.mul=="mul"):
                gui.initialval*=s
            else:
                gui.mul="mul";
                gui.initialval=s
            self.result_box["text"]="0";            
    
    #for action related to but_div
    def pressdiv(self):
        if(gui.initialval==-1):
            self.result_box['text']="On it first"
        else:
            if '.' in str(self.result_box["text"]):
                s=float(self.result_box["text"])
            else:
                s=int(self.result_box["text"])
            if(gui.div=="div"):
                gui.initialval/=s
            else:
                gui.div="div"
                gui.initialval=s
            self.result_box["text"]="0"
    
    #for action related to but_eq
    def presseq(self):
        if(gui.initialval==-1):
            self.result_box['text']="On it first"
        else:
            if '.' in str(self.result_box["text"]):
                s=float(self.result_box["text"])
            else:
                s=int(self.result_box['text'])
            if gui.sum=="sum":
                self.result_box['text']=str(gui.initialval+s)
                gui.sum="dump"
            if gui.mul=="mul":
                self.result_box['text']=str(gui.initialval*s)
                gui.mul="dump"
            if gui.sub=="sub":
                self.result_box['text']=str(gui.initialval-s)
                gui.sub="dump"
            if gui.div=='div':
                self.result_box['text']=str(gui.initialval/s)
                gui.div="dump"
            if gui.pow=='pow':
                self.result_box['text']=str(gui.initialval**s)
                gui.pow="dump"
    #for action related to but_pow
    def presspow(self):
        if(gui.initialval==-1):
            self.result_box['text']="On it first!!!"
        else:
            if '.' in str(self.result_box["text"]):
                s=float(self.result_box["text"])
            else:
                s=int(self.result_box["text"])
            if(gui.pow=="pow"):
                gui.initialval=pow(gui.initialval,s);
            else:
                gui.initialval=s
                gui.pow="pow";
            self.result_box["text"]="0";

if __name__=='__main__':
    A=gui()
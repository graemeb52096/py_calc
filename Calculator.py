
from Tkinter import *
from ttk import *
from Math_Functions import *
from math import *
from threader import *

class Calculator(Frame):
	'''This class houses the entire
	Calculator in all its glory
	'''
	global mode
	mode = "rad"
	
	def __init__(self, parent):
		Frame.__init__(self, parent)
		
		self.parent = parent
		self.parent.title("Calculator: RADIANS")
		
		#self.centerWindow()
		self.initUI()
		
	def centerWindow(self):
		'''Takes no specific input,
		purpose is to center the 
		window
		'''
		
		w = 500
		h = 300
		
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		
		x = (sw - w)/2
		y = (sh - h)/2
		
		self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
		
	def initUI(self):
		
		Style().configure("TButton", padding=(0, 2.5, 0, 2.5), font='serif 10', background="red")	
		
		self.columnconfigure(0, pad=3)
		self.columnconfigure(1, pad=3)
		self.columnconfigure(2, pad=3)
		self.columnconfigure(3, pad=3)
		self.columnconfigure(4, pad=3)
		self.columnconfigure(5, pad=3)
		
		self.rowconfigure(0, pad=4)
		self.rowconfigure(1, pad=4)
		self.rowconfigure(2, pad=4)
		self.rowconfigure(3, pad=4)
		self.rowconfigure(4, pad=4)
		self.rowconfigure(5, pad=4)
		
		#-----Row 0------#
		entry = Entry(self)
		entry.grid(row=0, columnspan=6)
		#Initialize at zero
		entry.delete(0, END)
		entry.insert(0, 0)
		
		#-----CALL BACKS-----#
		def eCallBack():
			x = entry.get()
			x = float(x)
			
			y = E(x)
			
			entry.delete(0, END)
			entry.insert(0, y)
		
		def SinCallBack():
			global mode
			
			x = entry.get()
			#if there is no input, set default to zero
			if x == '':
				x = 0
				
			if mode == "deg":
				x = ((x)*(pi))/180
				
			x = float(x)


			print '\nCALCULATING SINE of:', x ,'Radians\n'

			y = Sin(x)
			
			entry.delete(0, END)
			entry.insert(0, y)
	
		def CosCallBack():
			x = entry.get()
			#if there is no input, set default to zero
			if x == '':
				x = 0
			x = float(x)
			print '\nCALCULATING COSINE of:', x ,'Radians\n'

			y = Cos(x)

			entry.delete(0, END)
			entry.insert(0, y)

		def TanCallBack():
			x = entry.get()
			#if there is no input, set default to zero
			if x == '':
				x = 0
			x = float(x)
			print '\nCALCULATING TANGENT of:', x ,'Radians\n'

			y = Tan(x)
			
			entry.delete(0, END)
			entry.insert(0, y)
	
		def CscCallBack():
			x = entry.get()
			#if there is no input, set default to zero
			if x == '':
				x = 0
			x = float(x)
			print '\nCALCULATING COSECANT of:', x ,'Radians\n'

			if x != 0:
				y = Csc(x)
			else:
				y = "Undefined"
			
			entry.delete(0, END)
			entry.insert(0, y)
	
		def SecCallBack():
			x = entry.get()
			#if there is no input, set default to zero
			if x == '':
				x = 0
			x = float(x)
			print '\nCALCULATING SECANT of:', x ,'Radians\n'

			y = Sec(x)
			
			entry.delete(0, END)
			entry.insert(0, y)

		def CotCallBack():
			x = entry.get()
			#if there is no input, set default to zero
			if x == '':
				x = 0
			x = float(x)
			print '\nCALCULATING COTANGENT of:', x ,'Radians\n'
			if x != 0:
				y = Cot(x)
			else:
				y = "Undefined"
			
			entry.delete(0, END)
			entry.insert(0, y)
		
		def dtr_call():
			x = entry.get()
			
			x = float(x)
			
			y = (x*(pi))/180
			
			entry.delete(0, END)
			entry.insert(0, y)
		
		def rtd_call():
			x = entry.get()
			
			x = float(x)
			
			y = (x*180)/(pi)
			
			entry.delete(0, END)
			entry.insert(0, y)
			
		def clear_call():
			entry.delete(0, END)
			entry.insert(0, 0)
			
		def zer_call():
			entry.insert(END, 0)
			
		def one_call():
			if entry.get() == '0':
				entry.delete(0, END)
			entry.insert(END, 1)
			
		def two_call():
			if entry.get() == '0':
				entry.delete(0, END)
			entry.insert(END, 2)
			
		def thr_call():
			if entry.get() == '0':
				entry.delete(0, END)
			entry.insert(END, 3)
			
		def fou_call():
			if entry.get() == '0':
				entry.delete(0, END)
			entry.insert(END, 4)
			
		def fiv_call():
			if entry.get() == '0':
				entry.delete(0, END)
			entry.insert(END, 5)
			
		def six_call():
			if entry.get() == '0':
				entry.delete(0, END)
			entry.insert(END, 6)
			
		def sev_call():
			if entry.get() == '0':
				entry.delete(0, END)
			entry.insert(END, 7)
		
		def eig_call():
			if entry.get() == '0':
				entry.delete(0, END)
			entry.insert(END, 8)
		
		def nin_call():
			if entry.get() == '0':
				entry.delete(0, END)
			entry.insert(END, 9)
		
		def Pi_call():
			if entry.get() == '0':
				y = (pi)
				entry.delete(0, END)
				entry.insert(END, y)
			else:
				y = float(pi) * float(entry.get())
				entry.delete(0, END)
				entry.insert(END, y)
		
		def div_call():
			global Temp_Function
			Temp_Function = 'div'
			global Temp_Val
			Temp_Val = entry.get()
			Temp_Val = (Temp_Val)
			entry.delete(0, END)
			
		def mul_call():
			global Temp_Function
			Temp_Function = 'mul'
			global Temp_Val
			Temp_Val = entry.get()
			Temp_Val = (Temp_Val)
			entry.delete(0, END)
			
		def add_call():
			global Temp_Function
			Temp_Function = 'add'
			global Temp_Val
			Temp_Val = entry.get()
			Temp_Val = (Temp_Val)
			entry.delete(0, END)
			
		def sub_call():
			global Temp_Function
			Temp_Function = 'sub'
			global Temp_Val
			Temp_Val = entry.get()
			Temp_Val = (Temp_Val)
			entry.delete(0, END)

		def eql_call():
			global Temp_Function
			global Temp_Val
			if Temp_Function == 'div':
				y = Temp_Val/(entry.get())
			elif Temp_Function == 'mul':
				y = Temp_Val * (entry.get())
			elif Temp_Function == 'add':
				y = Temp_Val + (entry.get())
			elif Temp_Function == 'sub':
				y = Temp_Val - (entry.get())
			else:
				y = entry.get()
			
			y = (y)
			
			Temp_Function = 'null'
			Temp_Val = 0
			entry.delete(0, END)
			entry.insert(0, y)
		
		def dot_call():
			entry.insert(END, '.')
			
		def mod_call():
			global mode
			global trig_sin
			if mode == "deg":
				mode = "rad"
				self.parent.title("Calculator: RADIANS")
			else:
				mode = "deg"
				self.parent.title("Calculator: DEGREES")
				initialize_sin()
				
		def sign_change():
			temp_string = entry.get()
			temp_string = str(temp_string)
			if temp_string[0:1] == '-':
				entry.delete(0,1)
			else:
				entry.insert(0, '-') 
		
		#-----Row 1------#
		
		cls = Button(self, text="Cls", command=clear_call)
		cls.grid(row=1, column=0)
		
		mod = Button(self, text="Mode", command=mod_call)
		mod.grid(row=1, column=1)
		
		sign = Button(self, text="+/-", command=sign_change)
		sign.grid(row=1, column=2)	
	
		quitButton = Button(self, text="Quit", command=self.quit)
		quitButton.grid(row=1, column=3)
		
		def initialize_sin():
			trig_sin = Button(self, text="sin", command = SinCallBack)
			trig_sin.grid(row=1, column=4)
		
		def initialize_csc():
			trig_csc = Button(self, text="csc", command = CscCallBack)
			trig_csc.grid(row=1, column=5)
		
		
		#-----Row 2------#
		def initialize_sev():
			sev = Button(self, text="7", command=sev_call)
			sev.grid(row=2, column=0)
		
		def initialize_eig():
			eig = Button(self, text="8", command=eig_call)
			eig.grid(row=2, column=1)
		
		def initialize_nin():
			nin = Button(self, text="9", command=nin_call)
			nin.grid(row=2, column=2)
		
		def initialize_div():
			div = Button(self, text=" /", command=div_call)
			div.grid(row=2, column=3)
		
		def initialize_cos():
			trig_cos = Button(self, text="cos", command = CosCallBack)
			trig_cos.grid(row=2, column=4)
		
		def initialize_sec():
			trig_sec = Button(self, text="sec", command = SecCallBack)
			trig_sec.grid(row=2, column=5)
		
		#-----Row 3------#
		def initialize_fou():
			fou = Button(self, text="4", command=fou_call)
			fou.grid(row=3, column=0)
		
		def initialize_fiv():
			fiv = Button(self, text="5", command=fiv_call)
			fiv.grid(row=3, column=1)
		
		def initialize_six():
			six = Button(self, text="6", command=six_call)
			six.grid(row=3, column=2)
		
		def initialize_mul():
			mul = Button(self, text="*", command=mul_call)
			mul.grid(row=3, column=3)
		
		def initialize_tan():
			trig_tan = Button(self, text="tan", command = TanCallBack)
			trig_tan.grid(row=3, column=4)
		
		def initialize_cot():
			trig_cot = Button(self, text="cot", command = CotCallBack)
			trig_cot.grid(row=3, column=5)
			
		#-----Row 4------#
		def initialize_one():
			one = Button(self, text="1", command=one_call)
			one.grid(row=4, column=0)
		
		def initialize_two():
			two = Button(self, text="2", command=two_call)
			two.grid(row=4, column=1)
		
		def initialize_thr():
			thr = Button(self, text="3", command=thr_call)
			thr.grid(row=4, column=2)
		
		def initialize_mns():
			mns = Button(self, text="-", command=sub_call)
			mns.grid(row=4, column=3)
		
		def initialize_rtd():
			rtd = Button(self, text="r -> d", command = rtd_call)
			rtd.grid(row=4, column=4)
		
		def initialize_dtr():
			dtr = Button(self, text="d -> r", command = dtr_call)
			dtr.grid(row=4, column=5)
		
		#-----Row 5------#
		def initialize_zer():
			zer = Button(self, text="0", command=zer_call)
			zer.grid(row=5, column=0)
		
		def initialize_dot():
			dot = Button(self, text=".", command=dot_call)
			dot.grid(row=5, column=1)
			
		def initialize_eql():	
			eql = Button(self, text="=", command=eql_call)
			eql.grid(row=5, column=2)
		
		def initialize_pls():		
			pls = Button(self, text="+", command=add_call)
			pls.grid(row=5, column=3)
		
		def initialize_Pi():
			Pi = Button(self, text="PI", command=Pi_call)
			Pi.grid(row=5, column=4)
		
		def initialize_exp():
			exp = Button(self, text="e^x", command=eCallBack)
			exp.grid(row=5, column=5)

		#--- Trig buttons initialize ---#
		initialize_sin()
		initialize_csc()

		initialize_cos()
		initialize_sec()
		
		initialize_tan()
		initialize_cot()
		
		#--- Math Operation Buttons ---#
		initialize_mul()
		initialize_div()
		initialize_pls()
		initialize_mns()
		initialize_eql()
		
		#--- Conversion Button initialize --#
		initialize_rtd()
		initialize_dtr()
		
		#--- Initialize Exponential Button ---#
		initialize_exp()
		
		#--- Initialize pi button ---#
		initialize_Pi()
		
		#--- Initialize dot button ---#
		initialize_dot()
		
		#--- Number buttons initialize --#
		initialize_zer()
		initialize_one()
		initialize_two()
		initialize_thr()
		initialize_fou()
		initialize_fiv()
		initialize_six()
		initialize_sev()
		initialize_eig()
		initialize_nin()
		
		self.pack()
		
		
		
def main():
	
	root = Tk()
	root.configure(background='grey')
	app = Calculator(root)
	root.mainloop()
	
if __name__ == '__main__':
	main()
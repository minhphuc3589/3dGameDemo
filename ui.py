import tkinter as tk
import tkinter.font as font
import time
# from PIL import Image, ImageTk

from calculation import *

class Casio:
	def __init__(self):
		self.SCREEN_WIDTH_DEFAULT = 260
		self.SCREEN_HEIGHT_DEFAULT = 560

		self.app = tk.Tk()
		self.app.title("CASIO FX-580FAKE")
		self.app.geometry(f"{self.SCREEN_WIDTH_DEFAULT}x{self.SCREEN_HEIGHT_DEFAULT}")
		self.app['bg'] = "#616363"

		self.resultAns = 0

	def button0(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn0['text'])
		self.textScreen['state'] = 'disabled'

	def button1(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn1['text'])
		self.textScreen['state'] = 'disabled'

	def button2(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn2['text'])
		self.textScreen['state'] = 'disabled'

	def button3(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn3['text'])
		self.textScreen['state'] = 'disabled'

	def button4(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn4['text'])
		self.textScreen['state'] = 'disabled'

	def button5(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn5['text'])
		self.textScreen['state'] = 'disabled'

	def button6(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn6['text'])
		self.textScreen['state'] = 'disabled'

	def button7(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn7['text'])
		self.textScreen['state'] = 'disabled'

	def button8(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn8['text'])
		self.textScreen['state'] = 'disabled'

	def button9(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btn9['text'])
		self.textScreen['state'] = 'disabled'

	def buttonAddition(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btnADDITION['text'])
		self.textScreen['state'] = 'disabled'

	def buttonSubtraction(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btnSUBTRACTION['text'])
		self.textScreen['state'] = 'disabled'

	def buttonMultiplication(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btnMULTIPLICATION['text'])
		self.textScreen['state'] = 'disabled'

	def buttonDivision(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btnDIVISION['text'])
		self.textScreen['state'] = 'disabled'

	def buttonDEL(self):
		text = self.textScreen.get('1.0', tk.END)

		if str(text[len(text) - 2]) == "S":
			self.textScreen['state'] = 'normal'
			self.textScreen.delete('1.0', tk.END)
			self.textScreen.insert(tk.INSERT, text[0:len(text) - 4])
			self.textScreen['state'] = 'disabled'

		else:
			self.textScreen['state'] = 'normal'
			self.textScreen.delete('1.0', tk.END)
			self.textScreen.insert(tk.INSERT, text[0:len(text) - 2])
			self.textScreen['state'] = 'disabled'

	def buttonAC(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.delete('1.0', tk.END)
		self.textScreen['state'] = 'disabled'

		self.resultScreen['state'] = 'normal'
		self.resultScreen.delete('1.0', tk.END)
		self.resultScreen['state'] = 'disabled'

		CheckResult("")

	def buttonAns(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btnANS['text'])
		self.textScreen['state'] = 'disabled'

	def buttonDot(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, self.btnDOT['text'])
		self.textScreen['state'] = 'disabled'

	def buttonSQRT(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, f"({self.btnSQRT['text']}")
		self.textScreen['state'] = 'disabled'

	def buttonLUYTHUAHAI(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, f"{self.btnLUYTHUAHAI['text']}")
		self.textScreen['state'] = 'disabled'

	def buttonLUYTHUA(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, f"{self.btnLUYTHUA['text']}")
		self.textScreen['state'] = 'disabled'

	def buttonSIN(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, f"{self.btnSIN['text']}(")
		self.textScreen['state'] = 'disabled'

	def buttonCOS(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, f"{self.btnCOS['text']}(")
		self.textScreen['state'] = 'disabled'

	def buttonTAN(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, f"{self.btnTAN['text']}(")
		self.textScreen['state'] = 'disabled'

	def buttonDONGNGOACDON(self):
		self.textScreen['state'] = 'normal'
		self.textScreen.insert(tk.INSERT, f")")
		self.textScreen['state'] = 'disabled'


	def buttonEquality(self):
		# Bắt các lỗi như "<Number>--"
		try:
			# Tạo giá trị cho ANS
			strResult = Calculating(self.textScreen.get('1.0', tk.END), ANS = self.resultAns)
			result = eval(strResult)
			checkTextScreen = self.textScreen.get('1.0', tk.END)
			checkTextScreen = CheckResult(checkTextScreen)

			self.resultAns = result if result else 0

			if "ANS" in strResult:
				if strResult[strResult.find("S")] == "S" and type(strResult[len(strResult) - 1]) == int:
					self.resultScreen['state'] = 'normal'
					self.resultScreen.delete('1.0', tk.END)
					self.resultScreen.insert(tk.INSERT, "ERROR")
					# self.resultScreen['state'] = 'disabled'

			else:
				# Thử xem có bấm dấu "=" 2 lần trở lên không ? 
				# Nếu có thì màn hình hiện thị "ANS"
				if checkTextScreen >= 2:
					self.textScreen['state'] = 'normal'
					self.textScreen.delete('1.0', tk.END)
					self.textScreen.insert(tk.INSERT, "ANS")
					self.textScreen['state'] = 'disabled'

				self.resultScreen['state'] = 'normal'
				self.resultScreen.delete('1.0', tk.END)
				self.resultScreen.insert(tk.INSERT, str(result))
				self.resultScreen['state'] = 'disabled'


		except:
			self.resultScreen['state'] = 'normal'
			self.resultScreen.delete('1.0', tk.END)
			self.resultScreen.insert(tk.INSERT, "ERROR")
			self.resultScreen['state'] = 'disabled'
	

	def main(self):
		IPADX_DEFAULT = 115
		IPADY_DEFAULT = 114

		########################################################

		### Sreen Frame ###
		self.ScreenFrame = tk.Frame(self.app)

		self.borderTopScreenCanvas = tk.Canvas(self.ScreenFrame, width = IPADX_DEFAULT * 2 - 2, height = 2, highlightbackground = "#161717")
		self.borderRightScreenCanvas = tk.Canvas(self.ScreenFrame, width = 2, height = IPADY_DEFAULT * 2, highlightbackground = "#161717")
		self.borderBottomScreenCanvas = tk.Canvas(self.ScreenFrame, width = IPADX_DEFAULT * 2 - 2, height = 2, highlightbackground = "#161717")
		self.borderLeftScreenCanvas = tk.Canvas(self.ScreenFrame, width = 2, height = IPADY_DEFAULT * 2, highlightbackground = "#161717")

		self.textScreen = tk.Text(self.ScreenFrame, fg = "#adadad", bg = "#017a50", state = "disabled", width = 24, height = 1, font = font.Font(size = 12), border = 0)
		self.resultScreen = tk.Text(self.ScreenFrame, fg = "#adadad", bg = "#00613f", state = "disabled", padx = 2, width = 24, height = 1, font = font.Font(size = 12), border = 0)


		# Screen Frame settings
		self.ScreenFrame.pack(anchor = tk.CENTER, ipadx = IPADX_DEFAULT + 2, ipady = 78 / 2 + 6)
		self.ScreenFrame['bg'] = '#017a50'

		self.borderTopScreenCanvas['bg'] = "#393d3c"
		self.borderRightScreenCanvas['bg'] = "#393d3c"
		self.borderBottomScreenCanvas['bg'] = "#393d3c"
		self.borderLeftScreenCanvas['bg'] = "#393d3c"

		self.borderTopScreenCanvas.place(x = 0, y = 0)
		self.borderRightScreenCanvas.place(x = 230, y = 0)
		self.borderBottomScreenCanvas.place(x = 0, y = 87)
		self.borderLeftScreenCanvas.place(x = 0, y = 0)

		self.textScreen.place(x = 8, y = 8)
		self.resultScreen.place(x = 8, y = 61)

		# self.app.bind("<Motion>", motion)

		########################################################

		# Advanced Calculating Frame
		self.AdvancedCalcuFrame = tk.Frame(self.app)
		self.AdvancedCalcuFrame['bg'] = "black"

		# img = Image.open("./blackbgRoundedButton.jpg")
		# image_resize = img.resize((20, 20))
		# image = ImageTk.PhotoImage(image_resize)

		# self.btnSHIFT = tk.Label(self.AdvancedCalcuFrame, image = image, border = 0)
		# self.btnALPHA = tk.Label(self.AdvancedCalcuFrame, image = image, border = 0)
		# self.btnMENU_SETUP = tk.Label(self.AdvancedCalcuFrame, image = image, border = 0)
		# self.btnON = tk.Label(self.AdvancedCalcuFrame, image = image, border = 0)

		# self.textSHIFT = tk.Label(self.AdvancedCalcuFrame, text = "SHIFT", fg = "yellow", bg = "black", font = font.Font(size = 5), cursor = "hand2")
		# self.textALPHA = tk.Label(self.AdvancedCalcuFrame, text = "ALPHA", fg = "pink", bg = "black", font = font.Font(size = 5))
		# self.textMENU = tk.Label(self.AdvancedCalcuFrame, text = "MENU", fg = "white", bg = "black", font = font.Font(size = 5))
		# self.textSETUP = tk.Label(self.AdvancedCalcuFrame, text = "SETUP", fg = "yellow", bg = "black", font = font.Font(size = 5))
		# self.textON = tk.Label(self.AdvancedCalcuFrame, text = "ON", fg = "white", bg = "black", font = font.Font(size = 5))

		self.btnSQRT = tk.Button(self.AdvancedCalcuFrame, text = "√", width = 4, height = 1, relief = "raised", borderwidth = 3, font = font.Font(size = 8))
		self.btnLUYTHUAHAI = tk.Button(self.AdvancedCalcuFrame, text = "^2", width = 4, height = 1, relief = "raised", borderwidth = 3, font = font.Font(size = 8))
		self.btnLUYTHUA = tk.Button(self.AdvancedCalcuFrame, text = "^", width = 4, height = 1, relief = "raised", borderwidth = 3, font = font.Font(size = 8))
		self.btnSIN = tk.Button(self.AdvancedCalcuFrame, text = "sin", width = 4, height = 1, relief = "raised", borderwidth = 3, font = font.Font(size = 8))
		self.btnCOS = tk.Button(self.AdvancedCalcuFrame, text = "cos", width = 4, height = 1, relief = "raised", borderwidth = 3, font = font.Font(size = 8))
		self.btnTAN = tk.Button(self.AdvancedCalcuFrame, text = "tan", width = 4, height = 1, relief = "raised", borderwidth = 3, font = font.Font(size = 8))
		self.btnDONGNGOACDON = tk.Button(self.AdvancedCalcuFrame, text = ")", width = 4, height = 1, relief = "raised", borderwidth = 3, font = font.Font(size = 8))

		# Advanced Calculating Frame settings
		self.AdvancedCalcuFrame.pack(anchor = tk.CENTER, ipadx = IPADX_DEFAULT, ipady = IPADY_DEFAULT)

		# self.btnSHIFT.place(x = 20, y = 15)
		# self.btnALPHA.place(x = 55, y = 15)
		# self.btnMENU_SETUP.place(x = 160, y = 15)
		# self.btnON.place(x = 195, y = 15)

		# self.textSHIFT.place(x = 15, y = 0)
		# self.textALPHA.place(x = 50, y = 0)
		# self.textMENU.place(x = 140, y = 0)
		# self.textSETUP.place(x = 165, y = 0)
		# self.textON.place(x = 195, y = 0)

		self.btnSQRT.place(x = 50, y = 65)
		self.btnLUYTHUAHAI.place(x = 95, y = 65)
		self.btnLUYTHUA.place(x = 140, y = 65)
		self.btnSIN.place(x = 50, y = 100)
		self.btnCOS.place(x = 95, y = 100)
		self.btnTAN.place(x = 140, y = 100)
		self.btnDONGNGOACDON.place(x = 95, y = 135)

		self.btnSQRT['command'] = self.buttonSQRT
		self.btnLUYTHUAHAI['command'] = self.buttonLUYTHUAHAI
		self.btnLUYTHUA['command'] = self.buttonLUYTHUA
		self.btnSIN['command'] = self.buttonSIN
		self.btnCOS['command'] = self.buttonCOS
		self.btnTAN['command'] = self.buttonTAN
		self.btnDONGNGOACDON['command'] = self.buttonDONGNGOACDON

		########################################################


		# Calculating Frame
		self.CalcuFrame = tk.Frame(self.app, highlightbackground = "red")
		self.text1 = tk.Label(self.CalcuFrame, text = "Testing", fg = "white")
		self.btn1 = tk.Button(self.CalcuFrame, text = "1", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btn2 = tk.Button(self.CalcuFrame, text = "2", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btn3 = tk.Button(self.CalcuFrame, text = "3", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btn4 = tk.Button(self.CalcuFrame, text = "4", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btn5 = tk.Button(self.CalcuFrame, text = "5", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btn6 = tk.Button(self.CalcuFrame, text = "6", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btn7 = tk.Button(self.CalcuFrame, text = "7", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btn8 = tk.Button(self.CalcuFrame, text = "8", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btn9 = tk.Button(self.CalcuFrame, text = "9", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btn0 = tk.Button(self.CalcuFrame, text = "0", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btnDEL = tk.Button(self.CalcuFrame, text = "DEL", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12), bg = "blue", fg = "white")
		self.btnAC = tk.Button(self.CalcuFrame, text = "AC", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12), bg = "blue", fg = "white")
		self.btnMULTIPLICATION = tk.Button(self.CalcuFrame, text = "×", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btnDIVISION = tk.Button(self.CalcuFrame, text = "÷", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btnADDITION = tk.Button(self.CalcuFrame, text = "+", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btnSUBTRACTION = tk.Button(self.CalcuFrame, text = "-", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btnDOT = tk.Button(self.CalcuFrame, text = ".", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btnNULL = tk.Button(self.CalcuFrame, text = "×10", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btnANS = tk.Button(self.CalcuFrame, text = "ANS", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))
		self.btnEQUALITY = tk.Button(self.CalcuFrame, text = "=", width = 3, height = 2, relief = "raised", borderwidth = 3, font = font.Font(size = 12))

		# Calculating Frame settings
		self.CalcuFrame.pack(anchor = tk.S, ipadx = IPADX_DEFAULT, ipady = IPADY_DEFAULT)
		self.CalcuFrame['bg'] = 'black'


		# Maximum of X is +40
		# Maximum of Y is +52
		self.btn7.place(x = 7, y = 0)
		self.btn8.place(x = 52, y = 0)
		self.btn9.place(x = 97, y = 0)
		self.btnDEL.place(x = 142, y = 0)
		self.btnAC.place(x = 187, y = 0)

		self.btn4.place(x = 7, y = 57)
		self.btn5.place(x = 52, y = 57)
		self.btn6.place(x = 97, y = 57)
		self.btnMULTIPLICATION.place(x = 142, y = 57)
		self.btnDIVISION.place(x = 187, y = 57)

		self.btn1.place(x = 7, y = 114)
		self.btn2.place(x = 52, y = 114)
		self.btn3.place(x = 97, y = 114)
		self.btnADDITION.place(x = 142, y = 114)
		self.btnSUBTRACTION.place(x = 187, y = 114)

		self.btn0.place(x = 7, y = 171)
		self.btnDOT.place(x = 52, y = 171)
		self.btnNULL.place(x = 97, y = 171)
		self.btnANS.place(x = 142, y = 171)
		self.btnEQUALITY.place(x = 187, y = 171)

		self.btn7['command'] = self.button7
		self.btn8['command'] = self.button8
		self.btn9['command'] = self.button9
		self.btnDEL['command'] = self.buttonDEL
		self.btnAC['command'] = self.buttonAC

		self.btn4['command'] = self.button4
		self.btn5['command'] = self.button5
		self.btn6['command'] = self.button6
		self.btnMULTIPLICATION['command'] = self.buttonMultiplication
		self.btnDIVISION['command'] = self.buttonDivision

		self.btn1['command'] = self.button1
		self.btn2['command'] = self.button2
		self.btn3['command'] = self.button3
		self.btnADDITION['command'] = self.buttonAddition
		self.btnSUBTRACTION['command'] = self.buttonSubtraction

		self.btn0['command'] = self.button0
		self.btnDOT['command'] = self.buttonDot
		self.btnANS['command'] = self.buttonAns
		self.btnEQUALITY['command'] = self.buttonEquality

		########################################################

		self.app.resizable(False, False)
		self.app.mainloop()



import numpy

count = 0

def ANSWER(ANS):
	return str(ANS)

def Calculating(strResult, ANS):
	strResult = strResult.replace("×", "*")
	strResult = strResult.replace("÷", "/")
	strResult = strResult.replace("ANS", str(ANS))
	strResult = strResult.replace("^", "**")

	countMO_NGOAC_DON = 0
	countDONG_NGOAC_DON = 0

	newValue = 0
	
	for i in strResult:
		if i == "(":
			countMO_NGOAC_DON += 1

		if i == ")":
			countDONG_NGOAC_DON += 1

	if countMO_NGOAC_DON != countDONG_NGOAC_DON:
		return "ERROR"

	posSQRT = strResult.find("√")
	if strResult[posSQRT-1:posSQRT+1] == "(√":
		newValue = strResult[strResult.find("√") + 1:strResult.find(")")]
		strResult = strResult.replace(f"{strResult[strResult.find('√') - 1:strResult.find(')') + 1]}", str(numpy.sqrt(int(newValue))))

	if strResult[strResult.find("sin("):strResult.find("sin(") + 4] == "sin(":
		newValue = strResult[strResult.find("sin(") + 4:strResult.find(")")]
		strResult = strResult.replace(f"{strResult[strResult.find('sin('):strResult.find(')') + 1]}", str(numpy.sin(int(newValue) * numpy.pi/180)))

	if strResult[strResult.find("cos("):strResult.find("cos(") + 4] == "cos(":
		newValue = strResult[strResult.find("cos(") + 4:strResult.find(")")]
		strResult = strResult.replace(f"{strResult[strResult.find('cos('):strResult.find(')') + 1]}", str(numpy.cos(int(newValue) * numpy.pi/180)))

	if strResult[strResult.find("tan("):strResult.find("tan(") + 4] == "tan(":
		newValue = strResult[strResult.find("tan(") + 4:strResult.find(")")]
		strResult = strResult.replace(f"{strResult[strResult.find('tan('):strResult.find(')') + 1]}", str(numpy.tan(int(newValue) * numpy.pi/180)))

	return str(strResult)

def CheckResult(check):
	global count

	if check != "":
		count += 1
	else:
		count = 0

	return count
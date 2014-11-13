number = 123456789
string = ""

div_result = number / 10
mod_result = number % 10
string = str(mod_result) + string

while div_result >= 10:
	mod_result = div_result % 10
	div_result = div_result / 10
	string = str(mod_result) + string

string = str(div_result) + string #add last number

print string



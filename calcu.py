import telethon
from telethon import events
from config import *


# 1- input FIRST NUMBER
first_number = int(input("enter firstvnumber: "))

# 2- input operation
operation = input("enter operation type: ")

# 3-input second number
second_number = int(input("enter second number: "))

# 4- print the reslt

if operation == "+":
  print(first_number + second_number)
elif operation == "-":
 print(first_number + second_number)
elif operation == "*":
 print(first_number * second_number)
elif operation == "/":
 print(first_number / second_number)
else:
   print("error")"


@baythun.on(events.NewMessage(outgoing=True, pattern=".احسبلي  (.*)"))
async def _(event):
    try:
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        num1 = int(msg[0])
        num2 = int(msg[2])
        fun = str(msg[1])
        await event.edit(f''' الناتج = `{calc(num1, num2, fun)}`''')
    except:
        await event.edit('''خطأ, يرجى ادخال الرقم مثل :
7 + 7
7 - 7
7 x 7
7 ÷ 7''')

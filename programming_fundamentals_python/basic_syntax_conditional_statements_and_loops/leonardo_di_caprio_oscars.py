number = int(input())
# If the number is 88
# "Leo finally won the Oscar! Leo is happy"
# If the number is 86
# "Not even for Wolf of Wall Street?!"
# If the number is not 88 nor 86 (and below 88)
# "When will you give Leo an Oscar?"
# If the number is over 88
# "Leo got one already!"
status = ""
if number == 88:
    status = "Leo finally won the Oscar! Leo is happy"
elif number == 86:
    status = "Not even for Wolf of Wall Street?!"
elif number < 88:
    status = "When will you give Leo an Oscar?"
else:
    status = "Leo got one already!"

print(status)
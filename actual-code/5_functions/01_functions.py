# scope
# define
# default value
# 3. Naming things, counting things
def print_message_with_borders(message, border_symbol="=", border_length=10):
  """
  Prints a message with borders. You can change the border symbol and length.
  """
  print(border_symbol * border_length)
  print(message)
  print(border_symbol * border_length)

# message

# call or invoking
print_message_with_borders("Hello Kev! Come on Man U!", border_length=22)
print_message_with_borders(border_symbol="-", message="Hello Luke!", border_length=11)
result = print_message_with_borders("Hello Middlesbrough!", "🥊")

print_message_with_borders("Hello from Belfast","-*-", 12)

print(f"The result is {result}")



# # What's the one job that this function is doing and doing well?
# def build_report():
#   # This collects in this 
#   data = collect_data()
#   # cleaned
#   cleaned_data = clean_data(data)
#   # formatted
#   formatted_data = format_data(data, company="Casper")
#   # wrote to a file

#   # emailed you a status update

def get_message_with_borders(message, border_symbol="=", border_length=10):
  """
  Prints a message with borders. You can change the border symbol and length.
  """
  message = f"""{border_symbol * border_length}
{message}
{border_symbol * border_length}"""
  return message

message = get_message_with_borders("This is a function that returns things")

with open("test.txt", mode="a") as f:
  f.write(message)
import logging
import traceback

logging.basicConfig(filename="app.log",   
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level="DEBUG")
logger = logging.getLogger()

# DEBUG - information and diagnositics
logger.debug("Program Started")
# INFO - informational and confirmation
# WARNING - Something unexpected but recoverable
# ERROR - A failure that needs attention
# CRITICAL - Severe failure!

try: 
  # users, files, networks, databases, customer data!
  user_input = int(input("Give me a number: "))
  logger.debug(user_input)
  print(10/user_input)
except ValueError as e:  # bare  
  print("Whoops! That didn't look a number! I'm going to use 10 instead.")
  logger.warning(traceback.format_exc())
  user_input = 10
except ZeroDivisionError:
  print("Uh-oh! You can't divide by zero!")
except Exception:
  print("Something unexpected happened!")
  logger.critical(traceback.format_exc())

print("End of program!")




# TypeError
# ValueError
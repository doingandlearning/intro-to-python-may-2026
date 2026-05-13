from casper_errors import CasperNegativeError
import logging
import traceback

logging.basicConfig(filename="app.log",   
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level="DEBUG")
logger = logging.getLogger()

try:
  user_number = int(input("> "))
  if user_number < 0:
    raise CasperNegativeError("Needs to be a positive number")
except CasperNegativeError as e:
  print("Whoops! That wasn't a positive number.")
  logger.warning(f"{e} - what an idiot!")
except ValueError:
  print("Those weren't digits.")
else:
  logger.info("All ran successfully.")
finally:
  logger.info("Will always")

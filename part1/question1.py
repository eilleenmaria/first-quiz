################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

def get_city_temperature(city):
   match city:
      case "Quito" :
            return 22
      case "Sao Paulo":
            return 17
      case "San Francisco":
            return 16
      case "New York":
            return 14
      case _:
            return None
   
def get_city_weather(city): 
   match city:
      case "Sao Paulo":
            sky_condition= "cloudy"
      case "New York":
            sky_condition= "rainy"
      case "Quito":
            sky_condition = "sunny" 
      case _:
            sky_condition= "empty"
   temperature = get_city_temperature(city)
   return str(temperature) + " degrees and " + sky_condition

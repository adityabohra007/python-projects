
alphabet = ['0', '!', 'a', 'b', '1', 'c', 'd', '2', 'e', 'f', ',', 'g', 'h', '3', 'i', 'j','.', 'k', 'l', '4', 'm', ' ', 'n', '5', 'o', 'p', ':', 'q', 'r', '6', 's', 't', '\'', 'u', 'v', '7', 'w', 'x', '8', 'y', 'z', '?', '9']

def convert(text):
  text = text.strip()
  output = ""
  mult = 0

  if function == "encode":
    mult = 1
  elif function == "decode":
    mult = -1

  for letter in range(len(text)):  
    uppercase = "N/A"
    input = text[letter]

    input = input.lower() #Temporary until I figure out a way to make capitals work

    if input == "`":
      input = " "
    """  
    if input == input.lower():
      uppercase = 0
      input = input.lower()
    elif input == input.upper():
      uppercase = 1
      input = input.lower()
    """
    if input not in alphabet:
      return "Sorry, \"" + input + "\" is not supported."
      
    key = (alphabet.index(input) + mult)
    if key > 42:
      key = 0
    elif key < 0:
      key = 42
    """      
    if uppercase == 0:
      output += alphabet[key].lower()
    elif uppercase == 1:
      output += alphabet[key].upper()
    """

    output += alphabet[key] #Also temporary
    
    mult *= -1

  if output[0] == " ":
    output = "`" + output[1:len(output)]
  if output[(len(output) - 1)] == " ":
    output = output[0:(len(output) - 1)] + "`"
  return output

print("")

print("Welcome to ComplexCipher v1.1 by Om Gupta!")

quit_wish = "y"

while quit_wish == "y":
  makes_sense = "n"
  while makes_sense == "n":
    function = input("Enter function to be performed. (Encode/Decode): ")
    function = function.lower()
    function = function.strip()
    if function == "encode" or function == "decode":
      makes_sense = "y"
    else:
      print("")
      print("Sorry, that doesn't make sense.")      

  print("")

  print("Special characters except (!), (?), (,) and (') are not supported.")
  text = input("Enter text to be " + function + "d: ")

  print("")

  print("Output:")
  print(convert(text))

  print("")

  makes_sense = "n"
  while makes_sense == "n":
    quit_wish = input("Do you want to continue? (Y/N): ").lower()
    if quit_wish == "y" or quit_wish == "n":
      makes_sense = "y"
    else:
      print("")
      print("Sorry, that doesn't make sense.")

print("")

end_stop = input("Press enter to quit.")

import logging

logging.basicConfig(level=logging.INFO)

#Function start

def decode(text):
  dictionary = ['0', '!', 'a', 'b', '1', 'c', 'd', '2', 'e', 'f', ',', 'g', 'h', '3', 'i', 'j','.', 'k', 'l', '4', 'm', ' ', 'n', '5', 'o', 'p', ':', 'q', 'r', '6', 's', 't', '\'', 'u', 'v', '7', 'w', 'x', '8', 'y', 'z', '?', '9']

  text = text.strip()
  offset_included = 0

  offset_l = int(text[0]) + 1
  offset = int(text[1:offset_l])

  mult = -1 * offset
  output = ""

  for letter in range(offset_l,len(text)):
    input = text[letter].lower() #Taking the first character.

    if input == "`": #"`" is converted back into a space.
      input = " "

    if input not in dictionary: #Checking if the user entered an unsupported character.
      return "Sorry, \"%s\" is not supported." % (input)

    key = (dictionary.index(input) + mult) #Converts the input character into its index in the dictionary, and then adds the multiplier to it to convert it to something else.
    key %= 42 #Ensuring that the index is in the range of the dictionary.

    output += dictionary[key] #Converting the new index to a character and adding it to the output string.

    offset += 1 #Increasing offset, increasing and flipping multiplier for maximum scrambling.
    if mult > 0:
      mult += offset
    elif mult < 0:
      mult -= offset
    mult *= -1

  return output

#Function end
#Program start

import discord

TOKEN = 'NDkxOTMxNTg1MzIzNTk3ODM1.DoPERA.mgg0RKedZH_oHpzs0FgXxRy2X3M'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print("\nChecking message by %s in %s..." % (message.author,message.channel))

    if int(message.content[0:(int(message.content[0]) + 1)]) in range(11,99999):
        msg = ('{0.author.mention} said in %s:\n```\"%s\"```' % (message.channel, decode(message.content))).format(message)
        await client.send_message(client.get_channel('491938711693426688'),msg)
        print("Succesfully decoded.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

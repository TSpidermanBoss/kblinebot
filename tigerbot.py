from pyrogram import Client, Filters
import time

app = Client ("sssrs",bot_token="915514825:AAGpsYi_nwP7RhYTOW7nxveTMjxfg7AhFQI",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")
                                                                                
ferrari = -1001499814617                                             
k = -1001386985008

@app.on_message(Filters.chat(ferrari) & ~ Filters.edited)
def main(client, message):
 mes = client.send_message( k, "**" + message.text + "**" )
 fie = open("ids.txt","a")
 fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
 fie.close()

@app.on_message(Filters.chat(ferrari) & Filters.edited)
def main(client, message):
   files = open("ids.txt" , "r")
   d = files.readlines()
   files.close()
   for c in d:
    x = c.split()
    id = str(message.message_id)
    if id in x:
     try:
       if message.text == ".":
        client.delete_messages(k,int(x[x.index(id)+1]))
       else:
        client.edit_message_text(k,int(x[x.index(id)+1]), "**" + message.text + "**" )
     except FloodWait as e:
        time.sleep(e.x)


@app.on_message(Filters.command('clear') & Filters.user(491634139))
def forward(client, message):
 fie = open("ids.txt","w")
 fie.write("001 002")
 fie.close()
 message.reply("☢️ Done, Editing data cleared ✅✅")



@app.on_message(Filters.command("start"))
def forward(client, message):
 if message.from_user.id == 491634139:
   message.reply("♻️ Welcome to your LineBot . ✅✅")
 else:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")

@app.on_message(Filters.private)
def forward(client, message):
 if not message.from_user.id == 491634139:
   message.reply("♻️ You need admins permission to use my functions. ✅✅")

app.run()

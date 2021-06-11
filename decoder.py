import json
import re
import os
from datetime import datetime

print("-------------------------------------------\n")

print("JSON DECODER MADE BY -")
print("     __  __   ___   .--.                   ")
print("    |  |/  `.'   `. |__|                   ")
print("    |   .-.  .-.   '.--.                   ")
print("    |  |  |  |  |  ||  | ____     _____    ")
print("    |  |  |  |  |  ||  |`.   \  .'    /    ")
print("    |  |  |  |  |  ||  |  `.  `'    .'     ")
print("    |  |  |  |  |  ||  |    '.    .'       ")
print("    |__|  |__|  |__||__|    .'     `.      ")
print("                          .'  .'`.   `.    ")
print("                        .'   /    `.   `.  ")
print("                       '----'       '----' \n")

print("-------------------------------------------")

print("This might take a while. Go for a Monster or something.")

for root, dirs, files in os.walk(os.getcwd()):
    print(f"Searching in {root} ...")
    found = False
    for file in files:
        if file.endswith(".json"):
            print(f"Found {file}")
            found = True
            chat = json.load(open(os.path.join(root + "\\" + file), "r", encoding="utf-8"))
            print(f"Decoding - {file} ...")
            if "messages" not in chat:
                print("Can't decode. Invalid file [Missing \"messages\" list].")
                continue

            messages_history = ""
            for message in chat["messages"]:
                time = datetime.fromtimestamp(message["timestamp_ms"] / 1000.0)
                name = re.sub(r'[\xc2-\xf4][\x80-\xbf]+', lambda m: m.group(0).encode('latin1').decode('utf8'), message['sender_name'])

                if "content" in message:
                    content = re.sub(r'[\xc2-\xf4][\x80-\xbf]+', lambda m: m.group(0).encode('latin1').decode('utf8'), message['content'])
                    messages_history = f"{time:%H:%M:%S %d-%m-%Y} : [ {name} ] -> [ {content} ]\n" + messages_history

                elif "photos" in message:
                    for i in range(len(message["photos"])):
                        try:
                            photo_url = message["photos"][i]["uri"].split("/photos/")
                            messages_history = f">[PHOTO](/photos/{photo_url[1]}) \n" + messages_history
                        except IndexError:
                            messages_history = f">[PHOTO]({message['photos'][i]['uri']}) \n" + messages_history
                    messages_history = f"{time:%H:%M:%S %d-%m-%Y} : [ {name} ] sent photo/s:\n" + messages_history

                elif "videos" in message:
                    for i in range(len(message["videos"])):
                        try:
                            video_url = message["videos"][i]["uri"].split("/videos/")
                            messages_history = f">[VIDEO](/videos/{video_url[1]}) \n" + messages_history
                        except IndexError:
                            messages_history = f">[VIDEO]({message['videos'][i]['uri']}) \n" + messages_history
                    messages_history = f"{time:%H:%M:%S %d-%m-%Y} : [ {name} ] sent video/s:\n" + messages_history

                elif "gifs" in message:
                    for i in range(len(message["gifs"])):
                        gif_url = message["gifs"][i]["uri"].split("/gifs/")
                        messages_history = f">[GIF](/gifs/{gif_url[1]}) \n" + messages_history
                    messages_history = f"{time:%H:%M:%S %d-%m-%Y} : [ {name} ] sent gif/s:\n" + messages_history

                elif "audio_files" in message:
                    for i in range(len(message["audio_files"])):
                        audio_url = message["audio_files"][i]["uri"].split("/audio/")
                        messages_history = f">[AUDIO FILE](/audio/{audio_url[1]}) \n" + messages_history
                    messages_history = f"{time:%H:%M:%S %d-%m-%Y } : [ {name} ] sent audio file/s:\n" + messages_history

                elif "sticker" in message:
                    sticker_url = message["sticker"]["uri"].split("/stickers_used/")
                    messages_history = f">[STICKER](/stickers/{sticker_url[1]}) \n" + messages_history
                    messages_history = f"{time:%H:%M:%S %d-%m-%Y } : [ {name} ] sent sticker:\n" + messages_history

                elif "type" in message:
                    messages_history = f"{time:%H:%M:%S %d-%m-%Y} : [ {name} ] sent unknown message:\n" + messages_history

                else:
                    print("Message doesn't contain valid object")

            open(os.path.join(root + "\\" + file[:-5] + ".txt"), "wb").write(messages_history.encode("utf-8"))
            print(f"Decoding of {file} finished! Saved in {root}\\{file[:-5]}.txt")
    if not found:
        print("No \".json\" file found.")
    print("------------------------------------------------------------------------------------------------------------")

print("Finished, enjoy reading :)")
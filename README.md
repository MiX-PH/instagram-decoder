# instagram-decoder
Decoder and sorter for fetched JSON's of Instagram chats

# How to use
Place this python script in a folder, and run it. It will use `os.walk()` to loop through subfolders to search for files with the `.json` extension.
If it finds a valid file, it will check if it's a valid IG chat fetch and, if it is, it will start decoding and sorting the JSON file. When it's finished, it will save the result file as `.txt` in its directory in chat-like format.  
**Example:**  
13:00:37 31-3-2021  : [ User ] -> [ Message ]

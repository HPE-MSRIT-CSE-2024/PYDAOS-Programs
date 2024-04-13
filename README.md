# PYDAOS-Programs
Program Descriptions:
- chunks.py: This program uploads a file in chunks of sizes specified by the user, and gives the time taken to upload the file in that many number of chunks. Can be used to experiment with different chunk sizes and see which one takes the least amount of time to upload as well as to retrieve it from the directory in those many number of chunks.
-file_upload.py: This program directly uploads a file and gives the time taken to upload. Can be used with files of different sizes to assess how much time each file takes to get uploaded to the daos directory.
-sender.py and receiver.py : This program stores class definitions in the daos directory by serializing it and retrieves it so that an instance of the class, an object, can be created.
-sender_dict.py and receiver_dict.py : This program stores dictionary objects in a serialized form in the daos directory and retrieves them, so that they can be used in a different program.

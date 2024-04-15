# PYDAOS Programs

## Program Descriptions:

### chunks.py:
- This program uploads a file in chunks of sizes specified by the user and provides the time taken to upload the file in that many number of chunks. 
- It can be used to experiment with different chunk sizes to determine which one takes the least amount of time to upload, as well as to retrieve it from the directory in those many numbers of chunks.

### file_upload.py:
- This program directly uploads a file and provides the time taken to upload. 
- It can be used with files of different sizes to assess how much time each file takes to be uploaded to the DAOS directory.

### sender.py and receiver.py:
- This program stores class definitions in the DAOS directory by serializing them and retrieves them so that an instance of the class, an object, can be created.
- file:///home/hpecty/Downloads/Screenshot%20from%202024-04-15%2015-14-30.png

### sender_dict.py and receiver_dict.py:
- This program stores dictionary objects in a serialized form in the DAOS directory and retrieves them, allowing their use in a different program.

import os
import time
from pydaos import DCont, DDict

# Create a DAOS container
daos_cont = DCont("pydaos", "kvstore", None)

# Create a DAOS dictionary or get it if it already exists
try:
    daos_dict = daos_cont.get("pydaos_kvstore_dict")
except:
    daos_dict = daos_cont.dict("pydaos_kvstore_dict")

# Directory to store uploaded files
upload_dir = "uploads"
os.makedirs(upload_dir, exist_ok=True)

# Function to print help
def print_help():
    print("?\t- Print this help")
    print("r\t- Read a key")
    print("u\t- Upload file for a new key")
    print("p\t- Display keys")
    print("q\t- Quit")

n=int(input("Enter size of chunks (in MB) : "))
CHUNK_SIZE=n*1024*1024

# Function to read a key with time measurement
def read_key():
  try:
    key = input("Enter key to read: ")
    chunk_count = 0
    assembled_data = b""
    
    start_time = time.time() 
    while True:
      chunk_key = f"{key}chunk{chunk_count}"
      try:
        chunk_data = daos_dict[chunk_key]
        assembled_data += chunk_data
        chunk_count += 1
      except KeyError:
        break

    end_time = time.time()
    retrieval_time = end_time - start_time

    if assembled_data:
      save_value_as_file(key, assembled_data)
      
      print(f"Value retrieved successfully. Total chunks: {chunk_count}.Time taken: {retrieval_time} seconds")
    else:
      print("Key not found.")

  except KeyError:
    print("\tError! Key not found")


# Function to save value as a file
def save_value_as_file(key, value):
    filename = os.path.join(upload_dir, f"{key}.dat")
    with open(filename, "wb") as f:
        f.write(value)
    print(f"Value saved as file: {filename}")

#Function to print all keys
def print_keys():
    for i in daos_dict:
        print(i)

# Function to upload file for a new key with time measurement
def upload_file():
  key = input("Enter new key: ")
  file_path = input("Enter path to file: ")

  chunk_dict={}
  if os.path.exists(file_path):
    start_time = time.time()
    with open(file_path, "rb") as f:
      chunk_count = 0
      while True:
        data = f.read(CHUNK_SIZE)
        if not data:
          break
        chunk_key = f"{key}chunk{chunk_count}"
        chunk_dict[chunk_key]=data
        chunk_count += 1
    daos_dict.bput(chunk_dict)
    end_time = time.time()
    upload_time = end_time - start_time

    print(f"File uploaded in {chunk_count} chunks successfully.Time taken: {upload_time} seconds")
  else:
    print("File not found.")



# Main loop
while True:
    print("\nCommands:")
    print_help()
    cmd = input("Enter command (? for help): ")

    if cmd == "?":
        print_help()
    elif cmd == "r":
        read_key()
    elif cmd == "u":
        upload_file()
    elif cmd == "q":
        break
    else:
        print("Invalid command. Enter '?' for help.")

print("Program ended.")

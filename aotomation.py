import os
import shutil

def organize_files(directory):
  for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
      extension = os.path.splitext(filename)[1]
      if extension:
        new_directory = os.path.join(directory, extension[1:])
        if not os.path.exists(new_directory):
          os.makedirs(new_directory)
        shutil.move(filepath, new_directory)

if __name__ == "__main__":
  directory = input("Enter the directory to organize: ")
  organize_files(directory)
  print(f"Files organized in {directory}")
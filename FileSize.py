# INPUT:The first argument to your program has the path to the file you need to check the size of.
# OUTPUT SAMPLE: Print the size of the file in bytes.

import os

def fileSize(path_to_file):
    file_size = os.path.getsize(path_to_file)
    print file_size


# Open files to read or write
# Open an existing file named 'test.txt'
# This open the file in 'read-only' mode where you can only read the file contents. You can check the 'my_file'
# object's file mode and encoding properties by printing the file object.
my_file = open('test.txt')
print('my_file : ', my_file)
# Python uses the idea of the cursor to read a file
# Reading the file content in one go
print("my_file.read() : ", my_file.read()) # The cursor used for reading file has reached the end of the file
print("my_file.read() : ", my_file.read()) # There is nothing left to read in the file
my_file.seek(0) # Set the Cursor back to the start of the file
print("my_file.seek(0)")
print("my_file.read() : ", my_file.read()) 

print()
print()

my_file2 = open('text2.txt')
# read a file line-by-line using readline()
print("my_file2.readline() : ", my_file2.readline())
print("my_file2.readline() : ", my_file2.readline())
print("my_file2.readline() : ", my_file2.readline())
print()
print()
# Use readlines() to get all the lines of the file as a list
print("my_file2.readlines() : ")
print(my_file2.readlines())

# Close the files after reading through / writing into them
my_file.close()
my_file2.close()


# A better way to read or write and close files is using the 'with' statement
with open('text2.txt') as my_file2:
    print(my_file2.readlines())
    # The file automatically closes when the 'with' code block is executed


# Read and Write to an existing file using the 'r+' mode
# Using the 'r+' mode will always start from the start of the file, and will overwrite any existing file content
try:
    with open('write.txt', mode='r+') as my_file3:
        my_file3.write("hey it's me")
    with open('write.txt', mode='r+') as my_file3:
        my_file3.write("bo")
except FileNotFoundError as err: # Error Handling for File IO
    print('the file does not exist!')
    raise err
except IOError as err:
    print('IO error - something wrong in your system')
    raise err

# Create a new file of the given name and write into it. Any existing file of the same name will be erased.
# Here, we are using relative path to create a new file - the 'test' directory is accessible to this script because
# this script is in the same directory as the 'test' directory.
# Relative paths starting with './' mean from current directory.
# Relative paths starting with '../' mean from parent directory of current directory.
with open('test/write.txt', mode='w') as my_file3:
    my_file3.write(':)')


# We can also provide absolute paths of files like: 'C:\Users\pdcdi\Desktop\haha.txt'
with open('C:\\Users\\pdcdi\\Desktop\\haha.txt', mode='w') as my_file3:
    my_file3.write('hoho haha')


# The 'pathlib', 'glob' and 'os' are some common modules to work with file and directory paths in python.
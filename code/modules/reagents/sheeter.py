import os



def textparser(file_path):
    file = open(file_path, 'r')
    for line in file:
        print(line)
    file.close

# iterate through all file
ourpath = os.getcwd()
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".dm"):
        file_path = f"{ourpath}\{file}"

        # call read text file function
        textparser(file_path)


#open file
# for line
# recognize if core datum, on_mob_life, overdose_process, on_transfer
# write datum line as ID to list
# write
# end for when newline without whitespace at start

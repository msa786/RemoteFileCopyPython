# # search for drives in windows
# # find pdf etc in each drive recursively
# # store the found files in a folder
# # create a remote connection to sftp socketserver
# # upload it to the remote server
# close the connection
# delete the folder where pdf etc was stored


# finding the available drives in windows

import os

def get_drives():
    drives = []
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        drive = letter + ':'
        if os.path.exists(drive):
            drives.append(drive)
    return drives

# finding specific extension files in each drives
def find_files(directory, extensions):
    """Recursively finds files with specified extensions in a given directory.

    Args:
        directory (str): The root directory to search.
        extensions (list): A list of file extensions to search for.

    Returns:
        list: A list of file paths.
    """

    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(tuple(extensions)):
                files.append(os.path.join(root, filename))
    return files



def searchFileExtension():
    extensions = ['.pdf']  # Add more extensions as needed
    drives = get_drives()  # Use any of the methods from the previous response to get drives

    for drive in drives:
        try:
            files = find_files(drive, extensions)
            for file in files:
                print(file)
        except OSError:
            print(f"Error accessing drive: {drive}")





if __name__ == '__main__':
    drives = get_drives()
    print(drives)
    searchFileExtension()
    find_files()

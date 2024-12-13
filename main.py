import os
import zipfile
import tempfile
import csv
from emulator.commands import CommandHandler
from emulator.filesystem import FileSystem

def load_config(config_path):
    with open(config_path, mode='r') as file:
        reader = csv.reader(file)
        config = list(reader)
        username = config[0][0]
        fs_path = config[1][0]
        start_script_path = config[2][0]
    return username, fs_path, start_script_path

def main():
    username, fs_path, start_script_path = load_config('config.csv')

    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(fs_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        print(f"Extracted virtual file system to: {temp_dir}")

        fs = FileSystem(temp_dir)

        handler = CommandHandler(fs)

        with open(start_script_path, 'r') as script:
            for line in script:
                handler.execute_command(line.strip())

        while True:
            try:
                command = input(f"{username}@shell: {fs.current_path}$ ")
                handler.execute_command(command.strip())
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()

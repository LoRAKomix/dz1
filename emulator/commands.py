import os

class CommandHandler:
    def __init__(self, fs):
        self.fs = fs

    def execute_command(self, command):
        parts = command.split()
        cmd = parts[0]

        if cmd == "pwd":
            self.pwd()
        elif cmd == "cd":
            self.cd(parts[1])
        elif cmd == "ls":
            self.ls()
        elif cmd == "exit":
            self.exit()
        elif cmd == "chmod":
            if len(parts) != 3:
                print("Usage: chmod <permissions> <path>")
                return
            self.chmod(parts[1], parts[2])
        else:
            print(f"Unknown command: {cmd}")

    def pwd(self):
        print(self.fs.current_path)

    def cd(self, path):
        self.fs.change_directory(path)

    def ls(self):
        resolved_path = self.fs.resolve_path(self.fs.current_path)
        if os.path.isdir(resolved_path):
            print("\n".join(os.listdir(resolved_path)))
        else:
            print(f"Error: {resolved_path} is not a directory")

    def exit(self):
        print("Exiting...")
        quit()

    def chmod(self, permissions, path):
        self.fs.chmod(path, permissions)

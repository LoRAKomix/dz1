def parse_command(command_line):
    parts = command_line.strip().split()
    if not parts:
        return None, []
    return parts[0], parts[1:]

def is_valid_command(command):
    supported_commands = {"ls", "cd", "pwd", "chmod", "exit"}
    return command in supported_commands

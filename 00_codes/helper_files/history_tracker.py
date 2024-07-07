import os
import subprocess
import time


history_file = "/home/aurora/Desktop/00_vinayd/topics/00_command_history.md"
zsh_history = "/home/aurora/.zsh_history"
def append_command_to_history(command):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(history_file, "a") as file:
        file.write(f"- [{timestamp}] {command}\n")

def get_previous_commands():
    previous_commands = set()
    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            for line in file:
                if line.startswith("- "):
                    command = line.split("]", 1)[-1].strip()
                    if command:
                        previous_commands.add(command)
    return previous_commands

def monitor_commands():
    while True:
        previous_commands = get_previous_commands()
        current_commands = set()
        with open(zsh_history, "r") as file:
            for line in file:
                current_commands.add(line.strip())
                
        # current_commands = subprocess.getoutput("history").split("\n")
        new_commands = [cmd for cmd in current_commands if cmd not in previous_commands]
        for cmd in new_commands:
            append_command_to_history(cmd)
            previous_commands.add(cmd)
        time.sleep(300)  # Check every 5 mins


def main():
    
    if not os.path.exists(history_file):
        with open(history_file, "w") as file:
            file.write("# Command History\n")
    monitor_commands()

if __name__ == "__main__":
    main()

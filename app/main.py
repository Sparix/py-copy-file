def copy_file(command: str) -> None:
    command_split = command.split()
    old_file = command_split[1]
    new_file = command_split[2]
    if old_file != new_file and command_split[0] == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            for file_line in file_in:
                file_out.write(file_line)

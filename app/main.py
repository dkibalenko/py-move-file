import os


def move_file(command: str) -> None:
    command_, current_file, path_new_file = command.split()

    path_new_file_list = path_new_file.split('/')
    destination_dir = "/".join(path_new_file_list[:-1])
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    with (
        open(current_file, "r") as file_in,
        open(path_new_file, "w") as file_out
    ):
        file_out.write(file_in.read())

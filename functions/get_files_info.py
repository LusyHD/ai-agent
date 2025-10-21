import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    working_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(full_path)

    if target_abs == working_abs or target_abs.startswith(working_abs + os.sep):
        if os.path.isdir(target_abs):
            try:
                names = os.listdir(target_abs)
                line_list = []

                for name in names:
                    entry_path = os.path.join(target_abs, name)
                    is_dir = os.path.isdir(entry_path)
                    size = os.path.getsize(entry_path)
                    line = (f'- {name}: file_size={size} bytes, is_dir={str(is_dir)}')

                    line_list.append(line)

                return('\n'.join(line_list))

            except Exception as e:
                return(f'Error: {e}')

        else:
            return(f'Error: "{directory}" is not a directory')

    else:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

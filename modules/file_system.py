import os

exclude_files_on_cleanup = [
    "layout.json",
]

class PathInfo ():
    def __init__(self, path):
        self.path = path.replace('./', '')
        parts = self.path.split('/')
        dir_parts = parts[:-1] if len(parts) else []
        self.is_dir = False
        try:
            os.listdir(path)
            self.is_dir = True
        except OSError:
            pass

        self.prev_dirs = []
        for dir in dir_parts:
            self.prev_dirs.append((self.prev_dirs[-1] if len(self.prev_dirs) else ".") + os.sep + dir)

        self.dir = (os.sep).join(dir_parts) if len(dir_parts) else ""
        self.parent_dir_exists = False
        try:
            len(os.listdir(self.dir))
            self.parent_dir_exists = True
        except OSError:
            pass

def cleanup_dir (path_list = os.listdir('./'), prev_path=""):
    for path in path_list:
        current_path = prev_path + (os.sep if prev_path else "") + path
        path_info = PathInfo(current_path)
        print("current_path in cleanup_dir", current_path)
        if current_path not in exclude_files_on_cleanup:
            if path_info.is_dir:
                cleanup_dir(os.listdir(current_path), current_path)
                try:
                    os.rmdir(current_path)
                except OSError:
                    pass
            else:
                try:
                    os.remove(current_path)
                except OSError:
                    pass

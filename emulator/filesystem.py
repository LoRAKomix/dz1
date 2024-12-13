import os

class FileSystem:
    def __init__(self, base_path):
        self.base_path = os.path.abspath(base_path)  # Абсолютный путь к базе
        self.current_path = "/"  # Установите начальную текущую директорию на корень

    def resolve_path(self, path):
        print(f"Resolving path: {path}")  # Для отладки
        
        if path.startswith("/"):
            resolved = os.path.normpath(os.path.join(self.base_path, path.lstrip("/")))
        else:
            resolved = os.path.normpath(os.path.join(self.base_path, self.current_path, path))

        print(f"Resolved path: {resolved}")  # Для отладки
        
        if not os.path.exists(resolved):
            raise FileNotFoundError(f"Directory not found: {path}")
        
        if not resolved.startswith(self.base_path):
            raise ValueError(f"Path is outside of mounted filesystem: {resolved}")
        
        return resolved

    def change_directory(self, path):
        print(f"Changing directory to: {path}")  # Для отладки
        resolved = self.resolve_path(path)
        if os.path.isdir(resolved):
            self.current_path = os.path.relpath(resolved, self.base_path)
        else:
            raise FileNotFoundError(f"Directory not found: {path}")

    def chmod(self, path, permissions):
        resolved = self.resolve_path(path)
        if os.path.exists(resolved):
            mode = 0
            if 'r' in permissions:
                mode |= 0o444
            if 'w' in permissions:
                mode |= 0o222
            if 'x' in permissions:
                mode |= 0o111

            os.chmod(resolved, mode)
        else:
            raise FileNotFoundError(f"File or directory not found: {path}")

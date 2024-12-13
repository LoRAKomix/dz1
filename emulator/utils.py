import os
import logging

def log_error(message):
    logging.error(message)

def validate_path(path, base_path):
    resolved_path = os.path.normpath(os.path.join(base_path, path.lstrip("/")))
    if not resolved_path.startswith(base_path):
        raise ValueError("Path is outside of the mounted filesystem")
    return resolved_path

def format_output(data):
    if isinstance(data, list):
        return "\n".join(data)
    return str(data)

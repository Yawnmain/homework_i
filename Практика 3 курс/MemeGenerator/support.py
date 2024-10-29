import os
import json

def set_env_vars_from_json(file_path):
  with open(file_path, 'r') as file:
    env_vars = json.load(file)

  for key, value in env_vars.items():
    os.environ[key] = value

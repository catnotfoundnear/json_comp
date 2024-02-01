py -3.13 -m venv json_env_py3_13
py -3.12 -m venv json_env_py3_12
py -3.11 -m venv json_env_py3_11
py -3.10 -m venv json_env_py3_10
py -3.9 -m venv json_env_py3_9
py -3.8 -m venv json_env_py3_8

start install_deps.bat json_env_py3_13
start install_deps.bat json_env_py3_12
start install_deps.bat json_env_py3_11
start install_deps.bat json_env_py3_10
start install_deps.bat json_env_py3_9
start install_deps.bat json_env_py3_8

py -3.8 move_data.py
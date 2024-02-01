import shutil
import lzma
import os


def decompress(path):
    with open(path, "rb") as f:
        data = lzma.decompress(f.read())

    with open(path[:-3], "wb") as f:
        f.write(data)


def copy_data_to_folder(folder):
    shutil.copy("data/citm_catalog.json", folder)
    shutil.copy("data/github.json", folder)
    shutil.copy("data/twitter.json", folder)
    shutil.copy("data/canada.json", folder)
    shutil.copy("bench.py", folder)


os.chdir("data")

decompress("citm_catalog.json.xz")
decompress("github.json.xz")
decompress("twitter.json.xz")
decompress("canada.json.xz")

os.chdir("..")

copy_data_to_folder("json_env_py3_13/scripts")
copy_data_to_folder("json_env_py3_8/scripts")
copy_data_to_folder("json_env_py3_9/scripts")
copy_data_to_folder("json_env_py3_10/scripts")
copy_data_to_folder("json_env_py3_11/scripts")
copy_data_to_folder("json_env_py3_12/scripts")

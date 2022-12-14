import os
import sys
import shutil

try:
    import wget
except ImportError:
    os.system("python -m pip install wget")


def zip_downloader():
    """
    Function to download any zip file from the url passed in the 1st argument and
    extracted in the folder specified in 2nd argument to the script.
    """
    zip_url = sys.argv[1]
    zip_folder = sys.argv[2]
    new_file_name = zip_url.split("/")[-1]
    wget.download(url=zip_url, out=zip_folder)
    shutil.unpack_archive(
        filename=zip_folder + "\\" + new_file_name,
        extract_dir=zip_folder,
        format="zip",
    )
    os.system(f"del {zip_folder}\*.zip") # Clean up
    print(
        f"{new_file_name} is successfully downloaded and extracted inside {zip_folder} folder"
    )


if __name__ == "__main__":
    zip_downloader()

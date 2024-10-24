import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)
            
if __name__ == "__main__":
    make_archive(filepaths=["test1",  "test2", "test3"], dest_dir="dest")
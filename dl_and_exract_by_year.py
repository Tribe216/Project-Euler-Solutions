#!/usr/bin/env python3
from pathlib import Path
from shutil import unpack_archive

zip_files = Path(r"gain_zips").rglob("*.zip")
while True:
    try:
        path = next(zip_files)
    except StopIteration:
        break  # no more files
    else:
        extract_dir = path.with_name(path.stem)
        unpack_archive(str(path), str(extract_dir), 'zip')

BASE_URL = "http://ratedata.gaincapital.com/"

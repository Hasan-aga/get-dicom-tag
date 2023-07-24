import argparse
import os
import pydicom
from typing import Set

def extract_dicom_tag(directory: str, tag: str) -> Set[str]:
    tag_values = set()

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".dcm"):
                filepath = os.path.join(root, filename)
                dataset = pydicom.dcmread(filepath)
                if tag in dataset:
                    tag_values.add(str(dataset.data_element(tag).value))

    return tag_values

def main():
    parser = argparse.ArgumentParser(description='Extract DICOM tag values.')
    parser.add_argument('directory', help='Directory containing DICOM files')
    parser.add_argument('keyword', help='keyword of tag you want to find')

    args = parser.parse_args()

    tag_values = extract_dicom_tag(args.directory, args.keyword)
    print(tag_values)

if __name__ == '__main__':
    main()

import os
import glob
import pathlib
import argparse


# Setting up Argument Parser
parser = argparse.ArgumentParser(description='Merge all markdown files in a specified folder into a single file.')
parser.add_argument('--folder-path', type=str, help='Path to the folder containing text files')
parser.add_argument('--output-fpath', type=str, default='merged_file.md', help='Name of the output file')

args = parser.parse_args()


def main():
    folder_path = os.path.expanduser(args.folder_path)
    output_fpath = os.path.expanduser(args.output_fpath)

    md_fpaths = glob.glob(os.path.join(folder_path, '*.md'))

    with open(output_fpath, 'w') as output_file:
        for fpath in md_fpaths:
            with open(fpath) as input_file:
                for line in input_file:
                    output_file.write(line)

    print(f"Files merged successfully into '{output_fpath}'.")


if __name__ == "__main__":
    main()

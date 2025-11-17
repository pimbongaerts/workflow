#!/usr/bin/env python
"""
Download model folder from remote server using rsync
"""
import argparse
import os
import subprocess

BASEPATH = "/home/coral3d/focal_plots"
USERNAME = "deepcat"
COMPUTER = "deepsheep"


def parse_size(size_str):
    """Convert size string to format rsync understands (e.g., '5GB' -> '5G')"""
    size_str = size_str.upper()
    if size_str.endswith("GB"):
        return size_str.replace("GB", "G")
    elif size_str.endswith("MB"):
        return size_str.replace("MB", "M")
    elif size_str.endswith("KB"):
        return size_str.replace("KB", "K")
    return size_str


def main():
    parser = argparse.ArgumentParser(
        description="Download model folder from remote server using rsync"
    )
    parser.add_argument(
        "model",
        help=("Model name (e.g., 'model_part1_part2' or " "'model_part1_part2_part3')"),
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Download everything without any exclusions",
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help=(
            "Download everything except files over max_filesize "
            "(includes subfolders)"
        ),
    )
    parser.add_argument(
        "--small",
        action="store_true",
        help=(
            "Download everything except files over 300MB and subfolders "
            "(same as default but with 300MB max_filesize)"
        ),
    )
    parser.add_argument(
        "--max_filesize",
        default="5GB",
        help=(
            "Maximum file size to download (default: 5GB). "
            "Files larger than this will be excluded unless --full is used."
        ),
    )

    args = parser.parse_args()

    # Build target path using same logic as get_model_folder.py
    cols = args.model.split("_")
    if len(cols) == 4:
        target_path = "{0}/{1}_{2}/{1}_{2}_{3}/{1}_{2}_{3}_{4}/".format(
            BASEPATH, cols[0], cols[1], cols[2], cols[3]
        )
    elif len(cols) == 3:
        target_path = "{0}/{1}_{2}/{1}_{2}_{3}/".format(
            BASEPATH, cols[0], cols[1], cols[2]
        )
    elif len(cols) == 2:
        target_path = "{0}/{1}/".format(BASEPATH, args.model)
    else:
        parser.error("Incorrect model name format")

    # Get current working directory
    cwd = os.getcwd()

    # Extract parent folder name from target_path
    # Remove trailing slash and get basename
    parent_folder = os.path.basename(target_path.rstrip("/"))
    if not parent_folder:
        # If basename is empty, get the last non-empty component
        parent_folder = os.path.basename(os.path.dirname(target_path.rstrip("/")))

    # Create destination folder in current working directory
    dest_folder = os.path.join(cwd, parent_folder)
    os.makedirs(dest_folder, exist_ok=True)

    # Construct rsync command
    remote_path = f"{USERNAME}@{COMPUTER}:{target_path}"
    rsync_cmd = ["rsync", "-avz"]

    # Add options based on scenario
    if args.full:
        # Download everything, no restrictions
        print(f"Downloading everything from {target_path}...")
    elif args.compact:
        # Download everything except files over max_filesize
        # (includes subfolders)
        max_size = parse_size(args.max_filesize)
        rsync_cmd.extend(["--max-size", max_size])
        print(
            f"Downloading {target_path} "
            f"(excluding files over {args.max_filesize})..."
        )
    elif args.small:
        # Default behavior but with 300MB max_filesize
        max_size = parse_size("300MB")
        rsync_cmd.extend(["--max-size", max_size, "--exclude", "*/"])
        print(
            f"Downloading {target_path} "
            f"(excluding files over 300MB and subfolders)..."
        )
    else:
        # Default: exclude files over max_filesize and exclude subfolders
        max_size = parse_size(args.max_filesize)
        rsync_cmd.extend(["--max-size", max_size, "--exclude", "*/"])
        print(
            f"Downloading {target_path} "
            f"(excluding files over {args.max_filesize} and subfolders)..."
        )

    rsync_cmd.extend([remote_path, dest_folder])

    print(f"From: {USERNAME}@{COMPUTER}")
    print(f"To: {dest_folder}")
    subprocess.run(rsync_cmd)


if __name__ == "__main__":
    main()

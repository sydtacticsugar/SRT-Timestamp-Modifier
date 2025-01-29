import re
import argparse
import sys
import pathlib
import glob
import os

def arguments():
    parser = argparse.ArgumentParser(description="""Adjust the timing of a subtitle file by adding or subtracting a specified number of seconds to each timestamp.""",
                usage="""%(prog)s [-f FILE] [-s SECONDS] [-d DIRECTION]""", add_help=False)
    parser.add_argument('-f', '--file',
                    required=False, default=None, type=pathlib.Path,
                    help="""Path to the SRT subtitle file""")
    parser.add_argument('-s', '--seconds',
                    required=False, default=None, type=int,
                    help="""Number of seconds to add or subtract to each timestamp""")
    parser.add_argument('-d', '--direction',
                    required=False, default=None, choices=['forward', 'forwards', 'backward', 'backwards'], type=str.lower,
                    help="""Direction of time change (either "forward"/"forwards" or "backward"/"backwards")""")
    parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 2.0', help="""Show program's version number and exit.""")
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help="""Show this help message and exit.""")
    return parser.parse_args()
args = arguments()

def adjust_subtitle_time(file_path, seconds_to_add, direction):
    """
    Adjusts the timing of a subtitle file by adding or subtracting a specified number of seconds to each timestamp.

    Args:
        file_path (str): Path to the SRT subtitle file
        seconds_to_add (int): Number of seconds to add or subtract to each timestamp
        direction (str): Direction of time change (either "forward" or "backward")
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression pattern to match timestamp lines
    pattern = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})')

    # Find all timestamp lines and adjust the timing
    adjusted_content = pattern.sub(lambda match: adjust_timestamp(match, seconds_to_add, direction), content)

    # Write the adjusted content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(adjusted_content)

def adjust_timestamp(match, seconds_to_add, direction):
    """
    Adjusts a single timestamp by adding or subtracting the specified number of seconds.

    Args:
        match (re.Match): Match object containing the timestamp
        seconds_to_add (int): Number of seconds to add or subtract to the timestamp
        direction (str): Direction of time change (either "forward" or "backward")
    """
    start_time, end_time = match.groups()
    start_hours, start_minutes, start_seconds, start_milliseconds = map(int, start_time.replace(':', ',').split(','))
    end_hours, end_minutes, end_seconds, end_milliseconds = map(int, end_time.replace(':', ',').split(','))

    # Calculate the new timestamp values
    if direction == "forward" or direction == "forwards":
        new_start_seconds = start_seconds + seconds_to_add
        new_end_seconds = end_seconds + seconds_to_add
    elif direction == "backward" or direction == "backwards":
        new_start_seconds = start_seconds - seconds_to_add
        new_end_seconds = end_seconds - seconds_to_add

    # Handle cases where the seconds value exceeds 59
    new_start_minutes = start_minutes
    new_end_minutes = end_minutes
    if new_start_seconds >= 60:
        new_start_minutes += 1
        new_start_seconds -= 60
    elif new_start_seconds < 0:
        new_start_minutes -= 1
        new_start_seconds += 60

    if new_end_seconds >= 60:
        new_end_minutes += 1
        new_end_seconds -= 60
    elif new_end_seconds < 0:
        new_end_minutes -= 1
        new_end_seconds += 60

    # Format the new timestamp values
    new_start_time = f'{start_hours:02d}:{new_start_minutes:02d}:{new_start_seconds:02d},{start_milliseconds:03d}'
    new_end_time = f'{end_hours:02d}:{new_end_minutes:02d}:{new_end_seconds:02d},{end_milliseconds:03d}'

    return f'{new_start_time} --> {new_end_time}'

def filecheck(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print("SRT file loaded successfully!")
    except FileNotFoundError:
        print("Error: SRT file not found. Please check the file path and try again.")
    except UnicodeDecodeError:
        print("Error: Unable to decode file. Please try specifying a different encoding.")

# check if file_path is a single file or a glob
# returns [] if file(s) not found
def fileOrGlob(file_path):
    if os.path.isfile(file_path) == True:
        return 1
    else:
        return glob.glob(str(file_path), recursive=True)
        

def main():
    # assign values based on args - defaults are all set to "None"
    file_path = args.file
    seconds_to_add = args.seconds
    direction = args.direction

    # if no args provided - run in interactive mode
    if len(sys.argv) == 1:
        print("Please enter the path to your SRT file:")
        file_path = input()

        print("Do you want to adjust the timing forward or backward?")
        direction = input().lower()
        while direction not in ["forward", "forwards", "backward", "backwards"]:
            print("Invalid input. Please enter 'forward'/'forwards' or 'backward'/'backwards':")
            direction = input().lower()

        print("How many seconds do you want to adjust the timing?")
        seconds_to_add = int(input())
    #if all args present - run without further interaction
    elif file_path is not None and seconds_to_add is not None and direction is not None:
        pass
    else:
        print("""Missing argument(s).
        usage: subtitle-time-adjuster.py [-f FILE] [-s SECONDS] [-d DIRECTION]""")
        sys.exit(1)

    globby = fileOrGlob(file_path)
    # if glob instead of single file - iterate over the list of files
    if globby and globby != 1:
        for file in globby:
            try:
                adjust_subtitle_time(file, seconds_to_add, direction)
            except Exception as e:
                print(f"Error: Timing adjustment failed. {str(e)}")
        print(f"Timing adjustment successful! Your SRT files have been adjusted by {seconds_to_add} seconds {'forward' if direction == 'forward' else 'backward'}.")
    else:
        filecheck(file_path)
        try:
            adjust_subtitle_time(file_path, seconds_to_add, direction)
            print(f"Timing adjustment successful! Your SRT file has been adjusted by {seconds_to_add} seconds {'forward' if direction == 'forward' else 'backward'}.")
        except Exception as e:
            print(f"Error: Timing adjustment failed. {str(e)}")


if __name__ == "__main__":
    main()
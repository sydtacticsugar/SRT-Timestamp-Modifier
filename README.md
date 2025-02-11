# Subtitle Time Adjuster

Subtitle Time Adjuster is a simple Python script that helps you adjust the timing of subtitles in `.srt` files. If you've ever found that your subtitles are out of sync with the movie or video, this tool allows you to move the entire subtitle timing forward or backward by a specified number of seconds.

## Changes Made in This Fork

This is a fork of tepelekas' SRT-Timestamp-Modifier script. This fork adds the ability to run the program in a single line, with no further interaction/input needed. 

It also adds the ability to use backwards/forwards as direction words (in addition to the existing backward/forward options). This was merely to account for potential [dialectic/idiolectic differences](https://english.stackexchange.com/questions/109924/is-it-backward-forward-or-backwards-forwards).

Lastly - I have added the ability to use wildcards, in order to batch process files that are all "off" by the same amount of time in the same "direction".

## Features

- Adjust subtitle timing forward or backward.
- Easily modify the timing of all subtitles in a `.srt` file at once.
- Simple command-line interface.
- Capable of handling wildcards for batch processing.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/sydtacticsugar/SRT-Timestamp-Modifier.git
    ```

2. Navigate to the project directory:

    ```bash
    cd subtitle-time-adjuster
    ```

3. Ensure you have Python 3 installed. If not, download and install it from [python.org](https://www.python.org/).

### Usage

#### Using a single command

```bash
python subtitle-time-adjuster.py -f FILE -d DIRECTION -s SECONDS
```

##### Options
```
  -f FILE, --file FILE  Path to the SRT subtitle file
  -s SECONDS, --seconds SECONDS
                        Number of seconds to add or subtract to each timestamp
  -d {forward,forwards,backward,backwards}, --direction {forward,forwards,backward,backwards}
                        Direction of time change (either "forward"/"forwards" or "backward"/"backwards")
  -v, --version         Show program's version number and exit.
  -h, --help            Show this help message and exit.
```

#### Using interactive mode

1. Run the script:

    ```bash
    python subtitle-time-adjuster.py
    ```

2. Follow the on-screen prompts:

    - Enter the path to your `.srt` file.
    - Choose whether to adjust the timing forward or backward.
    - Enter the number of seconds you want to shift the subtitles.

3. The script will adjust the timings and save the modified subtitles back to the same file.

### Examples

Assume you have an `.srt` file located at `/movies/subtitles.srt` that is ahead by 5 seconds. You can correct the timing by running the script as follows:

```bash
python subtitle-time-adjuster.py -f "/movies/subtitles.srt" -d backward -s 5
```

#### Wildcard usage

Let's say - like me, when I began modifying this script - you have nearly 100 `.srt` files that are all ahead by 4 seconds. You can batch process these like so:

##### Single command
If they're all in the same directory:

```
movies/
├── file1.srt
├── file2.srt
├── file3.srt
├── fileA.srt
├── fileB.srt
└── fileC.srt
```

You can run this command to adjust all 6 `.srt` files at once:
```bash
python subtitle-time-adjuster.py -f "/movies/*.srt" -d backward -s 4
```

If they are in different subdirectories:

```
movies/
├── subDir1/
│   ├── file1.srt
│   ├── file2.srt
│   └── file3.srt
└── subDir2/
    ├── fileA.srt
    ├── fileB.srt
    └── fileC.srt
```

You can run this command to adjust all 6 `.srt` files at once:
```bash
python subtitle-time-adjuster.py -f "/movies/**/*.srt" -d backward -s 4
```

##### Interactive mode
```
Please enter the path to your SRT file(s):
movies/*.srt
Do you want to adjust the timing forward or backward?
backward
How many seconds do you want to adjust the timing?
4
```

**Please note:** Interactive mode will automatically enclose your path input in quoation marks - do not try entering `"/movies/*.srt"` in this mode, as it will result in an error.
# Subtitle Time Adjuster

Subtitle Time Adjuster is a simple Python script that helps you adjust the timing of subtitles in `.srt` files. If you've ever found that your subtitles are out of sync with the movie or video, this tool allows you to move the entire subtitle timing forward or backward by a specified number of seconds.

## Features

- Adjust subtitle timing forward or backward.
- Easily modify the timing of all subtitles in a `.srt` file at once.
- Simple command-line interface.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/tepelekas/SRT-Timestamp-Modifier.git
    ```

2. Navigate to the project directory:

    ```bash
    cd subtitle-time-adjuster
    ```

3. Ensure you have Python 3 installed. If not, download and install it from [python.org](https://www.python.org/).

### Usage

1. Run the script:

    ```bash
    python subtitle_adjuster.py
    ```

2. Follow the on-screen prompts:

    - Enter the path to your `.srt` file.
    - Choose whether to adjust the timing forward or backward.
    - Enter the number of seconds you want to shift the subtitles.

3. The script will adjust the timings and save the modified subtitles back to the same file.

### Example

Assume you have an `.srt` file located at `C:/movies/subtitles.srt` that is out of sync by 5 seconds. You can correct the timing by running the script as follows:

```bash
python subtitle_adjuster.py

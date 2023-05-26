# Audio File Divider

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)

A Python script that allows you to divide an audio file into 10-minute pieces.

## Prerequisites

- Python 3.6 or above
- `pydub` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/audio-file-divider.git
   ```

2. Install the required dependencies:

   ```bash
   pip install pydub
   ```

## Usage

Run the script from the command line with the audio file path as an argument:

```bash
python audio_divider.py path/to/audio/file.mp3
```

The audio file will be divided into 10-minute pieces, and the resulting pieces will be saved in the same directory as the script.

## Example

Let's say you have an audio file named audio.mp3 located in the audio_files directory. You can run the script as follows:

```bash
python audio_divider.py audio_files/audio.mp3
```

The script will divide the audio.mp3 file into 10-minute pieces and save them as audio_0_600000.mp3, audio_600000_1200000.mp3, and so on, representing the start and end times of each segment in milliseconds.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the MIT License.

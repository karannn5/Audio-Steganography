# Audio Steganography CLI

Audio Steganography is a technique used to hide secret messages within audio files. This project provides a command-line interface (CLI) for encoding and decoding messages in audio files using various steganography algorithms. Additionally, it provides a method to calculate the accuracy of the decoded message against the original secret message.

## Contents

- **Original Audio Sample**: `input/original_sample.wav`
- **Supported Algorithms**:  - Standard LSB Steganography
## Algorithms Overview

###  Standard LSB Steganography

This algorithm hides the secret message in the least significant bits (LSB) of the audio file. It modifies the LSB of each byte in the audio data to encode the secret message. This method is simple and has minimal impact on audio quality but is relatively easy to detect.

- **Code File**: `algorithms/basic_lsb_steganography.py`
- **Output Audio File**: `output/basic_lsb_encoded.wav`

## Setup

To run this project, ensure you have Python installed (version 3.6 or higher).

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/audio-steganography.git
   cd audio-steganography
   ```

2. **Install required dependencies:**
   If there are any dependencies listed in a `requirements.txt` file, install them using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Directory Structure:**

   Ensure the following directory structure:

   ```
   audio-steganography/
   ├── cli/
   │   ├── config.py
   │   ├── helpers.py
   │   ├── main.py
   |   ├── gui.py                                                                                                                      
   │   ├── accuracy.py
   ├── algorithms/
   │   ├── basic_lsb_steganography.py
   ├── utils/
   │   ├── logging_util.py
   ├── input/
   │   ├── original_sample.wav
   ├── output/
   ├── README.md
   └── requirements.txt
   ```

## Running the Application

The application is run through a command-line interface (CLI).

### Start the CLI

To start the CLI, run the following command in your terminal or command prompt:

```bash
python cli/main.py
```

### Options in the CLI

Once the CLI is running, you will see a menu with the following options:

1. **Encode a Message**: Select this option to encode a secret message into an audio file.
2. **Decode a Message**: Select this option to decode a secret message from an audio file.
3. **Calculate Accuracy**: Select this option to calculate the accuracy of the decoded message compared to the original secret message.
4. **Exit**: Exit the application.

### Encoding a Message

1. Choose the "Encode a Message" option.
2. Choose the input audio file (default is `original_sample.wav` or a custom file).
3. Enter the secret message you wish to encode.
4. The encoded audio will be saved to the output directory specified in `cli/config.py`.

### Decoding a Message

1. Choose the "Decode a Message" option.
2. Choose the input encoded audio file (default or a custom file).
3. The decoded message will be displayed in the terminal.

### Calculating Accuracy

1. Choose the "Calculate Accuracy" option.
2. Enter the original secret message used for encoding.
3. Choose the input audio file and output audio file (press Enter to use standard files).
4. The accuracy of the decoded message will be calculated and displayed in the terminal.


## Contributing

Feel free to contribute to this project by adding more features or improving the existing code. Follow the standard GitHub flow for contributions:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-new-feature`).
5. Create a new Pull Request.

---

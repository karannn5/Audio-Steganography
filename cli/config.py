# Configuration constants
STANDARD_INPUT_FILE_PATH = "input/original_sample.wav"
OUTPUT_BASIC_LSB = "output/basic_lsb_encoded.wav"

# Import algorithm module
from algorithms import basic_lsb_steganography

# Dictionary to store algorithms
ALGORITHMS = {
    1: {
        "name": "Basic LSB Steganography",
        "encode": basic_lsb_steganography.encode,
        "decode": basic_lsb_steganography.decode,
        "output_file": OUTPUT_BASIC_LSB
    }
}

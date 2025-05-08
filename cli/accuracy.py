from utils.logging_util import setup_logger

logger = setup_logger(__name__)

def calculate_accuracy(original_message, algorithm, input_file_path, output_file_path):
    """
    This function calculates the accuracy of the decoded message.
    
    :param original_message: The original secret message used in encoding.
    :param algorithm: The algorithm used for encoding/decoding (to use the decode method).
    :param input_file_path: The path to the input file (to read the audio file for decoding).
    :param output_file_path: The path to the output file (the encoded/decoded audio file).
    """
    # Decode the message from the output file using the selected algorithm
    decoded_message = algorithm['decode'](output_file_path)
    
    # Compare the decoded message with the original message
    if decoded_message == original_message:
        logger.info("The decoded message matches the original message!")
        print("The decoded message matches the original message!")
    else:
        logger.error("The decoded message does not match the original message.")
        print("The decoded message does not match the original message.")

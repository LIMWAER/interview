import argparse
import string

from convertor.convertors import Decoder
from convertor.convertors import Encoder

KEY_FILE = 'key'


def prepare_text_source(text: str):
    # reworked because of stacking quantifiers
    return text.lower().translate(str.maketrans('', '', string.punctuation))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source_text',
                        type=str,
                        help='Returns encoded or decode text')
    return parser.parse_args()


def decode(text=parse_args().source_text):
    converted_text = Decoder(KEY_FILE).convert_text(text)
    print(converted_text)
    return converted_text


def encode(text=parse_args().source_text):
    converted_text = Encoder(KEY_FILE).convert_text(prepare_text_source(text))
    print(converted_text)
    return converted_text

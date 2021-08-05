import os

from typing import Dict
from collections import OrderedDict

from convertor.abstract_base_convertor import AbstractFileConvertor
import glob


class Decoder(AbstractFileConvertor):
    @staticmethod
    def _file_to_dict(filename) -> OrderedDict[str, str]:
        d = {}
        with open(filename) as file:
            for line in file:
                key, *value = line.split(':')
                d[value[0].split(',')[0].lstrip().rstrip('\n')] = key.lower()
        return OrderedDict(sorted(d.items(),key=lambda x: len(x[0]), reverse=True))

    def convert_text(self, input_text: str) -> str:
        for original, replace in self._latter_mapper.items():
            input_text = input_text.replace(original, replace, -1)
        return input_text

    def _create_map(self, file: str, **kwargs) -> Dict[str, str]:
        assert file
        return self._file_to_dict(file)

    def convert_files(self, *, input_dir: str, input_mask: str,
                      output_dir: str, input_prefix: str,
                      output_prefix: str):
        os.makedirs(output_dir, exist_ok=True)
        for filename in glob.glob(os.path.join(input_dir, input_mask)):
            output_name = self.output_name_generator(
                filename,
                input_prefix,
                output_prefix,
                output_dir,
            )
            with open(filename) as file:
                with open(output_name, 'w') as outfile:
                    converted_text = self.convert_text(file.read())
                    outfile.write(converted_text)

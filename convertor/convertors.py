from collections import OrderedDict
from convertor.abstract_base_convertor import BaseConvertor


class Decoder(BaseConvertor):
    def _use_right_dict(self, filename: str) -> OrderedDict[str, str]:
        d = super(Decoder, self).file_to_dict(filename)
        return d


class Encoder(BaseConvertor):
    def _use_right_dict(self, filename: str) -> OrderedDict[str, str]:
        d = super(Encoder, self).file_to_dict(filename)
        return OrderedDict((d[i], i) for i in d)

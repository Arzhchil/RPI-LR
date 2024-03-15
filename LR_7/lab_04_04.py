class Encoder:
    def encode(self):
        raise NotImplementedError("Encode method not implemented.")

    def decode(self):
        raise NotImplementedError("Decode method not implemented.")

class HuffmanEncoder(Encoder):
    def __init__(self):
        self.compressionCoef = 0.0

    def encode(self, input_string):
        encoded_string = ''.join(format(ord(i), '08b') for i in input_string)
        self.__setCompressionCoef(input_string, encoded_string)
        return encoded_string

    def decode(self, input_string):
        bits = [input_string[i:i+8] for i in range(0, len(input_string), 8)]
        decoded_string = ''.join(chr(int(b, 2)) for b in bits)
        return decoded_string

    def __setCompressionCoef(self, input_string, encoded_string):
        if len(input_string) > 0:
            self.compressionCoef = len(encoded_string) / (len(input_string) * 8)
    
    def getCompressionCoef(self):
        return self.compressionCoef

class LZEncoder(Encoder):
    def __init__(self):
        self.compressionCoef = 0.0

    def encode(self, input_string):
        encoded_string = input_string.replace(" ", "")
        self.__setCompressionCoef(input_string, encoded_string)
        return encoded_string

    def decode(self, input_string):
        return input_string

    def __setCompressionCoef(self, input_string, encoded_string):
        if len(input_string) > 0:
            self.compressionCoef = len(encoded_string) / (len(input_string) * 8)
    
    def getCompressionCoef(self):
        return self.compressionCoef

# Тестирование кода
test_string = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991"

huffman_encoder = HuffmanEncoder()
lz_encoder = LZEncoder()

encoded_huffman = huffman_encoder.encode(test_string)
decoded_huffman = huffman_encoder.decode(encoded_huffman)

encoded_lz = lz_encoder.encode(test_string)
decoded_lz = lz_encoder.decode(encoded_lz)

print("Хаффман шифровка:", encoded_huffman)
print("Хаффман дешифровка:", decoded_huffman)
print("Хаффман коэффициент сжатия:", huffman_encoder.getCompressionCoef())

print("\nЛемпеля-Зива шифровка:", encoded_lz)
print("Лемпеля-Зива дешифровка:", decoded_lz)
print("Лемпеля-Зива коэффициент сжатия:", lz_encoder.getCompressionCoef())

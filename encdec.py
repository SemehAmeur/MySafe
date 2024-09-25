from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class EncryptDecrypt:
    def __init__(self, password):
        self.salt = b'\x1f\x81\x02yu\x9cHn\xa4+j\x96P\x1bKQ/\xc9\x97F\xadK\xc9\x94\xafi\\j\x86\xa0_\xbe'
        self.key = PBKDF2(password, self.salt, dkLen=32)

    def encrypt(self, data_to_encode):
        data_to_crypt = data_to_encode.encode('UTF-8')
        cipher = AES.new(self.key, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(data_to_crypt, AES.block_size))
        data_array = [str(cipher.iv), str(ciphered_data)]
        data_array_string = str(data_array)
        return data_array_string

    def decrypt(self, data_array_string):
        data_array = eval(data_array_string)
        iv_string = data_array[0]
        iv = eval(iv_string)
        data_to_decrypt_string = data_array[1]
        data_to_decrypt = eval(data_to_decrypt_string)
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        decrypted_data = unpad(cipher.decrypt(data_to_decrypt), AES.block_size)
        data_to_preview = decrypted_data.decode('UTF_8')
        return data_to_preview


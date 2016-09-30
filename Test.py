if math.gcd(Cipher.getModulo(self), key1) == 1:
    for key2 in range(2, 16):
        c3 = Affine()
        translated = c3.decode(self.plain_text, (key1, key2))
        equal = self.check_hacking(translated)
        if equal > most_equals:
            most_equals = equal
            self.decoded_text = translated
            self.key = key1, key2
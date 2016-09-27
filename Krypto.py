import KryptoHjelpekode
import random


# Ferdig implimentert
class Cipher:
    modulo = 95
    dictionary = {0: ' ', 1: '!', 2: '"', 3: '#', 4: '$', 5: '%', 6: '&', 7: "'", 8: '(', 9: ')',
                  10: '*', 11: '+', 12: ',', 13: '-', 14: '.', 15: '/', 16: '0', 17: '1', 18: '2',
                  19: '3', 20: '4', 21: '5', 22: '6', 23: '7', 24: '8', 25: '9', 26: ':', 27: ';',
                  28: '<', 29: '=', 30: '>', 31: '?', 32: '@', 33: 'A', 34: 'B', 35: 'C', 36: 'D',
                  37: 'E', 38: 'F', 39: 'G', 40: 'H', 41: 'I', 42: 'J', 43: 'K', 44: 'L', 45: 'M',
                  46: 'N', 47: 'O', 48: 'P', 49: 'Q', 50: 'R', 51: 'S', 52: 'T', 53: 'U', 54: 'V',
                  55: 'W', 56: 'X', 57: 'Y', 58: 'Z', 59: '[', 60: '\\', 61: ']', 62: '^', 63: '_',
                  64: '`', 65: 'a', 66: 'b', 67: 'c', 68: 'd', 69: 'e', 70: 'f', 71: 'g', 72: 'h',
                  73: 'i', 74: 'j', 75: 'k', 76: 'l', 77: 'm', 78: 'n', 79: 'o', 80: 'p', 81: 'q',
                  82: 'r', 83: 's', 84: 't', 85: 'u', 86: 'v', 87: 'w', 88: 'x', 89: 'y', 90: 'z',
                  91: '{', 92: '|', 93: '}', 94: '~'}
    # Tar inn en tekst som skal krypteres og dekrypteres
    def __init__(self, ):
        raise NotImplementedError

    def encode(self, text, key):
        raise NotImplementedError

    def decode(self, text, key):
        raise NotImplementedError

    def encode_with_multi_key(self, text, first_key, second_key):
        raise NotImplementedError

    def decode_with_multi_key(self, text, first_key, second_key):
        raise NotImplementedError

    def generate_keys(self):
        raise NotImplementedError

    def getModulo(self):
        return 95

    def __str__(self):
        return "Skal kryptere teksten %s" %self.text

# Ferdig implimentert
class Person:

    def __init__(self):
        raise NotImplementedError

    def set_key(self):
        raise NotImplementedError

    def get_key(self):
        raise NotImplementedError

    # Tar inn en subklasse av chiper
    def operate_cipher(self, cipher):
        raise NotImplementedError

# Ferdig implimentert
class Sender(Person):

    # Initialiserer sender klassen, kaller på person super klasse og legger inn
    # teksten som skal sendes.
    def __init__(self, plain_text):
        super(Person, self).__init__()
        self.plain_text = plain_text
        self.coded_message = ""

    # Velger hvilken krypteringsalgoritme som skal brukes
    def operate_cipher(self, cipher):
        self.cipher = cipher

    # Setter nøkkelen
    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    # Krypterer meldingen
    def encode_message(self, text, key):
        self.coded_message = self.cipher.encode(text, key)
        return self.coded_message

    def get_text(self):
        return self.plain_text

# Ferdig implimentert
class Receiver(Person):
    def __init__(self):
        super(Person, self).__init__()
        self.decoded_text = ""

    #Velger hvilken krypterinsalgoritme som skal brukes
    def operate_cipher(self, cipher):
        self.c1 = cipher

    # Setter nøkkelen
    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    # Dekoder teksten
    def decode_message(self, text, key):
        self.decoded_text = self.c1.decode(text, key)
        return self.decoded_text

# IKKE ferdig implimentert
#class Hacker(Person):


# Ferdig implimentert
class Caesar(Cipher):
    def __init__(self):
        self.cipher_name = "Caesar"
        self.decoded_text = ""

    # Krypterer meldingen
    def encode(self, text, key):
        self.plainText = text
        self.cipher = ""

        for i in self.plainText:
            c = (ord(i) + key - 32) % Cipher.getModulo(self)
            self.cipher += Cipher.dictionary[c]
        return self.cipher

    # Dekoder meldingen
    def decode(self, text, key):
        self.encrypted_text = text

        # Gar gjennom teksten, bokstav for bokstav og finner tilbake til den riktige boktaven
        for i in self.encrypted_text:
            c = (ord(i) - key - 32) % Cipher.getModulo(self)
            self.decoded_text += Cipher.dictionary[c]

        return self.decoded_text

    # Generer en random nøkkel fra 1 til 10
    def generate_keys(self):
        self.key = random.randint(1,Cipher.getModulo(self))
        return self.key

# Ferdig implimentert
class Multiplicative(Cipher):
    def __init__(self):
        self.cipher_name = "Multiplicative"
        self.decoded_text = ""

    # Krypterer meldingen
    def encode(self, text, key):
        self.plain_text = text
        self.cipher = ""

        for i in self.plain_text:
            c = (ord(i) * key - 32) % Cipher.getModulo(self)
            self.cipher += Cipher.dictionary[c]
        return self.cipher

    # Dekoder meldingen
    def decode(self, text, key):
        self.decoded_text = ""

        # Går gjennom teksten, bokstav for bokstav for og finner tilbake til den riktige bokstaven
        for i in text:
            c = ((ord(i) * key) - 32) % Cipher.getModulo(self)
            self.decoded_text += Cipher.dictionary[c]

        return self.decoded_text

    # Generer en nøkkel
    # Ikke ferdig implementert
    def generate_keys(self):
        self.key = random.randint(1, 95)

        while True:
            if not KryptoHjelpekode.modular_inverse(self.key, Cipher.getModulo(self)):
                print("Lager ny nøkkkel... \n")
                self.key = random.randint(1,999)
            else:
                return self.key

# Ferdig implimentert
class Affine(Cipher):
    def __init__(self):
        self.cipher_name = "Affine"
        self.decoded_text = ""
        self.coded_text = ""

    # Krypterer meldingen
    def encode_with_multi_key(self, text, first_key, second_key):
        self.plain_text = text

        for i in self.plain_text:
            c = ((ord(i) * first_key + second_key) - 32) % Cipher.getModulo(self)
            self.coded_text += Cipher.dictionary[c]
        return self.coded_text

    # Dekrypterer meldingen
    def decode_with_multi_key(self, text, first_key, second_key):
        for i in text:
            c = (((ord(i) - second_key) * first_key) - 32) % Cipher.getModulo(self)
            self.decoded_text += Cipher.dictionary[c]
        return self.decoded_text

    def generate_keys(self):
        self.first_key = random.randint(0,95)
        self.second_key = random.randint(0,95)

        while True:
            if not KryptoHjelpekode.modular_inverse(self.first_key, Cipher.getModulo(self)):
                print("Lager ny nøkkkel... \n")
                self.first_key = random.randint(1, 999)
            else:
                return self.first_key, self.second_key




# IKKE ferdig implimentert
#class Unbreakable(Cipher):


# IKKE ferdig implimentert
#class RSA(Cipher):



# Kjører de forskjellige cipher algoritmene 
def runCaesar():
    # Initialiserer en sender
    s1 = Sender("abcdefghijklmnopqrstuvwxyz - ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Velger hvilken krypterinsalgoritme som skal brukes senderen
    c1 = Caesar()
    s1.operate_cipher(c1)

    # Generer en nøkkel
    key = c1.generate_keys()

    # Gir nøkkelen til sender
    s1.set_key(key)

    # Krypterer teksten
    kode = s1.encode_message(s1.get_text(), s1.get_key())

    # Initialiserer en mottaker
    r1 = Receiver()

    # Velger krypteringsalgoritme som skal brukes hos mottakeren
    r1.operate_cipher(c1)

    # Gir nøkkelen til mottaker
    r1.set_key(key)

    # Dekrypterer teksten og printer den ut
    decoded_text = r1.decode_message(kode, r1.get_key())

    print()
    print(c1.cipher_name)
    print("Den orginale teksten : " + s1.get_text())
    print("Kryptert tekst       : " + kode)
    print("Nøkkelen             : %s"  %r1.get_key())
    print("Dekryptert tekst     : " + decoded_text + "\n")

    return (decoded_text)

def runMultiplicative():
    # Initialiserer en sender
    s1 = Sender("abcdefghijklmnopqrstuvwxyz - ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Velger hvilken krypterinsalgoritme som skal brukes senderen
    c1 = Multiplicative()
    # s1.operate_cipher(c1)
    s1.operate_cipher(c1)

    # Generer en nøkkel
    # key = c1.generate_keys()
    key = c1.generate_keys()

    # Gir nøkkelen til sender
    s1.set_key(key)

    # Krypterer teksten
    kode = s1.encode_message(s1.get_text(), s1.get_key())

    # Initialiserer en mottaker
    r1 = Receiver()

    # Velger krypteringsalgoritme som skal brukes hos mottakeren
    r1.operate_cipher(c1)

    # Gir nøkkelen til mottaker
    r1.set_key(KryptoHjelpekode.modular_inverse(key, c1.getModulo()))

    # Dekrypterer teksten og printer den ut
    decoded_text = r1.decode_message(kode, r1.get_key())

    print()
    print(c1.cipher_name)
    print("Den orginale teksten : " + s1.get_text())
    print("Kryptert tekst       : " + kode)
    print("Nøkkelen for sender  : " + str(s1.get_key()))
    print("Nøkkelen for mottaker: " + str(r1.get_key()))
    print("Dekryptert tekst     : " + decoded_text + "\n")

    return decoded_text

def runAffine():
    # Initialiserer en sender
    s1 = Sender("abcdefghijklmnopqrstuvwxyz - ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Velger hvilken krypterinsalgoritme som skal brukes senderen
    c1 = Affine()
    # s1.operate_cipher(c1)
    s1.operate_cipher(c1)

    # Generer en nøkkel
    key = c1.generate_keys()

    print(key)

    # Gir nøkkelen til sender
    s1.set_key(key)

    # Krypterer teksten
    kode = c1.encode_with_multi_key(s1.get_text(),s1.get_key()[0],s1.get_key()[1])

    # Initialiserer en mottaker
    r1 = Receiver()

    # Velger krypteringsalgoritme som skal brukes hos mottakeren
    r1.operate_cipher(c1)

    # Gir nøkkelen til mottaker
    new_key = KryptoHjelpekode.modular_inverse(int(key[0]), c1.getModulo())
    key = [new_key,s1.get_key()[1]]
    r1.set_key(key)

    # Dekrypterer teksten og printer den ut
    decoded_text = c1.decode_with_multi_key(kode, r1.get_key()[0], r1.get_key()[1])

    print()
    print(c1.cipher_name)
    print("Den orginale teksten : " + s1.get_text())
    print("Kryptert tekst       : " + kode)
    print("Nøkkelen for sender  : " + str(s1.get_key()))
    print("Nøkkelen for mottaker: " + str(r1.get_key()))
    print("Dekryptert tekst     : " + decoded_text  + "\n")

    return decoded_text

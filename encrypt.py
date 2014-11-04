from hashlib import *
from argparse import ArgumentError, Action
import random
import string

class PwCrypt():
    """
    PwCrypt provide two tools for the password security.

    You can use them to encrypt a password and validate someone's input with it
        - hash_password(text_password, salt=None): 
                  Take care of the password to make it safe.
                  Make it cannot be reused by another one even the DBA.
        - validate_password(text_password, stored_password):
                  Is the password correct?
                  Is it exactly same with the one recorded in my place.
    
    :param algorithm: Hash Algorithm whose options are sha512, sha384, sha256, 
                      sha224, sha1, md5
    """

    def __init__(self, algorithm='sha512'):
        # Here using named constructor func rather than new func because of computing speed
        algorithm = algorithm.lower()
        if algorithm == 'sha512':
            self.algorithm = sha512
            self.pw_length = 128
        elif algorithm == 'sha384':
            self.algorithm = sha384
            self.pw_length = 96
        elif algorithm == 'sha256':
            self.algorithm = sha256
            self.pw_length = 64
        elif algorithm == 'sha224':
            self.algorithm = sha224
            self.pw_length = 56
        elif algorithm == 'sha1':
            self.algorithm = sha1
            self.pw_length = 40
        elif algorithm == 'md5':
            self.algorithm = md5
            self.pw_length = 32
        else:
            raise ArgumentError(Action(option_strings=['algorithm - %s' % algorithm], 
                                       dest='hashlib\'s algorithm'),
                                'Wrong hash algorithm which you passed')

    def hash_password(self, text_password, salt=None):
        """
        Encrypt your text-password to a hashed-password
        
        :param text_password: The original text-password waitting to be encrypt
        :param salt: Noise for more security. If you don't know what's this, ignore it.
        """
        if not salt:
            salt = ''.join([random.choice(string.letters+string.digits) for i in range(12)])
        hashed_password = self.algorithm(text_password + salt).hexdigest()
        return '%s|%s' % (hashed_password, salt)

    def _check_pw_type(self, stored_password):
        pw_terms = stored_password.split('|')
        return len(pw_terms) == 2 and len(pw_terms[0]) == self.pw_length

    def validate_password(self, text_password, stored_password):
        """
        Validate a text-password(maybe someone's input) with a 
        hashed_password(holding on your hands)
        
        :param text_password: The password waitting to be verified
        :param stored_password: The password already on your hands
        """
        if self._check_pw_type(stored_password):
            salt = stored_password.split('|')[1]
            hashed_password = self.hash_password(text_password, salt)
        else:
            raise ArgumentError(Action(option_strings=['stored_password - %s' % stored_password],
                                       dest='hashlib\'s algorithm'),
                                'Invalid coding type')

        return hashed_password == stored_password

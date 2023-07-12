"""
Module containing test cases for the 'generate_invite' function.

This module provides test cases to verify the behavior of the 'generate_invite'
function in generating unique invites.

Test cases:
- MyTestGenerateInvite: Test case for generating unique invites.
"""

import unittest
from intel.source.functions import *


class MyTestGenerateInvite(unittest.TestCase):
    """
    Test case for generating unique invites using the 'generate_invite' function.

    This test case verifies that the 'generate_invite' function generates unique
    invites. It also checks that the generated invites do not contain whitespace
    characters and have a length equal to INVITE_LENGTH.

    Methods:
        test_generate_invite: Test if function generates unique invites.
    """
    def test_generate_invite(self):
        """
        Checks if the function generate unique invites.

        Expected behavior:
            The function should generate unique invites.
            The generated invites should not contain whitespace characters.
            The length of each invite should be equal to INVITE_LENGTH.
        """
        invite = generate_invite()
        for token in invite:
            self.assertFalse(token.isspace(), 'Invite should not be a whitespace character')
            self.assertEqual(INVITE_LENGTH, len(token), f'The length of the invite must be = {INVITE_LENGTH}')
        self.assertEqual(len(invite), len(set(invite)), 'Invites are not unique')


if __name__ == '__main__':
    unittest.main()

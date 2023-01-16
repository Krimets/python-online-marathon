import unittest
import unittest.mock


def file_parser(file, string, new_string=None):
    if new_string:
        with open(file, 'r') as f:
            old_data = f.read()
        new_data = old_data.replace(string, new_string)
        with open(file, 'w') as f:
            f.write(new_data)
    else:
        f = open(file)
        data = f.read()
        occurrences = data.count(string)
        return f'Found {occurrences} strings'


class ParserTest(unittest.TestCase):
    @unittest.mock.patch('__main__.file_parser')
    def test_file_parser(self, mocked_file_parser):
        self.assertFalse(mocked_file_parser.called)

    @unittest.mock.patch('__main__.file_parser')
    def test_file(self, mocked_file_parser):
        file_parser('parser.txt', 'test')
        self.assertTrue(mocked_file_parser.called)

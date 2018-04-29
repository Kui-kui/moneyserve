"""
Define the commands to run import
"""
from flask.ext.script import Command, Option
import logging


class ImportDataCommand(Command):
    """Command to import a CSV file."""

    option_list = (
        Option(
            '--file',
            '-f',
            dest='file',
            required=True,
            help='The full path of the file to be imported.'),
        Option(
            '--model',
            '-model',
            dest='model',
            required=True,
            help='The model about to be imported.'),
    )

    def run(self, file):
        """Import the given CSV file."""
        print('Yé')

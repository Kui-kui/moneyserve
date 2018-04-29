"""
Define the commands to run import
"""
from flask.ext.script import Command, Option
from sqlalchemy.orm import sessionmaker

from service import Importer


class ImportDataCommand(Command):
    """Command to import a CSV file."""

    option_list = (
        Option(
            '--file',
            '-f',
            dest='file',
            required=True,
            help='The full path of the file to be imported.'),
    )

    def run(self, file):
        """Import the given CSV file."""
        Session = sessionmaker()
        session = Session()

        importer = Importer(session, file)
        importer.run(file)

"""
Define a base model for import tasks
"""
import csv
import os

import model
from model import Supermarket


class Importer():
    """Define a process to run import tasks."""

    def __init__(self, session, file):
        self.model_class = self.get_model_class(file)
        self.session = session

    @staticmethod
    def get_model_class(file):
        """Get model from file name."""
        file_name = os.path.basename(file)[:-4]
        class_name = ''.join(map(str.capitalize, file_name.split('_')))

        return getattr(model, class_name)

    def run(self, file):
        """Entry point of the import."""
        with open(file, encoding='utf-8-sig') as csvfile:
            self.import_file(csvfile)

    def import_file(self, csvfile):
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            print(row)

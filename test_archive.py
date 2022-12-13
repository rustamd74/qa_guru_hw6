import csv
from zipfile import ZipFile, ZIP_DEFLATED
import os
import pytest
import xlrd
from PyPDF2 import PdfReader

current_dir = os.path.dirname(os.path.abspath(__file__))
path_resources = os.path.join(current_dir, 'resources')
path_myzip = os.path.join(path_resources, 'archive.zip')


# Архив

def test_create_archive(myzip=None):
    with ZipFile(os.path.join(path_resources, 'archive.zip'), 'w', compression=ZIP_DEFLATED) as myzip:
        myzip.write(os.path.join(path_resources, 'names.csv'))
        myzip.write(os.path.join(path_resources, 'docs-pytest-org-en-latest.pdf'))
        myzip.write(os.path.join(path_resources, 'accounts.xlsx'))


def test_csv():
    with ZipFile(path_myzip) as zipfile:
        csvfile = zipfile.read('names.csv')
        with open(csvfile) as csvfile:
            csvfile = csv.reader(csvfile)

        assert csvfile.contains('Anna')

# def test_pdf():
#   pass

# def test_xls():

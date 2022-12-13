import csv
from zipfile import ZipFile, ZIP_DEFLATED
import os
import pytest
import xlrd
from PyPDF2 import PdfReader
from os.path import basename

current_dir = os.path.dirname(os.path.abspath(__file__))
path_resources = os.path.join(current_dir, 'resources')
path_myzip = os.path.join(path_resources, 'archive.zip')


# Архив

def test_create_archive():
    with ZipFile(os.path.join(path_resources, 'archive.zip'), 'w', compression=ZIP_DEFLATED) as myzip:
        myzip.write(os.path.join(path_resources, 'names.csv'), 'names.csv')
        myzip.write(os.path.join(path_resources, 'docs-pytest-org-en-latest.pdf'), 'docs-pytest-org-en-latest.pdf')
        myzip.write(os.path.join(path_resources, 'accounts.xlsx'), 'accounts.xlsx')


def test_csv():
    with ZipFile(path_myzip, 'r') as zip_file:
            csvfile = str(zip_file.read('names.csv'))
            with open(csvfile) as csvfile:
                csvfile = csv.reader(csvfile)
                assert csvfile.__contains__("Anna")

# def test_pdf():
#  pass

# def test_xls():

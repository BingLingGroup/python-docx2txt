import glob
from distutils.core import setup

setup(
  name='docx2txt',
  packages=['docx2txt'],
  entry_points={
    'console_scripts': [
      'docx2txt = docx2txt:main',
    ]
  },
  version='0.8',
  description='A pure python-based utility to extract text and images '
              'from docx files.',
  author='Ankush Shah',
  author_email='ankush.shah.nitk@gmail.com',
  url='https://github.com/ankushshah89/python-docx2txt',
  download_url='https://github.com/ankushshah89/python-docx2txt/tarball/0.8',
  keywords=['python', 'docx', 'text', 'images', 'extract'],
)

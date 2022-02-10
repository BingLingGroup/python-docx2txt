from docx2txt import utils
import os
import sys
import shlex
import subprocess
import chardet

VERSION = '0.8'


def main():
    args = utils.process_args()
    # text = utils.process(args.docx, args.img_dir)
    output_name = os.path.splitext(args.docx)[0] + '.txt'
    output_dir = os.path.dirname(output_name)

    if output_dir:
        libre_office_command = \
            "soffice \"{docx_name}\" --headless --convert-to \"txt:Text (encoded):UTF8\" " \
            "--outdir {output_dir} *.txt".format(docx_name=args.docx,
                                                 output_dir=output_dir)
    else:
        libre_office_command = \
            "soffice \"{docx_name}\" --headless --convert-to " \
            "\"txt:Text (encoded):UTF8\" *.txt".format(docx_name=args.docx)
    print(libre_office_command)
    if sys.platform.startswith('win'):
        libre_office_command = libre_office_command
    else:
        libre_office_command = shlex.split(libre_office_command)

    p = subprocess.Popen(libre_office_command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate()

    if out:
        print(out.decode(chardet.detect(out)['encoding']))
    if err:
        print(err.decode(chardet.detect(err)['encoding']))

    with open(output_name, mode='rb') as input_file:
        content = input_file.read()
        test_str = content[:50]
        text = content.decode(encoding=chardet.detect(test_str)['encoding'])
    text = text.replace('    [', '[')
    with open(output_name, 'wb') as output_file:
        output_file.write(text.encode('utf-8'))

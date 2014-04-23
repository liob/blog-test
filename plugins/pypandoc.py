# -*- coding: utf-8 -*-
from __future__ import with_statement

__author__ = 'Juho Vepsäläinen'
__version__ = '0.8.1'
__license__ = 'MIT'
__all__ = ['convert', 'get_pandoc_formats']

import subprocess
import os



def convert(source, to, format=None, extra_args=()):
    '''Converts given `source` from `format` `to` another. `source` may be either a file path or a string to be converted. It's possible to pass `extra_args` if needed. In case `format` is not provided, it will try to invert the format based on given `source`.

    Raises OSError if pandoc is not found! Make sure it has been installed and is available at path.
    '''
    
    print "pypantest 1"
    
    return _convert(_read_file, _process_file, source, to, format, extra_args)

def _convert(reader, processor, source, to, format=None, extra_args=()):
    print "pypantest 2"
    source, format = reader(source, format)

    formats = {
        'dbk': 'docbook',
        'md': 'markdown',
        'rest': 'rst',
        'tex': 'latex',
    }

    format = formats.get(format, format)
    to = formats.get(to, to)

    if not format:
        raise RuntimeError('Missing format!')

    from_formats, to_formats = get_pandoc_formats()

    if format not in from_formats:
        raise RuntimeError('Invalid input format! Expected one of these: ' + ', '.join(from_formats))

    if to not in to_formats:
        raise RuntimeError('Invalid to format! Expected one of these: ' + ', '.join(to_formats))
        
    print "pypantest 3"

    return processor(source, to, format, extra_args)

def _read_file(source, format):
    if os.path.exists(source):
        with open(source) as f:
            format = format or os.path.splitext(source)[1].strip('.')
            source = f.read()

    return source, format

def _process_file(source, to, format, extra_args):
    args = ['pandoc', '--from=' + format, '--to=' + to]
    args.extend(extra_args)
    
    print "pypantest 4"
    
    env = os.environ
    env['PYTHONIOENCODING'] = 'utf-8'
    p = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
            env=env)
    
    print "pypantest 5"

    result = p.communicate(source.encode('utf-8'))[0].decode('utf-8')
    
    print "pypantest 6"
    
    return result

def get_pandoc_formats():
    '''
    Dynamic preprocessor for Pandoc formats.
    Return 2 lists. "from_formats" and "to_formats".
    ''' 
    try:
        p = subprocess.Popen(
                ['pandoc', '-h'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE)
    except OSError:
        raise OSError("You probably do not have pandoc installed.")
    
    help_text = p.communicate()[0].decode().splitlines(False)
    txt = ' '.join(help_text[1:help_text.index('Options:')])

    aux = txt.split('Output formats: ')
    in_ = aux[0].split('Input formats: ')[1].split(',')
    out = aux[1].split(',')

    return [f.strip() for f in in_], [f.strip() for f in out]

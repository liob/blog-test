import os
from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open
import pypandoc

class NewReader(BaseReader):
    enabled = True
    file_extensions = ['md', 'markdown', 'mkd', 'mdown']


    def read(self, filename):
        with pelican_open(filename) as text:
            print "-------------------"
            print "     mdtest 1"
            metadata_items = []
            in_content = False
            MD = ''
            for line in text.splitlines():
                splitted = line.split(':', 1)
                if len(splitted) == 2 and not in_content:
                    metadata_items.append(splitted)
                else:
                    in_content = True
                    MD += line + '\n'
            
            print "     mdtest 2"
            metadata = {}
            for item in metadata_items:
                name, value = item
                name = name.lower()
                value = value.strip()
                meta = self.process_metadata(name, value)
                metadata[name] = meta
        
        print "     mdtest 3"
        os.chdir(self.settings['PATH']) # change the cwd to the content dir
        if 'PANDOC_ARGS' in self.settings:
            print "     mdtest 4"
            output = pypandoc.convert(MD, 'html5', format='md', extra_args=self.settings['PANDOC_ARGS'])
            print "     mdtest 5"
        else:
            print "     mdtest 6"
            output = pypandoc.convert(MD, 'html5', format='md')
            print "     mdtest 7"
        
        print "     mdtest 8"
        return output, metadata

def add_reader(readers):
    readers.reader_classes['md'] = NewReader

def register():
    signals.readers_init.connect(add_reader)

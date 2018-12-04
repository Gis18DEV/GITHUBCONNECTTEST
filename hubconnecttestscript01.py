#----------------------------------------------------------------------------
#demo script for git hub project test
#s sunderland, 4/12/18
#
#

import unicodedata,string,time, traceback,os,sys


validFilenameChars = "-_.() %s%s" % (string.ascii_letters, string.digits)

#######################################################################
def removeDisallowedFilenameChars(filename):
    cleanedFilename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore')
    cleanstr =  ''.join(c for c in cleanedFilename if c in validFilenameChars)
    cleanstr = cleanstr.replace(" ","_")
    return cleanstr
##########################################################################################
######################################################################################################################
def iter_baskets_contiguous(items, maxbaskets=3, item_count=None):
    '''
    generates balanced baskets from iterable, contiguous contents
    provide item_count if providing a iterator that doesn't support len()
    '''
    item_count = item_count or len(items)
    baskets = min(item_count, maxbaskets)
    items = iter(items)
    floor = item_count // baskets
    ceiling = floor + 1
    stepdown = item_count % baskets
    for x_i in xrange(baskets):
        length = ceiling if x_i < stepdown else floor
        yield [items.next() for _ in xrange(length)]
#######################################################################################################################
#!/usr/bin/env python
if __name__ == '__main__':
    # explicitly append the ./src directory to the current path.
    # PyCharm does this implicitly but it is better to have it explicit
    # this makes the tool work the same in tests and in CLI
    import sys
    import inspect
    from os.path import dirname, abspath, join
    #when in CLI use inspect to locate the source directory
    src_dir = join(dirname(abspath(inspect.getfile(inspect.currentframe()))), 'src')
    sys.path.append(src_dir)

__author__ = 'saflores'

from FileComparator import FileComparator

###############################################################################
print('Test...')
t = './tests/00_install/test_214.csv'
r = './tests/00_install/ref_214.csv'

fc = FileComparator(t, r)
res = fc.compare()
print()
if res:
    print('### Files do not have significant differences: PASS')
else:
    print('### Files differ significantly: FAIL')

sys.exit(0)
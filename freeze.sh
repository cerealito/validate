#!/bin/sh
echo 'freezing...'
freeze_cmd='cxfreeze gcompare.py --base-name=Win32GUI --target-dir dist --include-path=src --include-modules=matplotlib.backends.backend_tkagg'
$freeze_cmd
echo
if [[ $? -eq 0 ]]; then
	echo 'OK done';
else
	echo 'Oops! something went wrong';
fi

#!/bin/sh
echo 'freezing...'
freeze_cmd='cxfreeze validate.py -c --base-name=Win32GUI --target-dir dist --include-path=src'
$freeze_cmd
echo
if [[ $? -eq 0 ]]; then
	echo 'OK done';
else
	echo 'Oops! something went wrong';
fi

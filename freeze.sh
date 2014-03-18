#!/bin/sh
echo 'freezing...'
freeze_cmd='cxfreeze validate.py -c --base-name=Win32GUI --target-dir dist --include-path=src --icon=ui/icons/account-logged-in.ico'
$freeze_cmd
echo

echo erasing un-needed files:
rm -v dist/_bz2.pyd
rm -v dist/_ctypes.pyd
rm -v dist/_decimal.pyd
rm -v dist/_hashlib.pyd
rm -v dist/_lzma.pyd
rm -v dist/_multiprocessing.pyd
rm -v dist/_ssl.pyd
rm -v dist/icudt49.dll
rm -v dist/icuin49.dll
rm -v dist/icuuc49.dll
rm -v dist/libGLESv2.dll
rm -v dist/matplotlib.ttconv.pyd
rm -v dist/numpy.core._dotblas.pyd
rm -v dist/platforms/qminimal.dll
rm -v dist/platforms/qoffscreen.dll
rm -v dist/pyexpat.pyd
rm -v dist/select.pyd

rm -vRf dist/imageformats/
rm -vRf dist/mpl-data/fonts/
rm -vRf dist/mpl-data/images/
rm -vRf dist/mpl-data/sample_data/

if [[ $? -eq 0 ]]; then
	echo 'OK done';
else
	echo 'Oops! something went wrong';
fi

read
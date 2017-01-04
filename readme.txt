
1. For enabling Excel integration download Pywin32 wheel from e.g. http://www.lfd.uci.edu/~gohlke/pythonlibs/
accordingly to your OS and Python versions and then install it.

Examples for Windows 32-bit and 64-bit versions with Python 3.6:

- for Win 64-bit:
pip install pywin32-220.1-cp36-cp36m-win_amd64.whl

- for Win 32-bit:
pip install pywin32-220.1-cp36-cp36m-win32.whl

Then go to your Python directory and run the command with administrative privileges
python.exe Scripts\pywin32_postinstall.py -install


2. For enabling mathematical algorithms be sure to have installed the following.

From http://landinghub.visualstudio.com/visual-cpp-build-tools
- Visual C++ Build Tools

From http://www.lfd.uci.edu/~gohlke/pythonlibs
- numpy+mkl
- scipy
- scikit-learn

Troubleshooting:
In case scikit-learn crashes with np_version error see
http://stackoverflow.com/questions/40824903/unorderable-types-error-when-importing-sklearn

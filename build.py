import os

# python3 -m pip install --user --upgrade setuptools wheel

if __name__ == '__main__':
    os.system('rmdir /s /q "build"2>nul')
    os.system('rmdir /s /q "dist"2>nul')
    os.system('rmdir /s /q "python_zhmh.egg-info"2>nul')
    os.system('python setup.py sdist bdist_wheel')
    # os.system("twine upload dist/*")

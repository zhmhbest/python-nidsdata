import setuptools

with open('README.md', 'r', encoding='utf-8') as fp:
    long_description = fp.read()

setuptools.setup(
    python_requires='>=3',
    install_requires=['pandas>=0.24.2', 'numpy>=1.14.0', 'python-home>=0.0.8'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    author="zhmh",
    author_email="zhmhbest@gmail.com",
    name="nidsdata",
    version='0.0.1',
    description="Python Common Command",
    keywords="nids data",
    license="MIT",  # https://choosealicense.com/
    url="https://github.com/zhmhbest/python-nidsdata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

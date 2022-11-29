"""
*** sbvirtualdisplay ***
A modified version of pyvirtualdisplay for optimized SeleniumBase performance.
(Python 2.7+ and Python 3.6+)
"""

from setuptools import setup
import os
import sys


this_dir = os.path.abspath(os.path.dirname(__file__))
long_description = None
total_description = None
try:
    with open(os.path.join(this_dir, "README.md"), "rb") as f:
        total_description = f.read().decode("utf-8")
    description_lines = total_description.split("\n")
    long_description_lines = []
    for line in description_lines:
        if not line.startswith("<meta ") and not line.startswith("<link "):
            long_description_lines.append(line)
    long_description = "\n".join(long_description_lines)
except IOError:
    long_description = "A customized pyvirtualdisplay for SeleniumBase."
about = {}
# Get the package version from the sbvirtualdisplay/__version__.py file
with open(
    os.path.join(this_dir, "sbvirtualdisplay", "__version__.py"), "rb"
) as f:
    exec(f.read().decode("utf-8"), about)

if sys.argv[-1] == "publish":
    reply = None
    input_method = input
    if not sys.version_info[0] >= 3:
        input_method = raw_input  # noqa: F821
    confirm_text = ">>> Confirm release PUBLISH to PyPI? (yes/no): "
    reply = str(input_method(confirm_text)).lower().strip()
    if reply == "yes":
        print("\n*** Checking code health with flake8:\n")
        os.system("python -m pip install 'flake8==5.0.4'")
        flake8_status = os.system("flake8 --exclude=recordings,temp")
        if flake8_status != 0:
            print("\nWARNING! Fix flake8 issues before publishing to PyPI!\n")
            sys.exit()
        else:
            print("*** No flake8 issues detected. Continuing...")
        print("\n*** Removing existing distribution packages: ***\n")
        os.system("rm -f dist/*.egg; rm -f dist/*.tar.gz; rm -f dist/*.whl")
        os.system("rm -rf build/bdist.*; rm -rf build/lib")
        print("\n*** Installing build: *** (Required for PyPI uploads)\n")
        os.system("python -m pip install --upgrade 'build>=0.9.0'")
        print("\n*** Installing twine: *** (Required for PyPI uploads)\n")
        os.system("python -m pip install --upgrade 'twine>=4.0.1'")
        print("\n*** Installing tqdm: *** (Required for PyPI uploads)\n")
        os.system("python -m pip install --upgrade tqdm")
        print("\n*** Rebuilding distribution packages: ***\n")
        os.system("python -m build")  # Create new tar/wheel
        print("\n*** Publishing The Release to PyPI: ***\n")
        os.system("python -m twine upload dist/*")  # Requires ~/.pypirc Keys
        print("\n*** The Release was PUBLISHED SUCCESSFULLY to PyPI! :) ***\n")
    else:
        print("\n>>> The Release was NOT PUBLISHED to PyPI! <<<\n")
    sys.exit()

setup(
    name="sbvirtualdisplay",
    version=about["__version__"],
    description="A customized pyvirtualdisplay for SeleniumBase.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdmintz/sbVirtualDisplay",
    project_urls={
        "Changelog": "https://github.com/mdmintz/sbVirtualDisplay/releases",
        "Download": "https://pypi.org/project/sbvirtualdisplay/#files",
        "SeleniumBase": "https://github.com/seleniumbase/SeleniumBase",
        "PyPI": "https://pypi.org/project/sbvirtualdisplay/",
        "Source": "https://github.com/mdmintz/sbVirtualDisplay",
    },
    platforms=["Windows", "Linux", "Mac OS-X"],
    author="Michael Mintz",
    author_email="mdmintz@gmail.com",
    maintainer="Michael Mintz",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: Web Environment",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Topic :: Utilities",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",  # noqa: E501
    install_requires=[],
    extras_require={
        # pip install -e .[coverage]
        # Usage: coverage run -m pytest; coverage html; coverage report
        "coverage": [
            'coverage==5.5;python_version<"3.6"',
            'coverage==6.2;python_version>="3.6" and python_version<"3.7"',
            'coverage==6.5.0;python_version>="3.7"',
            'pytest-cov==2.12.1;python_version<"3.6"',
            'pytest-cov==4.0.0;python_version>="3.6"',
        ],
        # pip install -e .[flake8]
        # Usage: flake8
        "flake8": [
            'flake8==3.7.9;python_version<"3.6"',
            'flake8==5.0.4;python_version>="3.6"',
            'mccabe==0.6.1;python_version<"3.6"',
            'mccabe==0.7.0;python_version>="3.6"',
            'pyflakes==2.1.1;python_version<"3.6"',
            'pyflakes==2.5.0;python_version>="3.6"',
            'pycodestyle==2.5.0;python_version<"3.6"',
            'pycodestyle==2.9.1;python_version>="3.6"',
        ],
    },
    packages=[
        "sbvirtualdisplay",
    ],
    include_package_data=True,
    entry_points={},
)

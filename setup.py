from distutils.core import setup
import setuptools

setup(
    name="cc3200tool",
    version="0.1.0",
    description="A tool to upload files to TI CC3200 ",
    author="Kiril Zyapkov",
    author_email="k.zyapkov@allterco.com",
    url="http://github.com/s1ider/cc3200tool.git",
    packages=setuptools.find_packages(),
    package_data={'cc3200tool': ['dll/*.dll', 'dll/gen2/*.ptc']},
    scripts=[
                'scripts/cc3200tool',
                'scripts/cc3220tool',
            ],
    install_requires=['pyserial', 'progress'],
)

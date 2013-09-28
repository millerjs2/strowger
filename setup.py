from setuptools import setup

from strowger import __version__


REQUIRES = ["twilio >= 3.6.1", "flask >= 0.9"]

setup(
    name="strowger",
    version=__version__,
    description="Lightweight Twilio SMS application framework",
    author="Sam Kimbrel",
    author_email="samkimbrel@gmail.com",
    url="https://github.com/skimbrel/strowger",
    keywords=["strowger", "twilio", "twiml", "sms"],
    install_requires=REQUIRES,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    long_description="""\
    Strowger - Twilio SMS Application Framework
    -------------------------------------------

    DESCRIPTION
    Strowger is a simple framework for building SMS-driven applications
    on the Twilio platform using Flask.
    See https://github.com/skimbrel/strowger for more information.

    LICENSE
    Strowger is licensed under the BSD License."""
)
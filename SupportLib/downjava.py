# Create by 2z0h0m9
import os

from download import download


def setUp():
    download('http://ftp.de.debian.org/debian/pool/main/o/openjdk-17/openjdk-17-jre-headless_17~19-1_arm64.deb',
             'Java17.deb')
    os.system('sudo dpkg -i Java17.deb')

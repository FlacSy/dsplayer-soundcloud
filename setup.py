from setuptools import setup, find_packages

setup(
    name='dsplayer-soundcloud',  
    version='1.2.0',
    packages=find_packages(),
    install_requires=[
        'dsplayer',
        'yt-dlp'
    ],
    entry_points={
        'dsplayer.plugins': [
            'soundcloud = dsplayer_soundcloud.soundcloud:SoundCloudPlugin',
        ],
    },
)
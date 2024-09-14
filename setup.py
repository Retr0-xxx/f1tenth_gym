from setuptools import setup

setup(
    name='f110_gym',
    version='0.2.1',
    author='Hongrui Zheng',
    author_email='billyzheng.bz@gmail.com',
    url='https://f1tenth.org',
    packages=['f110_gym'],  # Ensure your actual package name here
    package_dir={'f110_gym': 'gym'},  # Adjust path to your package correctly
    install_requires=[
        'gym==0.19.0',
        'numpy>=1.18.0,<1.23.0',  # Broaden the version range if possible
        'Pillow>=9.0.1',
        'scipy>=1.7.3',
        'numba>=0.55.2',
        'pyyaml>=5.3.1',
        'pyglet<1.5',
        'pyopengl'
    ],
    extras_require={
        'dev': [
            'pytest>=5.4.1',
            'coverage>=5.1'
        ]
    }
)

from setuptools import setup

setup(
    name='ADT',
    version='0.1.1',
    py_modules=['ADTexceptions',
                'ADTiterator',
                'ADTtypemap',
                'arraystack',
                'dynamicarray',
                'listABC',
                'stackABC',
                'dequeueABC',
                'arrayqueue',
                'boundedarraystackint',
                'boundedstackintABC',
                'queueABC'] 
,
    install_requires=[],
)

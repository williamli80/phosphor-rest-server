from distutils.core import setup

setup(name='obmc-rest',
      version='1.0',
      scripts=['phosphor-rest'],
      data_files=[('obmc-rest', ['cert.pem'])],
      )

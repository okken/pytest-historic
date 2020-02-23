from setuptools import find_packages, setup

setup(
      name='pytest-historic',
      version="0.1.0",
      description='Custom report to display pytest historical execution records',
      long_description='Pytest Historic is custom report to display historical execution records using MySQL + Flask',
      classifiers=[
          'Framework :: Pytest',
          'Programming Language :: Python',
          'Topic :: Software Development :: Testing',
      ],
      keywords='pytest historical execution report',
      author='Shiva Prasad Adirala',
      author_email='adiralashiva8@gmail.com',
      url='https://github.com/adiralashiva8/pytest-historic',
      license='MIT',
      
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'pytest',
          'config',
          'flask',
          'flask-mysqldb'
      ],
      entry_points={
          'console_scripts': [
              'rfhistoric=pytest_historic.app:main',
          ]
      },
)
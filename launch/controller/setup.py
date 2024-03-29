from setuptools import setup

package_name = 'controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=['controller_sub'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='farhan',
    maintainer_email='huq.shoaib@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'controller_sub = controller_sub:main'
        ],
    },
)

from setuptools import setup

package_name = 'video'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'video_publisher'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robosub',
    maintainer_email='robosub@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'video_pub = video_publisher:main'
        ],
    },
)

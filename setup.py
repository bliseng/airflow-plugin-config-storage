from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='airflow-plugin-config-storage',
    version='0.1.0',
    packages=find_packages(),
    url='https://bliseng.github.io/airflow-plugin-config-storage/',
    license='LGPLv3',
    author='Drew J. Sonne',
    author_email='drew.sonne@gmail.com',
    description='Inject connections into the airflow database from configuration',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=open('requirements.txt').read().split('\n'),
    entry_points={
        'console_scripts': [
            'load-airflow-conf-env-var=airflow_plugin_config_storage.cli:run_env_var',
            'delete-all-airflow-connnections=airflow_plugin_config_storage.cli:run_delete_all_connections'
            # 'load-airflow-conf-aws-ssm=airflow_plugin_config_storage.cli:run_aws_ssm [aws]'
        ]
    },
    build_requires=['twine']
    # extras_require={
    #     'aws': ['boto3']
    # }
)

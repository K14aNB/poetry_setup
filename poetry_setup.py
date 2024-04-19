import os
import sys
from subprocess import run,CalledProcessError

def setup_virtualenv(repo_path:str):
    '''
    Takes repo_path as argument and creates a virtualenv and installs the dependencies specified in pyproject.toml

    Arguments:
    repo_path:str : Relative path of the current repo

    Returns:None
    '''
    try:
        import poetry
    except Module as e1:
        print('Poetry is not installed!!')
        print('Installing poetry')
        try:
            run(['pip','install','poetry','--quiet'],check=True)
        except CalledProcessError as e2:
            print(f'{e2.cmd} failed')
    
    os.chdir(repo_path)

    try:
        run(['poetry','config','virtualenvs.in-project','false'],check=True)
    except CalledProcessError as e3:
        print(f'{e3.cmd} failed')

    try:
        run(['poetry','install','--quiet'],check=True)
    except CalledProcessError as e4:
        print(f'{e4.cmd} failed')

    try:
        poetry_env_info_cmd=run(['poetry','env','info','--path'],capture_output=True,check=True)
        poetry_env_path=poetry_env_info_cmd.stdout.decode('utf-8').replace('\n','',1)
    except CalledProcessError as e5:
        print(f'{e5.cmd} failed')
    
    python_version='python'+poetry_env_path[-4:]

    sys.path.insert(0,os.path.join(poetry_env_path,'lib',python_version,'site-packages'))

    try:
        run(['poetry','env','use',os.path.join(poetry_env_path,'bin','python')],check=True)
    except CalledProcessError as e6:
        print(f'{e6.cmd}')







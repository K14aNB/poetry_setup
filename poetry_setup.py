import os
from subprocess import run,CalledProcessError

def setup_virtualenv():
    '''
    Creates a virtualenv and installs the dependencies specified in pyproject.toml

    Returns: none
    '''
    try:
        import poetry
    except ModuleNotFoundError as e1:
        print('Poetry is not installed!!')
        print('Installing poetry')
        try:
            run(['pip','install','poetry','--quiet'],check=True)
        except CalledProcessError as e2:
            print(f'{e2.cmd} failed')
    
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
    
    poetry_env_path=poetry_env_info_cmd.stdout.decode('utf-8').replace('\n','',1)
    python_version=os.listdir(os.path.join(poetry_env_path,'lib'))[0]
    
    try:
        run(['poetry','env','use',os.path.join(poetry_env_path,'bin','python')],check=True)
    except CalledProcessError as e6:
        print(f'{e6.cmd}')
    
    print(f'poetry_env_path={poetry_env_path}')
    print(f'python_version={python_version}')

  







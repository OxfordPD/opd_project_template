# Example OPD python CLI project template

A cookiecutter templated repo for setting up a new OPD project in an opinionated way to establish common structure and best practises.

## powershell SSH based usage
Follow the atlassian steps for setting up an ssh key to authenticate with bitbucket

https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-windows/

Once you have an ssh-key setup and loaded into an active ssh-agent you can create a temporary venv to install cookiecutter into 

```powershell
mkdir {project_name}

python -m venv cc
python -m venv {project_name_venv}

cc/scripts/activate.ps1
pip install cookiecutter

cd {project_name}
git init

cookiecutter git+ssh://git@bitbucket.org/opd-projects/test-template.git --checkout pure-python

  [1/9] project_name (Package Name): monitoring-tool
  [2/9] project_slug (monitoring-tool):
  [3/9] package_name (monitoring_tool):
  [4/9] module_name (monitoring_tool): monitor
  [5/9] class_prefix (MonitoringTool):
  [6/9] author_name (Your Name): Josh Harris
  [7/9] author_email (your.email@example.com): jjh@op.uk.com
  [8/9] description (Package description): A package to run monitoring on the Innotive PAS
  [9/9] python_requires (3.10): 3.12

```

Above you can see the inputs and the auto-generated defaults from the package_name inputs, you can accept the auto-generated inputs by just pressing enter, or you can override it by entering a new value, such as "monitor" for the module name instead of the auto-generated monitoring_tool. 

```powershell
deactivate
Remove-Item -Path ".\cc\" -Recurse -Force
../{project_name_venv}/scripts/activate.ps1

pip install -e .[dev]
```

Expected similar output:

```powershell
monitoring-tool> pip install -e .[dev]
Obtaining file:///C:/Users/josh.harris/OneDrive%20-%20Oxford%20Product%20Design/Documents/develop/newrepo/monitoring-tool
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Collecting pytest>=8.0 (from monitoring-tool==0.1.0)
  Downloading pytest-9.0.2-py3-none-any.whl.metadata (7.6 kB)
Collecting pytest-cov>=4.0 (from monitoring-tool==0.1.0)
  Downloading pytest_cov-7.0.0-py3-none-any.whl.metadata (31 kB)
Collecting ruff>=0.3 (from monitoring-tool==0.1.0)
  Downloading ruff-0.14.13-py3-none-win_amd64.whl.metadata (26 kB)
Collecting colorama>=0.4 (from pytest>=8.0->monitoring-tool==0.1.0)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting iniconfig>=1.0.1 (from pytest>=8.0->monitoring-tool==0.1.0)
  Downloading iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
Collecting packaging>=22 (from pytest>=8.0->monitoring-tool==0.1.0)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pluggy<2,>=1.5 (from pytest>=8.0->monitoring-tool==0.1.0)
  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting pygments>=2.7.2 (from pytest>=8.0->monitoring-tool==0.1.0)
  Using cached pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Collecting coverage>=7.10.6 (from coverage[toml]>=7.10.6->pytest-cov>=4.0->monitoring-tool==0.1.0)
  Downloading coverage-7.13.1-cp312-cp312-win_amd64.whl.metadata (8.7 kB)
Downloading pytest-9.0.2-py3-none-any.whl (374 kB)
Downloading pytest_cov-7.0.0-py3-none-any.whl (22 kB)
Downloading ruff-0.14.13-py3-none-win_amd64.whl (14.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.1/14.1 MB 28.6 MB/s eta 0:00:00
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading coverage-7.13.1-cp312-cp312-win_amd64.whl (222 kB)
Downloading iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Using cached pygments-2.19.2-py3-none-any.whl (1.2 MB)
Building wheels for collected packages: monitoring-tool
  Building editable for monitoring-tool (pyproject.toml) ... done
  Created wheel for monitoring-tool: filename=monitoring_tool-0.1.0-0.editable-py3-none-any.whl size=1789 sha256=16456a01072e71611f48ddb134bf8df7da636cf72f7cc685ad3f411356e59067
  Stored in directory: C:\Users\josh.harris\AppData\Local\Temp\pip-ephem-wheel-cache-2sbqxdv1\wheels\2f\d8\97\89a8c224bdf542411b67638c8d012151795e9daae2d2e6c13a
Successfully built monitoring-tool
Installing collected packages: ruff, pygments, pluggy, packaging, monitoring-tool, iniconfig, coverage, colorama, pytest, pytest-cov
Successfully installed colorama-0.4.6 coverage-7.13.1 iniconfig-2.3.0 monitoring-tool-0.1.0 packaging-25.0 pluggy-1.6.0 pygments-2.19.2 pytest-9.0.2 pytest-cov-7.0.0 ruff-0.14.13

[notice] A new release of pip is available: 25.0.1 -> 25.3
[notice] To update, run: python.exe -m pip install --upgrade pip
```
# First Time Installation
#### Install Virtual Environment
```bash
$ python -m pip install --user virtualenv
```
#### Create virtual environment
```bash
$ python -m virtualenv .venv
``` 
### Setting up environment Manager
1. Download environment manager (latest version | any version is fine)
2. Copy the environment manager folder to C:\ root folder
3. Rename the environment manager to EnvironmentManager_BBDVersion
4. Make sure that when you access EnvironmentManager.exe the path is in this form C:\EnvironmentManager_BBDVersion\EnvironmentManager.exe
# When running the project
#### Activate Virtual Environment
```bash
$ .\.venv\Scripts\activate
```
#### Install Python modules
```bash
$ pip install -r requirements.txt
```
#### Manually run Winium stored in .\WiniumDriver from the root of your project which will start HTTP service on port 9999. If you do not have the WiniumDriver installed download it on this github [link](https://github.com/2gis/Winium.Desktop/releases) and then store it under .\WiniumDriver folder for ease of accesse.

behave -f allure_behave.formatter:AllureFormatter -o allure-results

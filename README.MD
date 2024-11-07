# First Time Installation
#### Install Virtual Environment
```bash
$ python -m pip install --user virtualenv
```
#### Create virtual environment
```bash
$ python -m virtualenv .venv
``` 
#### Allure Report
Download [Allure Reports](https://allurereport.org/docs/install/) and once done add it to your environment variables under PATH
# When running the project
## Service Manager
1. Find sevice manager executable located on this path: C:\Users\bbdnet#####\AppData\Local\SARSSM\app-4.25.##\sm
2. Once you are in the directory start service manager using the following command
```bash
$ ServiceManager.exe -atm
```
This command will start service manager with the automation flag in which will triggure forms to open as xml.

3. When service manager starts it will use the cache from the previous session, meaning that if you previously logged in QA the latest session will be started in QA
## Running automation scripts
#### Activate Virtual Environment
```bash
$ .\.venv\Scripts\activate
```
#### Install Python modules
```bash
$ pip install -r requirements.txt
```
#### Running all the scripts without trigguring reports
```bash
$ behave
```
#### Running all the scripts with reports
```bash
$ behave -f allure_behave.formatter:AllureFormatter -o allure-results
```
#### Running a single script without trigguring reports
```bash
$ behave /path/to/a/feature/file
```
#### Running a single script with reports
```bash
$ behave -f allure_behave.formatter:AllureFormatter -o allure-results /path/to/a/feature/file
```
#### Serving Allure Reports
```bash
$ allure serve .\allure-results\
```
You can also generate HTML reports, refer to this [documentation](https://allurereport.org/docs/)
# Resources
[Pywinauto Documentation](https://pywinauto.readthedocs.io/en/latest/contents.html)

[GUI Inspector Tools](https://github.com/blackrosezy/gui-inspect-tool)

[Behave Documentation](https://behave.readthedocs.io/en/latest/)
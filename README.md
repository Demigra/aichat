# AI-Chat

For Debian based Linux distribution
In order to complete these steps, you should have a non-root user with sudo privileges.
Open terminal and run the commands given below.
To make sure that your versions are up-to-date, let’s update and upgrade the system with the apt command:
```bash
$ sudo apt update
$ sudo apt -y upgrade
```
Check whether Python3 is installed on the system or not using the following command:
```bash
$ python3 --version
```
Installing Python 3
Now you can start the installation of Python 3.8 with the command:
```bash
$ sudo apt install python3.8
```
Allow the process to complete and verify the Python version installed successfully:
```bash
$ python3 --version
```

Check whether pip3 is installed on the system or not using the following command:
```bash
$ pip3 --version
```
Installing pip3
Pip is a tool that will install and manage programming packages we may want to use in our development projects.
```bash
$ sudo apt install python3-dev python3-pip
```
Update pip3
If already installed then make sure pip version is up to date:
```bash
$ pip3 install -U pip
```
Installing Git
For the latest stable version for your release of Debian:
```bash
$ sudo apt install git
```
Verify the installation by typing the following command which will print the Git version:
```bash
$ git --version
```
Cloning project files on local machine
In your working directory run the following command:
```bash
$ git clone https://github.com/Demigra/aichat.git
```
This will create a directory containing all the project files.
Virtual Environment
Create a new virtual environment by choosing a Python interpreter and making a ./virtualenv directory to hold it:
```bash
$ python3 -m venv ./virtualenv
```
Activate the virtual environment:
```bash
$ source ./virtualenv/bin/activate
```
To deactivate virtual environment run:
```bash
$ deactivate
```
Rasa
Make sure to activate virtual environment and run:
```bash
(virtualenv)$ pip3 install rasa
```
Installing Additional dependencies:
```bash
(virtualenv)$ pip3 install rasa[spacy]
(virtualenv)$ python3 -m spacy download en_core_web_md
(virtualenv)$ python3 -m spacy link en_core_web_md en
```
Upgrading to the latest version of Rasa Open Source:
```bash
(virtualenv)$ pip3 install --upgrade rasa
```
Rasa X
Installing Rasa X local mode using following command:
```bash
(virtualenv)$ pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
```
Upgrading to the latest version of Rasa X Local mode:
```bash
(virtualenv)$ pip install -U rasa-x --extra-index-url https://pypi.rasa.com/simple
```
Training model/Bot
go to project directory:
```bash
(virtualenv)$ cd aichat/
```
Trains a model using your NLU data and stories, saves trained model in ./models:
```bash
(virtualenv)$ rasa train
```
Loading trained model and talking with bot
Launching in Terminal
```bash
(virtualenv)$ rasa shell
```
Launching Rasa X (with GUI) 
```bash
(virtualenv)$ rasa x
```

# License
Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE.txt)

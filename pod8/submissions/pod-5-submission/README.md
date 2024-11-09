# Pod 5 Readme Submission
* **Completed:** Novemeber 11, 2024
* **Members:** Mitchelle Mennelle, Nicholas Maag, Dan Trethaway
* **Version:** 1.0
__
# Ultraleap & Python Bindings Setup
## Description
The purpose of this document is to provide a summary on how to set up Ultraleap SDK and the python bindings for it. It will walk you through:
- Downloading Gemini SDK
- Pulling the Python bindings
- Setting up the Virtual Env
- Building the Python Bindings
- Running an example
__
## Step 1: Gemini SDK
The Gemini SDK is the SDK we will be using for Ultraleap Camera development, since it is compatable with Linux machines (our RaspPis)
1. Navigate to https://leap2.ultraleap.com/downloads/
2. Select Ultra Leap Controller 2
3. Select OS for your device
4. Install once finished downloading
- DO NOT change default location. This will cause issues with the Python Bindings.

## Step 2: Pull Python Bindings
The Python bindings are what we are using to interface with the SDK for the camera for Python development.
1. Pull from the repo https://github.com/ultraleap/leapc-python-bindings into a safe place.

## Step 3: Setting Up the Virtual Environment
Setting up the virtual environment allows you to install the required Python packages later.
1. Open the folder in VSCode
2. Open VSCode terminal
3. Run `python -m venv venv`
4. Run `./venv/Scripts/activate`
5. Run `pip install leap`

### If you have issues with activating the virtual environment, see here:
1. Open powershell as admin
2. Run `Get-ExecutionPolicy`
3. Run `Set-ExecutionPolicy RemoteSigned`
4. In VSCode terminal, run `./venv/Scripts/activate`

## Step 4: Building Python Bindings
1. Open VSCode terminal
2. Run `pip install -r .\leapc-python-bindings\requirements.txt`
3. Run `python -m build .\leapc-python-bindings\leapc-cffi`
4. Run `pip install .\leapc-python-bindings\leapc-cffi/dist/leapc_cffi-0.0.1.tar.gz`
5. Run `pip install -e .\leapc-python-bindings\leapc-python-api`

## Step 5: Running An Example
1. Take an example out of python bindings folder and place it in root
- If you don't have a camera, `print_current_time.py` will still work
2. Plug in Camera if you have one
3. Run example
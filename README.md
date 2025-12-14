# Mini Rag App

## Requirments

- python 3.10 or later

#### Install python using MiniConda
1) Download and install MiniConda from [here] (https://www.anaconda.com/docs/getting-started/miniconda/install#linux-terminal-installer)
2) create a new environment using the following commands:
```bash
$ conda create -n myapp python=3.10
```
3) Activate the environment:
    ```bash
    $ conda activate myapp
    ```

4) Upgrade the pip:
    ```bash
    $ python3 -m pip install --upgrade pip
    ```

5) install the requirments:
    ```bash
    $ pip install -r requirements.txt
    ```

 

``` bash 
$ cp .env.example .env
```

set you environment variables in the `.env` file. Like 


### Run the FastApi Server
``` bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
NOTE: To stop the Sever press CTRL + C



# clone the repo
# Create Virtual Enviroment 

# install WSL using this command
# wsl --install

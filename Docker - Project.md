# Docker - Project

Zervoudis Stefanos-me2009

## Περιγραφή



### Εντολές Δημιουργίας -  Εκτέλεσης  Docker - Project



**Create** [Dockerhub Account](https://hub.docker.com/) 

​	Username : szervoudis

---



#### Create the folder DockerProject

```visual basic
mkdir DockerProject

cd DockerProject
```

#### Create Dockerfile

```visual basic
nano Dockerfile

cat Dockerfile	# If you want to see the code of Dockerfile
```

#### Build a Container

```visual basic
sudo docker build -t szervoudis/mycontainername .
```

#### Push the Container in Dockerhub

```visual basic
sudo docker push szervoudis/mycontainername	# If needed
```

#### Run the container

```visual basic
sudo docker run -p 8080:5000 szervoudis/mycontainername
```

#### **Install docker-compose**

```visual basic
Step 1:

sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

---

```visual basic
Step 2:

sudo chmod +x /usr/local/bin/docker-compose
```

#### Create the configuration file

```visual basic
nano nginx.conf
```

#### Create docker-compose.yml 

```visual basic
nano docker-compose.yml

cat docker-compose	# If you want to see the code of docker-compose file
```

#### Run docker-compose 

```visual basic
sudo docker-compose up
```

#### Run docker-compose

```visual basic
sudo docker-compose down
```

#### Create a GitHub repository

```visual basic
Name of Repository is : 
```

---



### Εντολές Εκτέλεσης Docker - Project

---



#### **Run the application**

1. git clone https/...  .git
2. cd DockerProject
3. sudo docker-compose up
4. https://localhost:80

<img src="C:\Users\Στέφανος\Desktop\qwer.png" alt="Alt text" style="zoom:120%;" />


5. sudo docker-compose down





Code - Files 
---

#### Dockerfile

```dockerfile
FROM python:3.8

# set a directory for the app
WORKDIR ./

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 8080

# run the command
CMD ["python", "./app.py"]
```

#### Dockercompose.yml

```visual basic
version: '3.1'
 services:
     nginx:
         image: nginx:1.13.7
         container_name: nginx
         restart: always
         depends_on:
             - stef_flask_app
         volumes:
             - ./nginx.conf:/etc/nginx/conf.d/default.conf
         networks:
             - my-network
         ports:
             - 80:80

     stef_flask_app:
         image: szervoudis/mycontainer
         container_name: mycontainer
         restart: always
         environment:
             - ./app.py
         networks:
             my-network:
                 aliases:
                     - flask-app
         

 networks:
    my-network:
```

#### nginx.conf

```visual basic
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://flask-app:8080/;
        proxy_set_header Host "localhost";
    }
}
```

#### app.py

```python
from flask import Flask,render_template,send_file
import io
import os
import random
import datetime
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
from scipy.stats import norm


app = Flask(__name__)

list_of_stocks = ['IBM','GOOG','FB']


def inputs(Stock_name,start_date,stop_date):
    
    df = web.DataReader(f'{Stock_name}','yahoo',start_date,stop_date)
    df.to_csv(f'{Stock_name}' + ' - Rates.csv')


def daily_fluctuation():
    df = pd.read_csv(f'{Stock_name}' + ' - Rates.csv')
    df['Fluctuation'] = 100 * (df['Close'] - df['Open']) / df ['Open']
    output_excel_writer = pd.ExcelWriter(f'New_{Stock_name}.xlsx')
    df.to_excel(output_excel_writer, index=False)
    output_excel_writer.save()
    output_excel_writer.close()

    
def normalize():
    df = pd.read_excel(f'New_{Stock_name}.xlsx')
    # Υπολογσιμός Standard Deviation & Mean
    std = np.std(df['Fluctuation'],ddof=1)
    mean = np.mean(df['Fluctuation'])
    
    bins = (df['Fluctuation'].max() - df['Fluctuation'].min()) * 10
    bins = int(bins)

    domain = np.linspace(np.min(df['Fluctuation']),np.max(df['Fluctuation']))
    plt.plot(domain,norm.pdf(domain,mean,std))
    plt.hist(df['Fluctuation'], edgecolor = 'black',alpha=0.5,bins=bins, density=True)
    plt.title(f'{Stock_name}' + " - Normal Fit")
    plt.xlabel("Day_Var")
    plt.ylabel("Density")

    # Title box with blue line
    blue_line = mlines.Line2D([], [], color='blue', marker='',markersize=10,
                        label= "\n" + '$\mathcal{N}$ ' +  
                        f'$( \mu  \\approx {round((mean),5)} , \
                           \sigma  \\approx {round((std),5)} )$\n')
    plt.legend(handles=[blue_line])

    
def save_image():

      plt.savefig('static/images/image.jpg')


PEOPLE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/')
def index():
 
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
    return render_template("index.html", user_image = full_filename)


if __name__ == "__main__":
	
    # 1
    Stock_name = random.choice(list_of_stocks)
    print("The Chosen Stock Name : " + f'{Stock_name}')
    start_date = datetime.datetime(2019,11,1)
    stop_date = datetime.datetime(2020,11,1)
    
    # 2
    inputs(Stock_name,start_date,stop_date)
    
    # 3
    daily_fluctuation()
    
    # 4
    normalize()
    
    # 5
    save_image()
    
    # Export Port
    app.run(host='0.0.0.0',port=5000,debug=False)
  

```

#### requirements NA TA BRW

```python
matplotlib==3.3.0

pandas==1.0.5

flask==1.1.2

numpy==1.19.4

```



 


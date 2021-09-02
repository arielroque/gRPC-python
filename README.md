# gRPC-python

## :bookmark: Requirements

- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## :triangular_flag_on_post: Starting

```bash
# Clone repository
git clone https://github.com/arielroque/gRPC-python.git

cd gRPC-python

# Prepare enviroment
virtualenv -p python3 env

# Go to enviroment
source env/bin/activate
```

## :building_construction: Building 

```bash

#Install requirements
pip3 install -r requirements.txt

#Generate files from types created in Protocol Buffer
cd src
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

## :runner: Running Server

```bash
python server.py
```

## :runner: Running Client

```bash
python client.py
```


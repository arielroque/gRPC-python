# gRPC-python

Expose functions via gRPC between a server and a client using Python


## :bookmark: Requirements

- [Virtualenv](https://virtualenv.pypa.io/en/latest/)


## :question: What is gRPC?

RPC or remote procedure calls are the messages that the server sends to the remote system to get the task(or subroutines) done.
Google’s RPC is designed to facilitate smooth and efficient communication between the services.

![](https://global-uploads.webflow.com/5d2dd7e1b4a76d8b803ac1aa/5e95a1342e7addf4779de6bf_gMcq6oqNPLjx3789zJJo5lliby7MMg5xhTTr4T1seja9RSIEANF0zwIPR8VyCCDyLCKbVlvqV7PsF-KEZ_thEO4i9x59wwd4msRHQj2e4e5MJJdwKlg78H7PelXs1vs2ulRSzfJs.png)

Font: [gRPC](https://grpc.io/)


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


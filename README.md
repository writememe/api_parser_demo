# api_parser_demo
A demo repo containing some examples of parsing APIs to solve a networking problem.

# Overview

This demonstration is to show how network professionals can solve a common problem, but use modern
automation techniques in order to solve it. The idea is that you learn concepts but working towards
an outcome, which hopefully helps you retain the knowledge.

# Problem Statement

The problem is as a firewall administrator, you might need to find out all the allowed public IP
prefixes for a cloud service, so that only those explicit ranges can be added to your firewall policy.

This may come to you in the form of a following business requirement:

| Source | Destination | Service | Business Reason|
| ---------- | ------------ | ----------------- | ------------- | 
| <DATA_CENTRE_DMZ_SUBNET> |Amazon Web Services (AWS) Public IP Ranges |TCP/443|Allow outbound access to AWS to reach public AWS services|

The problem is, where is that public IP range(s) defined? How often does it change? How do I know when it has been updated, so I can updated my firewall rule(s)?

This demo will show you how to use automation on how to retrieve and parse this information.


## Supported Environments

This demonstration is only supported on:
 - Python 3.6 or greater
 - Linux/unix machines only


## Installation/Operating Instructions

There are two methods for installing or operating the demo. The instructions for each method are described below.

### Python 3.X

The most popular way of running this application is using it in a standard Python environment. To do so, please follow the options below:

1) Clone the repository to the machine on which you will run the application from:

```git
git clone https://github.com/writememe/api_parser_demo.git
cd api_parser_demo
```

2) Create the virtual environment to run the application in:

```console
virtualenv --python=`which python3` venv
source venv/bin/activate
```
3) Install the requirements:
```
pip install -r requirements.txt
```

#!/usr/bin/env python
# encoding: utf-8

from fabric.api import env,local,cd,run,sudo,get

env.hosts=['bulain@localohst']

def hello():
    print("Hello world!")

def helloc(name, value):
    print("%s = %s!" % (name, value))
    
def lsfab():
    local('cd')
    local('ls')
    
def remote():
    print("remote run")
    with cd('~'):
        run('ls -l')

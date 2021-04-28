#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, task
from subprocess import call

use_plugin("python.core")
use_plugin("python.unittest")

use_plugin("pypi:selenium")
use_plugin("pypi:behave")


name = "curso_python"
default_task = "behave"

DEV_URL = "http://localhost:3000"
PROD_URL = "http://localhost:4000"

@init(environments='develop')
def initialize_dev(project):
    print("Initializing DEVELOP env...")
    project.set_property("URL_END",DEV_URL)
    
@init(environments='prod')
def initialize_prod(project):
    print("Initializing PROD env...")
    project.set_property("URL_END",PROD_URL)
    

@task
def behave(project):
    call(["behave",f"-D entorno={project.get_property('URL_END')}"])




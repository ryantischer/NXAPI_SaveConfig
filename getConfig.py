__author__ = 'ryantischer'

# Created by Ryan Tischer @ Cisco
# rytische at cisco.com
# use at your own risk
# this script is not supported by TAC or anyone else

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



#TODO Error checking


import requests
import json
import sys
import os

# Get url, username and password
node = sys.argv[1]
switchuser = sys.argv[2]
switchpassword = sys.argv[3]

#check if input is a single node or a json file of nodes

if  os.path.exists(node):
    json_data=open(node)
    elements = json.load(json_data)
else:
    elements = {1:node}


#------------------------------------------------
def getHostname(url):
#Get hostname

#Build var called myheaders to pass to NXAPI
    myheaders={'content-type':'application/json-rpc'}
#build payload var to POST show hostname
    payload=[
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
        "cmd": "show hostname",
        "version": 1
        },
        "id": 1
    }
    ]

#this is where the magic happens.  'Response' is a var assigned to requests.post.  Requests is a python library that
# makes it easy to get/post data from a website.  In this case we are asking for and recieving json data.
# Notice .json at the end.

    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

# requests.post puts the json data in a python dictionary.  Python dictionaries are also formatted in key:value pairs
# so it lines up nicely with json.  The actual data in 'response is...
# {u'jsonrpc': u'2.0', u'result': {u'body': {u'hostname': u'Spine2'}}, u'id': 1}
# THis a a nested dictionary (notice the "{" so to get the output we need...

    hostname = response['result']['body']['hostname']
    return(hostname)


#------------------------------------------------
#Get configuration in XML file

myheaders2={'content-type':'application/xml'}
payload2="""<?xml version="1.0"?> <ins_api> <version>1.0</version> <type>cli_show_ascii</type> <chunk>0</chunk> <sid>sid</sid> <input>show run</input> <output_format>xml</output_format> </ins_api>"""


for i in elements:

#CHANGE http to https for secure communication

    url = "http://" + elements[i] + "/ins"
#request to get configuration
    response2 = requests.post(url,data=payload2,headers=myheaders2,auth=(switchuser,switchpassword)).text

#TODO strip XML headers/footer

#build the file.
    output = open(getHostname(url), "wb")
    output.write(response2)
    output.close()





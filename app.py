#! python3


# ---- Notes

"""
Attention!!! check Imports and Dependencies section below.
             Use Pip to install eel, tinydb, and pyautogui

Everything is Squished into one python file because of how the Eel library works.
Pushing this application to the Flask Framework in the future might be beneficial.

"""


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#                  Imports and Dependencies
#....................................................................

import eel, json, secrets
from tinydb import TinyDB, Query
#import pyautogui

#.....................................................................
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#=====================================================================

'''                          &                                      '''


#=====================================================================
#                           Variables
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

db = TinyDB('web/db.json')
scrumb = db.table('scrumb')
queryenv = []
scrumlistenv = []
caughtid = []

#=====================================================================
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#=====================================================================

'''                           &                                     '''



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
eel.init('web')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''                           \/                                      '''

#-----------------------------------------------------------------------

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#-----------------------------------------------------------------------
#                   Task Object Creation --Scrum
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def save_to_db(n):
    #returnvalues = json.loads(n)
    #db.insert(task)
    taskobjectID = secrets.token_hex(25)
    taskstring = (n)
    tasklist = taskstring.split('..,|,..')
    tsksub = tasklist[0]
    tskdesc = tasklist[1]
    print("worked")
    scrumb.insert({"id": taskobjectID, "subject": tsksub, "description": tskdesc, "list": "tasktabletodo"})

@eel.expose
def object_pitcher():
    envelope = []
    for item in scrumb:
        envelope.append(item['id'])
        envelope.append(item['subject'])
        envelope.append(item['list'])
    envstr = '..,|,..'.join(envelope)
    return envstr


#-----------------------------------------------------------------------

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#-----------------------------------------------------------------------
#                   Random development Tools
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@eel.expose
def print_objects():
    for item in scrumb:
        print(item)

@eel.expose
def read_db():
    printout = scrumb.all()
    print(printout)

@eel.expose
def clear_db():
    scrumb.purge()


#------------------------------------------------------------------------

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#------------------------------------------------------------------------    
#              Query Functions for Taskclick Modal - Scrum
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def taskobject_id_catcher(n):
    thisguy = n
    query_by_id(thisguy)

def query_by_id(n):
    if len(queryenv) > 0:
        queryenv.pop()
    query = scrumb.get(Query().id == n)
    qsub = query['subject']
    qdesc = query['description']
    qlist = query['list']
    qpack = qsub + "..,|,.." + qdesc + "..,|,.." + qlist
    queryenv.append(qpack)
    eel.query_trigger()


@eel.expose
def query_pitcher():
    envstr = queryenv[0]
    return envstr

#------------------------------------------------------------------------

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#------------------------------------------------------------------------    
#              Taskobject dragndrop change List - Scrum
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def list_change_id_catcher(n):
    thisguy = n
    query_list_change(thisguy)

#need id of taskobject

def query_list_change(n):
    containera = n.split('..,|,..')
    if len(scrumlistenv) > 0:
        scrumlistenv.pop()
    if len(queryenv) > 0:
        queryenv.pop()
    query = scrumb.update({'list': containera[1]}, Query().id == containera[0])



#-------------------------------------------------------------------------

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#-------------------------------------------------------------------------

'''                             #                                       '''

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
eel.start('main.html', block=False)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''                             \/                                      '''



@eel.expose # decorator that makes this python function callable in javascript
def task_button(): 
    eel.form_fetch()(save_to_db) # Javascript function with python function in argument, said function grabs value returned from javascript side and saves to database


@eel.expose
def id_exchange_button():
    eel.taskobject_id_pitcher()(taskobject_id_catcher)

@eel.expose
def list_exchange_button():
    eel.listchange_pitcher()(list_change_id_catcher)




'''                             #                                       '''

#==========================================================================
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#==========================================================================  
# opens the devtools
#..........................................................................

eel.sleep(1.5)
#pyautogui.hotkey('ctrl', 'shift', 'j')

#print_objects()
#..........................................................................


'''                                 &                                       '''


#==========================================================================
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#==========================================================================
# Keeps program from closing
#..........................................................................

while True:
   eel.sleep(1.0)

#..........................................................................
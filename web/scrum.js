
//-------------------------------------------------------
//              Variables
// ------------------------------------------------------
var subjectsobj = [];
var caughtid = [];
// ------------------------------------------------------


function console_test() {
    console.log("she works friend")

}

//=============================================================================
//|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
//=============================================================================

//                      Task Click and modal Expose
//-----------------------------------------------------------------------------



eel.expose(taskobject_id_pitcher) // is capable of sending data to python 
function taskobject_id_pitcher() {
    return caughtid[0]
}

eel.expose(taskobject_id_grabber)
function taskobject_id_grabber(id) { //works
    caughtid.pop()
    caughtid.push(id)
    eel.id_exchange_button()
}

function query_catcher(n) {
    querylist = n.split('..,|,..')
    console.log("We've got the stuff: " + querylist)
    qdata_insertion()
}

eel.expose(query_trigger)
function query_trigger() {
    eel.query_pitcher()(query_catcher)
}

function qdata_insertion() {
    var qsubnode = document.getElementById("subjectdet")
    var qdescnode = document.getElementById("descriptiondet")
    //var qlistnode = document.getElementById("listdet")
    qsubnode.innerHTML = querylist[0]
    qdescnode.innerHTML = querylist[1]
}

//=============================================================================
//|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
//=============================================================================

//                      Taskobject Creation
//-----------------------------------------------------------------------------

eel.expose(form_fetch)
function form_fetch() { 
    var taskobjsub = document.getElementById("sub1").value;
    var taskobjdesc = document.getElementById("desc1").value;
    return taskobjsub + '..,|,..' + taskobjdesc;    
}


eel.expose(object_catcher)
function object_catcher(n) {
    objdata = (n)
    objlist = objdata.split('..,|,..')
    howmanyarrays = objlist.length / 3
    var iterarray = []
    iterarray.length = howmanyarrays
    var i = 0
    var looper = function(){
        while (i < howmanyarrays){
            var arraycontainer = objlist.splice(0, 3)
            var tasktableitem = document.createElement("LI");
            tasktableitem.innerHTML = '<button class="btn btn-primary btn-lg" mouseenter="" onclick="taskobject_id_grabber(this.id)" data-toggle="modal" data-target="#modaltaskobjectdetails" id="' + arraycontainer[0] + '">'
             + arraycontainer[1] + '</button>';
            tasktableitem.setAttribute("class", "list-group-item")
            document.getElementById(arraycontainer[2]).appendChild(tasktableitem);
            i++
        }

    }
    looper()    
}



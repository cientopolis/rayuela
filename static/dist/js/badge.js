function init(){
    document.getElementById('task_types').style.display = '';
    document.getElementById('time_restrictions').style.display = 'none';
    document.getElementById('areas').style.display = 'none';
};

function taskTypesSelected(){
    document.getElementById('task_types').style.display = '';
    document.getElementById('time_restrictions').style.display = 'none';
    document.getElementById('areas').style.display = 'none';
};

function timeRestrictionsSelected(){
    document.getElementById('task_types').style.display = 'none';
    document.getElementById('time_restrictions').style.display = '';
    document.getElementById('areas').style.display = 'none';
};

function areaSelected(){
    document.getElementById('task_types').style.display = 'none';
    document.getElementById('time_restrictions').style.display = 'none';
    document.getElementById('areas').style.display = '';
};

function changeCriterion(){
    const criterion = document.getElementById('criterion').value;
    if (criterion === 'task_type'){
        taskTypesSelected();
    }
    else if (criterion === "time_restriction"){
        timeRestrictionsSelected();
    }
    else{
        areaSelected();
    }
};

init();
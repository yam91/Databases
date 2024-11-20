const addDiv = document.querySelector("#addDiv");
addDiv.addEventListener("click", insertDiv);
var fileNum = 2;
function insertDiv() { 
const subject = document.querySelector("#insert");
innerHTML = `
  <div class= 'd-flex form-group' id="div-file${fileNum}">
  <label for="file${fileNum}"> File ${fileNum}</label>
  <input type="file" class="form-control flex-shrink-3" name="file${fileNum}" id="file${fileNum}" required>
  <button type="reset" class="form-control" value="Reset">Reset</button>
  </div>
  `;
subject.insertAdjacentHTML("beforebegin", innerHTML);
fileNum = fileNum+1;
};

const removDivButt = document.querySelector("#removDiv");
removDivButt.addEventListener("click", removDiv);
function removDiv() { 
  const subject = document.querySelector("#div-file"+`${fileNum-1}`);
  subject.remove();
  fileNum = fileNum - 1;
}

const addTask = document.querySelector("#addTask");
addTask.addEventListener("click", insertTask);
var taskNum = 2;
function insertTask() { 
const here = document.querySelector("#insertTask");
innerHTML = `<div class= 'd-flex form-group' id="div-task${taskNum}">
  <label for="task${taskNum}"> Task ${taskNum}</label>
  <input type="text" class="form-control flex-shrink-3" name="task${taskNum}" id="task${taskNum}" required/>
  <button type="reset" class="form-control" value="Reset">Reset</button>
  </div>
  `;
here.insertAdjacentHTML("beforebegin", innerHTML);
taskNum = taskNum+1;
};

const removTaskButt = document.querySelector("#removTask");
removTaskButt.addEventListener("click", removTask);
function removTask() { 
  const subject = document.querySelector("#div-task"+`${taskNum-1}`);
  subject.remove();
  taskNum = taskNum - 1;
}
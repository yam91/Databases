const addDiv = document.querySelector("#addDiv");
addDiv.addEventListener("click", insertDiv);
var fileNum = 2;

function insertDiv() { 
const subject = document.querySelector("#insert");
innerHTML = `
  <div class= 'd-flex form-group' id="div-file${fileNum}">
  <label for="file${fileNum}">File ${fileNum}</label>
  <input type="file" class="form-control flex-shrink-3" name="file${fileNum} id="file${fileNum}" required>
  <button type="reset" class="form-control" value="Reset">Reset</button>
  </div>
  `;
subject.insertAdjacentHTML("beforebegin", innerHTML);
fileNum = fileNum+1;
}

const removDivButt = document.querySelector("#removDiv");
removDivButt.addEventListener("click", removDiv);
function removDiv() { 
  const subject = document.querySelector("#div-file"+`${fileNum-1}`);
  subject.remove();
  fileNum = fileNum - 1;
}

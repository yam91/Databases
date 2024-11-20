const link = document.getElementByID('edit-link');
link.addEventListener('click', addForm);
function addForm() {
    const here = document.querySelector("#insert-form");
    innerHTML = `
    <div class="row">
        <form id = "form" action="/tasklist" method="POST" >
            <input type="text" name="edit-content" id="edit-content" class="form-control mt-3 mb-3 ml-3" style="background-color: white;" required>
            <button type="submit" class= "btn btn-primary ml-3">Save</button>
        </form>
    <div>`;
    here.insertAdjacentHTML("beforebegin", innerHTML);
  }
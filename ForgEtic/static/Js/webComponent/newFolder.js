const newFolder = document.createElement('template'); 
newFolder.innerHTML = `
    <style>

    </style>

    <div class= "newFolder">
        <input type="text" id="newFolderInput" placeholder="Enter folder name">
        <button class="newFolderButton">Create</button>
        <button class = "cancel">Cancel</button>

    </div>

`;
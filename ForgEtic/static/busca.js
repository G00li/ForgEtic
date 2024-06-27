document.addEventListener('DOMContentLoaded', (event) => {
    const searchInput = document.getElementById('search-input');
    const folders = document.querySelectorAll('.folders');
    const files = document.querySelectorAll('.divfile');

    searchInput.addEventListener('input', () => {
        const searchTerm = searchInput.value.toLowerCase();

        folders.forEach(folder => {
            const folderName = folder.querySelector('.folder-name').innerText.toLowerCase();
            if (folderName.includes(searchTerm)) {
                folder.style.display = '';
            } else {
                folder.style.display = 'none';
            }
        });

        files.forEach(file => {
            const fileName = file.querySelector('.labelFileName').innerText.toLowerCase();
            if (fileName.includes(searchTerm)) {
                file.style.display = '';
            } else {
                file.style.display = 'none';
            }
        });
    });
});
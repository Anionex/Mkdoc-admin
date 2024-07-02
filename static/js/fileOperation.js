function deleteFile(button) {
    if (confirm("Are you sure you want to delete this file?")) {
        const fileItem = button.parentElement;
        const filePath = fileItem.querySelector('.file-link').getAttribute('href');
        // Create a form
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = deleteFileUrl; // Your server-side script to handle the deletion

        // Create an input to hold the file name
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'filePath';
        input.value = filePath;

        // Append the input to the form
        form.appendChild(input);

        // Append the form to the body (not displayed)
        document.body.appendChild(form);

        // Submit the form
        form.submit();

        // Optionally remove the file item from the DOM
        fileItem.remove();
        form.remove();
        console.log(`File "${filePath}" deleted`);
    }
    return false; // 阻止默认的提交操作
}


let currentFileItem = null;

// 右键点击显示自定义菜单
document.querySelectorAll('.file-link').forEach(item => {
    item.addEventListener('contextmenu', function(event) {
        event.preventDefault();
        
        currentFileItem = item;
        
        const contextMenu = document.getElementById('contextMenu');
        contextMenu.style.display = 'block';
        contextMenu.style.left = `${event.pageX}px`;
        contextMenu.style.top = `${event.pageY}px`;

    });
});

// 添加右键点击事件监听器到 .side-bar 元素
document.querySelector('.sidebar').addEventListener('contextmenu', function(event) {
    event.preventDefault();
    
    // 检查点击的目标是否是 .file-item 或其子元素
    if (event.target.closest('.file-link')) {
        return; // 如果点击的是 .file-item，忽略 .sidebar 的处理
    }


    // currentFileItem = item.closest('li');
    const contextMenu = document.getElementById('contextMenuForBlank');
    contextMenu.style.display = 'block';
    contextMenu.style.left = `${event.pageX}px`;
    contextMenu.style.top = `${event.pageY}px`;
        
});


// 点击页面其他地方时隐藏上下文菜单
document.addEventListener('mousedown', function(event) {
    const contextMenus = document.querySelectorAll('.context-menu');
    contextMenus.forEach(menu => {
        menu.style.display = 'none';
    });
});

function deleteFileFromMenu() {
    if (currentFileItem) {
        const filePath = currentFileItem.querySelector('.file-link').getAttribute('href');
        fetch(deleteFileUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // 如果你使用 CSRF 保护
            },
            body: JSON.stringify({ filePath: filePath })
        })
        .then(response => {
            if (response.ok) {
                currentFileItem.remove();
                console.log(`File "${filePath}" deleted`);
            } else {
                console.error('Failed to delete file');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}

function renameFileFromMenu() {
    if (currentFileItem) {
        const fileLink = currentFileItem.querySelector('.file-link');
        const filePath = fileLink.getAttribute('href');
        const newFileName = prompt("Enter new file name:", fileLink.textContent);
        
        if (newFileName) {
            fetch('/rename-file', {  // 假设你的重命名端点是 /rename-file
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // 如果你使用 CSRF 保护
                },
                body: JSON.stringify({ oldFilePath: filePath, newFileName: newFileName })
            })
            .then(response => {
                if (response.ok) {
                    fileLink.textContent = newFileName;
                    fileLink.setAttribute('href', newFileName); // 假设新文件名即为新路径
                    console.log(`File renamed to "${newFileName}"`);
                } else {
                    console.error('Failed to rename file');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }
}
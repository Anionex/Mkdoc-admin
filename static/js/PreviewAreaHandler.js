document.addEventListener("DOMContentLoaded", function() {
    const textarea = document.getElementById('markdown-input');
    const previewArea = document.getElementById('markdown-content');

    if (typeof marked !== 'undefined') {
        marked.setOptions({
            gfm: true,  // 启用 GitHub 风格的 Markdown
            breaks: true,  // 将单个换行符转换为 <br>
            highlight: function(code, lang) {
                const validLanguage = hljs.getLanguage(lang) ? lang : 'plaintext';
                return hljs.highlight(code, { language: validLanguage }).value;
            }
        });

        textarea.addEventListener('input', function() {
            let markdownString = textarea.value;
            markdownString = markdownString.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
            // markdownString = markdownString
            //     .replace(/  /g, '&nbsp;&nbsp;')  // 替换双空格为不间断空格
            const htmlContent = marked(markdownString);
            previewArea.innerHTML = htmlContent;
            document.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightBlock(block);
            });
        });

        // Initial render
        const markdownString = textarea.value;
        const htmlContent = marked(markdownString);
        previewArea.innerHTML = htmlContent;
        document.querySelectorAll('pre code').forEach((block) => {
            hljs.highlightBlock(block);
        });
    } else {
        console.error("marked.js library is not loaded correctly.");
    }
});

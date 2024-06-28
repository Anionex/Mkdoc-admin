// document.addEventListener('DOMContentLoaded', (event) => {
    const textarea = document.querySelector('.text-area');

    textarea.addEventListener('keydown', function(event) {
        if (event.key === 'Tab') {
            event.preventDefault(); // Prevent the default tab action

            let start = this.selectionStart;
            let end = this.selectionEnd;

            if (start === end) {
                // Insert tab at single cursor position
                document.execCommand('insertText', false, "  ");
            } else {
                // Handle multi-line tab insertion
                let strBefore = this.value.slice(0, start);
                let curLineStart = strBefore.lastIndexOf('\n') + 1;
                let strBetween = this.value.slice(curLineStart, end);
                let newStr = "  " + strBetween.replace(/\n/g, '\n  ');

                this.setSelectionRange(curLineStart, end);
                document.execCommand("insertText", false, newStr);

                // Adjust selection range after insertion
                let lineBreakCount = strBetween.split('\n').length;
                let newStart = start + 2;
                let newEnd = end + lineBreakCount * 2;

                this.setSelectionRange(newStart, newEnd);
            }
        }
    });
    document.getElementById('edit-form').addEventListener('submit', function(event) {
        if (!confirm_save()) {
            event.preventDefault();
        }
    });
    function confirm_save() {
        // 执行确认操作
        if (confirm("Are you sure you want to save?")) {
            document.getElementById("edit-form").submit(); // 手动提交表单
        }
        return false; // 阻止默认的提交操作
    }
    const textArea = document.querySelector(".text-area");
    const initialContent = textArea.value;
    function confirm_discard() {
        console.log(initialContent);
        if (confirm("Are you sure you want to discard all the chages you make?")) {
            textArea.value = initialContent;
        }
        return false;
    }

    function collapseSidebar() {
        document.querySelector('.sidebar').classList.toggle('collapsed');
        document.querySelector('.sidebar-container').classList.toggle('collapsed');
    }

    document.addEventListener("DOMContentLoaded", function() {
        const textarea = document.getElementById('markdown-input');
        const previewArea = document.getElementById('markdown-content');

        if (typeof marked !== 'undefined') {
            marked.setOptions({
                highlight: function(code, lang) {
                    const validLanguage = hljs.getLanguage(lang) ? lang : 'plaintext';
                    return hljs.highlight(code, { language: validLanguage }).value;
                }
            });

            textarea.addEventListener('input', function() {
                const markdownString = textarea.value;
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
// });
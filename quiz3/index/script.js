document.getElementById('generateBtn').addEventListener('click', () => {
    const count = parseInt(document.getElementById('blockCount').value);
    if (isNaN(count) || count < 1) return;
    
    const container = document.getElementById('blockContainer');
    for (let i = 0; i < count; i++) {
        const block = document.createElement('div');
        block.className = 'block';
        block.onclick = () => container.removeChild(block);
        container.appendChild(block);
    }
});
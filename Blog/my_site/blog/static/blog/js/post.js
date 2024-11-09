const submitButton = document.getElementById('submitComment');
const commentInput = document.getElementById('commentInput');
const commentsList = document.getElementById('commentsList');

submitButton.addEventListener('click', () => {
    const commentText = commentInput.value.trim();
    if (commentText) {
        const commentDiv = document.createElement('div');
        commentDiv.classList.add('comment');
        commentDiv.innerHTML = `<p>${commentText}</p>`;
        commentsList.appendChild(commentDiv);
        commentInput.value = ''; // Очищаем поле ввода
    } else {
        alert('Пожалуйста, введите комментарий.');
    }
});
let currentPage = 1;
const totalPages = 10;
const currentPageElement = document.getElementById('currentPage');
const totalPagesElement = document.getElementById('totalPages');
const prevButton = document.getElementById('prevButton');
const nextButton = document.getElementById('nextButton');
function updatePagination() {
    currentPageElement.textContent = currentPage;
    totalPagesElement.textContent = totalPages;

    prevButton.disabled = currentPage === 1;
    nextButton.disabled = currentPage === totalPages;
}
prevButton.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        updatePagination();
    }
});
nextButton.addEventListener('click', () => {
    if (currentPage < totalPages) {
        currentPage++;
        updatePagination();
    }
});
updatePagination();
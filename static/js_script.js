const modal = document.getElementById("portfolioModal");
const modalImgContainer = document.querySelector(".modal-image-container");
const modalCaption = document.querySelector(".modal-caption");
const closeBtn = document.querySelector(".close");
const leftArrow = document.querySelector(".arrow.left");
const rightArrow = document.querySelector(".arrow.right");

let currentImages = [];
let currentIndex = 0;

// Open modal on thumbnail click
document.querySelectorAll(".work-item-thumb").forEach((thumb) => {
  thumb.addEventListener("click", () => {
    const group = thumb.getAttribute("data-group");
    const images = document.querySelectorAll(
      `.modal-images[data-group='${group}'] .portfolio-image`
    );

    currentImages = Array.from(images);
    currentIndex = 0;
    showImage(currentIndex);
    modal.style.display = "block";
  });
});

// Show image in modal
function showImage(index) {
  modalImgContainer.innerHTML = "";
  const imgElement = currentImages[index].querySelector("img").cloneNode();
  const captionText = currentImages[index].querySelector(
    ".portfolio-caption"
  ).innerText;

  modalImgContainer.appendChild(imgElement);
  modalCaption.innerText = captionText;
}

// Navigation
leftArrow.addEventListener("click", () => {
  currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
  showImage(currentIndex);
});

rightArrow.addEventListener("click", () => {
  currentIndex = (currentIndex + 1) % currentImages.length;
  showImage(currentIndex);
});

// Close modal
closeBtn.addEventListener("click", () => {
  modal.style.display = "none";
});

// Close when clicking outside content
window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
  }
});

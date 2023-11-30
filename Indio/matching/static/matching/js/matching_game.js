window.selectedImages = [];

window.selectImage = function(imageUrl) {
    const imageContainers = document.querySelectorAll('#image-container div.about-img img');
    console.log(imageUrl + " is selected.");

    for (let i = 0; i < imageContainers.length; i++) {
        // Replace the 'gradient.jpeg' image in the answer with the selected choice
        if (imageContainers[i].src.includes('gradient.jpeg')) {
            imageContainers[i].src = imageUrl;
            window.selectedImages.push(imageUrl);
            break;
        }
    }

    if (window.selectedImages.length === 2) {
        window.compareAnswers();
    }
};

window.deselectImage = function(clickedImage) {
    console.log(clickedImage.src + " is deselected.");
    if (!clickedImage.src.includes('gradient.jpeg')) {
        clickedImage.src = gradientImageUrl;
        window.selectedImages = window.selectedImages.filter(imgUrl => imgUrl !== clickedImage.src);
    }
};

window.compareAnswers = function() {
    // TODO
};

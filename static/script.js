// To preview image before submitting.

var previewImage = function (event) {
                var preview = document.getElementById('your-image');
                preview.src = URL.createObjectURL(event.target.files[0]);
                preview.style.display = "block";
            };
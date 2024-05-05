var image = document.getElementById('profileImage');
    
// Add a click event listener to the image
image.addEventListener('click', function() {
    // Check if browser supports fullscreen API
    if (image.requestFullscreen) {
        image.requestFullscreen();
    } else if (image.mozRequestFullScreen) { /* Firefox */
        image.mozRequestFullScreen();
    } else if (image.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
        image.webkitRequestFullscreen();
    } else if (image.msRequestFullscreen) { /* IE/Edge */
        image.msRequestFullscreen();
    }
});


// Read More Button Functionality

document.addEventListener("DOMContentLoaded", function() {
    var shortDescription = document.getElementById("short-description");
    var fullDescription = document.getElementById("full-description");
    var readMoreBtn = document.getElementById("read-more-btn");

    // Check if the short description has less than 100 words
    if (shortDescription.textContent.split(" ").length < 100) {
        // If less than 100 words, hide the "Read More" button
        readMoreBtn.style.display = "none";
    } else {
        // If more than or equal to 100 words, show the "Read More" button
        readMoreBtn.style.display = "inline"; // Or any other display property
    }

    readMoreBtn.addEventListener("click", function(event) {
        event.preventDefault(); // To prevent default link behavior

        shortDescription.style.display = "none";
        fullDescription.style.display = "block";
        readMoreBtn.style.display = "none";
    });
});

// JavaScript functions to show/hide boxes
function showSkills() {
    document.getElementById('skillsBox').style.display = 'block';
    document.getElementById('educationBox').style.display = 'none';
}

function showEducation() {
    document.getElementById('skillsBox').style.display = 'none';
    document.getElementById('educationBox').style.display = 'block';
}

// Dark Color calculate
function darkenColor(color, percentage) {
    // Convert hex color to RGB
    const r = parseInt(color.substring(1, 3), 16);
    const g = parseInt(color.substring(3, 5), 16);
    const b = parseInt(color.substring(5, 7), 16);

    // Calculate darker RGB components
    const newR = Math.round(r * (100 - percentage) / 100);
    const newG = Math.round(g * (100 - percentage) / 100);
    const newB = Math.round(b * (100 - percentage) / 100);

    // Convert RGB components back to hex
    const newColor = '#' + ((1 << 24) + (newR << 16) + (newG << 8) + newB).toString(16).slice(1);

    return newColor;
}

// Usage example
const originalColor = getComputedStyle(document.documentElement).getPropertyValue('--main-color').trim();
const darkenedColor = darkenColor(originalColor, 50);
// Set the darkened color as a CSS variable specifically for .dark-mode
document.documentElement.style.setProperty('--bg-color-dark-mode', darkenedColor);



 // menu icon
 let menuicon = document.querySelector('#menu-icon');
 let navbar = document.querySelector('.navbar');
 menuicon.onclick = () => {
     menuicon.classList.toggle('bx-x');
     navbar.classList.toggle('active');
 };


 // scroll section 
 let sections = document.querySelectorAll('section');
 let navLinks = document.querySelectorAll('header nav a');

 window.onscroll = () => {

     sections.forEach(sec => {
         let top = window.scrollY;
         let offset = sec.offsetTop - 150;
         let height = sec.offsetHeight;
         let id = sec.getAttribute('id');

         if (top >= offset && top < offset + height) {
             navLinks.forEach(links => {
                 links.classList.remove('active');
                 document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
             });
         };
     });
     // sticky navbar
     let header = document.querySelector(".header");

     header.classList.toggle("sticky", window.scrollY > -1);


     menuicon.classList.remove('bx-x');
     navbar.classList.remove('active');


 };

 /*slidebar*/




    let darkMode = document.querySelector('#darkmode-icon');
    darkMode.onclick = () => {
        darkMode.classList.toggle('bx-sun')
        document.body.classList.toggle('dark-mode');
    };

    ScrollReveal({
        reset: true,
        distance: '80px',
        duration: 2000,
        delay: 200
    });
    ScrollReveal().reveal('.home-content, .heading', { origin: 'top' });
    ScrollReveal().reveal('.home-img img,.about-img img,.service-container, .portfolio-box, .resume-box,.resume-container,.contact form', { origin: 'bottom' });

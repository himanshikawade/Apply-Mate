document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    navToggle.addEventListener('click', function() {
        navMenu.classList.toggle('active');
    });
    
    // Smooth hover effect for "KA-VA-VI"
    const ScholarPath = document.querySelector('.ScholarPath');

    ScholarPath.addEventListener('mouseover', () => {
        ScholarPath.style.transition = "all 0.5s ease";
        ScholarPath.textContent = "स्कॉलरपाथ"; // Marathi equivalent for KA
    });
    ScholarPath.addEventListener('mouseout', () => {
        ScholarPath.textContent = "ScholarPath";
    });


    
});

document.addEventListener('DOMContentLoaded', () => {
    const logosContainer = document.querySelector('.logos');
    const logos = logosContainer.innerHTML;
    logosContainer.innerHTML += logos; // Duplicate logos for infinite loop effect
    
    const totalLogosWidth = logosContainer.scrollWidth;
    const logosWidth = logosContainer.firstElementChild.clientWidth;
    
    let startTime = null;
    const duration = 100000; // 20 seconds

    function scrollLogos(timestamp) {
        if (!startTime) startTime = timestamp;
        const elapsed = timestamp - startTime;
        
        const progress = elapsed / duration;
        const translateX = totalLogosWidth * progress;
        
        logosContainer.style.transform = `translateX(${-translateX}px)`;

        if (elapsed < duration) {
            requestAnimationFrame(scrollLogos);
        } else {
            startTime = null; // Reset start time to loop again
            logosContainer.style.transform = `translateX(0)`;
            requestAnimationFrame(scrollLogos);
        }
    }

    requestAnimationFrame(scrollLogos);
});

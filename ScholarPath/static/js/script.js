
document.addEventListener("DOMContentLoaded", function () {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
                    if (entry.isIntersecting) {
                        const pairIndex = Math.floor(index / 2);
                        entry.target.style.animation = `fadeInUp 0.5s forwards ${pairIndex * 0.5}s`;
                    }
                });
            }, {
                threshold: 0.1
            });

    document.querySelectorAll('.title, .subtitle, .service').forEach((element, index) => {
        observer.observe(element);
    });
});

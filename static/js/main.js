document.addEventListener('DOMContentLoaded', () => {
    // Register GSAP ScrollTrigger
    gsap.registerPlugin(ScrollTrigger);

    // 1. Hero Cinematic Animation
    // Image scales down and text fades out slightly as we scroll away
    gsap.to('.hero-product-img', {
        scrollTrigger: {
            trigger: '.hero-cinematic',
            start: 'top top',
            end: 'bottom top',
            scrub: 1 // smooth scrubbing
        },
        scale: 0.8,
        y: 100,
        opacity: 0.5
    });

    gsap.to('.hero-content', {
        scrollTrigger: {
            trigger: '.hero-cinematic',
            start: 'top top',
            end: 'center top',
            scrub: 1
        },
        y: -50,
        opacity: 0
    });

    // 2. Bento Box Reveals
    // Each bento row fades and slides up beautifully as it enters the viewport
    const bentoRows = document.querySelectorAll('.bento-row');
    
    bentoRows.forEach((row) => {
        gsap.fromTo(row, 
            {
                opacity: 0,
                y: 100,
                scale: 0.95
            },
            {
                scrollTrigger: {
                    trigger: row,
                    start: 'top 85%', // Trigger when top of row hits 85% of viewport
                    end: 'bottom center',
                    toggleActions: 'play none none reverse' // play on enter, reverse on leave back
                },
                opacity: 1,
                y: 0,
                scale: 1,
                duration: 1.2,
                ease: 'power3.out'
            }
        );
    });

    // 3. Image Parallax inside Bento Boxes
    // Make images move slightly faster than the box for depth
    const bentoImages = document.querySelectorAll('.bento-img');
    
    bentoImages.forEach((img) => {
        gsap.to(img, {
            scrollTrigger: {
                trigger: img.parentElement,
                start: 'top bottom',
                end: 'bottom top',
                scrub: 1.5
            },
            y: -30,
            ease: 'none'
        });
    });

    // 4. Database Products Animation
    // Stagger fade-up for dynamically loaded products
    const dbProducts = document.querySelectorAll('.bento-small');
    
    if (dbProducts.length > 0) {
        gsap.fromTo(dbProducts, 
            {
                opacity: 0,
                y: 50,
                scale: 0.95
            },
            {
                scrollTrigger: {
                    trigger: '.db-products-section',
                    start: 'top 80%',
                    toggleActions: 'play none none reverse'
                },
                opacity: 1,
                y: 0,
                scale: 1,
                duration: 0.8,
                stagger: 0.15,
                ease: 'power3.out'
            }
        );
        
        // Text reveal for the section title
        gsap.fromTo('.text-reveal-trigger h2',
            {
                opacity: 0,
                y: 30
            },
            {
                scrollTrigger: {
                    trigger: '.text-reveal-trigger',
                    start: 'top 85%',
                    toggleActions: 'play none none reverse'
                },
                opacity: 1,
                y: 0,
                duration: 1,
                ease: 'power3.out'
            }
        );
    }
});

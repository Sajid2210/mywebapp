import Lenis from 'lenis';
import Swiper from 'swiper';
import { Navigation, Pagination, Autoplay, Thumbs, } from 'swiper/modules';
import { Power2, gsap } from "gsap";
import { ScrollTrigger } from "gsap/all";
import SplitType from 'split-type';
import Splitting from "splitting";
import GLightbox from 'glightbox';
import VanillaTilt from 'vanilla-tilt';

document.addEventListener("DOMContentLoaded", function () {

    // Initialize Lenis for smooth scrolling
    // const lenis = new Lenis({ smooth: true, duration: 2, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) });
    // function raf(time) {
    //     lenis.raf(time);
    //     requestAnimationFrame(raf);
    // }
    // requestAnimationFrame(raf);

    // Initialize splitting
    Splitting();

    // Initialize Glightbox
    GLightbox({
        selector: '.video-popup'
    });
    GLightbox({
        selector: '.product-popup-box'
    });
    GLightbox({
        selector: '.post-img-popup'
    });
    GLightbox({
        selector: '.review-img-gallery'
    });

    // Initialize Swipers
    const initSwiper = (selector, config) => {
        const element = document.querySelector(selector);
        if (element) {
            return new Swiper(element, config);
        }
        return null;
    };


    // Hero slider
    initSwiper('.hero-swiper', {
        modules: [Autoplay, Navigation],
        slidesPerView: 1,
        spaceBetween: 24,
        loop: true,
        speed: 1000,
        autoplay: { delay: 6000, },
        effect: 'fade',
        fadeEffect: {
            crossFade: true
        },
        navigation: { nextEl: '.hero-swiper-next', prevEl: '.hero-swiper-prev' },
    });

    // text slider
    initSwiper('.text-slider', {
        modules: [Autoplay],
        slidesPerView: 'auto',
        loop: true,
        speed: 6000,
        spaceBetween: 16,
        autoplay: { delay: 1, },
        breakpoints: {
            575: {
                spaceBetween: 24,
            },
        }
    });

    // best product slider
    initSwiper('.best-product-slider', {
        modules: [Autoplay, Pagination],
        slidesPerView: 1.1,
        spaceBetween: 24,
        loop: true,
        speed: 1000,
        autoplay: { delay: 6000, },
        centeredSlides: true,
        pagination: { el: ".best-product-pagination", clickable: true },
        breakpoints: {
            576: {
                slidesPerView: 1.5,
            },
            768: {
                slidesPerView: 2,
            },
            992: {
                slidesPerView: 2.5,
            },
            1400: {
                slidesPerView: 3.5,
            },
        }
    });

    // brand slider
    initSwiper('.brand-slider', {
        modules: [Autoplay],
        slidesPerView: 'auto',
        spaceBetween: 24,
        loop: true,
        speed: 6000,
        autoplay: { delay: 1, },
        breakpoints: {
            1200: {
                spaceBetween: 40,
            },
            1400: {
                spaceBetween: 60,
            },
            1600: {
                spaceBetween: 80,
            }
        }
    });

    // gallery slider
    initSwiper('.gallery-slider', {
        modules: [Autoplay],
        slidesPerView: 'auto',
        loop: true,
        speed: 6000,
        autoplay: { delay: 1, },
    });

    // move with us slider
    initSwiper('.move-with-us-slider', {
        modules: [Autoplay, Navigation],
        slidesPerView: 1.1,
        spaceBetween: 24,
        loop: true,
        speed: 1000,
        autoplay: { delay: 6000, },
        centeredSlides: true,
        navigation: { nextEl: '.move-swiper-next', prevEl: '.move-swiper-prev' },
        breakpoints: {
            576: {
                slidesPerView: 1.5,
            },
            768: {
                slidesPerView: 2,
            },
            992: {
                slidesPerView: 2.5,
            },
            1400: {
                slidesPerView: 3.5,
            },
        }
    });


    // Hero 2 slider 
    initSwiper('.hero-2-swiper', {
        modules: [Autoplay, Navigation],
        slidesPerView: 1,
        loop: true,
        speed: 1000,
        autoplay: { delay: 6000 },
        navigation: { nextEl: '.hero-2-swiper-next', prevEl: '.hero-2-swiper-prev' },
        on: {
            slideChangeTransitionStart: function () {
                const currentSlide = this.slides[this.activeIndex];
                const tl = gsap.timeline();
                tl.fromTo(currentSlide.querySelector('.slider__image:nth-child(1)'), { x: '5vw' }, { x: '0%', duration: 1.5, ease: Power2.easeOut },)
                    .fromTo(currentSlide.querySelector('.slider__image:nth-child(2)'), { x: '11vw' }, { x: '0%', duration: 1.5, ease: Power2.easeOut }, '-=1.5')
                    .fromTo(currentSlide.querySelector('.slider__image:nth-child(3)'), { x: '-7vw' }, { x: '0%', duration: 1.5, ease: Power2.easeOut }, '-=1.5')
                    .fromTo(currentSlide.querySelector('.slider__image:nth-child(4)'), { x: '13vw' }, { x: '0%', duration: 1.5, ease: Power2.easeOut }, '-=1.5')
                    .fromTo(currentSlide.querySelector('.slider__image:nth-child(5)'), { x: '-9vw' }, { x: '0%', duration: 1.5, ease: Power2.easeOut }, '-=1.5');
            }
        }
    });

    // text slider
    initSwiper('.text-slider-2', {
        modules: [Autoplay],
        direction: 'vertical',
        slidesPerView: 'auto',
        spaceBetween: 24,
        loop: true,
        speed: 6000,
        autoplay: { delay: 1, },
    });

    // team slider
    initSwiper('.team-slider', {
        modules: [Autoplay, Navigation],
        slidesPerView: 1.5,
        spaceBetween: 24,
        loop: true,
        speed: 1000,
        autoplay: { delay: 6000, },
        navigation: { nextEl: '.team-swiper-next', prevEl: '.team-swiper-prev' },
        breakpoints: {
            480: {
                slidesPerView: 2,
            },
            576: {
                slidesPerView: 2.5,
            },
            768: {
                slidesPerView: 3,
            },
            992: {
                slidesPerView: 3.5,
            },
            1400: {
                slidesPerView: 4.5,
            },
        }
    });


    // product slider
    let productThumb = initSwiper('.swiper-thumb', {
        modules: [Thumbs, Navigation],
        slidesPerView: 3.5,
        spaceBetween: 10,
        navigation: {
            nextEl: '.thumb-next',
            prevEl: '.thumb-prev',
        }
    });

    initSwiper('.product-swiper', {
        modules: [Thumbs],
        slidesPerView: 1,
        spaceBetween: 0,
        thumbs: {
            swiper: productThumb,
        }
    });

    // you also like
    initSwiper('.you-also-like', {
        modules: [Autoplay, Pagination],
        slidesPerView: 1,
        spaceBetween: 24,
        autoHeight: true,
        loop: true,
        speed: 1000,
        autoplay: { delay: 6000, },
        pagination: { el: '.you-also-like-pagination', clickable: true },
        breakpoints: {
            768: {
                slidesPerView: 2,
            },
        }
    });

    // initialize VanillaTilt
    const cardTilt = document.querySelectorAll('.card-tilt')
    if (cardTilt) {
        VanillaTilt.init(cardTilt, {
            max: 5,
            speed: 500,
            glare: true,
            "max-glare": 0.3,
            perspective: 1500,
        })
    }

    // gsap
    // Register GSAP plugins
    gsap.registerPlugin(ScrollTrigger,);

    // Image reveal animation
    const revealAnimation = (selector, axis, itemPercent, imgPercent, scale) => {
        gsap.utils.toArray(selector).forEach(revealItem => {
            const image = revealItem.querySelector("img");
            const tl = gsap.timeline({
                scrollTrigger: {
                    trigger: revealItem,
                    toggleActions: "play none none reverse",
                    markers: false
                }
            });
            tl.set(revealItem, { autoAlpha: 1 })
                .from(revealItem, 1.5, { [`${axis}Percent`]: itemPercent, ease: Power2.out })
                .from(image, 1.5, { [`${axis}Percent`]: imgPercent, scale, delay: -1.5, ease: Power2.out });
        });
    };

    revealAnimation(".reveal-left", 'x', -100, 100, 1.3);
    revealAnimation(".reveal-bottom", 'y', -100, 100, 1.3);
    revealAnimation(".reveal-scale", 'x', 100, -100, 1.3);


    // Title animation
    const splitAndAnimate = (selector, splitType, child, triggerStart, staggerDelay) => {
        gsap.utils.toArray(selector).forEach(title => {
            new SplitType(title, { types: splitType });
            const elements = title.querySelectorAll(`.${child}`);
            elements.forEach((el, index) => {
                gsap.timeline({
                    scrollTrigger: {
                        trigger: el,
                        start: `top ${triggerStart}%`,
                        end: "bottom 60%",
                        scrub: false,
                        toggleActions: "play none none reverse"
                    }
                }).from(el, {
                    duration: 0.8,
                    x: 70,
                    delay: index * staggerDelay,
                    autoAlpha: 0
                });
            });
        });
    };

    splitAndAnimate(".text-animation-line", "lines", "line", 100, 0.03);
    splitAndAnimate(".text-animation-word", "words", "word", 100, 0.01);


    // Animate elements on scroll
    ScrollTrigger.batch(".animate-box", {
        onEnter: elements => {
            gsap.from(elements, {
                autoAlpha: 0,
                y: 60,
                stagger: 0.15,
            });
        },
        once: true,
    });
    // ScrollTrigger.batch(".animate-box", {
    //     onEnter: elements => {
    //         gsap.from(elements, {
    //             autoAlpha: 1,
    //             y: 100,
    //             stagger: 0.15,
    //             duration: 0.6,
    //             ease: "power3.out",
    //             scrollTrigger: {
    //                 trigger: elements,
    //                 start: "top 90%",
    //                 end: "bottom 10%",
    //                 toggleActions: "play none none reverse",
    //                 markers: true
    //             }
    //         });
    //     },
    // });

    const blogWrapper = document.querySelector('.news-and-articles-wrapper')
    let blogCardItem = document.querySelectorAll('.news-and-articles-card')

    blogCardItem.forEach((item) => {

        const txt = item.querySelector('.card-body')
        const thumb = item.querySelector('.card-thumb')
        const img = thumb.querySelector('img')
        const overlay = item.querySelector('.overlay')
        const hit = item.querySelector('.hit')


        item.onpointerenter = (e) => {
            gsap.to(thumb, { boxShadow: 'rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px', duration: 0.3, ease: 'power2.out' });
            gsap.to(img, { duration: 0.3, scale: 1.3, overwrite: 'auto', ease: 'back' })
            gsap.to([thumb, txt], { ease: 'power3', yPercent: (i) => [-6, 2][i], overwrite: 'auto' })
            gsap.to([hit], { duration: 0.7, x: 0, y: 0, yPercent: 0, ease: 'elastic.out(0.8)', overwrite: 'auto' })
            gsap.to(overlay, { duration: 0.7, ease: 'power2', x: 0, y: 0, overwrite: 'auto', opacity: 0.5 })
        }

        item.onpointermove = (e) => {
            const xp = gsap.utils.interpolate(-40, 20, e.offsetX / 500)
            const yp = gsap.utils.interpolate(-40, 40, e.offsetY / 400)
            gsap.to(overlay, { duration: 0.7, ease: 'power2', x: xp * 4, y: yp * 4 })
            gsap.to([hit, thumb], { duration: 0.7, ease: 'power2', x: xp, y: yp })
            gsap.to([img], { duration: 0.7, ease: 'power2', x: -xp / 1.3, y: -yp / 1.3 })
            gsap.to(txt, { duration: 0.7, x: xp, y: yp })
        }

        item.onpointerleave = (e) => {
            gsap.to(thumb, { boxShadow: 'none', duration: 0.3, ease: 'power2.out' });
            gsap.to(overlay, { opacity: 0, x: 0, y: 0, overwrite: 'auto' })
            gsap.to(img, { duration: 0.3, scale: 1, x: 0, y: 0, overwrite: 'auto' })
            gsap.to([hit, thumb, txt], { duration: 0.7, x: 0, y: 0, yPercent: 0, ease: 'elastic.out(0.8)', overwrite: 'auto' })
        }

        // stagger reveal
        gsap.timeline()
            .to(blogWrapper, { opacity: 1 })
            .from(item, { x: innerWidth, skewX: 20, stagger: 0.2, duration: 1, ease: 'elastic.out(0.3)' }, 0.4)
            .from(txt, { x: innerWidth, stagger: 0.2, duration: 1, ease: 'elastic.out(0.2)' }, 0.44)
            .set(blogWrapper, { pointerEvents: 'auto' }, 1)//enable mouse interaction
    })

})
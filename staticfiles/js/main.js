// MENU
const mobileMenu = document.querySelector(".header__mob");
const mobileButton = document.querySelector(".header__menu.link__hover");
const logoLink = document.querySelector('.header__logo');

const menuItemZero = document.querySelector("#menu-item-0");
const menuItemOne = document.querySelector("#menu-item-1");
const menuItemTwo = document.querySelector("#menu-item-2");
const menuItemThree = document.querySelector("#menu-item-3");
const menuItemFour = document.querySelector("#menu-item-4");
const menuItemFive = document.querySelector("#menu-item-5");

const menuLinkZero = document.querySelector("#menu-link-zero");
const menuLinkOne = document.querySelector("#menu-link-one");
const menuLinkTwo = document.querySelector("#menu-link-two");
const menuLinkThree = document.querySelector("#menu-link-three");
const menuLinkFour = document.querySelector("#menu-link-four");
const menuLinkFive = document.querySelector("#menu-link-five");

function toggleReveal() {
    menuItemZero.classList.toggle('reveal');
    menuItemOne.classList.toggle('reveal');
    menuItemTwo.classList.toggle('reveal');
    menuItemThree.classList.toggle('reveal');
    menuItemFour.classList.toggle('reveal');
    menuItemFive.classList.toggle('reveal');
}

function toggleMobileMenu() {
    mobileButton.classList.toggle('link__hover_active');
    if(mobileButton.textContent === "menu"){
        mobileButton.textContent = "close";
    } else {
        mobileButton.textContent = "menu";
    }
    mobileMenu.classList.toggle('active');
    document.body.classList.toggle('fixed');
    toggleReveal();
}

logoLink.addEventListener('click', () => {
    mobileMenu.classList.remove('active');
    mobileButton.classList.remove('link__hover_active');
    document.body.classList.remove('fixed');
    menuItemZero.classList.remove('reveal');
    menuItemOne.classList.remove('reveal');
    menuItemTwo.classList.remove('reveal');
    menuItemThree.classList.remove('reveal');
    menuItemFour.classList.remove('reveal');
    menuItemFive.classList.remove('reveal');
});

mobileButton.addEventListener('click', () =>{
    toggleMobileMenu();
});

menuLinkZero.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkZero.classList.toggle('reveal');
});

menuLinkOne.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkOne.classList.toggle('reveal');
});

menuLinkTwo.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkTwo.classList.toggle('reveal');
});

menuLinkThree.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkThree.classList.toggle('reveal');
});

menuLinkFour.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkFour.classList.toggle('reveal');
});

menuLinkFive.addEventListener('click', () => {
    toggleMobileMenu();
    menuLinkFive.classList.toggle('reveal');
});

const servicesInput = document.getElementById("services-drop-down");
const arrowDownServices = document.getElementById("arrow-down-services");
const selectionContainerServices = document.getElementById("container-services");

if (servicesInput && arrowDownServices && selectionContainerServices) {
    servicesInput.addEventListener('click', () => {
        selectionContainerServices.classList.toggle("open-selection");
        arrowDownServices.classList.toggle("open-arrow");
    });
}

const socialInput = document.getElementById("social-drop-down");
const arrowDownSocials = document.getElementById("arrow-down-socials");
const selectionContainerSocials = document.getElementById("container-socials");
if (socialInput && arrowDownSocials && selectionContainerSocials) {
    socialInput.addEventListener('click', () => {
        selectionContainerSocials.classList.toggle("open-selection");
        arrowDownSocials.classList.toggle("open-arrow");
    });
}

// Open a light box for images
function openLightbox(imgSrc) {
    document.getElementById('lightbox-img').src = imgSrc;
    document.getElementById('lightbox').classList.add('show');
    document.getElementById('lightbox').addEventListener('click', handleLightboxClick);
}

function closeLightbox() {
    document.getElementById('lightbox').classList.remove('show');
    document.getElementById('lightbox').removeEventListener('click', handleLightboxClick);
}

function handleLightboxClick(event) {
    if (event.target === document.getElementById('lightbox') || event.target.classList.contains('close')) {
        closeLightbox();
    }
}

// Play and Stop video on Project page
let currentVideo = null;

function togglePlayPause(videoId) {
    const video = document.getElementById(`video_${videoId}`);
    const playButton = document.getElementById(`play_button_${videoId}`);

    if (currentVideo !== video && currentVideo !== null && !currentVideo.paused) {
        currentVideo.pause();
        const prevPlayButton = document.querySelector(`#play_button_${currentVideo.id.split('_')[1]}`);
        prevPlayButton.style.display = 'block';
    }

    video.addEventListener('click', () => {
        if (currentVideo === video && video.click) {
            video.pause();
            playButton.style.display = 'block';
            currentVideo = video.paused ? null : video;
        }
    })

    if (video.paused) {
        video.play();
        playButton.style.display = 'none';
        currentVideo = video.paused ? null : video;
    }
}


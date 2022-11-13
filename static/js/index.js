// Change favicon with theme
lightSchemeIcon = document.querySelector("link#fav-green");
darkSchemeIcon = document.querySelector("link#fav-white");

function onUpdate() {
  if (matcher.matches) {
    lightSchemeIcon.remove();
    document.head.append(darkSchemeIcon);
  } else {
    document.head.append(lightSchemeIcon);
    darkSchemeIcon.remove();
  }
}

matcher = window.matchMedia("(prefers-color-scheme: dark)");
matcher.addListener(onUpdate);
onUpdate();

// LOGIN MODAL
// let loginModal = document.querySelector(".login-modal");

function hideLoginModal() {
  let loginModal = document.querySelector(".login-modal");
  loginModal.style.display = "none";
}
function showLoginModal() {
  let loginModal = document.querySelector(".login-modal");
  loginModal.style.display = "block";
}

//  Password Reset Modal
// function hideResetModal() {
//   let resetModal = document.querySelector(".reset-password-modal");
//   resetModal.style.display = "none";
// }
// function showResetModal() {
//   let resetModal = document.querySelector(".reset-password-modal");
//   resetModal.style.display = "block";
// }

// MOBILE MENU
const menu = document.querySelector(".mobile_menu");
const openMenuBtn = document.querySelector(".hamburger");
const closeMenuBtn = document.querySelector(".hamburger_close");

openMenuBtn.onclick = () => {
  menu.classList.add("showMenu");
  document.querySelector(".mobile_search").style.display = "none";
  openMenuBtn.style.display = "none";
  closeMenuBtn.style.display = "block";
};

closeMenuBtn.onclick = () => {
  menu.classList.remove("showMenu");
  document.querySelector(".mobile_search").style.display = "block";
  openMenuBtn.style.display = "flex";
  closeMenuBtn.style.display = "none";
};

// MOBILE MENU SUBSCRIBE BUTTON ACTION
function subscribeMobile() {
  menu.classList.remove("showMenu");
  document.querySelector(".mobile_search").style.display = "block";
  openMenuBtn.style.display = "flex";
  closeMenuBtn.style.display = "none";
  window.location.href = "#subscribe";
}

// PASSWORD SHOW/HIDE   ||
function passwordToggle() {
  // console.log("why");
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
    document.querySelector(".bi-eye").style.display = "none";
    document.querySelector(".bi-eye-slash").style.display = "block";
    // x.classList.remove("bi-eye");
    // x.classList.add("bi-eye-slash");
  } else {
    x.type = "password";
    document.querySelector(".bi-eye").style.display = "block";
    document.querySelector(".bi-eye-slash").style.display = "none";
  }
}

// close contact us form pop up
function closeContactPopup() {
  let contactModal = document.querySelector(".msg_sent_pop_up");
  contactModal.style.display = "none";
}

// HIDE TOP BANNER ON SCROLL DOWN
// var lastScrollTop;
// topBanner = document.querySelector(".nav_outer");
// window.addEventListener("scroll", function () {
//   var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
//   if (scrollTop > lastScrollTop) {
//     topBanner.style.opacity = "0";
//   } else {
//     topBanner.style.opacity = "1";
//   }
//   lastScrollTop = scrollTop;
// });
// var prevScrollpos = window.pageYOffset;
// window.onscroll = function () {
//   var currentScrollPos = window.pageYOffset;
//   if (prevScrollpos > currentScrollPos) {
//     document.querySelector(".nav_outer").style.opacity = "0";
//   } else {
//     document.querySelector(".nav_outer").style.opacity = "1";
//   }
//   prevScrollpos = currentScrollPos;
// };

//--------------- Dark Bright Theme ---------------------//

const sun = document.getElementById("sun-icon");
const moon = document.getElementById("moon-icon");
const body = document.getElementsByTagName("body")[0];
const introText = document.querySelector("#intro p");
function darkMode() {
  sun.style.display = "none";
  moon.style.display = "block";
  body.classList.toggle("body-dark");
  introText.style.color = "#EEEFF1";
}

function lightMode() {
  sun.style.display = "block";
  moon.style.display = "none";
  body.classList.toggle("body-dark");
  introText.style.color = "#3c404a";
}

// ----------- Success & Error Alerts -------

    window.addEventListener("load", function () {
        const errorMessage = document.getElementById("success-alert");
        if (errorMessage !== null) {
          errorMessage.style.display = "block";
          setTimeout(function () {
            errorMessage.style.display = "none";
          }, 2000);
        }
      });
      
      window.addEventListener("load", function () {
        const errorMessage = document.getElementById("error-alert");
        if (errorMessage !== null) {
          errorMessage.style.display = "block";
          setTimeout(function () {
            errorMessage.style.display = "none";
          }, 2000);
        }
      });



// --------- Modal -----------
document.addEventListener('DOMContentLoaded', function() {
  const openButtons = document.querySelectorAll('.link-button');
  const modalContainers = document.querySelectorAll('.modal-container');
  const closeIcons = document.querySelectorAll('.fa-close');
  const closeButtons = document.querySelectorAll('.btn-close');

  openButtons.forEach((button, index) => {
    button.addEventListener('click', function() {
      modalContainers[index].classList.add('show');
    });
  });

  closeIcons.forEach((icon, index) => {
    icon.addEventListener('click', function() {
      modalContainers[index].classList.remove('show');
    });
  });

  closeButtons.forEach((button, index) => {
    button.addEventListener('click', function() {
      modalContainers[index].classList.remove('show');
    });
  });
});

const graphBtn = document.querySelector(".graph-fold");
const graphWrapDiv = document.querySelector(".graph-wrap");

graphBtn.addEventListener("click", () => {
  graphWrapDiv.classList.toggle("graph-none");
});

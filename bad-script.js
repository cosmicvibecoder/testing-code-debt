// bad JS that assumes DOM elements and has syntax errors

function init() {
  const el = document.getElementById('non-existent')
  el.innerHTML = "<p>Oops</p>"
  console.log("Initialized")
}

init(;
// document.getElementById("datetime").innerHTML = Date();
function docReady(fn) {
  // see if DOM is already available
  if (
    document.readyState === "complete" ||
    document.readyState === "interactive"
  ) {
    // call on next available tick
    setTimeout(fn, 1);
  } else {
    document.addEventListener("DOMContentLoaded", fn);
  }
}

function onLogin() {
  var x = document.getElementById("login_password").value;
  var hash = md5(x);
  document.getElementById("login_password").value = hash;
}

function hiddenOverlay() {
  document.getElementById("overlay").style.display = "none";
}

function displayOverlay() {
  document.getElementById("overlay").style.display = "block";
}

function hiddenLoginDiv() {
  document.getElementById("wrapbox").style.display = "none";
  document.getElementById("active").innerHTML = "登录";
  document.getElementById("active").style.fontWeight = "bold";
  document.getElementById("active").href = "javascript:displayLoginDiv()";
  hiddenOverlay();
}

function displayLoginDiv() {
  document.getElementById("wrapbox").style.display = "block";
  document.getElementById("active").innerHTML = "隐藏";
  document.getElementById("active").style.fontWeight = "bold";
  document.getElementById("active").href = "javascript:hiddenLoginDiv()";
  displayOverlay();
  displayLoginTab();
}

document.addEventListener("keydown", function (e) {
  if (e.key == "Escape") {
    // 目前无论何时按Esc都是安全的
    hiddenLoginDiv();
  }
});

document.onclick = function (e) {
  var a;
  if (e.srcElement) a = e.srcElement.getAttribute("class");
  else a = e.target.getAttribute("class");
  // window.alert(a);
  // if (a != null) window.alert(a.search("wrap"));
  if (a == null || a.search("wrap") == -1) hiddenLoginDiv();
};

function displayLoginTab() {
  document.getElementsByClassName("wrap input")[0].placeholder = "昵称";
  document.getElementById("loginTab").style.fontWeight = "bold";
  document.getElementById("loginTab").style.color = "#515151";
  document.getElementById("registerTab").style.fontWeight = "normal";
  document.getElementById("registerTab").style.color = "#9d9d9d";
}

function onDebug() {
  x = document.getElementById("debugAction");
  if (x != null) x.style.display = "block";
}

function offDebug() {
  x = document.getElementById("debugAction");
  if (x != null) x.style.display = "none";
}

function show_mryw() {
  document.getElementsByClassName("item-8")[0].innerHTML =
    '<object type="text/html" data="mryw1.html"></object>';
}

init = function () {
  // DOM is loaded and ready for manipulation here
  onDebug();
  offDebug();
};

docReady(init);


let tg = window.Telegram.WebApp;
let reserve = document.getElementById("reserve");
let buy = document.getElementById("buy");
let main = document.getElementById("main");
let form = document.getElementById("form");
let user_name = document.getElementById("user_name");
let user_phone = document.getElementById("user_phone");
let first_name = tg.InitDataUnsafe.user.first_name;
let last_name = tg.InitDataUnsafe.user.last_name;

buy.addEventListener("click", () => {
    main.style.display = "none";
    form.style.display = "block";
    user_name.value = first_name + last_name;

})

ondragover.addEventListener("click", () => {
    tg.close();
})
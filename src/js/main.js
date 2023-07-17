
let tg = window.Telegram.WebApp;
let reserve = document.getElementById("reserve");
let order = document.getElementById("order");
let main = document.getElementById("main");
let form = document.getElementById("form");
let user_name = document.getElementById("user_name");
let user_phone = document.getElementById("user_phone");
let first_name = tg.InitDataUnsafe.user.first_name;
let last_name = tg.InitDataUnsafe.user.last_name;

reserve.addEventListener("click", () => {
    main.style.display = "none";
    form.style.display = "block";
    user_name.value = first_name + last_name;
})

order.addEventListener("click", () => {
    tg.close();
})
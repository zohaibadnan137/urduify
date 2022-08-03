const fromText = document.querySelector(".from-text"),
    toText = document.querySelector(".to-text"),
    exchageIcon = document.querySelector(".exchange"),
    selectTag = document.querySelectorAll("select");
translateBtn = document.querySelector("button"),

    selectTag.forEach((tag, id) => {
        for (let language_code in languages) {
            let selected = id == 0 ? language_code == "ru" ? "selected" : "" : language_code == "u" ? "selected" : ""; // Set default translation direction (Roman Urdu to Urdu)
            let option = `<option ${selected} value="${language_code}">${languages[language_code]}</option>`;
            tag.insertAdjacentHTML("beforeend", option);
        }
    });

// Event listener for exchange button 
exchageIcon.addEventListener("click", () => {
    let tempText = fromText.value,
        tempLang = selectTag[0].value;
    fromText.value = toText.value;
    toText.value = tempText;
    selectTag[0].value = selectTag[1].value;
    selectTag[1].value = tempLang;
});

fromText.addEventListener("keyup", () => {
    if (!fromText.value) {
        toText.value = "";
    }
});

// Event listener for translate button 
translateBtn.addEventListener("click", () => {
    let text = fromText.value.trim(),
        translateFrom = selectTag[0].value,
        translateTo = selectTag[1].value;
    if (!text) return;

    toText.setAttribute("placeholder", "Translating...");
    let apiUrl = `http://127.0.0.1:5000/translate?text=${text}&from_lang=${translateFrom}&to_lang=${translateTo}`; // API call
    fetch(apiUrl).then(res => res.json()).then(data => {
        toText.value = data['data']
        toText.setAttribute("placeholder", "Translation");
    });
});


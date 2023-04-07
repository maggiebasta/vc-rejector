const apiHost = "http://127.0.0.1:5050";
const credentials = "admin:d6#gk0REN35l";

const composeEmail = async target => {

    // get message box object
    const composer = Array.from(
        document.getElementsByClassName("Bk")
    ).filter(composer => composer.contains(target))[0];
    if (composer) {
        replyBox = composer.querySelector('div[aria-label="Message Body"]');
        if (replyBox) {
            replyBox.innerHTML = "⏳ Generating ⏳";
        } else {
            console.error('replyBox is null or not found');
        }
    } else {
        console.error('composer is null or not found');
    }

    // get previous email content
    const prev_email = document.getElementsByClassName("ii")[0].innerText;

    const headers = new Headers({
        "Authorization": `Basic ${btoa(unescape(encodeURIComponent(credentials)))}`
    });
    headers.append("Content-Type", "application/json")

    // generate response
    let resp_email = {}
    try {
        const r = await fetch(`${apiHost}/email`, {
            method: "POST",
            headers: headers,
            body: JSON.stringify({prev_email, resp_email})
        });
        if (!r.ok) {
            throw "Unable to generate email: please check if GPT access is operational";
        }
        resp_email = await r.json();
    } catch (e) {
        alert(e);
        return;
    }
    let email = resp_email.email.split(/\n+/).map(
        paragraph => `<div>${paragraph}</div>`)
    .join("<div><br></div>");
    replyBox.innerHTML = email
};

const checkForComposer = setInterval(_ => {
    const menus = Array.from(document.getElementsByClassName("J-M Gj jQjAxd"));
    if (menus) {
        menus.forEach(menu => {
            if (menu.getAttribute("ready")) {
                return;
            }
            const sep = document.createElement("div");
            sep.setAttribute("class", "J-Kh");
            sep.setAttribute("role", "separator");
            menu.prepend(sep);
            const button = document.createElement("div");
            button.setAttribute("class", "J-N");
            button.setAttribute("role", "menuitem");
            button.addEventListener("mouseover", _ => button.setAttribute("class", "J-N J-N-Je J-N-JT"));
            button.addEventListener("mouseout", _ => button.setAttribute("class", "J-N"));
            button.addEventListener("click", e => composeEmail(e.target));
            const label = document.createElement("div");
            label.setAttribute("class", "J-N-Jz");
            label.append("Reject This VC");
            button.append(label);
            menu.prepend(button);
            menu.setAttribute("ready", true);
        });
    }
}, 100);
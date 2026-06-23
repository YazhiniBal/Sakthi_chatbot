function handleKey(event){

    if(event.key==="Enter"){
        askBot();
    }

}

function askBot(){

    let question=document.getElementById("question").value;

    if(question===""){
        return;
    }

    let chat=document.getElementById("chat");

    // User message

    chat.innerHTML +=
    `
    <div class="user">
        👤 ${question}
    </div>
    `;

    // Typing animation

    chat.innerHTML +=
    `
    <div class="typing" id="typing">
        🤖 Typing...
    </div>
    `;

    chat.scrollTop=chat.scrollHeight;

    fetch("/api/ask?question="+encodeURIComponent(question))

    .then(response=>response.json())

    .then(data=>{

        document.getElementById("typing").remove();

        chat.innerHTML +=
        `
        <div class="bot">
            🤖 ${data.answer}
        </div>
        `;

        chat.scrollTop=chat.scrollHeight;

        document.getElementById("question").value="";

    });

}

function clearChat(){

    document.getElementById("chat").innerHTML=
    `
    <div class="bot">
        👋 Welcome! Ask me anything about Sakthi Sugars.
    </div>
    `;
}
function insertImage() {
    let imageLink = prompt("Введите ссылку на изображение:", "https://...");
    if (imageLink) {
        let imgTag = `<img src="${imageLink}" alt="Изображение" style="max-width: 60%; height: auto;">`; 
        document.querySelector('textarea[name="text"]').value += imgTag; 
    }
}

function bText() 
{
    let imgTag = '<b></b>';
    let textarea = document.querySelector('textarea[name="text"]'); 
    textarea.value += imgTag; 
}


function iText() 
{
        let imgTag = '<i></i>';
        let textarea = document.querySelector('textarea[name="text"]'); 
        textarea.value += imgTag; 
}


function pText() 
{
    let imgTag = '<p></p>';
    let textarea = document.querySelector('textarea[name="text"]'); 
    textarea.value += imgTag; 
}


function dText() 
{
    let imgTag = '<del></del>';
    let textarea = document.querySelector('textarea[name="text"]'); 
    textarea.value += imgTag; 
}


function enlargeButton(buttonId) {
    const button = document.getElementById(`button${buttonId}`);
    button.classList.add('enlarged');
}

function shrinkButton(buttonId) {
    const button = document.getElementById(`button${buttonId}`);
    button.classList.remove('enlarged');
}

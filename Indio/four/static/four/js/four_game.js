window.selectLetter = function(letter) {
    const blanks = document.querySelectorAll('#word-blanks button');
    let selectedLetters = '';

    // Find the first empty button and set its text to the selected letter
    const emptyButton = findEmptyButton(blanks);
    if (emptyButton) {
        setButtonValue(emptyButton, letter);
        attachButtonClickEvent(emptyButton, letter);
        selectedLetters = gatherSelectedLetters(blanks);
        checkAnswer(selectedLetters);
    }
};

window.findEmptyButton = function(buttons) {
    for (let i = 0; i < buttons.length; i++) {
        if (buttons[i].innerText === '') {
            return buttons[i];
        }
    }
    return null;
};

window.setButtonValue = function(button, value) {
    button.innerText = value;
};

window.attachButtonClickEvent = function(button, letter) {
    button.addEventListener('click', function() {
        if (this.innerText === letter) {
            this.innerText = '';
            const blanks = document.querySelectorAll('#word-blanks button');
            const selectedLetters = gatherSelectedLetters(blanks);
            checkAnswer(selectedLetters);
        }
    });
};

window.gatherSelectedLetters = function(buttons) {
    let selectedLetters = '';
    buttons.forEach(button => {
        selectedLetters += button.innerText;
    });
    return selectedLetters;
};

window.checkAnswer = function(letters) {
    const correctAnswer = '{{ current_game.correct_answer }}';
    const output = document.getElementById('output');

    if (letters === correctAnswer.replace(/\s/g, '')) {
        output.innerText = 'Correct!';
        output.style.color = 'yellow'; // Change the color to yellow
    } else {
        output.innerText = 'Incorrect!';
        output.style.color = 'red'; // Change the color to red for incorrect
    }
};

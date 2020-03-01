

//Show and hide Create tournament form

document.getElementById('button_generate').addEventListener('click', function() {
    document.getElementById('tournament_generate').style.display = 'flex';
    this.style.display = 'none';
})

document.getElementById('close_creation').addEventListener('click', function() {
    document.getElementById('tournament_generate').style.display = 'none';
    document.getElementById('button_generate').style.display = 'flex';
})



// Hide inactive tab elements

document.getElementById('user-tab').addEventListener('click', function() {
    document.getElementById('user').style.display = 'flex';
    document.getElementById('tournament').style.display = 'none';
    document.getElementById('league').style.display = 'none';
})

document.getElementById('tournament-tab').addEventListener('click', function() {
    document.getElementById('user').style.display = 'none';
    document.getElementById('tournament').style.display = 'flex';
    document.getElementById('league').style.display = 'none';
})

document.getElementById('league-tab').addEventListener('click', function() {
    document.getElementById('user').style.display = 'none';
    document.getElementById('tournament').style.display = 'none';
    document.getElementById('league').style.display = 'flex';
})
document.addEventListener('DOMContentLoaded', () => {
    const formAnalyse = document.querySelector('form[action="/analyse"]');
    const resultatAnalyse = document.querySelector('#resultat');
    const formTraduction = document.querySelector('form[action="/traduire"]');
    const resultatTraduction = document.querySelector('#resultatTraduction');
    const boutonTraduire = document.querySelector('#traduire');
    
    formAnalyse.addEventListener('submit', (e) => {
        e.preventDefault();
        const texte = e.target.querySelector('textarea[name="texte"]').value;
        fetch('/analyse', {
            method: 'POST',
            body: new URLSearchParams({ texte }),
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        })
        .then(response => response.text())
        .then(html => {
            resultatAnalyse.innerHTML = html;
        });
    });
    
    formTraduction.addEventListener('submit', (e) => {
        e.preventDefault();
        const texte = e.target.querySelector('textarea[name="texte"]').value;
        const direction = e.target.querySelector('#direction').value;
        fetch('/traduire', {
            method: 'POST',
            body: new URLSearchParams({ texte, direction }),
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        })
        .then(response => response.text())
        .then(translation => {
            resultatTraduction.innerHTML = translation;
        });
    });
});

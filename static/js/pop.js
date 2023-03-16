
    const popup=document.querySelector('.popup');
    const btn=document.querySelector('.send-btn');
    const bun=document.querySelector('.bun');

    btn.addEventListener('click', function() {
        popup.style.transform = 'translate(-50% ,-50% )';
        popup.style.visibility = 'visible'
        popup.style.top='50%'
        
    });
    bun.addEventListener('click', function() {
        popup.style.transform = 'translate(-50%,-50%,scale(0.1))';
        popup.style.visibility='hidden'
        popup.style.top='0%'
    });
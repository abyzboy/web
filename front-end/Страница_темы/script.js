window.onload = function() {
    const title = localStorage.getItem('selectedTitle'); // Получаем заголовок из localStorage
    const video = localStorage.getItem('selectedVideo');

    if (title) {
        document.getElementById('theme-title').textContent = title; // Устанавливаем заголовок на странице
    }
    
    if (video) {
        const videoSrc = "/front-end/Видео/" + video; // Путь к видео
        const videoPlayer = document.getElementById('myVideo');
        const source = videoPlayer.querySelector('source');
        source.setAttribute('src', videoSrc);
        videoPlayer.load(); // Обновляем видеоплеер
        localStorage.removeItem('selectedVideo');
    }
};

function updateContent(title, video) {
    // Обновляем заголовок
    document.getElementById('theme-title').textContent = title;

    // Обновляем видео
    const videoSrc = "/front-end/Видео/" + video;
    const videoPlayer = document.getElementById('myVideo');
    const source = videoPlayer.querySelector('source');
    source.setAttribute('src', videoSrc);
    videoPlayer.load();
}

const video = document.getElementById('myVideo');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const volumeSlider = document.getElementById('volumeSlider');
    const fullscreenBtn = document.getElementById('fullscreenBtn');

    playPauseBtn.addEventListener('click', function() {
        if (video.paused) {
            video.play();
            playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
        } else {
            video.pause();
            playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
        }
    });

    volumeSlider.addEventListener('input', function() {
        video.volume = volumeSlider.value;
    });

    fullscreenBtn.addEventListener('click', function() {
        if (video.requestFullscreen) {
            video.requestFullscreen();
        } else if (video.mozRequestFullScreen) { /* Firefox */
            video.mozRequestFullScreen();
        } else if (video.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
            video.webkitRequestFullscreen();
        } else if (video.msRequestFullscreen) { /* IE/Edge */
            video.msRequestFullscreen();
        }
    });

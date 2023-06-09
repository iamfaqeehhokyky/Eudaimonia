// Loads the YouTube IFrame Player API asynchronously
function loadYouTubeAPI() {
  var tag = document.createElement('script');
  tag.src = 'https://www.youtube.com/iframe_api';
  var firstScriptTag = document.getElementsByTagName('script')[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
}

// Created an <iframe> (video player) for each video ID
function createPlayer(videoId) {
  new YT.Player(videoId, {
    height: '100%',
    width: '100%',
    videoId: videoId,
    playerVars: {
      autoplay: 1,
      controls: 1,
      modestbranding: 1,
      rel: 0
    },
    events: {
      'onReady': onPlayerReady
    }
  });
}

// The API calls this function when the player is ready
function onPlayerReady(event) {
  // Do something when the player is ready
}

// Added click-to-play functionality to the video containers
const videoContainers = document.querySelectorAll('.click-to-play');
videoContainers.forEach((container) => {
  container.addEventListener('click', () => {
    const videoId = container.getAttribute('id');
    container.style.display = 'none';
    createPlayer(videoId);
  });
});
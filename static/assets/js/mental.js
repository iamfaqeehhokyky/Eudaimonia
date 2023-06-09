var apiKey = '{{ api_key }}';  // Retrieve the API key from Flask route

// Load the YouTube IFrame Player API asynchronously
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// Create an <iframe> (video player) for each video ID
var players = [];
function onYouTubeIframeAPIReady() {
  {% for video_id in video_ids %}
  players[{{ loop.index0 }}] = new YT.Player('player{{ loop.index }}', {
    height: '360',
    width: '640',
    videoId: '{{ video_id }}',
    playerVars: {
      modestbranding: 1,
      showinfo: 0,
      controls: 1,
      key: apiKey  // Pass the API key to the playerVars
    }
  });
  {% endfor %}
}

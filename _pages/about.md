---
permalink: /
layout: archive
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
classes: wide
---
Hi, I am Abhijeet! I study Economics and I am currently doing my PhD at the Indira Gandhi Institute of Development Research (IGIDR) in Mumbai. Before this, I completed my master's degree at CESP, JNU. 

My research focuses on network economics—basically trying to understand how human networks form, why people connect, and why those connections sometimes break. 

### My View on Research
I do not believe we can predict human behavior. We are not like physical matter—our actions are far too unpredictable. To me, trying to predict people misses the point, and if we ever fully figured people out, life would lose its charm!

What I truly enjoy is the process itself: sitting down with complex math, tweaking equations step-by-step, and working through problems until everything lands on a clean result. For me, the beauty is in doing the work, not just the final answer.

---

Outside of my main research, I am deeply interested in philosophy—especially the ideas of Albert Camus. I often spend time just sitting and reflecting, genuinely curious about where life goes next.

I also love exploring random hobbies in my free time:
* <i class="fas fa-fw fa-desktop"></i> **Tech & Linux:** Building electronics, tinkering with my PC setup, trying out different Linux Distributions, and collecting cool gadgets.
* <i class="fas fa-fw fa-dumbbell"></i> **Fitness:** Gym workouts, bodyweight training, and playing badminton.
* <i class="fas fa-fw fa-tv"></i> **Anime:** Big fan of story-driven shows like *Death Note*, *Vinland Saga*, and especially *Attack on Titan*.

---

<!-- START LISTENBRAINZ BANNER -->
<style>
  .scrobble-banner {
    display: flex;
    align-items: center;
    background: rgba(128, 128, 128, 0.08); /* Adapts perfectly to light/dark themes */
    border-left: 4px solid #eb743b; /* ListenBrainz brand orange */
    padding: 14px 20px;
    border-radius: 0 6px 6px 0;
    margin: 2em 0;
  }
  .scrobble-icon {
    font-size: 2em;
    color: #eb743b;
    margin-right: 20px;
  }
  .scrobble-details {
    display: flex;
    flex-direction: column;
    line-height: 1.4;
  }
  .scrobble-label {
    font-size: 0.75em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    opacity: 0.7;
    margin-bottom: 2px;
  }
  .scrobble-track {
    font-size: 1.05em;
    font-weight: 500;
  }
  .scrobble-track a {
    color: inherit;
    text-decoration: none;
  }
  .scrobble-track a:hover {
    text-decoration: underline;
  }
</style>

<div class="scrobble-banner">
  <div class="scrobble-icon">
    <!-- Uses the FontAwesome compact-disc icon -->
    <i id="lb-icon" class="fas fa-compact-disc"></i>
  </div>
  <div class="scrobble-details">
    <span class="scrobble-label" id="lb-label">Music Status</span>
    <span class="scrobble-track" id="lb-track">Checking ListenBrainz...</span>
  </div>
</div>
<!-- END LISTENBRAINZ BANNER -->

> "We're born free. All of us. Free. Some don't believe it, some try to take it away. To hell with them! Water like fire, mountains of ice... Lay your eyes on that, and you'll know what freedom is, that it's worth fighting for! Fight to live, risk it all for even a glimmer of real freedom!... Fight. Fight. Fight. FIGHT! FIGHT!!!"  
> — **Eren Yeager, Attack on Titan**

<script>
  // Insert your ListenBrainz username here
  const lbUsername = "thisiseren"; 
  
  const lbLabel = document.getElementById("lb-label");
  const lbTrack = document.getElementById("lb-track");
  const lbIcon = document.getElementById("lb-icon");

  const playingUrl = `https://api.listenbrainz.org/1/user/${lbUsername}/playing-now`;
  const recentUrl = `https://api.listenbrainz.org/1/user/${lbUsername}/listens?count=1`;

  // Helper function to update the DOM
  function updateBanner(label, trackName, artistName, isPlaying) {
    lbLabel.innerText = label;
    lbTrack.innerHTML = `<a href="https://listenbrainz.org/user/${lbUsername}/" target="_blank"><strong>${trackName}</strong> by ${artistName}</a>`;
    
    // Add a spinning animation to the record icon if music is live
    if (isPlaying) {
      lbIcon.classList.add("fa-spin");
      lbIcon.style.animationDuration = "3s";
    } else {
      lbIcon.classList.remove("fa-spin");
    }
  }

  fetch(playingUrl)
    .then(res => res.json())
    .then(data => {
      // 1. Check if playing right now
      if (data.payload && data.payload.listens && data.payload.listens.length > 0) {
        const track = data.payload.listens[0].track_metadata;
        updateBanner("Now Playing", track.track_name, track.artist_name, true);
      } else {
        // 2. Fallback to last played
        fetch(recentUrl)
          .then(res => res.json())
          .then(recentData => {
            if (recentData.payload && recentData.payload.listens && recentData.payload.listens.length > 0) {
              const track = recentData.payload.listens[0].track_metadata;
              updateBanner("Recently Played", track.track_name, track.artist_name, false);
            } else {
              lbTrack.innerText = "Offline";
            }
          });
      }
    })
    .catch(() => {
      lbTrack.innerText = "Unable to load data.";
    });
</script>

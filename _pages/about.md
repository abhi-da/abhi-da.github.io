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

<!-- START LIVE ACTIVITY DASHBOARD -->
<style>
  .activity-dashboard {
    background: rgba(128, 128, 128, 0.05);
    border: 1px solid rgba(128, 128, 128, 0.15);
    border-radius: 8px;
    padding: 20px;
    margin: 2em 0;
  }
  .dashboard-title {
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 1.1em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid rgba(128, 128, 128, 0.15);
    padding-bottom: 10px;
  }
  .pulse-dot {
    color: #4CAF50;
    animation: pulse 2s infinite;
    margin-right: 8px;
  }
  .activity-item {
    display: flex;
    align-items: center;
    padding: 10px 0;
  }
  .activity-item:not(:last-child) {
    border-bottom: 1px dashed rgba(128, 128, 128, 0.15);
  }
  .activity-icon {
    font-size: 1.5em;
    width: 40px;
    text-align: center;
    margin-right: 15px;
  }
  .activity-details {
    display: flex;
    flex-direction: column;
    line-height: 1.4;
  }
  .activity-label {
    font-size: 0.75em;
    font-weight: 700;
    text-transform: uppercase;
    opacity: 0.6;
  }
  .activity-text {
    font-size: 1.05em;
  }
  .activity-text a {
    color: inherit;
    text-decoration: none;
  }
  .activity-text a:hover {
    text-decoration: underline;
  }
  @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
</style>

<div class="activity-dashboard">
  <h3 class="dashboard-title"><i class="fas fa-circle pulse-dot"></i> Live Activity</h3>
  
  <!-- ListenBrainz Item -->
  <div class="activity-item">
    <div class="activity-icon" style="color: #eb743b;"><i id="lb-icon" class="fas fa-music"></i></div>
    <div class="activity-details">
      <span class="activity-label" id="lb-label">Music</span>
      <span class="activity-text" id="lb-track">Checking status...</span>
    </div>
  </div>

  <!-- Trakt Item -->
  <div class="activity-item">
    <div class="activity-icon" style="color: #ed1c24;"><i id="trakt-icon" class="fas fa-tv"></i></div>
    <div class="activity-details">
      <span class="activity-label" id="trakt-label">Watch</span>
      <span class="activity-text" id="trakt-title">Checking status...</span>
    </div>
  </div>
</div>
<!-- END LIVE ACTIVITY DASHBOARD -->

> "We're born free. All of us. Free. Some don't believe it, some try to take it away. To hell with them! Water like fire, mountains of ice... Lay your eyes on that, and you'll know what freedom is, that it's worth fighting for! Fight to live, risk it all for even a glimmer of real freedom!... Fight. Fight. Fight. FIGHT! FIGHT!!!"  
> — **Eren Yeager, Attack on Titan**

<script>
  // --- CREDENTIALS ---
  const lbUsername = "thisiseren"; 
  const traktUser = "v08503149";
  const traktClientId = "KFHSt5fLLdqTnScBJ4T2udExu0UpaX_syhFJtSAnkkU"; 

  // --- LISTENBRAINZ LOGIC ---
  const lbLabel = document.getElementById("lb-label");
  const lbTrack = document.getElementById("lb-track");
  const lbIcon = document.getElementById("lb-icon");

  function updateLb(label, trackName, artistName, isPlaying) {
    lbLabel.innerText = label;
    lbTrack.innerHTML = `<a href="https://listenbrainz.org/user/${lbUsername}/" target="_blank"><strong>${trackName}</strong> by ${artistName}</a>`;
    if (isPlaying) {
      lbIcon.classList.remove("fa-music");
      lbIcon.classList.add("fa-compact-disc", "fa-spin");
      lbIcon.style.animationDuration = "3s";
    }
  }

  fetch(`https://api.listenbrainz.org/1/user/${lbUsername}/playing-now`)
    .then(res => res.json())
    .then(data => {
      if (data.payload && data.payload.listens && data.payload.listens.length > 0) {
        const track = data.payload.listens[0].track_metadata;
        updateLb("Listening Now", track.track_name, track.artist_name, true);
      } else {
        fetch(`https://api.listenbrainz.org/1/user/${lbUsername}/listens?count=1`)
          .then(res => res.json())
          .then(recent => {
            if (recent.payload && recent.payload.listens.length > 0) {
              const track = recent.payload.listens[0].track_metadata;
              updateLb("Recently Played", track.track_name, track.artist_name, false);
            } else {
              lbTrack.innerText = "Nothing logged yet.";
            }
          });
      }
    }).catch(() => lbTrack.innerText = "Offline");

  // --- TRAKT.TV LOGIC ---
  const tLabel = document.getElementById("trakt-label");
  const tTitle = document.getElementById("trakt-title");
  const tIcon = document.getElementById("trakt-icon");

  const traktHeaders = {
    "Content-Type": "application/json",
    "trakt-api-version": "2",
    "trakt-api-key": traktClientId
  };

  function updateTrakt(label, data, isPlaying) {
    tLabel.innerText = label;
    let text = "";
    if (data.type === "movie") {
      text = `<strong>${data.movie.title}</strong> (${data.movie.year})`;
    } else if (data.type === "episode") {
      const s = data.episode.season.toString().padStart(2, '0');
      const e = data.episode.number.toString().padStart(2, '0');
      text = `<strong>${data.show.title}</strong> — S${s}E${e}`;
    }
    tTitle.innerHTML = `<a href="https://trakt.tv/users/${traktUser}" target="_blank">${text}</a>`;
    
    if (isPlaying) {
      tIcon.style.animation = "pulse 2s infinite";
    }
  }

  fetch(`https://api.trakt.tv/users/${traktUser}/watching`, { headers: traktHeaders })
    .then(res => {
      if (res.status === 204) {
        return fetch(`https://api.trakt.tv/users/${traktUser}/history?limit=1`, { headers: traktHeaders })
          .then(r => r.json())
          .then(history => {
            if (history.length > 0) updateTrakt("Recently Watched", history[0], false);
            else tTitle.innerText = "Nothing logged recently.";
          });
      } else if (res.ok) {
        return res.json().then(now => updateTrakt("Currently Watching", now, true));
      }
    }).catch(() => tTitle.innerText = "Offline");
</script>

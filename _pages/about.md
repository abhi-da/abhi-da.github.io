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
* <i class="fas fa-fw fa-music"></i> **Music:** <span id="lb-status">Checking ListenBrainz...</span>

---

> "We're born free. All of us. Free. Some don't believe it, some try to take it away. To hell with them! Water like fire, mountains of ice... Lay your eyes on that, and you'll know what freedom is, that it's worth fighting for! Fight to live, risk it all for even a glimmer of real freedom!... Fight. Fight. Fight. FIGHT! FIGHT!!!"  
> — **Eren Yeager, Attack on Titan**

<script>
  // Just change this to your actual ListenBrainz username
  const lbUsername = "thisiseren"; 
  const lbStatus = document.getElementById("lb-status");

  const playingUrl = `https://api.listenbrainz.org/1/user/${lbUsername}/playing-now`;
  const recentUrl = `https://api.listenbrainz.org/1/user/${lbUsername}/listens?count=1`;

  fetch(playingUrl)
    .then(res => res.json())
    .then(data => {
      // 1. Check if a track is actively playing right now
      if (data.payload && data.payload.listens && data.payload.listens.length > 0) {
        const track = data.payload.listens[0].track_metadata;
        lbStatus.innerHTML = `Listening to <a href="https://listenbrainz.org/user/${lbUsername}/" target="_blank"><strong>${track.track_name}</strong> by ${track.artist_name}</a> 🎵`;
      } else {
        // 2. Fallback to the most recent scrobble if nothing is playing
        fetch(recentUrl)
          .then(res => res.json())
          .then(recentData => {
            if (recentData.payload && recentData.payload.listens && recentData.payload.listens.length > 0) {
              const track = recentData.payload.listens[0].track_metadata;
              lbStatus.innerHTML = `Recently played: <a href="https://listenbrainz.org/user/${lbUsername}/" target="_blank"><strong>${track.track_name}</strong> by ${track.artist_name}</a>`;
            } else {
              lbStatus.innerHTML = "Offline";
            }
          });
      }
    })
    .catch(() => {
      lbStatus.innerHTML = "Offline";
    });
</script>

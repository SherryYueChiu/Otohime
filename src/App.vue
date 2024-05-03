<script setup lang="ts">
import { onMounted, ref } from "vue";
import AnimatedBackground from "./components/AnimatedBackground.vue";
import Swal from "sweetalert2";
import { commitHash } from "./projectVersion.json";

const semanticVersion = "1.0.0";
const fullVersion = `version: ${semanticVersion ? "v" + semanticVersion : ""}${
  commitHash ? "-" + commitHash.slice(0, 6) : ""
}`;
console.log(`version: ${fullVersion}`);

const bgm = ref<HTMLAudioElement>();
const isPlaying = ref(false);

const Toast = Swal.mixin({
  toast: true,
  position: "bottom",
  iconColor: "white",
  customClass: {
    popup: "colored-toast",
  },
  showConfirmButton: false,
  timer: 5000,
  timerProgressBar: true,
});

onMounted(() => {
  bgm.value.addEventListener("timeupdate", function () {
    var buffer = 0.44;
    if (this.currentTime > this.duration - buffer) {
      this.currentTime = 0;
      this.play();
    }
  });

  if ("mediaSession" in navigator) {
    const player = bgm.value;

    navigator.mediaSession.metadata = new MediaMetadata({
      title: "音姬",
      artist: "玥餅",
      album: "未知",
      artwork: [
        {
          src: "/images/logo/maskable_icon_x512.png",
          sizes: "512x512",
          type: "image/png",
        },
      ],
    });

    navigator.mediaSession.setActionHandler("play", () => player.play());
    navigator.mediaSession.setActionHandler("pause", () => player.pause());
    navigator.mediaSession.setActionHandler("seekbackward", (details) => {
      const skipTime = details.seekOffset || 1;
      player.currentTime = Math.max(player.currentTime - skipTime, 0);
    });

    navigator.mediaSession.setActionHandler("seekforward", (details) => {
      const skipTime = details.seekOffset || 1;
      player.currentTime = Math.min(
        player.currentTime + skipTime,
        player.duration
      );
    });

    navigator.mediaSession.setActionHandler("seekto", (details) => {
      if (details.fastSeek && "fastSeek" in player) {
        player.fastSeek(details.seekTime);
        return;
      }
      player.currentTime = details.seekTime;
    });

    navigator.mediaSession.setActionHandler("previoustrack", () => {
      player.currentTime = 0;
    });
  } else {
    Toast.fire("不支援背景播放");
  }
});

function toggleBGM() {
  const player = bgm.value;
  if (player.paused) {
    isPlaying.value = true;
    player.play();
    Toast.fire("開始");
  } else {
    isPlaying.value = false;
    player.pause();
    Toast.fire("暫停");
  }
}
</script>

<template>
  <transition name="slide-fade">
    <AnimatedBackground v-show="isPlaying"></AnimatedBackground>
  </transition>
  <div class="container" @click="toggleBGM">
    <div class="title">{{ isPlaying ? "點擊暫停音姬" : "點擊播放音姬" }}</div>
  </div>
  <audio ref="bgm" loop src="./otohime.mp3"></audio>
  <div class="version">{{ fullVersion }}</div>
</template>

<style scoped lang="scss">
.container {
  position: fixed;
  width: 100%;
  height: 100vh;
  display: grid;
  place-content: center;

  & > .title {
    color: white;
    font-size: 2em;
  }
}

.version {
  position: fixed;
  bottom: 0;
  width: 100%;
  text-align: center;
  font-size: 0.8em;
  color: #888;
  padding: 1em 0 1em;
}

.slide-fade-enter-active {
  transition: all 0.1s ease;
}
.slide-fade-leave-active {
  transition: all 1.5s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active for below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>

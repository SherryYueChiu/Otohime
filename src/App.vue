<script setup lang="ts">
import { onMounted, ref } from "vue";
import { commitHash } from "./projectVersion.json";

// print version
const semanticVersion = "2.0.0";
const fullVersion = `version: ${semanticVersion ? "v" + semanticVersion : ""}${
  commitHash ? "-" + commitHash.slice(0, 6) : ""
}`;
console.log(`version: ${fullVersion}`);
</script>

<template>
    <router-view></router-view>
  <div class="version">{{ fullVersion }}</div>
</template>

<style scoped lang="scss">
.version {
  position: fixed;
  bottom: 0;
  width: 100%;
  text-align: center;
  font-size: 0.8em;
  color: #888;
  padding: 1em 0 1em;
}
</style>

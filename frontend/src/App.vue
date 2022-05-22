<template>
  <div class="navbar">
    <Navbar/>
  </div>
  <router-view/>
</template>

<script>
import Navbar from "./components/Navbar.vue"

export default {
  components: {
    Navbar,
  }
}
</script>

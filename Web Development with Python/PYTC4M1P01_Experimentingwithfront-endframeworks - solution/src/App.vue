<script setup>
/* To use a Vue component, it can be imported in the script area of the App.vue file like: */
/* import ComponentName from './components/ComponentName.vue' */
import Heading from './components/Heading.vue'
import Copyright from './components/Copyright.vue'
import Information from './components/Information.vue'
</script>

<template>
  <h1>Coursera Vue.js Demo</h1>
  <!-- To display a Vue component, the name of the component is treated similar to an HTML tag. -->
  <Heading />
  <Information />
  <Copyright />
</template>

<style>
  /* The body will have a background of antique white and a mid-black font. */
  body {
    color: #242424;
    background-color: antiquewhite;
  }
</style>

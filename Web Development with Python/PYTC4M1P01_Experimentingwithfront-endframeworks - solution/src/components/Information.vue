<script>
  // This code defines a variable named bgColor and gives it a default value of false.
  export default {
    data() {
      return {
        bgColor: false
      };
    }
}

</script>

<template>
  <h2>Completed Vue Demo!</h2>

  <!-- Binding is a more advanced way to interact with the Document Object Model (DOM)-->
  <div v-bind:class="{ vueBg: bgColor }" class="main-info">
    <p>
      Vue.js is a progressive JavaScript framework that's garnered immense popularity for its approachable learning curve and adaptable nature. Its component-based architecture empowers developers to craft user interfaces with remarkable efficiency and maintainability. Whether you're building a small interactive widget or a full-fledged single-page application, Vue.js provides the tools and flexibility to bring your vision to life. 
      <br/>
      With its intuitive syntax, extensive documentation, and vibrant community, Vue.js is an excellent choice for developers of all skill levels.
    </p>
    <!-- Clicking the button will switch the bgColor class on and off for the current div-->
    <!-- This is the div containing the paragraph about Vue.-->
    <!-- This will give the effect of switching from a white to purple background and vice versa -->
    <button v-on:click="bgColor = !bgColor">Toggle Background Color</button>
  </div>
</template>

<style scoped>
  /* This defines a CSS class rule that has a solid border. */
  .main-info {
    border: 3px solid;
  }

  /* This defines a CSS class rule that has a background color of a light purple. */
  .vueBg{
    background-color: #CBC3E3;
  }

</style>
<template>
  <div id="app">
    <div id="top-bar">
      <h1>Riksdagen &mdash; Cheap Seats</h1>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="scss">
@import '@/styles/typography.scss';
@import '@/styles/material/color.scss';
@import '@/styles/mixins/layout.scss';

* {
  box-sizing: border-box;
  &:after, &:before {
    box-sizing: border-box;
  }
}

body {
  margin: 0;
}

#top-bar {
  @include contained();
  padding-top: 100px;
  padding-bottom: 20px;
  background: mcolor('yellow', '500');
  border-bottom: 12px solid mcolor('yellow', '300');
  h1 {
    margin: 0;
  }
}
</style>

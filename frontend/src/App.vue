<template>
  <div id="app">
    <div id="top-bar">
      <div class="left">
        <h1><span>Riksdagen &mdash; Cheap Seats</span></h1>
      </div>
      <div class="right">
        <div class="logo-container">
          <img src="@/assets/logo.png" alt="">
        </div>
      </div>
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
  overflow-x: hidden;
}

#top-bar {
  @include contained();
  display: grid;
  grid-template-columns: 1fr auto;
  background: mcolor('yellow', '500');
  border-bottom: 12px solid mcolor('yellow', '300');
  .left {
    padding-top: 100px;
    padding-bottom: 20px;
  }
  .right {
    padding-top: 50px;
    margin-bottom: 15px;
  }
  h1 {
    margin: 0;
    span {
      border-bottom: 5px solid mcolor('yellow', '200')
    }
  }
  .logo-container {
    padding: 15px;
    border-radius: 50%;
    background: #fff;
    height: 100px;
    margin-right: 15px;
    img {
      width: 70px;
      transform: translate(-5%, -6%);
      filter: hue-rotate(55deg);
    }
  }
}
</style>

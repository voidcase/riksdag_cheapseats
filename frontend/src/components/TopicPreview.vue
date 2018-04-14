
<template>
  <div class="topic-preview">
    <h3>Utbildning & Försvar &mdash; hur går det ihop?</h3>
    <div class="author">Jonas Axelsson</div>
    <p>
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officia ipsam tempora corrupti ea harum fugit at nihil, odio nulla earum laudantium in natus doloribus maxime vitae a praesentium similique suscipit
    </p>
    <div class="buttons">
      <router-link to="/doc/1" class="button primary">Läs mer</router-link>
      <router-link to="/doc/2" class="button secondary">Relaterade</router-link>
      <div class="button-wrapper"><img class="lbutton" src="@/assets/bluedelta.svg"/></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TopicPreview'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
@import '@/styles/mixins/shadow.scss';
@import '@/styles/mixins/element.scss';

.topic-preview {
  box-shadow: $shadow-3;
  padding: 1rem;
  margin-top: 15px;
  max-width: 700px;
  h3 {
    margin-bottom: 0;
    margin-top: 0.5em;
    font-weight: 500;
    font-size: 1.1rem;
  }
  .author {
    font-weight: 300;
    font-size: 1.1rem;
  }
  .button {
    &.primary {
      @include button-primary();
    }
    &.secondary {
      @include button-secondary();
    }
  }
  .lbutton {
      width: 40px;
      height: 40px;
      background-color: #dddddd;
      border-radius: 20%;
      transition: 0.05s linear;
  }

  .lbutton:hover {
    opacity: 0.9;
    cursor: pointer;
  }

  .lbutton:active {
    transform: scale(0.8, 0.8);
  }

  .button-wrapper {
    width: 50px;
  }

  .buttons {
    display:flex;
    flex-direction: row;
  }
}

</style>

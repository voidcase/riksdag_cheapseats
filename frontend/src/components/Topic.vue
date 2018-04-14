
<template>
  <div class="topic-container">
    <div class="root-content">
      <h1>{{title}}</h1>
      <div class="author">{{author}}</div>
      <div class="body-text">
        <p v-for="(paragraph, index) in text.paragraphs" :key="index">
          {{ paragraph }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Topic',
  data () {
    return {
      title: 'Skolreform — Ett nytt betygsystem',
      author: 'Jonas Axelsson',
      text: {
        paragraphs: [
          'lorem ipsum dolor sit amet.',
          'Mi septo kira nime.'
        ]
      }
    }
  }
}
</script>

<style lang="scss">
@import '@/styles/mixins/layout.scss';

.topic-container {
  margin-top: 60px;
  @include contained();
}

.root-content {
  h1 {
    margin-bottom: 0;
  }
  .author {
    font-weight: 300;
    font-size: 1.3rem;
    color: #445566
  }
}

</style>

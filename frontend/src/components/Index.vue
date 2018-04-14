<template>
  <div id="home">
    <h1>Senaste Motioner</h1>
    <topic-preview/>
    <topic-preview/>
  </div>
</template>

<script>
import TopicPreview from '@/components/TopicPreview'

export default {
  name: 'Index',
  components: {
    'topic-preview': TopicPreview
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
@import '@/styles/mixins/layout.scss';
@import '@/styles/material/color.scss';

#home {
  padding-top: 60px;
  @include contained();
  h1 {
    display: inline-block;
    margin: 0;
    padding-bottom: -5px;
    border-bottom: 3px solid mcolor('blue', '400');
  }
}

</style>

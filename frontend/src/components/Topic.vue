<template>
  <div :class="{'topic-container': true, 'bleed': viewedAnnotations.length > 0 || this.selection}">
    <h1>{{title}}</h1>
    <div class="author">{{author}}</div>
    <div class="annotation-meta" v-if="viewedAnnotations.length > 0">
      {{viewedAnnotations.length}} {{viewedAnnotations.length == 1 ? 'Annotering' : 'Annoteringar'}}
    </div>
    <div class="body-text" v-on:mouseup="mouseUp">
      <p v-for="(paragraph, index) in text.paragraphs" :key="index">
        <span
        v-for="(word, word_number) in annotate(paragraph, index, text.annotations)"
        :key="word_number"
        :word_index="word_number"
        :paragraph_index="index"
        :annotations="word.annotations.join()"
        :annotations_count="word.annotations.length"
        :class="{
          'annotated': word.annotations.length > 0,
          'selected': wordIsSelected(index, word_number)
        }"
        v-on:click="viewAnnotations(word.annotations)">
          {{word.text}}
        </span>
      </p>
    </div>
    <div class="annotations" v-if="viewedAnnotations.length > 0">
      <ul>
        <li v-for="annotation in viewedAnnotations" :key="annotation.id">
          <p>{{annotation.text}}</p>
          <div class="reactions-wrapper">
            <div class="button-wrapper"><img class="lbutton" src="@/assets/bluedelta.svg" v-on:click="increment(annotation)"/>{{annotation.deltas}}</div>
            <div class="button-wrapper"><img class="lbutton" src="@/assets/annotations.svg"/>{{viewedAnnotations.length}}</div>
            <div class="button-wrapper"><img class="lbutton" src="@/assets/surprised.svg" v-on:click=""/> {{ annotation.disputes }}</div>
          </div>
        </li>
      </ul>
    </div>
    <hr  class="right-separator" v-if="selection && viewedAnnotations.length > 0" />
    <div class="add-annotation" v-if="selection">
      <h3>Lägg till annotering</h3>
      <textarea name="annotation-text" v-model="message" id="annotation"></textarea>
      <button class="submitButton" type="submit" v-on:click="submitAnnotation()">Submit</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Topic',
  data () {
    return {
      message: '',
      title: 'Skolreform — Ett nytt betygsystem',
      author: 'Jonas Axelsson',
      text: {
        paragraphs: [
          'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil, provident ab sequi id delectus fugit temporibus quaerat minus praesentium, minima suscipit impedit omnis quis fugiat, doloribus fuga optio voluptatum enim.',
          'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Consequatur incidunt iure amet cumque delectus nulla officiis odio similique inventore. Similique quos debitis ea explicabo delectus corporis in unde quod quibusdam?'
        ],
        annotations: [
          {
            annotation_id: 0,
            start_paragraph: 0,
            start_index: 4,
            end_paragraph: 0,
            end_index: 7,
            deltas: 1,
            disputes: 56,
            text: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Esse corrupti architecto dignissimos vitae consectetur natus tempore voluptatem quidem at debitis! Dignissimos, vero molestias neque debitis dolor animi excepturi consequatur optio?"
          },
          {
            annotation_id: 1,
            start_paragraph: 0,
            start_index: 5,
            end_paragraph: 0,
            end_index: 5,
            deltas: 4,
            disputes: 6,
            text: "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Esse corrupti architecto dignissimos vitae consectetur natus tempore voluptatem quidem at debitis! Dignissimos, vero molestias neque debitis dolor animi excepturi consequatur optio?"
            }
        ]
      },
      selection: null,
      viewedAnnotations: []
    }
  },
  methods: {
    annotate (text, paragraphIndex, annotations) {
      let annos = _.filter(annotations, ann => paragraphIndex >= ann.start_paragraph &&
      paragraphIndex <= ann.end_paragraph)
      annos = _.map(annos, ann => {
        return {
          start_index: paragraphIndex === ann.start_paragraph ? ann.start_index : 0,
          end_index: paragraphIndex === ann.end_paragraph ? ann.end_index : 1000,
          id: ann.annotation_id,
          deltas: ann.deltas,
          disputes: ann.disputes,
          text: ann.text
        }
      })

      let words = _.split(text, ' ')
      words = _.map(words, (word, index) => {
        let annotationsForWord = _.filter(annos, ann => index >= ann.start_index && index <= ann.end_index)
        return {
          text: word,
          annotations: annotationsForWord
        }
      })
      return words
    },
    increment(annotation) {
      annotation.deltas+=1
    },
    viewAnnotations (annotations) {
      this.viewedAnnotations = annotations
    },
    mouseUp () {
      const selection = window.getSelection()
      const range = selection.getRangeAt(0)
      if (range.startContainer !== range.endContainer || range.startOffset !== range.endOffset) {
        const firstWord = selection.anchorNode.parentElement.attributes
        const lastWord = selection.focusNode.parentElement.attributes
        this.selection = {
          start_paragraph: parseInt(firstWord.getNamedItem('paragraph_index').value),
          start_index: parseInt(firstWord.getNamedItem('word_index').value),
          end_paragraph: parseInt(lastWord.getNamedItem('paragraph_index').value),
          end_index: parseInt(lastWord.getNamedItem('word_index').value)
        }
      } else {
        this.selection = null
      }
      if (window.getSelection().empty) {
        window.getSelection().empty()
      } else if (window.getSelection().removeAllRanges) {
        window.getSelection().removeAllRanges()
      }
    },
    wordIsSelected (paragraph, word) {
      if (!this.selection) return false
      const startIndex = paragraph === this.selection.start_paragraph
        ? this.selection.start_index : 0
      const endIndex = paragraph === this.selection.end_paragraph
        ? this.selection.end_index : 1000
      return paragraph >= this.selection.start_paragraph &&
        paragraph <= this.selection.end_paragraph &&
        word >= startIndex &&
        word <= endIndex
    },
    submitAnnotation() {
      var annotation = {
        annotation_id: 1,
        start_paragraph: this.selection.start_paragraph,
        start_index: this.selection.start_index,
        end_paragraph: this.selection.end_paragraph,
        end_index: this.selection.end_index,
        text: this.message,
        deltas: 0,
        disputes: 0
      }

      this.text.annotations.push(annotation)
      document.getElementById("annotation").value = ""
      this.message = ""
    }

  }
}
</script>

<style lang="scss">
@import '@/styles/mixins/layout.scss';
@import '@/styles/material/color.scss';

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slide {
  from {
    transform: translateX(($bleed-width - $container-width)/2);
  }
  to {
    transform: translateX(0);
  }
}

@keyframes slide-reverse {
  from {
    transform: translateX(($container-width - $bleed-width)/2);
  }
  to {
    transform: translateX(0);
  }
}

.topic-container {
  @include contained();
  margin-top: 60px;
  display: grid;
  grid-template-columns: 800px 1fr;
  grid-column-gap: 2rem;
  & > * {
    grid-column: 1;
    animation: slide-reverse 1s;
  }
  & > .annotations, & > .annotation-meta, & > .add-annotation {
    grid-column: 2;
  }
  &.bleed {
    @include contained_bleed();
    & > * {
      animation: slide 1s;
    }
    & > .annotations, & > .annotations-meta, & > .add-annotation {
      animation: slide 1s, fadeIn 0.4s;
    }
  }
}

.topic-container > .right-separator {
  grid-column: 2;
  width: 100%;
  border: none;
  border-bottom: 2px solid mcolor('yellow', '500');
  width: 80%;
  margin: 1rem auto;
  display: block;
}

.annotation-meta {
  font-size: 1.2rem;
  font-weight: 300;
  padding-left: 1rem;
}

.topic-container {
  h1 {
    margin-bottom: 0;
  }
  .author {
    font-weight: 300;
    font-size: 1.3rem;
    color: #445566
  }
  p {
    ::selection {
      background: mcolor('green', '100');
    }
    line-height: 1.9em;
    .annotated {
      background: mcolor('yellow', '100');
      &[annotations_count="2"] {
        background: mcolor('blue', '200');
      }
      &:hover {
        cursor: pointer;
      }
    }
    .selected {
      background: mcolor('green', '200') !important;
    }
  }
}

.annotations ul {
  list-style: none;
  padding: 0;
  li {
    padding-left: 1rem;
    margin-bottom: 1.5rem;
    border-left: 3px solid mcolor('blue', '200');
  }
}

.add-annotation {
  padding-bottom: 1rem;
  margin-bottom: 1rem;
  padding-left: 1rem;
  padding-right: 1rem;
  border-left: 3px solid mcolor('green', '300');
  h3 {
    font-weight: 300;
  }
  textarea {
    width: 100%;
    min-height: 150px;
    font-family: "Poppins";
    padding: 1rem;
    color: #333;
    font-weight: 400;
  }
}
.lbutton {
    width: 20px;
    height: 20px;
    background-color: #dddddd;
    border-radius: 20%;
    transition: 0.05s linear;
    vertical-align: text-bottom;
    opacity:0.8;
}

.lbutton:hover {
  opacity: 0.6;
  cursor: pointer;
}

.lbutton:active {
  transform: scale(0.8, 0.8);
}

.button-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  width: 60px;
}

.reactions-wrapper {
  display:flex;
  flex-direction: row;
  justify-content: space-evenly;
}

.submitButton {
  border-radius: 500px;
  font-weight: 500;
  border: 2px solid #555;
  padding: 0.75em 1.5em;
  display: inline-block;
  margin-right: 1em;
  border: none;
  background: #81c784;
  color: #333;
  text-decoration: none;
  outline: none;
  font-size: 1.17em;
  font-family: 'Poppins', Helvetica, Arial, sans-serif;


  transition: 0.05s linear;
}

.submitButton:focus {
  outline: none;
  cursor: pointer;

}
.submitButton:active {
  transform: scale(0.8, 0.8);
  outline: none;
}
/*
body {
  transition: 4s linear;
}

body:hover {
  transform: rotate(80deg) translate(200px, 200px) scale(1.5, 1.5);
  animation: blinka 4s linear infinite;
}

@keyframes blinka {
  10% {
    background-color: blue;
    width: 70%;
  }

  20%{
    background-color: green;
    width: 100%;
    transform: rotate(180deg);
  }

  40% {
    background-color: black;
    width:50%;
  }

  60% {
    background-color: red;
    width: 70%;
    transform: rotate(310deg);

  }

  80% {
    background-color: pink;
    width: 100%;
  }

  100% {
    background-color: white;
    width: 80%;
  }

}
*/

</style>

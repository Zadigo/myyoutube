<doc>
  This section regroups the comments and displays other
  additional pieces of information on the total amount
  of comments on the video.

  Comments are iterated using "comment-card".
</doc>

<template>
  <div class="col-sm-12 col-md-8">
    <div class="card">
      <div class="card-body">
        <p class="fw-bold fs-5">{{ currentVideo.comments.count }} Comments</p>
        <base-dropdown-button-vue :items="[{ name: 'Newest' }, { name: 'Oldest' }]" icon="sort" button-name="Sort" @dropdown-click="setSort" />
        <!-- <button class="btn btn-info"><span class="mdi mdi-sort me-2"></span>Sort</button> -->
        <!-- <button class="btn btn-info"><span class="mdi mdi-filter me-2"></span>Filter</button> -->
        <!-- <div class="btn-group">
              </div> -->

        <hr class="my-4">

        <!-- New comment -->
        <div class="card mb-3 shadow-none">
          <div class="card-body">
            <div class="d-flex justify-content-around">
              <div class="me-3">
                <img :src="require('@/assets/avatar2.png')" class="img-fluid rounded-circle" width="100" alt="Image 2">
              </div>

              <div class="w-100">
                <textarea v-model="newComment" cols="30" rows="2" class="form-control" style="resize: none;"></textarea>


                <div class="btn-group shadow-none my-2">
                  <button type="button" class="btn btn-sm btn-light" @click="newComment = null">
                    {{ $t('Cancel') }}
                  </button>

                  <!-- Emojis -->
                  <emoji-picker v-if="showEmojis" @emoji-click="appendEmoji" />
                  <button type="button" class="btn btn-sm btn-light" @click="showEmojis = !showEmojis">
                    <font-awesome-icon icon="fa-solid fa-face-laugh"></font-awesome-icon>
                  </button>

                  <button type="button" class="btn btn-sm btn-light" @click="createComment">
                    <span class="mdi mdi-comment me-2"></span>Comment
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- NOTE: Should be moved to it's own single comment
              component which will allow to trigger replies individually -->
          <!-- <div v-if="isLoading" class="text-center my-4">
            <div class="spinner-border" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div> -->

          <!-- Pinned Comments -->
          <transition-group id="pinned-comments" tag="div" name="opacity">
            <comment-card v-for="comment in pinnedComments" :key="comment.id" :comment="comment" :shadow="shadow" />
          </transition-group>

          <!-- Comments -->
          <transition-group id="comments" tag="div" name="opacity">
            <comment-card v-for="comment in unpinnedComments" :key="comment.id" :comment="comment" :shadow="shadow" />
          </transition-group>
        </div>
      </div>

      <div class="card-footer text-center">
        <button type="button" class="btn btn-primary btn-lg" @click="getComments">
          <font-awesome-icon icon="fa-solid fa-refresh" class="me-2"></font-awesome-icon>
          {{ $t('Load more') }}
        </button>
      </div>
    </div>
  </div>
</template>


<script>
import _ from 'lodash'
import useTesting from '@/composables/testing'

import BaseDropdownButtonVue from '@/layouts/BaseDropdownButton.vue'
import CommentCard from './CommentCard.vue'
import EmojiPicker from '@/layouts/emojis/EmojiPicker.vue'

export default {
  name: 'CommentSection',
  components: {
    BaseDropdownButtonVue,
    CommentCard,
    EmojiPicker
  },
  inject: ['isLoading', 'darkMode'],
  props: {
    currentVideo: {
      type: Object,
      required: true
    },
    shadow: {
      type: Boolean
    }
  },
  emits: {
    'like-video': () => true
  },
  setup () {
    // const isLoading = inject('isLoading')
    const { comments } = useTesting()
    return {
      // isLoading,
      comments
    }
  },
  data () {
    return {
      showEmojis: false,
      // comments: [],
      newComment: null
    }
  },
  sortedComments () {
    // if (this.sortMethod === 'Newest') {
    //   return this.comments.sort((a, b) => {
    //     return dayjs(a.created_on) - dayjs(b.created_on)
    //   })
    // }

    // if (this.sortMethod === 'Oldest') {
    //   return this.comments.sort((a, b) => {
    //     return dayjs(b.created_on) - dayjs(a.created_on)
    //   })
    // }
    return this.comments
  },
  computed: {
    unpinnedComments () {
      return _.filter(this.comments, ['is_pinned', false])
    },
    pinnedComments () {
      return _.filter(this.comments, ['is_pinned', true])
    }
  },
  // mounted () {
  //   this.getComments(
  //     () => {
  //       this.isLoading = true
  //     },
  //     () => {
  //       this.comments[0].is_pinned = true
  //       this.isLoading = false
  //       this.isLoadingRecommendations = false
  //     }
  //   )
  // },
  methods: {
    async likeVideo () {
      this.$emit('like-video', true)
    },
    appendEmoji (emoji) {
      this.newComment = this.newComment + emoji
    },
    setSort (params) {
      this.sortMethod = params[1]
    }
  }
}
</script>

<style scoped>

.show {
  display: block;
}
.emoji_picker {
  position: absolute;
  top: 0;
  z-index: 1055;
}
</style>

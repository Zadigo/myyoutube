import { onMounted, ref } from 'vue'
import dayjs from '../plugins/dayjs'

export default function useTesting () {
  const comments = ref([])
  // const isLoading = ref(false)
  // const isLoadingRecommendations = ref(false)

  async function getComments (before, success) {
    before()
    // this.isLoading = true
    setTimeout(() => {
      var d = dayjs('2022-1-1')
      for (let i = 0; i < 3; i++) {
        const createdOn = d.add(dayjs.duration({ days: Math.random() * (1, 30) + 1 }))
        comments.value.push({
          id: i,
          is_pinned: false,
          replies: [{ id: 1 }, { id: 2 }],
          user: {
            username: 'Lucie Paul'
          },
          created_on: createdOn.format('YYYY-MM-DD')
        })
      }
      success()
      // this.comments[0].is_pinned = true
      // this.isLoading = false
      // this.isLoadingRecommendations = false
    }, 1000)
  }

  onMounted(() => {
    getComments(
      () => {
        // this.isLoading = true
      },
      () => {
        comments.value[0].is_pinned = true
        // this.isLoading = false
        // this.isLoadingRecommendations = false
      }
    )
  })
  
  return {
    // getComments,
    comments,
    // isLoading,
    // isLoadingRecommendations
  }
}

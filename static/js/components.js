// A card that contains a video and used
// in order to show multiple videos on
// a given page
app.component("video-card-component", {
    name: "VideoCardComponent",
    // props: ["href", "src", "reference", "viewcount", "createdon", "videotitle", "channelname"],
    props: {
        href: {
            type: String,
            required: true
        },
        src: {
            type: String,
            required: true
        },
        reference: {
            type: String,
            required: true
        },
        viewcount: {
            type: String,
            default: 0
        },
        createdon: {
            type: String
        },
        videotitle: {
            type: String
        },
        channelname: {
            type: String
        }
    },
    template: "#video-card-component",
    data() {
        return {
            loading: false,

            player: null,

            playeroptions: {
                aspectRatio: "16:9",
                fluid: true,
                responsive: true,
                inactivityTimeout: 2000,
            }
        }
    },

    mounted() {
        var self = this
        self.player = videojs(self.$refs.videoplayer, self.playeroptions)
        self.player.on("loadedmetadata", function (e) {
            self.loading = false
        // setTimeout(() => {
        //     }, 1000)
        // })
        })
    },

    methods: {
        previewvideo: function (e) {
            this.player.play()
            var previewtimeout = setTimeout(() => {
                this.stoppreview()
            }, 4000)
        },
        
        stoppreview: function (e) {
            // clearTimeout(previewtimeout)
            this.player.pause()
            this.player.currentTime(0)
        }
    }
})


app.component('base-messages', {
    name: 'BaseMessages',
    delimiters: ['[[', ']]'],
    computed: {
        ...Vuex.mapState([
            'messages'
        ])
    }
})

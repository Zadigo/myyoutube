// var sendview = (payload) => {
//     // When a video has been read up to a
//     // certain time, update the view count
//     return axios({
//         url: 'https://jsonplaceholder.typicode.com/todos/1',
//         method: "post",
//         data: payload,
//         responseType: "json"
//     })
// }

var sendview = ($client) => {
    return (payload) => {
        return $client({
            url: 'https://jsonplaceholder.typicode.com/todos/1',
            method: 'posts',
            data: payload
        })
    }
}


var likeVideo = ($client) => {
    return (url, data) => {
        console.log(data)
        return $client({
            url: url,
            method: 'post',
            data: data
        })
    }
}


var dislikeVideo = ($client) => {
    return (url, data) => {
        return $client({
            url: url,
            method: 'post',
            data: data
        })
    }
}

var newComment = ($client) => {
    return (url, data) => {
        return $client({
            url: url,
            method: 'post',
            data: data
        })
    }
}

var deleteComment = ($client) => {
    return (url, data) => {
        return $client({
            url: url,
            method: 'delete',
            data: data
        })
    }
}

var updateComment = ($client) => {
    return (url, data) => {
        return $client({
            url: url,
            method: 'patch',
            data: data
        })
    }
}

var APIInterface = {
    install: (Vue, options) => {
        var repositories = {
            views: {
                sendview: sendview(axiosclient)
            },
            video: {
                like: likeVideo(axiosclient),
                dislike: dislikeVideo(axiosclient),
                comment: {
                    new: newComment(axiosclient),
                    delete: deleteComment(axiosclient),
                    update: updateComment(axiosclient)
                }
            }
        }

        Vue.prototype.$api = repositories

        //
    }
}

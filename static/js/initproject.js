var PROJECT = PROJECT || (function () {
    var csrftoken = null

    var setCSRF = (csrftoken) => {
        this.csrftoken = csrftoken
    }

    var getCSRF = () => { return this.csrftoken }

    return {
        init: {
            setCSRF,
            getCSRF
        }
    }
})()

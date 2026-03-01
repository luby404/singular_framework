

document.body.addEventListener("htmx:historyRestore", function (e) {
    const root = document.querySelector("#root_singular")
    if (root) {
        htmx.ajax("GET", location.pathname, { target: root })
        try {
            const title = e.detail.xhr.getResponseHeader("X-Page-Title")
            if (title) {
                document.title = title
            }
        } catch (error) {

        }
    }

})

document.body.addEventListener("htmx:afterSwap", function (e) {

})
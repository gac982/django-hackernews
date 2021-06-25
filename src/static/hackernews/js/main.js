const API = "api/v1/news/"

new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        news: []
    },
    mounted: function () {
        this.getNews();
    },
    methods: {
        getNews: function () {
            fetch(API)
                .then(function(response) {
                    // Transforma la respuesta. En este caso lo convierte a JSON
                    return response.json();
                })
                .then((json) => {
                    // Usamos la información recibida como necesitemos
                    this.news = json;
            });
        },
				votar: function(id) {
					fetch(API, {
						  	headers: {
						    	'Content-type': 'application/json'
						  },
						  	method: 'PUT',
						  	body: JSON.stringify({ 'id': id })
						  })
						  .then((json) => {
						    	// Transforma la respuesta. En este caso lo convierte a JSON
						    	this.getNews()
						 });
				}
    }
})

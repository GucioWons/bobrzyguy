const sendSearchData = (series) => {
        $.ajax({
            type: 'POST',
            url: '/search/',
            data :{
                'csrfmiddlewaretoken':csrf,
                'series':series,
            },
            success: (res) => {
                const data = res.data
                result_box.innerHTML += "";
                if(Array.isArray(data)){
                    result_box.innerHTML = "";
                    data.forEach(series => {
                        result_box.innerHTML += `
                        <div class='row mt-2 mb-2'>
                            <div class='col-2'>
                                <!-- tu wjebać zdjęcie -->
                                <h5 ${series.avatar}></h5>
                            </div>
                            <div class="col-10">
                                <a href="/profile/${series.pk}">
                                <h5>${series.email}
                                </a>
                                <a href="/team/invite/{{object.pk}}/${series.pk}">+</a></h5>
                            </div>
                        </div>
                        `
                });
            }else{
                if(search_input.value.lenght > 0){
                    result_box.innerHTML = `<b>${data}</b>`
                }
                else{
                result_box.classList.add('not-visible')
                }
            }
        },
        error: (err) => {
            console.log(err);
        }
    })
}
const search_form = document.getElementById('search-form')
const search_input = document.getElementById('search-input')
const result_box = document.getElementById('result-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
search_input.addEventListener('keyup', e=>{
    console.log(e.target.value);
    if(result_box.classList.contains('not-visible')){
        result_box.classList.remove('not-visible')
    }
    sendSearchData(e.target.value);
});
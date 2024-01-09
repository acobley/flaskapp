def column_card(title:str, href:str, imgsrc:str) -> str:
        
    elem = '\
    <div class="col-sm-12 col-md-12 col-lg-3 d-flex mt-5 mb-1 justify-content-center"> \
        <div class="card" style="width: 24rem;">\
            <a href="/Videos/'+href+'">\
                <img src="'+imgsrc+'" class="card-img-top" alt="'+title+'"> \
            </a>\
            <div class="card-body">\
                <h5 class="card-title">'+title+'</h5>\
            </div>\
        </div>\
    </div>\
    '
    
    return elem
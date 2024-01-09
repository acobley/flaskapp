def carouselItem(src, alt, isActive: bool) -> str: 
    element = ''
    if (isActive):
        element = ' <div class="carousel-item active">\n\t<img src="'+ str(src) +'" class="d-block w-100" alt="'+str(alt)+'">\n</div>'
    else:
        element = ' <div class="carousel-item">\n\t<img src="'+ str(src) +'" class="d-block w-100" alt="'+str(alt)+'">\n</div>'
    return element

def carouselIndicator(data_target_id:str, index:int, isActive: bool) -> str:
    element = ''
    
    if (isActive):
        element = '<button type="button" data-bs-target="#'+str(data_target_id)+'" data-bs-slide-to="'+str(index)+'" class="active" aria-current="true" aria-label="Slide '+str(index+1)+'"></button>\n'
    else:
        element = '<button type="button" data-bs-target="#'+str(data_target_id)+'" data-bs-slide-to="'+str(index)+'" aria-label="Slide '+str(index+1)+'"></button>\n'
    return element
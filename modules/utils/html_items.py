def carouselItem(src, alt, isActive) -> str: 
    element = ''
    if (isActive):
        element = ' <div class="carousel-item active">\n\t<img src="'+ str(src) +'" class="d-block w-100" alt="'+str(alt)+'">\n</div>'
    else:
        element = ' <div class="carousel-item">\n\t<img src="'+ str(src) +'" class="d-block w-100" alt="'+str(alt)+'">\n</div>'
    return element
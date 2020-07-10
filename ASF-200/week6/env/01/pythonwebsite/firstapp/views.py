from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index. I wasn't sure what else to type to make 2 paragraphs SO I got here some loram ipsum: </h1> <h2><p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent accumsan ante ac turpis consequat, ut dignissim nisl consectetur. Etiam eget justo nec nisi egestas laoreet. Sed feugiat iaculis imperdiet. Curabitur lacinia sagittis elit, convallis condimentum enim porttitor eu. Nunc tristique eros quis diam dapibus, nec facilisis erat ornare. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum at neque ante. Mauris quis nunc quis neque euismod dignissim. Duis ornare rutrum elit, mattis malesuada odio hendrerit a.</p></h2><h3><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Aenean quam purus, lacinia nec imperdiet non, hendrerit ac erat. Cras tristique risus vel tortor dictum, sed cursus magna tempor. Nullam fringilla ultrices augue ac vehicula. Duis maximus, ex feugiat dictum imperdiet, erat est viverra tellus, eu egestas nisl est quis enim. Phasellus non lorem vitae felis vestibulum egestas. Duis a luctus nibh. Praesent eu porta arcu. Vestibulum ut lectus in sem dignissim facilisis vel ac augue.</p></h3>")
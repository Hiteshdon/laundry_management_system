@echo ON
set laundry=%1
echo %laundry%
echo {% extends 'main.html' %} > %laundry%\templates\%laundry%\navbar.html
echo:
echo {% block main %} > %laundry%\templates\%laundry%\navbar.html
echo {% include '%laundry%/navbar.html' %} > %laundry%\templates\%laundry%\navbar.html
echo:
echo {% endblock main %} > %laundry%\templates\%laundry%\navbar.html
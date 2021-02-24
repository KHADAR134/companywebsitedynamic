# Dynamic Web Design for a Manufacturing Company
## AIM: 
To design a dynamic website for a clothes manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 6:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Uzma industries Limited </title>
    <link rel="stylesheet" href="{% static 'css/layout1.css' %}">
    <link rel="icon" href="{% static 'images/e1.jpg' %}" type="image/x-icon">

</head>

<body>
    <div class="container">
        <div class="banner">
            UZMA INDUSTRIES LIMITED
        </div>
        <div class="menu">
            <div class="menuitem"><a href="/home">Home</a></div>
            <div class="menuitem"><a href="/products">Products</a></div>
            <div class="menuitem"><a href="/people">People</a></div>
            <div class="menuitem"><a href="/contactus">ContactUs</a></div>
        </div>
        <div class="content">
            {% block content %}
            {% endblock  %}
        </div>
        <div class="footer">
            Copyright © 2020 Uzma Industries Limited, Developed by Khadar basha.
        </div>
    </div>
</body>

</html>
```

### home.html
```
{% extends "mywebsite/base.html" %}

{% block content %}
<div class="homecontent">
    <h1>About Us</h1>
    <img src="/static/images/a1.jpg" alt="Building">
    <div class="contenttext">
        Uzma manufacturing is a major industry. It is largely based on the conversion of fibre into yarn, yarn into
        fabric. These are then dyed or printed, fabricated into clothes which are then converted into useful goods such
        as clothing, household items, upholstery and various industrial products it summarizes the types of trade and
        industry along the production and life chain of clothing and garments, starting with the textile industry
        (producers of cotton, wool, fur, and synthetic fibre), embellishment using embroidery, via the fashion industry
        to apparel retailers up to trade with second-hand clothes and textile recycling. The producing sectors build
        upon a wealth of clothing technology some of which, like the loom, the cotton gin, and the sewing machine
        heralded industrialization not only of the previous textile manufacturing practices.Different types of fibres
        are used to produce yarn. Cotton remains the most important natural fibre, so is treated in depth. There are
        many variable processes available at the spinning and fabric-forming stages coupled with the complexities of the
        finishing and colouration processes to the production of a wide range of products.
     <ul>
        <li>Levi's</li>
        <li>Flying Machine</li>
        <li>Allen Solly </li>
        <li>Numero Uno</li>
        <li>Mufti</li>
        <li>Pepe Jeans</li>


        </ul>
    </div>
</div>
{% endblock  %}
```
### products.html
```
{% extends "mywebsite/base.html" %}

{% block content %}
<div class="productcontent">
    <h1>Our Premium Products</h1>
    <div class="productitems">

        {% for products in products %}
        <div class="productitem">
            <div class="itemimage">
                <img src="{{ products.photo.url }}" alt="product image" height="200" width="200">
            </div>
            <div class="productsname"><strong>PRODUCT NAME:</strong>{{ products.name }}
            </div>
            <div class="productsprice"><strong>PRODUCT PRICE:</strong>{{ products.price }}
            </div>
            
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```
## people.html:
```
{% extends "mywebsite/base.html" %}

{% block content %}

<h1 id="Ex">Our Team Executives</h1>
<div class="container">

    {% for people in peoples %}

    <div class="peoplelist">
        <img src="{{ people.photo.url }}" alt="executive image" width="250" height="200">
        <div class="membername"><strong><u>EXECUTIVE</u>:{{ people.name }}</strong>
        </div>
        <div class="designation"><strong><u>DESIGNATION</u>:{{ people.designation }}
            </strong></div>
    </div>
    {% endfor %}
</div>
{% endblock %}
```
## contactus.html:
```
{% extends "mywebsite/base.html" %}

{% block content %}

<div class="content1">
    <h1 class="contactcenter">
        CONTACT US</h1>
    <h2 class="contactcenter">
        CONTACT ADDRESS:2nd industrial City, Al Kharj Road, Street No.: 175, 3rd Lane Zone D. Riyadh, Kingdom of Saudi Arabia | P.O. Box: 26862 | Riyadh: 11496, Saudi Arabia
        <br>
        EMAIL:uzamkhan87@gmail.com
        <br>
        MOBILE:+966568421579
    </h2>
</div>
{% endblock  %}
```    
## MODELS.PY
```
from django.db import models
from django.contrib import admin

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'photo')

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'photo')
    
```

## ADMIN.PY
```
from django.contrib import admin
from .models import People,PeopleAdmin
from .models import Product,ProductAdmin

# Register your models here.

admin.site.register(People,PeopleAdmin)

admin.site.register(Product,ProductAdmin)

```




## OUTPUT:
![output](./static/images/output1.png)

![output](./static/images/output2.png)

![output](./static/images/output3.png)

![output](./static/images/output4.png)

![output](./static/images/output5.png)

![output](./static/images/output6.png)

## ADMIN PAGE
![output](./static/images/admin1.png)

![output](./static/images/admin2.png)

## CODE VALIDATION REPORT:
![output](./static/images/report1.png)

![output](./static/images/report2.png)

![output](./static/images/report3.png)

![output](./static/images/report4.png)

![output](./static/images/report5.png)



## RESULT:
Thus a website is designed for the clothes manufacturing company and is hosted in the URL http://khadar.student.saveetha.in:8000/. HTML code is validated.
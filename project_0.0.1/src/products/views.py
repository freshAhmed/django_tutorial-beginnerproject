from django.shortcuts import render
from .models import Product
import math
from .forms import ProductForm






def product_create_view(request):
 context={}
 print(dir(request.POST))
 return render(request,'products/product_create.html',context)




# def product_create_view(request):
#  form=ProductForm(request.POST or None)
#  if form.is_valid():
#   form.save()
#   form=ProductForm()

#  context={'form':form} 
#  return render(request,'products/product_create.html',context)







def product_detail_view(request):
 obj=Product.objects.get(id=1)
 discount=0.5
 aplay_discount=True
 if aplay_discount:
  obj.price=str(float(math.floor(float(obj.price)-float(obj.price)*discount)))
 context={'obj':obj,'discount':discount,"aplay_discount":aplay_discount}
 return render(request,"products/product_detail.html",context)
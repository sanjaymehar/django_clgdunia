from django.shortcuts import render
from clgdunia.models import Carsale
import matplotlib.pyplot as plt
from operator import itemgetter
from django.views.generic import CreateView
# Create your views here.
def home(request):
    a=Carsale.objects.all()
    
    ##############################################################################
    total_Manufacturer=[]
    cont_total_Manufacturer={}

    for i in a:
        total_Manufacturer.append(i.Manufacturer)

    for i in set(total_Manufacturer):
        cont_total_Manufacturer[i]=total_Manufacturer.count(i)


    company_name=[]
    company_name_count=[]
    for i,j in cont_total_Manufacturer.items():
        company_name.append(i)
        company_name_count.append(j)

    plt.figure(figsize=(10,10))
    plt.pie(company_name_count,labels = company_name,autopct = '%.2f%%')
    plt.title('Manufacturer', fontsize = 20)
    plt.savefig('clgdunia/static/Manufacturer_data.png')

    plt.title('Manufacturer', fontsize = 20)
    plt.figure(figsize=(30,7))
    plt.bar(company_name, company_name_count, color ='maroon',width = 0.4)
    plt.savefig('clgdunia/static/Manufacturer_data_bar.png')
####################################################################################################
    
    car_model_name_Fuel_capacity={}
    for i in a:
        car_model_name_Fuel_capacity[i.Model]=float(i.Fuel_capacity),i.Manufacturer
    
    
    car_Fuel_capacity_data=[]
    for i,j in car_model_name_Fuel_capacity.items():
        car_Fuel_capacity_data.append([i,j[1],j[0]])
    
    sortted_car_Fuel_capacity_data=(sorted(car_Fuel_capacity_data, key=itemgetter(2)))

    
    top_5_car_Fuel_capacity=sortted_car_Fuel_capacity_data[:5]
    bottom_5_car_Fuel_capacity=sortted_car_Fuel_capacity_data[-5:]

    car_name_model_top5=[]
    Fuel_capacity_top5=[]

    for i in top_5_car_Fuel_capacity:
        car_name_model_top5.append([i[0],i[1]])
        Fuel_capacity_top5.append(i[2])
    
    plt.figure(figsize=(5,5))
    plt.pie(Fuel_capacity_top5,labels = car_name_model_top5,autopct = '%.2f%%')
    plt.title('Top 5 Fuel_capacity car ', fontsize = 17)
    plt.savefig('clgdunia/static/top5_Fuel_capacity car.png')

    car_name_model_bottom5=[]
    Fuel_capacity_bottom5=[]

    for i in bottom_5_car_Fuel_capacity:
        car_name_model_bottom5.append([i[0],i[1]])
        Fuel_capacity_bottom5.append(i[2])

    plt.figure(figsize=(5,5))
    plt.pie(Fuel_capacity_bottom5,labels = car_name_model_bottom5,autopct = '%.2f%%')
    plt.title('Bottom 5 Fuel_capacity car ', fontsize = 17)
    plt.savefig('clgdunia/static/bottom5_Fuel_capacity car.png')
################################################################################################


    car_model_name_Fuel_efficiency={}
    for i in a:
        car_model_name_Fuel_efficiency[i.Model]=float(i.Fuel_efficiency),i.Manufacturer

    car_Fuel_efficiency_data=[]
    for i,j in car_model_name_Fuel_efficiency.items():
        car_Fuel_efficiency_data.append([i,j[1],j[0]])

    sortted_car_Fuel_efficiency_data=(sorted(car_Fuel_efficiency_data, key=itemgetter(2)))
    
    top_5_car_Fuel_efficiency=sortted_car_Fuel_efficiency_data[:5]
    bottom_5_car_Fuel_efficiency=sortted_car_Fuel_efficiency_data[-5:]

    car_name_model_efficiency_top5=[]
    Fuel_efficiency_top5=[]
    
    for i in top_5_car_Fuel_efficiency:
        car_name_model_efficiency_top5.append([i[0],i[1]])
        Fuel_efficiency_top5.append(i[2])

    plt.figure(figsize=(5,5))
    plt.pie(Fuel_efficiency_top5,labels = car_name_model_efficiency_top5,autopct = '%.2f%%')
    plt.title('Top 5 Fuel_efficiency car ', fontsize = 17)
    plt.savefig('clgdunia/static/top5_Fuel_efficiency car.png')

    car_name_model_efficiency_bottom5=[]
    Fuel_efficiency_bottom5=[]

    for i in bottom_5_car_Fuel_efficiency:
        car_name_model_efficiency_bottom5.append([i[0],i[1]])
        Fuel_efficiency_bottom5.append(i[2])

    plt.figure(figsize=(5,5))
    plt.pie(Fuel_efficiency_bottom5,labels = car_name_model_efficiency_bottom5,autopct = '%.2f%%')
    plt.title('Bottom 5 Fuel_efficiency car ', fontsize = 17)
    plt.savefig('clgdunia/static/bottom5_Fuel_efficiency car.png')
    
##############################################################################################################
    price_car=[]
    for i in a:
        price_car.append([i.Model,int(i.Price_in_thousands),i.Manufacturer])

    price_car_sorted=(sorted(price_car, key=itemgetter(1)))
    expensive_car=price_car_sorted[-1]
    cheap_car=price_car_sorted[0]
    

    return render(request,"home.html",{"expensive_car":expensive_car,"cheap_car":cheap_car})


  

class Adddata(CreateView):
    template_name='add_data.html'
    model=Carsale
    fields=['Manufacturer','Model','Sales_in_thousands','Price_in_thousands','Engine_size','Horsepower','Fuel_capacity','Fuel_efficiency']
    context_object_name='form'
   

    
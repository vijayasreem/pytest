from django.shortcuts import render
from .forms import PaymentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def payment_gateway_form(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            #process the payment and redirect user to a secure payment page
            payment_data = form.cleaned_data
            if payment_data['payment_method'] == 'creditcard':
                return HttpResponseRedirect(reverse('credit_card_payment',kwargs=payment_data))
            elif payment_data['payment_method'] == 'paypal':
                return HttpResponseRedirect(reverse('paypal_payment',kwargs=payment_data))
            elif payment_data['payment_method'] == 'stripe':
                return HttpResponseRedirect(reverse('stripe_payment',kwargs=payment_data))
            else:
                #error handling
                return HttpResponseRedirect(reverse('payment_failed'))
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})

def credit_card_payment(request,payment_data):
    #process the credit card payment
    #handle successful and failed payment transactions
    #logging to capture any payment-related issues for debugging purposes
    #if payment is successful, redirect user to confirmation page
    return HttpResponseRedirect(reverse('payment_success'))

def paypal_payment(request,payment_data):
    #process the paypal payment
    #handle successful and failed payment transactions
    #logging to capture any payment-related issues for debugging purposes
    #if payment is successful, redirect user to confirmation page
    return HttpResponseRedirect(reverse('payment_success'))

def stripe_payment(request,payment_data):
    #process the stripe payment
    #handle successful and failed payment transactions
    #logging to capture any payment-related issues for debugging purposes
    #if payment is successful, redirect user to confirmation page
    return HttpResponseRedirect(reverse('payment_success'))

def payment_failed(request):
    #display failed payment message
    return render(request, 'payment_failed.html')

def payment_success(request):
    #display successful payment message
    return render(request, 'payment_success.html')
from django.urls import path

urlpatterns = [
    path('', payment_gateway_form, name='payment_gateway_form'),
    path('credit_card_payment/', credit_card_payment, name='credit_card_payment'),
    path('paypal_payment/', paypal_payment, name='paypal_payment'),
    path('stripe_payment/', stripe_payment, name='stripe_payment'),
    path('payment_failed/', payment_failed, name='payment_failed'),
    path('payment_success/', payment_success, name='payment_success'),
]
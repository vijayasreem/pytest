# models.py

from django.db import models

class PaymentGateway(models.Model):
    """
    Model representing a payment gateway integration
    """
    PAYMENT_METHODS = (
        ('credit_debit', 'Credit/Debit Card'),
        ('paypal', 'PayPal'),
        ('stripe', 'Stripe'),
    )
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    is_active = models.BooleanField(default=False)
    
class PaymentTransaction(models.Model):
    """
    Model representing a payment transaction
    """
    payment_gateway = models.ForeignKey(PaymentGateway, on_delete=models.CASCADE, related_name='payment_transactions')
    payment_status = models.CharField(max_length=20)
    payment_message = models.TextField()
    payment_log = models.TextField()
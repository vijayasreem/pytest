#!/usr/bin/env python

import logging
import os
import sys

from payment_gateway import PaymentGateway

def main():
    try:
        # Initialize the Payment Gateway
        payment_gateway = PaymentGateway()

        # Set up payment methods
        payment_gateway.add_payment_method("Credit/Debit Cards")
        payment_gateway.add_payment_method("PayPal")
        payment_gateway.add_payment_method("Stripe")

        # Redirect the user to the secure payment page
        payment_gateway.redirect_to_payment_page()

        # Ask the user to enter their payment details
        payment_gateway.enter_payment_details()

        # Process the payment
        payment_status = payment_gateway.process_payment()

        # Handle successful and failed transactions
        if payment_status == "Successful":
            print("Thank you for your payment!")
        else:
            print("There was an issue with your payment. Please try again.")

    except Exception as e:
        # Log any errors for debugging
        logging.error(e)

if __name__ == "__main__":
    # Execute main()
    sys.exit(main())
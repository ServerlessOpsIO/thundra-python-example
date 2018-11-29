# # Wild Rydes Promo Discount
[![Serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Build Status](https://travis-ci.org/ServerlessOpsIO/wild-rydes-promo-discount.svg?branch=master)](https://travis-ci.org/ServerlessOpsIO/wild-rydes-promo-discount)

This is the Promo Discount service which returns a discount multiplier for ride requests.  It is part off an experiment that rewards certain users randomly based on their activities.

We plan to measure user retention and user generated revenue to see if randomized discounts make a difference.

## Resources

This will create:
* Lambda Function
* API Gateway

## Outputs

__WildRydesPromoDiscountInvokeUrl:__ URL of API Gateway.

__WildRydesGetPromoDiscountUrl:__ URL of _GetPromoDiscount_ endpoint.


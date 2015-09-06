---
layout: post
title: Setup And Secure Amazon Vpc
---

[logo]: http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/images/subnets-diagram.png

Setting Up Amazons Virtual Private Cloud web service

The entire Vpc App Cluster will be addressed on 10.0.0.0/16 and each EC2 instance
will be on a priviate subnet 10.0.N.0/24. 

![alt text][logo]

#Todo: Verify
Routing between private subnets will be managed by the Vpc service.

Dns will be configured via AWS Route 53. Entries will need to be made for
mail.icaroslabs.com, devel.icaroslabs.com, cms.icaroslabs.com, and an MX record
for mail.icaroslabs.com.

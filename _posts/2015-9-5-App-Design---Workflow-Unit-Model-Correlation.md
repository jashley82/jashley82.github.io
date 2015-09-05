---
layout: post
title: App Design - Workflow Unit Model Correlation
---

Let's say we are working on a CMS and we wanted an integration to AWS.

The first thing we would want to setup in an AWS deployment might be IAM. So we
create a Model in our app called AWSIam with fields corresponding to configuration 
settings for one IAM User. Along with the CRUD views associated with this model,
this body of woirk would be considered One Workflow Unit.

One Workflow Unit would correlate to one Model and one set of CRUD views.

The second step would be to setup a VPC cluster. Create a model called AWSVpc and
fields corresponding to it's configuration settings. Build out it's CRUD actions
and maybe start to add some styling.

By now we are probably starting to see the need for some proper navigation. A 
nav bar on the left with some rails style jquery to hide it when it gets annoying.
The navbar might consist of a template for each model and it's fields. Researching
how to lookup a class's name and it's fields seems beneficial, in order to populate
the hierarchies in the navbar template fields.

So we would build out Workflows for each service...

* AWSIam
* AWSVpc
* AWSR53
* AWSS3
* AWSCloudFront
* AWSBeanStalk
* AWSEcs
* Others

Now we want to build out a proper dashboard with proper real time metrics. Let's
build out some models with redis backends and polling on the front end. Or perhaps
Models with a Redis back end PLUS tethered to a Tornado Pub/Sub style server. 
If we are working with Python, for example, we could use Django and it's Swampdragon 
component on the back end and maybe Angular or React on the front end. I am
interested in how this would be accomplished in a Rails environment.

One consideration to make when dealing with a live data model would definitely
be persistence. How is data handled in the database layer and redis layer? Perhaps
take a snapshot every hour from redis and put it in the database.



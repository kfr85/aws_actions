#!/usr/bin/env python3
# coding: utf-8

from botocore import loaders
from botocore import model

if __name__ == "__main__":
  type_name = "service-2"
  loader = loaders.Loader()

  for serv in loader.list_available_services(type_name):
    res = loader.load_service_model(serv, type_name)
    mo = model.ServiceModel(res)
    for ope in mo.operation_names:
      print(serv + ": " + ope)

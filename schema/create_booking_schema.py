"""Схема для api restful, create booking"""

schema = {
    "type": "object",
    "properties": {
        "bookingid":{
            "type":"number"
            },
        "booking":    
    {
  "type": "object",
  "properties": {
    "firstname": {
      "type": "string"
    },
    "lastname": {
      "type": "string"
    },
    "totalprice": {
      "type": "number"
    },
    "depositpaid": {
      "type": "boolean"
    },
    "bookingdates": {
      "type": "object",
      "properties":
      {
          "checkin":
          {
              "type":"string"
          },
          "checkout":
          {
              "type":"string"
          }
      },
      "required":[
          "checkin",
          "checkout"
          ]
    },
    "additionalneeds":
    {
        "type":"string"
    }
  },
  "required": [
    "firstname",
    "lastname",
    "totalprice",
    "depositpaid",
    "bookingdates",
    "additionalneeds"
  ]
}
    },
    "required": [
    "bookingid",
    "booking"
  ]
}
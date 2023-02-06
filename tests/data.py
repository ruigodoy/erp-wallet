CASH_BACK_PAYLOAD = {
   "sold_at":"2026-01-02 00:00:00",
   "customer":{
      "document":"00000000000",
      "name":"JOSE DA SILVA"
   },
   "total":"100.00",
   "products":[
      {
         "type":"A",
         "value":"40.00",
         "qty":1
      },
      {
         "type":"B",
         "value":"60.00",
         "qty":5
      }
   ]
}

CASH_BACK_PAYLOAD_WITH_INVALID_DATE = {
   "sold_at":"2026-31-02 00:00:00",
   "customer":{
      "document":"00000000000",
      "name":"JOSE DA SILVA"
   },
   "total":"100.00",
   "products":[
      {
         "type":"A",
         "value":"40.00",
         "qty":1
      },
      {
         "type":"B",
         "value":"60.00",
         "qty":5
      }
   ]
}

CASH_BACK_PAYLOAD_WITH_DOCUMENT = {
   "sold_at":"2026-01-02 00:00:00",
   "customer":{
      "document":"0000000000",
      "name":"JOSE DA SILVA"
   },
   "total":"100.00",
   "products":[
      {
         "type":"A",
         "value":"40.00",
         "qty":1
      },
      {
         "type":"B",
         "value":"60.00",
         "qty":5
      }
   ]
}

CASH_BACK_PAYLOAD_WITH_TOTAL = {
   "sold_at":"2026-01-02 00:00:00",
   "customer":{
      "document":"00000000000",
      "name":"JOSE DA SILVA"
   },
   "total":"100.00",
   "products":[
      {
         "type":"A",
         "value":"40.00",
         "qty":1
      },
      {
         "type":"B",
         "value":"61.00",
         "qty":5
      }
   ]
}
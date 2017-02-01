# bijou-web-service

A tiny web service to retrieve categories and products

## Endpoints

### `GET /categories`

Example response:

```
{
  "categories": [
    {
      "title": "Shirts"
    },
    {
      "title": "T-shirts"
    },
    {
      "title": "Polo Shirts"
    },
    {...}
  ]
}
```

### `GET /category/{title}`

Example response:

```
{
  "category": {
    "title": "Shirts"
  },
  "products": [
    {
      "name": "THE JENKINS LONG SLEEVE SHIRT",
      "discounted_price": "",
      "high_price": "355.00",
      "item_number": "F4KS70D6GP"
    },
    {
      "name": "THE MATLOCK LONG SLEEVE FLANNEL SHIRT",
      "discounted_price": "",
      "high_price": "342.00",
      "item_number": "F4WF50G0GP"
    },
    {
      "name": "THE BLYTHE POP-OVER SHORT SLEEVE SHIRT",
      "discounted_price": "",
      "high_price": "355.00",
      "item_number": "F4WS70A1GP"
    },
    {...}
  ]
}
```

### `GET /products`

Example response:

```
{
  "products": [
    {
      "name": "THE JENKINS LONG SLEEVE SHIRT",
      "discounted_price": "",
      "high_price": "355.00",
      "item_number": "F4KS70D6GP"
    },
    {
      "name": "THE MATLOCK LONG SLEEVE FLANNEL SHIRT",
      "discounted_price": "",
      "high_price": "342.00",
      "item_number": "F4WF50G0GP"
    },
    {
      "name": "THE BLYTHE POP-OVER SHORT SLEEVE SHIRT",
      "discounted_price": "",
      "high_price": "355.00",
      "item_number": "F4WS70A1GP"
    },
    {...}
  ]
}
```



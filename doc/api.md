## API

The API currently has four routes:

* `/moneyserve/routes` which lists all the routes of the API
* `/moneyserver/supermarket/{id}` which returns the supermarket whose id is given in the url
* `/moneyserver/supermarkets` which returns all the supermarkets in the database. It can have four query parameters:
  * `with_address`: if it equals 'true', supermarkets are retrieved with their address
  * `order_by` which can take four values (`id_asc`, `id_desc`, `name_asc`, `name_desc`)
  * `per_page` which states the number of supermarkets retrieved per page (default value is 20)
  * `page` which states the page to retrieve (default value is 1)
* `moneyserve/product/{id}` which returns the number of products in the supermarket whose id is given is the url

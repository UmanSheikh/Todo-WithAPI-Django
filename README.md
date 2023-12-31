
# Todo with Apis

In this project, I used Django Rest Framework for api calls and performe CURD operations.

## Running the project

make sure you have `Django` and `djangorestframework` installed in your system. Then run 
`Django Version: 5.0` 
`djangorestframework Version: 3.14.0`
```bash 
python manage.py runserver
```

in the terminal where manage.py file is located

## API Reference

#### Get all items

```http
  GET /api/view/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None` | `None` | None |

#### Create Todo

```http
  POST /api/create/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Item Name`      | `string` | **Required**. Name of item to Create or Add |


#### Update Todo

```http
  POST /api/update/{$id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Item ID`      | `integer` | **Required**. ID of item to Update Status |

#### Delete Todo

```http
  POST /api/Delete/{$id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Item ID`      | `integer` | **Required**. ID of item to Delete Todo |


## Author

- [@UmanSheikh](https://www.linkedin.com/in/umansheikh/)


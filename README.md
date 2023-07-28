# Pokemon API Documentation

## 1st API - Fetch Pokemon Details from External API and Persist

**Endpoint**: `http://localhost:8000/pokemon/external/{Pokemon_name}/`

**Method**: GET

**Description**: This API connects to an external Pokemon API to fetch details for a given Pokemon by its name. It then persists these details in the local PostgreSQL database. The API response will include the Pokemon's ID and the fetched details.

**URL Parameters**:
- `Pokemon_name` (string): The name of the Pokemon for which details will be fetched.

**Response**:
```json
{
    "id": 32,
    "pokemon_details": {
        "Pokemon_id": 25,
        "name": "pikachu",
        "ability_name": "static",
        "height": 4,
        "weight": 60,
        "species_color": "yellow"
    }
}
```

## 2nd API - Fetch Persisted Pokemon Details from Local Database

**Endpoint**: `http://localhost:8000/pokemon/details/{pokemon_id}/`

**Method**: GET

**Description**: This API retrieves the persisted Pokemon details from the local PostgreSQL database based on the provided `pokemon_id`. It returns the stored details of the Pokemon.

**URL Parameters**:
- `pokemon_id` (integer): The ID of the Pokemon for which details will be fetched from the local database.

**Response**:
```json
{
    "pokemon_details": {
        "Pokemon_id": 25,
        "name": "pikachu",
        "ability_name": "static",
        "height": 4,
        "weight": 60,
        "species_color": "yellow"
    }
}
```

## 3rd API - Update Persisted Pokemon Details

**Endpoint**: `http://localhost:8000/pokemon/update/{pokemon_id}/`

**Method**: PUT

**Description**: This API allows updating the details of a previously persisted Pokemon in our PostgreSQL database. It expects a JSON payload containing the updated details, and upon successful update, it returns a success message.

**URL Parameters**:
- `pokemon_id` (integer): The ID of the Pokemon to be updated in the database.

**Request**:
```json
{
    "pokemon_details": {
        "name": "ditto_updated",
        "ability_name": "limber",
        "height": 47,
        "weight": 40,
        "species_color": "black"
    }
}
```

**Response**:
```json
{
    "message": "Pokemon details updated successfully."
}
```

## Running the Application

To run the application, we have dockerized it for easy setup. Follow these steps to start the application:

1. Make sure you have Docker installed on your system.

2. Open a terminal and navigate to the directory where the `docker-compose.yml` file is located.

3. Execute the following command to start the application and run the necessary containers:
   > Go to folder which contains your docker file.
   ```
   docker build -t crawler:latest .
   docker-compose up -d
   docker exec -it <container_id> bash 
         - Please run below commands in bash :-
              -python manage.py makemigartions
              -python manage.py migrate
   ```

4. Once the containers are up and running, you can access the APIs using the provided endpoints and methods.

# Document Retrieval System  

## Setup  

1. Clone the repository.  
2. Navigate to the project directory.  
3. Run `docker-compose up --build` to start the services.  

## API Endpoints  

- **GET /health**: Check if the API is active.  
- **POST /search**: Search for documents.  
  - Parameters:  
    - `text`: The search query.  
    - `top_k`: Number of top results to return.  
    - `threshold`: Minimum score for results.  
    - `user_id`: Unique identifier for the user.
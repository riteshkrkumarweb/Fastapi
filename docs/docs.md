 # The Path() 
    function in FastAPI is used to provide metadata, validation rules, and documentation hints for path parameters in your API endpoints. Title ,Description ,Example:- ge, gt, le, lt Min_length Max_length regex
    ...,Three dot in this it means it is required not be ignored 
# HTTPException
    HTTPException is a special built-in exception in FastAPI used to return custom HTTP error responses 
    when something goes wrong in your API.
    Instead of returning a normal JSON or crashing the server, you can gracefully raise an error with a proper HTTP status code (like 404, 400, 403, etc.)a custom error message(optional) extra headers
# Query()
    Query() is used in FastAPI to define and validate query parameters.
    It helps add validation, default values, and documentation to query parameters.
    Syntax
    Query(default, description="", min_length=1)

    Important Parameters
    * default            → Sets the default value.
    * description        → Adds a description in API docs.
    * example            → Shows an example value.
    * min_length         → Minimum allowed string length.
    * max_length         → Maximum allowed string length.
    * ge                 → Value must be greater than or equal to a number.
    * gt                 → Value must be greater than a number.
    * le                 → Value must be less than or equal to a number.
    * lt                 → Value must be less than a number.
    * pattern            → Validates text using a regex pattern.
    * alias              → Uses a different name in the URL.
    * deprecated         → Marks the parameter as deprecated.
    * include_in_schema  → Shows or hides the parameter in API docs.

    🌍 Real-Life Example
    Imagine searching on Amazon:
    /products?category=laptop&price=50000
    Here, category and price are query parameters because they come after ?.

    💻 Code Example
    from fastapi import Query

    @app.get("/search")
    def search(
        q: str = Query(
            min_length=3,
            description="Enter search keyword"
        )
    ):
        return {"query": q}
    Memory Trick

    Query = Questions in the URL

    Anything after ? in a URL is usually a query parameter.

    Common Mistake
    Using Query() for path parameters.
    /users/{id}
    id is a path parameter, so use Path(), not Query().

    One-Line Summary
    Query() is used to validate and document values passed after ? in a URL.

# Most Common HTTP Status Codes
    * 200 → OK (Request successful)
    * 201 → Created (Resource created successfully)
    * 400 → Bad Request (Invalid input from client)
    * 401 → Unauthorized (Authentication required)
    * 403 → Forbidden (Access denied)
    * 404 → Not Found (Resource does not exist)
    * 405 → Method Not Allowed (Wrong HTTP method used)
    * 409 → Conflict (Resource already exists)
    * 422 → Unprocessable Entity (Validation error)
    * 500 → Internal Server Error (Server-side error)


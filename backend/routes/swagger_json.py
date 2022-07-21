from flask import Blueprint

blueprint = Blueprint('swagger_json', __name__)


@blueprint.route('/swagger.json', methods=['GET'])
def swag():
    return {
        "openapi": "3.0.0",
        "info": {
            "version": "1.0.1",
            "title": "Swagger Petstore",
            "license": {
                "name": "MIT"
            }
        },
        "servers": [
            {
                "url": "http://localhost:8000/petstore_api/"
            }
        ],
        "paths": {
            "/pets": {
                "get": {
                    "summary": "List all pets",
                    "operationId": "listPets",
                    "tags": [
                        "pets"
                    ],
                    "responses": {
                        "200": {
                            "description": "List of pets",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/Pets"
                                    }
                                }
                            }
                        }
                    }
                },
                "post": {
                    "summary": "Create a pet",
                    "operationId": "createPet",
                    "tags": [
                        "pets"
                    ],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/PetIn"
                                }
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Created pet response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/PetOut"
                                    }
                                }
                            }
                        },
                        "default": {
                            "description": "unexpected error",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/Error"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "PetIn": {
                    "type": "object",
                    "required": [
                        "name"
                    ],
                    "properties": {
                        "name": {
                            "type": "string"
                        }
                    }
                },
                "PetOut": {
                    "type": "object",
                    "required": [
                        "id",
                        "name"
                    ],
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        }
                    }
                },
                "Pets": {
                    "type": "array",
                    "items": {
                        "$ref": "#/components/schemas/PetOut"
                    }
                },
                "Error": {
                    "type": "object",
                    "required": [
                        "code",
                        "message"
                    ],
                    "properties": {
                        "code": {
                            "type": "integer"
                        },
                        "message": {
                            "type": "string"
                        }
                    }
                }
            }
        }
    }

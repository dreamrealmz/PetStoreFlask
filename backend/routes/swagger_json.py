from flask import Blueprint

blueprint = Blueprint('swagger_json', __name__)


@blueprint.route('/swagger.json', methods=['GET'])
def swag():
    return {
        "openapi": "3.0.0",
        "info": {
            "version": "1.0.2",
            "title": "Swagger Petstore",
            "license": {
                "name": "MIT"
            }
        },
        "servers": [
            {
                "url": "http://localhost:5000/petstore_api"
            }
        ],
        "paths": {
            "/breeds": {
                "get": {
                    "summary": "List all breeds",
                    "operationId": "listBreeds",
                    "tags": [
                        "breeds"
                    ],
                    "responses": {
                        "200": {
                            "description": "List of breeds",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/Breeds"
                                    }
                                }
                            }
                        }
                    }
                },
                "post": {
                    "summary": "Create a breed",
                    "operationId": "createBreed",
                    "tags": [
                        "breeds"
                    ],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/BreedIn"
                                }
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Created breed response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/BreedOut"
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
            },
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
                "BreedIn": {
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
                "BreedOut": {
                    "allOf": [
                        {
                            "$ref": "#/components/schemas/BreedIn"
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                }
                            }
                        }
                    ]
                },
                "Breeds": {
                    "type": "array",
                    "items": {
                        "$ref": "#/components/schemas/BreedOut"
                    }
                },
                "PetIn": {
                    "type": "object",
                    "required": [
                        "name"
                    ],
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "breed_id": {
                            "type": "integer"
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
                        },
                        "breed_name": {
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

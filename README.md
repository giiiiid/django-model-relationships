swagger: '2.0'
info:
  title: Giiid Todo Snippet API
  description: Giiid's way
  termsOfService: https://www.google.com/policies/terms/
  contact:
    email: contact@snippets.local
  license:
    name: BSD License
  version: v1.0
host: 127.0.0.1:8000
schemes:
- http
basePath: /
consumes:
- application/json
produces:
- application/json
securityDefinitions:
  Basic:
    type: basic
security:
- Basic: []
paths:
  /postget/order/createapi/:
    get:
      operationId: postget_order_createapi_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
      tags:
      - postget
    post:
      operationId: postget_order_createapi_create
      description: ''
      parameters: []
      responses:
        '201':
          description: ''
      tags:
      - postget
    parameters: []
  /postget/order/updateapi/{id}:
    get:
      operationId: postget_order_updateapi_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Order'
      tags:
      - postget
    put:
      operationId: postget_order_updateapi_update
      description: ''
      parameters:
      - name: data
        in: body
        required: true
        schema:
          $ref: '#/definitions/Order'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Order'
      tags:
      - postget
    patch:
      operationId: postget_order_updateapi_partial_update
      description: ''
      parameters:
      - name: data
        in: body
        required: true
        schema:
          $ref: '#/definitions/Order'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Order'
      tags:
      - postget
    delete:
      operationId: postget_order_updateapi_delete
      description: ''
      parameters: []
      responses:
        '204':
          description: ''
      tags:
      - postget
    parameters:
    - name: id
      in: path
      required: true
      type: string
  /todo/list:
    get:
      operationId: todo_list_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
      tags:
      - todo
    parameters: []
  /todo/tdetail/{id}:
    get:
      operationId: todo_tdetail_read
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Todo'
      tags:
      - todo
    put:
      operationId: todo_tdetail_update
      description: ''
      parameters:
      - name: data
        in: body
        required: true
        schema:
          $ref: '#/definitions/Todo'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Todo'
      tags:
      - todo
    patch:
      operationId: todo_tdetail_partial_update
      description: ''
      parameters:
      - name: data
        in: body
        required: true
        schema:
          $ref: '#/definitions/Todo'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/Todo'
      tags:
      - todo
    delete:
      operationId: todo_tdetail_delete
      description: ''
      parameters: []
      responses:
        '204':
          description: ''
      tags:
      - todo
    parameters:
    - name: id
      in: path
      required: true
      type: string
  /todo/todo/:
    get:
      operationId: todo_todo_list
      description: ''
      parameters: []
      responses:
        '200':
          description: ''
      tags:
      - todo
    post:
      operationId: todo_todo_create
      description: ''
      parameters: []
      responses:
        '201':
          description: ''
      tags:
      - todo
    parameters: []
definitions:
  Order:
    type: object
    properties:
      id:
        title: ID
        type: integer
        readOnly: true
      location:
        title: Location
        type: string
        enum:
        - Bantama
        - Santasi
        - Abrepo
        - North
        - South
        x-nullable: true
      invoice:
        title: Invoice
        type: string
        maxLength: 150
        minLength: 1
        x-nullable: true
      delivery:
        title: Delivery
        type: string
        enum:
        - Pick up
        - Delivery
        x-nullable: true
      customer_name:
        title: Customer name
        type: integer
        x-nullable: true
  Todo:
    required:
    - name
    - desc
    - owner
    type: object
    properties:
      name:
        title: Name
        type: string
        maxLength: 200
        minLength: 1
      desc:
        title: Desc
        type: string
        minLength: 1
      is_complete:
        title: Is complete
        type: boolean
      owner:
        title: Owner
        type: integer

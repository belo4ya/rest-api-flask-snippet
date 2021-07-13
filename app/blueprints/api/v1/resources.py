from app.utils import status

from flask_restx import Namespace, Resource, fields


TODOS_MOCK = [
    {
        'id': 0,
        'title': 'Title 0',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                       'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    },
    {
        'id': 1,
        'title': 'Title 1',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                       'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    },
    {
        'id': 2,
        'title': 'Title 2',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                       'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    },
]

ns = Namespace('todos', description='todos description')

todo = ns.model('Todo', {
    'id': fields.String(readonly=True),
    'title': fields.String(),
    'description': fields.String(),
})


@ns.route('/<int:todo_id>')
@ns.param('todo_id', 'The Todo identifier')
class Todo(Resource):

    @ns.marshal_with(todo)
    def get(self, todo_id):
        return TODOS_MOCK[todo_id]

    @ns.expect(todo, validate=True)
    @ns.marshal_with(todo, code=status.CREATED)
    def put(self, todo_id):
        TODOS_MOCK[todo_id] = ns.payload
        return TODOS_MOCK[todo_id], status.CREATED

    @ns.response(status.NO_CONTENT, 'Deleted')
    def delete(self, todo_id):
        TODOS_MOCK.pop(todo_id)
        return '', status.NO_CONTENT


@ns.route('/')
class TodoList(Resource):

    @ns.marshal_list_with(todo)
    def get(self):
        return TODOS_MOCK

    @ns.expect(todo, validate=True)
    @ns.marshal_with(todo, code=status.CREATED)
    def post(self):
        new_todo = ns.payload
        new_todo['id'] = len(TODOS_MOCK)
        TODOS_MOCK.append(new_todo)
        return new_todo, status.CREATED


@ns.route('/batch')
class TodoBatch(Resource):

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

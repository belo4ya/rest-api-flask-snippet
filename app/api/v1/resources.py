from flask_restx import Namespace, Resource, fields

todos = Namespace('todos', description='todos description')

todo_model = todos.model('Todo', {
    'id': fields.String(),
    'title': fields.String(),
    'description': fields.String(),
})

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


@todos.route('/<int:todo_id>')
@todos.param('todo_id', 'The Todo identifier')
class Todo(Resource):

    @todos.doc('get_todo')
    @todos.marshal_list_with(todo_model)
    def get(self, todo_id):
        return TODOS_MOCK[todo_id]


@todos.route('/')
class TodoList(Resource):

    @todos.doc('list_todos')
    @todos.marshal_list_with(todo_model)
    def get(self):
        return TODOS_MOCK

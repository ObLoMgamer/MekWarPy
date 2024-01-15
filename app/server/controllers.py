# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from endpoints import Controller

class Default(Controller):
  async def GET(self):
    return "boom"

  async def POST(self, **kwargs):
    return 'hello {}'.format(kwargs['name'])

class Foo(Controller):
  async def GET(self):
    return "bang"

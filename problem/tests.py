from django.test import TestCase
from .models import Problem
# Create your tests here.


def add_fake_problem(problem_id):

    problem_id = str(problem_id)

    problem = Problem()
    problem.problem_id = problem_id
    problem.testset_id = problem_id
    problem.title = "A+B Problem"
    problem.description = "desc"
    problem.input_description = "input desc"
    problem.output_description = "output desc"
    problem.hint = "hint"
    problem.samples = '[{"input":"1 2", "output":"3"}, {"input":"4 5", "output":"9"}]'
    problem.public = True

    problem.save()


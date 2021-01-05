from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles

def make_div_node(self, classname, lines):
    div = nodes.container()
    div['classes'] = [classname]
    
    rst = ViewList()
    # Add the content one line at a time.
    # Second argument is the filename to report in any warnings
    # or errors, third argument is the line number.
    for line in lines:
        rst.append(line, "make_div.rst", 0)
    # Create a node.
    node = nodes.section()
    node.document = self.state.document
    # Parse the rst.
    nested_parse_with_titles(self.state, rst, node)        

    div.extend(node)
    return [div]

def visit_node(self, node):
    pass

def depart_node(self, node=None):
    self.body.append("</div><div class='api-section-body'>")

class ApiMainSectionAnnotation(nodes.General, nodes.Element): 
    pass

class ApiMainSectionDirective(Directive):
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = False
       
    def run(self):
        node = ApiMainSectionAnnotation()
        if self.arguments and len(self.arguments):
            node.extend(make_div_node(self, "api-section-annotation", [self.arguments[0]]))
        return [node]


def setup(app):
    app.add_node(ApiMainSectionAnnotation, html=(visit_node, depart_node))
    app.add_directive("api-section-annotation-hack", ApiMainSectionDirective)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      
      self.root = nodes_to_visit.pop(0)
    
      if self.root['id'] == id:
        result.append(self.root)

      nodes_to_visit = self.root['children'] + nodes_to_visit

    return result[0] if result else None

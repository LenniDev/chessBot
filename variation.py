class VariationRoot():
    children = []
    def __init__(self):
        self.children = []

    def appendChild(self):
        newChild = VariationNode(None,None)
        self.children.append(newChild)
        return newChild

    def getChildrenAsMoves(self):
        return [(child.move,child.evaluation, child)for child in self.children]

    def str(self):
        return f'Variation:\n' + ''.join([child.str(spacing=1) for child in self.children])

class VariationNode():
    def __init__(self,move,evaluation):
        self.move = move
        self.evaluation = evaluation
        self.children = []

    def appendChild(self):
        newChild = VariationNode(None,None)
        self.children.append(newChild)
        return newChild

    def getChildrenAsMoves(self):
        return [(child.move,child.evaluation, child)for child in self.children]

    def str(self,spacing):
        return spacing*'  ' + f'{str(self.move)} ({self.evaluation}):\n' + ''.join([child.str(spacing=spacing+1) for child in self.children])

if __name__ == '__main__':
    variation = VariationRoot()
    childNode1 = variation.appendChild()
    childNode2 = variation.appendChild()
    childNode11 = childNode1.appendChild()
    print(variation.children)

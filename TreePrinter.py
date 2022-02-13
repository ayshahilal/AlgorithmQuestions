class TreePrinter:
        
    def printTree(rs):
        
        tree={}
        childs = []
        # create a tree of parents and childs
        for relation in rs:
            childs.append(relation.child)
            if relation.parent not in tree:
                tree[relation.parent] = list()
            tree[relation.parent].append(relation.child)
        #print(tree)

        # find the parent that is not a child of any parent
        for relation in rs:
            if relation.parent not in childs:
                node = relation.parent
                break
        #print("node 0 :", node)

        TreePrinter.dfs(node, 0, tree)
        


    def dfs(node, level, tree):
        print("\t"*level,node)
        if node in tree.keys():
            children = tree[node]
        else:
            return
        
        for child in children:    
            TreePrinter.dfs(child, level+1, tree)

if __name__ == '__main__':

    rs = []

    rs.append(Relation("animal", "mammal"))
    rs.append(Relation("animal", "bird"))
    rs.append(Relation("lifeform", "animal"))
    rs.append(Relation("cat", "lion"))
    rs.append(Relation("mammal", "cat"))
    rs.append(Relation("animal", "fish"))
    
    TreePrinter.printTree(rs)

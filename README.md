Here are some example questions and codes that I have written. 
# TreePrinter: 
  Write a function, printTree(), which prints a given tree. 
  Details:
  * The argument of printTree is a stream of Relations: pairs of "parent -> child" relationships.
  * Each parent can have many children. 
  * The input list may contain Relations in any order
  * The order in which the pairs appear in the input list determines the nodes order with respect to its siblings.


Example input: 

rs.append(Relation("animal", "mammal"))

rs.append(Relation("animal", "bird"))

rs.append(Relation("lifeform", "animal"))

rs.append(Relation("cat", "lion"))

rs.append(Relation("mammal", "cat"))

rs.append(Relation("animal", "fish"))
  
Expected output:

lifeform

  animal 
  
    mammal
    
      cat
      
        lion
        
    bird
    
    fish

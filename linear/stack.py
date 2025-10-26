

"""
1. push() = insert/push element into top of stack
2. pop() = returns the top most element from stack reducing its size
3. top() = only returns the value of top most element without modifying stack
"""

# Initialise Global Variables
STACK_SIZE = 6

stack = [""] * STACK_SIZE

top_of_stack = -1


"""Function to PUSH an element into Stack"""
def push(element):
  global top_of_stack
  if top_of_stack < STACK_SIZE - 1:
    top_of_stack += 1
    stack[top_of_stack] = element

"""Function to POP an element into Stack"""
def pop():
  global top_of_stack
  if top_of_stack >= 0:
    element = stack[top_of_stack]
    top_of_stack -= 1
    return element
  else:
    return None

"""Function to TOP an element into Stack"""
def top():
  global top_of_stack
  if top_of_stack >= 0:
    element = stack[top_of_stack]
    return element
  else:
    return None


def is_valid(s):

  # PUSH Logic: If opening brackets are identified, push them into stack
  for i in s:
    if i == "{" or i == "(" or i == "[":
      push(i)

    # POP Logic: If closing brackets are identified, check for it's opening
    elif i == "}" or i == ")" or i == "]":
      check = top()
      if check is None:
        return False

      # Parenthesis
      elif i == "}":
        if top() == "{":
          pop()
        else:
          return False

      # Regular Brackets
      elif i == ")":
        if top() == "(":
          pop()
        else:
          return False

      # Square Brackets
      elif i == "]":
        if top() == "[":
          pop()
        else:
          return False

    else:
      print("Please enter brackets.")
      return False

  if top_of_stack == -1:
    return True
  else:
    return False

def main():

  string = input("Input s: ")

  result = is_valid(string)

  print("Output:", result)


if __name__ == "__main__":
  main()

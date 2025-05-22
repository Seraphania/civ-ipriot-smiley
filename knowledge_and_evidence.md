<style>

body {
    counter-reset: h2counter;
}

/* H1 - No numbering */
h1 {
    /* No counter reset or increment */
}

/* H2 - Level 1 numbering */
h2 {
    counter-reset: h3counter;
}

h2::before {
    counter-increment: h2counter;
    content: counter(h2counter) ". ";
}

/* H3 - Level 2 numbering */
h3 {
    counter-reset: h4counter;
}

h3::before {
    counter-increment: h3counter;
    content: counter(h2counter) "." counter(h3counter) " ";
}

/* H4 - Level 3 numbering (optional) */
h4 {
    counter-reset: h5counter;
}

h4::before {
    counter-increment: h4counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) " ";
}

</style>

# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## Required evidence

### Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file


**Project Directory**
![Project Dirctory](./screenshots/project-directory.png)  
![main.py execution](./screenshots/mainpy-execution.png)  


~~If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:~~  
```bash
ls
python3 main.py
```

### Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name       | value             |
   | ----------              | ---------- | ------------------|
   | built-in primitive type | dimmed     | True              |
   | built-in composite type | WHITE      | (255, 255, 255)   |
   | user-defined type       | Smiley     | N/A               |

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type                    |
   | ------------------------ | ----------------------- |
   | self.pixels              | List                    |
   | A member of self.pixels  | String                  |
   | self                     | Smiley                  | ### Come back to this

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow | File      | First line                | Line range  |
   | ------------ | ----------| ------------------------- | ----------- |
   |  sequence    | smiley.py | `YELLOW = (255, 255, 0)`  | 8-26        |
   |  selection   | sad.py    | `if wide_open:`           | 25-29       |
   |  iteration   | happy.py  | `for pixel in mouth:`     | 21-22       |

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used? | Example |
   | ----------------------- | ----- | --------|
   | int                     | Y     | 42         |
   | float                   | Y     | 0.25       |
   | str                     | N     | "Cat"      |
   | bool                    | Y     | True       |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

   > `WHITE = (255, 255, 255)` is a class variable - defined within the main body of the class.
   > `self.pixels = [...]` is an instance variable - defined after the initializer.
   > 
   > `WHITE` remains constant across all smileys, however 'pixels' values may vary bwtween different instances of smilieys.

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?
      > The constructor is `def __init__(self):` which will create an instance of the class (in this case Happy)

   2. What statement(s) does it execute (consider the `super` call), and what is the result?
      > It first initialises the attributes of 'Smiley' and Blinkable' with the `super().__init__()` method.
      > Then the attributes of Happy Smilieys are defined - they have a mouth and eyes. `self.draw_mouth()` `self.draw_eyes()`

### Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:
   > PEP8. It is likely that the SenseHat module uses the same style.  
   > This is indicated by the naming convention (CapWords/PascalCase) of the SenseHat class that is encapsulated in smiley.py, and the way it's methods are called (and their naming conventions). for example: `self.sense_hat.set_pixels(self.pixels)`

2. List three aspects of this convention you see applied in the code.
   > Naming conventions eg in classes, methods, variables, contants etc.  
   > The style and consistent use of docstrings on all public funtions etc.
   > Consistent use of 4-space indentation.

3. Give two examples of organizational documentation in the code.
   > "# We have encapsulated the SenseHat object" - smiley.py  
   >     """
         Set the SenseHat's light intensity to low (True) or high (False)
         :param dimmed: Dim the display if True, otherwise don't dim
         """  - smiley.py  

### Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s) |
| ---------- | ------------- | ---------------- |
| Smiley     | Super         | N/A              |
| Blinkable  | Super (ABC)   | N/A              |
| Happy      | Sub           | Smiley, Blinkable|
| Sad        | Sub           | Smiley           |

2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)
   > Abstraction is making use of the functionality of code without worrying about it's impleentation. for example main.py makes use of the various modules to implement `smiley = Happy()` etc. The defenition and implementation of what a 'smiley' is, and what 'happy' is, are defined elsewhere.

3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)
   > Inheritance. In this project it is used to make objects re-useable, and buildable. so "Happy" and "Sad" take a base "Smiliey" and each can modify it in different ways, without having to each redefine what a base smiliey is.

### Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > The mouth shape is different to express the different states (happy/sad)
   
2. What are the key similarities?
   > Both happy and sad smileys are types of smileys. They both have eyes and a mouth, although these behave differrently for each type of smiliey.
   
3. What difference stands out the most to you and why?
   > The happy smiley has Blink functionality. This is a design choice that has meant that the code to render eyes is repeated in both classes (although in slightly different forms).
   
4. How does this difference affect the functionality of these classes
   > Sad smileiys do not have the ability to blink as htey have no blink() method.


### Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   > smiley, happy, sad.
   
2. Which of these classes directly interact with the SenseHat functionalities?
   > smiliey
   
3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > The sensehat is encapsulated by the statement `self.sense_hat = SenseHat()` This allows the functionality of the Sensehat to be used, but does not expose it's code.
   > Not exposing tyhe sensehat's code prevents accidental interferance with it.

### Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.
   > Yes, the Blinkable abstract base class was included to make that functionality available. However, the author did not think that all smilies *must* be able to blink, or it would have been included in the smiley base class.

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.
   > All instances of the happy smiley can blink. The author expects that all blinking smileys *should* blink for 0.25 second. This is included as an argument in the blink method `def blink(self, delay=0.25):`. It can however be overridden by specifying a different delay time when calling the method in main.py, so the author did not think they had to blink the same way.

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.
   > Polymorphism is implementing the same behaviour in different ways. For example if Sad smilies had a blink method, it might be different (perhaps a slow blink), but couuld be called in the same way as a happy smiliey's blink. Both are blinks even if they look different.

4. How is inheritance used in the blink method, and why is it important for polymorphism?
   > the blink method inherits from the abstract class Blinkable. This is what allows polymorphism to be achieved.

5. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python   
   def blink(self, delay=0.25):
       pass  # Replace 'pass' with your implementation
   ```

6. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

7. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

> ![Sad Smiley Blinking](./screenshots/sad_blinking.png)  
> ![Modified main.py](./screenshots/modified_main.png)  

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.
  > No issues, I did choose not to remove the code for the happy smilie in `main.py`, and noted that it executed a second instance of the mock sensehat window for sad. This is understandable as smiley.show() initialises the sensehat each time it is run. I wonder what would happen with a real sensehat?

  ### If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.
     > Abstract Base Class (ABC)

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.
      > It is an interface as it contains abstract methods.

  1. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.
      > Abstraction; it identifies and exposes functionality, but it doesn't implement it itself.

  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.
      > The sad class was modified to have it's own `blink()` method, it does not need to refer to the abstract method.

  1. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.
      > Duck Typing. Typology doesn't need to be explicitly defined in dynamically typed languages, it does in statically typed languages though.

  ***

  ## Refactoring

  ### Does a Smiley Have to Be Yellow?
  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > WHITE, GREEN, RED, YELLOW and BLANK are defined in the smiley class. No other classes define colours, these are constants.
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > The short sting variables 'Y' and 'O' the only ones implemnted in the smiley class. Whether the colours are displayed or not can change, the colours themselves can't.
     3. Add the color blue to the appropriate class using the appropriate format and values.

  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > Happy, Sad and Smiley.

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > change line 16 in smiley.py: `Y = self.YELLOW` to `Y = self.GREEN` - yep didn't even bother changing 'Y' to 'G', definately bad, but easy!, also the 'eyelids' remain yellow during blink.

  Here's a revised version of the "Flexible Colors – Step 1" section for the smiley project, incorporating your specifications for formatting and content updates:

  ### Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.
      > Abstraction.

  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.

  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

  ![Bulk Rename](./screenshots/bulk_rename.png)

  1. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  2. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***

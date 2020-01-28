## Lines Challenge (Python)

### Given
* A list of 2D (all different) points: (x_1, y_1), ..., (x_K, y_K);
* numbers use floating point representation.

### The goal
* to find all _lines_ that have more than two points on them from the input set.

---
As known from basic geometry, one can draw a straight line through(not between,
because it becomes a segment) any two such points.
You can choose any way to represent a line, but the common one is:

`y = a*x + b`

### Test
**Input:** `[(0, 0), (1,1), (3,5), (2,2)] `

**output:** `{a: 1, b: 0}`

because this line has three points from the input set: `[(0, 0), (1,1), (2,2)]`.

### Solution
I have BA in math and IT, but my specialization is Web development. So it may be a faster solution then I found,
but the goal of that is to present my stack and style, so the system of 2 equations is:

    y1 = a*x1 + b
    y2 = a*x2 + b

then

    a = (y1-y2) / (x1-x2)
    b = y1 - a*x1

by adding 3d point to the system, we now have:

    y3 = a*x3 + b  # True/False

so in fact, we are not making a lines by 2 points, but checking triples of points
if the third point fits 2 previous equations.

### Run it!

That is simple, you need to have Docker installed, then run

    docker-compose build points

after we have it built, you may run tests:

    docker-compose run --rm points pytest

That should work. I like that way to deliver a product, because it's simple to keep README up to date with
deploying on a random machine. Python virtual environment or Vagrant is a previous century...

### Updates
* I missed a possibility that a coordinate may be float, in fact it is required by the "Given" section - fixed.

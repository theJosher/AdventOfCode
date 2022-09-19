# Snail day

## Part 1
Recursion on the binary tree seemed the natural choice for this one, and as the problem set was only 100 lines, there were no tricky efficiency gotchas hiding in the problem. It wasn't clear at first whether values in a pair of normal numbers count for left and right explode targets, but the last part of the first example made that obvious after a point. Also, to not have tons of code, I did things a little awkwardly, using some extra variables to maintain references to python objects that they can be modified after returning from the explode (finding everything first and then performing the replace intuitively seemed the most tenable). Everything about this was easy except for that much of how explode works wasn't explicitly stated, but rather had to be inferred from examples. Easy to get, but TBH difficult to code in a way that is highly legible. That said, it could probably could use some cleanup, but as usual, this isn't meant to be perfect.

## Part 2
Main way I tripped myself up here is forgetting that I was modifying the input space. Shortcuts can cut both ways! Either way, Part 2 was a no-brainer, especially after mention of the commutative bit.
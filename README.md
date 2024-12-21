# Convert MD docs to CSV

Input docs have the format

```
## Question 1
Answer line 1
Answer line 2
Answer line 3
...etc


## Question 2
Answer line 1
Answer line 2
Answer line 3
...etc

... and so on
```

Output csv has the format

```
"Question 1","Answer line 1\nAnswer line 2\nAnswer line 3"
"Question 2","Answer line 1\nAnswer line 2\nAnswer line 3"
... etc
```

Input must be called "input.md"

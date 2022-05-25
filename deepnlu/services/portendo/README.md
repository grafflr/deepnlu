# Oortendo: to predict
This microservice performs the classification of parse results

https://github.com/grafflr/graffl-core/issues/169


## Usage
Inspect `portendo/tests/driver.py` for API usage



## Classification via Mapping
Classification of Unstructured Text is a mapping exercise

The mapping is composed of these elements
1. Include One Of
2. Include All Of
3. Exclude One Of
4. Exclude All Of

The classifier will map extracted entities from unstructured text using the listed elements.

for example,

```yaml
TEST_INTENT
  - include_one_of:
    - alpha
    - apple
  - include_all_of:
    - beta
    - gamma
  - exclude_one_of:
    - delta
  - exclude_all_of:
    - epsilon
    - digamma
```

This intent will be selected if the set of extracted entities has either `alpha` or `apple` and has both `(beta, gamma)`. The intent will be discarded if `delta` occurs or if both `(epsilon, digamma)` occur.

In python, everything can be loaded into a native set structure and use native operations like `difference`, `intersection`, `union`, and `symmetric difference`. 

Because all set operations are native (underlying C modules), it's extremely fast to find an accurate classification.

The system adds more smarts by figuring out what to do if the rule states `delta` is excluded, and a descendant of `delta` is present. 

Or if `alpha` should be included and a sibling or child of `alpha` is present, etc. 

In this case, I usually rely on a heuristic to boost or lower confidence and tweak that overtime to get a good result.
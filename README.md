# RAFT
Refer to the [RAFT](https://arxiv.org/pdf/2403.10131) paper

# Known Issues
- [ ] Split by "=====" did not work for a few questions, 3 in total
- [ ] The order question-answer-chunk_index was not consistent, 2 occurrences
- [ ] Did not add chunk index, 2 occurrencese  
  
<i>ps. I'd recommend to run the question and CoT part separately, generate the QA pairs and make sure they are in the correct format.</i>

# Sample Output
```
Who typically works the fields in the village?
-----
assistant: To answer the question "Who typically works the fields in the village?" based on the provided context:

1. Tardo asked Saranta about the fields, noticing that no one was working them. Saranta mentioned that their labor supply is transient, indicating that the villagers do not typically work the fields.
2. Saranta explained that laborers from other towns or beyond are the ones who work the fields for a wage.
3. The context does not provide specific details about the demographics or identities of the laborers who work the fields, but it is clear that it is not the villagers themselves.

Therefore, based on the context, the answer to the question is: Laborers from other towns or beyond typically work the fields in the village.
-----
The laborers from the next town or beyond.
-----
```

# Acknowledgement
[Disqualified by Charles L. Fontenay](https://www.gutenberg.org/ebooks/30251)  
[RAFT](https://arxiv.org/pdf/2403.10131)  
[LLMA indexig RAFT datapack](https://github.com/run-llama/llama_index/tree/main/llama-index-packs/llama-index-packs-raft-dataset)

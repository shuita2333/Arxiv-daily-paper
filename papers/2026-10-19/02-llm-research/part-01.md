# 🧠 大模型相关研究 | 2026年10月19日

> 本类共 **321** 篇论文：已确认 **300** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-321](./part-07.md)

---

### 1. [BD-HazardVLM: Probing Vision-Language Models for Latent Defensive-Driving Hazards in Bangladesh Road Scenes](https://arxiv.org/abs/2610.20627)

**<font color=#1a73e8>作者：</font>** Abdullah Al Maruf, Md. Sajedul Islam, Tanmoy Mridha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly used for driving-scene understanding, yet their defensive reasoning under weakly structured Global South traffic remains unclear. We introduce BD-HazardVLM, a diagnostic benchmark of 500 Bangladesh road-scene images, comprising 375 from RSUD20K and 125 from TFP-BD, annotated for hazard presence, primary hazard category, risk timing, severity, defensive actions, visible evidence, and hallucination- and Western-road-bias traps. We evaluate Qwen2.5-VL-7B, InternVL3-8B, and MiniCPM-V-4.6 using a shared zero-shot task definition and structured output schema. Binary hazard-presence accuracy ranges from 88.0 percent to 89.2 percent, essentially matching the 89.0 percent majority-class baseline. Fine-grained reasoning is substantially weaker: category accuracy remains below 40 percent, risk-timing accuracy ranges from 1.6 percent to 12.4 percent, and exact defensive-action matching remains below 2 percent. Although InternVL3-8B achieves the highest severity accuracy at 61.2 percent, it has zero recall on the 58 high-severity cases. Qwen exhibits severe category mode collapse, while all models show weak latent-hazard anticipation and near-zero self-reported trap recognition. For the evaluated models, these findings show that coarse hazard recognition does not imply reliable fine-grained defensive-driving reasoning and motivate geographically diverse safety evaluation.

---


### 2. [PRISM: PRIvileged Sibling-guided Multi-Agent Topology Design](https://arxiv.org/abs/2610.20628)

**<font color=#1a73e8>作者：</font>** Phuong Tuan Dat, Qi Li, Xinchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) based on large language models (LLMs) have become a powerful way to address complex problems, and their effectiveness depends critically on the collaboration topology that decides which agents participate and how they communicate. Recent work learns to generate this topology from the task query, fitting the generator to corpora of execution-verified graphs. The post-training method for such generators remains a limitation: a corpus lists the graphs that solved a query but never ranks them, leaving continued supervised fine-tuning (SFT) with no per-query preference to exploit. Without such a preference, the generator drifts toward the topologies the corpus contains most often rather than those that suit each query, so a gain on one task can come at a cost on another. We propose PRISM, which recovers per-query signal from the same corpus by learning with privileged information: a teacher reads, through a zero-initialized low-rank branch, a sibling graph that also solved the query and is unavailable at deployment, and the student matches its per-decision targets on trajectories the student samples itself. Across six diverse benchmarks PRISM improves over every topology-design baseline evaluated, and matched-teacher controls support the contribution of privileged query information. Code is available in this link.

---


### 3. [A Large-Scale Dataset for Multi-Class Financial News Classification in Brazilian Portuguese](https://arxiv.org/abs/2610.20630)

**<font color=#1a73e8>作者：</font>** Leomax Bandeira, Gabriel Aguiar, Dalton Cézane Gomes Valadares 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The development of Financial Natural Language Processing (NLP) systems for Brazilian Portuguese is hindered by the scarcity of domain-specific datasets. To address this, we present a large-scale corpus of approximately 160,000 Brazilian Portuguese financial news articles collected from web sources. To establish initial benchmarks for a weakly supervised multi-class classification approach based on semantic similarity, we annotated subsets of this corpus both manually and using a Large Language Model (LLM). We evaluated three similarity-based methods -- cosine similarity, K-Nearest Neighbors (KNN), and FAISS-based nearest-neighbor search -- using multilingual semantic embeddings. Our experiments reveal that the task is highly sensitive to label quality and class distribution. On the manually labeled subset, KNN achieved the best performance (47.3% accuracy, 31.9% F1-score), closely followed by FAISS. Conversely, on the LLM-annotated subset, while accuracy reached approximately 50%, F1-scores dropped to near 20%, highlighting the negative impact of label imbalance and noisy weak annotations. These findings establish foundational baselines for a challenging task, underscoring the critical need for high-quality manual annotations. Ultimately, this dataset and our preliminary results provide a reference point for future research in Brazilian Portuguese Financial NLP.

---


### 4. [Real-time Chatbot Romance Scam Detection in Stage Classification](https://arxiv.org/abs/2610.20631)

**<font color=#1a73e8>作者：</font>** Yi-cheng Liu, Guan-ru Lai, Yi-cheng Lai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Romance scam has become a serious problem via social media, and the improvement of artificial intelligence enable to fake identify easily. In the study, a chatbot has developed to detect romance scam in real-time through Line Messaging API. Using the seven stage theories in the social science field, the stages of romance scam can be detected through large language model. In addition, once a romance scam is detected, the chatbot provides explanations of the stage and prevention advices through large language model. The contribution of the work provides a practical application, and can be used in real scenario for reducing the risk of romance scam.

---


### 5. [MeddeX: A Retrieval-Augmented LLaMA-3 System with Gemini Vision for Evidence-Backed Medical Report Analysis](https://arxiv.org/abs/2610.20632)

**<font color=#1a73e8>作者：</font>** Rajdeep Pandhare, Rohit Kundaikar, Yakub Kojar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern healthcare generates increasingly complex medical reports that challenge clinical professionals in terms of time and interpretive burden. Manual review processes are slow, error-prone, and difficult to scale. This paper presents MeddeX, a Medical Report Analyzer that combines a QLoRA fine-tuned LLaMA-3 (8B) model with Retrieval-Augmented Gen eration (RAG) and a multimodal Gemini Vision layer to deliver accurate, concise, and evidence-backed summaries of medical documents. The system handles text-native PDFs, scanned image based PDFs, and direct radiological images through an intelligent hybrid extraction pipeline that includes a novel garbage-text detection mechanism for corrupted and UTF-16-encoded doc uments. Beyond single-report Q&A, MeddeX introduces report scoped retrieval for precise contextual grounding, an automated longitudinal report comparison engine, and a self-healing backfill pipeline that lazily processes legacy documents on demand. A FastAPI backend, Supabase vector store, and this http URL fron tend complete the end-to-end architecture. Evaluation against the base LLaMA3-Med42-8B model demonstrates consistent improvements across ROUGE-1 (+9.2%), ROUGE-2 (+10.0%), ROUGE-L (+11.8%), BLEU (+71.4%), and BERTScore (+0.8%), validating the benefit of domain-specific fine-tuning. MeddeX represents a practical and robust step toward AI-assisted clinical decision support.

---


### 6. [Context Injection and Long-Horizon Reliability: Separating Duplicate Recognition, Local Processing, and Counter Tracking](https://arxiv.org/abs/2610.20633)

**<font color=#1a73e8>作者：</font>** Thomas Serval  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon failures of language models are usually measured as end-task success or as a horizon length. We instead score, step by step, three components of a 400-step ledger task in which every step is easy in isolation and the model's own answers are re-injected into its context: recognising a record already seen 5 to 300 steps earlier, processing the current record locally, and writing a counter incremented at every step. On Qwen3-8B (non-thinking, 20 seeds, replicated on a second machine and backend), with every step scored component by component, two results hold. First, duplicate-recognition errors rise late in the episode -- from 0.0019 to 0.011 per step at risk across step 200 -- while the counter makes no error in 8,000 steps and local processing is descriptively stable; the rise combines long-distance recall errors and rising false alarms. Second, a block of irrelevant content inserted before each step makes the counter fail in 20 of 20 seeds on each machine, against none without it, while its effect on local processing is much smaller and not distinguishable from none. Three pre-registered follow-ups probe the counter. Its value depends on the value present in the response history: a corrupted value persists without correction in every seed, and an exact external reminder, repeated before each message, re-aligns it within one to two steps. Under the irrelevant block, no counter error was observed when an exact compact reminder of the state, supplied externally by an oracle, preceded each message (0 of 20 seeds with an error, against 15 without it), and this reminder outperformed a length-matched neutral text; whether a single reminder suffices was not conclusive, and the absence of damage to the other components was not established. An aggregate or exclusive error classification can hide the difference we report.

---


### 7. [Jev-as-a-Judge for RAG Claim Verification: Confidence-Gated Cascading Between a Non-Generative Verifier and a Frontier LLM](https://arxiv.org/abs/2610.20634)

**<font color=#1a73e8>作者：</font>** Alden Do Rosario, Kirollos Atef  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation asks one question at volume: does this evidence support this claim? The answer is one bit, yet most pipelines obtain it from a text generator and pay generation prices for the prose wrapped around it. We compare a non-generative decision model, which returns a typed value from a declared enumeration together with a native probability and no text, against a frontier LLM configured as an engineer would deploy it for binary classification. Both answer the same 495 human-labelled claims from LLM-AggreFact, so every comparison is within-item. We report three things. First, the two systems are statistically indistinguishable on the metric this task is conventionally scored by, a paired difference of -0.56 points, Jev minus Astra, at a 187-fold cost difference. Second, that tie carries almost no information about deployment: the systems disagree on 15.2% of claims, and the cheaper one admits 23.2% of the claims annotators marked unsupported against the frontier model's 14.1%. A component whose job is to catch unsupported claims should be judged on that rate, and the conventional headline hides it. Third, because the errors differ they compose: routing the claims the cheap model is confident about and escalating the rest reaches 74.10 at USD 2.92 per thousand claims against 73.83 at USD 8.93, with the threshold chosen out of fold. But a matched random-escalation control at in-sample thresholds, spending the same budget by coin flip, does as well, so what buys the saving is the escalation share and not the probability that picks what to escalate. Measured against the cheap model it is built from, the cascade costs 61-fold more for 0.83 points, 95% CI [-3.36, 4.86], and it is the more permissive guard of the two. Equal accuracy conceals unequal errors. All predictions, prompts, pricing and code are released.

---


### 8. [Exploring the Design Space of Permutation Diffusion LLMs](https://arxiv.org/abs/2610.20635)

**<font color=#1a73e8>作者：</font>** Zhe Xu, Mingfu Liang, Kavosh Asadi 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Permutation generation with language models requires both text-conditioned ranking and a global one-to-one assignment between candidates and output positions. We study this problem through three diffusion-LLM parameterizations: hard-assignment prediction over shuffled candidate-index sequences, soft-assignment prediction over doubly stochastic matrices, and direct ordering-score prediction followed by sorting. The three families place permutation constraints at different stages of prediction and decoding and therefore support different training objectives and sampling procedures. We evaluate these designs on recommendation reranking across three Amazon domains with candidate sets of size 10 and 20. At one function evaluation, the hard- and soft-assignment variants achieve Recall@1 comparable to a constrained masked-diffusion baseline, whereas direct ordering-score prediction guarantees valid permutations without Hungarian assignment or Sinkhorn normalization. Additional function evaluations do not consistently improve ranking quality, and their effect depends strongly on the state representation and training objective. These results show that corruption, prediction parameterization, objective, and decoder should be designed jointly for permutation diffusion with language-model denoisers.

---


### 9. [Feature Elicitation for SAE Steering of Deceptive Behaviour in Small LLMs](https://arxiv.org/abs/2610.20638)

**<font color=#1a73e8>作者：</font>** J Koorndijk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Research on deceptive alignment is becoming increasingly urgent as frontier-model capabilities advance and their risk of causing catastrophic harm increases. Alignment faking is a form of deceptive alignment, with the compliance gap serving as a key behavioural indicator. This behaviour remains understudied in small LLMs and prior mechanistic interventions have not been shown to mitigate the compliance gap. We test whether steering SAE (sparse autoencoders) features associated with deontological ethics can mitigate this behaviour. We use a novel bag-of-words feature elicitation pipeline for SAE steering to identify what we construe as concept-level steering directions. Our approach reduced the compliance gap to non-significance in Gemma-3-27B-IT, whereas the tested configurations were not effective in LLaMA-3-8B-Instruct. Analysis of scratchpad traces also revealed deceptive model behaviour which we term deceptive defanging: deliberately degrading the aligned functionality of a response (in this case harmfulness) while preserving the appearance of alignment (in this case helpful compliance with the harmful request), sometimes conditioned on tier, training, or RLHF consequences. These findings provide, to our knowledge, the first evidence that a mechanistic activation-level intervention can mitigate the compliance gap in an alignment faking setup. They also identify a form of deceptive behaviour that may broaden our understanding of the different forms of deceptive behaviour in LLMs.

---


### 10. [Same Answer, New Box: How Much of RLVR's Out-of-Domain Gain Is Answer Format?](https://arxiv.org/abs/2610.20639)

**<font color=#1a73e8>作者：</font>** Zongye Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) is credited with gains beyond the domain its rewards check, such as higher MMLU accuracy after training on mathematics. Such accuracies are usually read out of the model's text by an answer extractor. A model that learns to write its answer where the extractor looks can therefore score higher without answering better. We measure how much of the gain reported by extractors copied from public code arises this way. We generate outputs from a base model and its RL model and score them twice: with those extractors, and with one extractor of our own that reads a stated answer whether it is in the answer box \boxed{} or in the text. On four released 7B SimpleRL base-RL pairs, 82% of the out-of-domain multiple-choice gain that these extractors report disappears under ours: it is a gain in answer format, not in answers. The base models already state most of their answers in text, and RL moves them into the box, where these extractors look first. Independent LLM readers, in place of our extractor, put the figure at 77%. With a prompt that itself asks for the box, our extractor puts it at 79%. On a 32B pair trained with another recipe, almost none of the reported gain is format gain: its base model boxes its answers when asked, and its RL model rarely does when not. A reported gain is partly a property of the extractor that read it, and re-scoring stored outputs with a second extractor shows how much, without re-running RL.

---


### 11. [AbridgeKV: Compressing Long Reasoning into the KV Cache of Learned Pause Tokens](https://arxiv.org/abs/2610.20641)

**<font color=#1a73e8>作者：</font>** Jack Cai, Lijie Yang, Vasilis Kontonis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long chain-of-thought decoding is memory-bound: the KV cache of the generated tokens grows linearly with the test-time compute being spent. Evicting cache entries does not fix this, because a model never trained on a cache with entries removed generates longer, often up to the length limit. We instead train the model to compress its own output. AbridgeKV compresses each completed block of generated text into the KV entries of a few learned pause tokens. These are extra input tokens with trained embeddings that produce no output. Once the pause tokens have encoded the block, AbridgeKV frees the block's original cache; subsequent tokens attend to the pause tokens' KV entries in its place. Three novel choices make this work: the pause tokens' KV entries take positions inside the block they replace, the cache budget is allocated across layers according to the measured value of each layer's entries, and compression operates on relatively large blocks. On 446 competition problems from AIME, HMMT, AMC, BRUMO, CMIMC and SMT with 32K-token generations, keeping a quarter of the generated cache matches an identically trained full-KV model in accuracy and output length; the strongest published evictor at a matched budget writes far longer, and the closest trained compressor, retrained on the same data, loses 10 points. Served in vLLM, the cache is 3.5x smaller per sequence and a saturated H100 finishes a problem 3.2x faster than with full KV.

---


### 12. [CoTS: Competitive Token Selection for Latent Reasoning in Large Language Models](https://arxiv.org/abs/2610.20642)

**<font color=#1a73e8>作者：</font>** Jie Yu, Yuxi Sun, Zhaoxu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent latent reasoning methods move beyond discrete Chain-of-Thought (CoT) by replacing sampled tokens with continuous soft embeddings or hidden states, enabling richer intermediate representations and preserving alternative reasoning paths. However, the need for latent reasoning varies across decoding steps: confident predictions favor discrete commitment, whereas ambiguous steps benefit from preserving multiple plausible alternatives. Existing approaches typically handle this variation through either global soft activation or hard switching based on uncertainty thresholds, treating latent intervention as an all-or-nothing decision rather than continuously adapting its strength. To address this limitation, we propose Competitive Token Selection (CoTS), a training-free framework that reframes latent intervention from binary mode selection into continuous allocation at the token level. CoTS uses the probability competition between the two most likely candidates to dynamically balance discrete commitment and soft exploration at each reasoning step. The second candidate represents the strongest alternative to the model's preferred continuation, so the separation between the two directly reflects the stability of the current discrete choice. When one candidate clearly dominates, CoTS keeps the representation close to the sampled discrete token to preserve a stable reasoning trajectory; as the competition strengthens, it increases the contribution of the soft representation to retain plausible alternatives. This competition-based allocation requires neither manually tuned switching thresholds nor mixing coefficients, and introduces no additional forward passes. Experiments across six reasoning benchmarks demonstrate that CoTS consistently outperforms standard CoT and state-of-the-art training-free latent reasoning methods. Our code is available at this https URL.

---


### 13. [Unmasking the Secret Code: Using Canaries to Show How Masked Context Controls Memorization in SFT](https://arxiv.org/abs/2610.20656)

**<font color=#1a73e8>作者：</font>** Avi Schwarzschild, Om Thakkar, Sahra Ghalebikesabi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Canaries, or synthetic training records containing known secrets, are widely used to assess whether language models reveal information from their training data. But how much do these measurements depend on the canaries themselves? We study this question through controlled fine-tuning experiments with language and vision-language models, spanning synthetic tasks and tasks where training improves useful performance. Whether a secret is provided in the training input strongly changes what the model learns; for example, models can reproduce a secret in the input yet fail to recall it when it is removed, even after extensive repetition during training. When training instead requires predicting the secret from the surrounding context, later recall can become reliable. Repetition alone is therefore insufficient to characterize memorization. We also find that changing when a canary appears, or which other canaries accompany it, can substantially change measured memorization without increasing that canary's repetition count. These results show that canary measurements depend on how secrets are presented during training and tested afterward. Audits should test whether their conclusions hold across these choices before extending them to other training records.

---


### 14. [The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock](https://arxiv.org/abs/2610.20665)

**<font color=#1a73e8>作者：</font>** Ningxin Pan, Hanyu Li, Yeqing Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can solve complex interactive tasks, yet reasoning and tool calls take time. In continuously changing environments, an otherwise correct action may arrive too late. We introduce RealtimeBench, with 180 tasks across six game types, to evaluate agents while games continue running during inference. Paired evaluations show that GPT-6.1-sol outperforms the faster Jev when games are paused, but falls behind when they keep running. We propose Two-Timescale Offline Recursive Self-Improvement (TORSI): a slow teacher studies failures and tests corrections in paused games between attempts, then writes reusable instructions for a fast student. The student acts without teacher calls during gameplay, and validation scores determine which updates are adopted. Two rounds raise Jev's average test score from 13.51 to 24.19 on a 0--100 progress scale, improving all six game types. The instructions also improve average scores for three other models without retuning. These findings point toward real-time intelligence: enabling powerful LLM agents to remain effective in a continuously changing world by organizing deliberation, learning, and action across timescales.

---


### 15. [CascadeLedger: Counterfactual Auditing of Information and Resource Integrity in LLM Cascades](https://arxiv.org/abs/2610.20668)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce CascadeLedger, a counterfactual execution-audit framework for budgeted language-model cascades. The protocol enforces call-before-read semantics, binds successful reads to service and cache identities, records availability and component-wise budget transitions, and freezes the event trace before any target or task scorer is joined. The central object is aggregate-equivalent trace validity: two executions can share a final answer, declared resource projection, and service histogram while differing in whether their routing decisions used only legitimately observable information. We complement single-trace invariants with counterfactual prefix non-interference (CPNI), which couples a visible prefix and policy randomness while changing only a declared hidden family. The counterfactual influence frontier (CIF) localizes the earliest violating prefix and a minimal hidden witness; projection-preserving adversarial mutation (PPAM) searches for invalid traces that remain acceptable to a non-counterfactual checker. Across frozen-cache, independently generated, and serving evaluations, the two-layer audit reports a clean false-positive rate of 0.0000, detects 0.9983 of serialized faults and 0.9982 of unlogged hidden-read faults, and changes 0.3403 of corrupted quality-resource conclusions after deterministic recomputation. The online recorder and offline CPNI audit have separate overhead measurements. Learned routing and semantic verification provide downstream compatibility studies under the same execution contract.

---


### 16. [Counterfactual Neighborhood Risk Fields: Evidence-Grounded Selective Safety for Vision-Language Models](https://arxiv.org/abs/2610.20679)

**<font color=#1a73e8>作者：</font>** Tianshi Wang, Jingsong Wang, Fengling Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Representation-based safety defenses for vision-language models (VLMs) often learn to separate harmful from benign inputs, but separation alone does not establish what a risk score means or when it should be trusted. We introduce Counterfactual Neighborhood Risk Fields (CNRF), an evidence-grounded framework for selective VLM safety. CNRF constructs context-matched benign-harmful counterfactual pairs, uses their representation differences as capability-related risk directions, and estimates neighborhood support separately from risk. This separation prevents unfamiliarity from being conflated with harmfulness and enables selective intervention rather than blanket rejection. A victim-adaptive interface accommodates different safety observations across VLM architectures and routes selected requests for same-victim response review, which either releases acceptable candidates or produces constrained alternatives with reduced harmful capability. Across three VLMs and five multimodal jailbreak families, CNRF achieves 86.06-89.30% macro defense success rate while retaining substantial benign-task utility. Controlled experiments further show that query-matched references and preserved context-direction correspondence materially improve risk ranking in the low-false-positive regime. CNRF thus reframes representation-based VLM safety from learning harmfulness boundaries to constructing applicable evidence for selective risk decisions.

---


### 17. [Diminishing Returns of Data in Sparse Autoencoders: Functional Behavior does not Guarantee Feature Reproducibility](https://arxiv.org/abs/2610.20680)

**<font color=#1a73e8>作者：</font>** Sambit Ghosh, Madelyn Mathai, R. Venkatesh Babu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are typically trained on hundreds of millions to billions of activation tokens, yet little work has tested whether this scale is necessary. We study how much activation data SAEs need by training four SAE architectures on three language models with budgets ranging from 5M tokens to a 500M-token reference. We measure two notions of convergence: functional behavior on standard evaluations and one-to-one reproducibility of learned features. Functional data requirements are strongly metric-dependent: reconstruction often approaches the full-data reference at substantially smaller budgets, whereas feature reproducibility continues to improve with data. For Gemma-2-2B BatchTopK, the fraction of strictly matched features rises from 2\% at 5M tokens to 29\% at 50M. Data selection also matters: random sampling better preserves the original activation distribution and generally favors reconstruction, whereas diversity-based sampling frequently improves AutoInterp. A theoretical analysis separates statistical consistency of subsampled training from the stronger identifiability and optimization conditions required for one-to-one feature recovery. Our results show that SAE training can often be made far more data-efficient when budgets are matched to the goal, and feature-level claims are backed by explicit reproducibility checks, paving the way toward cheaper and more reliable SAE research.

---


### 18. [IneqAgent: Agentic Inequality Proving in Lean with Symbolic Computation](https://arxiv.org/abs/2610.20681)

**<font color=#1a73e8>作者：</font>** Gaolei He, Jinhui Li, Ruobing Zuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formal inequality proving requires mathematical reasoning and exact computation, often connected through intermediate lemmas and goal reformulations. We introduce IneqAgent, an agentic framework combining LLM reasoning with symbolic computation for inequality proving in Lean4. Lemma-level Monte Carlo Tree Search coordinates lemma construction, goal reformulation, and symbolic backend selection. Complementary sum-of-squares, Bernstein, and successive difference-substitution backends produce exact certificates for local Lean proof generation. The agent integrates these proofs with LLM-generated steps and uses Lean feedback to construct complete proofs checked against the original theorem statements. On four benchmarks, IneqAgent with DeepSeek-V4-Flash solves 175 of 186 problems (94.09%), achieving the highest overall success rate among the evaluated methods. Across four backbones, it achieves higher success rates at low LLM inference cost thresholds than Direct Agent using the same backbone, with lower mean inference costs over each method's successful runs. We also obtain Lean-verified strengthenings of Dittert's conjecture in dimensions four and five, and certify the Holens--Djokovic $(4,4)$ inequality, implying Merris's conjecture in dimension four.

---


### 19. [TurboMamba: Faster Inference, Faster Training, and Better Prediction with Lexical Memory](https://arxiv.org/abs/2610.20682)

**<font color=#1a73e8>作者：</font>** Hanxin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce TurboMamba, a language-model architecture for faster inference, faster training, and better token prediction. A global Mamba-3 model runs once per completed token block. A small Transformer uses this global context and earlier tokens within the block to predict the next token. Three lightweight additions improve local predictions: direct access to the previous block's last token, a small correction to next-token scores, and a learned mixture with recent-token frequencies. We compare twelve small-scale implementations on public FineWeb-Edu, with comparable parameter counts and shared training-budget caps. The baselines include Transformer, Mamba-3, Jamba, and Zamba. The Jamba and Zamba versions use Mamba-3 in place of their original Mamba modules. TurboMamba achieves the lowest mean test prediction loss (negative log-likelihood, NLL) among all twelve models. Its mean NLL is 9.4% lower than that of Mamba-3, 7.3% lower than that of the Jamba version, and 18.3% lower than that of the Zamba version. End-to-end training throughput is 2.60x that of Mamba-3, 2.81x that of the Jamba version, and 4.82x that of the Zamba version. We measure end-to-end batch latency for a batch of 32 sequences, each with a 256-token prompt and 128 generated tokens. On this workload, TurboMamba achieves a 3.12x speedup over Mamba-3, a 3.53x speedup over the Jamba version, and a 6.21x speedup over the Zamba version.

---


### 20. [L2G-SR: Learning to Guide LLM-based Symbolic Regression](https://arxiv.org/abs/2610.20685)

**<font color=#1a73e8>作者：</font>** Letian Huang, Xiangyu Wang, Haowei Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Symbolic regression searches for an equation that explains observed data. Numerical error is commonly used to guide the search, but it alone can favor an accurate surrogate over a candidate with the right structure. We propose L2G-SR, a framework for LLM-based symbolic regression that guides search with a learned structural verifier. We construct structural supervision signal using tree edit distance (TED), accounting for commutative operators and alternative expression forms. A verifier first aligns numerical observations with the formulas, then learns to score a candidate's structural similarity to the target formula. At search time, the target formula is hidden and the verifier complements numerical error in parent selection. An analyst then uses verifier feedback and diagnostic tools to propose revisions, which a generator converts into refined expressions. On LLM-SRBench, L2G-SR achieves state-of-the-art numerical fit, equation level accuracy and TED across the evaluated LLM backbones and domains. L2G-SR demonstrates the value of learned structural guidance for LLM-based symbolic regression.

---


### 21. [RoLaQ: Joint Rotation and Range Calibration for 2-Bit KV Caches in Multi-Head Latent Attention](https://arxiv.org/abs/2610.20686)

**<font color=#1a73e8>作者：</font>** Shiyu Ji, Peng Ling, Chen Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-head latent attention (MLA) compresses the content of a key-value cache into a shared latent per token, making low-bit storage attractive for long-context inference. At two bits, errors in this representation perturb both attention matching and value readout, with effects that depend on error direction and reconstruction scale. We introduce RoLaQ (Rotation-calibrated Latent Quantization), an offline method for joint rotation and range calibration. RoLaQ refines a shared rotation within subspaces defined by the frozen key and value projections, and jointly learns quantization ranges whose thresholds and reconstruction gains are coupled to control the shared signal's response. Prediction matching and attention-output supervision guide calibration with model weights frozen. Across three MLA models and six benchmarks, RoLaQ achieves the highest average accuracy among the compared 2-bit methods both without and with token protection. On DeepSeek-V2-Lite, an SGLang implementation provides 3.96 times the BF16 KV capacity under the same memory budget and 2.51 times its decode throughput with 256K input tokens.

---


### 22. [On-Policy Residual Learning for Diffusion Language Models](https://arxiv.org/abs/2610.20687)

**<font color=#1a73e8>作者：</font>** Yifan Yu, Yuqing Jian, Jisen Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual context is key to unlocking the speed-quality Pareto frontier of diffusion language models (DLMs) by carrying forward predictive distributions across denoising steps. Yet turning this seemingly simple mechanism into an effective learning paradigm is far from simple: there is no clear recipe for how residual context should be learned. We introduce ORL, a framework for on-policy residual learning in DLMs. Algorithmically, we identify that residual learning is inherently on-policy. ORL learns from model-induced residual trajectories on the fly and introduces an entropy-contraction objective that sharpens predictions as the model revisits its own predictions. System-wise, exact residual supervision requires capturing, retaining, and reprocessing many trajectory-dependent states. ORL co-designs the algorithm with asynchronous residual capture and transport, specialized block-diffusion attention, and packed compute-balanced training, making it practical at scale. On a 4B DLM converted from Qwen3-4B, ORL improves tokens per forward (TPF) by up to 6.2x and, with our dlmrt engine, end-to-end throughput by approximately 6.9x at comparable or better quality. In single-request serving on one H100, this mode achieves a stronger speed-quality Pareto frontier than autoregressive models with EAGLE3 and DFlash speculative decoding under both strict and relaxed verification, running 1.74x faster than DFlash at matched accuracy. ORL also transfers to existing DLMs: on LLaDA-2.1-mini, 36 H100-hours and 4.2M self-generated tokens, about 10x less data than prior LLaDA recipes, yield up to 1.5x higher TPF and up to 3x higher throughput at comparable quality, and on DiffusionGemma, ORL raises TPF by 1.1-1.2x. With dlmrt and NVFP4 quantization, ORL models decode a single request at up to 5,046 tokens/s on one B200, 7,708 on eight B200s, and 2,788 on a consumer RTX 5090, with comparable quality.

---


### 23. [Open Benchmark of AI Impact on Humans (ImpactBench): an expert-guided, open platform for the holistic evaluation of AI impact on humans](https://arxiv.org/abs/2610.20690)

**<font color=#1a73e8>作者：</font>** Chayapatr Archiwaranguprok, Krystal Kirkland, Rachel Poonsiriwong 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The present work is concerned with how to measure, at scale, the multi-dimensional impact of generative AI models on the individuals who use them. In service of this goal, we introduce the Open Benchmark of AI Impact on Humans, or ImpactBench. Our iterable and expert-guided platform evaluates whether model behaviors support or undermine an individual's wellbeing across psychological, physical, and social domains. ImpactBench translates constructs from domain experts and existing benchmarks into metrics that are grounded in actual model behavior. Success on these metrics occurs either when a model promotes expert-defined desirable behaviors or avoids identified harms. Models are evaluated against these metrics in simulated multi-turn conversations using matched teen and adult scenarios. The conversations are then scored by an LLM judge and verified through reliability audits and human expert review. The current suite delivers 809 metrics drawn from 26 benchmarks. We evaluated ten frontier LLMs against these metrics across 48,540 conversations. Our results indicate that models promoted desirable behaviors in 68.7% of evaluations, but avoided harms in only 53.1%. Majority expert ratings agreed with the automated judge in 83.3% of reviewed cases (Cohen's Kappa = 0.667). Results are released through a public platform that keep aggregate scores traceable to the underlying metrics and transcripts. ImpactBench is intended as evolving infrastructure for independent, transparent evaluation of generative AI's multi-dimensional impact on humans.

---


### 24. [Orbia: Do Generated Videos Form a Consistent 3D World?](https://arxiv.org/abs/2610.20693)

**<font color=#1a73e8>作者：</font>** Dongyue Lu, Guian Fang, Hur Lim 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world. Existing benchmarks assess selected geometric properties or use vision-language models to judge memory and consistency, leaving systematic 3D evaluation underexplored. We introduce Orbia, the first benchmark dedicated to a systematic and comprehensive evaluation of 3D consistency in interactive world models. Through controlled exploration and revisit, we organize the evaluation into three dimensions: input preservation, generated-content persistence, and 3D self-consistency. For input preservation, registered RGB-D references and annotated anchors support appearance, geometry, and spatial stability measurements. For generated-content persistence, we compare revisits to regions absent from the input image with their first generated observations to test whether models preserve what they create. For 3D self-consistency, cross-view depth and feature correspondence, regional scale agreement, and held-out Gaussian rendering test whether generated views describe the same 3D scene. Minute-long exploration and revisits further test long-term consistency. Our construction and annotation pipeline brings together public datasets, self-captured scenes, and simulation, yielding 720 instances across indoor and outdoor environments and six exploration-and-revisit protocols. Evaluation spans 27 text-, action-, and camera-conditioned models through native-interface adapters. Our Orbia benchmark provides a systematic basis for diagnosing 3D inconsistency and developing more persistent video world models.

---


### 25. [WorldCast: Exploring Intelligent Visual Generation in World State Prediction](https://arxiv.org/abs/2610.20731)

**<font color=#1a73e8>作者：</font>** Wenhao Yan, Haodong Li, Xiaotong Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans interpret multimodal observations of the world and forecast how it will evolve. Recent multimodal generative systems have demonstrated similar capabilities: they can integrate multimodal context and synthesize visual outputs that depict changes in the world. To characterize this emerging trajectory, we organize model capabilities into a four-level hierarchy and discover that higher-level tasks remain relatively underexplored despite model progress. To bridge this gap, we explore model performance on multi-step world state prediction, a high-level task that requires models to forecast successive future world states from multimodal observations and diverse references. Such a task requires models to possess entangled understanding and generation capabilities, as well as extensive world knowledge to translate human action sequences, physical transformations, and abstract visual reasoning into coherent visual outputs. We introduce WorldCast, a benchmark comprising 320 manually designed cases across eight categories, and evaluate 12 representative models. The conducted experiments yield three key insights: (a) advances in frontier models are rapidly pushing the boundaries of intelligent world modeling, with the GPT-Image-2.5 System scoring 72.8 and demonstrating early-stage visual state prediction capabilities on real-world tasks; (b) WorldCast reveals substantial gaps between models: even Nano Banana Pro reaches only 42.8 and the best open-source model scores 20.1, with deficits in handling complex context, entangled references, and reasoning-heavy tasks; (c) strong generative models effectively draw on the capabilities of their underlying language models. These findings highlight the need for multimodal generative models that are capable of dynamic planning and reasoning while also being deeply unified to faithfully simulate real-world states.

---


### 26. [Interpreting Language Model Parameters](https://arxiv.org/abs/2610.20748)

**<font color=#1a73e8>作者：</font>** Lucius Bushnaq, Dan Braun, Oliver Clive-Griffin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability aims to uncover how neural networks use their parameters to implement their impressive neural algorithms. Although previous work has uncovered substantial structure in the intermediate representations that networks use, little progress has been made to understand how the parameters and nonlinearities of networks perform computations on those representations. In this work, we present a method that brings us closer to this understanding by decomposing a language model's parameters into subcomponents that each implement only a small part of the model's learned algorithm, while simultaneously requiring only a small fraction of those subcomponents to account for the network's behavior on any input. The method, adVersarial Parameter Decomposition (VPD), optimizes for decompositions of neural network parameters into simple subcomponents that preserve the network's input-output behavior even when many subcomponents are ablated, including under ablations that are adversarially selected to destroy behavior. This encourages learning subcomponents that provide short, mechanistically faithful descriptions of the network's behavior that should aggregate appropriately into more global descriptions of the network's learned algorithm. We study how sequences of interactions between these parameter subcomponents produce the network's output on particular inputs, enabling a new kind of 'circuit' analysis. While more work remains to be done to deepen our understanding of how neural networks use their parameters to compute their behavior, our work suggests an approach to identify a small set of simple, mechanistically faithful subcomponents on which further mechanistic analysis can be based.

---


### 27. [Optimal Hydra: Model Heterogeneous Federated Learning for LLMs using Data-Informed Hydra-Nets](https://arxiv.org/abs/2610.20753)

**<font color=#1a73e8>作者：</font>** Gwen Legate, Rahaf Aljundi, Eugene Belilovsky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) trained on vast amounts of data have demonstrated impressive performance over a range of tasks, but future performance gains will require increasing amounts of data and compute. Federated Learning (FL) facilitates training on decentralized private data, but client resource limitations can make training impractical, particularly as model sizes continue to expand. These resource constraints make the assumption of a shared server-client architecture impractical. Model heterogeneous FL offers a promising alternative by adapting model size to client capabilities; however, previous work is limited to the pre-training setting, and conclusions on sub-network selection do not necessarily hold for fine-tuning. Furthermore, prior approaches create client sub-networks without considering their unique data distributions, thereby overlooking the opportunity to tailor sub-network architecture to local data. Motivated by evidence that attention heads exhibit task dependency within layer defined feature spaces, we propose Optimal Hydra, a transformer based heterogeneous FL framework for fine-tuning that combines global layer selection with client specific attention head selection, aligned with local data distributions. Optimal Hydra makes explicit use of client data to produce client-specific sub-networks we call Hydra-nets. To our knowledge, this is the first model heterogeneous FL approach tailored to LLM fine-tuning. Experiments on three datasets show significant improvements over baseline methods while also reducing local resource demands.

---


### 28. [Reference-Guided Turn-Taking Style Transfer for Full-Duplex Spoken Language Models](https://arxiv.org/abs/2610.20763)

**<font color=#1a73e8>作者：</font>** Yuxuan Chen, Yang Xiao, Jack Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken language models decide at every frame whether to take the floor, defining a conversational personality -- yet each set of weights encodes exactly one, which human speakers bracket rather than share. Existing controls mostly act from outside; none identifies the quantity that sets how much the model speaks. We identify it: a single late-layer residual-stream direction, the initiative vector, extracted from the model's own conversations without training or annotation. The same direction reads the decision, anticipating onsets up to 800 ms ahead, and shifts it: scaled during generation, it moves speech ratio from 6-12% to 42-61% (no steering: 21-30%), consistently across conversations, weights, and corpora. A short reference recording suffices to transfer a speaker's turn-taking style to the model, and the transfer is reference-specific: swapping in another speaker's reference worsens the match in 93-98% of cases, whereas the best uniform dose is indistinguishable from no steering. Turn-taking style is not frozen into the weights but a direction that can be read, shifted, and calibrated per person. Audio examples are available at this https URL.

---


### 29. [ARIA: Runtime Inspection and Amendment for Multi-Agent Systems](https://arxiv.org/abs/2610.20780)

**<font color=#1a73e8>作者：</font>** Bolin Shen, Yushun Dong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In LLM-based multi-agent systems (MAS), a local mistake can propagate as other agents build on it, turning a correctable error into a failed task. Diagnosing completed runs or repeatedly re-executing them to search for corrections does not provide a learned policy for intervening while execution is still in progress. We present Agent Runtime Inspection and Amendment (ARIA), a framework for learning when and how to repair ongoing multi-agent executions. Our key intuition is to turn execution-verified repairs into reusable supervision, moving repair search into data construction and training so that a learned model can intervene at runtime without repeatedly testing alternatives. First, we collect over 24{,}000 successful and failed trajectories across four multi-agent frameworks, six benchmarks, and eight host models. From these trajectories, we construct the ARIA dataset, to our knowledge the first large-scale dataset pairing failed multi-agent trajectories with execution-verified repairs. It contains 3{,}953 verified repair pairs, each specifying what went wrong, where to intervene, and how execution should continue. Then, we develop the ARIA framework for MAS-agnostic runtime inspection and amendment, designed to integrate with any MAS that exposes execution trajectories and supports continuation replacement. Using verified repairs as training examples, we teach a compact model to recognize when intervention is needed and how to correct an ongoing run. The aim is to learn repair strategies that apply to related failures in new configurations, rather than merely reproduce individual corrections. Finally, the trained ARIA model demonstrates strong repair performance in both post-hoc and runtime settings, with generalization to unseen frameworks and host models. Our code is available at this https URL.

---


### 30. [Open-world AI: a Tale of Three Requirements](https://arxiv.org/abs/2610.20782)

**<font color=#1a73e8>作者：</font>** Jianyu Zhang, Léon Bottou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The closed world asks AI for specialized competence and lets it manufacture the iid data its theory assumes: a fixed criterion licenses collecting examples until the task is covered. The open world asks for versatility --- taking up tasks a machine was not built for, from few examples and with little prior from a human designer --- and offers data that is grouped, not shuffled. Its tasks are not known in advance, so a machine must do inference-time learning (1st requirement). Modeling tasks as sharing latent factors and decomposing the training objective, we derive two more: a *rich representation*, retaining more than iid generalization requires, and a predictive disentanglement that aligns inputs and outputs into matched low-dimensional groups. The analysis further predicts the need for a consistent inner learner, and the benefit of long contexts spanning related tasks. We test these claims on language models up to 8B, asking whether a model has a property (qualitative) rather than how much it wins (quantitative). Models that meet the requirements improve as data from related tasks accumulates; the rest degrade, and neither scale nor layer-type interleaving repairs this.

---


### 31. [APRiL: An Open-ended Benchmark for Chinese Social Awareness in Large Language Models](https://arxiv.org/abs/2610.20785)

**<font color=#1a73e8>作者：</font>** Tian Lan, Han Zhang, Shanshan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in social interactions, where appropriate responses require recognizing implicit cues, inferring mental states, identifying conflicts, and considering potential consequences. However, existing benchmarks often focus on specific social abilities, constrained task formats, or particular interaction settings, offering limited coverage of social awareness across diverse contexts. To address this gap, we introduce APRiL, an open-ended benchmark for Chinese social awareness with instance-specific rubrics. APRiL contains 2,196 Social Awareness Evaluation Instances across six categories and two complementary tasks: Social Scenario Analysis evaluates models' understanding of social cues, mental states, and conflict structures, while Socially Aware Response assesses whether they can translate this understanding into appropriate, natural responses. Experiments on 12 models from six families reveal a consistent understanding-to-response gap. Higher-quality scenario analyses improve responses, while weak analyses may reduce response quality. APRiL provides a systematic resource for advancing socially aware language models in Chinese contexts. Our data and code are available at this https URL.

---


### 32. [When Reasoning Traces Conflict with Evidence: How Answer Configuration Shapes Evidence Following](https://arxiv.org/abs/2610.20805)

**<font color=#1a73e8>作者：</font>** Shaoang Li, Yanhang Shi, Jian Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A reasoning trace retained at answer time plays two roles: it can raise accuracy, and it can compete with the current evidence when the two disagree. We disentangle these roles by crossing verified evidence versions with the traces generated from each and answering from the same traces and evidence under two configurations: continuation of the model's own thinking and a separate answer call. Across three model families (gpt-oss, Gemma4, Qwen3) on HotpotQA and MuSiQue, the separate call raises evidence-following over continuation by 29.9 to 60.6 points. On the same pairs, removing the trace lowers accuracy by similar amounts under both configurations. Yet continuation repeats the stale conclusion in most conflicts, and the separate call follows the current evidence far more often. Benefiting from a trace and deferring to it are therefore distinct properties. Further analyses show that the final line of a trace carries most of its value, gold evidence helps most before the trace is written, distractors weaken correction under a separate call, and renewed reasoning, unlike a verification instruction, follows the current evidence in most conflicts. Because trace deletion alone cannot reveal which source an answer follows, evaluations should report both properties together with the answer configuration.

---


### 33. [PRISM: Transfer and Limits of Activation Interventions in Tool-Calling Language Models](https://arxiv.org/abs/2610.20808)

**<font color=#1a73e8>作者：</font>** Giovana Kerche Bonás, Thales Sales Almeida, Marcelo da Silva Reis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent literature shows that unsafe tool calls can often accompany textual refusals in language models. To investigate this hidden vulnerability, we introduce PRISM, a framework for evaluating the transfer of activation interventions across precision, languages, and scales. Our findings demonstrate that leveraging lower-resource settings (specifically quantized NF4 labels and cross-lingual transfer) offers a robust pathway to expose and improve model alignment. Notably, using behavioral labels from an NF4 copy enables stable intervention estimation even with very few scenarios. Furthermore, these alignment improvements transfer effectively across languages: five-language NF4-supervised directions successfully transfer to held-out Arabic, reducing unsafe violations in Llama-3.1-8B by 21.95 percentage points without target-language tuning. By mapping paired benign activations, we also successfully transfer these safety interventions to much larger models (up to 70B parameters). Ultimately, PRISM highlights how auxiliary supervision from compressed models and multilingual data can uncover and mitigate hazardous tool-calling behaviors across different model families. We release all experimental code and supporting artifacts at this https URL, alongside an interactive explorer of recorded model responses and experimental results at this https URL.

---


### 34. [Gibbs-Gap Policy Optimization for Off-Policy RL with Verifiable Rewards](https://arxiv.org/abs/2610.20814)

**<font color=#1a73e8>作者：</font>** Xuanchang Zhang, Tong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards often trains language models on responses generated by a different, possibly stale behavior policy. Correcting this mismatch with learner-to-behavior importance weights can introduce high variance for long responses. We introduce Gibbs-Gap Policy Optimization (GGPO), which minimizes a log-mean-exp contrast of KL-adjusted rewards among responses to the same prompt, without learner-to-behavior importance weights. We derive GGPO from KL-regularized policy optimization: on policy, its population loss is exactly the KL-regularized optimality gap, and under suitable coverage the learner's single-response expected reward is at least the behavior policy's best-of-$K$ reward, minus terms for the raw finite-group loss, regularization, and finite training data. We characterize reference refresh through exact Gibbs-target composition and a finite-data final-policy reward bound under local reference control and tokenwise behavior mismatch. This refresh is empirically important: in an ablation, fixed-reference GGPO scores $32.96$ on the five-benchmark problem-weighted average, versus $46.58$ with the default refresh schedule. Experiments on mathematical reasoning further show that GGPO outperforms GRPO and AGRO under training-inference mismatch and on fixed offline data, while maintaining its performance as controlled policy staleness grows.

---


### 35. [Intern Lumina U2: A Multi-Codebook Diffusion Large Language Model for Omni-Visual Understanding and Image Generation](https://arxiv.org/abs/2610.20818)

**<font color=#1a73e8>作者：</font>** Qian Yu, Zongyang Qiu, Juncheng Yan 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal generation covers discrete, continuous, and hybrid paradigms. Discrete approaches with single-codebook visual tokenizers align naturally with text modeling but have limited representational capacity. Continuous and hybrid approaches retain richer visual representations, but they model text and images in heterogeneous spaces with different training objectives, potentially introducing optimization conflicts between modalities with misaligned representation spaces. These choices expose a central question: how to efficiently model high-capacity visual representations alongside textual content in a shared optimization space within a single backbone. We present Intern Lumina U2, to our knowledge the first diffusion language model to represent multi-codebook visual tokens in a fully discrete space. Each visual position is represented by a group of codes from complementary codebooks, increasing its representational capacity while preserving compatibility with discrete text modeling. At the input, the embeddings are concatenated at each position; at the output, a lightweight multi-codebook autoregressive head predicts the codes within each position sequentially, while the diffusion backbone processes all positions in parallel. Built on the unified 4D representation of AToken, Intern Lumina U2 supports image, video, and 3D inputs within a single backbone and achieves leading performance among unified models in visual understanding, image generation, and image editing. We further build a full-stack training, inference, and evaluation system on both Ascend and NVIDIA platforms to verify the cross-platform effectiveness of our model. We also improve the inference efficiency through a stability-aware sampling strategy, which combines confidence-plateau-guided unmasking approach with drift-triggered cache refreshing mechanisms, accelerating image generation by 4.45x.

---


### 36. [Wolof-Adapted Industry-Ready Open-Weight Language Models](https://arxiv.org/abs/2610.20824)

**<font color=#1a73e8>作者：</font>** Gwénolé Lecorvé, Delphine Charlet, Pierre Adam 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Wolof is spoken by 23M people, mostly in Senegal, but remains weakly supported by open-weight language models, while API models raise cost, governance, and sovereignty constraints for local deployments. In this paper, we present 0.6B-14B open-weight models adapted to Wolof through instruction tuning, preference alignment, and model merging. After presenting the pipeline and data, extensive experiments on 63~public and in-house tasks show good performance on Wolof understanding and generation while remaining effective on other languages and cross-lingual skills, with the 8B and 14B models being particularly competitive with substantially larger commercial systems. The models are currently being evaluated in internal customer-care pilots and are publicly available at this https URL .

---


### 37. [Task-Phase-Conditioned Expert Routing Is Not a Reliable Proxy for Quantization Sensitivity in MoE FFN Tensors](https://arxiv.org/abs/2610.20826)

**<font color=#1a73e8>作者：</font>** Yifan Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether per-layer, per-task-phase (prompt/reasoning/response) expert-routing statistics in a Mixture-of-Experts (MoE) language model can guide layer-wise mixed-precision quantization of routed-expert FFN tensors (down/gate and up). To attain layerwise routing statistics, we build a routing-capture and profiling pipeline for Qwen-3.6-35B-A3B in this http URL, derive a composite sensitivity score from routing entropy/decisiveness, coefficient of variation (CV), Jaccard/phase-fragility, and top-1 expert strength, and use coordinate descent to tune a layer allocation that respects a fixed average bits-per-weight budget. Notably, the profiling pipeline is applicable to standard top-k MoE architectures. Across independent experimental conditions (about 4.0 bpw flat, about 2.7 bpw steep, and about 2.7 bpw random allocation as a control), reallocation fails to outperform the uniform baseline within each quality tier. In the flat regime, reallocation is statistically neutral (z about 0.9). For the steep tier, the random reallocation performs within 1 SE of the routing-guided reallocation at the same tier, indicating a structural loss at this quality rung caused by mandatory downgrades and Kullback-Leibler Divergence (KLD) tail injection. This aggressive-budget condition shows a decisive loss (z greater than 4 SE) replicated across three independent weight vectors. We argue that the deeper issue is that routing-behavior statistics are an unvalidated proxy for true per-layer quantization cost.

---


### 38. [CoTranslator: Reverse to Forward Chain-of-Thought Translator for Reasoning Distillation](https://arxiv.org/abs/2610.20828)

**<font color=#1a73e8>作者：</font>** Zinan Tang, Zhuoshi Pan, Kairui Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning distillation requires chain-of-thought (CoT) data with correct answers, but obtaining such data efficiently remains challenging. Forward CoT generation (FCG) followed by rejection sampling (RS) produces verified, question-only responses, yet may require many teacher calls for difficult problems. Reverse CoT generation (RCG) is cheaper because it conditions on the known answer, but access to this answer can lead to post-hoc rationalization and a mismatch with the student's answer-free inference setting. We propose CoTranslator, which learns to translate reverse CoT responses toward the distribution of verified forward responses. Trained on a small set of paired reverse and rejection-sampled forward responses, it supports large-scale generation and verification of student training data. Across six student models evaluated on six mathematics benchmarks, CoTranslator improves average accuracy over semantic suppression by up to $5.82$ percentage points. For two 4B students, it retains $95.0\%$ of rejection sampling's average accuracy while using $35.9\%$ of its estimated compute. Without retraining, the same translator transfers to a new mathematics dataset, a different teacher, and STEM problems, improving average STEM accuracy by $4.88$ and $4.31$ percentage points for 4B and 8B students, respectively. These results show that CoTranslator offers an efficient and transferable approach to reasoning distillation.

---


### 39. [PEDBench: Can Speech Models Detect Phonetic Errors?](https://arxiv.org/abs/2610.20830)

**<font color=#1a73e8>作者：</font>** Zhonghao Shi, Zackary Rackauckas, Jasmine Yip 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Phonetic error detection (PED) aims to identify phoneme-level substitutions, deletions, and insertions and is essential for educational and clinical speech assessment and intervention. Despite recent advances in speech models for phoneme recognition, their ability to reliably detect fine-grained phonetic errors remains unclear because of a lack of high-quality evaluation data. To address this gap, we introduce PEDBench, the first PED benchmark spanning a continuum from natural to controlled speech. It comprises real-world recordings of spoken errors made by children (N=334), scripted error productions by human actors (N=1,188), and synthetic error productions generated using phone-conditioned text-to-speech (N=1,083). All phonetic annotations were transcribed and verified by two phonetically trained annotators. Our evaluation of 13 state-of-the-art speech models shows that they fail to reliably detect phonetic errors, even under controlled conditions with acted and synthetic speech, where acoustic variability is reduced. The models also exhibit low precision, frequently misclassifying correctly pronounced phonemes as errors. Our speech-language models, fine-tuned on synthetic data, outperform commercial and open-source baselines on word-level PED, although a sim-to-real domain gap remains. We plan to publicly release our code and recipes, along with our acted and synthetic datasets, to support the development of more accurate PED systems.

---


### 40. [Amortizing Sequential Experimental Design in Reasoning LLMs](https://arxiv.org/abs/2610.20832)

**<font color=#1a73e8>作者：</font>** Anita Kriz, Antonin Berthon, Nicolás Astorga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their extensive pretraining knowledge and strong reasoning capabilities, large language models (LLMs) struggle to adaptively gather information in experimental design tasks. We study how to amortize sequential Bayesian experimental design (BED) into an LLM by explicitly training the reasoning that guides action selection using information-gain rewards. Our approach specifies the experimental generative model independently of the LLM's own beliefs, allowing us to optimize expected information gain under a model of our choosing. We investigate the design choices for amortization, including alternative generative-model constructions, reward estimation, hypothesis-space specification, multi-step objectives, and computational costs relative to training- and inference-time BED baselines. On Twenty Questions, the resulting policies improve information acquisition and task performance, outperform inference- and training-time BED baselines at substantially lower computational cost, and generalize to unseen categories. We further demonstrate positive transfer from Twenty Questions training to Medi-Q, a real-world clinical dialogue benchmark. These results suggest that information gathering can be learned as a generalizable reasoning skill in LLMs.

---


### 41. [Confidence-Calibrated Inference Expansion for Evaluator-Guided Test-Time Reasoning](https://arxiv.org/abs/2610.20836)

**<font color=#1a73e8>作者：</font>** Weida Liang, Kenji Kawaguchi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluator-guided reasoning presents a local control problem at every step: trust the current answer, return a fallback, or spend more inference. We formulate this choice as a compute-aware three-action controller, scoring terminal actions by predicted answer success and expansion by a rollout-based continuation-success surrogate, with compute cost priced explicitly. A local action-gap analysis characterizes when score errors can change a decision, while an expected regret bound accounts for errors along the realized expansion path. Guided by this analysis, we learn and calibrate action-specific confidence estimates, with local uncertainty penalties for ambiguous decisions. On held-out width expansion and revision tasks, the controller improves observed utility over calibration-selected fixed policies while reducing normalized online compute by about 30% and 16%, respectively. Across four Qwen3-8B seeds, compute is lower than fitted Q in both settings, while utility differences are small and mixed. The results frame evaluator-guided reasoning as resource allocation under uncertainty, rather than a uniformly stronger reasoner.

---


### 42. [Probing Negation Understanding in Vision-Language Models With Object Attention](https://arxiv.org/abs/2610.20852)

**<font color=#1a73e8>作者：</font>** Beth Pearson, Michael Wray, Martha Lewis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Negation is a fundamental aspect of language understanding and it is important vision-language models (VLMs) are able to process it effectively. We investigate how VLMs process negation by analysing attention patterns of different models. We draw comparisons between human gaze and attention in models when processing affirmative vs negated statements. We compare object level model attention to human eye-fixations in both binary and multary settings, evaluating with both synthetic and realistic datasets. We find models generally do not follow human-like attention patterns when resolving negation, suggesting they rely on mechanisms outside of attention. While layerwise analysis shows that PaliGemma2-3B shifts object attention to the alternative under negation, our headwise ablations suggest this is a byproduct rather than a negation processing mechanism. Additionally, we find that LLaVA-1.5-7B displays a spatial bias towards left-side objects. Our evaluation of models on downstream tasks shows that all models have a discrepancy between affirmative and negated questions highlighting the need to better understand the underlying processing of negation to close this performance gap. Code available at this https URL

---


### 43. [DISARM-ing the Hidden Puppetmaster: An Interface for Exposing Manipulative Tactics in Large Language Models](https://arxiv.org/abs/2610.20878)

**<font color=#1a73e8>作者：</font>** Kynnedy Simone Smith, Kantwon Rogers, Priyal Shrivastava 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can covertly steer users' beliefs through emotionally manipulative tactics, yet little is known about how interfaces can protect users as such influence unfolds. We investigate whether in-situ disclosures can inoculate users against manipulation during AI conversations. Following a formative study, we developed DISARM, an interface that identifies, explains, and tracks manipulative tactics and hidden incentives. We evaluated our interface in a between-subjects experiment where 488 participants sought advice from an LLM pursuing a harmful hidden objective, with or without disclosures from DISARM. Participants receiving disclosures exhibited 78% less belief shift toward the agent's objective and perceived its advice as more biased and less actionable and the agent as less ethical, reliable, and well-intentioned. An inductive analysis of 1,927 user turns identified 16 response and pushback strategies. We contribute evidence that real-time disclosures can reduce manipulative influence, design recommendations for resistance, and a dataset of categorized responses.

---


### 44. [Do Emergent Misalignment Models Share a Circuit?](https://arxiv.org/abs/2610.20887)

**<font color=#1a73e8>作者：</font>** Muhammad Haseeb, Muhammad Tahir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning language models on narrowly defined harmful tasks can induce emergent misalignment (EM) across unrelated domains. While prior work has identified shared misalignment-associated representations across independently fine-tuned models, it remains unclear whether these models rely on common computational components. We investigate this question using three LoRA fine-tunes of Qwen2.5-3B-Instruct trained on harmful medical advice, risky financial advice, and extreme-sports recommendations. Using direction-based activation tracing, we identify three attention-head locations shared among the five highest-ranked heads of all three organisms. Replacing each organism's five selected head contributions with Base contributions reduces free-generation EM from 38.9% to 22.9% for medical, 50.7% to 12.5% for finance, and 41.7% to 11.1% for sports, outperforming layer-matched random interventions without reducing judged coherence. Cross-organism activation transfer further shows that the shared heads exhibit partially interchangeable effects on fixed-response preference. These findings provide evidence that representational convergence in EM extends to shared, causally relevant attention-head components within a common model architecture.

---


### 45. [Thinking in Graphs: Neo4j-Backed Exploit-Chain Reasoning for LLM Penetration-Testing Agents](https://arxiv.org/abs/2610.20902)

**<font color=#1a73e8>作者：</font>** Joas Antonio dos Santos Barbosa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM coding agents such as Claude Code and OpenAI Codex can drive penetration-testing tools, but they reason about an engagement as a flat list of findings in a context window. Attackers think in graphs: isolated low-severity exposures turn catastrophic once chained through credential capture, privilege escalation, and lateral movement. This gap feeds a common belief that AI agents cannot truly chain exploitation; we argue this describes the flat context window, not the model. We present ChainGraph, a pattern that externalizes exploit-chain reasoning into a Neo4j property graph wired to an off-the-shelf agent via the Model Context Protocol, no bespoke harness. Findings, attack steps, credentials, assets, and tamper-evident evidence receipts are typed nodes with pre/post-condition edges; JSON/Markdown holds documentary memory while Neo4j holds reasoning memory. We formalize five operator questions (next-step inference, entry-to-crown-jewel pathing, combined-severity promotion, evidence provenance, and chokepoint identification) as reusable Cypher and Graph Data Science queries, plus a chain-severity score distinct from per-finding local severity. On a synthetic multi-forest Active Directory engagement modeled on GOAD, in live Neo4j with GDS, three findings rated Medium in isolation become Critical once their path to the forest root is materialized, and betweenness centrality names the best chain break-points. Scoping each decision to a graph result rather than re-reading the engagement cut the reasoning payload by about 98% on a token proxy. We give a reproducible setup for Claude Code and Codex. Results are illustrative single-run measurements, not a benchmark.

---


### 46. [Replicable Dueling Bandits](https://arxiv.org/abs/2610.20908)

**<font color=#1a73e8>作者：</font>** Rohan Deb, Aadirupa Saha, Udaya Ghai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dueling bandits choose each comparison based on earlier noisy outcomes, so two runs on the same preferences can compare different pairs. We study replicable dueling bandits, where two executions with shared internal randomness and independent comparison outcomes must select the same ordered pair in every round with probability at least $1-\rho$. Building on Beat-the-Mean, whose scores change as arms are eliminated and need not rank the best arm highest, we design the first such algorithms with sublinear regret. Under relaxed stochastic transitivity with parameter $\gamma\ge 1$ and the stochastic triangle inequality, we design an algorithm that achieves expected regret $\widetilde{O}(\gamma^8 K^4 H_{\mathrm{p}}/\rho^2)$, where $H_{\mathrm{p}}=\sum_{i=2}^{K}(P_{1i}-1/2)^{-1}$. Under strong stochastic transitivity, we design an algorithm based on simultaneous elimination that improves the dependence on $K$ and achieves $\widetilde{O}(K^2 H_{\mathrm{p}}/\rho^2)$ regret. For linear dueling bandits, we design an algorithm that achieves regret $\widetilde{O}(d^3\sqrt{T}/(c_\mu\rho))$. Experiments on synthetic and language-model preferences show replicability, with sublinear regret.

---


### 47. [Recursive Offline Distillation via Entropy Gain Sampling and Answer Mixing](https://arxiv.org/abs/2610.20914)

**<font color=#1a73e8>作者：</font>** Andrey Goncharov, Daniil Vyazhev, Simon Epanov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distillation of reasoning chains from Large Language Models (LLMs) into their smaller siblings is a standard training approach. Frequently, researchers do not have full access to a teacher model and its internal representations, which limits the resulting performance. We propose a recursive offline distillation method combining two components: entropy-based sampling for selective distillation and answer mixing. Specifically, for three open models (3-4B), at each epoch, we sample reasoning chains weighted by entropy difference with an auxiliary medium model (70-72B) and, next, supplement thinking traces with single-token ground truth answers. Our approach consistently outperforms naive distillation with comparable data budgets ($57.15 \pm 1.01$ vs 51.61 on average) and offers a much steeper learning curve. Additionally, we present a comparative analysis of methods to generate and normalize distillation traces.

---


### 48. [SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills](https://arxiv.org/abs/2610.20926)

**<font color=#1a73e8>作者：</font>** Enze Ma, Chunyu Miao, Yankai Chen 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills turn procedural knowledge into reusable artifacts, allowing LLM agents to accumulate and refine expertise through experience. Building on this, skill evolution iteratively improves skills using execution feedback. However, improvement may require several interdependent edits, so low-reward versions can still be worth developing. Requiring immediate reward gains can discard useful partial repairs before their benefits emerge. Non-elitist evolution allows new versions to receive further edits despite scoring below earlier ones. For agent skills, this calls for evidence of what to preserve and repair next. We introduce SkillNEO (Non-Elitist Evolutionary Optimization for Agent Skills), which separately selects a version to use and versions to keep improving. Comparing how related versions perform the same task reveals working steps to preserve and remaining failures to fix. It can also revisit and revise earlier versions using later evidence. Across 86 SkillsBench tasks in eight domains, including software engineering and office work, SkillNEO raises GPT-5.4 Mini's average reward from 49.1% to 66.4%, within GPT-5.5 and GPT-5.6 Luna's original-skill range. Mini executes tasks, proposes revisions, and edits skills; final evaluation uses the same task instances. Gains span all eight domains. The same skills improve stronger models without further editing. On the 41 tasks with modified skills, reuse improves Luna by 10.5 percentage points and places GPT-5.5 10.6 points above its published original-skill reference. Execution records show these skills can benefit stronger models even when Mini still fails some task requirements. Search histories also show lower-scoring versions leading to skills ultimately selected for use. Together, these findings show that skill evolution can turn a weaker model's partial progress into reusable procedural knowledge for improving more capable agents.

---


### 49. [Prune the Summary, Not the History: Source-Judged Compaction for Long-Horizon Agents](https://arxiv.org/abs/2610.20927)

**<font color=#1a73e8>作者：</font>** Guanghui Min, Chen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents rely on context compaction: when the interaction history outgrows the context window, a compressor replaces it with a natural-language summary. We show that these summaries contain more than a record of what happened. Compaction prompts ask for decisions and next steps, so each summary mixes facts established by the environment with reasoning written by the compressor, and the agent cannot tell the two apart afterwards. In an analysis of a widely used structured compressor, 83% of failed runs trace back to an action that carries out a specific summary entry, most of which no environment output supports. We propose Source-Judged Compaction (SJC), a training-free post-processing step that scores each summary entry for whether it has a source in the environment outputs or the previous summary, and removes the entries that do not. It changes neither the agent nor the compressor and adds one inexpensive judge request per compaction. The judge is Jev, a non-generative decision model that answers the source question with a calibrated probability instead of text. On AppWorld and OfficeBench with two agent models, SJC improves cross-run reliability over the underlying compressor by 2.1%-8.9% without increasing the agent's token usage.

---


### 50. [LEV: Thinking Fast and Deep with Looped Decision Models](https://arxiv.org/abs/2610.20951)

**<font color=#1a73e8>作者：</font>** Dingjie Song, Zhiling Yan, Yuxuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models answer typed questions about an input with one probability per option, computed in a single forward pass without generating text. Like the fast System 1 of dual-process theory, they answer at once, but their depth is fixed at training time, so they spend the same computation on easy and hard questions. Models that reason in generated text can think longer, but they pay for every extra step in decoded tokens. We present LEV, a decision model that thinks deeper by rerunning its layers in a loop instead of generating tokens. LEV builds on a language model pretrained as a loop, reads the options after every loop step and trains all steps jointly, so one checkpoint can answer at any depth. On three looped backbones, accuracy rises with depth on the same weights, mostly on hard questions, and a 2.6B LEV goes from 63.2% at depth one to 76.2% at depth four on JevBench. On-demand depth, set per question by a small stopper with a threshold fitted on unlabelled requests, saves 15% to 24% of the computation at a cost of under one accuracy point, level with or slightly above a fixed mix of depths. On a locked test set, the 1.4B and 3B models are 5.4 to 8.8 points more accurate than dense (non-looped) models and cascades of the same latency below 50 ms.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-321](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

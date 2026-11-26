# 🧠 大模型相关研究 | 2026年11月27日

> 本类共 **267** 篇论文：已确认 **249** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-267](./part-06.md)

---

### 1. [Constraint-Aware Test-Time Scoring for LLM and VLM Candidate Selection](https://arxiv.org/abs/2611.33161)

**<font color=#1a73e8>作者：</font>** Rangarajan Ramesh, Yongchao Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an LLM or VLM produces several candidate answers, picking the best one usually relies on the model's own confidence, a learned judge model, or a domain check. Each has a known weakness: an answer can be fluent but insecure, mathematically plausible but physically infeasible, or rated highly by a judge while quietly breaking a task requirement. We propose a scoring framework that combines a small set of hard checks every answer must pass with a wider set of softer checks whose scores are blended into one number per candidate. This adaptive scoring framework consists of three components: a drafting model that produces the candidates, a configuring model that selects and weights the checks for each task, and scoring models that rate properties no grounded tool can compute. We apply our proposed method to four tasks: writing code that is both correct and secure (CWEval), generating robot manipulation plans (LIBERO with added safety variants), passing competitive-programming hidden tests (LiveCodeBench), and answering questions from retrieved documents (HotpotQA). An ablation study isolates the contribution of each component and finds that the largest gains come from combining hard checks with candidate comparison: on tasks where the first sampled answer is often broken or unsafe, this pairing lifts joint correctness-and-safety by up to +0.21 (retrieval-augmented QA) and code-generation safety by up to +0.28 (CWEval), with the size of the gain tracking how weak the first sample is, falling to near zero or slightly negative where it is already strong. The per-task layer that selects and weights the softer checks adds no measurable value over simpler alternatives. This builds a unified scoring framework, together with an ablation that identifies the grounded hard checks, not the soft-factor configuration, as the source of the gain.

---


### 2. [Attributing Agentic Failure in Reasoning Vision-Language Models with Interactive 2D Environments](https://arxiv.org/abs/2611.33162)

**<font color=#1a73e8>作者：</font>** Pranav Guruprasad, Sean Rivera, Helen Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic benchmarks report a success rate that confounds distinct causes of failure: misreading the environment, never working out how components of the environment operates, operating the components in the wrong order, and failing to recover from a mistake, each of which calls for a different fix. We present an early preview of MultiNet v2.0-Gridworld - an interactive maze environment built for attribution rather than ranking. Four different types of mechanisms, namely key-door pairs, switch-gate pairs, distractors and decoys, and ordered combinations of these mechanisms, can be added, modified, or removed independently while the renderer, the action space, and the scoring function stay fixed. A breadth-first search over the joint state of position, facing direction, inventory, and mechanism state gives every instance an exact optimal action count, which sets its difficulty and grades unfinished episodes. We fix the evaluation protocol on 15 held-out mazes over 540 episodes, then evaluate three vision-language models on 50 mazes. They solve 6 of 150 episodes, 45 of the 50 mazes were not solved by any model, and no episode containing a switch-gate mechanism was solved.

---


### 3. [Code availability is not enough: schemas for documenting and extending data analysis](https://arxiv.org/abs/2611.33167)

**<font color=#1a73e8>作者：</font>** H. Sherry Zhang, Roger D. Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A data analysis involves a sequence of decisions, from data cleaning to model specification, each of which can affect the reported result. Reproducing that result is not the same as understanding the sequence of decisions that produced it and the reasons for each: the code mixes those decisions with implementation details, while the manuscript states the major decisions and their rationale but scatters them across its sections and often leaves out the minor ones. A reader may then ask how the result would change under a different decision: the question itself is easy to pose, but implementing it is often non-trivial in practice. In this work, we propose a schema that represents a data analysis as a collection of decisions in natural language, from which large language models (LLMs) can generate and validate analysis scripts directly. This workflow can also expand a single analysis into a full multiverse of alternatives, specified in an alternative file, ready for comparison. We demonstrate the proposed workflow in two applications. In the first, we construct a schema for a published regression analysis of heaped smoking data and show that it reproduces the reported estimates, and that a reviewer-suggested alternative can be specified through the alternative file and turned into code automatically. In the second, where no schema is provided, we show how the workflow serves instead as a reproducibility check, applied to the many-analysts football study. As an intermediate representation between the manuscript and code scripts, our schema gives a self-contained account of an analysis and makes it extensible from a reader's perspective.

---


### 4. [MGMem: An Efficient, Deterministic, and Provenance-Preserving Framework for Long-Horizon Agent Memory](https://arxiv.org/abs/2611.33174)

**<font color=#1a73e8>作者：</font>** Junhong Huang, Xin Tong, Jun Xia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon Large Language Model (LLM) agents need persistent memory that surfaces the right past interaction at the right time across thousands of turns. Many systems index by invoking generative LLMs to rewrite history into summaries, facts, or knowledge graphs--a step that is (a) costly (thousands of generative calls per build), (b) non-deterministic (undermining reproducibility and giving inconsistent answers across runs), and (c) provenance-erasing (the reader sees synthesized text, not the original turn). We propose MGMem, a framework with no generative indexing calls that replaces this step with a deterministic discriminative-parser pipeline: recurring mentions across sessions are organized into an incidence graph, question mentions are resolved by a subject-conditioned three-stage resolver, and raw dialogue episodes are returned to the reader. On English multi-session dialogue QA, MGMem outperforms matched-protocol baselines on LoCoMo without generative indexing calls; on the full LongMemEval-S, it remains competitive overall and leads or ties on single-session types among local retrieval comparisons. Code: this https URL

---


### 5. [Psychophysics of Duration Perception in Multimodal Large Language Models](https://arxiv.org/abs/2611.33176)

**<font color=#1a73e8>作者：</font>** Auss Abbood, Zihao Fu, Nigel Collier  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Studies of time perception in language models focus mainly on text-based settings. Yet multimodal models are increasingly used for tasks that require perceiving the passage of time, making the limits of their temporal perception important to understand. We measure the limits of duration perception from audio against a human baseline to address this gap. Drawing from psychophysics, we operationalise duration perception as a melody recognition task, testing when a melody becomes unrecognisable as it is slowed down. Of 21 tested models, most cannot recognise well-known melodies without labelled in-context examples. With in-context examples, seven recognise melodies reliably, most peaking within the median human recognition band. Generalisation is limited: (i) recognition peaks shift with in-context example speed, (ii) melody titles induce prediction bias, and (iii) providing examples with scientific pitch notation does not prevent accuracy declining at long note durations for most models. In humans, the recognition window is a property of the perceiver; in current models, it is largely a property of the prompt.

---


### 6. [Neighbor Crowding Predicts Feature Stability in Sparse Autoencoders](https://arxiv.org/abs/2611.33182)

**<font color=#1a73e8>作者：</font>** Denis Federico Lim, Naveen Dasari, George Flint 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Autoencoders (SAEs) offer an approach to identify language model representations by breaking apart polysemantic features into more sparse, interpretable ones. Yet, it is challenging to identify which of the learned features are actually stable, rather than artifacts of initialization. One approach is to train multiple SAE seeds, and compare the learned features across seeds by cosine similarity, but this is notably costly. This raises the question of whether stable features can be identified without the computational expense of training multiple seeds. In this work, we examine cross-seed feature stability across differing levels of training tokens, and demonstrate that in TopK SAEs, it is highly predictable using six computationally cheap statistics derived from a single training run. Neighbor crowding, a geometric property of the dictionary, is the strongest single predictor, with features that sit in dense regions of the unit sphere more likely to be stable than isolated ones.

---


### 7. [Semantic Density Does Not Predict Agent-Memory Collapse](https://arxiv.org/abs/2611.33184)

**<font color=#1a73e8>作者：</font>** Saksham Gupta, Yash Choudhary, Arpit Upadhyay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Persistent textual memory can improve LLM agents, but repeated updates can erode task performance. We ask whether memory-store statistics warn before held-out accuracy declines. We registered mean pairwise cosine similarity ($\rho$) and 13 additional geometry, retrieval, and graph statistics on 805 snapshots from 13 memory methods across ALFWorld, AppWorld, ScienceWorld, WebShop, and two ARC-AGI settings. These methods store trajectories, rules, workflows, strategies, or linked records, using selective retrieval or whole-store prompting. No such statistic reliably predicted early signs of task accuracy decline, and $\rho$ had zero median lead. With the checkpoint after peak accuracy as a secondary decline point, measures of highly similar pairs and nearest-neighbor crowding changed earlier but did not consistently outperform stored-item count. We trained classifiers on this corpus and applied them unchanged to PropWorld runs of up to 5,000 crafting tasks. They falsely flagged 56.9% of checkpoints from size-limited stores with stable accuracy and detected only 18% of checkpoints after task success fell to zero. Thus, global semantic density did not provide a reliable warning, while local crowding did not transfer consistently across memory designs. In these long-horizon runs, size-limited stores remained stable, while the sole failure arose when unbounded whole-store prompting exceeded model input capacity, which token growth predicted directly.

---


### 8. [General-Purpose Decision Models for AI Configuration Tuning](https://arxiv.org/abs/2611.33190)

**<font color=#1a73e8>作者：</font>** Jingzhi Gong, Jie M. Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI configuration tuning searches for settings that improve the performance of AI systems under a limited budget. Existing tuners use different sampling and search policies, making the choice of decision strategy central to both tuning quality and cost. We investigate whether general-purpose decision models can guide tuning, using Jev as a deployed representative that returns structured choices and numeric scores across diverse tasks. To assess where it helps, we compare its use as an optimizer, performance predictor, and region guider against conventional methods and a large language model (LLM) on eight AI tuning tasks. Conventional optimizers attain rank 1 in six of eight comparisons. Similarly, established predictors outperform Jev in seven. Through region guidance, however, it finds configurations with lower perplexity than those selected by the native tuner, offering a quality gain when additional decision time and API fees are acceptable. These findings yield actionable recommendations on selecting the decision role, retaining conventional predictors, and balancing tuning quality against cost.

---


### 9. [Dynamics of Collective Diversity in Human-AI Co-Creation for Creative Tasks](https://arxiv.org/abs/2611.33192)

**<font color=#1a73e8>作者：</font>** Manh Hung Nguyen, Chao Wen, Sebastian Tschiatschek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI systems are increasingly deployed at scale to support human users in creative tasks across a variety of domains. However, as more users adopt the same AI agent, the resulting artifacts may become increasingly homogeneous, leading to a collapse in collective diversity. Prior work has documented this risk, but lacks a systematic framework for understanding how collective diversity changes as AI adoption scales across co-creation settings. In this work, we conduct a large-scale crowdsourcing study to understand and model the dynamics of collective diversity, quality, and effort in human-AI co-creation across two creative domains: Creative Hypothesis Generation and Creative Story Writing. We find that current AI agents used in co-creation can improve artifact quality and reduce effort, but at the cost of declining collective diversity as adoption increases. We further show that more fine-grained human-AI interaction, along with more diverse agent policies, can mitigate this collapse. Finally, we fit predictive models that quantify how collective diversity scales with adoption across co-creation settings, providing insights for designing AI agents that aim to preserve collective diversity.

---


### 10. [Verified experience improves materials prediction with large language models](https://arxiv.org/abs/2611.33195)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Koji Tsuda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Materials discovery is an iterative loop: experiments and calculations verify predictions, and each outcome can inform the next. Yet most predictors are specialized single-task models fixed after training. Large language models have recently emerged as predictors across heterogeneous tasks but generally underperform specialized models, and retrieval-augmented variants discard their own outcomes. Benchmarks also score queries in isolation, leaving improvement from outcomes untested. Here we construct MatMemBench, a sequential benchmark of 22 materials tasks that reveals outcomes only after prediction and tests online adaptation, memory retention and cross-task transfer. We present MatRecall, a framework that lets large language models store verified predictions, with evidence, outcome and error, as episodes and recall them without retraining. MatRecall improved median performance by 62% over a memory-free model, exceeded specialized models on 11 tasks, remained useful after feedback stopped and transferred between related tasks. Verified experience could become a reusable resource for self-improving discovery loops.

---


### 11. [Extraneous Cognitive Load in Large Language Models](https://arxiv.org/abs/2611.33197)

**<font color=#1a73e8>作者：</font>** Arushi Gupta, Sheng Liu, James Zou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cognitive Load Theory (CLT) shows that human problem-solving is affected by both intrinsic load, arising from task difficulty, and extraneous load, arising from how task information is presented. Large language models (LLMs) show analogous effects: presentation alone can affect model performance, but these effects have not yet been systematically isolated from task difficulty. To address this gap, we introduce CogLoadBench, a controlled benchmark that varies five CLT-inspired presentation factors across three reasoning task families. Across models, we find that higher extraneous load conditions often reduce accuracy by either adding competition or complicating the reasoning path. To support diagnosis and mitigation of load-related effects, we propose the Extraneous Load Score (ELS), a prompt-time metric computed from activations that estimates a model's extraneous load, and show that it generalizes across reasoning task types and load levels. We further show that shifting model representations toward lower-load directions at inference time can improve average model performance without changing prompt content.

---


### 12. [Confidence-Based Adaptive Retrieval Fails Where It Matters Most: A Paradox in Biomedical Question Answering](https://arxiv.org/abs/2611.33210)

**<font color=#1a73e8>作者：</font>** Chengying She, Siyu Deng, Haiyan Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for biomedical question answering, but plausible incorrect answers remain a safety risk in clinical settings. Retrieval-augmented generation (RAG) can ground responses in medical literature, while confidence-based adaptive RAG retrieves only when the model appears uncertain. We evaluate this routing strategy on three biomedical QA benchmarks of increasing difficulty and compare models across a broad range of parameter scales. The results reveal a paradox: confidence is well calibrated (AUROC 0.78--0.89) on standard medical exam questions where retrieval adds little value (+2.4\% to -1.4\%), yet becomes \emph{near-random} (AUROC 0.506) on specialist-level questions where retrieval helps most (+11.2\%). Five uncertainty signals---first-token probability, margin, entropy, consistency-based sampling, and verbalized confidence---show the same failure pattern. Five post-hoc calibration correction strategies, including density-ratio reweighting and rank-preserving transformation, do not recover a useful routing signal on hard questions (best AUROC: 0.507). Cross-model comparison shows that larger parameter scale and higher base accuracy do not guarantee reliable confidence-based routing under specialist-domain difficulty shift. These findings challenge the premise of confidence-based adaptive RAG: in high-stakes biomedical settings, defaulting to always-retrieve is safer and more accurate than confidence-based routing when calibration on the target domain is unknown.

---


### 13. [Demystifying Real-world LLM Service Freeloading](https://arxiv.org/abs/2611.33218)

**<font color=#1a73e8>作者：</font>** Xinyi Hou, Shenao Wang, Wenhui Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party projects repackage free inference from LLM web applications and dedicated clients into independent APIs. We refer to such use beyond providers' permitted access, allocation, or redistribution conditions as LLM service freeloading (LSF). However, its scale and underlying mechanisms remain poorly understood. We present a systematic measurement study of 513 open-source projects, tracing 1,588 inference paths across 64 upstream LLM services and characterizing their development, dependencies, and operating mechanisms. We find that 93.0% of repositories were created in 2026. Direct HTTP or WebSocket requests account for 83.2% of paths, making reproduction of product protocols the dominant invocation method. Projects adapt messages, reconstruct conversation state, and convert responses to support compatible APIs. Account selection or rotation appears on 304 paths (19.1%), allowing projects with multiple eligible accounts to distribute requests across their separate allowances. Our policy analysis finds that 58 of the 62 services with available terms explicitly prohibit at least one examined practice, including automated access, account sharing, or service redistribution. These restrictions cover both downstream API provision and the means of obtaining upstream inference. Our findings inform defenses against unauthorized consumption and redistribution of free LLM resources. We have responsibly disclosed our findings to the relevant providers.

---


### 14. [Real Package, Wrong Controller: Static Auditing of Vendor--Protocol Mismatches in LLM-Generated PLC Code](https://arxiv.org/abs/2611.33227)

**<font color=#1a73e8>作者：</font>** S M Zia Ur Rashid, Sazidul Islam Hira, Suman Rath  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language models can generate Python that drives industrial protocols on programmable logic controllers, yet existing code-grounding checks ask whether an imported package or symbol exists rather than whether it suits the declared industrial target. We define \emph{metadata-conditioned, import-level vendor--protocol incompatibility} and build \textsc{Proteus-OT}, a label-free static verifier over a version-pinned graph of documented bindings. Across 883 generated scripts, 180 carry an import-level mismatch against the declared target (20.4\%); restricting to single-vendor targets gives 16.3\%, and additionally requiring the offending library to reach a protocol communication call gives 14.2\%, which we read as conditional on the corpus metadata rather than on verified intent. None of the 28 adjudicable human control files carries one, a sample too small to estimate a prevalence. Within the balanced subset, 96.6\% of mismatching scripts import packages and call methods that exist, so an existence baseline does not represent them, and every positive ships with an inspectable witness. We also audit machine-versus-human classification on the same corpus, where character $n$-grams reach macro-F1 1.000 under task, model and vendor-disjoint partitions and survive comment removal, an AST round trip and identifier anonymisation. The trailing newline present in 95.2\% of human files and in none of the generated ones separates the classes on its own. Vendor--protocol consistency is a useful static audit target, whereas provenance classification on repository-labelled corpora is not authorship detection.

---


### 15. [How Many Samples Is RL Worth? Best-of-N versus RL Post-Training for Text-to-Image Models](https://arxiv.org/abs/2611.33232)

**<font color=#1a73e8>作者：</font>** Salil Bhatnagar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) on a reward that can be checked automatically has become a common last step in the training of text-to-image models. A simpler way to get more correct images is best-of-N: draw N images from the base model and keep the one that a picker prefers. We ask how many base model samples one RL sample is worth, and call this number the exchange rate. We measure it for Stable Diffusion 3.5 Medium and its public Flow-GRPO checkpoint on 398 new prompts in the style of GenEval, the benchmark behind the RL reward, with human labels on every prompt and two automatic judges other than the reward. The answer depends on the prompt. Four fifths of the prompts do not ask for a position (for example, one object left of another). On these, the base model catches up: best-of-16 with an off-the-shelf vision-language model (VLM) as the picker is about as good as one RL image. A person who looks through up to 3 base images finds a correct one as often as one RL image is correct. On the prompts that ask for a position, RL is far ahead: a person finds a correct image among 8 base images for only 52% of the prompts, against 92% for one RL image. Over all prompts, our primary test, which we fixed in advance, finds best-of-16 with the VLM picker 9.3 points behind one RL image when both automatic judges must pass an image. People see a smaller gap, 5.5 and 6.5 points in two checks. FLUX.1-dev shows a similar gap in the same test. RL also solves 20 prompts that the base model misses in 128 tries, and 1,024 tries recover half of them. The automatic judges are wrong in opposite directions: a detector-based judge like the reward, as used in our primary test, reports a larger gap than people see, and VLM judges report little or none. Comparisons of RL with best-of-N should therefore check the selected images by hand.

---


### 16. [CypherMAS: Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2611.33242)

**<font color=#1a73e8>作者：</font>** Danil Kostromin, Andrey Sakhovskiy, Semen Budennyy  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) built on large language models (LLMs) distribute reasoning across specialized agents that must exchange messages and invoke tools reliably. Existing evaluations typically couple communication with open domain tasks, making it difficult to determine whether a failure arises from reasoning, malformed tool use, lost messages, or forgotten requests. Prior benchmarks do not isolate communication execution or measure routing redundancy against a known optimal path. We introduce CypherMAS, a synthetic benchmark that isolates communication and routing in fixed multi-agent graphs. Agents in chain, star, bipartite, or ring graphs route cyphered messages to remote peers holding the matching decoders; since the optimal route is known, redundant LLM calls can be measured and routing failures may be easily tracked. Across eleven open-weight models from 4B to 753B, small models fail at routing and tool use, dense models above 27B degrade with diameter, and successful runs exceed minimum LLM calls. These findings identify communication reliability as a distinct scaling bottleneck for multi-agent systems and provide a controlled diagnostic for complex multi-agent systems. The source code is freely available: this https URL.

---


### 17. [Typical Angina, Reversed: A Long-Standing Documentation Error in the UCI Heart Disease Data](https://arxiv.org/abs/2611.33248)

**<font color=#1a73e8>作者：</font>** Tejas Tovinkere Pattabhi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The UCI Heart Disease data are a widely used machine-learning benchmark. We show that their chest-pain variable is stored in reverse of its documentation. At all four sites, the code documented as "asymptomatic" (4) marks patients with typical angina, and the code documented as "typical angina" (1) marks patients with almost none of the classical angina features (at Cleveland, no chest pain).
Two complementary checks establish this: (i) the chest-pain table and regression coefficients of the original 1986 Cleveland study are reproduced only under the corrected reading; (ii) in the Budapest, Switzerland and Long Beach files, 93-96% of patients coded 4 have all three classical angina features. A 1990 word-labeled Cleveland file already uses the documented labels, and Statlog (Heart), a Cleveland subset, stores the same codes. OpenML, PMLB and two highly voted Kaggle copies that name the categories use the same documented labels (about 400,000 downloads combined).
We audited a seeded random sample of 150 records from a pre-specified Scholar query for SHAP studies of these data mentioning asymptomatic chest pain (124 readable). Of 32 papers that state a direction for a named category, 25 (78%; 95% CI 61-89%) state one inconsistent with the corrected category identities; 22 (69%; 51-82%; post hoc) are attributable to the documentation error, and nine of these explain it clinically. None of the 124 readable papers identifies the reversal.
Conventional models are essentially unaffected, one reason the error went unnoticed. Interpretations that attach the documented names to model effects are reversed, and zero-shot language-model classifiers that read the labels are misled: with the documented labels, three open-weight models lose 0.12-0.33 in area under the receiver operating characteristic curve (AUC) given age, sex and chest-pain type. We give the corrected mapping, evidence and code.

---


### 18. [Focus On Facts: Stylistically Invariant and Factually Sensitive Text Embeddings](https://arxiv.org/abs/2611.33250)

**<font color=#1a73e8>作者：</font>** Maximus Adeola  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text embedding models can conflate surface-form similarity with factual identity. Given an altered near-copy with one corrupted fact and a differently worded fact-preserving rewrite, the base model prefers the altered near-copy. We test whether hard-negative contrastive supervision can reduce this surface-similarity shortcut. We construct FOF-Bench, an 83,263-triplet benchmark spanning five domains. Each anchor is paired with an LLM-generated, fact-preserving stylistic rewrite and a matched fact-altered near-copy. We fine-tune FOF-80M (Focus On Facts), an 80M-parameter embedding model, with a triplet contrastive objective that ranks the rewrite above the factual alteration. On 8,327 held-out test triplets, the base model chooses the factually altered text in 99.58% of cases (0.42% factual preference rate; mean separation -0.1650). After fine-tuning, mean positive--negative separation is +0.0329, 98.5% of individual margins move in the intended direction, and the preference rate reaches 29.37%. On DiSC, an external style-transfer corpus, mean cross-style similarity increases from 0.7905 to 0.9559. The model also penalizes omission and transfers poorly to directional tasks such as NLI and summarization. We characterize FOF-80M as a soft factual fingerprint for studying factual retention under stylistic variation, not as a general-purpose factuality metric.

---


### 19. [One Token, Many Lessons: Sliding-Window Attention within Gated Delta Networks](https://arxiv.org/abs/2611.33257)

**<font color=#1a73e8>作者：</font>** Yuchen Song, Yangbin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention compresses historical context into a fixed-size recurrent state, reducing the computational and memory costs of long-sequence modeling. From the perspective of test-time regression (TTR), the state matrix can be viewed as an online-learned regression model, where keys and values serve as inputs and targets respectively, and queries are used to read from the model. From this perspective, the effectiveness of state learning depends not only on the update rule but also on how the key-value learning pairs used for state updates are constructed. While existing work has largely focused on how the state is updated and organized, we investigate how the learning pairs used for state updates are constructed. To this end, we propose Sliding-Window Gated DeltaNet (SWGDN), which replaces short convolutions in Delta-Rule linear attention with sliding-window attention to perform content-dependent local aggregation of projected queries, keys, and values. Our experiments show that SWGDN makes the key-value pairs used in consecutive updates more similar in both GDN2 and KDA. In SWGDN, carrying information from the same token across updates can help the recurrent state reinforce a previously learned association. The local mixing strategy can be incorporated into any Delta-Rule-based linear attention architecture without changing its state update equations or chunkwise parallel algorithms. We apply this strategy to two Delta-Rule variants, GDN2 and KDA, and experimental results demonstrate that SWGDN outperforms the original Delta-Rule baseline across multiple benchmarks.

---


### 20. [Same Tokenizer, Better Tokens: Choosing Image Tokens by MAP Inference](https://arxiv.org/abs/2611.33261)

**<font color=#1a73e8>作者：</font>** Piotr Kubaty, Jacek Tabor, Łukasz Struski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discrete visual tokens encode images for reconstruction and serve as training targets for autoregressive image generators. Vector-quantized tokenizers typically assign each encoder feature its nearest code independently. The decoder uses these codes jointly, so a sequence of individually nearest codes can reconstruct an image less faithfully than an alternative assignment. A local model of the reconstruction loss yields a closest-vector problem with a decoder-dependent target and metric. Reconstruction-only search improves PSNR across the frozen tokenizers we test. Different code sequences can achieve similar reconstruction quality, leaving room to favour more predictable ones.
We introduce RecaP (Reconstruction and Predictability), which selects codes for a frozen tokenizer by balancing how faithfully they reconstruct the image with how likely their sequence is under a pretrained autoregressive prior. On ImageNet, LlamaGen GPT-B trained on RecaP tokens achieves lower early-checkpoint FID against training images than GPT-B trained on nearest-neighbour tokens. The difference is smaller against held-out images. On an ImageNet subset, the prior improves generation at comparable reconstruction FID. Our code is available at: this https URL

---


### 21. [What, Who, and When: Structured Harm Assessment for Mental Health Safety via Short Reasoning](https://arxiv.org/abs/2611.33263)

**<font color=#1a73e8>作者：</font>** Catarina Botelho, António Farinhas, John Mendonça 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing use of large language models (LLMs) for mental health support raises important safety concerns. Existing guard models primarily identify categories of harmful content, often overlooking the context needed to determine an appropriate response. We introduce a clinically grounded taxonomy that characterizes harm along three dimensions: what the harm is, who is involved, and when it occurs. It further separates harm characterization from intervention decisions, thus enabling safety policies to be specified outside the model weights through explicit, clinician-curated instructions that can be updated and audited. We validate the taxonomy with expert clinicians and validate a panel of LLM judges to scale annotation. Relabeling public benchmarks in this taxonomy shows that they rarely contain harm directed at the user, which accounts for nearly half of the harm in real conversations. We then train MindGuard2, a 35B-A3B reasoning-based guard model using supervised fine-tuning on short reasoning traces followed by reinforcement learning with a reasoning-length penalty, to minimize inference overhead while preserving the benefits of reasoning. On two public benchmarks and real-world conversations, MindGuard2 achieves balanced accuracy comparable to the substantially larger GLM-5.3 at approximately 10x lower median latency, advancing the accuracy-latency Pareto frontier. Furthermore, it achieves low false-positive rates at high recall, helping balance the need to detect unsafe situations against the risk of unnecessary interventions that may disrupt support and undermine user trust. We release a safety guardrail model with SOTA performance trained on synthetic data, together with synthetic conversations and annotations of public benchmarks in our taxonomy.

---


### 22. [Two Timescales of Forgetting in Fine-tuning of Language Models: Fast Behavioral Suppression and Slow Representational Drift](https://arxiv.org/abs/2611.33302)

**<font color=#1a73e8>作者：</font>** Yilin Luo, Jin Hwa Lee, Andrew M. Saxe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Today, a core pipeline of artificial intelligence systems is pretraining on a broad range of text corpora and then fine-tuning on specific tasks or desired behaviors. Yet we still have limited understanding of how fine-tuning on a restricted data distribution modifies representations acquired during pretraining. In particular, it remains unclear whether surface behavioral suppression happens together with the erasure of latent representations that support it. In this work, we study supervised fine-tuning (SFT) by pretraining transformers on a controlled context-free grammar with hierarchical latent structure, the Random Hierarchy Model (RHM), and fine-tuning with a restricted subset of its generative rules. While during pretraining the model's ability to generate with the correct grammar rules coincides with building the internal representations of the corresponding latent, we find that SFT exhibits a very different dynamics: (i) the generation of deleted rules changes on a fast timescale inversely proportional to the magnitude of the token-latent correlation; meanwhile, their corresponding representations stay intact; (ii) the hidden representations of the deleted rules become forgotten on a much longer timescale, associated with a slow drift of the network parameters. Finally, we observe analogous results in a realistic setup with natural language, suggesting that this timescale separation in forgetting is a more general phenomenon of fine-tuning language models.

---


### 23. [Certify What You Plant: Shortcut-Free Proof Depth in Logical Reasoning Data](https://arxiv.org/abs/2611.33303)

**<font color=#1a73e8>作者：</font>** Baptiste Juran, Dimitri Kachler, Damien Sileo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Procedurally generated logic problems are used to both evaluate and train reasoning in language models. Their difficulty is usually set by planting a proof, that is, by sampling a proof of the desired depth and stating its premises as the problem. However, a planted proof is only one possible proof. A problem can also have shorter proofs, or several unrelated ones, and its stated depth then overstates what solving it requires. We measure what a problem actually requires, relative to a stated set of inference rules. For each problem, we compute the steps every proof must make, the shortest proof, the number of minimal proofs and the indispensable premises, and export certificates that an independent checker verifies. Audits of eight datasets find depth that is forced (ProofWriter, Blocksworld), problems labelled depth 5 that require about two specific rule applications (FLDx2), and answers that need no particular step (ZebraLogic). We then construct problems whose every proof has a requested structure, using a catalog of shortcuts proved once per rule set. Every constructed problem is checked in full and comes with its own certificate. In training, the best data mixes depths and problem types. At equal size, such mixtures of certified problem types, including model-checking problems that forward generation does not produce, transfer better than FLDx2-style derivation data for Qwen3 models from 0.6B to 8B.

---


### 24. [The Platonic Representation Hypothesis in Jacobian-Space: Language and Vision Models Agree Approximately Up to a Rotation](https://arxiv.org/abs/2611.33304)

**<font color=#1a73e8>作者：</font>** Ross Murphy, Gabriel Brostow  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Platonic Representation Hypothesis (PRH) posits that AI models converge toward a shared representation of the world, even when trained on different data modalities. Previous work has found evidence for the PRH in the activations of vision and language models. In this work, we ask whether vision and language models also converge in how they act on these representations: precisely, in how these internal representations affect the models' output. At a chosen layer of a transformer, the Jacobian lens gives every word in the vocabulary (or class in an image classifier) a vector in the hidden state: the vector that most increases the model's tendency to generate that word, at that position or later, or to predict that class. Collectively, these vectors make up what is referred to as the model's J-space. We find evidence of the PRH in J-space across vision and language models, and furthermore, we find that J-spaces mostly converge up to a rotation. That is, a single rotation, fitted on a subset of words, approximately maps one model's J-space onto another's, and so applies to words and classes it was not fitted on. A word's vector, rotated from a text-only language model's J-space into the visual patch tokens of a vision-language model, changes the object the vision-language model says is in the image (and only in the image region where it is added). Rotated into an image generator's text conditioning, a word's vector changes the object in the generated image. Rotated into an ImageNet classifier (trained without text), it raises that object's class score above almost all others, and vice versa. This suggests that models converge not only in how they represent the world, but also in how they act on it.

---


### 25. [Lost in Translation, Not in Confidence: Benchmarking and Calibrating Multilingual Decision Models](https://arxiv.org/abs/2611.33307)

**<font color=#1a73e8>作者：</font>** Mingzhe Du, Thong Thanh Nguyen, Nguyen Tran Cong Duy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision models are language models fine-tuned to return a probability for each option of a typed query, which routers and guardrails threshold directly. They are built on multilingual bases but ranked almost entirely in English. We evaluate 25 top-ranked open-weight decision models on 17 tasks in 14 languages, comparing each language with English on parallel items. Every model loses accuracy in every language, from about 2 points in high-resource languages to 8 in Tamil, while confidence falls only half as much: a threshold set for 95\% accuracy in English yields 90% in Tamil. The size of the loss is set by the language and the base model rather than by leaderboard rank. In 81 controlled fine-tuning runs, task skill learned in English transfers to other languages and a few thousand target-language items narrow large losses, but neither more data nor full-parameter tuning closes them. Finally, the same test items are answered more accurately in all 23 benchmark--language pairs we compare when an LLM rather than a person translated them, so LLM-translated test sets understate the gap.

---


### 26. [What Does RL Post-Training Teach Text-to-Image Models? A Skill-Wise Analysis of Flow-GRPO](https://arxiv.org/abs/2611.33316)

**<font color=#1a73e8>作者：</font>** Cheng Zhang, Jiesong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training has become a standard way to improve text-to-image flow models: Flow-GRPO lifts the GenEval score of SD3.5-M from 0.63 to 0.95, a gain read as the model having learned compositional generation. We ask how much of that gain the base model's own samples already contained, by measuring pass@k over shared noise seeds, one skill at a time, before and after RL, on prompts never used in training. The answer differs by skill. On four of GenEval's six skills, where 32 base samples already solve almost every prompt, the gain is sharpening: one post-trained sample is worth 4 to 10 base samples, and pass@32 barely moves. On spatial relations it is unlocking: pass@32 rises from 0.69 to 1.00, 128 base samples do not match one post-trained sample, and prompts the base model never solved in 32 samples are solved 93% of the time, as often as those it solved. The benchmark average, 31 base samples per post-trained sample, describes no skill. Relations carry 35% of the gain; of the other 65%, selecting among 8 base samples with the judge behind the reward recovers nine tenths. We propose an account of when each occurs: within a prompt, a group-relative update re-weights only the outcomes its samples contain, and a flow policy cannot widen the noise that produces them; across prompts, shared parameters let successes on some prompts repair a deficit common to many. The same anatomy applies to a text-rendering checkpoint. The account's predictions are tested with a checkpoint trained without KL, within-prompt diversity, and controlled training that holds object classes out, where sharpening comes first and transfers, and unlocking follows, on practised objects before unseen ones.

---


### 27. [What Must LLM Agents Communicate? From Information Loss to Communication Failures](https://arxiv.org/abs/2611.33318)

**<font color=#1a73e8>作者：</font>** Yi-Yun Chu, Xiaobin Shen  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> When evidence is distributed across LLM agents, a team may collectively possess all the information needed for a decision yet fail to use it effectively. What must agents communicate for accurate joint predictions, and when does interaction help? We study three requirements for effective communication: sufficiency of the information conveyed, selection of relevant evidence, and utilization of received information. Drawing on information theory and communication complexity, we develop a framework that combines theoretical benchmarks with controlled experiments and message-level analyses. We find that local probability reports can discard essential information, with theoretical information loss closely matching observed performance penalties. Query-first interaction improves predictions when relevant evidence depends on a private query, but compact one-shot representations can eliminate this advantage. Even when sufficient information is communicated, agents may fail to select or use it correctly. Together, these findings distinguish fundamental communication limits from failures in how LLM agents communicate and use information.

---


### 28. [Brand Recall and Category Accuracy in Language Models: An Audit of 1,000 B2B SaaS Brands](https://arxiv.org/abs/2611.33322)

**<font color=#1a73e8>作者：</font>** Ben Moore  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A language model can name a brand without classifying it correctly. This study measures these outcomes separately for 1,000 B2B SaaS brands across 333 product categories. On Gemma 4 12B, with no external retrieval, category prompts elicit 510 brands (51.0%). A separate five-candidate category probe ranks the reference label first for 787 brands, a distractor first for 194, and yields little separation for 19. Among the 981 separated rankings, the error rate is 19.8%. It falls to 3.5% for the 547 brands with a winner-to-runner-up log-probability margin above 0.6. These are within-cohort measurements, not calibrated confidence estimates. Exploratory regressions associate technical coverage with recall and an owned-properties composite with category accuracy, but the composites use different adjustment sets and do not establish causal effects. Across four Gemma generations, measured recall is 39.8%, 44.3%, 51.1% and 51.0%. A separate representation-based sentiment measure has little linear association with customer ratings (r=0.03, n=921). The findings support reporting recall and category accuracy separately. Failure to elicit a brand does not establish its absence from model parameters or training data.

---


### 29. [Sparse Adaptation for In-Context Learning on Data Streams](https://arxiv.org/abs/2611.33325)

**<font color=#1a73e8>作者：</font>** João Neves, Afonso Lourenço, Lizy K. John 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Internet of Things (IoT) generates massive data streams, making edge computing essential for low-latency applications and 5G networks. Tabular foundation models (TFMs) enable adaptation through in-context examples rather than parameter updates, but evolving streams challenge context relevance and computational efficiency. This work introduces SAIL, a framework for sparse adaptation of TFMs that reuses the model's key--value cache between adaptation events. SAIL reconstructs its support set only when drifts in stream structure indicate potential context inadequacy, while the structural representation itself is updated by changes in predictive performance. SAIL combines prequential error monitoring with online, class-specific micro-clustering to detect changes in cluster mass, class separability, and feature-space coverage. Upon adaptation, a context budget is allocated proportionally to class mass, and the most recently updated micro-clusters provide representative observations for refitting. This limits context redundancy and computational cost while preserving recent structural information.

---


### 30. [Who Attributes a Mind to Whom? Mutual Theory of Mind in Simulated User-Assistant Conversation](https://arxiv.org/abs/2611.33327)

**<font color=#1a73e8>作者：</font>** Mingxi Yan, Vasudha Varadarajan, Qiaosi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When users assume that an AI chatbot has mental states, they are more likely to develop over-reliance, emotional dependence, and in extreme cases, psychological harm or self-harm. However, how these mind attributions arise in conversations and how human or AI factors influence this is still unknown. We study how users attribute minds using a minimal framework: a simulated user with different characteristics chats with assistants that differ in social style and memory. We also introduce a message-level measure of who attributes a mind to whom in four directions, checked with trained coders and applied by a fine-tuned encoder that reproduces an LLM judge. Our results show that, on average, nine out of thirteen characteristics raised simulated users' attribution to the assistant. We found that relational needs such as attachment anxiety raised it as theory predicts, some general personality traits raised it as well, and AI-specific characteristics the least. By contrast, the assistant's social style barely changed simulated users' mind attribution. Instead, sycophantic instructions raised the assistant's attribution to itself. Memory raised users' attribution only with some user models. The model playing the user changed overall attribution and the effects of characteristics, style, and memory. Our framework measures how persona descriptions affect mind attribution in simulation. It gives concrete hypotheses for human studies and shows the need for more consistent user simulators.

---


### 31. [Temporal Weight Surgery: Repairing Video Grounding with LLM Editors](https://arxiv.org/abs/2611.33339)

**<font color=#1a73e8>作者：</font>** Ali Asgarov, Chris Thomas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A surgeon first finds what is wrong, then fixes only that part. We use this idea for video grounding, where video-language models often find the right moment in a long video but write its time wrong. In Temporal Weight Surgery (TWS), a general-purpose LLM reads the model's weights and activations, finds where the error arises and repairs it there, without gradients. Separate sessions find the same cause, and this diagnosis of where and why the model fails is our main contribution. Three GPT-6 Astra sessions trace a dropped digit in TimeLens-8B to one MLP layer, and the largest edit gains 7.9 mIoU on 1,215 unseen questions and 18.3 on videos of 30 minutes or more. Two Claude Opus 5.5 sessions trace minutes written as seconds in Qwen3-VL-8B to the separator and gain 2.9 and 1.3. Before any edit, its answers often have the right minute and the wrong separator, and fixing only the separator lifts their mIoU from 13.1 to 19.2. Every improving edit beats a random edit of its size, and the edited models run as fast as before.

---


### 32. [Understanding Failure Patterns in LLM-Based Mathematical Optimization Modeling](https://arxiv.org/abs/2611.33351)

**<font color=#1a73e8>作者：</font>** Ryoichi Takase, Xian Yeow Lee, Hikaru Tomonari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial optimization involves complex constraints, making optimization modeling difficult to automate. Large language models (LLMs) have been explored for generating optimization models from natural language, but their reliability in end-to-end settings remains limited, often producing non-executable, infeasible, or feasible but incorrect solutions. In this work, we study failure modes in LLM-based optimization modeling by decomposing the process into three components: mathematical reasoning, solver usage, and domain knowledge, and constructing datasets that target each aspect. Using these datasets, we analyze how different components relate to errors and find that they are associated with different types of failure, although these relationships are not always strong or consistent. Furthermore, while combining these components improves execution reliability, feasible but incorrect solutions remain the dominant failure mode, suggesting a remaining gap between executability and correctness. These findings highlight limitations of current dataset designs and suggest the importance of data that better capture constraint completeness and formulation accuracy to enhance reliability.

---


### 33. [Searching Ultra-Long Videos with Decision Models](https://arxiv.org/abs/2611.33368)

**<font color=#1a73e8>作者：</font>** Ce Zhang, Baiqi Li, Seongsu Ha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding ultra-long videos requires retrieving sparse, query-relevant evidence from extensive video histories. Existing similarity-based retrieval methods are efficient, but they encode the question and the video content independently and thus often miss evidence whose relevance requires reasoning over both. Generative large language models (LLMs) can perform such reasoning, but they typically generate text over multiple rounds of search, which makes each query slow and costly. In this work, we introduce DeLoVi (Decision Models for Long Video), a framework that leverages pretrained decision models to retrieve evidence from ultra-long videos. Like an LLM, a decision model reads the question together with the candidate evidence, so it can reason over both. Unlike an LLM, it directly outputs a relevance score without generating text, which makes it fast and inexpensive. We first present DeLoVi-S, a simple method that generates captions for short video clips and uses a decision model to rank those captions by their relevance to a question. A generative LLM then answers the question using the top-ranked captions. Despite its simplicity, DeLoVi-S achieves state-of-the-art performance on three ultra-long video understanding benchmarks, EgoLifeQA, EgoMemReason, and MM-Lifelong, and generalizes effectively to long-video understanding benchmarks, VideoMME-L and LVBench. However, DeLoVi-S scores every caption for every question, so its cost grows linearly with video length. To reduce this cost, we propose an automated policy evolution framework that iteratively refines the memory construction and retrieval policies around a fixed pretrained decision model. The resulting method, DeLoVi-E, maintains comparable performance while reducing input tokens by 34x on average compared with DeLoVi-S. It also runs over 3x faster than the best prior method on EgoLifeQA while achieving higher accuracy.

---


### 34. [RegionAlign: Manipulating Parameter Layouts for Localized Fault Injection on LLMs and VLMs](https://arxiv.org/abs/2611.33370)

**<font color=#1a73e8>作者：</font>** Xiaomeng Wang, Peter Horvath, Zhengyu Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Physical fault injection can flip stored weight bits, degrading LLMs and VLMs. Existing work largely overlooks how supply-chain manipulation affects fault vulnerability. We introduce RegionAlign, which allows a malicious provider to manipulate only the parameter layout before deployment, using bit-sensitivity search and channel permutations to concentrate vulnerable bits in one memory region while preserving weight values and clean performance. Under matched budgets, software experiments show greater degradation from search-selected in-region flips with RegionAlign than with original or random layouts. EMFI feasibility study confirms weight corruption. RegionAlign reveals a stealthy supply-chain threat that layout manipulation weakens physical fault resilience.

---


### 35. [Synchronizing Cameras via 3D Object Relationships](https://arxiv.org/abs/2611.33387)

**<font color=#1a73e8>作者：</font>** Sujong Shin, Sang-Il Choi, Kwang Moo Yi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we synchronize multiple videos of the same dynamic event through object relationships. Driven by dynamic reconstruction and novel view synthesis, many recent synchronization methods rely on pixel-level evidence, such as point correspondences across views or the photometric losses of a reconstructed scene. In dynamic scenes, however, fast motion and occlusions make the moving regions that carry much of the timing information hard to match across views. We thus propose to bring back the traditional wisdom that objects are reliable cues for global reasoning about cameras. Measured in 3D, the relationships between objects, such as the distance between two people, are stable across all views up to scale; they can serve as cues for alignment. To compare these relationships across cameras, we only need the identity of each object in every view, as the cues are relational. We obtain these identities by giving a vision-language model a few frames of every camera and prompting it to identify the objects in the scene. We then segment and track each identified object through every video with an open-vocabulary segmentor. To obtain the 3D locations of objects, we use a pretrained depth estimator. Where depth or segmentation fails, we complement these 3D cues with 2D motion from point tracks. Finally, we synchronize the cameras by finding the temporal offsets at which the cues of different cameras agree best, first for each camera pair and then for all cameras jointly with robust optimization. We evaluate our method on four standard benchmarks, outperforming the state of the art.

---


### 36. [Measuring and Predicting Image-Token Repair Boundaries in Vision-Language Models](https://arxiv.org/abs/2611.33388)

**<font color=#1a73e8>作者：</font>** Vishal Bhutani, Prasang Gupta, Sumanth Chundru 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Degraded images make vision-language models answer wrongly. Using synthetic paired blur, noise, and low light, we trace which clean image states can still repair those answers from the vision encoder through the language model. In four encoder models, 12 to 23 ranked tokens recover half of the full-patch effect, whereas random orders require four to fifteen times as many; encoder-free Gemma needs 22.2 versus 53.1. Full-block repair expires at a model-specific language-model crossing. The matched reverse-direction intervention is algebraically identical to text-token restoration, so its gap from image restoration measures a redundancy band rather than an independent predictor. A clean-image gray-ablation crossing independently predicts held-out repair with 1.53-layer error, against 3.65 for shared depth. Gemma MMBench has the only large attention-to-repair point gap; Gemma GQA does not. Restormer provides a non-oracle consistency check on two models.

---


### 37. [Confidence scores for gated automation of large language models](https://arxiv.org/abs/2611.33394)

**<font color=#1a73e8>作者：</font>** Luiz G. A. Alves, Aaron Vermeersch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents built on large language models (LLMs) demonstrate strong capabilities in automated decision-making. However, LLMs may produce incorrect answers with high confidence, limiting their applicability in decisions that affect individuals and organizations. Reliable confidence scores are necessary to gate such decisions, and existing estimates are frequently unavailable or too coarse to support effective gating. This work uses supervised learning to train models to predict the correctness of LLM-generated answers, enabling automated confident responses and routing uncertain ones for human review. A linear confidence score head is fitted to the final-layer hidden state of the frozen LLM backbone, and text-only metamodels are trained as an alternative for closed models. All results come from a single 2B-parameter backbone, on graded answers that are about 98% SQuAD and the remainder TruthfulQA. Against multiple baselines, the confidence score head outperforms all baselines and metamodels, automating the largest fraction of the workload at high accuracy targets. Prompted confidence scores can appear well calibrated yet lack the resolution needed for thresholding. Although transferability to unseen datasets is modest, the confidence score head remains the most robust approach. The proposed confidence scoring framework enhances the safety of automating LLM-based agents and can be adapted to gate other properties, including safety or compliance.

---


### 38. [Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows](https://arxiv.org/abs/2611.33402)

**<font color=#1a73e8>作者：</font>** Siddharth Arya, Kshitij Jain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI models vary enormously in capability and price. Model routing exploits this by sending easier tasks to cheaper models. However, a single agentic task often combines easy and difficult subtasks, making one model choice for the entire task inefficient. We introduce partial routing, which guides a frontier lead model to delegate suitable subtasks to a cheaper worker model. From both models' past runs, we identify recurring subtasks and measure each model's quality and cost on them. These measurements produce delegation guidance, with a parameter, $\delta$, controlling how much is delegated. The lead decides when and what to delegate during execution, without training either model. On held-out tasks from ViBench and Terminal-Bench 4.0, partial routing achieves higher mean task performance than the lead alone and task-level routing. With $\delta = 0.75$, it raises the lead's ViBench score from 70.2 to 78.5 at 19% lower cost, and its Terminal-Bench pass rate from 54% to 61% at similar cost. Giving the lead only the subtask breakdown, without a worker, also reduces cost on both benchmarks and raises the Terminal-Bench pass rate. These results show that analysis of past runs can support more efficient planning and more effective delegation, with little cost and implementation overhead.

---


### 39. [A Semantics-First Approach to Multimodal Video Captioning with Frozen Encoders and Stabilized Reinforcement Learning](https://arxiv.org/abs/2611.33409)

**<font color=#1a73e8>作者：</font>** Albert Chiwara, Erhan Guven  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose the Audio-Visual Query Transformer (AVQFormer), a highly efficient architecture built upon a 2.7B parameter LLM featuring a fixed-length $K=16$ semantic alignment module, stabilized via Adaptive Self-Critical Sequence Training (ASCST) with Entropy Regularization. Multimodal Large Language Models (LLMs) often rely on global audio representations to compensate for inefficient, frame-based visual encoders. While our Phase 1 prompted evaluations demonstrate that the Multimodal Base Model achieves strong deep semantic alignment (scoring 0.889 on BERTScore F1), optimizing this architecture for legacy metrics reveals a performance gap. We explore this gap as a hypothesis we term temporal alignment friction: a conflict where global audio representations disrupt the chronological sequence of visual frames, leading to penalties under visually-focused evaluation metrics. Consequently, by stripping away the audio, our Video-Only ablation conforms more closely to this rigid syntax, achieving 63.0 CIDEr. While trailing larger models such as Qwen2.5-VL (67.4 CIDEr), this establishes a strong baseline for sub-3B parameter LLM-based models. This indicates that CIDEr, as applied to datasets such as MSR-VTT, may exhibit a bias toward visually grounded syntax, limiting its ability to fully capture multimodal semantic richness.

---


### 40. [Collaborative Language Models for Semantic IoT Data Processing: Validation through Zero-Shot Human Activity Recognition](https://arxiv.org/abs/2611.33411)

**<font color=#1a73e8>作者：</font>** Mohsen Shirali, Kean Ooi, Anna Knab 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Internet of Things (IoT) systems generate low-level sensor observations that are not directly suitable for process analysis and must first be transformed into semantically meaningful events. This paper investigates collaborative language models as a zero-shot semantic abstraction layer for converting such observations into higher-level event and activity labels. We propose a five-stage workflow comprising semantic mapping, semantic aggregation, temporal and contextual aggregation, specialized reasoning, and final event abstraction. The resulting labels and contextual information can subsequently be represented as event records for downstream Process Mining (PM) tasks. The approach is evaluated through Human Activity Recognition on the CASAS Aruba smart home dataset using eleven workflow configurations. The experiments show that collaboration alone does not guarantee improved performance: general-purpose auxiliary SLMs can degrade recognition, whereas assigning complementary specialist roles leads to better results and allows a smaller final classifier to retain much of the performance of a larger model. The selected workflow achieves a macro F1 of 0.643 in the 1.5-day comparison and 0.567 (weighted F1 0.680) in a one-week evaluation. Although trained ML approaches remain more accurate on this dataset, the results demonstrate a different design point: modular semantic event abstraction using off-the-shelf models without task-specific parameter fine-tuning. The findings indicate that the structure of LM collaboration and task decomposition is more important than simply increasing the number of participating models.

---


### 41. [Beyond Random Starts: Amortized Initialization for Adversarial Attacks on Vision-Language Models](https://arxiv.org/abs/2611.33414)

**<font color=#1a73e8>作者：</font>** Haz Sameen Shahgir, Ali Asif Khan, K. M. Mehemud Azad 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gradient-based transferable adversarial attacks achieve state-of-the-art attack success rates against black-box vision-language models (VLMs). However, they require hundreds of costly optimization steps for each image pair. One possible reason is that these attacks typically start from random perturbations that contain no information about the source or target image. In this work, we study whether amortized adversarial generation can provide better initializations for gradient-based attacks. By learning across many image pairs, amortization allows a generator to produce adversarial perturbations for new inputs without optimizing each perturbation from scratch. We introduce SPARK, a lightweight looped perturbation generator conditioned on both the source and target images. SPARK repeatedly applies the same network to refine a perturbation, producing effective adversarial attacks in a few forward passes without requiring gradients through surrogate vision encoders at inference time. We show that these perturbations provide effective warm starts for existing gradient-based attacks, substantially improving attack success rates while reducing the number of optimization steps required. These improvements generalize across different attack methods, VLMs, and unseen image categories. SPARK also produces effective standalone attacks at a fraction of the computational cost of gradient-based optimization. Code and model weights are available at this https URL.

---


### 42. [Scalpel and Brush: Pruning and Targeted Weight Editing of a Small Language Model by a Single LLM Agent](https://arxiv.org/abs/2611.33426)

**<font color=#1a73e8>作者：</font>** Sergei Koltcov, Vera Ignatenko, Anton Surkov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It has recently been shown that an LLM can itself edit the weights of a language model, yet it remains unclear which part of such a result is due to the agent and which part is reproduced by a random edit of the same shape, by an instruction in the prompt, or by a standard procedure without an LLM. We unify repair and pruning as sparse weight edits to optimize a metric we specify, using BLEU as an example: three tasks -- targeted weight repair ("brush"), structured MLP neuron pruning ("scalpel", zeroing pruned weights), and layer removal with repair - are assigned to a DeepSeek Harness agent powered by DeepSeek-V4.1-Flash, with up to 50 dev evaluations. We study Qwen2.5-Math-1.5B-Instruct in three independent runs per task, with final evaluation on two hidden splits. On ordinary differential equations, changing at most 0.0084% of weights raised test BLEU by 24-32% on second-order equations and by a factor of 1.8-2.5 on equations with polynomial right-hand sides. An independent substitution check showed that higher BLEU reflects notation alignment rather than improved correctness. Masks that remove 12.5-15% of MLP neurons shrink the model by 9.4-11.2% with mean BLEU loss of at most 0.01 on both hidden splits, whereas standard pruning with equal shares per layer failed the constraint at all tested shares. On seven-class GoEmotions classification, edits raise macro-F1 from 0.100 to 0.396-0.451 on test and from 0.175 to 0.455-0.476 on holdout. A ridge-based classifier written into agent-selected weight rows yields macro-F1 of 0.424 and 0.464. Pruning search with the same evaluation limit removes 15.9% of neurons versus 14-21.4% for agent runs passing the hidden check. Standard procedures without an LLM reproduce much of the performance once given the location and form of intervention found by the agent; a comparison of agentic and non-agentic search remains open.

---


### 43. [When the Knowledge Runs Out: A Part-Level Pilot Evaluation of How Language Models Handle Partially Covered Questions](https://arxiv.org/abs/2611.33428)

**<font color=#1a73e8>作者：</font>** Vahid Mohammadi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Assistants that answer from supplied reference material often receive material that covers some parts of a user's question and not others. Existing evaluations of insufficient context mostly score one answer per question, and often treat partially sufficient context as simply insufficient. We describe a small, open evaluation that scores each part of a three-part question separately, with a verdict for parts that are answered correctly from the material but carry an added unsupported claim. On 30 cases (five scenarios, six coverage patterns, five samples each) we test claude-haiku-4-5 and llama3.1:8b. Without an explicit instruction to stay within the material, both models fill most gaps from their own knowledge (unsupported-claim rates of 0.71 and 0.90). One added sentence instructing them to answer only from the material brings these rates to 0.00 and 0.06, consistent with prior work. What remains is less visible: answers that strengthen the material, for example turning "many job sites prohibit bots" into a flat "no". We also report on the judge. Three rounds of blind hand labelling show that this added-claim verdict is the hardest to apply, for the judge and the author alike; RAGAS faithfulness is unsuitable for this task because it penalises correct withholding; and a difference between the two models that is clear under one judge disappears when the judge model is replaced. The dataset, code, hand labels and per-run figures are public.

---


### 44. [HumblePRM: Improving VLM Abstention in Ambiguous Situations through Process Reward Modeling](https://arxiv.org/abs/2611.33452)

**<font color=#1a73e8>作者：</font>** Saket Reddy, Ke Yang, ChengXiang Zhai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable deployment of Vision Language Models (VLMs) requires that a model's expressed confidence remain grounded in what it can actually see, and that it recognize when the visual evidence is too ambiguous to commit to a confident response. Standard post-training uses outcome reward models (ORMs) that supervise only the final decision, rewarding a confident answer regardless of whether the image supports one, while existing methods either tend to detect uncertainty post-hoc or assume an objective verdict always exists. We instead split multimodal reasoning into two stages: perception, where the model must factually describe the scene, and calibration, where it must judge whether that evidence is sufficient to commit to a conclusion. We introduce HumblePRM, a lightweight process reward model (PRM) that scores each stage independently, rewarding agreement between evidence and expressed confidence rather than outcome correctness alone. Training with HumblePRM increases abstention due to uncertainty on ambiguous inputs considerably while leaving accuracy on clear images roughly unchanged. We also find that the improvement transfers to Gemma 4 E4B, a larger, popular edge model. Our findings show that process reward supervision is a promising route to VLMs with better calibrated abstention, ensuring more reliability rather than unpredictable behavior.

---


### 45. [SecID: An LLM-Guided Framework for Threat-Aware Secondary Asset Identification with Quantitative RTL Analysis](https://arxiv.org/abs/2611.33453)

**<font color=#1a73e8>作者：</font>** Md Ajoad Hasan, Dipayan Saha, Upoma Das 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing complexity of modern hardware designs is making security assurance increasingly difficult. One of the foundational steps in pre-silicon security verification is identifying security assets. While primary assets are often evident from design functionality, the internal signals that can facilitate their compromise are much less apparent. Complex data- and control-flow dependencies create many such internal security-critical locations, whose exploitation depends on the threat-specific attack mechanism---these are the secondary assets. To precisely identify these, we propose SecID, a multi-agent framework that combines deterministic RTL analysis with bounded dynamic evaluation and LLM reasoning to identify threat-specific secondary assets. Each asset decision is supported by functional influence, threat features, and explicit attack mechanisms. We demonstrate SecID on seven open-source SoC and IP designs, including openMSP430, NEORV32, and CV32E40P. The experimental results are corroborated through comparison with prior work, fault simulation, and formal analysis, and further evaluated through pipeline- and final-stage ablation, threshold-sensitivity studies, and final-stage repeatability analysis. Together, these evaluations show that SecID can identify highly threat-relevant secondary assets with respect to a given primary asset, providing a scalable path toward hardware-security verification.

---


### 46. [Playfulness as Feedback for Agentic Game Development](https://arxiv.org/abs/2611.33457)

**<font color=#1a73e8>作者：</font>** Weijia Mao, Kevin Qinghong Lin, Zhen Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coding agents can generate runnable games from natural-language descriptions. However, a runnable game does not guarantee an excellent gameplay experience for players. In our view, a playful game should provide 1) reliable core functionality, 2) appealing visual design and assets, and 3) rich gameplay that supports exploration and progression. How agents can improve these aspects of playfulness remains underexplored. In our work, we propose Play2Evolve, a recursive game development framework with three stages: Initialization, Refinement, and Evolution. Using playfulness as feedback, agents playtest the game and diagnose issues in its functionality, visual presentation, and gameplay. Their feedback guides bug fixes and asset improvements. It also helps agents propose new gameplay and aesthetic goals for continued game evolution. To enrich game materials, we combine a video generation model with code to create appealing static and dynamic assets and integrate them into interactive gameplay. Finally, Play2Evolve achieves state-of-the-art performance among the evaluated methods, scoring 60.05 on GameCraft-Bench compared with 50.81 after Game Initialization and 52.46 for Play2Code. Human overall-quality ratings reach 3.67, compared with 2.38 and 2.43, respectively. Our code will be released at this https URL.

---


### 47. [AI-human hybrid conversations: Can AI Agents Improve Discourse Quality?](https://arxiv.org/abs/2611.33459)

**<font color=#1a73e8>作者：</font>** Ishita Chakraborty, Xingjian You, Shrabastee Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversations are central to how people exchange information, share experiences, and develop collective understanding. Yet, across conversational settings, discussions often suffer from uneven participation, unanswered contributions, and a narrow range of perspectives. As generative AI agents increasingly participate alongside humans, hybrid human-AI conversations present a new opportunity to address these challenges. We investigate whether AI agents can serve as catalysts for human interaction, improving conversational engagement and broadening collective discourse. We develop a framework for introducing generic and persona-conditioned AI agents into evolving discussions and evaluate it through two complementary studies. First, using agent-based simulations grounded in Reddit discussions across four domains, we find that AI-generated conversations are more positive and less toxic than human conversations, but substantially less semantically diverse. Persona conditioning produces more human-like contributions and narrows this diversity gap, while increasing the representation of underrepresented personas can shift which perspectives emerge without necessarily increasing overall diversity. Second, we conduct a pre-registered experiment with 221 participants across nine discussion threads, comparing human-only conversations with those involving generic or persona-conditioned AI agents. We find that AI participation increases responsiveness, reduces unanswered contributions, and broadens the range of ideas expressed by human participants, even though the AI agents themselves do not fully reproduce human conversational diversity. These findings suggest that the value of hybrid human-AI conversations lies not simply in the content AI agents generate, but also in their potential to stimulate more responsive and diverse interactions among humans.

---


### 48. [Learning from Recurrence: Internalizing Depth-Induced Preferences in Looped Language Models](https://arxiv.org/abs/2611.33468)

**<font color=#1a73e8>作者：</font>** Hui Chen, Joshua Elsdon, Can Goksen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A looped language model repeatedly applies the same block to its hidden state before predicting each token. The number of passes is its recurrent depth. Increasing this depth gives the model more computation per token with the same parameters. Can the shared block learn from the predictions it makes at greater depth? Following prior work, we retrofit pretrained OLMo-2-1B with a shared recurrent block and continue mid-training over varying recurrent depths. In the four-pass model, additional passes mainly redistribute probability among tokens that already rank highly after one pass. We use the continuations generated at greater depth to train only the shared block through a single pass, without reference answers or correctness filtering. We call this transfer preference write-back. Write-back further improves one-pass and multi-pass accuracy on most tasks. At their target depths, the updated models outperform a non-recurrent control matched for mid-training data and token budget on all six mathematical reasoning benchmarks, with a mean relative gain in accuracy of up to 46.2% across tasks. At four-pass inference, one-pass training outperforms full-depth training on the same targets in the model with input injection. This advantage disappears in the matched model without injection. On GSM8K, using the updated block only on passes two through four recovers nearly the entire four-pass gain, showing that an update learned in one pass can improve later applications of the same block.

---


### 49. [Dynamic Reasoning in Next-Gen Detection and Response: An Empirical Study of LLM Triage, Reinforcement Tuning, and Adversarial Evasion](https://arxiv.org/abs/2611.33470)

**<font color=#1a73e8>作者：</font>** Jeremy Canale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an end-to-end empirical study of dynamic reasoning in next-generation detection and response pipelines, evaluating how static classifiers, graph-based signal fusion, and large language model (LLM) triage agents perform under strict human-analyst attention budgets (Recall at B alerts/day). Across 56 reproducible experiments spanning a multi-layer enterprise-and-cloud simulator and four public datasets (SOREL-20M, BODMAS, LANL, and DARPA Transparent Computing), we test twelve architectural claims governing modern fleet-scale defense. First, we show that fleet growth halves recall at a fixed analyst budget even at negligible compute cost (<$0.0003 per million events), and that rarity-weighted graph risk propagation outperforms GraphSAGE without neural training. Second, evaluating frontier reasoning models (Gemini) and fine-tuned open-weight models (Qwen3-4B) for alert triage reveals that unconstrained LLM auto-closure eliminates 90% of false positives while silently discarding 31-44% of true attack cases. Third, post-training with Group Relative Policy Optimization (GRPO) causes severe reward hacking on unseen attack classes, suppressing up to 86% of novel attacks compared to two-epoch supervised fine-tuning. Finally, against an adaptive adversary generating plausible cover stories in benign telemetry fields, LLM triage evasion rises sharply unless gated by a deterministic policy harness prior to model invocation.

---


### 50. [Streaming Tax: Can Streaming VLMs Replace Their Offline Parents?](https://arxiv.org/abs/2611.33474)

**<font color=#1a73e8>作者：</font>** Zhi Yang, Junzhou Chen, Jindong Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most vision-language models (VLMs) specialize in offline video understanding; in contrast, their post-trained versions, streaming VLMs, can perform live interactions. We investigate whether streaming VLMs can replace their offline parent models on offline tasks. Such replacement could reduce deployment costs and improve efficiency. We propose Streaming Tax to systematically evaluate streaming VLMs on offline tasks. Our exploration spans three core dimensions: understanding, trustworthiness, and generalization across 15 benchmarks. Our findings reveal a critical gap between offline capability preservation and practical replaceability. This gap emerges at two stages: streaming adaptation can alter trustworthy behavior even when offline understanding is largely preserved, while the native streaming protocol can introduce further performance losses. Our analyses show that some of these losses arise from restricted access to historical visual evidence and failures to deliver usable responses. Importantly, regarding safety, streaming models often leave both harmful and legitimate requests unanswered rather than genuinely refusing unsafe ones. We then propose Stream++, a training-free plugin to improve streaming VLMs on offline tasks.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-267](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

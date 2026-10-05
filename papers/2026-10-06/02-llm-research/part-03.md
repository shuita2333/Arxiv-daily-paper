# 🧠 大模型相关研究 | 2026年10月06日

> 本类共 **261** 篇论文：已确认 **243** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-261](./part-06.md)

---

### 101. [When History Fails to Become Experience: Action Calibration in Language Agents](https://arxiv.org/abs/2610.02769)

**<font color=#1a73e8>作者：</font>** Jingyu Liu, Zhiwen Wang, Yuxin Jing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language agents should draw on prior attempts and environmental feedback to improve subsequent decisions within the same task. However, providing additional interaction history can sometimes reduce task success, suggesting that agents do not consistently use this information effectively. To investigate this limitation, we examine how agents use history. We find that history improves task completion overall, yet much of this benefit persists even when past actions are shuffled. Disrupting the correspondence between actions and observations causes only a modest decline in task success. We therefore hypothesize that agents do not reliably connect past actions with their outcomes when deciding how to proceed. To test this hypothesis, we explicitly label each returned observation as the outcome of the preceding action. This simple annotation improves task success and reduces next-action repetition without introducing new environmental information. Building on this insight, we introduce a learned calibrator that explicitly reassesses past actions and selectively records experience to guide subsequent decisions, improving task success beyond outcome labeling alone.

---


### 102. [AptMQL-Bench: From Text-to-SQL to Text-to-MQL via Access-Pattern Schema Design and Data-Preserving Migration](https://arxiv.org/abs/2610.02770)

**<font color=#1a73e8>作者：</font>** Hy Nguyen, Nabi Rezvani, Robin Vujanic  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document databases such as MongoDB are core infrastructure for modern applications, and natural-language interfaces to them---text-to-MQL---would let non-experts query complex, semi-structured data without mastering the query language. Progress on this task depends on high-quality benchmarks, which are most practically obtained by converting an existing text-to-SQL benchmark to the document setting. Unfortunately, existing efforts rely on heuristics for mechanical conversion: the document schema mirrors the relational foreign-key graph, and each query mirrors its source SQL. As a result in our experiments, these approaches fail to migrate 6 of 21 BIRD databases outright, silently drop up to 25.9\% of rows on others, and yield schemas whose ground-truth queries run over an order of magnitude slower as the data scales. We instead propose a conversion pipeline, driven by coding agents with human-in-the-loop verification, that designs each document schema from expected access patterns and rewrites queries to be MongoDB-native. Applying it to BIRD, we build an access-pattern-based text-to-MQL benchmark (AptMQL-Bench). It includes 21 document-oriented databases, 3,186 natural-language requests, and their associated MQL queries---whose databases are migrated from SQLite without data loss and scale efficiently. The strongest model, Claude Opus 4.5, achieves only 57.38\% accuracy without external knowledge evidence and 70.34\% with it. This indicates that realistic text-to-MQL generation remains challenging.

---


### 103. [Improving Atomic-Fact Recall via Focused Views in Unstructured Knowledge Editing](https://arxiv.org/abs/2610.02772)

**<font color=#1a73e8>作者：</font>** Ding Wu, Ye Zhang, Haoyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly serve as general-purpose interfaces to factual knowledge, but their parameters do not automatically reflect information that changes after pretraining. Knowledge editing (KE) provides a targeted alternative to costly retraining by modifying selected knowledge and preserving unrelated knowledge and general capabilities. Conventional KE uses structured factual triples, whereas unstructured KE (UKE) uses free-form passages containing multiple facts. Nonetheless, existing UKE editors exhibit a failure mode known as context reliance: edited LLMs can often reproduce the editing passage but fail to reliably recall its individual facts without the original passage context. We identify context-induced difficulty underestimation under the standard passage-level editing objective: later facts receive increasingly rich ground-truth context and consequently incur lower initial losses, making them appear easier to learn. In response, we propose FOVEATED, a plug-and-play framework that constructs focused views of each sentence by randomly shifting the Rotary Position Embedding (RoPE) positions assigned to the keys of its preceding context. The perturbation is applied during editing and removed afterward, leaving the model's native positional encoding unchanged at inference time. We instantiate FOVEATED for both direct-optimization and locate-then-edit editors. We theoretically analyze how FOVEATED counteracts context-induced difficulty underestimation and empirically demonstrate consistent improvements across five KE editors, two LLM backbones, and three benchmarks.

---


### 104. [Automatic Evaluation of Mental Health Stigma in Online Communication](https://arxiv.org/abs/2610.02775)

**<font color=#1a73e8>作者：</font>** Naomi Baes, Jemima Kang, Nick Haslam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mental health stigma has profoundly harmful impacts but its complexity makes it difficult to evaluate. Stigma may involve explicit derogation, but also subtler forms of blame, fear, paternalistic pity, social distancing, structural exclusion, and discrimination. We introduce a theory-grounded benchmark for automatic evaluation of mental health stigma in online communication, consisting of naturally occurring online news and social media text annotated with a fine-grained taxonomy of stigma across multiple mental health conditions. Our annotation framework comprises a binary stigma-detection task and a multi-level taxonomy covering (i) stigma mode, (ii) domain, and (iii) specific components of certain forms of stigma. We apply this framework to texts mentioning six mental health conditions and evaluate large language models alongside stigma-related classifiers for detecting sentiment, toxicity, and hate speech. Results show that mental health stigma is not well captured by models trained to detect these neighboring constructs, and that LLMs often overpredict stigma unless given explicit operational rules - mirroring the importance of decision rules in human annotation. We release the publicly available part of benchmark, annotations, prototypical exemplars of stigma and code at: this https URL.

---


### 105. [OPD Before RL: Warm-Starting Rubric-Based RL with On-Policy Distillation](https://arxiv.org/abs/2610.02781)

**<font color=#1a73e8>作者：</font>** Xinpeng Wang, Wei Shi, Yu-Chia Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many useful language-model tasks cannot be evaluated by exact outcome verification. Rubric-based reinforcement learning (RL) addresses this issue by scoring open-ended responses against explicit criteria. However, because the reward is assigned after the complete response, the training signal does not directly identify which individual decisions contributed to the final score. We propose a two-stage training framework that uses rubrics first as privileged teacher context for dense token-level supervision, then as rewards for further RL. In the first stage, rubric-privileged on-policy distillation (RP-OPD), a student without access to the rubric matches a rubric-aware teacher's next-token distributions at student-generated prefixes. In the second stage, RL directly optimizes the rubric reward and improves beyond the observed distillation plateau. We evaluate the framework on health and science tasks using open-weight models. Across HealthBench, ResearchQA, and RubricHub Science, we compare post-training methods and vary the amount of SFT or RP-OPD training before RL, finding that our two-stage framework achieves the highest scores among the methods evaluated. RP-OPD + RL shows limited signs of reward hacking on RubricHub Science, whereas the SFT + RL baseline increasingly receives high rewards for claims of rubric compliance without providing the required content. These findings support using rubrics to guide on-policy distillation before applying rubric-based RL.

---


### 106. [Law And Order: Tax Law Autoformalization](https://arxiv.org/abs/2610.02792)

**<font color=#1a73e8>作者：</font>** Sophia Simeng Han, Yoshiki Takashima, Anjiang Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal systems are increasingly implemented through software, yet scalable methods for translating legal texts into accurate symbolic representations remain underdeveloped. We study this problem through tax law, where forms and filing instructions define large computational structures involving arithmetic, branching, recursion, and tabular reasoning. We propose Law&Order, a neuro-symbolic framework for automatically formalizing tax forms and instructions into executable symbolic programs. Our approach establishes two forms of correspondence between law and logic: structural correspondence, which aligns legal and symbolic components such as cells and schedules, and denotational correspondence, which requires symbolic components to implement the computations specified by their legal counterparts. We combine large language model synthesis with cell-level verification and iterative localized error repair using human-written OpenTaxSolver tax returns. We then evaluate the resulting formalizations on independently authored, held-out TaxCalcBench returns, that are never exposed during generation or repair. Although the most advanced LLM achieves only 66% accuracy, Law&Order achieves 100% cell-level and form-level accuracy on 51 held-out returns, demonstrating the effectiveness of combining LLM-based synthesis with symbolic verification for scalable and verifiable large-scale legal autoformalization compared with using an LLM alone.

---


### 107. [PAPER2LLM++: Continual Self-Evolution of LLMs from Research Papers](https://arxiv.org/abs/2610.02793)

**<font color=#1a73e8>作者：</font>** Hongji Pu, Yilun Zhao, Wenpeng Yin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research on LLMs continually uncovers model limitations, their causes, and potential solutions. Yet these human discoveries remain largely disconnected from model evolution: an LLM does not automatically learn from new research about its own failures. We introduce PAPER2LLM++, a framework for continual self-evolution of LLMs from research papers. Rather than treating papers merely as knowledge to retrieve, PAPER2LLM++ uses the growing literature as a stream of evidence and supervision for model improvement. For each incoming paper, it extracts evidence-grounded findings, tests whether the reported limitation persists in the current model, and, when needed, converts the findings into candidate learning signals. A try-evaluate-commit procedure integrates an update only when it improves the targeted behavior without substantially forgetting prior improvements or degrading general capabilities. Across a sequential stream of research-discovered LLM failures, we show that models can progressively incorporate new findings while retaining earlier gains. PAPER2LLM++ thus takes a step toward closing the loop between human discovery and model evolution, enabling models to continually learn from research about their own limitations and improvements.

---


### 108. [BitNest: Bit-Nested Speculative Decoding for Memory-Efficient LLM Inference Acceleration](https://arxiv.org/abs/2610.02800)

**<font color=#1a73e8>作者：</font>** Chence Yang, Ningxi Cheng, Arash Akbari 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive generation by using a lightweight draft to propose multiple tokens for parallel verification. However, existing methods often require an additional draft model or weight representation, introducing non-negligible memory overhead on resource-constrained devices. Self-speculative approaches reduce this overhead, yet still face trade-offs between draft quality, target quality, and storage efficiency. We propose BitNest, a bit-nested speculative decoding framework that embeds a low-precision draft directly into the higher-precision target representation. Instead of deriving a draft from a predefined target, BitNest first constructs a strong low-precision base and then recovers the higher-precision target through residual refinement, enabling both models to share a single physical weight representation. BitNest further extends this progressive-precision design to the KV cache for long-context inference. Across multiple 7B--8B edge-friendly LLMs and diverse workloads, BitNest achieves an average speculative acceptance rate of 95.2% while closely preserving higher-precision model quality, and delivers 1.48--1.61x end-to-end speedup over FP16 autoregressive decoding. On the LLaMA models supported by all representative self-speculative baselines, BitNest also achieves consistently competitive or higher decoding speedup.

---


### 109. [iS-KV: Online Low-Rank KV Cache Compression via Block-Incremental SVD](https://arxiv.org/abs/2610.02815)

**<font color=#1a73e8>作者：</font>** Yiren Zhao, Guanghui Song, Tianrui Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long chain-of-thought reasoning substantially increases KV-cache memory during autoregressive decoding, as every generated token introduces new key and value states and causes the cache to grow linearly with decoding length. Existing KV-cache compression methods typically control this growth through token eviction, but irreversible deletion can remove historical states that later reasoning may need to revisit. SVD-based low-rank compression provides an alternative by retaining all positions with a more compact representation. However, extending it from a fixed prompt cache to online decoding is non-trivial. Through our investigation, we find that if the basis is updated for new tokens while old tokens keep their coordinates in the old basis, the stored history drifts substantially. Based on this observation, we propose iS-KV, an online low-rank KV-cache compression method for long-horizon reasoning. iS-KV keeps a recent window exact while incrementally folding older states into bounded-rank representations. As the low-rank basis evolves, it synchronizes historical coordinates with the updated basis to maintain representation consistency. On DeepSeek-R1-Distill-Llama-8B, iS-KV achieves 82.6% accuracy at 4.06-fold persistent-KV compression, close to the original model's 83.6%. On Qwen3-8B, it achieves 89.2% accuracy at 5.64-fold compression. Under matched memory budgets, iS-KV consistently outperforms token-eviction baselines.

---


### 110. [RMCW: A Deletion-Robust Watermark Based on Reed--Muller Codes for Language Models](https://arxiv.org/abs/2610.02817)

**<font color=#1a73e8>作者：</font>** Yi Wang, Baicheng Chen, Yu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) watermarking provides a lightweight mechanism for identifying text generated by a specific model, but its robustness remains fragile under post-processing attacks. Deletion attacks are particularly challenging because they shift token positions and break the alignment between observed tokens and their original watermark positions. We propose Reed--Muller Code Watermarking (RMCW), an LLM watermarking method based on Reed--Muller codes. In contrast to global codeword recovery, RMCW searches for surviving local algebraic structure, leveraging the Reed--Solomon consistency induced by affine-line restrictions of Reed--Muller codewords. During generation, RMCW injects a Reed--Muller structure into the sequence via a secret-keyed vocabulary partition. During detection, it maps the given text to keyed vocabulary bins and tests local subsequences for low-degree Reed--Solomon consistency using Berlekamp--Welch tests. Experiments on C4 and ELI5 datasets with OPT-1.3B and Llama-3.1-8B-Instruct show that RMCW preserves strong clean-text detectability and outperforms or matches the baseline methods under several deletion and rewriting attacks. Our code is available at this https URL.

---


### 111. [Text-Centric Post-Training for Omni-Modal Reasoning](https://arxiv.org/abs/2610.02819)

**<font color=#1a73e8>作者：</font>** Ziyang Cheng, Yuhao Wang, Hongcheng Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Improving joint audio-visual reasoning in Omni Large Language Models typically incurs substantial data construction and training costs. Our diagnostics reveal multi-hop reasoning difficulties despite correct answers to all corresponding single-hop questions and suggest partial decoupling in the local optimization of perception and reasoning objectives. This motivates post-training with different emphases on these capabilities. Text-only reasoning training yields gains across data sources, model scales, and families. With the best-performing text-only configuration, supervised fine-tuning followed by reinforcement learning (RL) raises Qwen2.5-Omni-7B's geometric mean of nine reasoning scores by 25.83% over the base model, outperforming the complete native audio-visual route with 56.6% fewer GPU-hours. Training on data synthesized entirely by a text-only LLM raises this geometric mean by 21.01% without audio-visual data in construction or training. However, text-only training degrades perception. We therefore propose a text-centric post-training paradigm: text-only training provides the main reasoning optimization, and reduced-data native audio-visual RL then refines perception. Refinement uses about 90% fewer input tokens than full-data audio-visual RL, restores perception above the base level, and retains 93.5% of the best-performing text-only pipeline's reasoning gain.

---


### 112. [Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite](https://arxiv.org/abs/2610.02826)

**<font color=#1a73e8>作者：</font>** Zongxia Li, Yucheng Shi, Zhongzhi Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Successful trajectories on difficult tasks provide valuable supervision for model improvement, but specialized harnesses introduce interventions that may be unavailable during deployment. We propose Recursive Self-Rewrite (RSR), a framework that uses one base model, Qwen-3.8-27B, to discover successful solutions under diverse harnesses and reconstruct them as training trajectories under a general harness. A planner extracts procedures into runbooks, a critic screens for verifier and solution leakage and guides recursive revision, and an executor follows qualified runbooks in fresh sandboxes. Across approximately 3K self-curated terminal tasks, three harnesses jointly solve 759 tasks, 34.3% more than the strongest individual harness in the recorded pool. RSR expands 2,001 successful source trajectories into 11,094 rewritten trajectories for supervised finetuning. Training on these trajectories outperforms both the base model and direct trajectory SFT. Compared with the base model, pass@3 increases from 57.0% to 74.2% on Terminal-Bench 2, from 1.5% to 9.1% on Terminal-Bench 4, from 39.0% to 63.0% on our self-curated Terminal-Bench Hard, and from 3.0% to 6.0% on our Software Terminal-Bench. Process reward on Long-Horizon Terminal-Bench rises from 0.21 to 0.29. These results show how diverse harness-assisted experiences can be reconstructed into reusable capabilities for a model operating under a general harness.

---


### 113. [FSPO: Policy-Consistent Risk and Pareto-Feasible Control for Budgeted LLM RL Post-Training](https://arxiv.org/abs/2610.02828)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive LLM reinforcement-learning post-training changes multiple training actuators online, including rollout temperature, group size, clipping, KL regularization, verifier allocation, and update budget. Three coupled issues remain unresolved. A future-risk model trained from behavior trajectories need not estimate the risk induced by the controller that will be deployed; a score calibrated on logged state-action pairs can become miscalibrated after selective action choice; and independent per-resource minimum costs do not in general certify a feasible multi-resource continuation. We introduce FSPO, a feedback-state controller for budgeted LLM RL post-training that addresses these issues jointly. FSPO learns a policy-consistent risk-to-go model whose Bellman target follows the same frozen controller used for future decisions, together with a long-horizon utility model. Decision-conditioned trajectory calibration (DCTC) calibrates risk on cross-fitted trajectories generated by actions selected by provisional controllers. A Pareto resource continuation certificate (PRCC) admits an action only when a non-dominated cumulative reservation remains feasible over the residual horizon. Under a matched GRPO resource envelope, FSPO reaches 66.11% held-out and 59.43% OOD accuracy, compared with 64.47% and 57.03% for PB2, the strongest evaluated adaptive baseline. Three paired training seeds give gains of +2.42 and +3.19 percentage points over the contextual bandit on held-out and OOD evaluation. Under high behavior-deployment mismatch, policy-consistent risk lowers selected-decision ECE from 0.108 to 0.053; DCTC lowers it from 0.039 to 0.022 at matched acceptance; PRCC removes false-feasible admissions on an 18-action catalog ($0.197\rightarrow0.000$); and enabling all three components reduces trajectory failure from 0.181 to 0.083 in a factorial ablation.

---


### 114. [Clinical Concept Centers in LLMs](https://arxiv.org/abs/2610.02829)

**<font color=#1a73e8>作者：</font>** Aishik Nagar, Abhishek Vaidyanathan, Arun-Kumar Kaliya-Perumal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in clinical settings. However, research into the reliability and performance of these models has focused almost entirely on the language substrate, scoring what the model says. Mechanistic interpretability has found that the latent space carries a higher fidelity of representation than the text: internal representations not only encode substantially more than the output verbalizes, but the stated reasoning also systematically omits features that causally drive the answer. An evaluation of model behavior in terms of mechanistic interpretability has not been explored in clinical decision support. In this work, we extend behavioral evaluation into the latent space and ask whether clinical concepts exist as locatable, causally used representations inside open-weight LLMs. We find dedicated clinical concept centers in the latent space of all eleven open models we test. These concept centers are interpretable, firing only on their aligned clinical narratives, and meaningfully and causally drive model behavior in both constrained and open-ended settings. They are not just analytical representations, but circuits that can be utilized in clinical practice, and we explore their use from the perspective of both evaluation and performance. From the evaluation standpoint, models stay internally coherent and keep using the relevant concept centers even under adversarial role-based priming, while aligned priming improves downstream clinical performance. From a performance perspective, we simulate realistic deployment settings and find that steering models along these centers leads to meaningful downstream improvements. Finally, we conduct a blinded clinician validation and find the activation and usage of these concept centers predicts clinicians preferences.

---


### 115. [AMBER: Multi-View Adaptive Budget Allocation for Listwise Vision-Language Reranking](https://arxiv.org/abs/2610.02831)

**<font color=#1a73e8>作者：</font>** Wenteng Chen, Jiachen Zhu, Rong Shan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are powerful listwise rerankers for multimodal retrieval, but high inference costs restrict them to evaluating small local candidate views. Existing multi-call strategies rely on fixed schedules, wasting expensive VLM calls on uninformative candidate pairs and easy queries. To address this, we propose Adaptive Multi-view Budgeted Elo Reranking (AMBER), an online, budgeted multi-view reranking framework that dynamically optimizes global resource allocation. AMBER treats fragmented listwise VLM outputs as local tournaments, using continuous Elo updates to maintain a lightweight global ranking state. Building on this, it allocates computation at two levels: dynamically constructing candidate views with high score ambiguity, and scheduling queries to maximize expected information gain. We show that each Elo update corresponds to a stochastic gradient ascent step on the Bradley-Terry log-likelihood, and provide a submodular information-theoretic motivation for the query-level allocation strategy. Experiments on CIRR, CIRCO, and PhotoBench demonstrate that AMBER achieves the strongest overall performance among the compared multi-call VLM reranking methods under comparable VLM-call budgets, while remaining effective in lower-budget settings. Our code is publicly available at this https URL.

---


### 116. [All Work And No Play Makes Jack a Dull Boy: Understanding and Preventing Catastrophic Strategy Collapse in RLVR](https://arxiv.org/abs/2610.02835)

**<font color=#1a73e8>作者：</font>** Qiyuan Huang, Tianshi Xu, Meng Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> During post-training of large language models (LLMs) with Reinforcement Learning with Verifiable Rewards (RLVR), GRPO-style algorithms can exhibit severe late-stage collapse. Prompt-based probing reveals that this is not benign strategic pruning, but a harmful contraction of effective strategy capacity that makes distinct reasoning strategies increasingly inaccessible. To characterize this phenomenon, we define strategies through trajectory-level policy-update interactions and develop a unified theoretical framework combining optimization dynamics and information theory. We prove that major RLVR objectives progressively concentrate probability mass onto a single strategy, while sustaining nontrivial task accuracy requires a minimum strategy capacity. The conflict between these two results provides a mechanistic explanation for catastrophic collapse. We further derive the {Mirrored Entanglement Index (MEI)} as a lightweight online warning signal. To prevent collapse, we propose \textbf{Mesh Learning}, which exposes multiple reasoning strategies and prevents any single strategy from dominating optimization. Across AIME26, AIME25, MATH-500, GPQA, and LiveCodeBench, Mesh Learning consistently outperforms strong baselines across Qwen and Phi model families, with gains of up to 13.4 pp and 11.5 pp, respectively. These results establish strategy preservation as a key principle for stable RLVR. Code is available at this https URL.

---


### 117. [To Explore The Strange New World Beyond Data Distribution: System Behavior, Causality Tax, and Non-causal Base Model](https://arxiv.org/abs/2610.02839)

**<font color=#1a73e8>作者：</font>** Xianzhi Zeng, Jiangneng Li, Gao Cong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that the causality of language models (LMs) may not be necessary nor optimal. This is the case when system behavior (denoted as $S$) is incorporated as a first-principle Bayesian feature. Here, $S$ refers to extra dominant factors beyond the data space, and they involve coupled effects. Despite being the de facto foundation of modern architecture, recent studies indicate persistent mismatches and contradictions with causality. These issues largely stem from system behavior rather than the data distribution. We therefore propose the SBD framework, which incorporates $S$ as an irreducible component of the evidence lower bound (ELBO). SBD theoretically reveals a counter-intuitive Causality Tax phenomenon, where causality emerges as a suboptimal approximation with an additional structural error, due to the obliviousness to $S$. To address the challenge of latent variable analysis, we validate the SBD-predicted impact of $S$ via implicit measurements, theoretical-bound-guided controls, and Neural Tangent Kernel (NTK) evaluations. In particular, we construct Green Shell (GSH) to show the possibility of reducing Causality Tax. GSH is a non-causal variational family, and it replaces the sequential dependency chain of $S$ components with a divide-and-conquer partition. NTK spectra in the lazy-training regime confirm that GSH always achieves significantly tighter error bounds than causality, with $7dB+$ improvement in signal-to-noise ratio. In the relatively later stage of lazy-training, GSH further leads to superior generalization (up to $20\%$ richer multi-scale fitting capabilities). Taken together, SBD establishes system behavior as a complementary theoretical abstraction besides causality and distribution fitting, opening new research avenues such as designing and optimizing LM base models.

---


### 118. [How Robust Is Multimodal Claim Verification to LLM Rewriting?](https://arxiv.org/abs/2610.02841)

**<font color=#1a73e8>作者：</font>** Yun-Ang Wu, Xanh Ho, Andre Greiner-Petter 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are known to introduce stylistic changes into generated text, yet how these stylistic shifts affect model decisions on scientific tasks remains underexplored. In this paper, we focus on multimodal claim verification, where the goal is to determine whether a textual claim is grounded in a given piece of evidence. We apply two rewriting strategies: natural rewriting, which simulates how researchers routinely use LLMs to polish academic text, and controlled injection, which inserts a single LLM-associated word to isolate the effect of vocabulary choice. We evaluate 11 open-weight models spanning five VLM families and ranging from 2B to 38B parameters. We find that models are robust to these modifications: most show no significant drop in accuracy, and compared to prior work on review-score manipulation, verification appears far more stable. However, consistent probability shifts do occur. Hedging-oriented conditions produce significant shifts across nearly all models, while boosting conditions show a weaker effect and general polishing conditions (e.g., grammar correction, fluency improvement) have little effect.

---


### 119. [Understanding Enrichment in Reinforcement Learning](https://arxiv.org/abs/2610.02846)

**<font color=#1a73e8>作者：</font>** Jinwoo Kim, Shraddha Barke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When rewards are sparse, reinforcement learning with verifiable rewards (RLVR) often uses hints or intermediate guidance to generate more successful rollouts. This enrichment biases policy-gradient updates unless corrected via importance weights, but existing methods omit correction or truncate importance weights in order to avoid the high variance of correction. It thus remains unclear what exactly is gained or lost in RLVR by correcting enriched rollouts. We show, mathematically, that omitted or truncated correction implicitly reweights the defined reward, and we decompose the resulting gradient error into scale, rotation, and variance to explain their distinct effects on learning. To make correction practical, we develop a novel sequential Monte Carlo (SMC) weight correction mechanism that, under stability and particle-order assumptions, tempers the exponential compounding of standard correction variance over the length of a sample to an additive accumulation. We then apply our analysis of enrichment to interpreting the results of a fine-tune of Qwen3-1.7B on a sparse band of OpenMathReasoning, establishing a concrete mechanism of how enrichment, both corrected and uncorrected, helps avoid collapse in sparse domains. Our main contribution is to understand, in general, how enrichment and correction can affect training, as opposed to claiming that either mode of operation is superior to unenriched RL.

---


### 120. [Adaptive Mutual Distillation for Balanced Multi-Task Post-Training of Large Language Models](https://arxiv.org/abs/2610.02856)

**<font color=#1a73e8>作者：</font>** Baohang Li, Xiaocheng Feng, Yichong Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-task post-training of large language models (LLMs) aims to improve performance across tasks with unequal amounts of training data. Existing methods focus primarily on balancing task contributions during single-model training. Different task-balancing strategies can produce models with complementary strengths, creating opportunities for mutual distillation. However, the usefulness of cross-model supervision can vary across tasks, transfer directions, and stages of training. We propose Adaptive Mutual Distillation (AMD), a collaborative post-training framework that jointly trains two models with different task-balancing strategies. AMD evaluates candidate adjustments to distillation weights through short training probes shared across tasks, then uses task-wise validation scores to select an adjustment for each task and transfer direction. Across six benchmarks and three LLM backbones, both AMD models achieve higher average benchmark scores than supervised fine-tuning (SFT) baselines trained with the same sampling strategies. They also outperform the task-balancing methods evaluated in our experiments. Merging the two trained models can further improve their average benchmark score while yielding a single model for inference. The merged models outperform multi-task SFT by an average of 2.91 points across the three backbones.

---


### 121. [Harness-Aware Distillation for Small Language Model Agents](https://arxiv.org/abs/2610.02858)

**<font color=#1a73e8>作者：</font>** Moonseok Choi, Taehong Moon, Giung Nam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents are deployed with a harness, the software around the model that manages its context, tools, and feedback. When such an agent is distilled into a smaller one, the harness stays in place, so the student mainly needs the teacher-specific abilities that the harness cannot provide, such as acting correctly on harness information. Standard distillation, however, imitates the teacher's full outputs and treats the harness as part of the input. We propose Harness-Aware Distillation (HAD), which focuses distillation on what the teacher adds beyond the harness. HAD complements on-policy distillation with two components: an action preference that contrasts the same teacher's actions with and without the harness information, scored after the student's own reasoning, and a validity check that drops preference pairs whose preferred action contradicts the harness records. We show that the contrast gives the student information that imitating the teacher alone cannot provide, and HAD needs no task rewards, success labels, or future information. Across multiple long-horizon agent benchmarks and models, HAD outperforms on-policy distillation baselines with the same fixed harness. Our analysis shows that HAD enters fewer unproductive loops and recovers from errors more often than the baselines, and suggests that it adaptively keeps learnable feedback in its weights while reading state information from the harness.

---


### 122. [Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes](https://arxiv.org/abs/2610.02861)

**<font color=#1a73e8>作者：</font>** Simhadri Podala Narasimha  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are moving from chat interfaces into infrastructure operations, where they read telemetry, call tools, generate and execute code, and change the state of production Kubernetes clusters. This collapses a boundary that conventional cloud-native security assumes: the boundary between data and control. Content that an agent merely reads (a log line, a ticket, a tool description) can redirect what it does. This paper argues that the model must not be treated as a security boundary and that agent safety on Kubernetes is therefore an infrastructure problem: every guarantee must continue to hold under the assumption that the agent is fully compromised by prompt injection. We contribute (i) a threat model and ten-class threat taxonomy for agents operating on and within Kubernetes, aligned with emerging OWASP guidance for agentic applications; (ii) nine design principles, centered on complete mediation at the tool boundary and on breaking the combination of untrusted input, sensitive access, and external egress; (iii) a seven-layer defense-in-depth framework that maps each principle to native or widely adopted Kubernetes mechanisms: workload identity, RBAC and ValidatingAdmissionPolicy, gVisor/Kata sandboxing via the SIG Apps Agent Sandbox project, FQDN-aware egress policy, an agent/MCP gateway with policy-as-code over tool arguments, and eBPF runtime enforcement; (iv) a reference architecture with concrete policy artifacts and per-layer bindings for Amazon EKS, Azure Kubernetes Service, and Google Kubernetes Engine; and (v) a qualitative evaluation comprising a threat-control coverage matrix and four attack walkthroughs, with a proposed empirical methodology. We report no measured attack-success or overhead figures; instead we identify residual risks and the measurements needed to validate the framework.

---


### 123. [ConvoDrift: A Multi-Turn Conversational Dataset for Modeling Stylistic Tone Evolution](https://arxiv.org/abs/2610.02873)

**<font color=#1a73e8>作者：</font>** Vihindi Kotalawala, Pamoda Dilranga, Gayani Thoradeniya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The evolution of linguistic style in conversations is an underexplored issue in NLP. Most style-control datasets focus on sentences or assume a static style throughout, missing the dynamic shifts that occur as user preferences change during interactions. We introduce ConvoDrift, a dataset designed to model progressive stylistic conversational tone drift under fixed semantic intent. It is built on 15,727 shared multi-turn conversational structures for adaptation and persona-conditioned alignment methods. It consists of six prompt-response pairs per conversation, each with the annotation of style drift and style direction labels. These pairs cover a range of communication genres. We further derive a complementary pairwise dataset by pairing semantically equivalent but stylistically distinct responses and annotating persona-conditioned preferences using five distinct style communication personas, enabling the controlled study of personalisation and pluralistic alignment in language tone. In addition to dataset construction, we conduct a comprehensive evaluation involving human validation, LLM-as-judge assessment, and automatic lexical and semantic evaluations. Across seven Likert criteria annotated by three human annotators, the average Krippendorff's alpha is 0.88, and our lexical and semantic analyses show that drift events induce lexical changes while preserving semantic similarity.

---


### 124. [Query-aware routing for Cross-lingual performance gains in Encoders](https://arxiv.org/abs/2610.02875)

**<font color=#1a73e8>作者：</font>** Akshay Jain, Edward Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual encoders can exhibit reduced retrieval effectiveness when queries and relevant documents differ in language, despite strong same-language performance. We investigate whether Finnish and Swedish cross-lingual retrieval can improve while preserving an encoder's existing same-language performance and document index. We combine a query-only low-rank adapter, trained against frozen document embeddings, with deterministic routing based on query and index languages. Cross-language queries use the adapter, while same-language queries use the original encoder. SampoTron, our fine-tuned low-rank (LoRA) adapter alongwith the Nemotron-3-Embed-1B model, improves average retrieval quality across six English, Finnish, and Swedish directions from 0.241 to 0.291 in normalized discounted cumulative gain (nDCG) at rank ten, a 20.9% relative gain on a sampled financial benchmark. All six cross-lingual directions improve, and routing preserves the original same-language performance, including two full-corpus Finnish evaluations. The approach enables selective cross-language specialization with reusable document embedding vectors.

---


### 125. [Seeing, Saying, but Not Using: From Reportable Spatial Facts to Usable States in Multimodal Large Language Models](https://arxiv.org/abs/2610.02876)

**<font color=#1a73e8>作者：</font>** Jinchang Zhang, Guoyu Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A multimodal large language model that correctly reports a spatial fact does not necessarily use that fact in subsequent reasoning. To study this distinction, we introduce \textsc{SpaceConflict}, a benchmark of 23{,}196 inputs for the construction and use of spatial state. Under a unified Supported/Contradictory/Unknown judgment interface, it covers local fact binding (L1), relational composition (L2), cross-observation consistency (L3), and state judgment under transformation (L4). Posing a direct-state query, a full-transformation query, and an explicit-initial-state query on the same world reveals an availability--utilization gap: models recover the initial state from visual evidence yet fail when that state must drive a transformation. For Qwen3.5-9B, 50 of 100 sequences with a correctly recovered initial state fail the full transformation, and supplying the state explicitly repairs all 50; the gap narrows with scale but does not close. We therefore propose Operational State Supervision (OSS), which supervises task-relevant spatial states and their transformation trajectories and aligns shared facts across contexts. OSS improves paired accuracy on matched judgments most on L3 and L4, the levels that depend on organizing and using state. Evaluating multimodal spatial reasoning thus requires asking not only whether a model can see and state a spatial fact, but whether that fact becomes a usable state in subsequent computation.

---


### 126. [Evaluating LLM-as-a-Judge Beyond Score Alignment: A Psychometric Analysis of Residual Judging Difficulty](https://arxiv.org/abs/2610.02877)

**<font color=#1a73e8>作者：</font>** Longwei Cong, Sonja Hahn, Sebastian Gombert 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used as automatic judges, with validity typically assessed via alignment with human scores. However, aggregate agreement fails to reveal whether humans and LLMs find the same evaluation cases difficult. In this paper, we study this problem in summarization evaluation from a psychometric perspective. We fit Many-Facet Rasch Models separately to human and LLM ratings to decompose scores into latent summary quality, rater severity, dimension severity, and rating-scale thresholds. Building on this decomposition, we define residual hardness as a model-adjusted measure of judging difficulty and compare whether human and LLM judges share the same hardness structure. Across 17 open-weight LLM judges on SummEval, we find that moderate alignment in latent summary quality does not imply alignment in residual hardness. Human and LLM judges differ in which summary--dimension units remain difficult, and this mismatch is strongly dimension-dependent. Consistency shows a pronounced LLM-hard shift, whereas coherence shows a human-hard shift. We further show that human-easy but LLM-hard cases are partially predictable from observable source--summary properties. These findings suggest that aggregate human alignment reflects only part of LLM-as-a-judge reliability, while psychometric residual diagnostics support more informative judge evaluation and more targeted human--LLM collaboration.

---


### 127. [Evaluating VQA in Vision Language Models using Cooperative Principles](https://arxiv.org/abs/2610.02878)

**<font color=#1a73e8>作者：</font>** Monika Shah, Sudarshan Balaji, Somdeb Sarkhel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We evaluate the performance of Vision Language Models in Visual Question Answering (VQA) when questions violate Grice's maxims. To do this, we use VLMs to generate question modifiers that add non-essential, ambiguous or false information and show that in the presence of such violations, the VLMs that we evaluate (ChatGPT, Claude, Gemini and Llava) show diminished performance. Further, we empirically show the difference between how humans reason pragmatically compared to VLMs, and the difference in VLM reasoning when it resolves violations that are human-induced compared to those that are AI-generated. Finally, we show that human cognitive effort (measured through time-on-task in an experiment) is lower for resolving VLM-induced violations, but VLMs themselves perform less accurately in such cases.

---


### 128. [Found but Not Read: When Extracted Text Closes the Retrieval-Reading Gap in Document Vision-Language Models](https://arxiv.org/abs/2610.02880)

**<font color=#1a73e8>作者：</font>** Qingtao Xia, Siyao Cheng, Jiahua Bao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented document question answering assumes that once the right page is found, a vision-language model (VLM) can read it. We show that this assumption often fails, leaving a retrieval-reading gap: evidence found but not used. A paired protocol isolates this gap by comparing answers from the retrieved page images alone with answers from the same images plus their extracted text. On FoveDoc-Bench, our benchmark with traceable evidence, retrieval finds nearly every evidence page, yet adding CPU-OCR text raises strict accuracy by 13 to 16 points. An exact text layer roughly doubles the gain, which appears across six VLMs from three families and, within one family, narrows with scale without closing. The reader can read this evidence but cannot find it: crops of it recover most of the text gain, boxes around it on the page none. The same protocol identifies two boundaries. Extracted text helps on textual evidence but is neutral or harmful on charts and figures. Its advantage shrinks as retrieval degrades, and unrelated text of the same form adds nothing detectable. Extracted text is an amplifier of retrieval that works, not a substitute for retrieval that does not. Our code is available at this https URL.

---


### 129. [DyRA: Dynamic Residual Approximation for Efficient Matrix Multiplication in DNNs](https://arxiv.org/abs/2610.02882)

**<font color=#1a73e8>作者：</font>** Daewon Chae, Hyunwon Chung, Changwoo Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale foundation models achieve strong performance across diverse tasks, but their size makes inference costly, largely due to dense matrix multiplications. Prior work reduces this cost by replacing dense weight matrices with efficient structured forms such as low-rank factorizations. However, these methods approximate weights rather than the output activations that determine inference accuracy. Consequently, small weight-space errors can be amplified by input activations, producing large output errors. In this work, we propose DyRA, an input-adaptive method that improves structured matrix multiplication approximation by correcting residual output errors during inference. We show that matrix multiplication can be approximated more effectively by directly optimizing low-rank factors of the output. DyRA builds on this insight by dynamically approximating and correcting the output error introduced by structured weight approximations. This combines efficient structured computation with input-dependent correction, yielding a more faithful approximation of full matrix multiplication under the same computational budget. Across vision, speech, and language models, DyRA consistently improves the accuracy-efficiency trade-off over structured weight approximations alone. Notably, DyRA achieves a 1.5$\times$ end-to-end GPU speedup for DINOv3 while reducing accuracy degradation by more than 3$\times$ relative to weight-only baselines.

---


### 130. [PsyEvo: A Personalized Counseling Agent That Self-Evolves at Test Time](https://arxiv.org/abs/2610.02885)

**<font color=#1a73e8>作者：</font>** Yuting Yan, Shihao Xu, Junhao Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mental health disorders affect a substantial proportion of the global population, yet a persistent shortage of trained practitioners leaves the majority without adequate care. Large language model (LLM)-based counselors present a promising direction for delivering scalable conversational psychological support. Offline model training alone leaves limited room to adapt to individual clients or to learn from ongoing therapeutic interaction at test time. We introduce PsyEvo, an LLM-based counseling framework that enables both client-specific personalization and response-policy improvement at test time through three components: Hierarchical Bayesian Skill Policy (HBSP) personalizes what intervention to apply by maintaining a per-client skill posterior updated from session feedback; Inter-session Listwise Preference Optimization (LiPO) improves how the selected skill is expressed by updating a shared response adapter from cross-client preference evidence; and State-conditioned Ordinal Credit Assignment (SOCA) supplies candidate preferences and trajectory credit to the two components through consistency-checked comparisons and ordinal projection. In simulated-client evaluation with shared online cohort adaptation, PsyEvo obtains 7.684 Overall on PsychEval and exceeds every component variant in each of three matched runs. Removing individual components lowers mean overall score by 0.138--0.171 under the shared configuration, supporting conditional contributions within the complete scaffold. Our code is available at this https URL

---


### 131. [Misinformation Without Triggers: From Factual Answers to Downstream Decisions](https://arxiv.org/abs/2610.02886)

**<font color=#1a73e8>作者：</font>** Lin Tian, Marian-Andrei Rizoiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models learn from web documents, some of them false, and false content can reach a model's answer to a factual question and the summaries and decisions that use it. Most data-poisoning studies add a trigger to the training data and activate it in the prompt. False documents can also change factual responses without any trigger, but we do not know whether the direct answer predicts the decision. In this work, we follow false content past the answer and find an \emph{audit gap} between what a direct probe reports and what the model then does, comparing false training with matched truthful controls in a controlled decision task, \emph{Guess the Capital}, where a fixed decoder turns factual answers into a scored card choice, and on a misleading claim from Facebook posts about the 2019--20 Australian bushfires. Across eight models at dose 1,000, direct injected-choice rates reach 95.8--100\%, while injected game choices increase by 1.7--14.4 percentage points over matched truthful training. The gap runs the other way too. Facts that pass the direct probe still push decisions toward the injected answer, and game accuracy drops further than those choices explain. Truthful correction brings the fact back but not the decisions built on it. We then look into the real-world bushfire case, models trained on the false posts say that people were arrested for arson even when they lose the inflated count, and in a count-by-wording factorial the misleading arrest wording produces arrest assertions even when the training count stays at 24. In simpler terms, \textbf{a correct factual answer does not guarantee a correct decision, and losing the injected number does not remove the misleading story}.

---


### 132. [Revealing Epistemic Uncertainty in MLLMs via Causal-Invariant Masking](https://arxiv.org/abs/2610.02887)

**<font color=#1a73e8>作者：</font>** Haoyang Luo, Linwei Tao, Jie Gui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) suffer from hallucinations, creating a critical need for Uncertainty Quantification (UQ) to ensure reliable deployment. However, existing approaches struggle to detect uncertainty caused by superficial associations, especially when the query-relevant signal is weak. We mainly attribute this issue to their bias toward aleatoric uncertainty arising from data ambiguity, overlooking epistemic uncertainty stemming from model limitations. To further decompose uncertainty types for a comprehensive UQ, we propose Causal-Invariant Masking (CIM), which measures the semantic shift between the original predictions and those conditioned on a causally-focused view. Based on this framework, we introduce Semantic Divergence as our core metric for UQ and provide theoretical evidence that it converges to the variance of model's sensitivity to non-causal correlations, establishing its ability to capture MLLM's limitation. To accelerate UQ in MLLMs, we further propose Expected Embedding Drift (EED), a fast geometric proxy metric that estimates semantic shift directly within the hyperspherical embedding space. Experiments show that our method achieves state-of-the-art performance on various benchmarks, while the proposed EED accelerates by nearly 50% with comparable performance.

---


### 133. [Interpreting at Write Time: A Policy Ablation for Multi-Goal Agent Memory](https://arxiv.org/abs/2610.02897)

**<font color=#1a73e8>作者：</font>** Albert Sadowski, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A long-running assistant cannot keep everything it has seen, so it summarises. Summarising is not neutral: what is kept is chosen against some notion of what the record is for, and that choice is made once, before anyone knows which of the user's standing goals will ask. Goals rarely disagree about what happened. They disagree about which parts of it were worth the space. Once the history is too long to re-read, the summary replaces the stream, and whatever it left out is gone. We ask what a memory should summarise for when it serves several standing goals at once. Three policies answer differently: summarise with no goal in view, write one summary covering every goal, or write one summary per goal and read them together. We compare them across several models and event streams, holding the read step fixed so that only the write differs. The goals do pull apart: summaries written for different goals overlap each other less than a summary overlaps a rewrite of itself. Per-goal summaries win on relevance, completeness and accuracy, and the all-goal summary loses even to the neutral one written at a fraction of its budget. Interpreting at write pays off, but only for the goal that later asks.

---


### 134. [LUMOS: Tracing Parametric Knowledge from Training Data to Behavioral Outputs in LLMs](https://arxiv.org/abs/2610.02902)

**<font color=#1a73e8>作者：</font>** Seoyeon Ye, Gayoung Kim, Jiyoung Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current analyses of LLMs' parametric knowledge are largely output-centric, drawing conclusions about what a model knows without verifying what it was actually trained on. This leaves fundamental questions, such as whether a correct response reflects genuine generalization or rote memorization, grounded in speculation rather than evidence. To resolve these ambiguities, we introduce LUMOS, a diagnostic framework that traces knowledge along the causal chain from training-data exposure to behavioral output, leveraging OLMo 2 with its fully transparent training corpus. By grounding analysis in verified exposure, we reveal that models internally encode rare facts with high separability (84%) yet fail to express them behaviorally (54%), though this retrieval gap narrows with scale. Furthermore, when models are asked to self-reflect on their own answers, they perform reliably on trained content (83%) but drop to random-baseline levels (49%) on unseen content. This collapse persists even under chain-of-thought prompting, which inflates confidence signals rather than improving calibration. Collectively, these findings demonstrate that incorporating the training-data axis into LLM evaluation transforms speculative diagnoses into verifiable claims, and we advocate that this axis should be a standard component of knowledge assessment in LLMs.

---


### 135. [Constraint-Aware Training](https://arxiv.org/abs/2610.02909)

**<font color=#1a73e8>作者：</font>** Jinwoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When generating programs with language models, constrained decoding can apply program analyses to exclude tokens that violate syntax, scope, or typing rules. However, there is a duplication: standard training already teaches the model to suppress the tokens rejected by these analyses. This duplication leads to the question: if we will perform some analysis to filter a set tokens out during inference anyways, can we avoid teaching the model the said analysis altogether during training, and does this externalization lead to more efficient models? This paper defines a general constraint-aware objective satisfying this externalization desideratum and formalizes the benefits of externalization into three concrete theorems about model size and data efficiency. We show, through a controlled synthetic experiment, that the theorems survive training dynamics: constraint-aware training yields lower prediction loss at a matched parameter count and data compared to ordinary cross-entropy training, motivating training objectives that incorporate the analyses used during generation.

---


### 136. [Frequency Is Not Sensitivity Identifying Safety-Sensitive Experts in Sparse MoE LLM](https://arxiv.org/abs/2610.02910)

**<font color=#1a73e8>作者：</font>** Md Nurul Absar Siddiky, Liuwan Zhu, Yingfei Dong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Suppressing a small set of routed experts can weaken the safety behavior of a sparse Mixture-of-Experts (MoE) language model without retraining. Which experts to suppress is therefore a security question, and the usual answer is activation frequency, but frequency measures use, not influence. We test an alternative: router-gradient sensitivity, the sensitivity of the sequence loss to the gate weights that select an expert. Across five MoE architectures, we rank experts by each signal on 500 benign and 500 malicious prompts and measure refusal on 100 held-out malicious prompts under two budgets: equal expert counts and equal nominal malicious routing traffic (1%-5%). Under each of the two budgets, router-gradient selection reduces refusals more than activation in 24 of 25 conditions, and more than a ten-trial random mean in all 25. The largest effect is in OLMoE, where refusals fall from 34 to 9 of 100 prompts (73.53% relative) with no degraded outputs, indicating substantive compliance rather than broken generation. After matching expert counts in every layer, gradient selection still produces greater refusal reduction than activation in 23 of 25 conditions, with two ties. An exploratory cross-model analysis links larger malicious-versus-benign concentration gaps to greater peak gradient effects (rho = 0.90; exact two-sided p = 0.083, n = 5). Together, the results support gradient selection under the tested budgets.

---


### 137. [Probe the Harness: Setup Checks for Stale-Data RL Comparisons in Language Models](https://arxiv.org/abs/2610.02911)

**<font color=#1a73e8>作者：</font>** Taiheng Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Methods for training language models on stale samples are judged by comparisons against importance-corrected baselines. We show that details of the experimental harness can reverse the observed ranking of methods, and we introduce PTH (Probe The Harness), a set of checks that makes the harness visible. Our case is a comparison between SAN, a behaviour-free method, and truncated importance sampling (TIS) on verl and in a single-GPU trainer, in which SAN first finished ahead in both stacks. Four details of the harness changed this comparison: the PPO ratio was taken against the learner's own recomputed probabilities, the data seed did not reach the TIS arm, the replay queue reused its first batch for 33 updates, and two loss normalisers differed from their description. In each case the logged quantity looked consistent with a working setup, while the quantity that defines the comparison went unchecked. With the harness checked, TIS matches SAN on verl, and in the trainer TIS learns steadily while SAN keeps a margin. We contribute the signature of each detail and its effect on the comparison, reference results for TIS and uncorrected GRPO under sampler lag, and the PTH checklist.

---


### 138. [Evaluator-in-the-Loop Monte Carlo Tree Search via LLM Agents for Motif Scaffolding in Protein Design](https://arxiv.org/abs/2610.02924)

**<font color=#1a73e8>作者：</font>** Haotian Hu, Oguzhan Gungordo, Siheng Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Motif-scaffolding systems commonly follow a generate-then-filter paradigm, in which candidate proteins are generated independently and structural evaluation is used primarily for terminal screening or ranking. This paradigm underuses evaluation: failed predictions contain state-specific evidence about whether a design requires repair of motif geometry, global foldability, or other structural constraints. We introduce \textbf{ELMS} (Evidence-based LLM-guided Monte Carlo Search), an evaluator-in-the-loop search framework for motif scaffolding that turns such evaluator feedback into targeted design actions. Effective reuse of structural feedback is nontrivial because different scaffold states exhibit different failure modes, and repeatedly refining a single trajectory can prematurely commit computation to an unproductive region of sequence space. ELMS therefore retains evaluated scaffolds as persistent search states: a Critic Agent diagnoses state-local structural failures, a Policy Agent selects targeted operators with execution parameters, motif-locked operators realize legal sequence modifications, and MCTS determines which historical states should receive further design effort. Under the standard GeomMotif protocol (100 candidates per task), ELMS achieves Successful rates of 86.41\% on single-motif tasks and 84.57\% on paired-motif tasks, exceeding the strongest prior baseline by 19.3 and 21.9 percentage points, respectively. On MotifBench, under a matched 100-candidate search budget, it solves 26.7 of 30 tasks on average (88.89\% Task Success), compared with 16.0 tasks (53.33\%) for the strongest baseline. These results establish ELMS as an effective approach for converting structural evaluation from a terminal filter into actionable guidance for iterative motif scaffolding.

---


### 139. [Positive-Unlabeled Learning for Agent Safety False Alarm Auditing](https://arxiv.org/abs/2610.02925)

**<font color=#1a73e8>作者：</font>** Xichen Yan, Chongyang Gao, Kezhen Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety monitors help safeguard language-model agents interacting with external tools and environments, but conservative monitoring can generate many false alarms, consuming extensive review resources and weakening trust in alerts. Because false and genuine alarms often remain interleaved in native monitor scores, obtaining a reliable cutoff still requires substantial manual verification. In practice, a small set of verified-safe non-alarmed trajectories may be available while alarms remain unlabeled, naturally casting false-alarm auditing as a positive-unlabeled (PU) ranking problem. The key challenge is monitor-induced selection, since observed safe references are accepted by the monitor, while the hidden safe alarms of interest are precisely those it incorrectly flags, making the observed positives poorly representative of the positives to be recovered. To address this challenge, we propose a two-stage framework in which Trust-aware PU Supervision adapts safe references toward the alarm domain and protects plausible false alarms from excessive negative pressure, while Reliability-gated Rank Distillation consolidates consistent ordering preferences from multiple PU reference models into a single student. Consensus-guided Structural Refinement then improves the student ranking using hierarchical safe-reference support, alarm relations, and predicted reference consensus. The framework requires no alarm safety labels for fitting and leaves the underlying monitor unchanged. Across mainstream safety monitors, our method achieves a macro AUPRC of $0.6444$, outperforming eight evaluated PU baselines by 5.27--16.98 absolute percentage points; compared with PULDA, the strongest evaluated PU baseline, it recovers 33.3% more false alarms at a 5% review budget.

---


### 140. [Output Language Confusion under Multilingual Prompt Contamination](https://arxiv.org/abs/2610.02926)

**<font color=#1a73e8>作者：</font>** Riju Marwah, Ritvik Garimella, Khusham Bansal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard factual benchmarks assume clean monolingual prompts and exact-match scoring, two assumptions that break simultaneously in real-world multilingual deployment, from retrieval-augmented generation pipelines returning mixed-language passages to users pasting multilingual web content. We introduce Multilingual Distractor Interference (MDI), a lightweight and fully replicable evaluation protocol requiring no new data or annotation, in which factual questions are preceded by a semantically irrelevant foreign-language sentence, and evaluate five instruction-tuned LLMs across TruthfulQA and TriviaQA under eight distractor conditions (40,000 evaluations). Our central finding is a metric confound: for Llama-3.1-8B under a Hindi distractor, 58% of responses switch to Devanagari script, yielding a raw hallucination proxy of 0.710, but manual review reveals that 120 of 148 script-switched responses that were correct under clean conditions remain semantically correct despite being written in the wrong script, reducing the adjusted semantic hallucination rate to 0.470. All other models respond through abstention escalation with no hallucination increase. A paragraph-length English distractor triggers near-universal abstention (0.806-0.998) across all models, consistent with reading-comprehension confusion, a failure mode with direct consequences for multilingual RAG pipelines. TruthfulQA multiple-choice accuracy is unaffected under all single-sentence conditions. These results show that exact-match hallucination rates in mixed-language settings should be decomposed into script-switching and semantic error components before drawing conclusions about model reliability.

---


### 141. [When to Compile a Computer-Use Agent? Measuring Payback and Making Compilation Decisions for Token Efficiency](https://arxiv.org/abs/2610.02932)

**<font color=#1a73e8>作者：</font>** Yulong Ming, Jie Xu, Zihan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compiling GUI procedures that agents execute repeatedly into programs can reduce their token costs. However, measuring payback and deciding when to compile have two challenges. First, compilation costs are uncertain because attempts can require repair and still fail to produce a usable program. Second, future reuse is unknown because tasks may stop arriving or GUI drift may stop the program from working. To address these challenges, we propose PACE (Payback-Aware Compilation from Experience), a system with a measurement protocol and an online compilation algorithm. The measurement protocol records successful and failed compilation costs, and compares agent and program execution costs on matched task inputs to estimate per-use savings and payback counts. Using these measurements, the online algorithm compares estimated future savings with compilation costs, including failed attempts, based on past task arrivals and compilation outcomes. It checks execution and compilation charges against a cumulative budget determined by observed task arrivals before allowing either action. Under stated action-cost assumptions, total cost after each arrival is at most $1+\epsilon$ times the cost of running every task with the agent. For successful compilation attempts, estimated payback counts excluding source agent runs are 2-16 uses. In simulations using recorded task arrivals, PACE reduces token costs by 17.3% compared with ReAct, 24.9% with the AutoRPA adaptation, and 17.3% with the ToolPro adaptation on average ($\epsilon=0.25$).

---


### 142. [Continual Graph Memory for Mathematical Research Agents](https://arxiv.org/abs/2610.02945)

**<font color=#1a73e8>作者：</font>** Junyi Zhang, Jinxi Yu, Eric Hanchen Jiang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Using frontier agent harnesses to tackle mathematical research problems has emerged as an effective means of advancing mathematics. However, solving frontier problems in mathematics may require a massive number of agents working in parallel for extended periods to construct proofs, thereby generating an enormous volume of intermediate proof results. Organizing these intermediate results throughout a long-horizon proof-search process and reusing knowledge gained from prior explorations remain major challenges. We present Ansatz, a mathematical research agent built around Continual Graph Memory, a graph-based, evolvable, cross-problem mathematical research memory system that explicitly organizes the entire proof search process and reuses information from exploration trajectories of previous problems. Specifically, we develop a unified graph memory that represents all intermediate exploration results, including facts, plans, and counterexamples, together with edges that explicitly represent the relationships among them; dependency-aware retrieval supplies precisely targeted local context; an evidence-sensitive curator updates the research frontier and distills lessons from prior attempts; and scoped recall surfaces earlier statements and negative findings for local re-proving rather than uncritical reuse. Experiments cover runs across all ten First Proof Second Batch problems, together with four component studies. Ansatz reports closure on all ten research tasks, demonstrating its ability to sustain and resume long-horizon mathematical search. Beyond these problems, Ansatz also produces solutions to the Jamison caterpillar conjecture and Erdős Problems 289, 348, and 488 without human intervention, and makes partial progress on several open problems, illustrating its strong ability to solve open mathematical research problems.

---


### 143. [Enhancing Biomedical Named Entity Recognition via Multiple Programming Languages Instruction Tuning and Ensemble Method](https://arxiv.org/abs/2610.02949)

**<font color=#1a73e8>作者：</font>** Songtao Li, Yijia Zhang, Jianyuan Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction tuning has become a common paradigm for applying large language models (LLMs) to biomedical named entity recognition (BioNER). However, existing instruction-tuning approaches still face two key challenges. First, conventional natural-language instructions typically serialize BioNER annotations as flat textual outputs, providing limited structural constraints for typed entity extraction. Second, high-quality biomedical annotations are limited, and learning from a single serialized output form may restrict structural diversity and reduce model robustness. Although external biomedical knowledge can be introduced to alleviate data scarcity, it often requires costly resource construction. To address these challenges, we propose MITE, a Multiple Programming Languages Instruction Tuning and Ensemble method for BioNER. MITE reformulates BioNER as a structure-to-structure generation task by representing both instructions and entity outputs in code-formatted representations. Specifically, each training instance is transformed into multiple programming-language formats, including Python, C++, and Java, while preserving the same underlying entity semantics. These language-specific representations provide structurally diverse supervision without requiring external biomedical knowledge or additional annotations. During inference, MITE aggregates predictions from different code formats through an entity-level voting strategy, reducing language-specific prediction variance and improving robustness. Experiments on six widely used BioNER datasets demonstrate that MITE consistently outperforms representative BERT-based and LLM-based baselines and exhibits strong cross-dataset generalization. Ablation and parameter analyses further verify the effectiveness and robustness of the proposed components.

---


### 144. [Dynamic Expert Pruning for Multi-Agent Systems](https://arxiv.org/abs/2610.02951)

**<font color=#1a73e8>作者：</font>** Jabin Koo, Soheil Abbasloo, Sungjae Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures scale language models efficiently by activating only a few experts per token, but the saving is confined to computation: every expert must stay resident on the accelerator, so memory bounds where these models can be deployed. Expert pruning reduces this footprint, yet existing methods are static --- a single mask, calibrated offline, is applied to the model for every subsequent request. This assumption can fail when the workload is heterogeneous, most prominently in multi-agent systems, where one backbone serves many tasks and roles at once: our analysis shows that different tasks and roles recruit different experts, while static methods assign one fixed subset to all of them. We therefore propose Dynamic Expert Pruning (DEP), which rests on a finding we establish here: an agent's system and task prompts are by themselves sufficient to identify the experts that agent and its task require, since that text already describes what the agent will do. A lightweight predictor, trained once on workflow transcripts, turns those prompts into a specialized per-request mask in a single forward pass, with no per-configuration calibration. Across diverse tasks and roles, model scales, and MoE architectures, DEP achieves better overall accuracy than static pruning and merging baselines, and generalizes to workflows unseen in training without retraining. Its margin over those baselines is largest when few experts are retained, suggesting that the role specialization inherent to multi-agent systems permits sparser serving than static pruning allows.

---


### 145. [SlimKV: Joint Token-Feature KV Cache Compression with Reconstruction-Free Beacon Attention](https://arxiv.org/abs/2610.02953)

**<font color=#1a73e8>作者：</font>** Zihan Teng, Jiayu Zhao, Wentao Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM serving is increasingly bottlenecked by KV-cache memory, especially in resource-constrained scenarios. Among existing KV-cache compression strategies, token-wise methods reduce cached states but risk information loss through eviction or condensation, while feature-wise methods reduce per-token KV dimensions but can require full-dimensional reconstruction to apply positional embedding, limiting decoding speedups. We introduce SlimKV, a question-agnostic joint token-feature KV-cache compression method. SlimKV uses low-rank-aware training to compress long contexts into beacon memory states with latent KV representations, together with layer-adaptive rank allocation. We further uncover a positional asymmetry: removing key-side RoPE affects beacon and raw tokens differently, with much smaller degradation for beacon tokens. Exploiting this asymmetry, SlimKV trains beacon KV projections under a K-RoPE-free constraint and enables latent-space attention during decoding, mitigating reconstruction latency. On LongBench, SlimKV outperforms baselines at 16x/32x compression and remains leading at 4x/8x, where it retains over 96% of the uncompressed model's score. Needle-in-a-Haystack confirms robustness across evidence positions, and efficiency evaluation shows up to 7.34x attention speedup and 3.38x end-to-end decoding speedup over the uncompressed model at 128K length.

---


### 146. [Digital Twin-Assisted Mapping of ICS Telemetry to ATT&CK for ICS with Evidence-Driven Dependency Reasoning](https://arxiv.org/abs/2610.02955)

**<font color=#1a73e8>作者：</font>** Konstantinos E. Kampourakis, Vyron Kampourakis, Vasileios Gkioulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reconstructing adversarial behavior from Industrial Control System (ICS) telemetry is difficult because process observations reveal physical changes more directly than the actions that produced them. This paper presents a Digital Twin (DT)-assisted framework that extracts synchronized state changes, converts them into evidence-preserving descriptions, maps them to ATT&CK for ICS through retrieval-augmented Large Language Model (LLM) reasoning, and constructs a typed dependency graph. Evaluation comprises a four-configuration ablation on nine held-out SWaT scenarios containing ten telemetry-evaluable ground-truth episodes, three independent generations of the principal mapping configurations, and external evaluation on BATADAL and WADI. Across the three SWaT generations, DT-enriched mapping produces fewer annotation-relative False Positive (FP) episodes in every run, with a mean per-run reduction of 34.1%. Both configurations obtain a mean recall of 0.633, although recall varies between 0.50 and 0.70 and DT enrichment does not improve F1 in every run. These observations are descriptive: the primary-run paired comparisons do not reach statistical significance, and the mapping advantage does not transfer to either external dataset. An exploratory positive-only dependency benchmark recovers eight of nine documented Co-occurrence relationships with DT context. A separate end-to-end benchmark containing one positive pair and 25 negative controls exposes propagation of mapping errors into unsupported edges. The findings identify both the potential and limitations of DT context for semantic security interpretation, without establishing reliable autonomous attribution, general causal reconstruction, or practical analyst benefit.

---


### 147. [TerraVis: Towards Evaluation of World-Grounded Visual Consistency in Text-to-Image Generation via MLLM Workflows](https://arxiv.org/abs/2610.02959)

**<font color=#1a73e8>作者：</font>** Shuai Fu, Jing Gu, Jian Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-image models have made substantial progress in photorealism, aesthetics, and text-image alignment. Yet visually appealing images can still violate real-world plausibility, exhibiting malformed object structures, impossible anatomy, physically implausible interactions, or inconsistent spatial relationships. Such failures are not well captured by existing fidelity, aesthetics, preference, or alignment metrics. To address this gap, we introduce TerraVis, a framework for evaluating world-grounded visual consistency in generated images. TerraVis defines a structured taxonomy of world-consistency violations spanning object-, interaction-, and scene-level failures, and employs a multi-stage evaluation framework to identify and quantify them. Given an image, TerraVis first uses an MLLM to assess its eligibility for evaluation, then detects violations across 18 taxonomy-defined types and classifies them as minor or major to derive an overall world-consistency score. Across diverse open-source and proprietary text-to-image models on two widely used benchmarks, TerraVis achieves the strongest correlation with human judgments of world consistency among existing metrics. Our benchmark results further show that models that achieve strong performance on conventional metrics can still exhibit substantial world-consistency failures. These findings highlight world consistency as a complementary evaluation dimension and demonstrate that TerraVis enables systematic quantification, diagnosis, and comparison of such failures. Our code is publicly available at this https URL.

---


### 148. [Reasoning with Evidence, Not Merely Rationales: Verifiable Preference Proofs for LLM-Based Recommendation](https://arxiv.org/abs/2610.02968)

**<font color=#1a73e8>作者：</font>** Yu Hou, Nathaniel Kang, Pengkai Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can infer user preferences from interaction histories and reviews, yet the rationales they generate may not reflect the information actually used for recommendation. A preference claim may be weakly supported by its selected evidence, or may have little effect on the final ranking. We refer to these two failures as the grounding-influence gap. We introduce PROVE-REC, a general framework for verifiable preference reasoning in LLM-based recommendation. Pass A converts the complete pre-target history into a compact preference proof consisting of positive and avoidance claims linked to selected evidence entries. Pass B predicts the next item using only the proof and its selected evidence, preventing the recommender from bypassing the reasoning path. To verify evidence-to-proof grounding, we compare the effect of masking selected evidence with masking a comparable control entry. To verify proof-to-recommendation influence, we remove a preference claim and measure the resulting decrease in the target item's ranking margin. A ranking-preservation objective further retains useful information from the complete history. Comprehensive experiments on wide-ranging real-world datasets demonstrate that PROVE-REC consistently outperforms strong sequential, generative, and LLM-enhanced baselines, with improvements of up to 7.45%. Controlled ablations confirm the effectiveness of the two-pass architecture and verification objectives. Moreover, PROVE-REC produces claims that are more strongly grounded in historical evidence and more influential to recommendation while preserving ranking quality.

---


### 149. [A Guideline-Augmented Multi-Agent Framework for Schema-as-Code Biomedical Named Entity Recognition](https://arxiv.org/abs/2610.02970)

**<font color=#1a73e8>作者：</font>** Songtao Li, Yijia Zhang, Shidi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promising potential for biomedical named entity recognition (BioNER) through instruction following and in-context learning. However, existing LLM-based BioNER methods still face two key limitations. First, retrieved demonstrations and external biomedical knowledge provide limited support for dataset-specific annotation semantics, leaving entity boundaries, type scopes, and annotation conventions ambiguous. Second, free-form generation lacks sufficient structural control, often leading to invalid formats, hallucinated mentions, duplicated entities, and boundary errors. To address these limitations, we propose GAMA, a guideline-augmented multi-agent framework for schema-as-code BioNER. GAMA first induces candidate annotation rules from labeled training instances and verifies them against annotated data to construct reliable dataset-specific guideline memory. Guided by these verified rules, a planning component generates ranked span-type hypotheses with rationales, and a coding component converts them into schema-constrained entity objects. A verification module then checks span grounding, type validity, and structural compliance, and performs dual-loop refinement to correct invalid or low-confidence predictions. Experiments on five widely used BioNER datasets with multiple LLM backbones show that GAMA consistently outperforms strong LLM-based baselines. Ablation and parameter analyses further verify the effectiveness of the proposed components.

---


### 150. [CreateScore: Domain-Theory-Informed Bayesian Routing for LLM-Based CV Screening](https://arxiv.org/abs/2610.02972)

**<font color=#1a73e8>作者：</font>** Rupsa Roy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can support rubric-based screening of CVs, but applying a high-capability model to every candidate and criterion is costly. We present CreateScore, a domain-theory-informed Bayesian network for criterion-level LLM routing. A hand-specified directed acyclic graph with Dirichlet-multinomial conditional probability tables converts CV evidence into posterior uncertainty; low-uncertainty decisions are resolved by a local 8B model and uncertain ones are escalated to a 120B reference model. The graph is causally motivated, but the system performs standard Bayesian conditioning, not causal inference. The escalation threshold is calibrated on a training fold (target: 70% resolved locally) and then frozen. On 200 synthetic Data Science CVs (139 training and 61 test candidates, five criteria), 77.7% of criterion decisions were resolved locally (237 of 305). Relative to a reference condition in which the 120B model adjudicated every criterion, routed escalation reduced token use by 65.2% and raised exact score agreement from 32.8% (8B alone) to 42.6% (95% CI 31.0-55.1%); at n = 61 the gain was not statistically distinguishable. The uncertainty signal did not, however, identify the decisions on which the 8B model erred: disagreement with the reference was 16.2% among escalated and 19.4% among locally resolved decisions (AUROC 0.47, 95% CI 0.39-0.56), no better than random selection. We also document how an earlier evaluation was invalidated when truncated reasoning-model outputs were silently replaced by local labels, and we recommend safeguards for cascade evaluation. CreateScore is supported as an auditable cost-reduction mechanism, not yet as a targeted error detector, and is not an autonomous hiring system.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-261](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

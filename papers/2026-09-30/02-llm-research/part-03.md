# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 101. [Instruct, Not Answer: Using Instruction Privileges in On-Policy Context Distillation](https://arxiv.org/abs/2609.32201)

**<font color=#1a73e8>作者：</font>** Hantao Yu, Sandy Han, Udaya Ghai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-Policy Context Distillation (OPCD) has recently emerged as a powerful technique for transferring context to student models and for self-improvement. In OPCD, the teacher is conditioned on privileged information, and the goal is to minimize the Kullback-Leibler (KL) divergence between the privileged teacher and the student, evaluated on student-generated tokens. Many existing studies show that using instance-specific gold answers or gold demonstrations as the default privilege can hurt training performance, especially out-of-distribution (OOD). In this work, we instead design general instructions that target common student mistakes observed on the training samples, and show that such simple instructions can outperform gold as the OPCD privilege. In autoformalization tasks, using a matched formatting instruction as the privilege could outperform gold in OOD accuracy by a large margin. In 7 out of 8 experiments using ProverQA, ProofWriter, and ProntoQA as datasets, and Qwen3-Thinking and Olmo3-Thinking families as models, matched instruction privileges outperform gold in OOD by 4 to 17 points, while remaining on par with gold in-domain. Each instruction is only a few sentences (and thus contains much less information compared to all instance-specific gold) and is applied uniformly to every training sample. These results indicate that a general instruction, which applies equally to source and target domain examples, can be substantially more transferable than instance-specific gold in OPCD while maintaining in-domain performance.

---


### 102. [Kernel-Based Steering of CLIP with Vision-Language Model Preferences](https://arxiv.org/abs/2609.32203)

**<font color=#1a73e8>作者：</font>** Sajjad Ghiasvand, Haniyeh Ehsani Oskouie, Sina Mansouri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs) can judge visual similarity, but their judgments are not directly available as compact image embeddings for efficient comparison. We study how to transfer these preferences into CLIP while retaining its image--text capabilities. We introduce ASK, a kernel-based steering method that learns from elicited pairwise judgments without accessing teacher embeddings or collecting new human similarity annotations. ASK constructs positive semidefinite target kernels within small image groups and combines visual kernel matching with an image--text distributional anchor. Low-rank adapters jointly update the visual and text encoders while regularizing predictions toward frozen CLIP. After adaptation, retrieval uses CLIP image embeddings and cosine similarity, with no VLM calls. Experiments across five image domains, four CLIP backbones, and six judges evaluate teacher agreement, retrieval, and recognition retention. For ViT-B/16, mean retrieval mAP on classes excluded from adaptation increases from 53.8 to 75.0, compared with 71.7 for DINOv2 targets with KL anchoring. Mean zero-shot accuracy with jointly adapted encoders increases from 61.8\% to 62.4\%, averaged over 12 benchmarks and the five adaptation domains. Prompting provides an additional capability: selecting which visual distinctions the student learns. Human-annotated evaluations across four datasets support this criterion-specific control.

---


### 103. [Witness: Discovery, Deciphering, and Epiphany in Interactive Puzzle Environments](https://arxiv.org/abs/2609.32208)

**<font color=#1a73e8>作者：</font>** Guanghan Ning, Ping Liu, Linyi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated science needs agents that can work out the rules of an unfamiliar environment by interacting with it. Interactive rule-discovery puzzles offer a controlled setting for studying this ability: an agent infers hidden rules through experimentation and uses what it has inferred to reach a stated goal. We ask what limits current language models on these puzzles and whether reinforcement learning (RL) improves performance on rules held out from training. To study both, we introduce WITNESS, a 2D grid-based puzzle environment with ground-truth ASCII observations and controlled access to rules. An agentic pipeline generates games for WitnessGym, the RL training suite, and WitnessBench, comprising public validation and private test games. The validation set separately tests new compositions of trained rule primitives and primitives absent from training. Under a shared harness, the best of 18 frontier proprietary and open-weight models solves only 24\% of private test level slots, with scores sensitive to the observation interface and agent configuration. Providing ground-truth rules raises Opus-5's validation RHAE-L5 (relative human action efficiency over the first five levels) from 59.9 to 97.8, whereas a 27B open-weight model gains only 2.1 points and remains limited even with the rules provided. RL on WitnessGym raises the 27B model's private test RHAE-L5 from 2.1 to 5.4 and yields a mean gain of 4.1 points on four external discovery benchmarks. Together, these results point to rule acquisition as a major difficulty for frontier models like Opus-5 while smaller models further struggle on rule-based execution, and indicate that RL on hidden-rule puzzles transfers to broader rules and real-world tasks beyond training. Benchmark is available at: this https URL

---


### 104. [A bilingual AI audiologist built through rubric-guided playbook induction outperforms human audiologists in a blinded evaluation of simulated cases](https://arxiv.org/abs/2609.32220)

**<font color=#1a73e8>作者：</font>** Linkai Li, Changgeng Mo, Hanlin Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audiology consultation requires structured history-taking, audiometric interpretation and patient-centred communication, yet real-world case material is scarce. We present a bilingual AI audiologist pairing a general-purpose large language model with rubric-guided playbook induction, multimodal audiogram interpretation and retrieval-augmented grounding, without fine-tuning the language-model backbone. Using a 21-item rubric and an AI patient simulator, we induced a 19-rule consultation policy from 73 training cases (43 English, 30 Chinese) and evaluated the system on 58 independent simulated cases (30 Chinese, 28 English) in a pre-specified, source-blinded comparison with 17 practising audiologists. The AI audiologist outperformed human audiologists on every case (58/58; mean paired $\Delta$ = +1.35 on a 5-point composite, Cohen's d = 1.84, $P = 4.5 \times 10^{-20}$), on 20 of 21 rubric items and in both languages. Component ablation identified the playbook as the largest contributor, offering a practical route to specialist consultation agents in low-data medical domains.

---


### 105. [RAO-Nav: Probing Omni-Language Models for Zero-shot Semantic Audio-Visual Navigation](https://arxiv.org/abs/2609.32224)

**<font color=#1a73e8>作者：</font>** Qilang Ye, Meng Liu, Yu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We explore whether Omni-Language Models (OLMs) can be directly applied to zero-shot Semantic Audio-Visual Navigation (SAVN). Recent work demonstrates that even state-of-the-art specialized models still struggle to achieve generalist multimodal navigation, despite extensive task-specific training. In this paper, we introduce RAO-Nav, short for Reasoning All-in-One OLM, a deployment pipeline for zero-shot SAVN. By leveraging the rich implicit audio-visual knowledge encoded in OLMs, the embodied agent is enabled to ``hear'', ``see'', ``reason'', and ``act'' in the environment. To further elicit the built-in thinking ability of OLMs, we propose a test-time Latent Navigation Reasoning (LNR) module that can be seamlessly integrated into the decoding space. LNR encourages the model to retrieve more target-relevant observations and make effective navigation decisions. Through comprehensive experiments, we show that our framework surpasses existing state-of-the-art baselines on public SAVN benchmarks without using any training data. Moreover, we introduce a new \emph{Global Navigation Instruction} setting to further evaluate the ability of OLMs to serve as embodied navigation agents. Code: this https URL\_Nav.

---


### 106. [OptiArena: Can LLMs Improve Executable Algorithms under Fixed Resource Budgets?](https://arxiv.org/abs/2609.32227)

**<font color=#1a73e8>作者：</font>** Wenjun Peng, Xinyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Static QA and code-generation benchmarks only partially capture the role that large language models (LLMs) now play as coding agents and research tools. We introduce OptiArena, a budget-controlled testbed for studying whether LLMs can improve executable game-playing algorithms through five rounds of code edits within a fixed minimal scaffold and under bounded evaluator feedback and fixed resource budgets. The testbed uses two optimization regimes, surface obfuscation controls, calibrated references, held-out/stress splits, and diagnostics for degradation and exceptional failures, with LLM API cost reported separately from local evaluator wall-clock. The empirical study asks three questions: whether models can close the calibrated gap between a designated weak starter and an editable competent baseline, whether they can refine editable competent baselines without damaging them, and whether gains survive surface obfuscation controls. Across twelve frontier LLMs and five games, models improve designated weak starters more consistently than they refine editable competent baselines, with substantial variation across games and models. OptiArena provides a practical testbed for measuring bounded-resource algorithm optimization within the five-edit, fixed-scaffold setting studied here. Code is available at this https URL.

---


### 107. [CompassPlay: Rewarding the Proposer for Where It Moves the Solver](https://arxiv.org/abs/2609.32228)

**<font color=#1a73e8>作者：</font>** Sophia Xiao Pu, Ximeng Sun, Jiang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In self-play, a proposer generates verifiable tasks to train a solver. Proposer rewards often depend on the solver's success rate, but equally difficult tasks can differ in their training value. We introduce CompassPlay, a self-play method that rewards the proposer through gradient alignment. The reward favors tasks whose solver loss gradients align with those of reference tasks representing the target capabilities. It draws on a first-order approximation to learning progress and scores each eligible task without additional solver training. Our experiments show gains in performance and training efficiency. In coding self-play with Qwen2.5-Coder-7B, a small external reference set guides task generation. CompassPlay improves average accuracy over AZR's difficulty reward by 1.5 percentage points on in-domain coding and 2.7 on out-of-domain mathematics. In Lean4 theorem proving, CompassPlay matches the difficulty baseline's 150-iteration cumulative coverage with 40\% fewer GPU-hours.

---


### 108. [Solving Every Step Is Not Enough: Milestone Oracles Reveal a Composition Gap in LLM Math Reasoning](https://arxiv.org/abs/2609.32235)

**<font color=#1a73e8>作者：</font>** Zhuohan Wang, Haoran Ma, Tianyu Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can solve every intermediate step of a multi-step math problem on its own and still fail the full problem, even when given a roadmap of the steps and all of their answers. We introduce OracleLadder, a diagnostic evaluation that locates where LLM math reasoning fails by giving the model increasing levels of oracle help. For each problem, a teacher model writes a fixed roadmap of intermediate sub-goals (milestones), and a deterministic symbolic verifier grades every answer. Testing the model with no help, with the roadmap, with the roadmap plus the milestone answers, and on each milestone alone sorts each failure into one of five reasoning gaps. On 354 NuminaMath problems and six models from 8B to 671B parameters (Qwen3, gpt-oss, Llama 3.3, DeepSeek-V3.1), the largest gap for every model is the composition gap, a stricter form of the compositionality gap. It covers 33-48% of problems, and 24-37% after removing problems that an LLM review flags as grading errors. Accuracy and milestone-help recovery rank the two strongest models differently, and two RLVR runs with similar accuracy gains move problems differently. The roadmap effect replicates on MATH500 and AIME 2024/25, per-problem recovery agrees for 83-87% of problems under an independent second teacher, and the help ladder carries over to code generation. We release the data, roadmaps, prompts, and code at this https URL.

---


### 109. [Anytime-Valid LLM Leaderboards via Benchmark-weighted and Block-Factorized e-Processes](https://arxiv.org/abs/2609.32248)

**<font color=#1a73e8>作者：</font>** Hongfu Gao, Songxin Zhang, Zejian Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) leaderboards compare model capabilities by ranking models according to their mean performance on fixed benchmarks. However, variability in evaluation outcomes across runs may produce unsupported claims of model superiority on the benchmark, a risk compounded by leaderboard updates. In this paper, we propose BB-EDGE (Benchmark-Weighted and Block-Factorized e-processes for Directed Graph Evaluation), a principled framework that represents an LLM leaderboard as a directed graph whose edges certify pairwise mean-performance advantages, with anytime-valid family-wise error rate (FWER) control. Concretely, for each direction, BB-EDGE constructs an empirical-Bernstein e-process by factorizing evidence over protocol-defined blocks and assigning stakes proportional to the corresponding block weights, then applies direct e-Holm across these $e$-processes to certify directional advantages as edges. Theoretically, we characterize weight-proportional linear stakes under heterogeneous benchmark-average nulls and prove anytime FWER control under arbitrary within-block and cross-pair dependence. BB-EDGE further supports anytime-valid Top-$k$ certification and simultaneous rank intervals. Extensive experiments on synthetic data and four real-world benchmarks demonstrate that BB-EDGE maintains anytime FWER control while achieving high efficiency.

---


### 110. [Clarify the User or Verify the World? Uncertainty Routing for Proactive Agents](https://arxiv.org/abs/2609.32255)

**<font color=#1a73e8>作者：</font>** Zhaofeng Li, Xuan Zhang, Xiaokui Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents must decide not only whether additional information is needed, but also which source can resolve the uncertainty. Existing proactive approaches often specialize in either user clarification or environment verification, without explicitly determining the appropriate information source for each decision. We formulate this problem as uncertainty routing among ACT, CLARIFY, and VERIFY, and propose PROUR, a proactive uncertainty routing framework. PROUR decomposes action uncertainty into disagreement across plausible user-goal interpretations, which signals user-side ambiguity, and the entropy remaining within each interpretation, which signals missing world-side evidence. To acquire information from the routed source, a query generator is trained with a mode-conditioned information-gain reward, targeting user-goal identification under CLARIFY and next-action identification under VERIFY. On $\tau$-bench, PROUR achieves 28.17% average success rate across retail and airline, outperforming the strongest prior method by 4.57% while using 2.17 fewer interaction steps. The learned policy further generalizes to stronger task agents and transactional domains of $\tau^3$-bench without retraining, demonstrating the benefit of source-aligned uncertainty resolution for proactive agents.

---


### 111. [LAM: Efficient Lossy Agent Memory Framework With A Retrieval-Score Error Bound](https://arxiv.org/abs/2609.32256)

**<font color=#1a73e8>作者：</font>** Baixi Sun, Le Chen, Anjir Ahmed Chowdhury 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent memory grows as agents read inputs, reason, and call tools. Longer histories increase inference cost and eventually exceed the context window. LLM-based summarization reduces this history but adds latency and provides no explicit bound on information loss. We propose LAM, a Lossy Agent Memory system with three components: a deterministic deduplication rule with a substitution bound on retrieval scores - a bound on score perturbation, not a certificate of unchanged ranking; a memory manager that preserves the cached prefix and overlaps compaction with inference; and a performance model that estimates compaction costs before deployment. On 600 agent trajectories, LAM removes 22.47% of observation tokens while retaining 99.984% of the measured gold-patch evidence. At a fixed deletion set, the performance model predicts a 71.4x-91.6x end-to-end speedup from removing records before prefill instead of deleting them from a prefilled context. That benefit comes from the schedule rather than the rule and applies to any prefix-preserving test.

---


### 112. [Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs](https://arxiv.org/abs/2609.32259)

**<font color=#1a73e8>作者：</font>** Vincent-Daniel Yun, Woosang Lim, Haneul Yoo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent multi-agent LLM systems increasingly combine heterogeneous models for specialized agent roles. However, text-based communication requires each receiver to prefill shared context already processed by the sender. Reusing the sender's key-value (KV) cache avoids this redundancy, but prefill-free transfer across model families must handle differences in tokenization, model depth, and KV representations. To address these issues, we propose \textit{HeteroFold}, a prefill-free cross-family KV cache transfer method that keeps both the sender and receiver frozen. HeteroFold aligns model structures, maps the sender cache into the receiver space, and calibrates it to preserve receiver behavior. Across six transfer directions, HeteroFold achieves the best cache-transfer performance on all four long-context benchmarks and most short-context settings. It also matches text-based communication on the multi-agent benchmark. At 32K context length, Llama-3.1-8B$\rightarrow$Ministral-3-14B transfer is $10.7\times$ faster than Native Prefill and $1.18$--$1.47\times$ faster than the state-of-the-art prefill-free baselines, Dense Latent and KV Ridge. These results show that HeteroFold enables efficient cross-family KV reuse without receiver prefill.

---


### 113. [LANTERN: Illuminating Hidden Mathematical Knowledge in Language Models](https://arxiv.org/abs/2609.32264)

**<font color=#1a73e8>作者：</font>** Pavel Tikhonov, Elena Tutubalina, Ivan Oseledets 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can now prove theorems, but people still decide which problems to pursue. We ask whether a model's internal representations can help identify promising mathematical connections. We develop LANTERN, a fast, cost-efficient pipeline that uses a classifier over pretrained-model activations to rank candidate relations, followed by staged filtering, hypothesis generation, executable verification, and analytical checking. Applied to the On-Line Encyclopedia of Integer Sequences (OEIS), LANTERN ranked 50 million pairs among 10,000 frequently referenced sequences and produced 62 verified relations between pairs without an existing OEIS cross-reference. A content screen retained 13 relations worth presenting; nine of these are informative or insightful, including four which are entirely novel to the best of our knowledge: none appears in the OEIS or in our targeted literature search. The entire end-to-end process including classifier training, candidate ranking, filtering and verification took under 8 hours.

---


### 114. [When Can Old Evaluations Certify a New Model? Label-Efficient Release Decisions under Evaluator Drift](https://arxiv.org/abs/2609.32267)

**<font color=#1a73e8>作者：</font>** Joyanta Jyoti Mondal, Mridul Banik, Md. Shifatul Ahsan Apurba 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Releasing a model update requires certifying that its current-population risk stays below a threshold. Trusted labels are expensive, while a cheap evaluator, such as an LLM judge, scores every example. Reusing evaluator errors from earlier audits is tempting, but when may such evidence replace current labels? It depends on the status of history. If the errors can change invisibly, no label-free test detects the change, and every valid, useful certifier must keep buying labels at a rate we characterize; if a bound on the change is assumed, label-free certification is valid at an explicit error cost. For the middle ground, where history is informative but untrusted, we propose \emph{portfolio vigilance}, a sequential certifier mixing a betting expert guided by history with one that learns only from current labels; history affects only how it bets, so validity holds for any history. The contribution is not prior-informed betting or expert mixtures, but separating history that may enter validity from history that may only guide label collection. In a canonical model, accurate history shortens decisions but never raises the evidence growth rate; stale history can destroy it. On held-out CIFAR-10N and DICES-990 data, portfolio vigilance needs 0.465 (95\% CI $[0.327,0.575]$) and 0.740 ($[0.618,0.877]$) times the labels of a matched prediction-powered monitor, with no observed false certification, and fewer labels on all six external blocks. Under corrupted advice it stays within 8.0\% of its better component, while trusting history alone costs up to 1.66 times as much. In post-confirmatory repeated-judge experiments on DICES-990 and ToxicChat, changing a fixed LLM judge's rubric moves its scores beyond run-to-run variation; the portfolio then needs 0.790 ($[0.667,0.909]$) and 0.631 ($[0.520,0.770]$) times the labels of the matched monitor, and fewer than trusting history alone.

---


### 115. [Before Answering: Evidence Sufficiency under Size-Matched Memory Construction](https://arxiv.org/abs/2609.32269)

**<font color=#1a73e8>作者：</font>** Joyanta Jyoti Mondal, Md. Shifatul Ahsan Apurba, Mridul Banik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents that answer questions from compressed or retrieved memory must recognize when the evidence a query needs is no longer in memory. Benchmarks for this task usually create insufficient-evidence examples by deleting supporting passages. We show that this construction leaks the label through memory size: on MuSiQue, a classifier that only counts paragraphs reaches an area under the ROC curve (AUROC) of $0.979$ for detecting unsafe memory, higher than the lexical estimator we initially evaluated. We propose a size-matched construction that provably removes this shortcut, and use it to study MemSafe, an estimator that cross-encodes the query with each memory unit and aggregates the units with a set transformer. Across three multi-hop question answering datasets and five seeds, MemSafe reaches $0.968$ and $0.983$ AUROC on MuSiQue and HotpotQA, $0.26$ to $0.39$ above a lexical baseline, while the third dataset, 2WikiMultiHopQA, is saturated. A frozen pretrained cross-encoder with a logistic head already closes $41\%$ of the MuSiQue gap between the lexical baseline and MemSafe. At the same time, MemSafe degrades more than a weak baseline on the unanswerable questions released with MuSiQue, reaches only $0.639$ AUROC on SQuAD~2.0, and needs several thousand clinical training examples before it outperforms a feature-based estimator. Used as a gate for a 7B reader, it reduces the error rate on answered questions from $0.850$ to $0.631$ at $5\%$ coverage, outperforming both reader confidence and, on average, the ground-truth integrity label, although a 7B LLM judge is the better gate at $10\%$ coverage. These results indicate that the way insufficient evidence is constructed matters as much as the estimator that detects it.

---


### 116. [HeroFrame-Bench: Reference-Anchored Evaluation via Rubric--Ranking Co-Evolution for Movie Hero Frame Selection](https://arxiv.org/abs/2609.32280)

**<font color=#1a73e8>作者：</font>** Weitai Kang, Hanieh Deilamsalehy, Yumo Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hero frames are in-film stills used as source imagery for theatrical posters, streaming cover art, film database listings, and other promotional placements. As the first visual entry point, they shape audiences' initial impressions of the movie and their subsequent willingness to watch it. Selecting these frames, a task we term hero frame selection, requires balancing content relevance with aesthetic appeal. A related task is keyframe selection, yet its benchmarks prioritize relevance over aesthetics, using either finite annotations that exclude valid alternatives or VideoQA that entangles selection quality with downstream model capability. We therefore introduce HeroFrame-Bench, built through a scalable VLM-as-a-Judge framework. We construct multimodal contexts from diverse metadata to ground a VLM judge that scores selected frames using our Reference-anchored Percentile. The percentile is obtained by inserting each frame into reusable, pre-ranked reference chains, enabling direct, extensible, and reliable evaluation. To reduce ambiguity and improve consistency in these subjective judgements, we further propose Rubric-Ranking Co-Evolution, which generates movie-specific rubrics to condition the VLM judge and refines rubrics jointly with the resulting rankings. Within this process, we introduce several verifiable signals, most notably the Inverted Rubric Attack, to select robust rubrics. Finally, HeroFrame-Bench is instantiated over 204 movies with 2,031 reference chains and 1,970 learned rubrics. We build an annotation interface for human-alignment studies which show that our construction design improves VLM agreement with human from 77.56% to 83.78%. Evaluation on multiple methods show that hero frame selection remains challenging.

---


### 117. [TRAP: Understanding and Mitigating Privacy Memorization in Language Models](https://arxiv.org/abs/2609.32293)

**<font color=#1a73e8>作者：</font>** Muhammed Ustaomeroglu, Ziyue Xu, Hanshen Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a language model on sensitive records can leave it able to reproduce them. We ask when this memorization arises and how to prevent it without knowing in advance which spans are sensitive. Our starting point is that most memorization scores and attacks share one statistical core: whether the model assigns a token more probability than some reference would. Taking as the reference a model trained on the complementary half of the same corpus gives the Target Reference Advantage (TRA), a per-token signal that separates what a model fit to a particular record from what it learned across records, and is cheap and differentiable. We then study what drives memorization during fine-tuning: it keeps growing well past the validation minimum, is larger on small datasets and at higher learning rates, and higher when the underlying task is harder. Early stopping removes much of it, but because it is chosen by aggregate validation loss it helps least for rare, hard-to-predict spans embedded in otherwise learnable text, which is exactly what sensitive information tends to be. We therefore introduce TRAP, a one-sided penalty on tokenwise TRA that acts only where the target model pulls ahead of its reference. On student essays with annotated personal information and clinical cases with patient identifiers, TRAP brings memorization near the level of an untrained model at little utility cost, where generic regularizers barely move and differential privacy gives up most of what fine-tuning bought.

---


### 118. [GLIDE: Generalized Layer-wise Intrinsic Distributional Evaluation for Heterogeneous LLM Agents](https://arxiv.org/abs/2609.32295)

**<font color=#1a73e8>作者：</font>** Wei Zhu, Yiming Wang, Rui Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents require reliable step-level evaluation to compare candidate branches and allocate computation effectively. However, lightweight evaluation remains challenging. External verifiers introduce additional inference cost, while agent-produced confidence or self-evaluation scores can be miscalibrated, especially when candidates are generated by heterogeneous agents. We propose \textbf{G}eneralized \textbf{L}ayer-wise \textbf{I}ntrinsic \textbf{D}istributional \textbf{E}valuation (\textbf{GLIDE}) for LLM agents. \textsc{GLIDE} derives intrinsic step evidence from layer-wise residual coherence, which measures whether local residual updates consistently support the global residual change induced by a candidate step. It calibrates this evidence against the recent score distribution of the generating agent and converts it into a pessimistic reward that jointly accounts for absolute residual evidence and agent-relative standing. The reward provides a cross-agent value signal for MCTS branch selection, while normalized predictive uncertainty guides adaptive branching. Experiments on multi-hop reasoning, sequential decision making, and symbolic logic show that \textsc{GLIDE} improves task performance, step-level ranking quality, and computational efficiency without external verifiers or task-specific supervision.

---


### 119. [On the Capability and Limitation of Hard Prompt](https://arxiv.org/abs/2609.32302)

**<font color=#1a73e8>作者：</font>** Lijia Yu, Shuaitong Liu, Gaojie Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prompt engineering has become an indispensable tool for using large language models (LLMs), turning LLMs into task-specific experts without changing their weights. Despite notable theoretical advances in prompt engineering, the theory for the more practical hard or discrete prompts is largely open. In this paper, we try to fill this gap either by providing a complete solution or by making substantial progress on the three core theoretical questions regarding hard prompts. First, we show that determining the existence of a hard prompt for a transformer to solve a downstream task is NP-complete and that finding an optimal hard prompt is NP-hard, which is the first computational complexity result for hard prompting, as far as we know. Second, we show that, unlike soft or continuous prompts, hard prompts have essential limitations: hard prompts are not complete; short hard prompts do not significantly enhance the ability of transformers; and long hard prompts exhibit the "prompt dominating answer phenomenon," meaning that, with high probability, the same answer is given for all queries of the same length. On the other hand, linear hard prompts do not have the limitations of short or long prompts. Third, we provide a tight bound on the size of the task in terms of the prompt length for the performance of prompts on the finite task to generalize to the entire data distribution, leading to a necessary and sufficient condition for generalizability. This is the first result on generalization for prompting, as far as we know. Our findings not only offer the first theoretical insights into hard prompts but also provide provably reliable practical guidance for real-world LLM usage.

---


### 120. [Train4Merge: A Controlled Single-Teacher Study of RL vs. SFT Teachers for OPD-Based Model Merging](https://arxiv.org/abs/2609.32303)

**<font color=#1a73e8>作者：</font>** Jingyuan Huang, Zuming Huang, Yucheng Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Domain experts trained from a shared checkpoint can be merged into one model through on-policy distillation (OPD), where they act as teachers supervising a student on its own trajectories. One upstream choice is rarely examined: whether to build each expert with supervised fine-tuning (SFT) or reinforcement learning (RL). Yet equally strong teachers need not be equally good teachers. We probe this choice through controlled single-teacher OPD, a building block of multi-teacher OPD: in Agentic, Reasoning, and Perception, comparably performing SFT and RL teachers are trained from Qwen3.5-9B, each guiding a student initialized from it. At their best checkpoints, RL-guided students outperform SFT-guided students by 4.27, 1.50, and 0.86 percentage points in Agentic, Reasoning, and Perception, respectively, and recover more of their teachers' performance gains over the base model. The contrast is clearest in Agentic, where the best SFT-guided student recovers only 44.44% of its teacher's gain, whereas the best RL-guided student recovers 115.00%, surpassing its teacher. Our analysis points to an explanation: RL teachers stay much closer to the shared initialization in parameter space than SFT teachers and are therefore easier for their students to follow.

---


### 121. [Delayed Supervision for Test-Time Language Models](https://arxiv.org/abs/2609.32312)

**<font color=#1a73e8>作者：</font>** Jinha Kim, Taksh Kothari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time language models adapt a compact memory while processing the input sequence. This
perspective encompasses nonlinear fast-weight learning in LaCT, associative delta-rule
updates in DeltaNet, and generalized delta-rule state updates in RWKV-7. Training these
models to predict the next token does not explicitly require a fact to remain accessible
after many subsequent memory updates. We study delayed supervision for this test-time memory:
during post-training, ask a simulator-grounded question only after a long interval of
unrelated events, and supervise its answer alongside ordinary next-token prediction.
Questions are evaluated on disposable branches, so their answers never enter the continuing
event stream. The construction distinguishes retention from revision: a retained fact must
remain valid throughout the delay, whereas a revised fact must be answered with its latest
value. We evaluate this approach on LaCT-760M and plain DeltaNet-1.3B using TextWorld
training trajectories and shared BABILong and RULER evaluation panels, and include a
separately reported RWKV-7 comparison. Relative to event-only training, delayed QA improves
BABILong by 5.48 percentage points for LaCT and 1.32 points for DeltaNet, and single-needle
RULER by 1.45 and 3.27 points, respectively. The RWKV-7 comparison reports gains of 4.60 and
7.00 points on its own panels. These results support delayed semantic supervision as a
practical outer training objective for usable test-time memory, while leaving open how much
of the benefit derives specifically from delay rather than general question-answering and
answer-termination supervision.

---


### 122. [What Can a Leaderboard Certify? Compositional Controllability for Fair Evaluation and Training of Biomedical Literature-Review Agents](https://arxiv.org/abs/2609.32318)

**<font color=#1a73e8>作者：</font>** Zhaowei Han, Xiang Zhang, Lingxiao Guan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leaderboards rank long-horizon agents by their final outputs. Yet a higher score alone does not establish whether two systems are comparable or which stage accounts for the difference. Unequal evidence, inputs, or budgets can affect scores, and statistical corrections do not remove this mismatch. We introduce compositional controllability to address these questions. A comparison window covers one stage, several stages, or the whole agent. Our central result bounds the gap between observed and controlled score differences using only nuisance outside the window. This yields an admissibility test applied before scores are inspected. Inadmissible comparisons are refused. For admissible pairs, an ordering is certified only when the score gap exceeds the combined sampling and nuisance radii; otherwise, it remains undecided. These decisions give each system a rank interval. We introduce BioLitBench, a benchmark of 2,042 biomedical articles represented as structured claim graphs. Among seven published pipelines, a conventional statistical analysis declares a winner in 14 of 21 pairwise comparisons. Yet the top-ranked system alone received the target review's bibliography. To isolate pipeline performance, our test requires matched inputs and a fixed backbone model. It refuses 11 of the 21 comparisons, including every comparison involving the top-ranked system. Seven of the 14 conventional conclusions fall within these refused pairs. The same comparison windows support stage-level training. We train SCRIBE on Qwen3.8-27B using rewards measured at each stage's exit. Under matched evidence, SCRIBE achieves a certified rank interval of [1,2], with certified advantages over all evaluated published pipelines and the evaluated Claude and OpenAI agents. Under same pool, SCRIBE matches the strongest published retriever and is certified above three published pipelines.

---


### 123. [HyperReCo: Retrieving and Connecting Evidence with Hypergraph Neural Networks for LLM Multi-hop Reasoning](https://arxiv.org/abs/2609.32327)

**<font color=#1a73e8>作者：</font>** Zicheng Zhao, Linhao Luo, Junnan Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong capabilities, with retrieval-augmented generation (RAG) supporting complex multi-hop reasoning by retrieving evidence distributed across documents. Graph-based approaches exploit connections among evidence, and hypergraph-based retrieval further preserves higher-order entity associations within documents and connects documents through shared entities. However, existing hypergraph retrievers often rely on predefined structural expansion or diffusion, which may miss query-dependent interactions needed to identify relevant evidence. They also leave connections among retrieved evidence implicit, requiring LLMs to reconstruct these connections before reasoning. Therefore, we propose HyperReCo, a framework for retrieving and connecting evidence with a hypergraph neural network (HyperGNN). We represent each document as a hyperedge over its extracted entities, with shared entities connecting the hyperedges. Through hypergraph message passing with joint supervision over documents and entities, the HyperGNN learns query-dependent interactions to retrieve complementary evidence. We further introduce Gradient-Guided Hyper-Path Decoding (GGHD), which uses gradient attribution to interpret the learned interactions and translate them into explicit hyper-paths that help LLMs combine complementary facts for multi-hop reasoning. Experiments on six benchmarks show that HyperReCo achieves the best retrieval performance among the compared methods on all three multi-hop QA datasets, together with strong downstream QA performance. Case studies and further analyses demonstrate the utility of decoded hyper-paths for connecting retrieved evidence.

---


### 124. [Language Distances are Practical for Equitable Cross-Lingual Transfer](https://arxiv.org/abs/2609.32331)

**<font color=#1a73e8>作者：</font>** York Hay Ng, Razan Ahsan Rifandi, Aditya Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual transfer is strongly conditional on how the source language is chosen, but it is impractical to determine the best candidate source for every target language, especially for low-resource target languages. Language distances are widely used to rank candidate sources due to their correlation with transfer efficacy and applicability in resource-sparse settings. However, the reliability of distance-based rankers across tasks and resource levels remains underexplored. We therefore present the first equity-focused evaluation of paradigms for ranking source languages, studying resource-level inequality and task inequality across ten cross-lingual tasks and two multilingual models. While both inequalities are most pronounced for individual language distances and an English-always baseline, they are substantially reduced by training-free composite distances, and nearly eliminated by trained rankers. We further demonstrate the reliability of rankers using language distances compared to rankers using language model internals. Overall, we find that language distances provide a practical basis for equitable and performant transfer language selection. We recommend using trained rankers when task-specific transfer evaluations are available, and composite distances otherwise.

---


### 125. [Progressive-View On-Policy Distillation for Regional-to-Global Transfer in Multimodal LLMs](https://arxiv.org/abs/2609.32333)

**<font color=#1a73e8>作者：</font>** Shanfeng Huang, Zhou Fang, Song Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Regional-to-global distillation uses crop-conditioned guidance to improve full-image understanding. The challenge is to effectively transfer the teacher's crop-based advantage to the student's full-image inference. We propose progressive-view on-policy distillation (PVD), which shifts the student's view distribution from the crop toward the full image through an intermediate aspect-preserving padded crop. The padded crop preserves regional content while matching the full image's visual-token grid. Across stages, the view mixture assigns increasing probability to the full image. A lightweight regional-advantage weighting reallocates token-level supervision using the crop-conditioned teacher-student log-probability gap. Evaluated under each sampled input, it applies mild reweighting when the gap is small and emphasizes higher-gap tokens when the gap widens. A Jensen-Shannon metric decomposition interprets this schedule as a shift from matched-input imitation toward the deployment objective. Across benchmarks spanning perception, visual mathematics and general multimodal question answering, PVD-full reaches an average accuracy of 77.51 over three seeds, improving on the reward-free distillation baseline by 2.01 points and on its reward-matched variant by 1.00 point. In the reward-free setting, PVD-distill still gains 1.16 points.

---


### 126. [Enabling Timely Guidance before Skill Retrieval: Retaining Helpful Warm Tips in Agent Context](https://arxiv.org/abs/2609.32339)

**<font color=#1a73e8>作者：</font>** Feng Liang, Yupeng Li, Runhao Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reusable skills help LLM-based agents solve complex tasks, but the agent must receive guidance before it commits to an ineffective approach. Existing skill mechanisms often expose only metadata and load full content on demand, leaving useful guidance unavailable until the agent decides to retrieve it. General memory methods can incur substantial maintenance overhead, while keeping guidance in conversation context risks repeatedly exposing the agent to irrelevant or harmful advice. We propose TipsWarm, a mechanism that complements existing skill mechanisms by maintaining a budgeted pool of skill-derived keypoints, or \textit{warm tips}, for selective injection into the context of every message turn. By separating event-triggered LLM assessment from inexpensive per-turn screening, it makes transferable skill guidance readily available while controlling maintenance costs. In three coding and iterative task-execution benchmarks, TipsWarm achieves the highest task success rate while remaining time-efficient, compared to recent skill and general memory baselines.

---


### 127. [SGA-Flow-GRPO: Spatial Gradient-Guided Credit Assignment for Flow-GRPO](https://arxiv.org/abs/2609.32340)

**<font color=#1a73e8>作者：</font>** Yunkai Yang, Yudong Zhang, Xinying Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has proven effective in aligning flow-based generative models with human preferences. Recently, Flow-GRPO has emerged as an efficient critic-free paradigm by calculating advantages over sampled candidate trajectories. However, standard Flow-GRPO applies a uniform scalar advantage across both temporal denoising steps and spatial latent dimensions, without explicitly accounting for the spatial structure of generated images, which may lead to sub-optimal policy updates. To address this, we propose a novel gradient-guided spatial credit assignment framework tailored for Diffusion Transformers (DiTs). We first reformulate the transition-level log-likelihood in Flow-GRPO into a token-wise representation natively aligned with DiT patch architectures, constructing spatially fine-grained importance sampling ratios. To allocate localized credit without rigid, boundary-sensitive segmentation heuristics, we introduce a continuous spatial credit map derived from reward gradients. Crucially, we employ an outlier-robust normalization scheme based on Median Absolute Deviation (MAD) coupled with temperature scaling, effectively eliminating gradient noise while highlighting functional prompt-aligned regions. Extensive evaluations on GenEval show that our approach delivers SOTA alignment quality, achieving a convergence rate comparable to top-tier methods like DiffusionNFT while substantially improving upon Flow-GRPO-based methods in alignment performance.

---


### 128. [A Comparative Analysis of Attention versus State-Space Models for In-Context Learning](https://arxiv.org/abs/2609.32341)

**<font color=#1a73e8>作者：</font>** Enes Arda, Semih Cayci, Atilla Eryilmaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers and state-space models (SSMs) are two prominent sequential learning architectures, yet their comparison remains largely empirical and existing theoretical analyses are typically task-specific or architecturally restricted. In this paper, we develop belief geometry, a unified analytical framework for comparing the representational capabilities of broad classes of attention and SSMs. Starting from a generalized formulation of in-context linear regression and using cumulative Bayes regret as our measure, we abstract three capabilities required by many sequential learning problems in our belief geometry: evidence assembly, belief maintenance, and addressing. We then study three cases of our formulation that isolate these capabilities and yield sharp architectural lessons: For belief maintenance, SSMs attain the optimal regret over stationary aggregation kernels; for positional assembly, SSMs have a memory advantage; and for content addressing, softmax attention has an exponential width advantage over sigmoid-selective SSMs. Experiments with LLaMA-type Transformers and Mamba-2 show that these architectural insights extend beyond our analytically tractable classes and linear-regression testbed.

---


### 129. [ALLOT: Budgeted Hybrid-Memory Routing for Knowledge Updates in LLMs](https://arxiv.org/abs/2609.32344)

**<font color=#1a73e8>作者：</font>** Shanfeng Huang, Zhou Fang, Song Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For large language models (LLMs), parametric adaptation is costly when retrieval already suffices. We introduce ALLOT, a hybrid-memory routing framework that separates learned write priority from a hard parametric budget. A memory-aware router combines frozen text representations, retrieval confidence, and relation metadata; a single ranking supports multiple write budgets while preserving all facts in external memory. On CounterFact with Qwen3-4B, ALLOT reaches 0.760 accuracy at a 20% parametric-write budget and recovers 78.4% of the budget-matched oracle gain, with 80% fewer parametric writes than dual-writing every fact. At this budget, jointly adding retrieval and relation features to text improves normalized oracle gain by 6.2 percentage points. Complementary Qwen3-0.6B shared-store results achieve dual-write-level accuracy with 6-14.5% parametric writes, and cross-benchmark transfer retains approximately 88% of in-domain gain. These results support allocating adaptation capacity according to its incremental value rather than treating every factual update as an equally valuable training target.

---


### 130. [From Trajectories to Grounded Preferences: Process Preference Synthesis via Interaction Element Graphs for Web PRMs](https://arxiv.org/abs/2609.32351)

**<font color=#1a73e8>作者：</font>** Yangzhe Peng, Xiaoyang Wang, Yiyang Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comparative Process Reward Models (PRMs) provide critical step-level guidance for autonomous web agents by evaluating state-conditioned preferences between candidate actions. However, existing preference training data synthesized via multi-policy sampling suffers from a severe scarcity of Grounded Minimal Contrastive Pairs (GMCPs)-where competing candidates target genuine on-page elements with identical action types. In representative baselines preference data (namely, WebArbiter), GMCPs account for merely 24.19%, biasing PRMs during training to rely on shallow shortcuts (such as element hallucinations and action type mismatches) rather than acquiring genuine contextual decision semantics. To address these challenges, we propose SURFPRM, a graph-guided process preference synthesis framework for comparative Web PRMs. SURFPRM structures web demonstrations into a persistent Interaction Element Graph that acts as an environment-grounded negative action proposal mechanism, systematically synthesizing contrastive negative actions across spatial, temporal, and spatiotemporal confusion axes. This elevates the GMCP proportion from 24.19% to 74.60%, producing the curated SURFPRM-DATA dataset. Across six open-source backbones (3B to 9B parameters), PRMs trained on SURFPRM-DATA outperform baseline-trained models on average on WEBPRMBENCH and rival leading proprietary LLMs. In downstream reward-guided trajectory search on WEBARENA-LITE, SURFPRM provides step-level guidance for both GPT-4o (+14.21%) and GPT-4o-mini (+12.83%) policies, yielding substantial improvements in complex web task success rates.

---


### 131. [EyeVQA: Benchmarking Ophthalmic Vision-Language Models from Recognition to Spatial Grounding](https://arxiv.org/abs/2609.32352)

**<font color=#1a73e8>作者：</font>** Gujie Shao, Zixun Xie, Xuechun Xing 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown increasing potential for medical image understanding, yet their capabilities in ophthalmic imaging remain insufficiently characterized. Existing ophthalmic datasets are typically designed for individual diseases or specialized tasks, making it difficult to systematically evaluate whether VLMs can move beyond disease recognition toward comparative reasoning and fine-grained spatial grounding. We introduce EyeVQA, a unified visual question answering benchmark for comprehensive evaluation of ophthalmic VLMs. EyeVQA is constructed from 21 available ophthalmic datasets and contains 20,000 question-answer pairs spanning six disease groups and seven question types: Single-Choice, Multi-Select, Variable-Select, True-False, Ranking, Point Location, and Bounding Box. Gold answers are deterministically derived from source-provided diagnoses, severity grades, clinical findings, segmentation masks, bounding boxes, and anatomical landmarks, enabling reproducible evaluation without relying on model-generated annotations. Notably, 44.5% of the questions require reasoning across multiple images, extending evaluation beyond conventional single-image medical VQA. We benchmark fourteen representative general-purpose, scientific, and medically specialized VLMs under a unified zero-shot protocol. The best-performing model only achieves an overall score of 62.8, while substantial gaps remain in spatial grounding and cross-task generalization. These results highlight the limitations of current VLMs in comprehensive ophthalmic visual understanding and establish EyeVQA as a diagnostic benchmark for developing more reliable and spatially grounded ophthalmic multimodal models. The project page is available at this https URL.

---


### 132. [Fewer Tokens, More Self-Teaching: On-Policy Self-Distillation for Extreme Visual Token Reduction](https://arxiv.org/abs/2609.32353)

**<font color=#1a73e8>作者：</font>** Junxian Li, Ruixuan Yang, Tianao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token reduction is an effective way to accelerate multimodal large language models (MLLMs), but performance deteriorates rapidly under extremely low token budgets. Existing work has explored both visual-token selection and training-based adaptation to reduced visual inputs. We take a step further by asking how a heavily compressed MLLM should learn from the states induced by its own generations. This setting naturally calls for on-policy self-distillation: a heavily compressed model is supervised on the states induced by its own generations, while its full-token counterpart serves as an information-rich teacher. Based on this insight, we propose LT-OPD, a training framework for extreme visual-token reduction. The student rolls out responses with only a small fraction of visual tokens, and a frozen full-token copy of the same MLLM provides distributional supervision along these student-generated trajectories. To stabilize on-policy learning when visual evidence is severely limited, we further introduce a budget-level curriculum that progressively decreases the token budget during training. Across nine benchmarks on Qwen3.5-4B, LT-OPD raises average retained performance under 5% visual-token retention from 68.6% to 82.3%, outperforming training-free, training-based, and reinforcement-learning baselines at the same budget. The gains transfer consistently to Qwen3.5-9B, GLM-4.6V-9B, and LLaVA-OV-1.5-4B. LT-OPD also reduces KV-cache usage by 85.2% and prefill FLOPs by 85.4% without additional inference overhead, demonstrating that on-policy learning can substantially recover capabilities lost to extreme visual-token reduction.

---


### 133. [Gradients for Interventions and Activations for Detection: Targeted Feature Learning in Language Models](https://arxiv.org/abs/2609.32355)

**<font color=#1a73e8>作者：</font>** Jonathan Drechsel, Steffen Herbold  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model-internal features can be studied through both their ability to identify a specified concept and their causal effect when manipulated, e.g., through steering or weight editing. A prominent approach to feature learning is Sparse Autoencoders (SAEs), which learn broad feature dictionaries whose relation to particular concepts is typically identified post hoc. However, many interpretability questions are instead hypothesis-driven and concern a concept specified in advance. We study this setting as targeted feature learning, where a single feature is constructed for such a predefined concept. We present a controlled comparison across three model signals (activation values, activation gradients, and parameter gradients) and two estimators (contrastive mean and a learned one-dimensional encoder-decoder), yielding six targeted methods, with CAA and GRADIEND as existing instances and four new methods covering the remaining combinations. We compare these methods against pretrained SAEs across 15 tasks and three language models, evaluating both detection and causal intervention. Across models, the strongest detection performance is achieved by contrastive activation value methods, whereas the strongest intervention performance is achieved by gradient-based methods. Overall, our results show that targeted feature quality depends jointly on the model signal and estimator, with detection and intervention capturing complementary properties.

---


### 134. [Graph Memory: Spectral Associative Memory via Dirichlet Energy](https://arxiv.org/abs/2609.32365)

**<font color=#1a73e8>作者：</font>** Zhaoyang Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dense associative memories have traditionally focused on storing and retrieving vector-valued patterns. Many modern machine learning problems, however, are naturally graph-structured, requiring memory mechanisms for relational patterns, graph diffusion geometries, community structures, and graph-based inductive biases. We propose a spectral dense associative memory for storage and retrieval of graph data, extending the classical vector-valued memories. Retrieval is performed through a log-sum-exp energy induced by Dirichlet energy with spectral norm distances, producing a softmax-weighted average of the stored Laplacians that remains a valid graph Laplacian. We prove exponential storage capacity and exponentially decaying retrieval error. Beyond graph retrieval, we establish theoretical guarantees for spectral quantities central to graph learning, including eigenvalues, eigenspaces, and diffusion operators. Experiments on synthetic graph data, real-world airline network, protein conformation data and wearable sensor data demonstrate robust graph retrieval while preserving the graph geometry of the data. Our framework provides a new associative memory paradigm for graph-structured data and bridges dense associative memory with modern graph learning and generative AI.

---


### 135. [AuthorityLens: Rethinking LLM-Based Agent Systems Through the Lens of Authority](https://arxiv.org/abs/2609.32378)

**<font color=#1a73e8>作者：</font>** Shaojin Chen, Huihao Jing, Wun Yu Chan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly deployed with authority over consequential resources and decisions in real systems. These agents often operate alongside human and LLM-based participants who hold different forms of authority. Yet workflow roles, permission settings, and review mechanisms do not necessarily reflect the authority realized in practice. We introduce AuthorityLens, a framework for measuring a system's authority structure. Starting from an authority portfolio, we evaluate a system along three dimensions: what the system is authorized to do (System Authority), how much joint participation is required to exercise that authority (Authority Separation), and how much authority each participant holds (Principal Authority). We derive these measurements from the minimal combinations of participants sufficient to realize each outcome across admissible runtime states. We apply AuthorityLens to Codex, OpenCode, and Gemini CLI across 13 operating configurations over a common portfolio of agent operations. We find that nominal configurations do not map cleanly onto realized authority. In Codex, Full Access changes System Authority only marginally while substantially concentrating authority in the executing Assistant. OpenCode's Build and Plan configurations have the same System Authority and Authority Separation despite different workflows and root-level permissions. In Gemini CLI, model-based review increases Authority Separation without changing System Authority. Principal Authority further distinguishes authority replication from authority separation: spawned or delegated agents can become alternative holders of the same authority without increasing the required joint participation. Together, these results demonstrate that AuthorityLens provides a unified framework for measuring and comparing realized authority structures across agent systems.

---


### 136. [Measurement Boundaries in LLM Financial Agent Evaluation: Fixed-Tape Execution and Multi-Defect Auditing](https://arxiv.org/abs/2609.32379)

**<font color=#1a73e8>作者：</font>** Weicheng Xue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What controls are needed to interpret execution performance and audit scores in LLM agent evaluations? We study two limits on these interpretations in a financial agent harness. In Study~A, comparing independent runs under idealized and stressed execution on three synthetic settings that share one 24-day upward phase mixes the execution rule with fresh model responses and portfolio feedback: the parsed decision paths agree in only $19.8\%$ of $450$ pairs. Replaying each stored response tape through both execution destinations gives a narrower result. Conditional on those responses, stressed execution changes total return by $-0.0170$ (95\% interval $[-0.0230,-0.0117]$), or $10.4\%$ of the idealized baseline, and ten seed clusters do not resolve the model ranking. Study~B corrects an incomplete answer key and replaces legacy tasks with matched zero-, one-, and two-defect tasks under an explicit multi-label prompt. The drop in target violation recall from one to two defects is positive in five of six combinations of auditor and source (median $0.267$), with three surviving Holm correction. Yet the auditor that includes both target labels most often has micro-precision $0.149$, emits findings on $98/100$ zero-defect tasks, and returns the exact dual-defect set in only $21/100$ cases. Target recall by itself therefore gives a poor account of audit quality on this construction. The studies address different limits: what an execution comparison estimates, and what target recall captures. Together, they show how fixed conditions and diagnostic controls bound the claims a score can support.

---


### 137. [Attribution Without a Second Pass: Inline Per-Sample Gradient Provenance at ~1% Overhead](https://arxiv.org/abs/2609.32380)

**<font color=#1a73e8>作者：</font>** Amit Nautiyal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data attribution methods used in practice (TRAK, LoGRA, EK-FAC) are post-hoc: after training they make a second pass over the training set to recompute per-sample gradients, repeated per checkpoint when ensembled. Traceprop avoids that pass by recording projected per-sample gradients inline on the training backward pass. A Kronecker-factored sketch scales from a single tracked layer to every layer without materializing a dense projection matrix. On LoRA fine-tunes of GPT-2 and Pythia models up to 2.8B on one NVIDIA L4, inline logging costs 0.30-1.08% of wall-clock time at last-block scope and stays under 1% (0.79%) even when tracking every layer of Pythia-1B. Against LogIX, the closest inline-capable competitor, the factored sketch is 2.0-4.1x cheaper at equal storage, a gap that grows with tracked scope and is significant at every scope tested, while matching or exceeding LogIX's attribution quality at matched storage. Building the attribution-ready store inline is 60-242x cheaper than one post-hoc pass and 301-1211x cheaper than a five-checkpoint TRAK ensemble, with recorded gradients matching autograd exactly. Because each stored gradient carries source-file lineage, the same pass also produces EU AI Act Article 26 audit trails.

---


### 138. [PlurVA-LLM-2026 Shared Task Track-1: Pluralistic Value Alignment in LLMs via Multilingual Fine-Tuning and Threshold Calibration](https://arxiv.org/abs/2609.32382)

**<font color=#1a73e8>作者：</font>** Vihindi Kotalawala, Nevidu Jayatilleke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our system for the PlurVA-LLM 2026 Shared Task Track-1, which focuses on pluralistic value alignment in the contexts of China, Indonesia, and Sri Lanka. For this resource-constrained track, we fine-tuned Llama 3.1 8B Instruct using 4-bit QLoRA. Our approach combines option-permutation augmentation for Chinese data, annotator vote expansion for Indonesian data, and binary reformulation with SinhalaMMLU augmentation for Sri Lankan data. We further applied conditional threshold calibration to the predictions for the Sri Lankan data. The final system achieved accuracies of 0.785 for Chinese, 0.715 for Indonesian, and 0.916 for Sri Lankan, resulting in an overall macro-average accuracy of 0.805.

---


### 139. [RefCompose: Multi-Reference Image Generation via LoRA-Conditioned Diffusion](https://arxiv.org/abs/2609.32389)

**<font color=#1a73e8>作者：</font>** Sai Sri Teja Kuppa, Parth Shinde, Priyadharsan Balaji S 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Filmmakers and visual artists routinely need to compose multiple references, actors, locations, props, cultural elements, into a single coherent shot, but existing tools either fail to scale past a handful of references or destroy fine grained subject identity in the process, since per reference tokenization scales memory linearly with reference count $N$ and generated content often departs from the given references rather than reproducing them. We propose \textbf{RefCompose}, a pixel space compositional conditioning framework that decouples \emph{where} things go from \emph{what} they look like, via a single fixed resolution reference canvas that keeps conditioning size constant regardless of reference count. Spatial layout is induced at inference time from a frozen diffusion transformer and extracted via Grounding DINO, requiring no LLM or dedicated layout model, while dual stream LoRA adapters inject a layout derived depth map and the encoded canvas through separate low rank streams, disentangling geometric scaffolding from localized appearance. On the Dense Layout protocol, RefCompose consistently outperforms layout based and state of the art multi reference baselines on color, texture, shape, spatial accuracy, and identity/content preservation at higher reference counts, all with constant inference memory, making it a practical building block for multi subject cinematic composition at production scale.

---


### 140. [SCLATE: a Substrate for Continual-Learning Agent Training and Evaluation](https://arxiv.org/abs/2609.32391)

**<font color=#1a73e8>作者：</font>** Youngmok Jung, Sirajul Salekin, Henry Tran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continual-learning agents are systems of models, harnesses, and memory operating over long multi-session horizons. Evaluating and training them requires interleaving tasks with agent-side events such as session stop and start, crons, and memory consolidation. Yet existing benchmarks and training frameworks schedule only the benchmark's own events, leaving each benchmark and agent pair to build a custom scheduling loop. We present SCLATE, an execution substrate where benchmarks and unmodified agents each add their events to one open event scheduler through an adapter. A hybrid simulated clock runs these events on a shared timeline, flowing in real time while the agent works and skipping idle gaps, which compresses a month-long scenario into hours. SCLATE also serves as a rollout engine that runs any agent's harness and memory unmodified, recording the tokens and log probabilities of every model call through an in-container proxy. We port seven benchmarks to SCLATE and compare ten unmodified harness and memory configurations head to head on ten models. The comparison shows that an added memory system does not reliably beat the harness's native memory and that models differ widely in how they use the same harness and memory. We then post-train Qwen3.5-4B through unmodified harnesses and memory systems. The model learns to use both, reading 6.8x fewer file lines with a 16.7-point higher SWE-bench Verified pass rate, and writing richer memory records, while its held-out MetaClaw accuracy rises by up to 11.8 points.

---


### 141. [Beyond Scripted Search: Sample-Efficient Reward Discovery via Agentic Black-box Optimization](https://arxiv.org/abs/2609.32394)

**<font color=#1a73e8>作者：</font>** Minghao Li, Rui Tan, Ruihang Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing dense reward functions for low-level reinforcement learning (RL) control remains difficult. Recent work uses large language models (LLMs) to iteratively generate and refine reward functions using policy-training feedback within scripted search algorithms. However, evaluating each candidate requires a full RL training run, making sample efficiency a central challenge for reward search on complex control tasks. To address this limitation, we propose an Agentic Reward Black-box Optimization (ARBO) framework, in which an LLM agent builds the search strategy at run time from an evaluation history maintained as its persistent workspace. The evaluation history comprises two components: observations maintained by the evaluation oracle, including candidate scores, per-term training curves, and error tracebacks; and an agent-maintained belief that records diagnoses and intended next steps. The agent queries both with tools and generates the next batch of reward candidates, rather than generating them in a single pass from a fixed prompt. Across four control domains, ARBO achieves gains of 29.9% in manipulation success rate and 192.8% in power-grid score over baseline means under a shared evaluation budget. Ablations examine each component's contribution and sensitivity to backbone choice.

---


### 142. [SinBrief: A Hybrid Framework for Abstractive Text Summarisation of Sinhala Legal Documents](https://arxiv.org/abs/2609.32397)

**<font color=#1a73e8>作者：</font>** Minduli Lasandi, Nevidu Jayatilleke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal document summarisation in low-resource languages presents significant challenges due to the scarcity of annotated data and the complexity of domain-specific terminology. This paper presents SinBrief, a hybrid abstractive summarisation framework for Sinhala legal documents that does not require human-annotated training data. The proposed framework combines domain-aware word graph construction with neural sentence scoring to generate abstractive summaries from Sinhala legal text. Five sentence scoring models are evaluated within the framework: mBert, Llama 3.1, Falcon 7B, Laser, and a continually pre-trained Llama model domain-adapted to Sinhala legal text. The framework is evaluated on a Sinhala legal corpus using reference-free metrics, including Coverage, Density, Compression Ratio, SummaC, and Self-BertScore. Experimental results demonstrate that SinBrief produces summaries with lower lexical overlap than extractive baselines while maintaining factual consistency, demonstrating the viability of hybrid, largely annotation-free abstractive summarisation for low-resource legal NLP tasks.

---


### 143. [Function Over Form: Distributional Orthogonalization in Mixture-of-Experts with Replica Expert Mechanism](https://arxiv.org/abs/2609.32398)

**<font color=#1a73e8>作者：</font>** Jinfan He, Yunzhuo Liu, Kai Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The scaling of LLMs increasingly relies on MoE architectures to decouple active computation from total parameter count. However, the efficacy of MoE is often constrained by expert collapse and representation redundancy, both leading to underutilization of model capacity. To address these challenges, this paper proposes Distributional Orthogonalization Loss (DO-loss), an auxiliary regularization that shifts the focus from static weight diversity to dynamic routing behavior. By representing each expert's token assignment history as a high-dimensional binary load signature, DO-loss penalizes signature overlap to prevent expert collapse while encouraging functional specialization. To align this algorithmic design with system efficiency, we further introduce the Replica Expert Mechanism (REM), which improves load balancing through a two-tiered strategy: adjusting replica expert placement at the global-batch level and performing real-time token dispatching at the micro-batch level. Empirical evaluations demonstrate that our method outperforms the evaluated routing algorithms on downstream tasks for both 4.8BA0.5B and 30BA3B MoE models, while maintaining comparable training efficiency.

---


### 144. [SkillDRE: Dual-Stage Red-Team Evolution of Agent Skills via Pre-Execution and Runtime Feedback](https://arxiv.org/abs/2609.32400)

**<font color=#1a73e8>作者：</font>** Pengyu Zhu, Jingyi Yang, Yi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills package instructions, executable code, and task-specific resources into reusable artifacts that agents can improve using execution feedback. The same mechanism also enables attackers to evolve malicious skills, making them more effective and less detectable. However, a candidate skill may pass pre-execution scanning yet fail to realize its target under runtime defenses, while a revision that repairs execution may introduce new scanner findings. We introduce SkillDRE, a fully automated framework for evolving complete malicious skill packages through a dual-stage feedback loop. Given a benign task and its associated skills, SkillDRE autonomously constructs and validates a task-conditioned malicious objective and a verifiable judge rule. It then holds both fixed while evolving the skill implementation, with preservation of legitimate task capability. SkillDRE combines scanner-guided evolution with runtime-guided refinement informed by execution outcomes observed under runtime defense. Each runtime-guided revision returns to the pre-execution stage for rescanning and further optimization before re-execution, forming a cross-stage closed loop. Evaluated on SkillsBench across four victim models, SkillDRE achieves an average attack success rate of 45.28%, exceeding the strongest baseline by 40.3%, while its final submitted skills receive no SkillScan findings and largely preserve benign-task performance. These results show that two-stage defense feedback can serve as a useful learning signal for adaptive red teaming and that evaluating either defense stage in isolation can miss the resulting attack capability. Codes is available at this https URL

---


### 145. [Shared Worlds, Private Minds: Structured Memory for Long-Form Writing as World Creation](https://arxiv.org/abs/2609.32401)

**<font color=#1a73e8>作者：</font>** Qiuyu Tian, Xiaowen Gu, Hang Su 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents that write long-form fiction need an explicit memory of the evolving storyworld to keep new events consistent with established facts. Such memory must keep heterogeneous narrative information distinct, integrate story developments across granularities, and recover dependencies that a writing request leaves implicit. We present NarraWorld, a structured memory system for long-form writing that treats memory construction as world creation. From a shared evidence-grounded graph, NarraWorld derives four connected views: world facts, per-character beliefs, open developments, and hypothetical branches (possible-world continuations). Hierarchical aggregation with atomic closure consolidates events into scenes, plotlines, and plots, keeping each higher-level node traceable to its constituent source spans. For retrieval, planned reconstruction infers a query's dependencies from the current narrative situation and a preview of memory, then assembles the relevant records within a token budget. Across three writing benchmarks, NarraWorld achieves the strongest aggregate results. Its memory also transfers to situated role-playing and largely preserves recall on a general-purpose long-term memory benchmark, paving the way for agents that sustain coherent storyworlds across diverse narrative tasks.

---


### 146. [Opening LLM Judges: Recovering Preference Signals Beyond the Final Verdict](https://arxiv.org/abs/2609.32407)

**<font color=#1a73e8>作者：</font>** Sourabrata Mukherjee, Sunayana Sitaram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judges are widely used to evaluate model outputs, but their verdicts can be unreliable: a judge may favor the worse answer for its position, length, or other surface features. When a judge is wrong, is the information needed to judge correctly absent from the model, or present in its internal representations but not reflected in the output? We study this across 64 open-weight evaluators and 14 datasets, including causal interventions on 41 judges (editing activations mid-run to see whether the verdict changes). On LLMBar, built so the superficially better answer is the worse one, the verdicts of 50 judges agree with human labels only 0.456 of the time, even after averaging both answer orders. Yet a small probe on the same judges' activations, with no weight updates, reaches 0.846, and 0.686 once surface features such as length and position are residualized out (0.507 with shuffled labels). The gap holds across eight benchmarks and model families, but is not universal: a score of how well surface features alone predict the human label, computed before any probe is trained, predicts the size of the gain (Spearman rho = 0.90). On rubric tasks that score one answer at a time, leaving no surface cue to exploit, reading the internals gives no advantage. The interventions also show that editing activations mid-network already changes the verdict, before it can be read off directly, and locate the pathways carrying position and length bias. At the same label budget, the recovered signal lets a judge flag cases where it is likely wrong and yields better labels for preference learning. A wrong verdict, then, does not mean the judge lacks the information, and a simple diagnostic shows when it is worth recovering.

---


### 147. [RefAdapt-DiT: Adaptive Joint Attention for Reference-Conditioned Diffusion Transformers](https://arxiv.org/abs/2609.32415)

**<font color=#1a73e8>作者：</font>** Jian Tang, Jiawei Fan, Qiannan Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have become the standard backbone for high-quality generative modeling, yet deploying them in conditional generation tasks remains computationally prohibitive because bidirectional joint attention repeatedly processes large reference streams. While existing optimization schemes mitigate generic temporal redundancy, they typically rely on coarse-grained static reuse and overlook the distinct dynamics of references and targets. Specifically, we observe that reference representations often evolve slowly along the generation trajectory, while the target often assigns little attention mass to them; reference drift and this target-to-reference exposure jointly shape how strongly stale reference states affect the target. To exploit these patterns, we introduce \RefAdapt, a training-free framework for adaptive control of joint attention between references and targets. Instead of rigid static strategies, \RefAdapt combines consecutive target-Q change with previously observed target-to-reference attention mass to control reference computation adaptively at block granularity. Under ultra-few-step settings, \RefAdapt enables speedups of up to $2.097\times$ on 4-step MiniMax H3 and $3.54\times$ on 8-step Qwen Image Edit, while maintaining comparable visual quality.

---


### 148. [MergeHEIR: Mitigating Multimodal Hallucinations as the Tax of Model Merging](https://arxiv.org/abs/2609.32422)

**<font color=#1a73e8>作者：</font>** Jinyu Li, Hao Fang, Zhiming Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model merging consolidates task-specialized experts into a single deployable model. However, we show that such capability consolidation incurs a merging tax of increased hallucination: across 8 model-merging methods, every merged checkpoint exhibits a higher hallucination rate than the average of its constituent experts. An intuitive approach is to adapt existing hallucination-mitigation methods to the post-merge model, yet this unconstrained adaptation disrupts inherited capabilities, creating a tension between hallucination mitigation and expertise retention. To tackle this challenge, we introduce MergeHEIR, a post-merge adaptation framework designed to reduce this merging tax while preserving expertise inherited from initial experts. Using small expert-task calibration sets, MergeHEIR constructs layer-wise null-space projectors via SVD from task-specific activations collected from the merged checkpoint, and periodically projects the accumulated post-merge displacement onto the resulting null spaces to preserve inherited expertise. Theoretically, we establish minimum-distortion and maximum-dimensionality guarantees, characterize the threshold-controlled adaptation-retention trade-off, and extend perturbation guarantees beyond finite calibration data. Across 24 paired comparisons spanning three MLLM configurations and 8 model-merging methods, MergeHEIR consistently mitigates hallucination while largely preserving inherited expertise, demonstrating a more favorable hallucination-retention trade-off.

---


### 149. [PluginRSI: Recursive Improvement of Agent Harnesses with Reusable Plugins](https://arxiv.org/abs/2609.32423)

**<font color=#1a73e8>作者：</font>** Yaorui Shi, Yuchun Miao, Yuxin Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The harness surrounding a language model is a central determinant of agent performance. Recent methods optimize harnesses by searching over complete programs, where individual mechanisms are difficult to isolate and reuse. We introduce PluginRSI, which represents a harness as a composition of atomized plugins and organizes harness evolution around these plugins. Individual plugins are improved independently and accumulated in a shared library, then recombined into new harnesses at each iteration. PluginRSI improves over existing harness optimization methods across software engineering, command-line interaction, and question-answering tasks. The resulting harnesses retain their advantage when transferred to other solver models without further optimization. The evolved plugin library accelerates subsequent optimization from the initial harness, which helps faster and higher convergence on unseen tasks. These results show that accumulating reusable mechanisms provides an effective basis for continued harness improvement.

---


### 150. [CyberClear: A Benchmark for LLM Agent Systems on APT Attack Chain Provenance](https://arxiv.org/abs/2609.32424)

**<font color=#1a73e8>作者：</font>** Qi Chen, Fushuo Huo, Hangli Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model agents have demonstrated promising capabilities in cybersecurity tasks, yet their ability to reconstruct complete Advanced Persistent Threat attack campaigns from complex security logs remains largely unexplored. Existing cybersecurity benchmarks for agents mainly focus on vulnerability discovery, exploitation, and security analysis tasks, leaving the evaluation of attack chain provenance under realistic security logs insufficiently studied. To address this gap, we introduce CyberClear, a benchmark for evaluating LLM agents and advanced agent systems on APT attack chain provenance from long-context security logs. CyberClear covers both single-step attacks and multi-stage attack chains, requiring agents to identify attack evidence, infer attack progression, and generate provenance graphs containing entities, causal relationships, MITRE ATT&CK techniques, and forensic evidence. To enable comprehensive evaluation, we develop an evaluation method tailored to APT attack chain provenance. Unlike conventional text similarity metrics that focus on surface-level matching, our evaluation examines whether reconstructed graphs preserve the semantics of attack chains across single-step behavior correctness, multi-step behavior identification, temporal and causal consistency, entity and relationship fidelity, and overall attack narrative consistency. Advanced multi-agent systems powered by state-of-the-art LLMs still struggle on CyberClear, motivating us to propose CyberProvenance, an agent cyber harness designed for multi-agents that augments LLM agents with evidence accumulation, execution-based validation, and feedback-guided refinement mechanisms for reliable attack-chain provenance. Extensive evaluations on CyberClear demonstrate the effectiveness of CyberProvenance in improving evidence reasoning, execution-grounded validation, and complete APT attack chain reconstruction.

---


> [!TIP]
> 当前位于：**101-150**（第 3/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

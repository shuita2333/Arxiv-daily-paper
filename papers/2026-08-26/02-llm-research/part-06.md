# 🧠 大模型相关研究 | 2026年08月26日

> 本类共 **363** 篇论文：已确认 **347** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-363](./part-08.md)

---

### 251. [WildHandBench: A Benchmark for Handwritten Text Understanding that Challenges MLLMs and Humans](https://arxiv.org/abs/2608.22959)

**<font color=#1a73e8>作者：</font>** Jun Zhang, Qiao Zhao, Cheng Cui 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While the top model on OmniDocBench now reaches 96.34% overall on printed-document parsing, the ability of current models to handle challenging handwritten documents remains largely uncharacterized. Existing benchmarks focus on isolated text or formulas, overlook handwritten tables and real-world degradation, and report aggregate accuracy without explaining why models fail.
We present WildHandBench, a benchmark containing 500 handwritten documents across three structures (free text, tables, formulas), four languages, and nine real-world scenarios. We introduce a Prior-Driven Error (PDE) metric that quantifies whether errors originate from language priors rather than visual evidence. Evaluating 18 state-of-the-art models together with calibrated human baselines, we find: (1) the best model achieves only 71.85% overall; (2) humans outperform all models yet the gap is narrow (77.09% vs. 71.85%); and (3) model errors are qualitatively different from human errors -- 63-91% of model errors are prior-driven versus only 49% for humans, exposing systematic reliance on language priors that conventional accuracy metrics cannot capture.

---


### 252. [What Process Evaluation of Coding Agents Actually Measures: Action, Task, and Step Are Three Different Levels](https://arxiv.org/abs/2608.22960)

**<font color=#1a73e8>作者：</font>** Jiawei He, Mengyu Shi, Jie jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are increasingly evaluated not only by whether they solve a task, but also by how they execute it. However, existing process-level evaluations often treat action prediction, task uncertainty, and step attribution as if they were the same problem, which makes it unclear what such evaluations actually measure. In this paper, we introduce a measurement framework for process evaluation in coding agents and instantiate step-level causal attribution with SCAE, a replay-based estimator derived from a structural causal model of agent execution. Our framework combines prefix-conditioned identification, replay/intervention-based estimation, and controlled judge-information manipulation to study process evaluation at the action, task, and step levels. Experiments on 499 file-localization episodes from 12 repositories show that next actions are driven primarily by execution provenance rather than code-graph transitions, execution uncertainty is structured at the task rather than step level, and full-trace judges exhibit systematic collider bias, suggesting that current process evaluation often measures semantic relevance rather than certified causal contribution.

---


### 253. [Buried in Textual Debt: Context Pruning with Visual Evidence Preservation for MLLM Agents](https://arxiv.org/abs/2608.22963)

**<font color=#1a73e8>作者：</font>** Yuchen Huang, Sijia Li, Jun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly deployed as multi-step agents, where explicit reasoning supports task decomposition and tool coordination but also accumulates self-generated text. Over long trajectories, this text can dominate the context and suppress visual evidence, creating textual debt. We observe that reasoning becomes redundant once task-relevant visual evidence is grounded, while stale hypotheses can misguide later inference when grounding remains uncertain. Pruning must therefore remove redundant text without discarding visual evidence. We propose SPARE, a Kullback--Leibler (KL)-guided framework for pruning accumulated reasoning in multimodal tool-use agents. SPARE uses a compact task-state summary as privileged diagnostic context. For each candidate segment, it replays the same model under the original and summary-conditioned contexts. Reverse-KL divergence from on-policy self-distillation (OPSD) then tests whether the summary sufficiently covers the segment without disrupting future reasoning. We further fine-tune the summarizer with supervised fine-tuning (SFT), enabling more compact summaries, broader coverage, and more aggressive pruning. Across multi-step visual tool-use benchmarks, SPARE achieves the highest average accuracy among pruning methods while removing 37.89--64.58\% of reasoning tokens. This favorable accuracy--context trade-off shows that reducing textual dominance restores reliance on visual evidence and mitigates over-conditioning on self-generated language.

---


### 254. [Closed-Loop Bayesian Molecular Inverse Design with Semantic LLM Surrogates](https://arxiv.org/abs/2608.22967)

**<font color=#1a73e8>作者：</font>** Yaoyao Xu, Xinjian Zhao, Xiaozhuang Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Practical molecular inverse design is rarely a one-shot generation problem; it often takes the form of closed-loop candidate-pool enrichment, where under a limited oracle budget the goal is to \emph{increase the fraction of generated molecules that match a desired property profile}. Bayesian optimization (BO) offers a natural framework for this setting, yet standard Gaussian-process surrogates typically operate in compressed continuous embeddings, which discard the substructural and reference-similarity signals that chemists naturally use to decide where to look next. We propose \textbf{\method}, a closed-loop framework in which the surrogate, rather than the generator, is treated as the locus of design choice, and instantiate it with a frozen large language model that reasons directly over the task instruction, SMILES-level optimization history, and oracle feedback in their native textual form. At each iteration, the surrogate returns a structured decision signal that selects informative reference molecules under an exploration and exploitation principle, optionally with a concise guidance sentence. This signal is converted into next-round conditioning text for a frozen molecular generator, yielding an inspectable optimization trace in natural language. Experiments on MolQA drug and material design tasks show that \method improves over one-shot prompting, is competitive with or stronger than GP-based BO baselines, and reveals a domain-dependent interface: reference-only transfer works best for binary drug targets, while adding a concise surrogate summary is more beneficial for continuous material

---


### 255. [ParallelWorld: Test-Time Scaling for Embodied Reasoning](https://arxiv.org/abs/2608.22971)

**<font color=#1a73e8>作者：</font>** Min Chen, Shengjun Zhang, Yuxin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied Reasoning constitutes a fundamental capability of embodied intelligence, serving as the basis for autonomous perception, reasoning, and interaction within physical environments. Recent studies have shifted the paradigm of embodied reasoning from static perception toward dynamic exploration, where agents acquire task-relevant information through interactions with the environment. However, existing active reasoning approaches generally generate exploration trajectories incrementally without long-horizon planning. Even recently emerged test-time scaling frameworks often resort to myopic, single-step lookaheads, which struggle to resolve the delayed feedback inherent in complex, occluded spatial environments. To address this limitation, we propose ParallelWorld, a multi-horizon test-time scaling framework for embodied reasoning. Instead of greedy, single-step trials, ParallelWorld empowers agents to simulate and evaluate multi-step future trajectories in parallel before committing to an action. Specifically, we introduce a verifier-guided tree-search paradigm. Starting from the current state, ParallelWorld branches into multiple parallel trajectories and rolls them out continuously across a multi-step horizon. At each simulation step, a verifier agent evaluates the intermediate state transitions, dynamically pruning unpromising branches and prioritizing paths with the highest information gain. Once the multi-step prospective simulation is complete, the agent synthesizes the long-horizon outcomes to commit to the optimal action sequence. Finally, an answer agent performs reasoning over the selected trajectory to produce the final reasoning. Extensive experiments on ESI-Bench demonstrate that ParallelWorld consistently improves active perception and reasoning performance.

---


### 256. [Optimize Surgical Triplet Recognition: A Knowledge-Driven Mixture-of-Experts Solution](https://arxiv.org/abs/2608.22972)

**<font color=#1a73e8>作者：</font>** Yiyi Zhang, Yuchen Yuan, Ying Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical action triplet recognition constitutes a critical task in context-aware robot-assisted surgery, facilitating automatic surgical action perception by identifying instrument, verb, target, and their association. However, existing works struggle to analyze such complex surgical scenes due to three main issues: (1) component-level optimization conflicts caused by entangled feature spaces, (2) category-level optimization conflicts arising from severe data imbalance, and (3) lack of domain knowledge guidance that limits model interpretability and robustness. To address these challenges, we propose a Mixture-of-Experts-guided Co-Optimization (\textit{MoeCo}) framework powered by knowledge-driven learning. Within the co-optimization pipeline, to first mitigate component-level conflicts, we introduce a component-tailored adapter that disentangles task-specific features across spatial-temporal regimes, facilitating effective component specialization. Next, we develop a coordinated gradient learning strategy to handle category-level conflicts, which adaptively rebalances positive-negative gradients to enhance the perception of rare categories. Notably, inspired by surgical domain expertise, we introduce a knowledge-driven mixture-of-experts mechanism that dynamically integrates multimodal large language model-guided knowledge via activated experts, thereby enriching the co-optimization pipeline with more expressive and robust representations. Extensive experiments on the public CholecT45 and CholecT50 datasets confirm the effectiveness of the proposed co-optimization pipeline and the superiority of dynamic priors integration via the knowledge-driven mixture-of-experts mechanism.

---


### 257. [Toward Effective and Reliable LLM Agents via Dynamic Ontology](https://arxiv.org/abs/2608.22974)

**<font color=#1a73e8>作者：</font>** Xiaohui Zhang, Zequn Sun, Chengyuan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents rely heavily on knowledge encoded in model parameters or presented as unstructured context. In domain-specific tasks, this leaves important semantic connections implicit. This often results in incomplete evidence use and brittle multi-step decisions. Ontologies offer a way to externalize domain concepts and relations as machine-interpretable structures, but constructing task-usable ontologies traditionally requires substantial effort from domain experts and is difficult to scale. Automatic construction is also challenging: an ontology that appears semantically plausible may not contain the relational structures needed for actual decision making. We present OaK, an ontology-as-a-kernel framework that dynamically constructs and refines task-oriented ontologies for LLM agents. Given task requirements and training data, OaK constructs an ontology and its knowledge graph, generates task-adaptation functions for graph reasoning, and uses judge feedback to iteratively refine both. By making relevant concepts and relations explicit, the ontology grounds knowledge retrieval and multi-step decision making. We evaluate OaK on TravelPlanner, CRMArenaPro, and ToolQA. Results show that OaK improves standard LLM agents, strengthens evidence grounding, and boosts the reliability of multi-step reasoning.

---


### 258. [LLM Pedagogical Behavior in AI Tutoring Interactions](https://arxiv.org/abs/2608.22993)

**<font color=#1a73e8>作者：</font>** Suhyeon Lee, Juneha Baek, Jaehyeong Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Students increasingly use LLMs as tutors for coursework and problem solving. Little is known about the level of assistance LLMs provide when students use them as tutors in authentic learning interactions. This matters because tutoring responses can differ substantially in how directly they help students complete a task. We operationalize this dimension as scaffolding level and develop a five-level scale, validated against human annotations, that characterizes responses according to the degree of direct assistance they provide. We apply the scale to 14,637 LLM responses from 203 students in a university AI course. Responses are overwhelmingly concentrated at high levels of assistance, with more than 95% classified as either Explaining or Solving. Scaffolding level is systematically associated with students' subsequent conversational behavior, but provides little additional predictive information about performance on three subsequent exams beyond prior achievement and dialogue behavior. These findings provide an empirical baseline for LLM assistance in tutoring interactions and a measurement framework for evaluating how alternative tutoring designs change that assistance.

---


### 259. [A Physical Response-and-Memory Model for Muon Optimization](https://arxiv.org/abs/2608.22994)

**<font color=#1a73e8>作者：</font>** Yinze Hu, Hongjun Xiang, Xingao Gong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models is costly. How low a loss the same compute can ultimately reach depends on how each step's gradient is converted into a weight update; the rule that performs this conversion is the optimizer. From SGD and AdamW to the recent Muon, effective update rules have mostly been shaped by engineering intuition and then selected on benchmarks. Muon semi-orthogonalizes the momentum matrix before applying the update and has kept breaking records on public training benchmarks; yet why the semi-orthogonalized direction works, and over how long a history the momentum should average, are two questions at present answered mainly by experience. Here we treat the weight matrix during training as a responsive medium with memory and build a physical model for it, in which both questions find answers: the semi-orthogonalized direction is the maximally dissipative response under an output-side safety budget, which explains why it works; momentum is the internal stress accumulated by the medium; how long it should average is set by the relaxation of this stress, and a real medium relaxes on more than one timescale, the simplest form being one fast and one slow. On this basis we propose the Bi-Maxwell optimizer. The framework further yields a testable consequence: gradient directions change fast early in training and more slowly later, so the optimal memory length should grow with training stage; step-by-step measurements of a proxy for it by a read-only probe across 8 independent training trajectories are consistent with this consequence. Replacing the memory kernel alone, from a single timescale to two, brings training to the target loss in noticeably fewer steps on a public large-language-model optimizer benchmark.

---


### 260. [ENCORE: Entropy-Guided Cropping and Attention Regularization for Robust Vision--Language Understanding](https://arxiv.org/abs/2608.22996)

**<font color=#1a73e8>作者：</font>** Yuanhao Sun, Huawei Ji, Jiaxin Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) perform well on diverse vision-language tasks, but transformer-based visual encoders split images into fixed-resolution sub-images, compromising object integrity in lightweight VLMs. Existing methods only focus on the visual modality and fail to dynamically preserve the integrity of prompt-relevant regions, limiting performance. In this work, we observe that the early-layer image-text entropy of cross-modal attention strongly correlates with answer grounding quality and task accuracy. Building on this finding, we propose \textbf{ENCORE}, an entropy-guided framework with two components: At inference, an \textbf{Entropy-based Cropping Strategy} (ECS) evaluates a small set of candidate crops and selects the one with minimal entropy, preserving contiguous regions relevant to the prompt. At training, \textbf{Entropy Regularization Training} (ERT) augments next-token prediction with an entropy term that sharpens attention on key visual tokens while down-weighting irrelevant ones. Experiments on ten VQA benchmarks show that ENCORE, fine-tuning only 0.14\% of parameters, achieves an average 1.43\% accuracy gain and state-of-the-art performance among recent 2B-parameter VLMs. Our code is released in this https URL.

---


### 261. [Coarse Indexing, Fine Evidence: Decoupling Temporal Granularity in Long-Video RAG](https://arxiv.org/abs/2608.23011)

**<font color=#1a73e8>作者：</font>** Zhe Jin, Zhimin Lin, Bin Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graph-based retrieval-augmented generation (RAG) provides a scalable paradigm for long-video understanding, but existing systems typically inherit a fixed temporal granularity from video segmentation when constructing their retrieval index. We argue that this design unnecessarily couples indexing granularity with evidence granularity: coarse representations can often suffice for locating relevant temporal regions, while fine-grained evidence remains important for downstream reasoning. We propose \textbf{Density-Aware Graph Construction (DAGC)}, a training-free approach that decouples a query-independent coarse retrieval index from the original fine-grained evidence space. DAGC constructs a compact, density-adaptive graph index by merging visually redundant neighboring chunks, while preserving mappings to the original temporal units. Retrieved coarse regions are subsequently expanded back to the original chunk granularity for fine-grained evidence refinement and answer generation. Experiments on MLVU, VideoMME, and LongVideoBench show that DAGC retains only about 40--50\% of the original graph nodes and achieves $1.3$--$1.7\times$ end-to-end wall-clock acceleration while preserving approximately 99\% of the original QA performance. The gains transfer across different LVLM backbones and video RAG pipelines, suggesting that long-video RAG need not maintain the same temporal granularity for indexing and evidence reasoning.

---


### 262. [SplitLite: Low-Rank Residual Compression for Split Learning](https://arxiv.org/abs/2608.23018)

**<font color=#1a73e8>作者：</font>** Tao Li, Yulin Tang, Qi Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of on-device large language models (LLMs) faces a significant computing burden. To overcome this limitation, split learning (SL) has emerged as a promising solution, which offloads the primary training workload to a powerful server. However, SL requires exchanging high-dimensional activations and gradients between clients and the server, resulting in prohibitive communication costs. To overcome this challenge, we propose SplitLite, a communication-efficient split federated LoRA fine-tuning method that exploits the low effective rank structure of consecutive-epoch activation and gradient residuals. Our key finding is that, when LoRA uses rank $r$ updates in parameter space, the activation and gradient residuals of the same data sample between adjacent epochs also exhibit effective rank-$2r$ and rank-$4r$ structures, respectively. By revealing this property, SplitLite transmits only quantized truncated singular value decomposition (SVD) residual factors, thereby significantly reducing both activation uplink and gradient downlink traffic. Extensive experiments on the GLUE benchmark across a series of advanced on-device LLMs demonstrate that our method reduces activation uplink communication costs by up to 93.5\% and total communication costs by up to 83.7\%, without performance degradation.

---


### 263. [Unlearning Is Not Just Erasing: Temporal Decoupling via Generation Inequality](https://arxiv.org/abs/2608.23020)

**<font color=#1a73e8>作者：</font>** Xunlei Chen, Qirui Ye, Yuang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) require effective unlearning to address privacy regulations and safety concerns. However, achieving precise forgetting without compromising general utility remains challenging. Existing sequence- and token-level methods penalize target outputs without modeling their context-dependent retrieval paths, which can disrupt linguistic structure or suppress benign knowledge. We present ADU, a fine-grained, training-based framework that shifts unlearning from token erasure to contextual attention-pathway decoupling. Exploiting the functional distinction between local and global attention heads, ADU identifies preplan positions that retrieve persistent sensitive anchors and fixes their candidate paths under the original model. It then trains attention-projection adapters to suppress attention mass along these paths while preserving local-attention structure and retain-set language modeling. Post-training activation exchange tests whether the modified attention-output module transmits the learned forgetting effect. ADU achieves the strongest aggregate performance among evaluated baselines on the TOFU and WMDP benchmarks, including a Forget Quality of (0.93) on TOFU. It preserves 87--98% of model utility (92.9% on average versus 81.9% for baselines) while reducing side effects in benign contexts.

---


### 264. [Most of the LLM routing gap is task type](https://arxiv.org/abs/2608.23023)

**<font color=#1a73e8>作者：</font>** Janghoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An LLM router picks which model should answer each query. The appeal is that models fail on different questions. Whatever single model is best overall still gets some wrong, and another model in the pool gets many of those right. Getting that choice right every time is the ceiling, and a router is an attempt to approach it.
However, recent work reports that routers do not get close. Across 21 routing methods on five benchmarks, sharply different designs land within a fraction of a point of each other, and all of them stay far below that ceiling. Learned routers often fail to beat simply always calling the strongest model.
We ask what those missed questions have in common. We set fourteen models to answer all 294 questions, with 7 task types across 3 languages: Korean, English and Hindi. We ran the whole matrix twice, changing nothing, but 5.37% of the 4,116 model-question pairs came out scored differently anyway. Run-to-run movement like that is normal, and we argue that a small win does not show that routing did anything, ours or anyone else's.
Counting an answer correct only when the model got it right in both runs, 29 questions on this matrix can be improved with routing. Every correct-answer count here is on that rule. Task type accounts for most of them: assigning each task type one model in advance, chosen once and never updated, improves 21 of the 29. Splitting each task type by language improves 2 more and leaves 6 of 294 unoptimized. That handful is what a learned router would have been built for, and it is smaller than the run-to-run movement above, which is a share of pairs rather than of questions. The static table we adopted answers 262 of 294 questions at $3.33 per run, against the best single model's 245 at $7.69.
All of this is fitted and scored on the same 294 questions with no holdout.

---


### 265. [Beyond Surface Cues: Disentangling Sociocultural Signals in Multilingual LLMs](https://arxiv.org/abs/2608.23026)

**<font color=#1a73e8>作者：</font>** Yuanjun Feng, Tanzhou Liu, Stefan Feuerriegel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual LLM outputs can vary across sociocultural contexts. However, evidence of cultural grounding can be misleading: identity labels may be inferred from explicit or indirect textual cues, while names and wording can reveal the source language. Treating all these signals as evidence of cultural grounding may obscure potential biases. We present a human-validated, multi-agent audit that separates three questions: whether outputs reproduce social biases, whether identity groups are represented differently, and whether outputs reflect cross-cultural patterns. The study analyzes 89,253 outputs from 12 LLMs in English, French, and Chinese, spanning 18 occupations and three task conditions.
We find that bias representation varies systematically across languages and tasks. Removing direct identity cues sharply reduces identity-label prediction in English and Chinese, but has a much smaller effect in French. Across all language-genre settings, the cultural context associated with the source language receives the highest average relevance score, with moderate agreement between automated and human ratings. However, the ability to identify the source language drops substantially after translation and again after masking names. Without these controls, multilingual audits may mistake surface cues for cultural understanding, leading to misleading conclusions about cross-cultural variation and bias. Our audit offers a practical framework for separating such shortcuts from more meaningful cross-cultural patterns.

---


### 266. [Meta-Moderator: Empowering Multi-Agent Debate with Meta-Cognition](https://arxiv.org/abs/2608.23029)

**<font color=#1a73e8>作者：</font>** Wentao Hu, Zhuoyue Wan, Jinhao Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate can improve large language model reasoning by eliciting diverse hypotheses and critiques, yet its performance is often constrained by weak moderation. Common pipelines rely on fixed budgets, agreement-based stopping, or untrained judges, leading to redundant deliberation and unreliable evidence aggregation. We cast moderation as a meta-cognitive process, monitoring debate utility, controlling deliberation, and adjudicating a final answer, and introduce Meta-Moderator, a learnable framework that dynamically regulates debate and decides when to finalize an answer. Meta-Moderator is trained independently of the debaters via outcome-driven policy optimization, making debate regulation an explicit capability rather than an incidental effect of prompting. Across five benchmarks, Meta-Moderator outperforms widely used decision layers and transfers across tasks and system configurations. Further analyses show that it allocates debate more selectively and reduces mis-aggregation after informative hypotheses appear.

---


### 267. [ST$^2$U: Stateful Test-Time Unlearning via Restricted Knowledge Boundary Control](https://arxiv.org/abs/2608.23034)

**<font color=#1a73e8>作者：</font>** Xunlei Chen, Qinghui Gong, Ruini Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Controlling restricted knowledge in large language models is essential for model alignment and safe deployment. Test-time unlearning avoids costly retraining and parameter updates by intervening only during inference. However, existing activation-editing methods apply isolated pointwise corrections, overlooking how autoregressive generation continually reconstructs hidden states from the prompt, cache, and generated prefix. Consequently, later states may return to restricted knowledge regions after a locally successful correction, causing restricted knowledge re-entry. In this work, we propose Stateful Test-Time Unlearning via restricted knowledge boundary control (ST$^2$U), which formulates test-time unlearning as trajectory-wide boundary control. ST$^2$U first models restricted knowledge boundaries in low-dimensional invertible coordinates while leaving orthogonal non-target components unchanged. During inference, ST$^2$U monitors risk along the trajectory, applies minimal boundary corrections with contextual anchoring, and propagates historical correction states across tokens to mitigate knowledge re-entry. This trajectory-wide control enables more persistent forgetting while preserving non-target capabilities and limiting inference overhead. Across three benchmarks and three model families, ST$^2$U delivers the strongest overall balance, combining best or second-best retention with competitive forgetting and substantially less restricted-knowledge re-entry than test-time baselines (13.76%-19.84% versus 46.50%-59.10%).

---


### 268. [MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks](https://arxiv.org/abs/2608.23035)

**<font color=#1a73e8>作者：</font>** Yi Zhu, Xiongwei Wu, Qiyi Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As on-device LLM agents evolve into personal copilots, the mobile operating system has become a key testbed for this paradigm, making rigorous capability evaluation essential. Yet existing benchmarks fall into two camps, each with a critical blind spot: GUI-centric benchmarks test surface-level screen manipulation while overlooking background tool use and long-horizon planning, whereas static function-calling benchmarks rely on offline API matching that is detached from real runtime constraints. To close this gap, we present \textbf{MobilePA-Bench}, an interactive, stateful, and tool-centric benchmark for evaluating the tool-calling and planning abilities of mobile planning agents. MobilePA-Bench runs on an executable sandbox that maintains live application databases and returns structured feedback, spanning $13$ functional domains and $212$ realistic mobile tools. Beyond basic tool use, it evaluates a central planning agent along three advanced dimensions: \emph{(1)~Sub-agent Collaboration}---decomposing a complex task and delegating specialized work to capable sub-agents; \emph{(2)~Memory Usage}---recalling stored memories, user profiles, and past preferences to resolve implicit requests; and \emph{(3)~Skill Usage}---invoking pre-packaged composite skills instead of planning every step from scratch. Extensive experiments show that current frontier LLMs remain unreliable in mobile settings: performance drops sharply under strict tool ordering, permission limits, and unexpected runtime errors. By pairing an interactive function-calling sandbox with evidence-based verification, MobilePA-Bench serves as both a practical diagnostic benchmark and an interactive foundation for agentic reinforcement learning---accelerating the development of dependable mobile agents.

---


### 269. [AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](https://arxiv.org/abs/2608.23041)

**<font color=#1a73e8>作者：</font>** Sungho Park, Wonjoong Kim, Rongyuan Tan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents remain unreliable on long-horizon tasks, where small local failures can compound over extended interactions and lead to overall task failure. Although external harnesses can substantially improve robustness, harness design remains a manual and expensive process that requires searching over a large space of prompts, tool configurations, and control logic. We propose AutoSaddler, an automatic harness optimization framework that formulates harness improvement as an offline learning problem and iteratively updates the harness using failure signals from mini-batches. AutoSaddler combines failure-trace diagnosis, structured patch generation that treats the harness as code, and validation-based update selection. Experiments on GAIA2, SWE-Bench Pro, and Terminal-Bench 2.0 show that AutoSaddler substantially improves agent performance over the corresponding base harnesses, achieving gains of 9.0, 9.6, and 10.0 percentage points, respectively. Ablation studies further suggest that effective harness optimization benefits from three ingredients: deep debugging rather than shallow reflection, targeted modifications rather than unconstrained editing, and generalization-aware selection rather than trajectory-specific repair. Together, these results suggest that automatic harness optimization is a promising path toward more performant and reliable agent systems.

---


### 270. [From Inertia to Objectivity: Improving Deep Research Agents with Noise Isolation](https://arxiv.org/abs/2608.23045)

**<font color=#1a73e8>作者：</font>** Xiangxin Zhang, Zhanwei Zhang, Zhihang Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web search agents powered by Large Language Models (LLMs) show strong promise, but deep research tasks expose a recurring failure mode: once an agent has produced a query, plan, or intermediate conclusion, it becomes less objective when later judging the consequences of that same action. We term this phenomenon \textbf{inertia bias}. To make it measurable, we introduce the IBIS benchmark, which controls the search observations while varying whether the model is evaluating the outcome of its own prior action. We find that models are substantially worse when they ``own'' the preceding search step, showing that self-authored action history can systematically distort subsequent judgment. We further show that this bias propagates into two forms of system-level degradation: search noise at the worker level and contextual noise at the manager level. To address this problem, we propose NIS-Agent, which applies context isolation at the two decision points most vulnerable to inertia bias: webpage triage and final-answer validation. Across GAIA, WebWalkerQA, BrowseComp, and BrowseComp-zh, NIS-Agent achieves competitive performance while reducing token cost by 33\% compared to our baseline. We further train an 8B model to be intrinsically more resistant to inertia bias; under the same NIS-Agent framework, it attains average performance comparable to GPT-4o on deep research benchmarks.

---


### 271. [Beyond Verdicts: A Graph-Based Analysis of Human and LLM Reasoning in Scientific Fact-Checking](https://arxiv.org/abs/2608.23047)

**<font color=#1a73e8>作者：</font>** Abdul Ghafoor, Muhammad Arslan Manzoor, Yufang Hou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Misinformation that cites legitimate papers can be especially harmful when it distorts what those studies actually report. While existing automatic fact-checking systems based on large language models (LLMs) can assess whether a model assigns an Incorrect verdict and can gen- erate explanations for that decision, they typi- cally do not indicate whether the model follows the same reasoning path as human experts or arrives at the verdict through a different but still valid path. In this work, we introduce a graph- based framework (typed reasoning graph) for comparing human and LLM reasoning paths in scientific fact-checking. Building on prior work on fallacious reasoning in biomedical misinformation, MISSCIPLUS (Glockner et al., 2025), we model each explanation as a rea- soning graph that links the false claim to the relevant study context, study findings, fallacy- supporting premises, and fallacy labels. This representation enables one-to-one alignment of human and LLM reasoning at the level of fallacy-specific sub-graphs. For non-human- aligned LLM paths, we validate grounding in the cited study, relevance to the claim, and suf- ficiency for the verdict. Using 84 false claims from MISSCIPLUS, we evaluate GPT-5, Claude Opus 4.7, and Qwen3-32B across prompt and evidence settings. Results show distinct perfor- mance dimensions: Qwen3-32B has the lowest verdict failure rate, GPT-5 the highest human alignment, and Claude Opus 4.7 weak verdict prediction but often valid reasoning in success- ful cases

---


### 272. [Reservoir of Importance: Learning Semi-Structured Sparsity with Differentiable Subset Sampling](https://arxiv.org/abs/2608.23048)

**<font color=#1a73e8>作者：</font>** Ha Dinh, Xuan Duy Ta, Khoat Than 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-structured $N$:$M$ sparsity has emerged as a practical direction for accelerating large language models (LLMs). However, existing learnable-mask approaches incur substantial parameter and memory overhead, limiting their scalability to large models and aggressive sparsity regimes. In this work, we revisit semi-structured pruning from a perspective that reconciles efficiency with scalability. We propose Reservoir of Importance (RoI), a lightweight semi-structured pruning framework that learns sparsity masks through differentiable subset sampling. Unlike prior methods that model full categorical distributions over all feasible $N$:$M$ patterns, RoI introduces a compact-logit parameterization for sparsity mask learning and performs sampling without replacement to select masks, thereby reducing trainable parameters from combinatorial complexity to $\mathcal{O}({M})$. As a result, RoI requires 1.5-8.75$\times$ fewer learnable parameters and significantly lower memory cost, while remaining fully aligned with hardware-friendly sparsity patterns. Extensive evaluations across multiple scales of the Qwen2.5 LLM family (0.5-7B parameters) demonstrate that RoI achieves competitive performance with strong memory efficiency, stability, and scalability to more aggressive $N$:$M$ sparsity patterns, offering a practical path toward efficient LLM deployment.

---


### 273. [What Makes an Initial Reaction Ready for Discussion?: Multi-Persona AI Support for Stance Reflection and Writing](https://arxiv.org/abs/2608.23050)

**<font color=#1a73e8>作者：</font>** Sky Shih-Kai Hong, Mu-Tien Kuo, Wei-Ji Chen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> An initial reaction to a social or community issue can feel meaningful before it is ready to become a message: people still need to clarify the claim, anticipate audience risks, and decide how much reasoning should become visible to others. We present StanceLab, a prototype for preparing a stance before entering a discussion. The prototype compares a three-persona mode, where an Interviewer, Mentor, and Opponent respond in parallel to help users diagnose and revise a stance, with a standalone LLM mode. In a formative within-subject pilot with six participants and 12 task sessions, every session produced a short final message in the notepad. The pilot revealed two design requirements: persona roles should diagnose useful blind spots or objections, and parallel responses need coordination support. We propose a future diagnosis-and-writing workflow that turns persona-based reflection into selective, audience-aware final messages.

---


### 274. [LLM-based Agents for Forecasting and Prediction: Methods, Training, Evaluation, and Applications](https://arxiv.org/abs/2608.23058)

**<font color=#1a73e8>作者：</font>** Xiaogang Xu, Jiaqi Tang, Jianmin Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) now support forecasting systems that combine language-based reasoning with temporal data, evidence retrieval, external tools, and iterative prediction. We investigate LLM-based forecasting agents, meaning systems in which a language model contributes to a scored prediction about a future or currently unobserved target. We organize architectures into three groups. Standalone LLM workflows operate on encoded time series or event context. Tool- and retrieval-augmented agents incorporate external evidence. Hybrid systems pair LLMs with statistical or foundation models. We then review training methods and evaluation protocols. We examine negative as well as positive evidence, including sensitivity to small input perturbations, ablations in which the LLM component does not improve accuracy, and benchmark gains that may reflect contamination instead of temporal reasoning. We cover applications in finance, weather, health, energy, and operations, and we summarize the benchmarks and datasets used for evaluation. The evidence indicates that measurement is a central limitation. Future work requires calibration under distribution shift, contamination-resistant live evaluation, explicit reporting of cost and accuracy together, and methods for handling feedback between deployed forecasts and the outcomes being forecast.

---


### 275. [Improving O-RADS Risk Stratification from Ultrasound Reports: A Comparative Evaluation of Hybrid versus End-to-End LLM Reasoning Strategies](https://arxiv.org/abs/2608.23061)

**<font color=#1a73e8>作者：</font>** Xiaotong Tan, Chunli Qiu, Xin Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Automating clinical guideline-based decision-making with large language models (LLMs) remains challenging because of reliability, hallucination, and limited interpretability. We compared the performance of LLMs and reasoning strategies for automated Ovarian-Adnexal Reporting and Data System (O-RADS) classification from free-text pelvic ultrasound reports. Methods: In this retrospective study, consecutive patients with ovarian masses who underwent pelvic ultrasound were included. Eight LLMs were tested with three reasoning strategies: implicit-knowledge end-to-end, rule-informed end-to-end, and a feature-based hybrid architecture that decoupled feature extraction from rule-based classification. The reference standard was O-RADS categorization established by expert consensus. Results: A total of 310 women with 390 ovarian masses were evaluated. The feature-based hybrid architecture using Gemini 3.6 Flash demonstrated the best performance, achieving an accuracy of 99.2% (387 of 390) and almost perfect agreement with the reference standard (weighted kappa = 1.00; 95% CI: 0.99-1.00). Its performance surpassed that of original clinical reports (accuracy, 87.7% [342 of 390]; weighted kappa = 0.94; 95% CI: 0.91-0.96) and end-to-end LLM strategies (accuracy range, 65.6% [256 of 390] to 95.9% [374 of 390]). For structured feature extraction, Gemini 3.6 Flash demonstrated higher overall accuracy than Claude Fable 5 (98.9% vs 97.8%; P < 0.001). The hybrid architecture reduced misclassification errors and mitigated the overstaging tendency observed in original reports. Conclusion: The feature-based hybrid LLM architecture that separates clinical feature extraction from deterministic guideline execution enables highly accurate, reliable, and interpretable automated O-RADS classification, providing a promising approach for standardized, guideline-based clinical decision-making.

---


### 276. [Cultural Moment Benchmark: Evaluating Video Cultural Reasoning and Grounding in Southeast Asia](https://arxiv.org/abs/2608.23065)

**<font color=#1a73e8>作者：</font>** Burak Satar, Zhixin Ma, Cheng Yu-Tong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cultural understanding in video means more than recognizing what is visible; it requires grasping the symbolic and temporal significance of cultural concepts. We decompose this into three abilities: naming what a concept symbolizes, visually recognizing it on video, and locating its sub-events in time. Existing video-cultural benchmarks tend to test what is seen, collapsing these three abilities into a single score that hides the bottleneck. We introduce the Cultural Moment Benchmark (CMB): 306 expert-curated concepts from seven countries in Southeast Asia across five categories. We evaluate each concept through three stages, one per ability. Given a description, Stage 1 (S1) selects from four candidate concept names, Stage 2 (S2) selects from four candidate video moments, and Stage 3 (S3) predicts the start and end times of the moment in a video. To keep each stage focused on a distinct ability, we use three design choices: semantic-similarity distractors (S1, S2), unlabeled video moments (S2), and free-form localization on a different example video (S3). Across six vision-language models, failure modes vary by ability and modality. i) Even the strongest closed-source models score below 30% when all three stages must be correct; ii) The three abilities do not fully cascade: naming a concept correctly helps half the models recognize it on video, but recognizing it has little effect on locating the sub-event in time; iii) Audio is complementary, redundant, or distracting depending on the concept, more often distracting in non-Latin-script countries; removing both audio and subtitles hurts Games and Music the most. Our 14-rater human study shows that even Expert raters score below chance on concepts from a neighboring country, indicating that CMB requires country-specific cultural knowledge. CMB acts as a diagnostic harness, attributing failures to a specific ability or modality.

---


### 277. [Signal or Noise? A Benchmark Study of Agent Skills in Web Development](https://arxiv.org/abs/2608.23067)

**<font color=#1a73e8>作者：</font>** Ziyue Yang, Fan Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent Skills are reusable procedural modules that are increasingly injected into coding-agent sessions to encode framework conventions, anti-patterns, and reusable tools. However, because each injected Skill expands the prompt of every query, an effective Skill benchmark must determine not only whether an agent can solve a task, but whether the Skill should have been injected at all. We introduce WebDev-Skills-Bench and use it for a controlled empirical study of 31 public WebDev Skills on 50 Web-Bench projects and 1,000 ordered tasks. The benchmark compares four matched conditions, including a length-matched irrelevant control and leave-one-out component ablations. To isolate Skill effects from prompt-length artifacts, we place only this http URL in the prompt while mounting auxiliary files into the agent workspace. Across four models, target Skill injection reduces mean Pass@2 by 1.3% to 4.2%, lowers task completion depth, and increases token cost by 72% to 394%, with gains in only 17% to 36% of Skill-project pairs. Length-matched controls reveal two failure modes: some models are length-distracted, where an equally long irrelevant Skill reproduces most of the loss, while others are content-misled, where prompt length is neutral but Skill content still lowers Pass@2 by 1.1% to 1.4%. Further analysis shows that losses concentrate on easy early tasks, Skill rankings transfer weakly across models, and anti-pattern rules outperform example-heavy content within helpful Skills. These findings recast a matched Skill as a hypothesis about a particular Skill-project-model triple rather than a portable asset, reframing injection as a per-deployment routing decision and making length-matched controls and per-model audits a minimum standard for Agent-Skill evaluation.

---


### 278. [Grounding Isn't Knowing: Do VLMs Need Object Localization for Spatial Reasoning?](https://arxiv.org/abs/2608.23074)

**<font color=#1a73e8>作者：</font>** Xiwei Liu, Yulong Li, Xinlin Zhuang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can answer spatial questions, yet the mechanisms connecting object grounding to spatial reasoning remain poorly understood. It is underexplored whether spatial reasoning internally requires precise objects localization, or can bypass explicit localization through global layout cues. In this work, we investigate two representative model families, LLaVA-1.5 and Qwen2.5-VL, using a suite of mechanistic interpretability tools, including token ablation, layer-wise probing, attention knockout, and causal mediation analysis. We find that spatial relation prediction follows a staged grounding-to-reasoning process in which object-aligned tokens establish coarse target-reference anchors, while precise bounding-box boundaries are not required. Positional information becomes decodable before relation decisions emerge, and a small set of attention heads mediates the causal effects of both localization and spatial reasoning. The two tasks share early grounding-related processing but ultimately rely on partially distinct specialized pathways. Through rigorous experiments, we provide a token-, layer-, and head-level account of how VLMs transform object grounding into spatial relations, showing that knowing where objects are is not equivalent to knowing how they relate.

---


### 279. [AgentWeave: Routing Before Reasoning for Efficient Function Calling in Tool-Rich Language Models](https://arxiv.org/abs/2608.23078)

**<font color=#1a73e8>作者：</font>** Saurav Singla, Aarav Singla, Advik Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly operate over large collections of tools, functions, APIs, and specialized agents. As the candidate action space grows, a function-calling model must process more schemas, consume more prompt tokens, and distinguish among increasingly similar or irrelevant alternatives. We study a complementary systems strategy: reduce the candidate set before language-model inference while leaving the downstream model unchanged. We introduce AgentWeave, a deterministic pre-inference routing layer that constructs a bounded model-visible action space using eligibility, requirement, capability, and routing signals. We evaluate AgentWeave with a frozen BFCL-derived routing-pressure protocol using the public MadeAgents/Hammer2.1-1.5b model. On 48 fresh BFCL V4 multiple-function tasks, AgentWeave achieves 6/48 (12.5%) native BFCL successes, whereas all-tools, deterministic random top-8, and semantic top-8 baselines each achieve 0/48. The paired success difference is +12.5 percentage points with a 10,000-resample paired bootstrap 95% confidence interval of +4.17 to +22.92 points and exact McNemar p=0.03125. Relative to all-tools exposure, AgentWeave presents 70.18% fewer tools, uses 61.70% fewer input tokens, and exhibits 50.95% lower mean local-model latency. The result is deliberately narrow: this is a BFCL-derived routing-pressure study rather than an official full BFCL leaderboard score, and absolute task success remains low. The evidence nevertheless shows that candidate-space construction can materially affect a fixed model's function-calling behavior and motivates evaluating routing as a distinct stage before model reasoning.

---


### 280. [POOL: Propagated Uncertainty Over Lookalikes](https://arxiv.org/abs/2608.23086)

**<font color=#1a73e8>作者：</font>** Rounak Sharma, Ananya B. Sai, Soumyabrata Pal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Black-box large language models need confidence scores that can separate likely-correct from likely-incorrect outputs, enabling systems to prioritize human review, route uncertain cases to stronger models, or choose abstention thresholds on development data. Yet existing confidence estimators face a cost-quality trade-off: verbal confidence is cheap but is often overconfident, while sampling-based uncertainty is more informative but scales linearly with the number of samples per query. We propose \textsc{POOL} (\emph{Propagated Uncertainty Over Lookalikes}),a cost-efficient framework that addresses this trade-off taking inspiration from group-testing.\textsc{POOL} clusters query stems with overlaps, evaluates a base estimator on representative medoids, softly propagates confidence scores to nearby queries, and selectively evaluates high-disagreement cases. We instantiate this framework with \textsc{Hy@}$p$, a hybrid estimator that combines verbal confidence with spectral answer diversity computed from the negative von Neumann entropy of sampled answer this http URL six domains from three datasets and five black-box LLMs, \textsc{Hy@}5 achieves higher average AUROC than verbal confidence and \textsc{Vn@}10 sampling while using half as many samples as \textsc{Vn@}10. \textsc{POOL}-\textsc{Hy@}5 retains 93.5--97.9\% of its AUROC while saving 19.3--39.3\% of generations. On paraphrase-dense workloads, generation savings rise to 73-76\%, showing that semantic redundancy can be leveraged to lower confidence-estimation costs.

---


### 281. [Definitional Sensitivity in Media Bias Detection: A Multi-Definition Dataset and Benchmark](https://arxiv.org/abs/2608.23095)

**<font color=#1a73e8>作者：</font>** Martin Wessel, Timo Spinde, Jürgen Pfeffer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Media bias detection relies on definitions and examples that specify what counts as bias, yet these specifications often vary across datasets or remain implicit, even when given the same name. Such variation makes it unclear whether models trained for the same bias category learn the same construct or different phenomena, a problem largely overlooked in prior work. We examine how definition choice affects bias annotation in a between-subjects experiment with 354 participants and a parallel evaluation with four LLMs. Participants and models rate six news articles across four bias categories using definitions that vary in conceptual framing and elaboration. Across 8,496 human and 28,800 LLM ratings, we find that the conceptual target of a definition drives annotation divergence, while construct-preserving elaboration does not: conceptual framing significantly shifts annotations for humans and does so even more strongly for LLMs. We discuss implications for construct specification in annotation protocols and prompt-based measurement, and consider how definitional sensitivity may propagate to downstream classification beyond media bias. We also release MUDD, the Multi-Definition Bias Detection Dataset.

---


### 282. [Training-Free Pseudo-Fusion for Composed Image Retrieval with Diffusion Models and Multimodal Large Language Models](https://arxiv.org/abs/2608.23102)

**<font color=#1a73e8>作者：</font>** Fan Xu, Luis A. Leiva  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) is an emerging paradigm in content-based image retrieval that enables users to formulate compositional queries by combining a reference image with an auxiliary modality, usually text-based. This approach supports fine-grained search where the target image shares structural elements with the user-provided image while incorporating the modifications specified by the auxiliary text. Conventional CIR methods rely on multimodal fusion to combine visual and textual features into a joint query embedding, which requires training modules that align composed queries with the targets. In this work, we propose PeFuse (for pseudo-fusion), a training-free framework that leverages pretrained Diffusion Models and Multimodal Large Language Models to bridge modalities via generative conversion. We introduce two novel strategies: uni-directional and bi-directional conversion, which convert CIR into four single-modality retrieval problems. These methods reformulate CIR as either intra-modal or cross-modal single-query retrieval tasks, bypassing the need for dedicated task-specific training. Extensive experiments on standard benchmarks demonstrate that converting CIR into text-to-image retrieval tasks is more effective than alternative conversion strategies, achieving competitive or superior performance compared with state-of-the-art methods, while maintaining high flexibility thanks to replaceable components of the conversion pipeline. These results highlight the effectiveness of the pseudo-fusion paradigm for zero-shot CIR. Our code is publicly available at: this https URL.

---


### 283. [Molecular LLM Agents: From Architectural Design to Scientific Autonomy](https://arxiv.org/abs/2608.23104)

**<font color=#1a73e8>作者：</font>** Jiatong Li, Wengyu Zhang, Weida Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Molecular science represents an important frontier for LLM-based agents. Unlike general agents that mainly operate over natural language, code, or web environments, molecular LLM agents must perceive, reason about, and act upon chemical objects across symbolic strings, molecular graphs, 3D conformations, spectra, simulations, and wet-lab measurements. Their capabilities depend on chemically faithful molecular perception, an LLM-centered agent framework, domain-specific tool grounding, and computational or experimental feedback, in addition to planning and tool use. This work develops a conceptual framework for molecular LLM agents from two complementary perspectives. First, we introduce an architectural view of molecular-agent design, covering molecular representation and perception, the agent framework, domain-specific toolboxes, and learning and optimization. Second, we propose a scientific autonomy ladder inspired by staged autonomy in engineering systems, categorizing agents into four levels: L1 assistive or fixed workflows, L2 adaptive computational agents, L3 feedback-aware physical experiment agents, and L4 scientific-agenda agents. Together, these two perspectives establish a comprehensive framework for comparing existing molecular LLM agents, identifying missing capabilities and deployment risks, and guiding the design, evaluation, and deployment of future agents in molecular discovery workflows.

---


### 284. [Bridge Damage Detection from Low-Light UAV Imagery via Degradation-Aware Mixture-of-Experts Enhancement](https://arxiv.org/abs/2608.23136)

**<font color=#1a73e8>作者：</font>** Hu Wang, Hongxu Pu, Zhiqi Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Poor illumination obscures small, low-contrast defects in UAV bridge imagery, reducing the reliability and operational flexibility of automated inspection. This paper investigates whether degradation-aware image restoration can improve bridge damage detection under low-light conditions and transfer from synthetic degradations to real inspection scenes. We propose DaL- MoE, a detector-agnostic restoration front end trained with an ISP-aware low-light synthesis pipeline and equipped with degradation-aware guidance estimation and complementary experts for noise suppression, color adjustment, and structural-detail recovery. On paired synthetic data, DaL-MoE achieves 23.12 dB PSNR and 0.8482 SSIM, increasing YOLOv11m box mAP50 from 0.3097 to 0.4923 and mask mAP50 from 0.2281 to 0.3529. On real low-light UAV imagery without paired normal-light references, sim-to-real evaluation shows improved defect visibility and more complete detections than direct inference on raw low-light inputs. Future work will develop low-light-aware bridge damage detectors with stronger cross-scene generalization across bridge sites, imaging conditions, and illumination levels.

---


### 285. [A Simulator-Grounded Framework For Constructing Verifiable Muscle-Grounded QA From 3D Tongue Meshes](https://arxiv.org/abs/2608.23137)

**<font color=#1a73e8>作者：</font>** Seungho Eum, Unsang Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing articulatory corpora based on real-time MRI and electromagnetic articulography capture tongue shape and motion but do not provide traceable labels for the muscle-driven process that generated an observed configuration. We introduce a simulator-grounded data-construction framework and instantiate it as 3DTongueQA. Controlled 11-dimensional muscle activations are mapped to fixed-topology tongue meshes with the ArtiSynth Badin finite-element model, converted into structured biomechanical records, and rendered as deterministic QA on muscle state, geometry, and target-directed change. We screen 295,157 configurations, retain 295,115 valid meshes, and construct 891,156 QA records per language. Language naturalization changes only surface form and is verified against the source records; English and Korean instantiations demonstrate construction-level portability. A swappable SpiralNet++--Qwen3-8B baseline reaches 62.9 $\pm$ 9.2 Muscle EM, 74.0 $\pm$ 0.2 Value Accuracy, and 65.9 $\pm$ 4.7 Direction EM, while mismatching the paired mesh reduces Muscle EM to 2.2; a dataset-leakage-controlled anchor-held-out model retains 80.4--98.6\% of the full-inventory scores on unseen anchors. Task-specific structured readouts further reach 88.7 $\pm$ 0.7 Muscle EM and 93.3 $\pm$ 1.0 Direction EM. These complementary results show that the constructed supervision supports both efficient structured prediction and heterogeneous natural-language QA rather than being tied to a particular decoder architecture.

---


### 286. [An end-to-end-trained vision-language model for native-language prostate pathology report generation](https://arxiv.org/abs/2608.23143)

**<font color=#1a73e8>作者：</font>** Christian Grashei, Fabian Gülhan, Maximilian Legnar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prostate cancer is among the most frequently diagnosed malignancies worldwide, and structured reporting of each biopsy core burdens pathologists. Existing tools frame this as classification, leaving pathologists to assemble coherent reports, while many slide-level vision-language models rely on English-centric encoders that transfer poorly to other clinical languages. We present a slide-level framework generating prostate biopsy reports that is language-independent by construction: tokenizer and model are trained from scratch, demonstrated here in German. To address paired-data scarcity, an automated pipeline uses a locally deployed large language model to split composite reports into core-specific image-text pairs, yielding 17,344 pairs from 2,402 historical cases without manual annotation. Evaluated for clinical attributes rather than linguistic similarity, the model achieves 96.2% F1 for malignancy detection and 65.2% for Gleason grading, competitive with an FDA-cleared classifier. Grading is further validated on three external cohorts with latent-space augmentation. Institutions can thus train native-language reporting models on their own archives.

---


### 287. [Activation-Weighted Seeded Residual Coding for Low-Bit LLM Weight Repair](https://arxiv.org/abs/2608.23144)

**<font color=#1a73e8>作者：</font>** Zehao Liu, Chuangchuang Fang, Yang Ren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit weight quantization saves storage but leaves errors that degrade language-model quality. We introduce Activation-Weighted Seeded Residual Coding (AWSRC), a compact repair codec for an existing quantization backbone. Given a reconstructed weight $W_0$, AWSRC encodes the residual $W-W_0$ using deterministic seed-generated bases. The sidecar stores seed selectors, low-bit coefficients, and scales rather than an explicit codebook. Activation statistics prioritize errors that affect layer outputs. On Qwen2.5-3B-Instruct, adding 0.162 scope-bits/weight to an INT4 RTN backbone closes 88.2%, 78.9%, and 71.3% of the matched PPL, KL, and accuracy gaps to BF16. Repairing a matched strong low-bit backbone also improves all measured quality metrics. With a matched 49.25 MB sidecar, about 0.8% of the BF16 model-weight payload, AWSRC gives the best perplexity and mean task accuracy among sparse, low-rank, and vector-quantized codecs.

---


### 288. [First Demonstration of Multi-Agent LLM System for Million-Scale Optical Link Management in Global Production AIDCs](https://arxiv.org/abs/2608.23145)

**<font color=#1a73e8>作者：</font>** Jingyi Su, Yihao Zhang, Dianxuan Fu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We present the first LLM-powered multi-agent system for autonomous fault management across millions of optical links in production AIDCs. Refined via SFT and continuous memory evolution, it achieves 97.7% F1 and over 60% fault-incident reduction, outperforming SOTA LLMs on a ten-week field data evaluation.

---


### 289. [Language Chain in Alignment: Cross-Lingual Ranking Preference Optimization](https://arxiv.org/abs/2608.23149)

**<font color=#1a73e8>作者：</font>** Seungyoon Lee, Minhyuk Kim, Jungseob Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The alignment of Large Language Models heavily relies on English-centric high-quality preference data, which often leads to suboptimal performance in other languages. In this paper, we propose Cross-Lingual Ranking Preference Optimization (CRPO), a novel framework that leverages robust preference knowledge from English to facilitate preference alignment in the target language. We design a hierarchical structure within parallel preference pairs across the target language and English to jointly optimize intra- and inter-lingual preferences, thereby enhancing language adaptation and output quality. Building on the LambdaLoss framework, CRPO goes beyond the binary comparison based optimization by providing a relative ranking signal across multiple candidate responses. Our experiments across five languages with varying resource scales demonstrate that CRPO consistently outperforms standard approaches in both instruction-following and knowledge utilization capability. Notably, the robust performance gains observed across various weighting schemes further validate the empirical effectiveness of our hierarchical design in a multilingual setup. Furthermore, our findings highlight that CRPO significantly improves both reward margins and the log-probability of desirable responses, contributing to a more stable preference manifold for cross-lingual alignment.

---


### 290. [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](https://arxiv.org/abs/2608.23152)

**<font color=#1a73e8>作者：</font>** Sujoy Nath, Aswini Kumar, Tanmoy Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, stereotype, conspiracy, dehumanizing, non-factual), and then maps it to a targeted counterspeech style. To facilitate FIRE, we curate FactualCS, a novel dataset of $4,784$ instances that provides the annotations regarding hate categories, reasoning traces, and evidence mappings, which are critical elements for grounded generation that are missing in prior work. A comprehensive evaluation across $28$ baseline configurations demonstrates that FIRE significantly surpasses existing methods, despite using compact agents ($<$2B). FIRE achieves a $\sim$ $12 \%$ and $\sim$ $11 \%$ improvements in factual and category-specific accuracy respectively, while simultaneously reducing toxicity by $\sim$ $11 \%$ relative to the strongest baselines. Further human evaluation confirms that responses generated by FIRE are significantly preferred over the strongest baselines, underscoring its effectiveness for real-world deployment. These findings show that decomposing the underlying intent of hate speech is essential for generating safe, effective, and contextually precise counterspeech.

---


### 291. [Accelerating Diffusion Language Models via Structured Suffix Modeling](https://arxiv.org/abs/2608.23167)

**<font color=#1a73e8>作者：</font>** Zifeng Cheng, Keda Li, Zhiwei Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) exhibit strong parallel decoding capabilities by denoising multiple tokens in a single generation step. However, this parallelism comes with substantial computational overhead, as each step requires interactions with all suffix tokens. Existing methods typically reduce this cost by retaining only a local suffix window as a substitute for the full suffix. Despite their effectiveness, these methods overlook the structural heterogeneity across suffix regions and re-initialize suffix tokens with identical representations at each timestep. To this end, we propose a structured suffix modeling method for efficient DLM inference. Specifically, we divide the suffix into three regions, i.e., the local, middle, and tail regions, and retain different numbers of suffix tokens in each region according to their structural roles. Moreover, we incorporate the decoding results from the previous step into the suffix token representations at the current step, allowing them to carry evolving denoising information across generation steps. Notably, our method is training-free and orthogonal to several existing acceleration techniques, such as parallel decoding strategies and KV cache. Empirical results across multiple benchmarks on three DLMs demonstrate that our method can further accelerate DLM inference and improve performance in most cases. In particular, in long-sequence inference, our method achieves up to a \(72.81\times\) speedup when combined with other acceleration techniques. Our code is available at this https URL.

---


### 292. [CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension](https://arxiv.org/abs/2608.23172)

**<font color=#1a73e8>作者：</font>** Abhilash Nandy, Rahul Seetharaman, Aman Bansal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale vision-language models (VLMs) have demonstrated remarkable versatility across a wide range of multimodal tasks. However, understanding humor remains challenging because humorous content often depends on subtle interactions among entities, events, context, and implicit relationships across image and text modalities. These interactions can involve complex chains of reasoning that are difficult to capture through conventional prompting or linear chain-of-thought reasoning. In this work, we propose CaRGo-T (Causal Reasoning Graph-of-Thought), a reasoning framework that represents the causal and contextual relationships underlying multimodal humor as a lightweight graph-based reasoning structure. The graph is serialized into a code-based representation generated by a VLM, which can subsequently be interpreted by the same or a different VLM to produce the final prediction in zero-shot or in-context learning settings. We evaluate CaRGo-T on humor understanding and humor detection across four datasets spanning diverse forms of comedic content, including satire, sarcasm, and memes. Experiments with state-of-the-art commercial and open-source VLMs show that CaRGo-T consistently improves performance over existing reasoning-based baselines, achieving gains of approximately 1-20% on humor understanding and 1-3% on humor detection. Further analysis using mutual information indicates that the reasoning representations produced by CaRGo-T contain more information relevant to the target output than those generated by baseline reasoning approaches. Code is available at this https URL.

---


### 293. [CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild](https://arxiv.org/abs/2608.23181)

**<font color=#1a73e8>作者：</font>** Jian Yang, Haau-Sing Li, Shawn Guo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) continue to advance in coding capabilities, their potential in cybersecurity has drawn increasing research attention, with closed-source LLMs (e.g., Mythos) delivering advanced cybersecurity capabilities. However, existing open-source efforts remain limited: frontier open-weight models do not provide reproducible cybersecurity training solutions, open-source training solutions focus on isolated tasks and lack scalable agentic data, and scaling agentic rollouts requires strong domain priors. In this work, we introduce \textbf{CyberFactory}, a unified open-source framework that connects data construction, trajectory synthesis, and model training across proof-of-concept (PoC) generation, vulnerability patching, and cybersecurity question answering (CyberQA). CyberFactory transforms public vulnerability artifacts, including CVEs from the wild, into executable and verifiable task instances. It further uses a reusable vulnerability-analysis skill to guide the teacher through source inspection, problem solving with domain prior, and evidence-based validation. The resulting supervision is agentic: the model interacts with tools and target environments and revises its solutions according to execution feedback. Using these trajectories, we train and release \modelname\footnote{\emph{Aegis} is, in Greek mythology, the protective shield of Zeus and Athena; the name reflects the model's defensive, security-oriented purpose.}, which internalizes the skill-guided procedure without requiring the skill at inference time. On CyberGym, \modelname reaches 52.4% Pass@1 under a one-hour budget, improving over its Qwen~3.5 base model by +22.8 points and outperforming the evaluated general-purpose backbones under the same scaffold.

---


### 294. [Towards Automated Cyber Threat Intelligence Elicitation in Underground Forums](https://arxiv.org/abs/2608.23185)

**<font color=#1a73e8>作者：</font>** Lorenzo Bossi, Federico Saccani, Francesco Panebianco 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber threat intelligence from underground forums has traditionally relied on passive monitoring. However, as users have become more aware of large-scale data collection, valuable intelligence has become increasingly rare in open forums, often migrating instead to private or harder-to-reach spaces, making passive approaches inadequate. Building on the intuition that relevant information can be obtained through active elicitation, this paper presents DarkBot, to the best of our knowledge, the first multi-agent LLM-based system for active CTI elicitation in underground forums. DarkBot decomposes the interaction task across eleven specialized agents organized into three functional blocks: engagement gating for relevance and safety filtering, context-aware question generation driven by MITRE ATT&CK tactics, and linguistic style adaptation to better align with real forum users. In a controlled evaluation across 100 CrimeBB conversations, the system recovered 72.8% of the validated MITRE ATT&CK techniques present in the original discussions by observing only the initial post at the start of each interaction, and it consistently outperformed a monolithic baseline. The proposed layered safety design contained all injected jailbreak attempts at the pipeline level. These results were further supported by real-world experiments: in a prospective matched deployment, threads assigned to DarkBot accumulated an average of 3.85 more CTI entities than their controls over seven days, and across 104 live forum conversations, the system elicited CTI-relevant disclosures without observed account suspensions, moderator interventions, or explicit accusations of automated participation.

---


### 295. [LongWoF-Bench: Evaluating EvoMap Genes for Verifiable Long-Workflow Tasks](https://arxiv.org/abs/2608.23200)

**<font color=#1a73e8>作者：</font>** Xiao Zhang, Qumeng Sun, Jihao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly expected to execute complex workflows whose success depends on maintaining interdependent constraints and producing artifacts that satisfy strict end-to-end verification. Yet successful execution experience is typically lost after a single run, forcing subsequent models to rediscover strategies and failure modes from scratch. We study whether such experience can instead be externalized and reused through EvoMap, where verifier-confirmed execution trajectories are consolidated into structured Gene. To evaluate this setting, we introduce the Long-Workflow Benchmark (LongWoF-Bench), comprising 778 machine-verifiable tasks across code generation, agent-environment synthesis, mathematical reasoning, and rule following. On the 252 tasks with verifier-confirmed Opus trajectories, evolved EvoMap Gene outperform Skill across all seven evaluated models by 8.7-15.5 percentage points, with the gains extending to consumer models from different model families. In contrast, reference-distilled Gene do not exhibit the same advantage, indicating that compact representation alone is insufficient and that Gene utility is closely associated with verified experience provenance. For Claude Opus, Gene reuse also completes 39 more tasks than Skill while reducing solve-time token consumption by 9.9%. Together, these results show that verified execution experience can be retained and shared as a reusable external resource, enabling models to improve long-workflow completion without repeatedly paying the full cost of experience discovery.

---


### 296. [Cognitive Profiling of LRMs' Reasoning Traces Using Bloom's Taxonomy](https://arxiv.org/abs/2608.23205)

**<font color=#1a73e8>作者：</font>** Maria-Eleni Zoumpoulidi, Georgios Paraskevopoulos, Alexandros Potamianos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have revolutionized reasoning in LLMs, and the increasing public availability of reasoning traces creates valuable opportunities to study model behavior not only at the surface level but also at the granularity of individual reasoning steps. However, understanding the types of thinking employed during reasoning - which offers critical insights into models' reasoning patterns and enables actionable applications - remains underexplored. To address this gap, we introduce a framework for automatic annotation of reasoning steps through the lens of Bloom's Taxonomy, which classifies thinking into six cognitive levels, such as Remembering, Applying and Evaluating. Using this framework, we perform a large-scale analysis across models and datasets, revealing both similarities and differences in thinking patterns across models and tasks. Moreover, we demonstrate that thinking-type information derived from reasoning traces correlates with correctness, paving the way for improved reasoning. Our findings establish a fine-grained framework for analyzing thinking patterns in LRMs and provide actionable insights for enhancing reasoning quality.

---


### 297. [MLLM-Assisted Audio VOS: A 3rd Place Report for the MeViS-Audio Track, 8th LSVOS Challenge](https://arxiv.org/abs/2608.23234)

**<font color=#1a73e8>作者：</font>** Liangtao Shi, Jinxia Xie, Xiantao Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this technical report, we present a training-free framework for audio-guided video object segmentation, which integrates Multimodal Large Language Models (MLLMs) with SAM-based segmentation models. We decompose the task into several stages and identify suitable foundation models for each stage. Without introducing additional model training or task-specific fine-tuning, our approach leverages the strong multimodal reasoning capabilities of MLLMs to model text-visual correspondence and employs SAM-based models for accurate object mask generation. The proposed framework demonstrates the effectiveness of leveraging foundation models for audio-guided video segmentation and achieves competitive performance in the MeViS-Audio Track of the 8th LSVOS Challenge.

---


### 298. [A Multi-Domain and Multi-Task Generative Framework with Explicit Task and Domain Conditioning for Cross-Domain Event Extraction](https://arxiv.org/abs/2608.23235)

**<font color=#1a73e8>作者：</font>** Siting Liang, Omar Adjali, Daniel Sonntag  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Event extraction aims to identify event triggers, classify event types, and extract arguments to construct structured event representations. Despite strong in-domain performance, developing models that generalize robustly across domains remains challenging due to variations in contextual expressions and event schemas. Prior unified and multi-task approaches improve in-domain accuracy but exhibit limited flexibility when applied to unseen domains. Even large language model-based methods that provide full event ontologies at inference time often underperform compared to smaller, task-specific fine-tuned models. We propose a unified multi-domain and multi-task training framework that models heterogeneous event schemas within a single model. Our approach introduces domain conditioning signals, jointly with task-specific prompts, enabling dynamic adaptation to dataset-specific schemas without requiring complete event label sets at inference time. The framework supports both pipeline and end-to-end extraction settings, facilitating efficient task- and domain-level transfer. Experiments on diverse event extraction benchmarks demonstrate that our method achieves competitive performance, strong cross-domain generalization, and practical scalability, while preserving domain-specific precision.

---


### 299. [Credal Large Language Models for Semantic Commitment under Uncertainty](https://arxiv.org/abs/2608.23244)

**<font color=#1a73e8>作者：</font>** Shireen Kudukkil Manchingal, Sofiia Nikolenko, Fabio Cuzzolin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often produce fluent but incorrect answers with unwarranted confidence. A central limitation is that standard LLMs represent uncertainty through a single predictive distribution, conflating epistemic ignorance with genuine ambiguity. We introduce Credal Large Language Models (CLLMs): an ensemble of LoRA adapters induces a credal set whose lower and upper probabilities expose the spread of plausible predictive distributions rather than collapsing to a single softmax output. From this representation we derive two complementary commitment scores. Credal Token Commitment (CTC) is a token-space score that combines lower-bound support, credal width, and intersection entropy, computed without additional generation. Semantic Commitment Consistency (SCC) extends commitment to semantic space using sampled completions, with SCC-Gap measuring the mismatch between token-level and semantic-level support. We evaluate hallucination detection, calibration, selective prediction, and reasoning on Gemma-2-9B, Llama-3.1-8B, and Qwen2.5-7B across OpenBookQA, CoQA, TriviaQA, and ARC-Challenge. CLLM is the best method on QA accuracy at competitive expected calibration error, and CTC tracks the best hallucination AUROC within 1.5 pp on most settings without additional generation. On selective prediction at 80% coverage, CLLM with SCC reaches 99.0% accuracy on OpenBookQA, and on ARC-Challenge CLLM with Csem confidence achieves <= 0.6% ECE across the three backbones.

---


### 300. [Future Querying: Can LLMs Serve as Implicit Medical World Models?](https://arxiv.org/abs/2608.23248)

**<font color=#1a73e8>作者：</font>** Siri Willems, James Butterworth, Lore Goetschalckx 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional clinical prediction models rely on task-specific pipelines and curated, structured data, which scale poorly and underutilize unstructured text. To address this, we introduce future querying, a paradigm that probes whether large language models (LLMs) can function as implicit medical world models by evaluating their ability to answer time-indexed clinical queries about a patient's future. Our framework operates on unstructured clinical documentation using endpoint-agnostic training, enabling a single model to answer diverse clinical queries over patient trajectories without manual feature engineering or task-specific retraining. We show that small, locally fine-tuned open-weight models can match or approach larger proprietary systems, making the framework suitable for privacy-preserving, on-premise deployment. Evaluated on a new synthetic medical reports dataset and real ICU notes from the MIMIC-IV dataset, our results provide encouraging evidence that LLMs can capture aspects of clinical dynamics.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-363](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

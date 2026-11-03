# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 101. [Designing Informative Actions: Action Construction for Long-Horizon Research Agents](https://arxiv.org/abs/2611.00773)

**<font color=#1a73e8>作者：</font>** Alkut Arxidin, Shaoning Zeng, Jianhang Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents support automated scientific research by connecting literature analysis and planning with experimentation. Evaluating which action an agent selects does not establish which experiment its instruction specifies, because omitted interventions or replication counts leave consequential choices to the executor. We introduce a reading-set framework for evaluating action construction under a common cost rule. Across 30 synthetic states, complete-design requests increase affordable efficiency by 465.98% and 327.91% relative to the action-name baseline in the two model families, respectively. An author-constructed research-action evaluation dataset provides 60 scenarios for complementary judgment evaluation. On this dataset, the scenario-level information-per-cost measure has a mean within-scenario correlation of 0.733 with judgments from 18 human participants. The framework makes design specification and execution ambiguity measurable, providing a reproducible basis for assessing how research agents translate scientific intent into informative, budget-feasible experiments.

---


### 102. [Decision-Centric Research: A Calibrated Decision Model and Benchmark for Scientific Agents](https://arxiv.org/abs/2611.00774)

**<font color=#1a73e8>作者：</font>** Shaoning Zeng, Wen Huang, Xinzhong Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific agents make consequential choices about evidence, next actions and research strategy, but choices embedded in generated text are difficult to evaluate independently. Decision-Centric Research (DCR) is introduced to make individual choices the common unit of supervision, prediction and evaluation through typed predictions over an explicit Research State. DCR defines 24 decision types, ten of which are instantiated in the Research Decision Benchmark (RD-Bench) of 2,000 rule-generated cases. The Decision-Centric Research Model (DCRM) shares a candidate-token readout across types to produce answers and option probabilities in one forward pass. Under a held-out research-domain split, a 0.6B DCRM (state-aware) achieves 89.4% Top-1 accuracy, compared with 27.8% for DCRM (question-only) trained with the same recipe and 36.4% for DeepSeek-V4.1-Flash. All 30 type-seed comparisons against DCRM (question-only) are significant after Holm correction. After held-out calibration, the resulting prediction sets contain a mean of 1.515 candidates at 97.1% empirical label coverage, reducing mean set size by 57.4% relative to DCRM (question-only) at similar coverage. These results establish a compact state-aware decision layer with accurate typed prediction and an inspectable uncertainty interface.

---


### 103. [Who Schedules Agent Memory? A Sidecar Approach to Long-Horizon Tasks](https://arxiv.org/abs/2611.00779)

**<font color=#1a73e8>作者：</font>** Qijia Zhuang, Rui Liu, Yuxiang Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language model agents increasingly undertake complex, long-horizon tasks, memory has become an important component for supporting sustained decision-making and action. Existing methods primarily focus on memory storage, updating, and retrieval, but often overlook how memory scheduling affects task execution: the main agent must identify memory needs, initiate retrieval, and wait for results while advancing the task, increasing both scheduling burden and execution time. To address this problem, we propose MemSidecar, which decouples memory scheduling from task execution through two independently selectable modes. Hooks directly delivers bound memory to the main agent when execution events match predefined conditions. Foresight uses an independent agent to predict potential queries, retrieve results in parallel, and store them in a cache, delivering matching and valid results when actual requests arrive. Hooks and Foresight achieve scores of 41.23% and 44.34% on MCP-Persona, respectively, while effectively reducing execution costs and latency and improving the efficiency of long-horizon agent execution.

---


### 104. [One Offset, Two Directions: Baseline Adjustment via Subgroup Offsets](https://arxiv.org/abs/2611.00782)

**<font color=#1a73e8>作者：</font>** Jiaying Zhou, Jiachen Liu, Qingchao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) estimates advantages against the within-prompt mean reward, a baseline shared across the group. In practice, rollouts within a prompt are not always homogeneous, differing in their solution strategies and reasoning trajectories, along which they may group into subgroups. We further find that these heterogeneous subgroups may exhibit distinct reward distributions. The global baseline, however, collapses them onto a single credit axis, where the credit reflects neither a rollout's standing within its subgroup nor the subgroup's standing relative to the rest. We therefore study how to adjust the baseline when the rollouts of a prompt fall into heterogeneous subgroups. We define the \emph{subgroup offset} as the deviation of a subgroup mean from the global mean, and shift the baseline along it by a single signed coefficient $\lambda$. The sign of $\lambda$ yields two opposing directions: \emph{Alignment} ($\lambda{>}0$) adds the offset to the baseline, drawing credit toward a rollout's relative position within its subgroup; \emph{Contrast} ($\lambda{<}0$) subtracts it, drawing a rollout's credit toward the relative quality of the subgroup it belongs to. The adjustment acts on the baseline alone, leaving the reward signal and the optimization objective unchanged. In this work, we induce subgroups from strategies, grouping rollouts that share a strategy into the same subgroup. We evaluate both directions on Qwen3-8B-Base and Olmo3-7B-Base across four competition-level math benchmarks, against a $\lambda{=}0$ anchor that shares the same strategy-conditioned sampling and differs only in the baseline. Against this anchor each direction yields modest but consistent gains in multi-sample coverage, with Contrast the stronger of the two.

---


### 105. [A Tool in the Forward Pass: Frozen Tape Modules as Layers of a Small Language Model](https://arxiv.org/abs/2611.00783)

**<font color=#1a73e8>作者：</font>** Michael Granitzer, Saber Zerhoudi, Mohammad Al-Maamari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Calling a tool through generated text adds decoding steps, even when the computation itself is short. We study an alternative: a small neural module that runs inside a language model's forward pass. A learned writer turns hidden states into a symbolic tape, a short sequence of discrete symbols that encodes the computation. The module, trained separately and then frozen, reduces the tape to a result, and a learned reader returns that result to the model. We evaluate arithmetic and object tracking in gemma-3-1b-it. With a writer trained on labelled tapes, the layer answers all 750 items of BIG-Bench Hard's tracking shuffled objects correctly. At seven people it needs about 1/10 of the GPU kernel time of a text-tool baseline that uses the same host model and exact code, with accuracy 1.00 against 0.99. The writer can also be learned from answers alone, guided by a hand-written copying prior, but less reliably: 5 of 6 runs succeed in the 1B host and 2 of 4 in the 4B host. Two independently trained layers keep their task accuracy when attached to one model, and a learned gate keeps them silent on the tested general-text and look-alike prompts. The results support a narrow use case: a bounded computation that returns one symbol can avoid the decoding cost of a textual tool call. Extracting the right input reliably, and deciding when to act, remain the main open problems.

---


### 106. [ConstraintMatch: Compositional Image-Text Matching through Constrained Regional Evidence Selection](https://arxiv.org/abs/2611.00784)

**<font color=#1a73e8>作者：</font>** Yuhong Zhou, Yubo Gao, Xiangbo Shu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Local image--text matching can find strong evidence for individual concepts yet favor captions with incorrect attribute--entity bindings. We introduce ConstraintMatch, a training-free inference method that turns entity-level regional consistency into an explicit matching cost. On the same frozen condition--region similarity matrix, it compares independent crop selection for each category and attribute with a shared crop choice within each entity. Their gap quantifies the score advantage obtained by relaxing the shared-region constraint. Spatial references from the same image calibrate this gap by keeping category evidence fixed while jointly shifting an entity's attribute maps. Per-entity clipping prevents cancellation across residuals, and the scaled mean cost is subtracted from global similarity. ConstraintMatch uses pooled embeddings, and spatial calibration requires no additional encoder calls. With parameters fixed per backbone across tasks, ConstraintMatch improves over global matching by 7.70 percentage points on full ARO Attribute and 5.63 points on held-out SugarCrepe++ attribute swaps, averaged across Qwen~2B and CORE~2B. Against SGI adapted to the same 13-crop budget, the respective gains are 4.85 and 3.51 points. Controlled analyses distinguish the effects of shared-region matching and candidate score calibration. The results establish entity-level evidence selection as a practical scoring principle for compositional multimodal retrieval.

---


### 107. [CheXPoT: Post-Hoc Visual Verification and Correction of VLM-Generated Radiology Reports](https://arxiv.org/abs/2611.00785)

**<font color=#1a73e8>作者：</font>** Joey Guo, Rayan Ansari, Alaa Youssef  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown promise for chest radiograph report generation, but adoption remains limited because of hallucinated findings that are not grounded in the image. Correcting these hallucinations and improving overall report quality remains a significant challenge. Prior work has addressed this problem by refining models with reinforcement learning, preference optimization, or chain-of-thought supervision, often at substantial compute cost. To address this gap, we introduce CheXPoT, a program-of-thought (PoT) framework that verifies each generated finding against image features and removes those it cannot ground. CheXPoT decomposes generated reports into predicates with RadGraph and an LLM, grounds these predicates against a DenseNet-121 and Grad-CAM visual evidence table, executes PoT verification code, and rewrites reports after removing unsupported predicates. On a 4,145-image held-out split, CheXPoT yields statistically significant precision gains on 8 of 14 CheXpert classes and F1 gains on 5, with no significant decreases in either metric. CheXPoT lifts micro-average precision from 19.2% (MedGemma-4B) to 46.8% (MedGemma-4B + CheXPoT) and micro-average F1 from 23.0% to 49.4%, absolute gains of 27.6% and 26.4% respectively. We also tested CheXPoT on other VLM report generators. On LLaVA-Med, CheXPoT lifts micro-average precision from 4.5% to 17.7% and micro-average F1 from 6.3% to 19.4%. On MAIRA-2, CheXPoT lifts micro-average precision from 15.6% to 42.1% and micro-average F1 from 21.0% to 45.3%. Our results suggest that inexpensive post-hoc visual verification may improve VLM trustworthiness by correcting unsupported findings from generated reports. CheXPoT lays a foundation for tools that help validate VLM-generated radiology reports and reduce unsupported findings. These innovations may subsequently help increase trust and adoption of VLM tools in Medicine.

---


### 108. [PhoneValue-Bench: A Multimodal Benchmark and Datasets for Consumer Smartphone Recommerce Valuation](https://arxiv.org/abs/2611.00791)

**<font color=#1a73e8>作者：</font>** Zihan Deng, Jun Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As consumer smartphone recommerce scales, buyers must quote binding repurchase prices from seller-uploaded multi-view photos and diagnostic screenshots before devices reach the warehouse. Accurate remote valuation requires fusing noisy cosmetic evidence with identity, battery, lock, and channel risk from screenshots and staff forms, since an error in any modality changes both grade and payout. However, existing multimodal resources mainly target general VLM competence, screen reading, or factory defect detection, and largely overlook staff-aligned trade-in fields, dual appearance/staff ground truth, and executable valuation scorecards. This gap stems from two challenges: (1) the lack of large-scale real trade-in data with audited dual annotations and a compact ranking benchmark kept separate from training labels, and (2) the need to jointly reason over unordered multi-view cosmetics and diagnostic screens under operational deduction rules. To address these challenges, we propose PhoneValue-Bench, a dual-GT evaluation suite with tier-gated scorecards, together with PhoneValue-Corpus, a matched weakly labeled training set of over twenty thousand orders and hundreds of thousands of captioned images. We further present ValueAgent, a staged perception-fusion-valuation reference pipeline aligned with production inspection, plus an executable public scorer and submission schema. Experiments show that ValueAgent reaches a measured 84.1/100 on Bench-Full, with 97.0 appearance fill and 54.1 staff-field fill, establishing a practical dual-GT benchmark for multimodal recommerce valuation.

---


### 109. [AI Data Analysis: A New Approach - Multi-engine Joint State Data Analysis](https://arxiv.org/abs/2611.00807)

**<font color=#1a73e8>作者：</font>** Jean Ye  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI data analysis today is three fragmented worlds: LLMs understand semantics but cannot compute; BI aggregates precisely but is stateless; ML processes large-scale data on a stateful kernel but lacks semantics. This paper proposes a combination mechanism, named Multi-engine Joint State Data Analysis, that fills a still-open gap - the multi-engine joint context: the data context is embedded into LLM conversational analysis, where the LLM serves only as the semantic, reasoning, and orchestration layer (not computation) and connects four engines through the 1M context window - Python and R ML kernels, SQL over relational databases, Cypher over graph databases - yielding two multiplications, "semantics and precise computation" and "relational and graph", under enterprise-grade governance. The novelty is a four-dimensional coordinate system: horizontal (engine kinds), vertical (state flow - the watershed), spatial (business generalization), temporal (iterative convergence); a deterministic grounding method (one-shot injection of this http URL + this http URL, M+S) carries the spatial and temporal dimensions. Empirically, all four dimensions are substantiated: horizontally, four engines are quantified - SQL, Cypher (96.5% on CypherBench movie), ML in Python and R (TabReD weather); vertically, state flows across engines and grounding is reused across kernels; spatially, SQL generalizes across three business databases - AdventureWorks 91.3%, financial 95.3%, formula_1 94.6% (average), about 20-23 points above single-shot SOTA 74.45%; temporally, accuracy converges monotonically as notes accumulate. The core invariant - the separation of semantics from computation plus a cross-data-domain persistent context - does not expire as LLMs and agents evolve or engine forms change.

---


### 110. [VCoT-SQL: Enhancing Text-to-SQL Generation through Dual Chain-of-Thought Validation Training](https://arxiv.org/abs/2611.00815)

**<font color=#1a73e8>作者：</font>** Rui Zhang, Yujia Su, Ruixuan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-source LLMs provide a flexible alternative to closed-source models for Text-to-SQL but still struggle with complex queries. Finetuning with chain-of-thought (CoT) data improves reasoning, yet standard datasets lack CoT annotations, requiring synthetic generation. Existing synthesis methods only verify the final answer, allowing flawed reasoning steps to corrupt the training data. We propose VCoT-SQL, a framework that improves Text-to-SQL generation through intermediate-step validated CoT supervision and a dedicated SQL validator, which enables small open-source models to outperform frontier closed-source models. VCoT-SQL trains two complementary models on curated reasoning traces: an SQL generator using clause-level CoT templates where reasoning steps are verified via execution and schema alignment checks, and an SQL validator using diagnostic CoT templates to detect syntactic, semantic, and type level errors. We further design a hierarchical schema filtering pipeline that integrates and refines complementary retrieval strategies to distill relevant database elements. VCoT-SQL achieves 66.82% execution accuracy on challenging dataset BIRD dev and 86.8% on Spider test, improving the base 7B model by 7% on BIRD. Notably, our CoT synthesis relies on 7B models yet outperforms methods that use 72B-scale or even proprietary closed source teachers for data generation, demonstrating that rigorous step-level validation can be more effective than scaling up teacher model size. Our dataset and code are available at this https URL.

---


### 111. [AdKnob: Ad Intensity Control and Labeling for LLM-Native Advertising](https://arxiv.org/abs/2611.00822)

**<font color=#1a73e8>作者：</font>** Woo Jae Kim, Seongho Keum, Joonsung Jeon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-native advertising has emerged as a viable monetization channel as LLM service providers seek sustainable revenue streams. However, integrating native ads into LLM responses introduces two largely understudied challenges: (1) controlling ad intensity -- how prominently advertising content appears -- and (2) ad labeling -- identifying which segments of the generated text constitute advertising. We propose AdKnob, a framework jointly addressing both challenges. For ad intensity control, we introduce new ad control tokens without pretrained semantic associations and align the model via direct preference optimization to generate ads at each desired level. For ad labeling, we propose an attention rollout-based attribution mechanism that identifies ad segments by tracing their attribution to input ad-related tokens, requiring no additional inference cost. We further construct MI-KnobSet, the first multi-level ad intensity preference dataset for LLM-native ads. Experiments across six LLMs and human evaluations show that AdKnob achieves uniformly spaced ad intensities where baselines collapse to a narrow range, achieves the highest ad labeling accuracy while being over 500x faster than the strongest baseline, and is preferred over baselines by human evaluators up to 89.6% of the time.

---


### 112. [Answer Correction with Verifiable Rewards: A Gemma-Family Study of Multi-View Driving QA](https://arxiv.org/abs/2611.00828)

**<font color=#1a73e8>作者：</font>** T N Rickesh, Pranav Vinodh, Sowmya Kamath S  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-camera driving question answering provides a discrete test of vision-language models, but post-training gains can reflect changed selected answers or improved answer extraction. We investigate this distinction within the Gemma model family using archived, task-linked WaymoQA evaluations. A zero-shot diagnostic on 5,519 test questions spans effective-small, mixture-of-experts, unified, and dense checkpoints, with serving differences disclosed rather than interpreted as architecture effects. The strongest controlled evidence is a matched-harness Gemma-4-12B base/GRPO pair: accuracy rises from 73.78% to 75.43%, a gain of 1.65 percentage points with a scene-cluster bootstrap interval of [+0.84, +2.41]. There are 215 improvements and 124 regressions; 213 improvements start from an extractable but incorrect base answer, and only two recover previously unextractable responses. Crossing correctness with extraction state shows why correct noncompliant outputs cannot be counted as prediction errors. Category counts reveal a critical safety asymmetry: routine perception gains (+5.93 pp) mask a regression in safety-critical hazard prediction (-1.82 pp), demonstrating that unweighted outcome rewards can trade off rare edge cases for aggregate accuracy. Reward saturation describes sampled training dynamics rather than an architectural ceiling. A separate archived Gemma-31B thinking comparison yields no detected average improvement, with uncertainty that does not establish equivalence. These results support a modest answer-selection gain for the recorded tuning configuration and a reproducible diagnostic accounting, without attributing corrected labels to specific grounding mechanisms or claiming superiority over matched supervised tuning.

---


### 113. [Fewer Tokens, More Answers: Verifiable-Reward Tuning of an Ornith-Style VLM for Multi-View Driving QA](https://arxiv.org/abs/2611.00833)

**<font color=#1a73e8>作者：</font>** T N Rickesh, Pranav Vinodh, Sowmya Kamath S  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning-enabled model derivatives must turn intermediate deliberation into a usable answer within a deployment budget. We study that transition in an Ornith checkpoint adapted to multi-camera driving question answering with verifiable rewards. Paired archived outputs show that, on a selected 400-question development screen with a 256-token cap, GRPO increases answer extraction from 78.25% to 90.25% and accuracy from 55.50% to 63.75%. Of 39 wrong-to-correct transitions, 33 begin with an unextractable base response. The base's 87 unextractable responses all reach the token cap. Checkpoint-verified reconstruction on those same questions gives a much smaller first-pass accuracy gain at 512 tokens: +0.75 percentage points, versus +8.25 at 256. A later answer-cued continuation is analyzed separately; it helps the base more and narrows the adapter difference. On the full 2,511-question development set, this recovery-enabled pipeline reduces mean generated tokens from 108.6 to 47.1, while the paired accuracy interval includes zero gain. We frame these findings as adaptation of answer delivery under finite budgets, with explicit selection and provenance limits. Ornith's self-scaffolding lineage and newer reasoning-enabled derivatives such as Bonsai motivate the problem, but our measured results concern Ornith alone and do not establish a shared architectural mechanism or cross-model transfer.

---


### 114. [Can Agentic AI Undermine Its Own Assurance Loop? Closed-Loop Dependency Assurance for Cognitive Network Digital Twins](https://arxiv.org/abs/2611.00838)

**<font color=#1a73e8>作者：</font>** Ahmed Hussain, Konstantinos Kalogiannis, Salahuddin Salahuddin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic Artificial Intelligence (AI) and Network Digital Twins (NDTs) are increasingly combined to form Cognitive Digital Twins (CDTs) that translate operational intents into network changes and support closed-loop management. However, a network change may achieve its intended objective while disrupting the monitoring or recovery mechanisms needed for subsequent decisions. For example, a service may be rerouted while its latency-monitoring traffic continues along the original path, producing measurements that no longer reflect the service's performance. We propose Closed-Loop Dependency Assurance (CLDA), an assurance mechanism that augments agentic AI-enabled NDTs with dependency-aware validation. In our framework, an agentic AI planner generates and refines network plans, while the NDT evaluates the projected network outcomes of these plans. CLDA extends this analysis using a Loop Dependency Graph (LDG) that connects service requirements to monitoring mechanisms, forwarding paths, failure domains, and recovery prerequisites. CLDA projects candidate actions onto these dependencies, checks intermediate states of multistep plans, and supports deterministic make-before-break repairs using temporary monitoring mechanisms. Unlike the Large Language Model (LLM)-based planner, CLDA uses explicit, deterministic rules for assurance decisions and repair. We evaluate CLDA through controlled reconfigurations, a 240-trial LLM-based planning campaign, and live network execution. A separate synthetic study examines deterministic assurance scalability across network models representing up to 1,024 routers.

---


### 115. [Toward Counterfactual Learning for Selective Re-Examination in Agentic Visual Search](https://arxiv.org/abs/2611.00848)

**<font color=#1a73e8>作者：</font>** Ao Chen, Shengchao Chen, Yan Luximon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual search over high-resolution images requires a vision-language model (VLM) not only to determine where to inspect, but also whether another observation is warranted before committing to an answer. Existing prompting, demonstrations, and outcome-based reinforcement learning can encourage re-examination, yet do not directly supervise whether it is beneficial at a particular search state. We introduce ReSee, a benchmark of re-examination decisions comprising 3,227 visual-search trajectories and 8,827 explicit commit-or-re-examine decisions, with counterfactual adjudication that distinguishes states where additional inspection is warranted from those where commitment is preferable. Building on this formulation, we propose CARE (Counterfactual Advantage for Re-Examination), a decision-level reinforcement learning method that compares paired continuations under commit and re-examine verdicts from the same search state. Their cost-aware return difference estimates the counterfactual value of an additional observation and is assigned only to the corresponding verdict tokens, providing localized credit for whether search should continue. Experiments expose limited re-examination selectivity in existing VLMs and show that CARE significantly improves accuracy and decision selectivity over GRPO across two backbones, with higher accuracy and fewer visual requests on six unseen OOD benchmarks.

---


### 116. [ShiftRAG: Bypassing the Textual Bottleneck via Decoupled Learning and Continuous Soft Tokens](https://arxiv.org/abs/2611.00871)

**<font color=#1a73e8>作者：</font>** Youmin Ko, Jihong Jeong, Hyunjoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite advances in retrieval-augmented generation (RAG), suppressing hallucinations during complex reasoning remains a persistent challenge. We identify that existing RAG pipelines suffer from a textual bottleneck: by passing only raw text to the generator, they discard discriminative signals of the retriever. Furthermore, recent attempts to unify retrieval and generation within a single LLM induce severe objective conflict and exacerbate the rank collapse of decoder-only architectures, degrading performance on both tasks. To address these limitations, we introduce ShiftRAG, a decoupled RAG framework that employs a single LLM backbone but isolates discriminative retrieval learning from autoregressive generation. To bridge these decoupled modes, we project retrieval alignments into continuous soft tokens, establishing a high-bandwidth interface that infuses the generator with retrieval-side signals. Concurrently, our soft orthogonality objective mitigates rank collapse, while layer-wise relevance dynamics preserve the fine-grained latent space required for highly discriminative evidence separation. Extensive evaluations demonstrate that ShiftRAG significantly improves retrieval and question answering performance over state-of-the-art baselines. ShiftRAG preserves foundational capabilities of the backbone while maintaining a favorable efficiency-performance trade-off on general text encoding and generative tasks.

---


### 117. [What Breaks and What Comes Back: Capability Damage and Recovery in Depth-Pruned Small Language Models](https://arxiv.org/abs/2611.00877)

**<font color=#1a73e8>作者：</font>** Piyush Dhoka, Vedant Pandhare, Varun Inamdar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depth pruning removes whole Transformer blocks to make a language model smaller and faster, but the damage is not spread evenly across what the model can do, and a short fine-tuning run, called healing, decides what comes back. We measure this for small models used as agents. Four instruction-tuned models of 1.2-1.7B parameters (Llama-3.2-1B, Qwen2.5-1.5B, SmolLM2-1.7B and OLMo-2-1B) are pruned and healed, and six capabilities are tracked: structured output, function calling, instruction following, mathematical reasoning, safety refusal and knowledge. Three results hold across the families. First, function calling and math collapse in every model (retention 0.00-0.07 of the unpruned score), and the order in which capabilities break agrees closely across the four (Kendall's W = 0.92; 0.62 after correcting for chance floors). Second, which parameters are trained matters as much as which data: fully tuning the last three blocks instead of adding low-rank adapters to all blocks costs up to 0.18 in capped mean retention on three families, and one 300k-token pilot per scope detects this. Third, we test a planner that allocates a 1M-token healing budget from 21 short pilot heals. At a fixed budget it raises the weakest capability on two families, although only one of these gains survives a test that also resamples training seeds. Once its 3.48M pilot tokens are counted, uniform healing with the same total number of training tokens matches or beats every planned variant on every family and retains math significantly better on three of them in an item-level test (on one when seeds are also resampled). Healing longer is a strong and simple baseline that planned recovery must beat. Code, per-item predictions and every result are public.

---


### 118. [Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand](https://arxiv.org/abs/2611.00883)

**<font color=#1a73e8>作者：</font>** George Ling, Shanshan Zhong, Lijin Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmark compression reduces the often prohibitive time and cost of model evaluation by evaluating models on a small benchmark subset that closely matches full-benchmark results. To quantify estimation error, we derive an accurate analytical approximation to the error distribution when estimating full-benchmark scores from a subset, showing that most subsets yield small errors, while a few produce much larger errors, resulting in a long-tailed distribution. This means random sampling alone can achieve surprisingly strong performance with high probability, but remains unstable due to rare large errors. We further show that this instability is inherent to modern foundation models and persists even as more models are evaluated. Based on these findings, we introduce BestRand, a stable and low-cost benchmark compression method that preserves the efficiency of random sampling while substantially reducing its high-error tail. We validate BestRand on 70+ text, multimodal, and agent benchmarks, and further extend it to VLA evaluation. Compared with competitive methods, BestRand reduces high-error risk by 50.2% and estimation error by 16.4% on average, while requiring only 51.3% of the construction cost. It further reduces OOD estimation error by 21.8% on average across score-range, model-family, and temporal shifts. Together, our theory provides practical guidance for understanding and predicting the accuracy and reliability of benchmark compression, while BestRand enables stable and accurate compression at low cost. The code and data are publicly available onhttps://github.com/George-Ling3/BestRand.

---


### 119. [Learning to Group and Order: Cross-Instance Self-Supervised RL for Vision-Centric MLLMs](https://arxiv.org/abs/2611.00892)

**<font color=#1a73e8>作者：</font>** Songming Yang, Hong-Tao Yu, Xiu-Shen Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training has become an important paradigm for improving multimodal large language models (MLLMs), especially with automatically verifiable rewards. Self-supervised visual pretext tasks provide such rewards without human annotations. However, existing methods mainly exploit within-instance structure, offering limited supervision for cross-instance discrimination and fine-grained comparison. We introduce Group-and-Order Self-Supervised Reinforcement Learning (GO-SSL), a cross-instance jigsaw framework for vision-centric MLLM post-training. Given two visual instances, GO-SSL mixes their local elements and trains the model to group them by instance of origin while recovering the order within each group, coupling instance-level comparison with spatial, temporal, or geometric structure recovery. This paired formulation turns the same unlabeled data into richer verifiable supervision through diverse pairings, shuffles, and a random-to-hard curriculum. We instantiate GO-SSL mainly on cross-image jigsaw tasks and further extend it to 3D depth and video temporal ordering. Across diverse benchmarks, GO-SSL consistently improves over the base MLLM and prior self-supervised post-training baselines, with clear gains in fine-grained perception and spatial understanding. Further evaluations across model scales and families support its generality. These results suggest that cross-instance comparison provides a useful self-supervised RL signal for improving transferable visual understanding in MLLMs. Code is available at this https URL.

---


### 120. [S1CogBench: What System One Decision Models Can and Cannot Do on Cognitive Experiments](https://arxiv.org/abs/2611.00911)

**<font color=#1a73e8>作者：</font>** Dengzhe Hou, Kazunori D Yamada  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are no longer used only to generate text. Software also asks them for decisions, in routing, guardrails, and automated gates. System One decision models, also called typed decision models, such as Jev and Laya, return one fast decision over the legal options, leaving no text to inspect. However, a fast, well-formed decision does not show that the model used the evidence. Cognitive experiments can test this, because they vary task demands and measure how behavior changes, yet existing cognitive benchmarks evaluate language and multimodal models. We introduce S1CogBench to ask what these models can and cannot do on 24 cognitive tasks, evaluating five open models and Jev and keeping conditions and scoring apart from disclosed adaptations. We find that decision models vary widely in reliability, acting well does not imply predicting humans, aggregate scores hide how decisions respond to conditions, and speed comes mainly from answering without generation. To our knowledge, S1CogBench is the first benchmark of System One decision models on established cognitive experiments, and it gives a shared test of whether their decisions respond to evidence, feedback, memory load, and future opportunities before software relies on them.

---


### 121. [Solvable dynamics model of in-context learning](https://arxiv.org/abs/2611.00921)

**<font color=#1a73e8>作者：</font>** Ruoran Bai, Haiping Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained Transformer architectures display a surprising in-context learning ability without additional training. How the learning process guides the network to achieve this intriguing capability remains unsolved. In this study, we focus on a single-layer, single-head linear attention model, where empirical risk minimization is defined for learning. Given a finite amount of training examples, we determine the exact solution of network parameter dynamics, which is linked to the training error and generalization error, characterizing how memorization and generalization emerge from learning and how these transitions are related to curvatures of the empirical risk landscape. Furthermore, we calculate a data-dependent free energy, from which the training and generalization errors in the long-time limit of learning dynamics can be well predicted. Our work adds insights toward understanding the mechanism of in-context learning, especially from a learning dynamics perspective.

---


### 122. [Illusion: Safeguarding Topology Confidentiality in LLM Multi-Agent Systems via Behavior-Preserving Obfuscation](https://arxiv.org/abs/2611.00923)

**<font color=#1a73e8>作者：</font>** Yiu-Fai Cheung, Hongzhi Guo, Miao Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The communication topology of Large Language Model Multi-Agent Systems (LLM-MASs) governs how information propagates among agents and encodes critical domain knowledge and expert workflow design. It is valuable intellectual property and plays a decisive role in system utility and safety, yet remains vulnerable to inference attacks that stealthily reconstruct it from agent outputs. Existing defenses detect or mitigate such attacks but do not proactively conceal the topology itself. We propose \textit{Illusion}, a proactive topology obfuscation defense for LLM-MAS. \textit{Illusion} injects fake edges and fake messages to present attackers with a deceptive topology, while selecting low-impact candidates that preserve output-distribution equivalence and task-accuracy non-inferiority. The resulting fake edges are designed to be indistinguishable from genuine messages under black-box observation. Extensive experiments show that \textit{Illusion} reduces edge-level F1 from over 0.87 to 0.62 and graph similarity from over 0.94 to 0.71. It also largely preserves output distributions and task performance, and its fake edges resist both similarity-based and LLM-judge filtering, even under adaptive pruning.

---


### 123. [UI-UG 2: Advancing Mobile UI Understanding and Generation with Fine-Grained Supervision and Reinforcement Learning](https://arxiv.org/abs/2611.00926)

**<font color=#1a73e8>作者：</font>** Hao Yang, Shuoyang Liu, Xiaoyu Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile UI understanding and generation require both fine-grained component perception and reliable structured synthesis. Inspired by the unified direction introduced by UI-UG, we present UI-UG 2, a compact 4B-parameter multimodal large language model (MLLM) that advances mobile UI Understanding and Generation with broader task coverage, a front-end-aligned taxonomy, and online render-aware reinforcement learning. UI-UG 2 constructs a multi-source understanding corpus from RICO, VINS, Android in the Wild, and Android Control, annotated with an 80-category two-level UI taxonomy aligned with front-end component semantics, and pairs it with over 5,000 requirement-screenshot-JSON tuples for progressive structured UI generation through a domain-specific language (DSL). For understanding, UI-UG 2 introduces decomposed rewards for category prediction, OCR fidelity, color recognition, dense grounding, and GUI grounding. Unlike the offline Direct Preference Optimization (DPO)-style generation optimization in UI-UG, UI-UG 2 optimizes generation through end-to-end online Group Relative Policy Optimization (GRPO): sampled DSL outputs are rendered with a Playwright-based server-side pipeline and evaluated using LLM-as-a-Judge and contrastive preference ranking. Experiments show that UI-UG 2 achieves the strongest referring and dense-grounding results among the evaluated models on our 80-category benchmark, and achieves the best composite generation score among compared models at a compact scale (4B). More importantly, we observe a consistent understanding-to-generation transfer: adding fine-grained UI perception supervision improves generation quality under a fixed training budget, suggesting that component-level semantics provide a shared representational foundation for both tasks.

---


### 124. [Labadain-MedQA: A Tetun Medical QA Dataset for Fine-Tuning and Evaluating Large Language Models](https://arxiv.org/abs/2611.00935)

**<font color=#1a73e8>作者：</font>** Gabriel de Jesus, Sérgio Nunes  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Advances in large language models (LLMs) have created opportunities for cross-lingual transfer of medical knowledge from high-resource to low-resource languages to support access to healthcare information. However, medical question-answering (QA) datasets for fine-tuning and evaluating LLMs remain scarce for Tetun. To address this gap, we translated MedAlpaca's Medical Flashcards and WikiDoc Patient Information collections into Tetun using Gemini 2.5 Flash, producing 39,077 medical QA pairs. Translation quality was assessed on 50 randomly sampled QA pairs (100 documents) using automatic metrics against human reference translations and evaluations by two native Tetun-speaking healthcare professionals, focusing on medical accuracy and Tetun fluency. Human translations achieved higher mean ratings than LLM-generated translations for both criteria (4.43/5 vs. 4.02/5), with statistically significant differences (Wilcoxon signed-rank test, p < 0.001). To assess downstream utility, we fine-tuned Gemma and Llama variants on the translated MedAlpaca dataset using parameter-efficient fine-tuning (PEFT) and evaluated them on 325 Tetun-translated United States Medical Licensing Examination multiple-choice questions. Gemma 4 12B fine-tuned using QLoRA achieved relative improvements in mean accuracy of 10.79% with 4-bit NormalFloat (NF4) inference and 10.42% after merging the LoRA adapters into the BF16 base model, compared with the corresponding base models. These results highlight the viability of automatic dataset translation for Tetun medical QA and the effectiveness of PEFT in enhancing model performance. The datasets, models, and evaluation resources are accessible at this https URL to support reproducible research on Tetun medical QA and facilitate machine translation, cross lingual, and multilingual research.

---


### 125. [HieraNTP: Structured Risk Representations for Time-Series Anomaly Detection via Hierarchical Next-Token Prediction](https://arxiv.org/abs/2611.00945)

**<font color=#1a73e8>作者：</font>** Yujie Li, Zezhi Shao, Boyu Diao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series anomaly detection commonly converts deviations from learned temporal regularities into anomaly scores. This practice can conflate violations of temporal regularity with task-specific anomaly judgments: the same deviation may be anomalous under one task definition and benign under another. Aggregating heterogeneous deviations into a single score before task-specific adaptation can obscure the evidence needed to distinguish these cases. We introduce HieraNTP, a Hierarchical Next-Token Prediction framework that separates self-supervised predictive modeling from task-specific risk interpretation. HieraNTP pretrains a hierarchical tokenizer and a causal next-token predictor to capture temporal regularities at multiple scales. It then organizes prediction discrepancies into a structured risk representation, preserving complementary evidence across temporal scales in token, local-statistic, and observation spaces. A task-adaptive detector uses anomaly labels to select and combine this evidence for the target task. Across anomaly detection benchmarks, HieraNTP improves VUS-PR by 12.0% on TSB-AD-U and 15.5% on TSB-AD-M relative to the strongest baselines, and achieves the highest composite score on both TAB tracks, with controlled comparisons supporting the value of retaining distinct evidence. Our code is available at this https URL.

---


### 126. [Self-Refining Prompt Induction for Streaming Text-to-SQL](https://arxiv.org/abs/2611.00960)

**<font color=#1a73e8>作者：</font>** Gaetano Rossiello, Alfio Gliozzo, Nandana Mihindukulasooriya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL assistants for streaming engines must handle dialect-specific types, windowing rules, and temporal semantics, including constructs poorly handled by generic prompts. We present Self-Refining Prompt Induction (SRPI), an offline method that converts generation failures into reusable dialect instructions while keeping model weights fixed. A Refiner revises the Generator's prompt using reference-conditioned feedback from three LLM judges; a sampled regression guard checks earlier successes, and a separate Compressor reduces prompt length. Inference uses the frozen prompt without retrieval or query repair. We evaluate cross-domain and cross-model transfer on Confluent Cloud Flink SQL using a controlled synthetic workload seeded by 30 expert-written examples, with 335 induction examples and 257 questions from held-out domains. The same induced prompt improves mean judge scores across seven Generators by 7.1-19.2 percentage points, including an increase from 85.3% to 97.5% for the induction model. A separate compression study reduces prompt length by 52.7% with a 0.19-percentage-point score decrease. An assistant using the induced prompt is in early access, with initial user feedback to inform subsequent refinement.

---


### 127. [A Token Is Not a Unit of Difficulty: Segmentation Controls Where Adaptive Computation Goes Inside a Word](https://arxiv.org/abs/2611.00983)

**<font color=#1a73e8>作者：</font>** Dipto Sumit, Mahima Mahzabin Sandria, Farig Sadeque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Early-exit language models decide for each token how much computation to spend, usually by stopping once the prediction is confident. Yet a token is not a fixed unit: tokenizers cut words into different numbers of pieces in different languages. We ask where inside a word such a policy spends its budget. In Qwen3, along two adaptive axes (the timesteps of a spiking conversion and the layers of the original Transformer), confidence stopping gives the continuation pieces of a word less computation than its first piece in English, German, and Turkish, but more in Bangla. Segmentation drives this. Re-segmenting the same parallel passages with BPE-dropout shifts the gap by up to eight exits on both axes, small models trained under two tokenizers shift Bangla's gap by six exits, and BLOOM and mGPT, which split Bangla less finely, give it the English pattern. Characters per token do not predict the gap across languages; within-word surprisal explains 75% of its variance. A learned stopping head beats confidence stopping by 7 to 8 points, but gains less than one point over the best mix of fixed exits at equal cost, and sometimes loses. All results come from offline analysis, not measured speedups.

---


### 128. [Pulse: Long-Horizon Tasks Need Streaming Personalization](https://arxiv.org/abs/2611.00988)

**<font color=#1a73e8>作者：</font>** Qijia Zhuang, Jialiang Liang, Yuxiang Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly undertake complex, long-horizon tasks that benefit from sustained personalized support through long-term memory. Existing memory-augmented methods retrieve and use memory primarily from the initial request, with limited awareness of ongoing execution and emerging personalization needs. Agents may therefore overlook user preferences and project constraints during multistep tasks. We propose Pulse, a streaming personalization method for long-horizon tasks. An independent, lightweight memory agent continuously monitors execution, identifies emerging personalization needs and potential preference conflicts, and uses user and project memories to provide targeted interventions at appropriate stages. Reinforcement learning optimizes when and how the memory agent intervenes, improving the timeliness and accuracy of personalized support. Pulse scores 71.9% on $\pi$-Bench and 46.4% on MCP-Persona, achieving the highest overall scores among the compared methods on both datasets while improving task execution efficiency.

---


### 129. [GURU: A Hierarchical Neuro-Symbolic Multi-Agent System for Verification-Aware Automation of Mission-Critical Digital Engineering and Operations](https://arxiv.org/abs/2611.01001)

**<font color=#1a73e8>作者：</font>** Allan Grosvenor, Anton Zemlyansky, Abdul Wahab 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An AI can find a safe action faster than any human, but it must never decide what counts as safe. We present GURU, a hierarchical neuro-symbolic multi-agent system for mission-critical digital engineering and operations, built on one partition of authority: learned models propose, rank, and accelerate; a symbolic rules engine checks every consequential action against hard limits before it executes; and validated physics confirms and decides. GURU runs a workflow as a closed control loop, with Navigation, Action, and Planning agents sharing one Common Internal Language and one training factory. Nuclear, aviation, and national-security guidance now requires this pattern; a harnessed language model keeps the model at the center, GURU puts a validated reference there. In computational fluid dynamics, the workflow raised the converged-simulation rate on unseen aircraft geometries from under 1 percent to 74 percent over 100 single-attempt cases, ran 54 live cases to Mach 6 on three facilities, and an ablation put the symbolic layer at 13 points of boundary-layer capture. Knowledge-graph retrieval and role adapters raised ParaView control success from 55 to 75 percent. In space domain awareness, where a language model cannot be trusted to decide, a frozen self-supervised world model under validated propagation scored highest of five methods at conjunction risk, including fully fine-tuned language models, with several-times-lower seed variance: the trustworthy design gives up nothing in accuracy, and the recipe transferred to reactor anomaly detection. A radar-to-avoidance debris pipeline was demonstrated in stages on a 2026 reentry; the hierarchy coordinates simulated teams of 200 aircraft. Training scaled near-linearly past 1,000 Aurora nodes and ran at 8,000. The approach extends to a control-grade microreactor digital twin with validated physics, not a learned model, as the safety basis.

---


### 130. [Leap-VLA: High-Rate Robot Control from a Low-Rate VLM Backbone](https://arxiv.org/abs/2611.01011)

**<font color=#1a73e8>作者：</font>** Lin Yang, Yunjie Shen, Zheyu Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models re-encode the full observation through a multi-billion-parameter vision-language model (VLM) at every control step, even though scene semantics evolve at roughly 1 Hz while reactive control requires 20-50 Hz. We present a VLA that decouples the two: a VLM runs as a low-frequency semantic anchor whose cached context is reused across control steps, while a flow-matching action expert operates at high frequency, consuming the cached semantics with a fresh, low-latency visual stream from a compact encoder pretrained on robot video with masked reconstruction, optical flow, and depth. The measured age $\tau$ of the cache conditions the expert through adaptive layer normalization. Reusing the cache makes the policy a function of its age, and training covers that function explicitly: cache ages sampled from real episode history, plus an age-ramped pixel corruption that erases the stale snapshot the way deployed staleness corrupts content. On the asynchronous deployment stack, the recipe closes most of the staleness gap: on LIBERO-Spatial, 61.4% to 95.5% at a 2 s semantic refresh (95.9% at 1 s, within 1.6 points of the frequency-matched anchor); averaged over the four LIBERO suites, the deployed policy holds 95.2% at a 1 s refresh and 94.5% at 2 s against a 96.3% matched anchor. A forward-only chunk-boundary correction (soft-nudge), an autograd-free reformulation of real-time-chunking guidance, carries per-control-step re-planning without loss (97.1%) at zero added latency. The same lens exposes a second defect: under an instruction-scene mismatch the policy keeps manipulating the scene, and a chain-of-thought verdict gate trained on zero-cost negative episodes freezes execution exactly on mismatched instructions without hurting feasible success.

---


### 131. [Jet-QSparse: Accelerating Agentic LLM Inference with 4-Bit Sparse Attention](https://arxiv.org/abs/2611.01022)

**<font color=#1a73e8>作者：</font>** Haozhan Tang, Hao Kang, Meng Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon reasoning and agentic workloads strain KV-cache capacity and decode attention throughput. We present Jet-QSparse, a training-free method that combines compact NVFP4 cache storage with native FP4 query-key computation on Blackwell tensor cores. A dense scan scores the full key history and selects 128-token blocks for sparse FP16 value aggregation with FP32 accumulation, preserving higher precision in the output-forming step while enabling contiguous tile loads. Calibrated key centering and at most two BF16 pages per sequence and layer address quantization error; FP8 prefill uses a temporary arena while the persistent cache is packed directly from BF16 activations. Across four hybrid LLMs, a budget of 128 blocks per KV head shows no detected accuracy loss on the evaluated mathematical reasoning, coding, and agentic benchmarks, although some smaller budgets incur losses. With 64 blocks, Qwen3.8-27B achieves a $1.94\times$ end-to-end decode speedup over dense BF16 at 128K context and batch size 16 on one GB300, and the measured Qwen KV pools provide $2.58$-$2.76\times$ BF16's token capacity.

---


### 132. [Constraint Dependency Graph Retrieval for Compliance Detection on Long SKILL Documents](https://arxiv.org/abs/2611.01042)

**<font color=#1a73e8>作者：</font>** Shuaitao Zhao, Feng Ni, Lichao Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents carry out business operations under enterprise documents we refer to as SKILL documents, which take the form of standard operating procedures (SOPs) that state the conditions to verify and the actions to take before an operation proceeds. Long, densely cross-referenced SKILL documents exceed the context budget of small deployed auditors. Similarity-based retrieval then brings in irrelevant rules while omitting mandatory prerequisites, and the two-stage audit policy provides no trainable signal for the retrieval stage. We present SkillCDG, a compliance detection framework that reformulates each SKILL document as a constraint dependency graph, shifting rule retrieval from similarity-based matching to closure-based selection under the deployment's context budget. Each atomic rule is anchored to its source text span as a graph node, and mandatory prerequisite relations form the sole edge type. Policy-generated retrieval keywords activate seed rules, whose dependency closure yields a compact and conditionally complete rule context within that budget. The same graph also supports a joint optimization scheme. The retrieval stage is trained with group-relative policy optimization using a verifiable reward that combines output-format validity with downstream verdict correctness, with closure non-emptiness serving as a validity gate, while selective on-policy distillation concentrates teacher supervision on high-entropy reasoning tokens, with verdict and termination tokens always included, to improve verdict accuracy. Experiments on three enterprise datasets and two public benchmarks show that SkillCDG improves accuracy and F1 over the full-document and retrieval-based baselines.

---


### 133. [Temperature, Not Knowledge: What Recursive Self-Training and Its Remedies Do to a Language Model's Confidence](https://arxiv.org/abs/2611.01059)

**<font color=#1a73e8>作者：</font>** Dipto Sumit, Syeda Fabiayee Jahan, Farig Sadeque  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-training can collapse language models, and many proposed remedies target overconfidence, yet their effects on confidence are rarely measured. We study a five-round self-training loop on Qwen3-1.7B, using three seeds per compared method, and distinguish confidence temperature (drift from a calibrated starting point) from discrimination (ranking correct answers above incorrect ones). Accuracy and overall discrimination remain nearly unchanged, but confidence sharpens and the most confident answers become less reliable. Matching predictive entropy to the calibrated starting model each round recalibrates nearly as well as label-based temperature fitting, at both 1.7B and 8B. Sharpening is not inherent to self-training: exact samples from a model's distribution have zero expected gradient. Instead, most drift comes from fitting each generated answer twice, with top-p truncation contributing the rest; removing both keeps entropy on generated outputs flat. Remedies affect the two properties differently: truncated cross-entropy, an entropy bonus, and single-pass training preserve temperature without improving discrimination, while focal loss and multi-sample targets improve discrimination but cause underconfidence. Reference-data mixing also overshoots. Pairing a ranking-improving loss with label-free recalibration achieves both.

---


### 134. [Multi-Turn Semantic Caching for Low-Cost LLM Serving](https://arxiv.org/abs/2611.01077)

**<font color=#1a73e8>作者：</font>** Baran Atalar, Selly Beyene, Xutong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic caching lowers the cost of serving large language models (LLMs) by reusing stored responses for similar requests. In multi-turn conversations, whether a cached response is acceptable depends on both conversations' histories, which embedding similarity of requests and histories predicts poorly (AUC 0.62--0.74 on five workloads). We therefore learn the \emph{reuse risk}, the probability that a cached response is unacceptable, from judge feedback, and choose a budgeted set of conversation states to cache by weighing the generation cost a reuse avoids against a price for unacceptable reuse. We propose CUCB-SC-MT, which learns a cache from logged conversations with a suboptimality guarantee, and CLCB-LS-MT, which learns online and has $\tilde O(\sqrt N)$ regret over $N$ requests when conversation states recur. On math-tutoring (SocraTeach) and movie-ticketing (Taskmaster-3) conversations, both achieve lower loss than prior semantic caching approaches: ContextCache, multi-turn variants of ElastiCache and vCache, and single-turn semantic caching at every cache budget. With 1,000 cache entries, CLCB-LS-MT avoids 35--41\% of the generation cost through acceptable reuses, against at most 22--25\% for the baselines, and lowers estimated serving latency by 19--35\%.

---


### 135. [Is That Clear? The Impacts of Clarifying Questions on Human-LLM Interaction](https://arxiv.org/abs/2611.01087)

**<font color=#1a73e8>作者：</font>** Chengbo Zheng, Yujie Zheng, Qian Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM assistants increasingly ask clarifying questions (CQs) to elicit preferences and tailor recommendations. Although prior work emphasizes improvements in answer quality and user experience, how CQs shape users' subsequent engagement and reliance remains unclear. We conducted a controlled experiment (N=180) across six everyday decision scenarios, comparing human-LLM interaction with and without CQs. We further manipulated whether responses violated explicit constraints and whether violations occurred in the sub-decisions the CQs addressed, while preserving elicited preferences. CQs increased perceived understanding and satisfaction, yet participants spent less time reviewing and evaluating responses and accepted more responses unchanged, including erroneous ones. Within the CQ condition, participants more often accepted responses containing CQ-adjacent violations than nonadjacent violations. These findings demonstrate that LLM's proactive CQs shape subsequent engagement and reliance with preference elicitation. We discuss implications for designing and evaluating proactive assistants that support continued user scrutiny of answers alongside personalization.

---


### 136. [Scute: Exact Batched Serving for PEFT Adapters Beyond LoRA](https://arxiv.org/abs/2611.01089)

**<font color=#1a73e8>作者：</font>** Thomas Walker, Richard Baraniuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing serving systems for large language models batch requests for many different LoRA adapters on one GPU. However, these systems reject adapters from other parameter-efficient fine-tuning (PEFT) methods such as DoRA, (IA), VeRA and OFT. One solution to this is to convert these adapters to LoRA, but this induces a significant memory and accuracy cost. Instead, we show that, under some modifications, a batched LoRA kernel can serve all of these methods exactly and efficiently. We achieve this by writing each method in one normal form, a LoRA computation with six slots for an adapter's own vectors and matrices. Some slots can merge into an adapter's weights at load time; the others remain live and induce a cost. We give ways to efficiently pay this cost and predict it from a zero-parameter byte model. We package this system, Scute, and build it on top of vLLM. Scute serves all five methods, coming as checkpoints from the Hugging Face PEFT library, in one batch, and it matches that library with a mean error of at most 1.5% of each adapter's effect. Under a burst of requests on an RTX A6000, a mix of these methods takes 5-17% more decode time than the same number of LoRA adapters. Furthermore, using Scute, the same GPU can serve 64 to 1024 (IA) and VeRA adapters at 1.5x to at least 2.5x the request rate of their LoRA conversions.

---


### 137. [The Blind Spots of Detection: Adversarial Perturbation Attacks against Watchdogs in Distributed LLM Inference](https://arxiv.org/abs/2611.01097)

**<font color=#1a73e8>作者：</font>** Siu Wai Shi, Xiaochen Zhu, Xinjian Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralizing large language model (LLM) inference across untrusted Web nodes requires robust verification to ensure computational integrity. Existing activation-based verification and detection mechanisms validate intermediate outputs against reference values, permitting bounded numerical deviations to accommodate benign cross-hardware discrepancies. However, a critical security question remains: what can a malicious worker achieve while operating within these tolerance bounds?
In this work, we introduce Hush-Up, a stealthy availability attack against distributed LLM inference, where a single malicious worker halts generation while evading attribution. The attacker first profiles its local execution to model an empirical bound of benign hardware errors. Using this error bound as a feasibility constraint, the attacker optimizes an adversarial perturbation on its output activations to maximize the final-layer probability of the end-of-sequence (EOS) token, i.e., to hush up the model. Across diverse models and benchmarks, Hush-Up effectively forces premature generation termination and collapses model capabilities. Furthermore, the attack hushes up the watchdogs themselves: existing defenses often fail to detect the sabotage entirely or falsely attribute the amplified downstream anomalies to honest workers. Our findings expose a fundamental gap between local numerical verification and end-to-end accountability: perturbations too small to indict a worker locally can nevertheless be powerful enough to break distributed inference globally.

---


### 138. [CogRSI: Evolving and Auditing Cognitive Reasoning Strategies](https://arxiv.org/abs/2611.01113)

**<font color=#1a73e8>作者：</font>** Yandan zheng, Haoran Luo, Xinliang Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can a language model learn better ways to reason about other people's minds by improving its own strategies, and are the strategies it learns actually right? We study this with cogrsi. A grounded reader marks who saw each event in a story and uses a short written principle to settle disagreements between its readings. With a principle written by experts, it beats self-consistency at the same token cost. A self-improvement loop then writes the principle itself. It keeps an update only if accuracy rises by a calibrated margin, and in one variant only if it also passes counterfactual test pairs. The learned principles transfer: on 800 BigToM pairs that no system had seen, each of them scores higher than the expert principle. We then check what the learned rules actually say. Each rule is translated into code and run on thousands of small stories with known answers. Most of them give a wrong answer in at least one situation they claim to cover, for example by treating a character who is in the room as knowing what happened even while asleep. Accuracy does not reveal which rules are wrong, and the counterfactual test does not fix this. A strategy can help in practice and still be wrong as a rule, so both need checking. Our code and data are publicly available.

---


### 139. [CompSkill: Compiling Execution Experience for Skill Retrieval](https://arxiv.org/abs/2611.01115)

**<font color=#1a73e8>作者：</font>** Qi Shen, Ziyue Zhu, Yongqing Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on skill documents, yet most retrievers rank them by description alone and ignore what earlier executions revealed, even though a relevant skill can hurt execution. We present CompSkill, which indexes skills with learned 512-d keys and compiles matched same-task comparisons into skill offsets and capped key residuals (KeyOpt), so experience changes which document the executor receives, never its text. Under a logistic outcome model with unknown task difficulty, matched comparisons cancel that difficulty and only discordant ones carry information; on support executions, predictions improve with each discordant task. An experience hypergraph keeps each comparison with its executor and document versions, recalls missed skills and grounds a cited review. Compact keys raise SkillRet NDCG@10 from 64.0 to 70.9 at one eighth of the dimension. With one document, CompSkill completes 256 and 260 of 332 ToolQA tasks with GPT-5.6-luna and DeepSeek-V4.1-Flash, respectively, more than every baseline, and stays on par with the strongest baselines on AppWorld and ALFWorld. On 332 newly generated ToolQA tasks, it completes 256 with GPT-5.6-luna, significantly more than BM25, SkillRet-8B, Tool2Vec and RankGPT; over all 844 ToolQA tasks, it completes 24 more than the strongest baseline. Selection matters beyond relevance: pairing the right guide with a same-database sibling instead of another database's guide costs 8 of 96 tasks. Code, models and support data: this https URL

---


### 140. [Zero-Gated Cross-Attention](https://arxiv.org/abs/2611.01116)

**<font color=#1a73e8>作者：</font>** Basavaraj R M, Manav Verma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Injecting non-text modalities into frozen language models often introduces early optimization instability, making it difficult to separate architectural gains from transient training dynamics. We introduce Inductively Gated Cross-Attention (IGCA), a zero-initialized cross-attention bridge that preserves pretrained model behavior at initialization while enabling gradual multimodal conditioning. Integrated across six decoder layers of frozen Falcon-40B, open_llama_30b, and Bloom-7b1 backbones (with 40,404,961,288 trainable adapter parameters used during training), IGCA acts as an exact algebraic no-op at initialization with a maximum output discrepancy of 0.00e+00. Over 59,500 training steps on Falcon-40B, the training loss decreases from 3.9403 to 0.0007 (with final ten step losses of [0.0001, 0.0003, 0.0005, 0.0002, 0.0005, 0.0011, 0.0005, 0.0006, 0.0005, 0.0007]). On held-out evaluation, the best gate-on checkpoint achieves a loss of 2.2201 compared to 4.3469 for the gate-off baseline -- a 48.9% reduction (2.1268 nats) -- while average held-out loss improves from 4.3423 to 2.2498 (1.9075 nats) with a mean gate magnitude of $\vert{}\tanh(\alpha)\vert{} = 0.0713$.

---


### 141. [StreamDuo: A Live Commentator and a Research Agent for Unseen Games](https://arxiv.org/abs/2611.01120)

**<font color=#1a73e8>作者：</font>** Zixian Gao, Penghao Luo, Xiangcheng Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video LLMs can now commentate live gameplay, but they are trained and tested on the same games. We study cross-game streaming commentary, in which a model trained on one game commentates games it has never seen, and find that current commentators transfer their timing but not their knowledge of the game world. We propose StreamDuo, which pairs a trainable commentator with a frozen research agent that reads the wiki of the game being played. When the commentator sees something it cannot name, it sends the current frames, and the research agent returns a few wiki entries two seconds later while the stream continues. We train only the commentator, on a single game, in two stages. Information-gain labels teach it to ask only where an answer would help it say what the human caster said, and on-policy self-distillation from a copy of itself that sees the ideal answer teaches it to use noisy answers. Trained on Baldur's Gate 3 and tested on ten unseen games, StreamDuo raises entity recall from 0.082 to 0.116 over Proact-VL trained on the same data, cuts source-game leakage from 9.9% to 1.0%, and achieves the best timing and the highest judged liveliness and overall quality among streaming models.

---


### 142. [Do Earnings Calls Help Predict Financial Restatements? Evaluating Text Beyond Public Firm Information](https://arxiv.org/abs/2611.01123)

**<font color=#1a73e8>作者：</font>** Ahmet Efe, Shivank Sapra, Bilal Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial restatements correct errors in previously published financial reports. Could managers' language in earnings calls warn of them in advance? Comparing 109 calls that precede restatements with 218 matched control calls, we find that the text predicts restatements but adds no detectable ranking gain beyond public firm information. A text classifier beats chance, largely because of restatements tied to special-purpose acquisition companies, but a model using only public information scores slightly higher. With refitting, the 95% interval for the gain from adding text (-0.05 to 0.11 AUROC) still leaves room for a meaningful benefit. A large language model scores higher, but we show that it names the exact ticker in 66% of masked transcripts, and it was released after the restatements occurred. Our results suggest that finding new warning signs in call text requires a public-information baseline and a check of what a language model already knows.

---


### 143. [What Does a Safety Label Measure? Auditing Situational-Safety Benchmarks for Multimodal LLMs](https://arxiv.org/abs/2611.01125)

**<font color=#1a73e8>作者：</font>** Wayner Barrios, Kenneth Barrios  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Situational-safety benchmarks label each scene SAFE or UNSAFE and score a multimodal large language model (MLLM) against that label, usually by judging its free-form answer, and these scores guide deployment. We ask what such a label measures. A label score can come from the scene, the request or the benchmark's own files. We propose the Benchmark Card, seven measured fields that tell them apart, and fill it for six benchmarks. Only MSSBench chat leaks the label through its image files: image size alone reaches 82.3% accuracy, matching or beating six of seven commercial models. Elsewhere the signal outside the scene comes from design. In MOSSBench the item partition fixes the label, and on HoliSafe the request alone ranks pairs about as well as the scene. On our corrected chat split, the size rule falls to chance. We then introduce the Spot-Stop decomposition, which compares ranking with labelling on pairs of a safe and an unsafe scene. It splits the gap above a label-swap null into three parts: a threshold part, overlap between safe and unsafe scores, and order that holds only within a pair. Most of fourteen open MLLMs rank better than they label, beyond what their AUROC predicts. On chat, one shared threshold repairs a third to a half of the excess, and label-free recentering recovers it on balanced batches. Recentering on unlabelled scenes of the same situation improves ranking on VSCBench for 13 of 14 models.

---


### 144. [What Must Be Done Here? Using a Bounded Application-Security Ontology at the Point of Change](https://arxiv.org/abs/2611.01127)

**<font color=#1a73e8>作者：</font>** Pedro Farinha  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The security guidance that bears on code is real but scattered. It lives across secure-development frameworks, verification standards, controls catalogues, threat taxonomies, and, increasingly, normative regimes such as the EU's NIS2 -- and most of it is written for readers other than the engineer, or the AI assistant, at a point of change. Existing cybersecurity ontologies largely model attacks, indicators, and risk for detection and analysis, not the engineering-practice substance one must act on. This paper presents a use case for an existing bounded application-security ontology, AppSec Core, whose construction and validation are reported separately. We show how it is used. It makes the engineering-actionable fraction of those authorities addressable as a typed working set: the control objectives that apply, the practices that realize them, the mechanisms that implement them, and the evidence artifacts they expect, each traceable to the sources that justify it. We reach that working set from two entry points that recur in practice. Forward, from a code change: a change to authentication middleware scopes to its governing domain slice and returns the obligations the change must satisfy. Inverse, from a normative obligation: "make this NIS2-compliant" resolves a generic legal duty into the concrete engineering obligations it implies across slices, surfacing precisely the fraction of a mostly-governance regulation that lands in code. The same working set is what a human engineer reads and what an LLM-grounded assistant is handed as grounding. The use turns "read every applicable authority" into "satisfy this typed working set", for a code change or a compliance duty alike. The contribution is the demonstrated use; the artefact, its validation, and its governance are companion work.

---


### 145. [HiGenTrans: Hierarchical LLM Knowledge Transfer for Generative Recommendation](https://arxiv.org/abs/2611.01129)

**<font color=#1a73e8>作者：</font>** Zhuohang Jiang, Yuxin Chen, Haohao Qu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative recommendation promises to simplify conventional multi-stage recommender systems by generating item Semantic IDs (SIDs) autoregressively. However, two obstacles limit its effective- ness in industrial settings: interaction-only supervision underuses the semantic knowledge encoded in pretrained language models, while beam-search likelihood ranks token sequences rather than directly estimating item relevance. To address these limitations, we propose HiGenTrans, a three-level framework that introduces LLM knowledge at the input, representation, and decision levels. First, Global Semantic Priming (GSP) adds an LLM-derived user representation to the beginning-of-sequence embedding, provid- ing a semantic prior before SID generation. Second, Hierarchi- cal Representation Transfer (HRT) aligns intermediate LLM representations with depth-matched GenRec layers through mean- centered projections and gated residual connections. Finally, Multi- Signal Decision Calibration (MDC) uses a lightweight mixture- of-experts calibrator to combine semantic relevance, generation confidence, and candidate-set context when reranking beam-search outputs. All semantic features are computed only from the observ- able interaction prefix, preventing target leakage, and can be cached offline. Experiments on three public benchmarks show that HiGen- Trans improves Recall@10 by up to 12.9% and NDCG@10 by up to 33.7% over the strongest baselines. These results demonstrate the value of transferring LLM knowledge at complementary stages of the generative recommendation pipeline.

---


### 146. [Rethinking LLM Pruning via Test-Time Scaling](https://arxiv.org/abs/2611.01133)

**<font color=#1a73e8>作者：</font>** Mingyang Song, Mao Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured pruning reduces the size of large language models, often at the cost of lower accuracy. Whether this decline reflects diminished reasoning capacity or greater difficulty in sampling correct solutions is less clear. We examine this question across expert, FFN and layer pruning on four mathematical and coding benchmarks, comparing original and pruned models through pass@k at matched sampling budgets. Even after substantial pruning, some models match or exceed the original model's reasoning coverage despite lower pass@1, and solve problems left unsolved in the original samples. Retaining broad coverage, however, does not mean that correct solutions remain easy to obtain. Under severe pruning, diverse generated chain-of-thought (CoT) traces can coexist with increased repetition and less reliable generation. As correct answers become harder to sample, the additional attempts can sharply increase total token use even when individual responses become shorter. This separation between coverage and sampling efficiency also clarifies expert-selection gains, as methods with markedly different pass@1 can solve the same problems at large budgets yet require different numbers of attempts to reach a common coverage target. Pruning should therefore be assessed by both the range of problems a model can still solve and the sampling cost of obtaining correct solutions.

---


### 147. [Compile as Hypothesis: A Headroom Typology for Prompt Optimization on Real Reasoning Models](https://arxiv.org/abs/2611.01135)

**<font color=#1a73e8>作者：</font>** Zhengshuai Yang, Changyun Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated prompt compilers search for or rewrite prompts under the implicit assumption that optimization consistently improves downstream task performance. We evaluate this assumption on frontier reasoning models through rigorous paired, same-day measurements. Across four optimizer families (genome search, profile-guided mutation, GEPA, and ESPO) and eight tasks, structured search yields no statistically significant accuracy gains on strong reasoners. However, a discrete structural genome provides essential architectural stability, preventing catastrophic bimodal seed-collapse (where unconstrained search collapses toward the judge floor in 3/5 runs). Through 190-problem evaluations on knowledge-intensive benchmarks, we establish a three-dimensional headroom typology: prompt optimization cannot compensate for intrinsic knowledge deficits or physical token truncation, but successfully resolves protocol and formatting errors. On gpt-6, while free-text reflective search (GEPA) yields a +.14 gain on a task where structured search remains flat, qualitative ablation reveals that ~.035 stems from judge-rubric reconstruction while ~.105 reflects genuine instruction refinement. Our pre-registered AutoAPC-Select deployment gate matches the oracle policy in 5/7 groups and rescues seed-collapse arms with zero regret. Finally, we expose silent backend-mixing in commercial APIs during outage windows and provide automated per-call audit verification tools to ensure empirical evaluation fidelity.

---


### 148. [GSLM2: Multi-Stream Speech Representation Learning and Generative Spoken Language Modeling](https://arxiv.org/abs/2611.01143)

**<font color=#1a73e8>作者：</font>** Yosuke Higuchi, Tom Fizycki, Mahi Luthra 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative spoken language models (SLMs) offer a route to learning linguistic structure purely from speech, yet they lag far behind text-based models in both capability and data scaling efficiency. We identify two bottlenecks underlying this gap: the limited linguistic quality of existing speech units and the reliance on a single stream of discrete units to represent speech. Multiple codebooks are widely used to encode acoustic features but rarely to represent speech semantics. We present GSLM2, which learns and models complementary properties of speech at multiple levels of abstraction. Its encoder, SpidR 2.0, uses self-supervised learning with differentiable prediction heads to induce high-quality discrete units at multiple levels. A multi-stream SLM then jointly models these units using a shared temporal backbone, stream-specific predictors, and an autoregressive head that captures cross-stream dependencies. Across training data sizes and model scales, up to 6M hours and 6.5B parameters, GSLM2 consistently improves linguistic competence while scaling more efficiently with data. As a result, it substantially narrows the gap between spoken and text-based LMs; across read and conversational speech domains, we shrink the gap by about two orders of magnitude on sWuggy, sBLIMP, and tSC, while also outperforming competitive speech-text systems on all three tasks. We open-source the training code and model checkpoints at this https URL.

---


### 149. [CivicBench: A Benchmark and Memory Framework for Web-Based Civic Data Analytics](https://arxiv.org/abs/2611.01145)

**<font color=#1a73e8>作者：</font>** Yangyu Wu, Siru Zhong, Haoyuan Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Municipalities publish service requests, geographic boundaries, weather observations, demographic estimates, and operational guidance through independently maintained Web portals. Civic analysis must combine these sources while preserving their schemas, source links, spatial and temporal scopes, and interpretive limits. Tool-using language agents can perform this integration, but existing task benchmarks rarely test whether a computed claim remains supported by the records used. We present CivicBench, a 400-task benchmark over four cities and two years that materializes civic Web data into frozen bundles for reproducible evaluation. Executable contracts score computation, source linkage, coverage, scope, qualified answers, and refusal when the requested conclusion is not supported. We also introduce Task-State Memory (TSM), which compiles tool observations into typed assertions, reconciles records only within compatible scopes, and retrieves a bounded state organized around unresolved constraints. Across nine completed model pairs, eight yield positive mean-score differences with 95\% semantic-contract-cluster bootstrap intervals excluding zero; the ninth interval crosses zero. The benchmark and memory framework make the records behind a claim inspectable at the point of decision.

---


### 150. [Capacity Planning for Resource-Constrained Clinical LLM Serving](https://arxiv.org/abs/2611.01152)

**<font color=#1a73e8>作者：</font>** Yi Tang, Geoffrey Martin, Yiye Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying large language models (LLMs) under a fixed accelerator budget requires jointly deciding how computational capacity is allocated across model sizes and how incoming requests are routed across that capacity. Although prior work has extensively studied LLM routing and serving efficiency, the relative importance of fleet composition and routing under resource constraints remains less understood. We investigate this question using a controlled four-GPU serving environment with heterogeneous clinical NLP workloads spanning short factual verification, biomedical semantic matching, and long-context clinical summarization. We systematically vary fleet composition, routing policy, and offered load while holding the workload trace and hardware budget fixed. Across 24 configurations, descriptive main-effect shares attribute more variation to fleet composition than to the evaluated routing policies in time to first token, latency, and long-context coverage. All-small fleets provide the best responsiveness and throughput but substantially lower long-context coverage, whereas larger-model capacity improves coverage at the cost of serving efficiency. Heterogeneous fleets provide intermediate operating points but can introduce strong-model bottlenecks when large-model capacity is scarce. In a focused evaluation of this bottleneck, capacity-aware routing reduces mean latency and increases throughput while incurring a small reduction in long-context coverage. Within this measured regime, the results support prioritizing capacity allocation, with routing managing demand within the provisioned capacity.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

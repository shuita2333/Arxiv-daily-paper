# 🧠 大模型相关研究 | 2026年09月25日

> 本类共 **172** 篇论文：已确认 **158** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-172](./part-04.md)

---

### 1. [FedCoT-VQA: A Federated Learning and Unlearning Framework for Chain-of-Thought Planners in VideoQA](https://arxiv.org/abs/2609.26814)

**<font color=#1a73e8>作者：</font>** Rui Lu, Tao Ling, Dan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) planners have emerged as an effective design for VideoQA, where a lightweight planner first generates intermediate reasoning steps to guide temporal evidence selection before answer prediction. This modularity makes CoT-based VideoQA attractive for federated learning, since only the planner side needs collaborative adaptation while the heavy vision-language backbone can remain fixed. However, in decentralized settings, the planner must not only be trained efficiently across heterogeneous clients but also support later client deletion requests. This is challenging because deleted-client influence is reflected both in model parameters and the planner's reasoning-trace behavior. We present FedCoT-VQA, a federated learning and unlearning framework for CoT planners in VideoQA. FedCoT-VQA consists of three modules: planner-side partitioning (PSP), which exposes a compact shared-residual adaptation space for efficient federated training; server-side aggregation (SSA), which aggregates planner-side updates while maintaining a deletion-ready contribution log; and a residual unlearning module (RUM), which approximates the retained-only counterfactual planner through retained-client replay and selective residual correction, without full retraining. We evaluate FedCoT-VQA in terms of federated training utility, federated unlearning utility, forgetting quality, and efficiency. Results show that compared to current federated approaches, FedCoT-VQA preserves strong federated training utility, improving grounding quality by up to 4.45%. After unlearning, it retains high accuracy and achieves a counterfactual gap of only 7.38%.

---


### 2. [Silent Failures in Agent-Tool Interaction: An Audit of ToolUniverse](https://arxiv.org/abs/2609.26836)

**<font color=#1a73e8>作者：</font>** Shreya Gopalan, Devansh Singh, Sundaraparipurnan Narayanan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems are increasingly adopting automated pipelines that integrate multiple tools. While prior research and benchmarks have studied about task success and task completion of these agentic systems, the research about agent to tool interaction, specifically in biology agentic workflow is limited. This study investigates specific failures in agent to tool interaction where a tool invocation appears successful, some or all of the information or functionality from the tool via API/ wrapper is incomplete or missing and there are no communications / notifications to the user or the agent about such missing information. We call this a silent failures as the user or the agents are not aware that such failure has occurred. For the purposes of this study we developed an audit mechanism to identify such silent failures in Agent to tool interaction, by examining 15 scientific tools (and their associated API documentation and tool documentations) integrated within ToolUniverse environment (ToolUniverse serves as our experimental environment rather than the object of the study itself). We structure our study around 7 failure locus characterising where the failure occurs in the chain. We observed 91 failures (manually validated post LLM based candidate discovery and automated testing), most frequent of them being missing data or fields and inconsistencies in search, filtering or ranking criteria. Most of the 91 failures occurred in API layer (51) or wrapper layer (25), with a potential of silent failure amplification downstream. The results show that silent failures originate upstream of the event and propagate downstream into apparently valid scientific outputs. We propose a concept of contextual reliability to handle such failures and suggest mechanisms for testing, disclosing, monitoring, and measuring such failures across the agent-tool interaction pipeline.

---


### 3. [COPE: Continual Personalization of LLMs under Sparse User Feedback via User Embeddings and Self-Evaluation](https://arxiv.org/abs/2609.26853)

**<font color=#1a73e8>作者：</font>** Ruike Cao, Fugen Yao, Liang Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have achieved remarkable results across various benchmarks, their alignment with normative values often results in homogenized responses that fail to address diverse user preferences. Existing training-free methods often occupy valuable context windows through prompt engineering, while training-based methods typically remain static post-training, failing to support the continual optimization required in real-world settings. To address these challenges, we propose COPE (Continual Optimization with Personalized embedding and self-Evaluation), a novel optimization framework tailored for real-world-motivated interaction settings with sparse user feedback. Our framework assigns learnable personalized embeddings to each user and synergistically integrates preference capture, self-evaluation calibration, and personalized response optimization within a single update step. A key innovation of our method is the use of self-evaluation to generate proxy rewards, enabling continuous model updates even when explicit user feedback is unavailable. Experiments show that COPE consistently outperforms strong training-free and training-based baselines under sparse feedback, and remains complementary to Retrieval-Augmented Prompting (RAP). Further analyses confirm COPE's reliable self-evaluation, meaningful preference patterns, stable general capabilities, and robustness under shifting preferences and alternative evaluators.

---


### 4. [SkillApt: Learning When to Activate Agent Skills from Counterfactual Evidence](https://arxiv.org/abs/2609.26863)

**<font color=#1a73e8>作者：</font>** Shuang Guo  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly retrieve reusable Skills and inject them into the active context. However, a retrieved Skill can be relevant yet unnecessary, costly, or even harmful in the current execution state. We present SkillApt, a post-retrieval activation framework that decides whether a retrieved Skill should actually be loaded. SkillApt builds execution evidence from matched WITH/WITHOUT runs and uses outcomes from similar historical states to make a LOAD/ABSTAIN decision for each candidate Skill. On the frozen confirmatory SRA-Bench evaluation, SkillApt-E achieved the same observed accuracy as BM25 Top-1 (0.838 vs. 0.838) while reducing the Skill activation rate from 100% to 31.5% and mean token usage by 74.3%. Further diagnostics show that both Skill utility and the learnability of its activation boundary vary across base models. These results suggest that Skill retrieval and Skill activation should be treated as separate decisions: retrieval identifies which Skill may be relevant, while SkillApt determines whether using it is worthwhile in the current state.

---


### 5. [Marginally Correct Tool Caches Can Reverse Group-Normalized Policy Updates](https://arxiv.org/abs/2609.26866)

**<font color=#1a73e8>作者：</font>** Shivam Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool-result caching reduces repeated execution in agent training, but also couples rollout randomness. We study a two-action model in which independent and shared execution preserve every rollout's conditional reward distribution. Despite this marginal agreement, sharing one stochastic result per group can reverse the expected group-normalized policy update. We derive an exact finite-group expression: against a constant alternative, the shared update follows the probability of winning minus the probability of losing, rather than the difference in expected reward. A Bernoulli specialization yields a wrong-direction region and a non-vanishing update-variance floor as group size grows. Centering without group standard-deviation scaling preserves the expected-return direction in this model, using an existing estimator control. Exhaustive finite sums verify 540 configurations and 3,240 estimator evaluations, with a separate ordered-sequence checker. An implementation audit reproduces the sharing path in a pinned, unmodified TVCache stack using 256 scripted rollouts. These results do not measure language-model training performance or refute TVCache's deterministic-output contract. They establish that marginal output validity alone cannot certify a stochastic cache as training-equivalent.

---


### 6. [Harness as a Language: A Minimalist Agent Framework With Maximal Expressivity](https://arxiv.org/abs/2609.26891)

**<font color=#1a73e8>作者：</font>** Zhening Li, Joshua Liu, Mateja Vukelic 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern language-model agents are built around the \textit{agent loop}, where the LLM is placed in an environment exposing a set of tools, and the LLM has full control over the workflow by alternating between tool calls and observing their output. However, certain workflows currently require additional engineering beyond the agent loop itself, such as memory systems and self-improving systems. We built an LLM agent framework, JAZ, to explore the extent to which a minimal harness that is little more than the agent loop itself can accomplish tasks these specialized systems are built for. JAZ exposes a single LLM-based primitive invoke and provides a set of built-in hooks that allow the programmer to apply constraints and monitoring. Generalizing existing code-mode agent loops, \texttt{invoke} is the simplest loop that satisfies two defining properties: (1) the LLM can write arbitrary executable code that can include recursive \texttt{invoke}; (2) everything visible to the LLM --- all inputs to \texttt{invoke} as well as its interaction history with the code environment --- are variables in the code environment. We motivate our design from first principles, viewing \texttt{invoke} as a language primitive representing a function whose implementation is provided at runtime by an LLM every time it is called. To validate the design of our core \texttt{invoke} primitive, we evaluate \texttt{invoke} --- with only prompting, no manually designed tools, harness, or external systems (e.g., memory or the file system) --- on workflows traditionally implemented through specialized external harnesses. On long-horizon workflows requiring recall beyond the context window, JAZ invoke outperforms Letta (MemGPT) by 8\% at half its cost on the recall-heavy portion of StuLife. On continual self-improvement, JAZ invoke outperforms ACE by 4\% at a lower cost on AppWorld.

---


### 7. [ACTS: A multi-tier benchmark evaluating LLM cipher identification under controlled blind conditions](https://arxiv.org/abs/2609.26893)

**<font color=#1a73e8>作者：</font>** Youssef Hamdi Zafaan Ibrahim, Mohammed Khalaf Salama  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce ACTS (Artifacts in Cipher Testing Suite), a reproducible benchmark that isolates cryptanalytic ability through tiered metadata deprivation (Tier-1: full metadata; Tier-2: filename only; Tier-3: completely blind) and tests forced reasoning (Tier-5: chain-of-thought, code-as-reasoning, self-correction) on ciphertext alone. A 10-configuration ablation study on 7,000 files, using a single 70/30 train-test split for feature-removal analysis, provides additional evidence at scale. Live API inference on a v2b corpus with fully randomised padding (PKCS7, ISO 10126, and ANSI X9.23 selected per file), unique CSPRNG keys, and unique plaintexts (127 files per model, 381 Tier-1 records, 380 Tier-3 records across three cloud systems, supplemented by 254 autonomous agentic evaluations in Tier-4) yields a combined Tier-3 accuracy of 30.8%, only modestly above the 14.3% random baseline for seven-way classification. The corresponding combined metadata-dependency gap is 40.9 percentage points (Tier-1: 71.7% vs. Tier-3: 30.8%). Against a classical Random Forest (69.2% on 7,000 files, trained on engineered byte-level features), the observed live gap is 38.4 percentage points. Because this comparison spans different input representations and training paradigms, the gap should be interpreted as an overall capability difference rather than a clean factorial decomposition. Six findings are reported: (1) Metadata dependency remains large; (2) Scaling failure under blind conditions; (3) Forced reasoning is epiphenomenal; (4) The observed live capability gap exceeds earlier heuristic estimates; (5) The signal is primarily structural rather than statistical; (6) Heuristic invariance versus ML fragility reveals different failure modes.

---


### 8. [TwinCheck: Evidence-Grounded Negative-Twin Verification for Stateful Tool Agents](https://arxiv.org/abs/2609.26911)

**<font color=#1a73e8>作者：</font>** Jiaxuan Dai, Tianyi Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A single locally plausible tool call can derail an otherwise successful agent trajectory. Suspicion alone does not justify intervention, because the replacement itself can introduce the very failure verification is meant to prevent. We introduce TwinCheck, an inference-time verification policy that considers replacement only when the trace satisfies an evidence condition tied to a trace-local failure hypothesis. It constructs a trace-grounded counterfactual alternative, a negative twin, and replaces the agent's proposal only if the twin passes structural checks and the pairwise verifier prefers it in both candidate orders. For paired evaluation, exact replay holds the agent's parsed responses and actions fixed until the first accepted replacement, separating intervention effects from resampling. In the primary analysis of 159 multi-turn BFCL V4 tasks with complete exact-replay pairs, the complete policy raises task success for GPT-5.6 Sol from 45.3% to 58.5% (95% task-bootstrap CI [8.2, 18.8]), with no observed success-to-failure regressions. Together, these findings recast execution-boundary repair as a constrained comparison, making the counterfactual action itself the object of verification.

---


### 9. [COMED: The Missing Middle Between Routing and Collaboration in Multi-LLM Inference](https://arxiv.org/abs/2609.26913)

**<font color=#1a73e8>作者：</font>** Norah Alballa, Wenxuan Zhang, Salma Kharrat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> No single Large Language Model (LLM) is uniformly reliable across queries, motivating multi-model inference systems that either route among models or combine their outputs. However, routing stops after selecting an initial model, while dense collaboration invokes peers on every query. We show that collaboration is non-monotonic: peers can recover failures that no model solves alone, but can also corrupt initially correct answers. We introduce COMED (Controlled Model Escalation for Multi-LLM Deliberation), a post-anchor controller for selective cross-model collaboration. COMED uses anchor self-consistency, router margin, and a lightweight peer probe to accept confident answers, verify ambiguous cases, and escalate only when collaboration is likely beneficial. We formalize this trade-off with a rescue-harm decomposition showing that selective collaboration improves when rescued errors outweigh collaboration-induced harms. Across medical, scientific, and general reasoning benchmarks, COMED improves fixed and routed anchors in all 16 open-weight settings, with gains up to +10.7 percentage points on MedQA while invoking fewer models and using fewer decoded tokens than dense collaboration. On HLE with frontier models, COMED improves GPT-5.5 from 23.1% to 28.1%, outperforming dense collaboration and achieving the best results.

---


### 10. [Experts Rise Where LLMs Disagree: Using Cross-Model Disagreement to Target Expert Effort in LLM Codebook Revision for Large-Scale Annotation](https://arxiv.org/abs/2609.26926)

**<font color=#1a73e8>作者：</font>** Zeyu He, Zhuqian Zhou, Kirk Vanacore 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale text annotation brings expert insight to millions of documents, often through a codebook that AI annotators follow. Developing a robust codebook, however, takes months. Large language models (LLMs) could speed this process by applying an early codebook to the data, surfacing cases with strong LLM disagreement, and eliciting expert feedback to address them. We examined three ways experts can provide feedback for LLM codebook revision: (i) editing LLM-generated revisions driven by cross-LLM disagreement (Codebook Verifying), (ii) answering questions about LLM disagreements (Question Answering), and (iii) labeling disagreement cases with rationales (Rationale Labeling). Experiments on thousands of tutoring-session transcripts show that Rationale Labeling yielded the highest LLM-labeling accuracy (64.9%) against expert labels, outperforming the expert-revised codebook (57.8%). The best Question Answering setting also outperformed it (60.5%). Our work shows that LLMs can be used to strategically target expert attention, shortening months of codebook revision to days without sacrificing labeling performance.

---


### 11. [Recognized but Not Produced: A Generation Benchmark for Culturally Specific Kinship Terms](https://arxiv.org/abs/2609.26942)

**<font color=#1a73e8>作者：</font>** Sahil Pardasani, Madhusudan Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current literature evaluates large language models (LLMs) on multilingual kinship understanding using multiple choice benchmarks, treating it as a recognition problem. We instead prompt five open weight LLMs to generate kinship terms in three non Western languages (Hindi, Tamil, and Korean) across two communicative tasks and pair this with a matched option-supported selection baseline. On identical relation language cells, GPT OSS120B selects the correct term in 90.67% of 75 valid cells but produces an accepted term in 36.00% of the corresponding attempts; Llama 3.370B shows the same pattern (77.92% versus 24.24%). Since the four-option condition displays the candidate terms and does not require script production, the difference is interpreted as an evaluation format gap rather than direct proof that lexical knowledge is intact. On explicitly specified L3 prompts, accuracy varies sharply, from GLM-5.1 at 72.29% to Llama-3.370B at 24.24%. The paternal-lineage advantage is language specific; it is large in Hindi but weak or reversed in Korean, while Tamil shared-term pairs provide a control for measurement variation. These results show that culturally specific kinship generation remains difficult even when the relationship is explicitly stated and motivate generation-based evaluation alongside multiple-choice testing.

---


### 12. [Classifying Interpretive Canons at the Sentence Level: A Benchmark from the German Federal Constitutional Court](https://arxiv.org/abs/2609.26945)

**<font color=#1a73e8>作者：</font>** Felix Ringe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Judicial reasoning remains challenging for large language models (LLMs) to analyze. This paper contributes a sentence-level benchmark for evaluating the ability of LLMs to classify interpretive canons as articulated by Larenz in the tradition of Savigny. Our contributions are threefold. First, we operationalize this conception of interpretation as classification criteria. Second, we provide a dataset of decisions of the German Federal Constitutional Court annotated at the sentence level. Third, we report baseline evaluations of four LLMs from three model families under expert hand-written prompts, compared against prompts optimized with Genetic-Pareto (GEPA). Mean F1 over the seven binary subtasks clusters between 70.4 and 79.2 across models, with grammatical interpretation usually the easiest canon to identify and systematic interpretation usually the hardest; under the tested configuration, GEPA-optimized prompts do not systematically outperform the hand-written ones, suggesting that the expert prompts provide a meaningful baseline.

---


### 13. [Escaping Python Dependency Hell: A Hybrid Replay-and-Repair Pipeline for Python Dependency Resolution](https://arxiv.org/abs/2609.26952)

**<font color=#1a73e8>作者：</font>** Veronica Poweska, Ariana Oyanguren, Jessica Pourleyli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dependency conflicts in Python ecosystems arise from incompatible version constraints, missing packages, and undocumented compatibility relationships, causing many real-world code snippets to fail at execution. This paper presents PLLM+, a hybrid dependency-repair pipeline evaluated on the HG2.9K benchmark of 2,891 dependency-failing snippets. PLLM+ prioritizes inexpensive deterministic steps before invoking LLM-based repair: static AST-based interpreter inference, replay of historically successful dependency configurations from the competition-provided solutions database, and live PyPI validation of candidate package versions. When these steps do not resolve a case, the system falls back to a structured LLM-based repair loop with typed error classification and Proposer/Critic agents. On HG2.9K, PLLM+ solves 1,500 out of 2,891 snippets, compared with 1,169 solved by the PLLM baseline. It also reduces average runtime from 368.7 to 71.8 seconds per snippet. Most successful fixes come from replaying known configurations: 1,495 of the 1,500 successful fixes are produced by the solutions database, while the LLM fallback accounts for 5 additional fixes. These results suggest that, in this benchmark setting, deterministic reuse of previously validated dependency configurations is a simple and effective strategy, with LLM-based repair serving as a secondary fallback for cases not covered by prior solutions.

---


### 14. [When Learned Context Planning Fails to Beat Strong Retrieval: A Controlled Study of Planning, Routing, and Reranking for Long-Context QA](https://arxiv.org/abs/2609.26976)

**<font color=#1a73e8>作者：</font>** Yingrui Li, Han Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learned context planning selects evidence atoms before an answer model reasons over them. We test whether this learned selection improves long-context multiple-choice QA after strong retrieval, routing, budgeted-selector, and reranking controls. Our primary diagnostic uses all 503 LongBench-v2 MCQ questions with Qwen2.5-7B-Instruct. The planner is SFT-trained on outcome-selected traces from 140 training and 28 development questions; because the 503-question analysis includes those questions, it is partly transductive. At an 18k-character budget, anchored hybrid retrieval reaches 36.18% accuracy and BM25 reaches 35.98%, while the best direct planner-guided method reaches 34.19%. On the untouched 152-question test split, anchored hybrid remains higher (42.11% versus 36.84%). Leakage-safe routers cannot convert a large oracle gap. Under tight budgets, the best planner is ahead by only 0.40 points at 6k and loses at 9k; planner-guided reranking has a +1.79-point estimate at 6k with a paired interval crossing zero and ties the control at 9k. Packing-order and score-flatness analyses did not identify a stable mechanism. Under this setup, learned planning is a weak relevance signal rather than a replacement for strong retrieval.

---


### 15. [Same evidence, different judgments: Evidence noncommutative in vision/speech-text conflicts](https://arxiv.org/abs/2609.26986)

**<font color=#1a73e8>作者：</font>** Zhuoyun Li, Boxuan Wang, Xiaowei Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For multimodal large language models, when images or speech conflict with accompanying text, measured text reliance can entangle modality preference with evidence position. Earlier studies of text bias often used a fixed evidence order or moved task instructions with the evidence, leaving the contribution of order unclear. In this paper, we use a paired comparison that keeps the instructions and evidence content fixed and swaps only the positions of the two sources to quantify this potential influence. Across vision and speech models, placing an image or recording after conflicting text consistently shifts answers toward its content. We also revisit previous studies and analyze why their experimental settings can lead to misleading conclusions. These findings reveal cross-modal evidence noncommutativity: the same evidence can lead to different judgments when its order changes, and placing perceptual evidence later can increase the model's reliance on its content.

---


### 16. [LEGO: Synergizing Expert GraphRAG and Expert Chain-of-Thought for Legal Reasoning](https://arxiv.org/abs/2609.27009)

**<font color=#1a73e8>作者：</font>** Qingjing Chen, Junkai Zhang, Shaochun Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly applied to high-risk domains such as law, yet complex legal reasoning remains limited by two structural challenges. First, existing RAG and GraphRAG methods emphasize lexical or semantic similarity while overlooking normative relations among legal provisions. Second, vanilla Chain-of-Thought prompting may generate plausible rationales without enforcing the normative structure of legal reasoning. To deal with the bottleneck of pipelines in the legal reasoning domain, we propose LEGO, a dual-module framework that synergizes Legal Expert GraphRAG and expert Chain-of-thought for complex legal reasoning. ExpertGraphRAG uses an expert-annotated civil code graph encoding these normative relations with a greedy normative-coverage retrieval algorithm to dynamically extract instance-specific provision subgraphs, while ExpertCoT organizes the retrieved provisions and case facts into structured Provision-Fact-Conclusion reasoning. With a Qwen3-8B backbone, LEGO achieves 40.53% exact-match accuracy on LawExamQA_Civil, outperforming the evaluated RAG and CoT baselines and performing comparably to the evaluated larger models, while remaining robust on multi-hop questions. It also achieves the best results among the evaluated baselines on the open-ended benchmarks. Ablation studies confirm the individual and complementary contributions of both modules, demonstrating LEGO's effectiveness in improving LLMs' complex legal reasoning ability. Code and dataset can be found in the link: this https URL

---


### 17. [ContraVis: Evidence-Grounded Visual Analytics for Contradiction Review in Legal Contracts](https://arxiv.org/abs/2609.27014)

**<font color=#1a73e8>作者：</font>** Luis Sante, Paula Lima, Mariana Rocha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Legal contracts are structurally complex documents in which contradictions may emerge across distant and interconnected provisions. Although large language models (LLMs) improve legal language understanding, contradiction analysis remains a human-centered and evidence-grounded review task. We present ContraVis, a visual analytics system for human-in-the-loop contradiction analysis in legal contracts. The system models contracts as typed paragraph graphs that combine explicit contractual references with semantic relationships between paragraphs. This graph plays a dual role: it conditions LLM reasoning and serves as the interactive representation the analyst explores, keeping model context and human inspection aligned across coordinated views. In a controlled comparison, graph-conditioned reasoning recovered more injected contradictions than standalone LLM analysis as contract length grew, while surfacing additional candidates for analyst validation. A formative study with contract-domain lawyers indicated that in-context evidence comparison supported contradiction validation, and we distill design implications for evidence-grounded, LLM-assisted document review.

---


### 18. [Reinforcement Learning with Decomposed Subtasks](https://arxiv.org/abs/2609.27035)

**<font color=#1a73e8>作者：</font>** Mattie Terzolo, Mikolaj Sacha, Ayan Sinha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) and related policy-gradient methods for training language model agents collapse an entire multi-turn rollout into a single scalar trajectory reward before it enters the policy update. When the task composes distinct skills, especially under sparse and delayed environmental feedback, this collapsing is lossy: the optimizer must implicitly infer which competency drove the outcome and how that should change behavior. We argue the right primitive is not a better scalar but a decomposition: trajectory reward should be split along subtasks before it enters the policy update. We introduce Reinforcement Learning with Decomposed Subtasks (RLDS), whose core is Subtask-Decomposed Advantage Estimation (SDAE): a replacement for the scalar GRPO advantage that splits trajectory reward into per-subtask shares on a fixed taxonomy, computes a group-relative advantage per subtask, and distributes per-token credit by weighting each subtask's advantage by its importance, concentrating it around the step where a reflection marks that subtask's execution as consequential. We evaluate on four agentic benchmarks: FrozenLake (sparse grid navigation), HotpotQA (multi-hop QA, one retrieval tool), ScienceWorld (long-horizon embodied science), and DeepResearch (long-form research, four tools, composite rubric reward). Heterogeneity diagnostics emitted during training show where decomposition pays off - gains scale with subtask heterogeneity, largest on the high-heterogeneity tasks ScienceWorld (+11.5 points, paired-bootstrap 95% CI [+9.8, +13.3]) and FrozenLake (+9.8 points, [+7.0, +12.8]), and within noise on HotpotQA and DeepResearch, where the diagnostics predicted little to recover. ScienceWorld is also more compute-efficient under RLDS than scalar GRPO (-10.9% wall-clock per step), as long rollouts amortize the fixed reflect-and-grade overhead.

---


### 19. [An open benchmark for machine learning-based polymer property prediction](https://arxiv.org/abs/2609.27036)

**<font color=#1a73e8>作者：</font>** Robert W. Learsch, Nicholas Liesen, Daniel S. Levine 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Polymer property prediction lacks open, standardized benchmarks that enable rigorous comparison of machine-learning methods, with existing resources covering only a narrow fraction of polymer architectures, such as homopolymers. We introduce Polymer Benchmark 2026 (PolyBench26), an open dataset comprising nearly 250,000 polymer-property datapoints across eight physical properties, including data from experimental measurements, density functional theory, and molecular dynamics. The benchmark supports four evaluation tasks across homopolymers and alternating, random, and block copolymers: in-distribution property prediction, dataset-size scaling, repeat-unit complexity, and transfer to held-out polymer architectures. We compare language model, graph-based, and descriptor-based approaches and find graph-based models provide the lowest errors in property prediction, retain their advantage across the evaluated training-set sizes, and remain robust to increasing repeat-unit complexity. PolyBench26 provides a reproducible foundation for developing models for the increasingly complex polymer design space. The PolyBench26 benchmark is available open-source at this https URL.

---


### 20. [Are Stated Reasoning Steps Causally Load-Bearing?](https://arxiv.org/abs/2609.27038)

**<font color=#1a73e8>作者：</font>** Abhiram Bhupatiraju, Rayan Nyaupane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring assumes that the reasoning a model writes reflects the computation that directly produces its answer. Previous faithfulness metrics have been predominantly behavioral, as they simply edit the reasoning text and observe the resulting answer. However, our methodology aims to measure faithfulness causally at the activation level, specifically on self-generated reasoning. Unlike previous causal audits, which measure degradation, our interventions carry a known predicted target. In this way, each patch should switch the answer to a specific counterfactual entity derivable by construction. Specifically, we use synthetic multi-hop lookup tasks (2-6 hops). We patch the residual stream at the token span where the model states each intermediate step with the corresponding activations from a counterfactual run. For Qwen3-4B, 76.9% +/- 2.8% of stated steps are causally load-bearing (CLB) at the most responsive mid-network layer (random-position null: 11.3%; patching the underlying prompt fact: 83%, so stated steps carry approximately 96% of the achievable effect). Moreover, the standard behavioral test on the same items yields 88.2%, which overstates causal faithfulness by 11.4 percentage points (item-matched; 111:14 discordant pairs, p < 1e-15) and, for the easiest items, by up to 20 percentage points. This gap also has a clear capability dimension. Qwen3-1.7B is far less causally faithful overall (54.8%), with its faithfulness collapsing as reasoning depth increases (68% at 2 hops to 30% at 6), while Qwen3-4B remains relatively flat. Although stated reasoning can be causally meaningful, standard behavioral tests tend to overestimate its causal faithfulness, particularly on easier examples where model reasoning appears most fluent.

---


### 21. [Math Reasoning in LLMs is Organized by Approach, Not Topic](https://arxiv.org/abs/2609.27041)

**<font color=#1a73e8>作者：</font>** Sajad Goudarzi, Samaneh Zamanifard, Moloud Nasiri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning benchmarks are typically organized by topic, but language models may organize their internal computation by reusable reasoning approach instead. In this paper, we investigate whether open math-capable LLMs organize internally by topical sub-skill or by reasoning approach, and we present evidence that the approach is the key. We introduce a generation-replay protocol: a model first generates a solution, after which we replay the exact prompt-plus-generation trajectory and extract activation-importance signatures over the reasoning tokens. We cluster these signatures without supervision across eight models and five mathematical reasoning sources, then evaluate the recovered structure with structural, semantic, and intervention tests. Across all 40 model-source cells, the recovered clusters outperform matched-size random baselines. Two independent frontier-LLM judges find approach-level coherence in 77-82% of real clusters versus 6-11% in within-source controls, and topic-pure clusters usually receive labels finer than the topic itself. In approach-controlled prompting, changing the requested reasoning approach shifts cluster assignment in seven of eight model conditions, whereas paraphrases largely preserve it. These results indicate that math-capable LLMs organize internal mathematical computation by reasoning approach rather than benchmark topic. The implication is that topic-stratified benchmarks and topic-balanced training corpora can still miss the axis that matters: even deliberately topic-balanced corpora may remain imbalanced over reasoning approaches.

---


### 22. [EduBehaviors: Assertion-based Schemas for Auditable Coding of Educational Dialogues](https://arxiv.org/abs/2609.27043)

**<font color=#1a73e8>作者：</font>** Julian Bernado, Ana Trindade Ribeiro, Xander Beberman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have allowed the rapid deployment of pedagogical annotations corresponding to constructs of interest, allowing a natural language interface for generating classifications on a conversational dataset. However due to the opaque nature of LLM reasoning, we have no verifiable, mechanistic insight into why a model chose a label for an utterance. We introduce the EduBehaviors framework, an interpretable, scalable approach to annotating educational data that uses LLMs to measure repeated observable behaviors relevant to many constructs of interest and then learns a classifier for the construct based on these observable behaviors. We evaluate the framework on the TalkMoves dataset, predicting the Teacher TalkMoves labels. Our best configuration results in a macro-F1 of 0.673 and 0.688 Cohen's kappa, proving competitive with direct prompting approaches. In addition, we release EduBehaviors Toolkit, two tools allowing researchers to operationalize the EduBehaviors framework in their own data.

---


### 23. [Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors](https://arxiv.org/abs/2609.27051)

**<font color=#1a73e8>作者：</font>** Bo Qu, Mingguang Chen, Licheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents now run the whole of quantitative factor research: they propose investment factors, backtest them, select the survivors and retire them. We ask which of those jobs an agent should keep. Our answer is governed self-evolution: the agent may propose, and a frozen statistical referee that the agent cannot touch must judge. The referee scores each candidate only on market outcomes revealed after submission, by betting, so its false-discovery guarantee holds at every stopping time for any proposal policy. We cross three proposers (a script, a bandit and a language model) with this referee and with three deliberately leaky ones, in a synthetic world with planted truth, a probe-authoring environment and a ten-year walk-forward on the CSI 500. Who judges sets the number of false admissions: the frozen referee admits 5-11 times fewer sub-threshold factors than the leaky referees under a scripted proposer, and no proposer closes that gap. Who proposes sets the yield: the language model beats the script, matches the bandit, and adds the one capability a bandit lacks, writing its own diagnostic probes. The certificate's price is time: an admitted true factor waits about 500 trading days, and the certified portfolio's Sharpe ratio therefore trails an ungated one. Judging belongs to the procedure; proposing and instrument-making belong to the agent.

---


### 24. [What Changes When Fact-Verification Scores Improve? Evidence and Answer Accounting Across Trained Verifiers and LLMs](https://arxiv.org/abs/2609.27064)

**<font color=#1a73e8>作者：</font>** Han Chen, Yingrui Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A joint fact-verification score assesses answers and submitted evidence together. When the score improves, how much of the gain remains if the answers are held fixed? On FEVEROUS, strict score is the percentage of claims with a correct answer and a complete annotated evidence group in the submitted evidence. Across four trained DeBERTa checkpoints and 7,890 claims, replacing DCUF evidence with UnifEE evidence raises strict score by 9.61 percentage points, compared with 1.96 percentage points in answer accuracy. The paired 95% interval for the strict-score gain is [8.77, 10.43], conditional on these checkpoints. Replacing only the evidence passed to the scorer accounts for 7.92 or 9.08 percentage points when we retain the answers generated from DCUF or UnifEE evidence, respectively. To examine how this evidence gain depends on evaluation choices, we generate 470,400 responses from two 8B LLMs on FEVER, FEVEROUS, and SciFact under two answer formats and two context budgets. Increasing context from 256 to 2,048 tokens raises the fixed-answer evidence gain on FEVEROUS by 3.84 and 3.10 percentage points for Qwen and Llama, respectively. The effects fall short of the prespecified cross-dataset criterion, while some intervals extend beyond the two-point small-effect bound. Post-hoc analyses quantify changes in answers and submitted evidence, and show when aggregate accuracy and evidence-coverage rates miss the claim-level pattern. The four answer-evidence score combinations reveal changes that endpoint and aggregate metrics leave unresolved.

---


### 25. [ChipMEM: Verification-Grounded Memory for EDA Agents](https://arxiv.org/abs/2609.27067)

**<font color=#1a73e8>作者：</font>** Abdulrahman AlRabah, Joshua Mabry, Dilek Hakkani-Tür 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents use Electronic Design Automation (EDA) tools to generate and revise register-transfer-level (RTL) designs under synthesis and verification feedback. Recent methods learn from this feedback by distilling reusable skills from execution traces or by training on rewards derived from EDA-tools. Both methods are typically evaluated on the tasks that produced the experience. Repeated access to benchmark feedback on the same task can reward task-specific revision rather than creating reusable knowledge that transfers. We introduce ChipMEM, a verification-grounded memory layer for EDA agents. It combines cross-task procedural memory with within-trajectory statistical guidance. Its procedural component distills and stores a skill only after it passes synthesis, simulation, or formal checks, rather than relying on model self-assessments. A Bayesian component maintains hierarchical Beta estimates over tool-call outcomes and ranks recovery strategies that succeeded under comparable errors. A common adapter applies the same memory interface to RTL optimization and testbench-generation agents while preserving each domain's tools and acceptance criteria. We measure performance on training tasks and evaluate whether learned skills transfer to unseen tasks. On RTLRewriter-Bench, under matched model and tool settings, ChipMEM produces equivalence-passing outputs on 39/54 scored designs versus 35/54 without memory; on the 49-design short suite, mean area improvement is 8.69% versus 5.66%. On held-out CVDP tasks, ChipMEM with a frozen procedural library achieves 20/20 accepted outcomes versus 18/20 without memory in a single evaluation per setting.

---


### 26. [Policy-as-Skill: Governed LLM Decision Support with Evidence, Deterministic Control, and Audit](https://arxiv.org/abs/2609.27087)

**<font color=#1a73e8>作者：</font>** Kabeh Mohsenzadegan, Vahid Tavakkoli, Kyandoghere Kyamakya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations increasingly use LLMs for policy, compliance, risk, and operational decision support, requiring evidence validation, review routing, version control, and auditability. We introduce Policy-as-Skill (PaS), a modular runtime that packages these functions as executable, versioned policy capabilities. Thirteen methods are evaluated with a fixed Gemma4 backend on 600 development tasks. PaS+Audit achieves 53.8% exact accuracy, macro-F1 0.346, review F1 0.854, citation precision 1.000, policy-reference recall 0.984, and audit completeness 1.000, outperforming LLM+RAG on most governance and review metrics. Deterministic control raises aggregate accuracy to 61.2% but is strongly task dependent, supporting selective rather than universal rule-based intervention.

---


### 27. [Solidity Meets LLMs: A Transformer-Based Approach to Smart Contract Vulnerability Detection](https://arxiv.org/abs/2609.27091)

**<font color=#1a73e8>作者：</font>** Djamel Eddine Hakim Ghorab, Farid Mokhati, Mostafa Anouar Ghorab  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing adoption of blockchain technologies, particularly the Ethereum platform, has amplified the critical role of smart contracts in decentralized applications. However, the increasing complexity and financial value of these contracts make them prime targets for cyber attacks. In this work, we present a transformer-based approach for the detection of vulnerabilities in smart contract fragments written in Solidity. Leveraging the representational power of pre-trained Large Language Models (LLMs), we construct a robust pipeline that includes the definition of a ground truth dataset, labeling code fragments as vulnerable or safe. We then fine-tune a BERT-based architecture on this dataset, enabling the model to capture the syntactic and semantic patterns specific to Solidity code. Our fine-tuned model demonstrates strong performance, achieving an F1 score of 92%, and highlighting the effectiveness of LLM adaptation in enhancing smart contract security through deep contextual understanding.

---


### 28. [When Direct Manipulation Becomes a Guess: Productive Friction in AI-Mediated Multisensory Visualization](https://arxiv.org/abs/2609.27104)

**<font color=#1a73e8>作者：</font>** Anchit Mishra  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative visualization increasingly embeds large language models within direct manipulation and multisensory interaction. Speech, gaze, touch, gesture, sound, and haptics can make probabilistic inference feel like familiar, deterministic tool use. I call this gap a deterministic-affordance mismatch: deterministic interaction cues persist while AI weakens predictability, locality, reversibility, or provenance. Reading the malleable interfaces of Iron Man 2 against systems from Blade Runner 2049, I propose productive friction, including cross-sensory renderings whose detail reflects model uncertainty. Four frictions expose the inference boundary, match action to effect, make stochastic branches tangible, and attribute sensory agreement.

---


### 29. [Provably Complete Generalized Planning with LLMs](https://arxiv.org/abs/2609.27105)

**<font color=#1a73e8>作者：</font>** Katharina Stein, Chaahat Jain, Jörg Hoffmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generalized planning aims to compute a plan that solves all instances of a planning domain. Recent work has used LLMs to automatically generate and debug such generalized plans in the form of Python programs and achieved perfect test data coverage for several domains. However, whether these generalized plans are actually complete, i.e. solve all instances of the domain, could only be determined by manual evaluation. Here, we present an approach for automatically generating generalized plans in Lean together with proofs of their completeness relative to a specification of the domain constraints provided as input. We introduce a semantic-preserving PDDL-to-Lean conversion, and use an LLM to generate both the generalized plan and the formal proof that it solves every instance satisfying the domain constraints. The correctness of the completeness proof is determined by Lean's kernel. We evaluate our approach on 13 commonly used benchmark domains, using GPT-5.6-Sol as the LLM. For 12 of the domains we obtain generalized plans together with valid completeness proofs. This is a major advancement of the state of the art in automatic generalized-plan completeness proofs.

---


### 30. [Feed the Panel Dimensions, Not Verdicts: Rubric-Decomposed Fusion of Vision-Language Aesthetic Judges](https://arxiv.org/abs/2609.27110)

**<font color=#1a73e8>作者：</font>** Amit Jadhav, Shaurya Beriwala, Beomjin Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are deployed as zero-shot judges of image aesthetics, and panels of several models are recommended, on thin evidence, as the way to make such judges reliable. On two human-rated datasets, EVA and PARA, we find that a panel of holistic judges never significantly beats its best member, whether the verdicts are averaged or fused by a learned combiner. What a panel is worth depends on what it is fed. We therefore have each model score each image on the five dimensions of a frozen, human-written rubric and fuse those scores, alongside each model's verdict, across model families with an out-of-fold combiner. The dimension scores measure what their labels claim: with the overall human score partialled out, a dimension prompt carries more attribute-specific information than the holistic prompt in 28 of 30 model-attribute cells. Fused, they beat the best single VLM in all ten three-family panels on EVA (against that best single model, +0.07 Spearman rho for the strongest trio and +0.10 for the pre-declared one, and +0.06 and +0.07 when averaged over twenty fold partitions; against the panel mean, the primary test gives +0.118 on its EVA design set), and on PARA they reach parity under Spearman rho and a small, non-significant loss under Kendall tau-b, where one model already captures 85% of the human noise ceiling. It is not a feature-count artefact: giving the same combiner an equal number of pure holistic columns, split from the same repetitions, does not reproduce it. The gain costs a few hundred labels, which do not transfer between datasets, and 4.8x the API calls on EVA; we report it with paired bootstraps and Kendall tau-b, alongside a failed pre-registration and the configurations that lost.

---


### 31. [A Hierarchy-Aware Video-Language Model Evaluation and Hyperbolic Baseline for Surgery](https://arxiv.org/abs/2609.27139)

**<font color=#1a73e8>作者：</font>** Ana Manzano Rodríguez, Pascal Mettes, Marlies P. Schijven 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical procedures follow a phase-to-step hierarchy, yet the video-language models used to recognize them are evaluated with flat per-level metrics that ignore cross-level coherence and error structure. In this paper we make two contributions to address this problem, (i) we introduce SurgHiBench, the first hierarchy-aware evaluation suite for surgical video understanding, with three tasks measuring recognition, consistency, and severity across granularity levels. We evaluate a general-purpose CLIP model, a Euclidean surgical model, and, as second contribution: (ii) HyperSurg, a new hyperbolic model that enforces phase-step containment via entailment cones, across four (existing) datasets spanning three procedure types. The suite reveals that two models with the same accuracy can produce predictions of very different error severity, ranging from sibling confusions within the correct phase to unrelated cross-phase predictions. Hyperbolic geometry shifts predictions toward the correct procedural neighborhood, and these gains scale with the tree-likeness of each dataset's annotation hierarchy, providing a principled indicator when hierarchy-aware geometry helps.

---


### 32. [ChartRevive: Reconstructing Data Visualizations from Chart Images Using MLLM](https://arxiv.org/abs/2609.27146)

**<font color=#1a73e8>作者：</font>** Yuki Ueno, Aditeya Pandey  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Static chart images are widely used in scientific publications, business reports, and presentations, yet recovering both the underlying data and visual design from chart images remains a labor-intensive manual process, making them difficult to reuse. While prior work has primarily focused on data extraction, the extraction of visual design specifications, including colors, marker shapes, and axis configurations, remains underexplored. To identify a suitable model for chart reconstruction, we systematically benchmark five multimodal large language models (MLLMs) across five basic chart types on both data and design extraction tasks. Our evaluation shows that textual and categorical information can generally be extracted reliably, whereas numeric and spatial information remain challenging. Among the evaluated models, GPT-5.4 achieves the best overall performance and is adopted as the backbone of our system. Guided by these findings, we present ChartRevive, a mixed-initiative system that combines MLLM-based extraction with an interactive verification interface, supporting users to efficiently inspect, correct, and refine reconstructed charts through overlay-based verification and real-time rebuilding.

---


### 33. [Do We Need Complex Topology Control? Distinct-Peer Random Routing Improves Cost-Efficiency in Sparse Multi-Agent Debate](https://arxiv.org/abs/2609.27150)

**<font color=#1a73e8>作者：</font>** Boxuan Wang, Zhuoyun Li, Xiaowei Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) has emerged as a promising paradigm for improving the reasoning accuracy of large language models (LLMs) through iterative peer interaction. Communication topology plays a central role in this process, motivating increasingly sophisticated mechanisms that learn, adapt, or dynamically reconfigure agent interactions to improve accuracy or reasoning reliability. Meanwhile, prior studies suggest that much simpler sparse communication can already achieve competitive performance at substantially lower cost. In this work, we take a closer look at sparse MAD and ask whether complex topology control is actually necessary to improve collective reasoning. We find that a simple random-without-replacement routing policy, which lets each agent debate with two distinct and newly sampled peers at every round, provides a surprisingly strong baseline and consistently improves the accuracy-cost trade-off of sparse MAD. Building on this observation, we further study deliberation stopping and show that lightweight stopping can substantially reduce inference cost while preserving competitive accuracy. Our results suggest that sophisticated topology control such as learned topology adaption should be evaluated against strong simple routing and stopping baselines before its additional complexity is justified.

---


### 34. [Giving Credit Where It's Due: Redundancy-Aware Learning for Efficient Reasoning](https://arxiv.org/abs/2609.27156)

**<font color=#1a73e8>作者：</font>** Yuqing Zhou, Hong Wang, Manqing Mao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models can produce correct yet unnecessarily long reasoning traces. Existing methods improve reasoning efficiency with trajectory-level objectives or local token- and step-level signals, but rarely model inter-step semantic dependencies. This limits their ability to distinguish redundant steps from those that support later deductions, making it harder to shorten reasoning without sacrificing accuracy. We introduce RECAP (REdundancy-aware Credit Assignment via Propagation), which addresses this limitation by assigning credit where it is due based on both a step's downstream role in the reasoning structure and its contribution to solving the problem correctly. We define structural responsibility to capture the step's downstream role by measuring how strongly later reasoning depends on it, using credit propagated backward from the final-answer node through an outcome-independent, LLM-annotated semantic dependency graph. However, a step can have high structural responsibility yet steer the reasoning away from the correct solution. RECAP therefore introduces step efficacy to measure answer-directed progress through changes in gold-answer log-likelihood as each step is added. Together, these signals reshape rollout-level GRPO advantages into step-specific updates. RECAP requires neither a separately trained process reward model nor preconstructed concise trajectories. Across two 7B models and four mathematical reasoning benchmarks, RECAP improves the accuracy-efficiency trade-off. On Qwen2.5-Math-7B, it improves pass@1 by 2.0-3.7 percentage points while reducing reasoning tokens by 8%-31% relative to GRPO across all four benchmarks. Analysis suggests these savings reflect fewer reasoning operations and less dead-end reasoning, rather than more compact expression.

---


### 35. [Count Evidence, Not Sentences: Tempered Evidence Fusion of LLM Judgments for Long-Text Value Measurement](https://arxiv.org/abs/2609.27165)

**<font color=#1a73e8>作者：</font>** Yuhe Wu, Rui Qian, Guangyu Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to measure public value orientations from long social media posts, yet such posts often mix background, quotations, concessions, and only a few stance-bearing sentences. Existing approaches either ask the model to predict a document-level label directly, which can be overconfident, or aggregate sentence-level predictions by majority or soft voting, which treat uncertain and decisive sentences as equally informative. We formulate long-text value measurement as a decision-fusion problem and propose Tempered Evidence Fusion (TEF), a training-free rule that weights each sentence's log-odds by its normalized information gain, as derived from a generalized Bayesian posterior. This makes the fused score nearly vanish for uncertain sentences while preserving the Bayes-optimal weight of decisive evidence. We further introduce Multi-event Insight Network Dimensions (MIND), a benchmark of 8,358 Chinese and English posts spanning five years of public events and six value dimensions. On MIND, TEF outperforms the strongest baseline among Direct, Majority Vote, and Soft Vote by an average of 4.5 accuracy points and 4.6 macro-F1 points across five LLMs and two languages. MIND dataset and code are available at this https URL.

---


### 36. [Scaling of Capability and Efficiency at Inference Time in Large Reasoning Models](https://arxiv.org/abs/2609.27166)

**<font color=#1a73e8>作者：</font>** Moritz Laber, Zohair Shafi, Germans Savcisens 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Capability and efficiency are two key dimensions of reasoning in large language models (LLMs). Capability refers to the ability to solve a given problem correctly, whereas efficiency refers to the ability to do so with limited resources. When LLMs use Chain-of-Thought (CoT) reasoning to solve problems of controlled hardness, both the number of problems solved correctly and the number of tokens required to reach a correct answer depend on problem hardness and model size. However, how these factors jointly shape capability and efficiency remains poorly understood. Here, we use hierarchical Bayesian models to evaluate the capability and efficiency of LLMs from the DeepSeek-R1-Distill model family across four classes of arithmetic and algorithmic reasoning problems. At a fixed model size, the probability of correctly solving an instance decays approximately exponentially with instance size, our proxy for problem hardness. The decay scale grows sublinearly with model size, indicating that larger models are more capable, but that capability gains diminish with scale. Output length grows as a power law with instance size, which serves as a proxy for difficulty. However, the parameters of this power law do not vary systematically with model size, suggesting that larger models do not become more efficient. Together, these findings reveal potential limitations of naive scaling as a strategy for developing more capable AI systems: capability improves with diminishing returns, while efficiency shows little to no improvement.

---


### 37. [Realize What Matters: Principled Context Representation for Large-Scale Reasoning](https://arxiv.org/abs/2609.27173)

**<font color=#1a73e8>作者：</font>** Michael Theologitis, Dean Light, Shuyue Stella Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Solving complex tasks in domains such as science, medicine, law, and finance often requires assembling interdependent information scattered across vast, heterogeneous sources far beyond model context limits. Existing approaches tackle this challenge by organizing information into more manageable representations over which models can reason, such as graphs, textual memories, and retrieval collections. These representations dictate what downstream reasoning is possible and, ultimately, whether it succeeds; yet their design and construction remain largely ad hoc. In this work, drawing on the cognitive theory of relevance realization, we propose concrete principles for designing AI systems that construct effective representations of very large contexts. We analyze existing approaches and show how their successes and failures map onto their alignment with these principles, and introduce R3Con, a harness designed to operationalize the principles more systematically. We evaluate R3Con against nine state-of-the-art baselines on two recent benchmarks of reasoning over large document corpora. On these benchmarks, R3Con substantially outperforms the strongest baseline, by $20$ and $8.4$ percentage points. It also enables smaller models to outperform much larger ones: R3Con with 4B and 9B models outperforms all evaluated 35B baselines, while R3Con with a 35B-A3B model outperforms Claude Code with Claude-Sonnet-5 at $3.7\times$ lower cost. Our results show that context representations following our principled approach can reduce reliance on model scale, pointing toward a future of AI systems with frontier-level performance powered by smaller models. Our code is available at this https URL

---


### 38. [Enhancing Small Language Models for Power Outage Report Generation via Minimum Risk Training](https://arxiv.org/abs/2609.27197)

**<font color=#1a73e8>作者：</font>** Hung Phan, Waqwoya Abebe, Youssef Hussein 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Minimum Risk Training (MRT) enables neural machine translation models to directly optimize sequence-level evaluation metrics instead of relying only on token- level maximum-likelihood objectives Shen et al. [2016]. Although introduced a decade ago, recent work shows renewed potential for risk-based optimization in modern language models Yang et al. [2024], Jinnai et al. [2025]. We apply MRT to power outage report generation for the Outage Data Initiative Nationwide (ODIN), transforming heterogeneous reports into standardized XML compliant with CIM IEC 61968-3. Our MRT approach improves Qwen2.5-7B-Instruct overall accuracy from 16.20% to 68.95%, demonstrating the effectiveness of sequence- level optimization for domain-specific structured generation

---


### 39. [ZO-COSMO: Index-Free One-Hop Mixing for Decentralized Zeroth-Order Optimization](https://arxiv.org/abs/2609.27199)

**<font color=#1a73e8>作者：</font>** Shengjun Zhang, Tingyi Liu, Heng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse communication in decentralized zeroth-order learning requires compatible peer-state coordinates. We characterize this one-hop condition and develop \textsf{ZO-COSMO}, coupling two-query estimation with average-preserving masked consensus using $q$ values per active link. Global supports serve all-neighbor mixing; matching updates require agreement only within each pair. We derive a sharp contraction-per-scalar bound within the matching class and convergence guarantees for the core and sparse-momentum updates. At fixed matching, exact moment identities characterize how shared directions preserve gradient-heterogeneity cancellation and redistribute estimation error and disagreement. Mechanism experiments cover unequal curvatures, noise, and sparse momentum. Further tests span $64$ synthetic agents and eight logical Qwen LoRA workers. At matched payload budgets, Qwen2-7B QNLI gains $3.65$ accuracy points over explicit-index Rand-$k$; edge-local updates gain $3.42$ and $2.53$ points over all-neighbor mixing on eight-worker complete and ring graphs. A matched-first-step ablation gives a $3.92$-point momentum benefit. Seed-aware and same-matching controls distinguish encoding, scheduling, and query correlation.

---


### 40. [Phonemizing User-Generated Text: A Benchmark, Taxonomy, and Compositional Approach](https://arxiv.org/abs/2609.27205)

**<font color=#1a73e8>作者：</font>** MinJu Jeon, Younghan Park, Han Sung Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-speech systems increasingly process user-generated text (UGT) such as ppl and imo, whose pronunciation must be inferred from the canonical rather than surface form. We introduce UGTPhon, the first grapheme-to-phoneme (G2P) benchmark for UGT in English, Vietnamese, and Korean, together with an inference-grounded taxonomy for fine-grained diagnosis. Existing G2P models and frontier LLMs exhibit a systematic canonical-to-non-canonical performance gap, reaching up to 66.8 PER points. As a benchmark baseline, we propose a simple compositional G2P approach that incorporates canonical-form evidence through exact-match lookup and staged decoding. Across matched ByT5 and Qwen2.5-0.5B backbones, explicit canonical-form modeling consistently reduces non-canonical G2P errors. The 0.5B variant also performs competitively with much larger few-shot frontier LLMs, highlighting the benefit of explicitly modeling canonical-form inference for UGT phonemization.

---


### 41. [LOCKR: A Hidden-State Trajectory-Guided Planner for Detecting and Repairing Stable-but-Wrong Lock-In in Diffusion Language Models](https://arxiv.org/abs/2609.27220)

**<font color=#1a73e8>作者：</font>** Guoshenghui Zhao, Tan Yu, Weijie Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models generate text through iterative denoising, exposing intermediate trajectories before final answers are produced. We identify a recurring reasoning failure, stable-but-wrong lock-in, where an answer stabilizes early around an incorrect value while substantial denoising remains. Surface-level decoding signals such as confidence, entropy, margin, and answer stability are insufficient to reliably distinguish correct from erroneous lock-in. We formulate selective reasoning repair as a lightweight test-time planning problem and propose LOCKR, a hidden-state trajectory-guided planner that decides when to allocate additional computation, expands a structured set of targeted repair branches, and selects the most promising continuation using trajectory-aware verification. Across two diffusion language models and three mathematical reasoning benchmarks, hidden-state trajectories consistently outperform surface signals and single hidden snapshots for both wrong-lock-in detection and repair selection. On natural evaluation distributions, LOCKR yields absolute accuracy gains of 2.21--5.37 percentage points across all five evaluated settings, with repair rates ranging from 22% to 41%. These results establish hidden diffusion trajectories as actionable signals for selective test-time reasoning repair.

---


### 42. [Meet, Compare, or Abstain: LatWeave for Deterministic Multi-Hop Question Answering on Knowledge Lattices](https://arxiv.org/abs/2609.27225)

**<font color=#1a73e8>作者：</font>** Yuze Ren, Shaoheng Fan, Tao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probabilistic question-answering systems -- whether large language models (LLMs) themselves, retrieval-augmented generation (RAG), or trained multi-hop retrievers -- conflate "what is known" and "how to reason" into a single probabilistic computation: hallucination cannot be eradicated, evidence chains cannot be audited, and the system answers even when it does not know. We present LatWeave, which organizes knowledge into a multidimensional knowledge lattice and compiles multi-hop QA into three deterministic operators -- meet (constraint intersection), compare (lattice-order comparison), and abstain (structural abstention); LLMs appear only on the construction side (one-shot extraction) and the query-planning side, while the answer-generation path is zero-LLM, zero-task-training, and auditable end to end -- so that question answering over Web-published knowledge becomes reproducible item by item. Rather than claiming across-the-board SOTA, we characterize the operating envelope of this paradigm on six public benchmarks: when knowledge is complete (MetaQA, 39,093 questions) meet chains are near-lossless over three hops (any-hit 0.9975, on par with fully supervised KBQA); on templated multi-hop home ground (2WikiMultihopQA held-out n=1,258) EM 0.865, well above published structure-augmented RAG reproductions; on open-text deep composition (MuSiQue) and extraction-coverage gaps (HotpotQA) we report degradation honestly and attribute it to causes outside the lattice-algebra layer; and when information is incomplete (IIRC) we achieve structural abstention with abstain accuracy 0.971 and leak rate 0.029. Within the operating envelope, deterministic execution pays no performance penalty, and every step on the answer path can be recomputed -- precisely the source of end-to-end auditability.

---


### 43. [Distilling Sequential Computation in Transformer Language Models](https://arxiv.org/abs/2609.27233)

**<font color=#1a73e8>作者：</font>** Zixuan Lan, Jessica Yang, Yanhong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer language models process sequences token by token in an autoregressive manner, making growing contexts increasingly expensive. Yet many adjacent token spans are highly predictable or frequently occur as stable units, suggesting that their representations may be compressible. We introduce a method for distilling sequential computation by replacing spans of input tokens with collapsed representations, computed on the fly by a lightweight merge module. This module generates a single surrogate embedding from a sequence of static token embeddings that captures the functional role of the multiple tokens, allowing pretrained models to operate on compressed inputs without architectural changes or re-training. We apply this approach during inference to compress both prompts and intermediate decoding steps, using a rollback mechanism to substitute stored multi-token KV cache entries with their single-step surrogates. Experiments across diverse models show that the merge module can be used to reduce effective sequence length by up to 40% with minimal accuracy degradation across language modeling evaluations and downstream tasks, including question answering, summarization, commonsense reasoning, and long-form mathematical reasoning. Additional lightweight adaptation of the merge module further improves the accuracy-compression trade-off in selected settings. These results demonstrate that sequential token computation in Transformers can be effectively approximated through condensed surrogate representations that approximate the original behavior without model updating.

---


### 44. [Discover, Falsify, Revise: Auditing Input-Use Claims from Source Code to Predictive Contribution in Agent-Discovered Cell Models](https://arxiv.org/abs/2609.27234)

**<font color=#1a73e8>作者：</font>** Mengran Li, Bo Li, Chengyang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI virtual cells aim to predict cellular responses to specified interventions, yet held-out predictive performance alone does not establish use of the supplied perturbation information. This prediction-claim gap matters in agentic model discovery, where language-model agents generate and revise predictors using score-based feedback. We introduce CELLAUDIT, which audits input-use claims by asking whether an input can enter the cited computation, whether fitted predictions depend on it, and whether that dependence improves prediction of observed response. On a paired morphology-transcriptomics perturbation benchmark (BBBC047), an agent-selected predictor attains a mean held-out Global Pearson correlation coefficient (PCC) of 0.3153 but remains invariant to compound replacement; a control-profile-only predictor reaches 0.3142. Source inspection identifies a compound-query pathway blocked by singleton key-value attention, and the invariance persists after refitting with disjoint control wells. In a stratified audit of 48 candidates across two linked tasks, 47 change predictions under compound replacement on both held-out folds, but only 20 show target-loss gains with intervals above zero on both folds. On BBBC047, falsification-guided revisions recover positive mean compound contributions while retaining gains over the control-profile-only baseline. In matched sci-Plex searches, audit-enriched feedback yields higher held-out performance and larger mean compound and dose contributions across five trajectories, although paired intervals span zero. Refitting fixed designs on an independently acquired cohort shows predictive generalization need not imply generalization of input-use claims: dose contribution persists, whereas support for compound identity does not. CELLAUDIT adds a falsification layer to agentic model discovery, moving from generate-score-revise toward discover-falsify-revise.

---


### 45. [Full-Covariance Smoothing of Bayesian Neural Networks for Online Adaptation](https://arxiv.org/abs/2609.27244)

**<font color=#1a73e8>作者：</font>** Oren Wright, Haoming Jing, Qiaoan Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A neural network's layers can be treated as time steps of a state-space model, turning Bayesian training into a smoothing problem: a forward pass propagates Gaussian moments through the network, and a backward Rauch--Tung--Striebel pass updates the weight posteriors in closed form. Such methods learn from each observation in a single pass, in an uncertainty-aware manner, and without gradient-based iterations or replay, which makes them well suited for online adaptation and data-efficient learning. Existing smoothing-based methods, however, are restricted to diagonal covariances across activations, discarding correlations between neurons. We overcome this limitation via a cross-covariance identity that enables full-covariance propagation through a network's nonlinear activations. We derive a one-step-per-layer smoother that approximates as Gaussian only each layer's affine output, and that applies both to deterministic systems with noisy observations and to stochastic systems described by output statistics. We demonstrate this method in non-stationary classification, online dynamics learning, and policy adaptation of a vision-language-action model, and find that it is generally more accurate than other smoothing-based methods.

---


### 46. [Repurposing Pre-trained LLMs as High Fidelity Continuous Text Autoencoders](https://arxiv.org/abs/2609.27248)

**<font color=#1a73e8>作者：</font>** Arkanath Pathak, Unnat Jain, Alexander C. Berg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next-token prediction has enabled highly fluent autoregressive language models, but it represents global structure only indirectly through sequential factorization. In contrast, high-fidelity autoencoders have become a standard primitive in image generation, enabling generative models to operate over continuous latent spaces; text lacks a comparably faithful continuous representation. We propose LLMAE, a method for repurposing a pretrained decoder-only language model as a continuous text autoencoder by exposing an intermediate fixed-length latent bottleneck within its internal activations. Instantiated with a parameter-efficient 270M Gemma 3 model, LLMAE uses structured attention masks, LoRA adaptation, and KL regularization to learn an autoencoding interface that leverages the generative prior of the original LLM. We train LLMAE to reconstruct text sequences up to 1024 tokens, significantly improving on this task to achieve near-perfect reconstruction. Furthermore, we demonstrate the downstream utility of this representation by training a latent text diffusion model for detailed image captioning using the learned LLMAE autoencoder. By mapping text into a fixed-length continuous latent space, our approach provides an effective substrate for downstream adaptation while benefiting from the fluency of the original LLM.

---


### 47. [What Converges in the Platonic Representation Hypothesis? Structure over Geometry](https://arxiv.org/abs/2609.27252)

**<font color=#1a73e8>作者：</font>** Junwon You, Mihyun Jang, Sangwoo Mo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Platonic Representation Hypothesis suggests that increasingly capable models converge toward shared representations. Recent work narrows this claim to shared local neighborhood relationships, finding that capacity-dependent trends in several global similarity measures largely disappear after calibration. We challenge this interpretation by showing that prior local-global comparisons confound structural scale (local versus global) with what is compared: relational structure, defined by which samples are related, versus metric geometry, characterized by quantitative relations such as distances, similarities, or correlations. To disentangle these factors, we construct a controlled $2\times2$ framework that evaluates both relational structure and metric geometry at local and global scales. We introduce $H_0$ skeleton overlap as a global counterpart to mutual $k$-nearest neighbors, together with matched distance-aware variants. Across vision-language models, relational structure exhibits robust representational convergence at both scales after calibration, whereas increasingly stringent distance agreement substantially weakens alignment and progressively flattens the capacity-dependent trend. We further extend the analysis beyond ambient Euclidean geometry by evaluating distance agreement under a Riemannian metric approximation and recover the same structure-geometry pattern. The pattern is also reproduced in video-text representations. Together, these results show that relational convergence extends beyond local neighborhoods to global spanning structure, whereas metric geometry exhibits substantially weaker convergence.

---


### 48. [Can One Adapted Model Do It All? Fine-Tuning Strategy Selection for Customer Support LLMs](https://arxiv.org/abs/2609.27262)

**<font color=#1a73e8>作者：</font>** Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production customer-support systems often require LLMs to support multiple skills, such as intent classification, question answering, summarization, or tool-use decisions. A central deployment question is whether these skills should be handled by separate task-specialist models or by a single model trained through multi-task training, sequential updates, or model merging. We study this question using thirteen models spanning five families (Qwen3, Qwen3.5, Gemma-3, Llama-3.1, and Mistral) from 0.6B to 32B parameters across eight customer-support datasets, spanning four public and four proprietary datasets with approximately 74.5k training and 8.7k evaluation samples. Under a fixed training protocol, we train more than 200 checkpoints. Our experiments reveal that multi-task full fine-tuning is the strongest operational default at every model size we test. Specialist models are strong on their target tasks but often degrade sharply off-task, making reliable routing important. Sequential Low-Rank Adaptation (LoRA) preserves earlier skills better than sequential full fine-tuning, while merging a specialist with its base model improves off-task robustness with limited same-task loss for larger models. We conclude with practical guidelines for selecting fine-tuning strategies in real-world settings.

---


### 49. [CAVEAT: Towards Robust Computer-Use Agents in Incentive-Misaligned Environments](https://arxiv.org/abs/2609.27273)

**<font color=#1a73e8>作者：</font>** Yuxuan Li, Will Epperson, Wesley Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) increasingly act on behalf of users online. What happens when the environments they operate in have incentives that do not align with the user's? In online marketplaces, for example, platforms may favor some products over others, potentially steering agents away from the user's objective. Existing CUA benchmarks cover cooperative settings or explicit attacks, but do not test whether agents preserve user objectives when the environment itself has a stake in the outcome. We introduce CAVEAT, a controlled benchmark spanning nine marketplace environments and a taxonomy of eight common steering mechanisms. Across five model families, agents purchase the user-optimal product in 78.6% of matched-control episodes but only 17.3% when steering mechanisms are enabled. Larger models and increased reasoning improve robustness, but substantial failures persist. Our trajectory analysis and targeted ablations identify three points where steering enters the decision process: (1) agents distort the user's priorities, (2) prematurely narrow the set of alternatives they consider, and (3) commit before resolving decision-relevant evidence. Guided by this diagnosis, we develop CAVEAT-Harness, which directly targets these failure modes and raises user-optimal purchasing by 55.0%. Targeted post-training further improves a smaller open model. These results establish incentive robustness as a distinct challenge for delegated agents, diagnose how it fails, and show that targeted interventions can substantially improve it.

---


### 50. [DRSR: Learning Set-Level Deletion Risk for Efficient Long-Horizon Agents](https://arxiv.org/abs/2609.27276)

**<font color=#1a73e8>作者：</font>** Mingxuan Wang, Bo Wang, Fei Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon language-model agents accumulate reasoning traces, tool exchanges, and observations whose relevance changes with the current decision. Existing compression strategies often score historical units independently, but the safety of deleting several units is generally not determined by their singleton scores: redundant evidence, accumulated small effects, and the information that remains after deletion all matter. We introduce Direct Relational Set-Risk Pruning (DRSR), which formulates agent-history compression as risk-constrained selection over deletion sets. Offline, DRSR constructs exact counterfactual supervision by jointly deleting protocol-valid history Blocks and measuring the change in teacher-forced likelihood of the same recorded next output. A lightweight scorer then predicts set-level harm from online-visible relations between candidate history and the current pre-action state, together with deleted-retained and pairwise set structure. At deployment, DRSR evaluates a small set of structurally valid deletion candidates with the lightweight scorer and removes the largest feasible set under recency, protocol, budget, and learned-risk constraints, abstaining when no set is sufficiently safe. On WorkBuddyBench Full260, DRSR increases mean reward from 0.699 to 0.802 while reducing total model tokens by 20.820%. On the fixed Eval40 comparison, it obtains 0.794 reward at 1.211M tokens per task, using 35.850% fewer tokens than the uncompressed agent. Mechanistic analyses and ablations further show that decision-conditioned relations, retained-context information, pair interactions, and abstention each contribute to reliable pruning.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-172](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

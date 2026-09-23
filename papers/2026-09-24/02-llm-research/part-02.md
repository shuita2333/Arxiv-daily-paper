# 🧠 大模型相关研究 | 2026年09月24日

> 本类共 **206** 篇论文：已确认 **192** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-206](./part-05.md)

---

### 51. [Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference](https://arxiv.org/abs/2609.25537)

**<font color=#1a73e8>作者：</font>** Md Mostafizer Rahman, Md Faizul Ibne Amin, Md Shahajada Mia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) inference is constrained by the quadratic scaling of self-attention and the linear scaling of the KV cache, increasing latency, energy consumption, and GPU memory demand as context length scales. Existing soft-compression methods either lack query-guided memory selection at inference time, train without answer-targeted supervision, or couple compression tightly to a specific decoder architecture. We propose a Context-to-Answer-Aligned Memory Compression (CMC) framework, which compresses long input contexts into compact Context Memory Embeddings (CMEs) aligned to any frozen decoder's embedding space, reducing inference costs without modifying decoder weights. CMC introduces a two-tier KV cache that combines question-guided CME selection with a local context window, and trains the compressor with answer-targeted distillation from a frozen LLM. Experiments across nine encoder-decoder combinations and four QA benchmarks show that CMC consistently outperforms the baseline, achieving up to 7.3 EM and 4.0 F1 point gains on SQuAD, while reducing inference time and energy consumption by up to 20% and peak reserved GPU memory by up to 50% at 3,000 generation tokens. Ablation studies confirm that each architectural component and training objective contributes to the performance.

---


### 52. [SambaGraph: Action-Reaction Spatio-Temporal Graphs for Soccer Tactical Response Modeling](https://arxiv.org/abs/2609.25569)

**<font color=#1a73e8>作者：</font>** Abel A. Reyes-Angulo, Henry O. Velesaca, Steven Araujo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Soccer tactics are interactive: an attacking action changes the opponent's defensive problem, and the observed response depends on the multi-agent match state. We introduce SambaGraph, an action--reaction spatio-temporal graph dataset and benchmark for soccer tactical response modeling. From tracking and event data for all 64 matches of the 2022 FIFA World Cup, we curate 4,070 action-centered episodes represented as temporally aligned 23-node player--ball graph sequences with attack/defense views, response labels, and 26,270 split-safe attack--defense pairs. We study three questions: whether observed responses can be classified from graph episodes, whether successful defenses can be retrieved for a query attack, and whether graph-derived summaries support grounded LLM reasoning. A compact signature MLP obtains $0.796\pm0.007$ macro-F1 for response classification, while a fused graph--signature dual encoder reaches $0.471\pm0.029$ Hit@5 and $0.655\pm0.051$ Hit@10 for full-bank defensive retrieval. Hard negatives maximize pair discrimination but not retrieval quality. Local LLMs underperform supervised encoders for direct classification and do not improve over a strong original order in eight-candidate reranking, but they provide grounded tactical rationales. These results position SambaGraph as a reproducible benchmark for graph-based soccer strategy-response research. Code and dataset are available at: this https URL.

---


### 53. [Recovering Agentic Sovereignty: Mitigating the Consensus Paradox via Contrastive Epistemic Decoding](https://arxiv.org/abs/2609.25570)

**<font color=#1a73e8>作者：</font>** Dahlia Shehata, Ming Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit a parametric vulnerability to adversarial swarm consensus. To mitigate this sycophancy, we introduce Contrastive Epistemic Decoding (CED), a zero-shot inference intervention. Unlike standard Contrastive Decoding (CD) which relies on a weaker secondary model, CED utilizes a dual forward-pass on a single architecture to isolate conformity bias. By introducing a novel asymmetric, zero-bounded probability clamp and discrete top-k truncation mask, CED mathematically suppresses toxic consensus tokens without causing grammatical collapse. Evaluated across 7,200 paired trajectories on complex benchmarks (GAIA, SWE-bench, Multi-Challenge) using Gemma-2 (9B), Llama-3.1 (8B), and Mistral v0.3 (7B), CED successfully neutralizes architectural and positional biases. By reducing cognitive loafing by up to 33.00% absolute, CED drives significant performance gains, yielding up to a 30.75% accuracy recovery. Regaining sovereignty induces distinct architectural behaviors---passive task-focus in Gemma-2 and active refutation of the simulated swarm in Llama-3.1---showing CED decouples compliance from capability without fine-tuning.

---


### 54. [A Behavioral Trait Leaks into Preferences: Diagnosing Trait Interference in LLM User Simulators](https://arxiv.org/abs/2609.25572)

**<font color=#1a73e8>作者：</font>** Chaehyun Kim, Sein Kim, Hongseok Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based user simulators aim to bridge the offline-online gap in recommender evaluation by emulating users through injected traits, where preference attributes determine what a user engages with and a behavioral activity trait governs how long they browse. However, we show this intended trait independence collapses during simulation, causing two failures: (i) Trait Interference, where amplified activity distorts preference boundaries and forces interactions with mismatched items to sustain browsing, and (ii) Evaluation Invalidity, where satisfaction scores inflate with activity-driven page counts despite taste mismatches, biasing evaluation toward trait distributions rather than recommender performance. To resolve this, we propose PQA, a page-level quality anchoring method that guides simulators using a personalized anchor reflecting each user's intrinsic preference standard. By assessing whether a page meets this standard before further browsing, PQA enables proactive exits from low-quality pages, letting the activity trait retain its intended role of modulating browsing depth within preference-conforming pages. Experiments show PQA mitigates trait interference and improves the reliability of LLM-based simulator evaluation under activity shifts. Our code is available at this https URL

---


### 55. [Direct Optimization of Generators for Search in Automated Theorem Proving](https://arxiv.org/abs/2609.25575)

**<font color=#1a73e8>作者：</font>** Adam Ousherovitch, Ambuj Tewari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuned Large Language Models (LLMs) significantly advance Automated Theorem Proving (ATP), but are often deployed as guiding policies within tree search rather than for single-attempt generation. Recent work shows cross entropy is suboptimal for an LLM used in flat search strategies such as aggregation or filtering and that work has developed new loss functions to correct this misalignment. Extending this alignment to tree search is more challenging: proof discovery depends on exploration and recovery through off-trace states that supervised demonstrations do not reveal. We extend Compute-Aligned Training (CAT) to this setting through an abstraction of policy-guided search, deriving tractable, trace-supported losses. Alongside these search-aware losses, we introduce a search-agnostic uniform-allocation (UA) loss that accounts for the budget without specifying the specific search. Both induce scalar weights on per-tactic cross-entropy gradients. We characterize how off-trace behavior affects the search-aware weights, including conditions for vanishing approximation error at large budgets. On a Lean benchmark, both approaches achieve higher observed proof-success rates than cross-entropy across six search strategies, with strong results from a single shared UA adapter. Budget sweeps show larger gains over cross-entropy at 16 than at 256 expansions, implying CAT scales with test time compute.

---


### 56. [Deflecting the Value Compass: Interacting with Large Language Models Temporarily Shifts Human Value Priorities Toward Personal Focus](https://arxiv.org/abs/2609.25586)

**<font color=#1a73e8>作者：</font>** Hasibur Rahman, Malak Sadek, Smit Desai  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly support decisions where values are in tension, yet little is known about whether interacting with them changes which values users prioritize. In a preregistered study, 200 U.S. adults interacted with ChatGPT, Claude, or Gemini as a thinking partner or read fixed AI-generated considerations. The prompt asked LLMs to support reasoning without recommending a decision and named no values. Participants advised people facing real dilemmas and completed parallel PVQ-RR forms before, immediately after, and one task later. Each LLM condition temporarily shifted value priorities toward personal focus relative to the control (d=0.37-0.51), primarily through increased Self-Enhancement. Participants' advice retained words and meaning from their exchanges. Thus, a brief LLM interaction that neither targets values nor seeks to persuade can reorient values active during judgment without detectable convergence in value directions or advice.

---


### 57. [Evaluating Coding Agents on Kernel Exploit Generation](https://arxiv.org/abs/2609.25591)

**<font color=#1a73e8>作者：</font>** Junyoung Jang, Gwanhyun Lee, Hwiwon Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents now find real vulnerabilities in production software. However, bug discovery results do not measure whether agents can construct exploit primitives. We introduce KEX-bench, a benchmark for evaluating coding agents on exploit primitive generation against real operating-system kernels. KEX-bench contains 45 task instances across 40 Linux and Windows CVEs, covering kernel address leak, instruction-pointer control, heap read, heap write, and arbitrary address write. Each task runs in an isolated virtual machine, exposes controlled tools, and uses a deterministic verifier to check primitive-specific success. We evaluate state-of-the-art coding agents paired with frontier and open-weight models under fixed tool-call budgets. Without a reference proof of concept (PoC), the strongest configuration solves 1 of 20 Windows tasks (5.0%) and 14 of 25 Linux tasks (56.0%). With a reference PoC, the strongest configuration solves 31 of 45 tasks (68.9%). This highlights the gap where agents reach kernel crashes but fail to shape kernel state into exploit primitives. We release KEX-bench for reproducible research on AI-assisted exploitation at this https URL.

---


### 58. [Rewired or Gated? How Instruction Tuning Shapes Knowledge-Conflict Circuits in LLMs](https://arxiv.org/abs/2609.25602)

**<font color=#1a73e8>作者：</font>** Shubham Santosh Pandere, Gautam Ranka, Ritika Varshney 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In language models, the choice between believing the prompt and believing the weights is made by a handful of identifiable attention heads. Instruction tuning changes how models behave under conflict, but whether it rewires the underlying circuit or merely gates/reweights already present components, remains unknown. We provide the first mechanistic base-vs-instruct comparison of conflict-resolution circuits, across three families (Llama-3.2-3B, Qwen-2.5-3B, Gemma-3-4B). Five independent methods, node and edge attribution, superposition role analysis, causal ablation, and path patching, converge on gating, with the same heads, in the same late-layers, are found to be reweighted rather than replaced with a high node overlap (0.60-0.82). Behaviorally, tuning shifts models toward parametric memory, making instruct models reject a terse counterfactual context far more than base ones, the opposite of a naive user-following expectation. Yet this added skepticism is a factor of framing since it disappears when the same false claim is delivered as a coherent, evidential passage. The robustness that instruction tuning buys against terse injection is therefore real but narrow. More broadly, we believe that because the conflict circuit is preserved rather than rebuilt, interpretability and control tools calibrated on base models should transfer directly to their deployed instruct siblings.

---


### 59. [ArticleMiner: Ontology-Guided Knowledge Graph Construction from Scientific Publications](https://arxiv.org/abs/2609.25607)

**<font color=#1a73e8>作者：</font>** Md Abrar Jahin, Craig A. Knoblock, Jay Pujara  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific papers keep much of their quantitative content in tables and supplementary files, where a number means something only through its header, caption, unit, analytical method, and the conventions of its field. Recovering the rows and columns of a table is therefore not the same as recovering the scientific fact it reports. Most semantic table-interpretation methods assume that a clean table is already available and subsequently map its cells or columns to ontology terms, whereas most publication-level extraction systems are designed for a single domain. We study a middle path: a shared process that reads a paper and its supplementary files, gathers evidence from several parsers and a language model, and reconciles that evidence, while a bounded human-authored task module for each task supplies the domain meaning. The module lists the canonical names the graph may use, the surface forms that map to them, a small set of derivation rules and validity constraints, an identity key, and the bindings used to write RDF. It defines what a task is allowed to emit; it does not try to list every convention of a field. We build four such modules (for drug-discovery chemistry, materials science, machine learning, and mineral geochemistry) in the ArticleMiner framework, and evaluate them on 163 papers, including a new geochemistry benchmark with expert-curated ground truth. In comparisons against a same-LLM few-shot baseline, the point estimates favor ArticleMiner on all four tasks, with uncertainty on the two smaller benchmarks. The geochemistry comparison also includes access to supplementary files, so its improvement cannot be attributed to domain guidance alone.

---


### 60. [Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611)

**<font color=#1a73e8>作者：</font>** Qwen Team  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Qwen3.8-Omni-Flash, a natively multimodal agentic model for real-world multimodal productivity. Compared with previous omni models, which primarily emphasized perception and interaction, Qwen3.8-Omni-Flash substantially improves multimodal understanding and reasoning, as well as performance on long-horizon agentic tasks. These capabilities are supported by a native multimodal co-training strategy that preserves strong text-domain capabilities while facilitating the transfer of agentic capabilities from text to audio and video tasks. The model inherits the sparse mixture-of-experts (MoE) architecture of Qwen3.8-Next and extends the context window to one million tokens, supporting long-context multimodal reasoning and long-horizon planning. These advances enable integration into production workflows as a primary agent or a specialized sub-agent, supporting video editing, long-form audio and video translation, music-conditioned music video or movie generation, and video-based note or omni-skill creation. To address the lack of native audio and video support in existing agent harnesses, we release Qwen-MM-Plugins, a lightweight open-source plugin framework for multimodal productivity. We further frame real-time multimodal interaction as a system-level challenge requiring orchestration of context and memory management, tool use, and sub-agent delegation. Accordingly, we release Qwen-Live-Harness, an open-source framework for building responsive, real-time multimodal agents based on Qwen3.8-Omni-Flash. Extensive evaluations demonstrate that Qwen3.8-Omni-Flash achieves strong performance across multimodal understanding, reasoning, long-horizon agentic execution, and video productivity tasks. These results and the accompanying open-source tools support Qwen3.8-Omni-Flash as a practical foundation for deploying natively multimodal agents in research and production.

---


### 61. [Reasoning-Preserving Fine-Tuning of Post-RL LLMs with Null-Basis LoRA](https://arxiv.org/abs/2609.25618)

**<font color=#1a73e8>作者：</font>** Wenzhi Fang, Nicholas Tzou, Lazar Valkov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL)-based post-training has become an effective approach for eliciting reasoning capabilities in large language models (LLMs). However, adapting post-RL models to new knowledge domains or behaviors through subsequent supervised fine-tuning (SFT) can severely overwrite these capabilities. Existing approaches mitigate such forgetting through experience replay, specialized initialization, or constrained optimization using gradient projection, but either provide limited preservation or incur substantial training overhead. Our analysis shows that reasoning activations concentrate in low-dimensional subspaces, leaving substantial null-space capacity for adaptation, and that the corresponding approximate null spaces can be reliably estimated from a modest number of examples. Motivated by these observations, we propose Null-Basis Low-Rank Adaptation (NB-LoRA), a parameter-efficient method for adapting post-RL LLMs while preserving their acquired reasoning ability. We formulate reasoning retention as a layer-wise hidden-state preservation constraint and construct a fixed approximate null basis from reasoning activations. LoRA updates are then reparameterized through this basis, enforcing the preservation constraint throughout fine-tuning. Extensive experiments across multiple RL-trained LLMs and diverse downstream tasks show that NB-LoRA matches standard LoRA in adaptation performance, maintains reasoning accuracy near pre-fine-tuning levels, and generalizes this preservation to held-out reasoning benchmarks.

---


### 62. [ChatT2: An Adaptive Framework for Developing a Large Language Model-Based Agent for Natural Product Domain Research](https://arxiv.org/abs/2609.25620)

**<font color=#1a73e8>作者：</font>** Yihan Wang, Qiandi Gao, Yihui Zhuang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific investigations into microbial natural products (NPs) present significant challenges for novices, largely due to the complexity of microbial systems, biochemical diversity, technical skill requirements, and the demands of bioinformatics and data analysis processes. To address these issues, we introduce ChatT2, a large language model (LLM)-based agent that is specifically tailored to the unique characteristics of bacterial type II polyketides. These polyketides form a structurally distinct and therapeutically important NP family. ChatT2 was developed within an autonomous multiagent framework composed of a mentor, an executor, and an evaluator, each with defined responsibilities. The mentor acts as an intermediary between ChatT2 and the user, utilizing chain-of-thought prompting to refine the intent of the user. Under the guidance of the mentor, the executor synthesizes multimodal information via retrieval-augmented generation techniques and seamlessly integrates bioinformatics and cheminformatics tools. The evaluator ultimately assesses the output of the executor to ensure the richness and accuracy of the retrieved information. Our research highlights how ChatT2, designed with this multiagent framework, addresses the challenges faced by general LLMs in terms of understanding limited, specialized corpora and complex biological information and provides both experts and novices with a valuable tool for exploring various NPs of interest. The ChatT2 webserver can be accessed at this https URL.

---


### 63. [Shallow to Deep: Aligning Token Pruning with Stage-wise Roles in LVLMs](https://arxiv.org/abs/2609.25635)

**<font color=#1a73e8>作者：</font>** Shuo Zhang, Jintao Tong, Yixiong Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) incur high computational costs from redundant visual tokens. Although training-free attention-based multi-layer pruning in the vision encoder stage has been explored as an effective strategy, we find that pruning in shallow layers consistently degrades performance. In this paper, we aim to understand this problem and seek a solution. By analyzing attention patterns across network depth, we find that shallow layers primarily function as edge detectors with chaotic attention maps, while deeper layers transition through local subject recognition and unstable semantic aggregation. To address the misalignment between pruning strategies and network stages, we propose STD, a hierarchical token pruning framework that adapts token selection mechanisms to the functional role of each network stage. STD employs High-Frequency Spectral Analysis in shallow layers to deterministically preserve structural edges, uses Gaussian-Smoothed Attention in intermediate layers to maintain spatial coherence, and introduces a Stability-Adaptive Trigger in deep layers to execute pruning only during semantically stable phases. Extensive experiments show that STD outperforms state-of-the-art pruning methods by 1.1% on LLaVA-1.5-7B with 88.9% token reduction, while also being plug-and-play and highly effective when combined with other methods, and by 2.1% on LLaVA-NeXT-7B with 94.4% reduction, delivering a 3.9x speed-up in the prefilling stage. Our code will be released at this https URL.

---


### 64. [SLED-IFV: Solver-Validated LLM-Guided Decomposition for Scalable Hardware Information-Flow Verification](https://arxiv.org/abs/2609.25637)

**<font color=#1a73e8>作者：</font>** Liangtao Dai, Yimin Gao, Melika Morsali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Formal hardware information-flow verification (IFV) provides strong guarantees against secret-dependent timing and control behavior, but often scales poorly on realistic RTL. We identify two recurring proof barriers in self-composed IFV: implementation complexity, where proof-hard datapath logic dominates even though the property needs only a compact boundary relation, and relational inductive complexity, where the proof depends on cross-copy public-control facts that the backend prover does not infer efficiently. To address them, we introduce two semantic proof decomposition forms: functional simplification, which replaces a proof-hard RTL region with a validated over-approximate summary, and relational strengthening, which exposes and proves the cross-copy relations needed for induction. We further present SLED-IFV, a solver-validated LLM-guided flow that automates the selection of these forms and their concrete targets. Given a self-composed miter and an oracle-free decision sheet, the LLM proposes a decomposition, then materializes it into proof artifacts under controller checks. The controller compiles the checked artifacts into proof obligations, and the formal verification backend remains the sole authority for acceptance. Across nine nontrivial benchmarks constructed from real RTL, SLED-IFV achieves up to 603x solver-only speedup and converts two 12-hour timeouts into completed proofs. The closed-loop flow produces verifier-accepted decompositions for all cases.

---


### 65. [Ladders of Thought: A Self-Evolving Curriculum of Progressively Simplified Reasoning Traces](https://arxiv.org/abs/2609.25643)

**<font color=#1a73e8>作者：</font>** Minghui Liu, Thomas Magelinski, Dehao Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at reasoning when scaled to hundreds of billions of parameters, but small- and mid-scale models remain brittle reasoners even with knowledge distillation (KD). We present Ladders-of-Thought (LoT), a framework that improves reasoning by combining progressive question rewrites with a self-evolving curriculum. LoT automatically generates semantically faithful but easier variants of reasoning problems, organizes them into difficulty buckets using step-based measures, and employs a self-evolving bandit scheduler to allocate training adaptively. Evaluated on two reasoning domains, math and multi-hop reasoning, across 1-8B models from different families, LoT consistently improves over KD. It delivers large gains on arithmetic tasks (e.g., +32 percentage points on AddSub, +25pp on SVAMP), +2-8pp improvements on in-domain test splits, and strong though dataset-dependent benefits on multi-hop reasoning (e.g., +16pp on QASC, +25pp on StrategyQA). LoT also converges faster than staged curricula, highlighting the value of adaptive progression. These results show that progressive rewrites coupled with adaptive curricula provide a simple yet effective recipe for strengthening reasoning in smaller LLMs.

---


### 66. [Efficient Cost-Aware LLM Evaluation via Bayesian Bandit Gittins Indices](https://arxiv.org/abs/2609.25645)

**<font color=#1a73e8>作者：</font>** Qian Xie, Yueli He, Nairen Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exhaustively evaluating every candidate LLM configuration on every benchmark item to identify a high-performing one is costly. We formulate configuration selection as a cost-aware Bayesian bandit problem and propose GittinsEval, which draws on the Bayesian-optimal Gittins policy to determine which configuration to evaluate next and when to stop. We extend the policy with an anytime recommendation rule over both fully and partially evaluated configurations, using an LCB-style score to account for posterior uncertainty. GittinsEval is computationally efficient, requiring only lightweight online updates after offline precomputation. Across GSM8K, PIQA, AlpacaEval, and MMLU response matrices, GittinsEval is consistently competitive, with particularly strong gains over configuration-level Bayesian optimization on large-example benchmarks and over cost-unaware bandit baselines on large-candidate tasks. Crucially, GittinsEval often attains near-zero simple regret using only 1% to 2% of the exhaustive-evaluation cost; it also offers an adaptive stopping rule that typically triggers at 1% to 10%.

---


### 67. [Testing-Driven Reliability Audit of Trajectory-Based Early Outcome Prediction for LLM Agents: Target-Specific Calibration Transfer Persists Within a Single Benchmark](https://arxiv.org/abs/2609.25647)

**<font color=#1a73e8>作者：</font>** YanZe Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting early outcomes based on trajectory can decrease the expenses associated with agent evaluation by terminating a run once the outcome becomes sufficiently predictable, assuming that the predictor's confidence is properly calibrated. Calibration is at risk when a predictor is applied to an agent on which it was never trained, but it is not known whether such transfer failures are broad across agent systems or concentrated in specific target agent/head combinations. Using public SWE-bench Verified trajectories and a frozen dual-head early-outcome prediction pipeline, we ran a leave-one-agent-out calibration audit, a shared-predictor leave-two-agents-out control, oracle prior correction, and a robustness battery over training cohorts, task resampling, task halves, jackknife, and thresholds. Fixed-scaffold TerminalBench analysis served as a pre-registered boundary test. Broad same-predictor pairwise heterogeneity was not supported; the median pairwise corrected-gap differences were 0.0180 (SUCCESS head, 45 pairs) and 0.0385 (FAILURE head, 35 pairs), and the pre-registered heterogeneity criterion was not met on either head. Two specific combinations, gpt-5-mini/SUCCESS and claude-opus-4.6/FAILURE, showed persistent calibration-transfer errors (median corrected gaps 0.1377 and 0.1107) without a sign reversal under any frozen control. TerminalBench did not establish cross-benchmark replication: the success target produced zero decisions (INDETERMINATE), and the failure target did not satisfy the pre-registered persistence criterion. Therefore, a strong target-specific calibration-transfer error can exist within one frozen environment, but the evidence does not establish that the error is intrinsic to the model or general across benchmarks.

---


### 68. [SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs](https://arxiv.org/abs/2609.25651)

**<font color=#1a73e8>作者：</font>** Jingying Wang, Rosiana Natalie, Marquise D Singleterry 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Surgical videos are a primary resource for teaching trainees anatomy, tool usage, and procedural skills. Yet learning from them at scale requires systems that understand surgical scenes. Existing approaches fall short: vision-language models lack fine-grained domain reasoning, task-specific models do not generalize, and prior scene graphs omit clinically meaningful detail. We present SurgGraph, a training-free pipeline that generates quantitative scene graphs from surgical videos. Operating on segmentation masks and depth maps, SurgGraph encodes each clinically meaningful relation (attachment, occlusion, separation, tool actions) as a <subject, verb, object, value> tuple whose numeric value quantifies the relation's extent over time. Technical evaluations show more precise scene understanding than state-of-the-art surgical VLM baselines. We then build SurgGraphQA, a proof-of-concept learning application that retrieves meaningful and boundary-case exemplars and generates visual explanations and feedback. A study with 17 medical students and 2 resident surgeons shows significant learning gains, demonstrating its educational value.

---


### 69. [From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs](https://arxiv.org/abs/2609.25655)

**<font color=#1a73e8>作者：</font>** Zhentao Tan, Chang Liu, Yao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) scale rapidly, dense full-parameter adaptation becomes increasingly expensive, motivating sparse and modular architectures such as Mixture-of-Experts (MoE) models. This shift raises a key question for parameter-efficient fine-tuning (PEFT): at what granularity should parameters be selected and updated? Existing PEFT methods such as LoRA operate on predefined weight matrices, while expert-level sparse tuning methods update entire selected experts. However, we observe that activated experts are internally sparse, with only a small fraction of intermediate channels strongly responding to downstream tasks, indicating that expert-level adaptation is still too coarse. We propose NSFT (Neural Sub-expert Fine-Tuning), a fine-grained PEFT framework that refines MoE adaptation from experts to sub-experts. NSFT decomposes each expert along the intermediate dimension into structured channel groups and selects task-relevant sub-experts by combining routing importance with intra-expert activation saliency. To optimize sparse partial updates, NSFT further introduces learning-rate scaling and dynamic gradient scaling to compensate for the reduced effective update magnitude. Experiments on OLMoE and Ling-mini-2.0 across challenging domain-specific tasks and general benchmarks show that NSFT consistently outperforms representative PEFT and expert-level sparse tuning baselines, while using substantially fewer trainable parameters and preserving competitive general capability. These results suggest that sub-expert-level adaptation is a more precise and efficient PEFT paradigm for MoE LLMs.

---


### 70. [From Utterances to Networks: Modelling Slang Adoption and Diffusion Across Subreddits](https://arxiv.org/abs/2609.25669)

**<font color=#1a73e8>作者：</font>** Xiaoning Wang, Ted Underwood, Zhewei Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adoption and diffusion of neologisms in online communities have received renewed attention in recent years. As internet slang terms such as APT, referring to a K-pop song, and phrases such as Canon Event meaning an embarrassing but pivotal event, go viral online, it becomes increasingly important to understand the mechanisms that contribute to their success. Prior studies have often explained slang diffusion either from the perspective of social interaction or from the linguistic properties of the slang itself, but rarely from both perspectives together. One major obstacle has been the high cost of annotating slang usage in large-scale online communication. Recent advances in large language models (LLMs), however, make it possible to use them as scalable annotators for such tasks. In this study, we first curate a human-annotated benchmark to evaluate LLM performance in detecting slang usage in real Reddit communication. We then leverage LLM-based annotations to model slang adoption and diffusion. Our results show that slang diffusers with higher bridging capital are associated with increased subsequent adoption, whereas diffusers with higher bonding capital are associated with reduced adoption. We also find that wider contextual usage of a slang term is associated with a longer time before new users officially adopt it. Together, these findings suggest that both social-network structure and linguistic context shape the diffusion of neologisms in online communities.

---


### 71. [Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest Visual Marketing](https://arxiv.org/abs/2609.25677)

**<font color=#1a73e8>作者：</font>** Yi-Lin Tsai, Yung-Hsiu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Marketers now deploy generative AI agents as synthetic consumers to pretest visual assets such as logos, packaging, and advertising at a fraction of human-panel cost. However, this procedure assumes that a model seeing a visual cue can also perceive its consumer meaning, which is largely untested. We stress-test the assumption using six canonical visual marketing experiments, varying the two levers managers control: model generation (GPT-4o-mini vs. GPT-5.4-mini) and input format (plain text vs. JSON). Every resulting configuration passed the manipulation checks; however, none of the configurations reproduced more than two of the six human effects, and the remainder were nonsignificant. The one exception was a significant reversal of the human pattern. Providing conceptual or empirical evidence through in-context learning steers average responses toward the human effect. Yet steering has a limit: even when it succeeds, a configuration reproduces less than half of the natural spread of human responses and so understates consumer heterogeneity. We integrate these results into an AI governance protocol (Calibrate, Intervene, Deploy) that delineates when synthetic consumers can responsibly screen creatives and when human panels remain necessary.

---


### 72. [Toolcompass: Guiding Tool Trialing, Not Suppressing It](https://arxiv.org/abs/2609.25678)

**<font color=#1a73e8>作者：</font>** Junlin Fang, Chong Zhang, Do Nguyen-Thanh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents must generalize from tools seen during training to unseen tools at deployment. A key challenge is tool trialing, i.e., excessive trials waste the interaction budget, whereas selective trials enable exploration of unfamiliar tools. Existing outcome-based post-training leaves wasteful trials unguided, while turn-level supervision may suppress necessary exploration. We introduce ToolCompass, a post-training framework that guides tool trialing by organizing tool-call representations according to shared functions. Specifically, ToolCompass models each function class as a von Mises--Fisher distribution and jointly reduces intra-function variation across domains and increases inter-function separation. This structure transfers experience from seen tools to functionally similar unseen tools, directing exploration away from unrelated alternatives. ToolCompass requires no ground-truth call traces or unseen-tool access and incurs no inference overhead. Experiments on AppWorld and FTRL show consistent gains across GRPO, RFT, and DMPO. improves AppWorld OOD task success by up to 10.71 percentage points over vanilla post-training and performs best among competitive baselines on both benchmarks.

---


### 73. [C-to-Rust Fallacy: Automatic Refactoring != Memory Security](https://arxiv.org/abs/2609.25682)

**<font color=#1a73e8>作者：</font>** Hung-Mao Chen, Xu He, Bo Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rust has emerged as the leading system programming language, offering strong memory and type safety guarantees without compromising performance. This positions it as a compelling alternative to traditional languages like C and C++, which are susceptible to memory security bugs. However, manually transforming C to Rust requires in-depth domain knowledge of the Rust language features, which requires significant effort for developers. To address this, tools for automatic C-to-Rust refactoring aim to generate safe Rust code leveraging static analysis and Large Language Models (LLMs). While these tools claim to achieve safety by reducing the unsafe Rust, the correlation with improving security is not clear. In this paper, we conduct a comprehensive empirical study on the reliability, safety, and correctness of various C-to-Rust refactoring methods. Specifically, we evaluate C2Rust-analyze, CROWN, C2SaferRust, and FLOURINE using a dataset of 116 C programs with memory security bugs from the NIST Juliet Test Suite. Based on 464 Rust programs generated by these tools, our evaluation focuses on three key aspects: the compilation correctness of the refactored programs, the effectiveness in mitigating original C bugs, and the tendency to introduce additional Rust bugs. The results indicate that 342 Rust programs fail to compile, 177 Rust programs inherit memory security bugs from the original C programs, and 77 new Rust bugs are introduced. We examine the rationale behind tool design and analyze the root cause of errors across various refactoring methods. Our findings indicate that current automated refactoring tools deliver memory safety as they define it, but not the broader memory security when adopting them.

---


### 74. [How Strongly Should Task State Influence an LLM Agent?](https://arxiv.org/abs/2609.25686)

**<font color=#1a73e8>作者：</font>** Chenyu Zhang, Wonbin Kweon, Jiawei Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon assigned work requires an LLM agent to track the state of a task: which steps are done, blocked, cancelled, or open to repetition. Agent systems either keep this state as text in the prompt and rely on the model to read that text, or move the state into a module that enforces it, and each system is evaluated as a whole, so no one knows how much reliability comes from the state being shown, told, or enforced. We fix the task rules, the model, and paired episodes and vary how strongly task state reaches the agent: a raw transcript, an exact checklist, per-turn directives from a state machine compiled from the brief and advanced only by execution receipts, or an enforcement gate on that machine that refuses state-violating actions; every episode is scored by exact payload matching against dynamic ground truth. Across three models, two reasoning regimes, and two domains, four findings hold without per-turn reasoning: displaying accurate state is unreliable, an unverified ledger the agent writes itself beats an accurate checklist it is shown, directives help in proportion to the model's obedience, and enforcement needs no obedience but is bounded by the correctness of its state and by the matcher that maps requests to steps; per-turn reasoning at a 235B agent compresses these separations without repairing the text rungs. The same gate, compiled from $\tau^2$-bench's airline policy, raises a 235B agent's pass$^1$ from 0.39 to 0.54 and changes nothing for a 35B agent that rarely violates the policy; on PM-Bench, where acting turns on recognizing a cue rather than on state, showing the record is the best rung--matching or beating both gates and reversing the ledger-over-checklist finding--and enforcing the matcher's judgement drops a 35B agent below its raw transcript. Enforcement pays when failures are state-decidable and frequent, and hurts when the gate's judgement is wrong.

---


### 75. [Harnessing LLMs Without Surrendering Control: Delegation Boundaries in Visual Data Storytelling Authoring](https://arxiv.org/abs/2609.25700)

**<font color=#1a73e8>作者：</font>** Zhuojun Jiang, Yuki Ueno, Chris Bryan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite the emergence of large language models (LLMs) for visual data storytelling workflows, there are open questions about how authors decide what activities or tasks to entrust to them and what should be "protected" or maintained under human control. To investigate this, we interviewed a cohort of 12 expert visual data storytellers. Our analysis shows that participants rarely treated LLMs as autonomous storytellers. Instead, they tend to selectively delegate execution-oriented tasks to LLMs while retaining control over activities that shape narrative intent and story meaning. Our findings show that LLM assistance is most productive after human seeding and constraint-setting, and that it shifts labor from production to verification. We discuss design implications for boundary-aware authoring tools, data-grounded generation, low-fidelity ideation, and reporting practices for LLM-based visualization research. Supplemental materials for this paper are available at this https URL.

---


### 76. [TCMaster: Confidence-Aware Querying and Workload-Guided Physical Design for Multi-Source Traditional Chinese Medicine Knowledge Graphs](https://arxiv.org/abs/2609.25712)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Yuzhu Li, Haoxuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-source knowledge graphs (KGs) need query mechanisms that expose reliability and exploit domain structure. This paper presents TCMaster, a property-graph query substrate for confidence-aware traversal and workload-guided physical design over Traditional Chinese Medicine KGs. TCMaster integrates pharmacopoeias, prescriptions, molecular databases, and LLM-extracted micro-semantics into a KG with approximately 221K entities and 723K base edges. It annotates edges with provenance-level confidence, rewrites Cypher queries with confidence predicates, ranks multi-hop paths under PRODUCT, MIN, or weighted-average policies, and uses ontology skew through direction selection, herb-attribute bitmaps, and materialized shortcut edges. On Neo4j, direction selection improves attribute lookup by a factor of 1.47, shortcuts accelerate high-fanout target counting by a factor of 4.42, confidence filtering removes 39.3 percent of low-quality heterogeneous paths, and KG retrieval improves TCMbench QA accuracy by 20.0 percentage points.

---


### 77. [LingLan: An Advancing Traditional Chinese Medicine Diagnosis LLM with Multimodal Data](https://arxiv.org/abs/2609.25715)

**<font color=#1a73e8>作者：</font>** Zheng Chen, Zhicheng Du, Haoxuan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Though artificial intelligence (AI) increasingly transforms modern medicine, its integration into Traditional Chinese Medicine (TCM) has been relatively slow, primarily due to TCM's reliance on holistic, subjective diagnostic methods---namely Inspection, Auscultation and Olfaction, Inquiry, and Palpation(I-AOI-P)---which are difficult to align with quantitative, standardized medical systems. In this work, we introduce a Unification Framework for Multimodal Data (UFMD), which automatically processes tongue and pulse images into structured, clinically standard descriptions, integrating multi-source diagnostic information into a unified digital record of I-AOI-P process. Building on this structured data, we create LingLan-14B, a TCM-specific large language model fine-tuned via supervised learning to emulate the diagnostic logic and workflow of I-AOI-P process. Experimental results show that our method significantly enhances diagnostic accuracy, achieving a relative improvement of 103.5% over the baseline (62.72% vs. 30.82%) and reaching an F1-score of up to 82%.

---


### 78. [Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages](https://arxiv.org/abs/2609.25721)

**<font color=#1a73e8>作者：</font>** Ryan Vo, Duc-Vu Nguyen, Matt Kretchmar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly trained on the outputs of other models, forming chains that we call lineages, in which a trait present in one generation can pass to the next. Prior work on subliminal learning has shown that a teacher's trait can transmit to a student through filtered data carrying none of the trait's content. However, the evidence covers only a single training step. We study whether such a trait holds or fades across lineages. We instill the trait into three copies of Qwen2.5-7B-Instruct and iterate the training step to depth ten from each, reading every generation two ways on the same held-out prompts: a keyword screen that looks for expressions of the trait in the model's output, and an activation probe that projects each model's displacement from the base onto a direction built from the other lineages' teachers. We report two findings. First, the trait persists through ten generations across three lineages. The instilled models express it on every completion; the keyword-screen rate falls to 55.6% after the first step and to 21.1% by generation ten. The base itself matches the screen on none of its 300 completions. Second, the trait can be present internally while absent behaviorally. When the model's default system prompt is removed at evaluation, the generation-ten students' keyword-screen rate is zero on every prompt while the probe score stays positive on every prompt. Steering the untreated base with the displacement of a generation-ten student, which is trained and measured under the default system prompt, induces screened expression of the trait even with the system prompt removed, while that same student shows no expression of the trait with the system prompt removed.

---


### 79. [Modular Norm RandOpt: Population-Efficient Ensembling through Architecture-Aware Perturbations](https://arxiv.org/abs/2609.25745)

**<font color=#1a73e8>作者：</font>** Kirato Yoshihara, Hiroaki Hamade  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RandOpt samples weight-perturbed language models and ensembles top-ranked candidates through plurality voting, but its global perturbation scale ignores heterogeneous module geometry. We propose \mbox{\textbf{\emph{Modular Norm RandOpt}}}, an architecture-aware sampling method using module-wise natural norms and calibrated scales while preserving selection and voting. It outperforms RandOpt using $3\times$ fewer candidates on Countdown and at least $12\times$ fewer on GSM8K, with corresponding wall-clock savings. Evaluations across seven tasks and three Qwen scales ($0.5$B--$3$B) show higher mean accuracy than RandOpt on Countdown, GSM8K, and MATH-500 at every scale. The gains extend to Llama 3.2 $3$B and Gemma 3 $4$B on Countdown and GSM8K. On Qwen2.5-1.5B, our ensembles also achieve higher mean accuracy than iterative baselines on both tasks at comparable main-run evaluation budgets. On GSM8K, a tail-density diagnostic implies only a $1.2$--$1.8\times$ candidate reduction, while most ensemble improvement is associated with more favorable correct-expert support. These results highlight perturbation geometry as a key design choice for population-efficient, gradient-free search around pretrained models.

---


### 80. [Syndrome, Synergy, and Safety: Structured Reasoning and Knowledge-Driven Alignment for TCM Prescription Generation](https://arxiv.org/abs/2609.25755)

**<font color=#1a73e8>作者：</font>** Zheng Chen, ZhiCheng Du, Haoxuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Applying large language models to Traditional Chinese Medicine (TCM) prescription generation reveals three clinically critical gaps: models produce end-to-end mappings without auditable reasoning following the li-fa-fang-yao paradigm (SR Gap), treat each encounter in isolation without follow-up adjustment via sui zheng jia jian (LA Gap), and fail to enforce absolute contraindication rules such as Shi Ba Fan (SC Gap). We propose a progressive four-stage framework (SFT $\to$ PG-CoT $\to$ Dynamic $\to$ K-RL) that addresses each gap: PG-CoT constrains CoT distillation under the li-fa-fang-yao paradigm to produce auditable diagnostic chains, Dynamic SFT models patient trajectories with explicit transition reasoning, and K-RL encodes deterministic pharmacological rules as rule-based DPO preference signals. Across 12 fine-tuned models and 6 zero-shot baselines, our framework substantially improves prescription quality over zero-shot baselines---with a 7B model (Mistral-7B) surpassing zero-shot GPT-5 on all three TCM evaluation metrics.

---


### 81. [The Limits of Simulated Societies: How Post-Training and Survey Fine-Tuning Erase Cross-Cultural Variance](https://arxiv.org/abs/2609.25760)

**<font color=#1a73e8>作者：</font>** Rojin Ziaei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Using large language models (LLMs) to simulate diverse human populations has the potential to transform many aspects of computational social science, yet many evaluations score the average response rather than the spread of opinion within real groups. Here, we develop a diagnostic framework that measures point accuracy alongside dispersion retention, the ratio of predicted to human standard deviation ($\dr$), on 10{,}000 respondent--question pairs from the World Values Survey (WVS) spanning twelve countries and six continents. We evaluate eleven zero-shot language models and five variants fine-tuned on WVS data with SFT, DPO, and GRPO. We identify a failure mode we term \textit{consensus collapse}, where alignment training compresses outputs toward one stereotype per group. Along the post-training trajectory from the Llama~3.1 70B base to the Tulu~3 checkpoints, the first stage, supervised instruction tuning, removes half of the spread with minimal accuracy gain ($\dr$ 1.22 to 0.59; accuracy $+0.9$ points), the later stages do not restore it, and a gap opens between WEIRD and non-WEIRD countries that survey fine-tuning then deepens while pursuing higher point accuracy. The most accurate model (Tulu~3 70B-DPO fine-tuned on WVS, 57.9\%) keeps half the human spread overall ($\dr = 0.50$) and 11\% of it for Nigeria, against 0.70--0.87 for WEIRD countries. Raising the sampling temperature to 1.0 leaves the Wasserstein-1 distance ($\wone$) to human distributions unchanged for both fine-tuned DPO models, and GRPO on Qwen~3.5 9B does not restore the spread under either an accuracy reward or a distribution-shaped reward. Mixing the aligned model with an unaligned prior raises $\dr$ from 0.51 to 0.62 on a held-out split but leaves Nigeria at 0.36. Point accuracy alone therefore misjudges these simulators, and current post-training trades diversity for consensus.

---


### 82. [Reading Right, Answering Wrong: How Visual Configuration Changes Affect Evidence Use in VLMs](https://arxiv.org/abs/2609.25770)

**<font color=#1a73e8>作者：</font>** Dingyang Lin, Yingfeng Luo, Chenglong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong performance on tasks such as visual question answering, yet small image resizes can turn correct answers into errors. We investigate whether changes in visual configuration, such as image tiling and token arrangement, contribute to this instability. Across seven checkpoints and four benchmarks, equally small resizes cause more correctness flips when they switch configurations. Surprisingly, in over half of these cases, models answer the question incorrectly but can still read the correct answer when told what to read. Furthermore, attention interventions in LLaVA-NeXT suggest that configuration changes can weaken the use of readable information during answering. We therefore guide models using field cues and their own transcriptions. With annotation assistance, these forms of guidance together correct 97.2% of errors with readable information. These findings show that configuration changes can affect how models use information they can still read.

---


### 83. [Video-HopChain: Multi-Hop Questions and Confidence-Gated Exploration for Video Reasoning Models](https://arxiv.org/abs/2609.25773)

**<font color=#1a73e8>作者：</font>** Trung Nguyen Quang, Yuhao Dong, Shuo Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> HopChain has shown on still images that multi-hop data synthesis improves vision-language reasoning, because long chain-of-thought reasoning exposes errors that compound across steps, while most data used for reinforcement learning with verifiable rewards (RLVR) rarely demands a chain of visual evidence, so these weaknesses are likely to stay unexposed. We observe the same problem in video, where this framework has not yet been explored. We therefore build Video-HopChain, a dataset of 22,550 multi-hop video questions over 13,378 videos, together with a held-out benchmark of 1,000 questions. Each question chains three to six yes/no questions about moments in one video, and each yields one of two integers depending on its answer. The final answer is the sum of these integers, so an exact match on that sum gives the verifiable reward that RLVR needs. We first train Qwen3-VL-8B with GRPO on a standard video dataset, and a second stage on Video-HopChain then raises the mean over eight video understanding and reasoning benchmarks from 55.4 to 57.9 and improves every one of them. Training on such a dataset, however, exposes a known limitation of GRPO: its learning signal comes from the reward variance within a group, so hard questions whose rollouts are all incorrect and easy questions whose rollouts are all correct both leave the group with no gradient. To recover these groups at the same compute budget, we introduce Confidence-Gated Exploration (CGE). With 8 rollouts per question, CGE samples the first 4 as usual. If these 4 are either all correct or all incorrect, it samples the last 4 with the policy's most confident token masked inside the reasoning span, and removes the masked positions from the loss while all 8 rollouts enter the advantage. With CGE, the mean rises further to 59.3. We release the dataset, the checkpoint, and the data generation and training code.

---


### 84. [Reply to comments arXiv:2512.07881 and arXiv:2601.06104 on quantum structure in human and AI-generated language](https://arxiv.org/abs/2609.25797)

**<font color=#1a73e8>作者：</font>** Massimiliano Sassoli de Bianchi, Roberto Leporini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We reply to the comments by M. Sienicki and K. Sienicki (arXiv:2512.07881) and by K. Sienicki (arXiv:2601.06104) on our work on quantum-mechanical statistics in human language (arXiv:2407.14924) and on quantum structure in AI-generated language (arXiv:2511.21731). We thank the authors for their careful reading and address what we consider to be the main points of criticism: the exploratory nature of the protocol used in the experiments with large language models; the role of marginal-law violations, and of the Contextuality-by-Default criterion, in the identification of entanglement; the limited diagnostic value of a Bose-Einstein fit taken in isolation; the meaning of assigning the lowest energy levels to the most frequent words; and the relation between the vector spaces used by LLMs and quantum state spaces. We also correct a typographical error in Table 3 of arXiv:2511.21731, which does not affect the reported CHSH value.

---


### 85. [Latest Exact Match Attention](https://arxiv.org/abs/2609.25802)

**<font color=#1a73e8>作者：</font>** Moritz Brösamle  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce latest exact match attention (LEMA), an attention variant for transformers where queries and keys are binarized and each query attends only to the latest exactly matching key. We prove that LEMA transformers with chain of thought can simulate word-RAMs, as was recently shown for the less restrictive rightmost hard attention. In contrast to prior hard attention variants, the restriction to exact matches enables an efficient converse direction: word-RAMs can simulate LEMA transformers at a cost per token independent of the context length. Together, these results yield a close correspondence between the two computational models in terms of both compute and memory. Beyond the theory, we propose a training method for LEMA transformers that handles their non-differentiable operations with a straight-through estimator for the binarization and a soft attention surrogate annealed towards LEMA. On a synthetic associative recall task, LEMA models trained this way use their growing state to store and recall a large number of associations, outperforming gated DeltaNet (GDN) with its fixed state size. As a first scaling test, we train LEMA language models with up to 834 million parameters. They match softmax transformers of around half their size in loss and, on repeated rare phrases and a needle-retrieval task, remain behind softmax transformers but recall across longer distances than GDN models of comparable size. Finally, we implement dictionary-based inference for LEMA transformers and show constant generation speed comparable to GDN despite their growing state, with the dictionaries residing in main memory rather than VRAM. Code is available at this https URL.

---


### 86. [The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks](https://arxiv.org/abs/2609.25804)

**<font color=#1a73e8>作者：</font>** Wenbo Pan, Zhichao Liu, Shujie Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly work on long-horizon tasks, and the decisions they make along the way, such as which hypothesis to test or which implementation to build on, determine the outcome of the whole run. Making these decisions well is becoming a key capability for both engineering and research agents. We refer to the ability to make good long-horizon decisions as the taste of an agent. While existing benchmarks measure the end-to-end success of agents on long-horizon tasks, none of them measures the taste of an agent. To address this problem, we build Taste-Bench, a benchmark of taste questions constructed automatically from trajectories that agents produced in engineering and research tasks. Each question presents a decision fork, a point in a trajectory where multiple directions are available and one of them leads to a better outcome, and the evaluated model chooses among these directions without seeing what happens after the fork. We mine these forks automatically from parallel attempts at the same task and from detours inside a single trajectory, without needing human annotation. We evaluate frontier models on Taste-Bench and find that the best model answers only 59.7% of the questions correctly. We further find that forks whose deciding evidence appears later in the trajectory are much harder for every model, and that a larger reasoning budget does not improve the accuracy. Finally, we show that taste can be trained. We distill the judgment of a teacher that has seen the outcome into a student model, and the student makes better decisions on unseen tasks and improves end-to-end success on held-out SWE-bench Pro tasks.

---


### 87. [You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs](https://arxiv.org/abs/2609.25809)

**<font color=#1a73e8>作者：</font>** Yuanteng Chen, Qiwei Lai, Chen Tianqi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-grained mixture-of-experts (MoE) architectures have become a mainstream design for open-weight LLMs, with hundreds of experts and increasingly many selected per token. This shift makes dynamic expert pruning an attractive route to cheaper inference. Yet existing evidence comes largely from coarser architectures and likelihood-scored multiple-choice benchmarks, leaving three central questions open in the fine-grained regime: how redundant per-token expert selection is, how effectively existing pruning methods exploit that redundancy, and what governs a model's sensitivity to pruning. We fill this gap with a systematic empirical study of twelve fine-grained MoE checkpoints spanning nine architecture families, with a core suite of eleven benchmarks covering knowledge QA, mathematics, code generation, and general reasoning. We find that expert selection is far more redundant than the field's operating points assume: uniformly retaining about two thirds of the selected experts preserves 98.8% of unpruned performance on average, requiring only a one-integer change and delivering 1.2-1.7x measured speedup across two serving backends. This simple baseline leaves little room for dynamic allocation at conservative budgets: even the best published rules differ from it by under 1% at matched expert budgets. Their value emerges under aggressive pruning, where the best rules recover up to 3.0% over uniform truncation, with gains concentrated in the generative tasks that suffer the sharpest degradation. Sensitivity to aggressive pruning also depends on the model: larger and thinking models are more resilient, whereas multimodal models are more vulnerable. Together, these findings reveal how much expert computation fine-grained MoEs can dispense with, and establish when dynamic allocation earns its complexity, informing both practical deployment and future pruning methods.

---


### 88. [ARAFA: An LLM-Generated Arabic Fact-Checking Dataset](https://arxiv.org/abs/2609.25833)

**<font color=#1a73e8>作者：</font>** Christophe Khalil, Shady Elbassuoni, Rida Assaf  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic fact-checking poses a significant challenge in Arabic natural language processing due to the scarcity of datasets and resources. In this manuscript, we introduce Arafa, a new large-scale dataset for fact-checking in Modern Standard Arabic, constructed through an automated framework leveraging large language models (LLMs). The dataset was constructed through a three-step pipeline: (1) claim generation from Arabic Wikipedia pages with supporting textual evidence, (2) claim mutation to generate challenging counterfactual claims with refuting evidence, and (3) an automatic validation step to validate that the generated claims are either supported or refuted by their accompanying evidence, or if the evidence does not provide enough information to judge the validity of the claims. The resulting dataset comprises 181,976 claim-evidence pairs labeled as supported, refuted, or not enough information. Human evaluation carried out on a test sample from the dataset demonstrated strong inter-annotator agreement (kappa = 0.89) using Cohen's Kappa for supported claims and (kappa = 0.94) for refuted claims. Automatic validation based on a human-evaluated sample achieved 86% accuracy for supported claims and 88% for refuted ones. To showcase Arafa's value as a resource for automatic Arabic fact-checking, four open-source transformer-based models were fine-tuned using Arafa, with the top-performing model achieving a Macro F1-score of 77% on the test data. In addition to Arafa being the first large-scale dataset for Arabic fact-checking, our framework presents a scalable approach for developing similar resources for other low-resource languages.

---


### 89. [Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes](https://arxiv.org/abs/2609.25841)

**<font color=#1a73e8>作者：</font>** Yuling Xi, Haokai Zhang, Muzhi Zhu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metric reasoning is a critical and challenging task for Vision Language Models (VLMs), playing a pivotal role in embodied AI tasks such as robotic manipulation and autonomous navigation. However, current spatial reasoning remains bottlenecked by rigid pixel-level supervision; such localized optimization often compromises general multimodal intelligence, triggering performance degradation or catastrophic forgetting of broad reasoning capabilities. To address these limitations, we introduce Metric-Bench, a focused benchmark designed to guide metric-spatial reasoning using contextual information. By incorporating in-image reference objects with known physical dimensions, Metric-Bench guides models to implicitly learn the 2D-to-3D mapping without camera intrinsics. We further present MetricReasoner, a task-adapted reinforcement fine-tuning recipe for reference-grounded metric reasoning, using structured prompts and verifiable numerical rewards. Extensive experiments on Metric-Bench demonstrate that our approach significantly enhances spatial metric understanding, outperforming existing and even larger proprietary models by 43.1\%, while improving downstream embodied performance over a spatial-specialized counterpart by 30.4\% on RoboSpatial overall accuracy and 9.3\% on ERQA, and additionally delivering consistent gains on general benchmarks (15.9\% on V$\star$Bench, 88.9\% on BLINK), indicating that the proposed adaptation does not necessarily compromise general VLM capabilities.

---


### 90. [Visual Jev: Accurate and Efficient Decisions from Shared Visual Context](https://arxiv.org/abs/2609.25845)

**<font color=#1a73e8>作者：</font>** Guanxu Yu, Yuhang Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many vision applications ask several independent, forced-choice questions about the same image. Visual Jev encodes the image and public context once, executes isolated question suffixes as a batch, and reads candidate probabilities from the backbone's language-model head. Across four benchmarks, answer-supervised post-training raises equal-weight macro accuracy from 70.6% to 76.1%, with the gain concentrated on the two task families represented in training. At N=32 questions per image, shared batched execution is 8.9x faster in warm amortized time than independent serial execution and remains 3.4x faster than an already-batched baseline that recomputes the prefix, at the cost of higher peak memory. A matched typed-head control offers no consistent accuracy advantage over the language-model-head readout. The supported design is therefore simple: adapt the backbone for quality, retain the existing readout, and share execution for efficiency.

---


### 91. [Optimizing the Score, Losing Sight of the Task: Reward Hacking Across Weights, Selection, and Prompts](https://arxiv.org/abs/2609.25848)

**<font color=#1a73e8>作者：</font>** Vansh Wahi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A higher evaluation score does not always mean a better language model system. When optimization exploits an evaluator's mistakes, measured progress can conceal unchanged or deteriorating task performance. This failure can arise through parameter updates, selection among generated outputs, or revisions to persistent prompts. We develop a comparative framework for reward hacking across these three optimization substrates: weights, selection, and text. Building on the Proxy Compression Hypothesis and research on inference-time and in-context reward hacking, we examine how reachable behavior, optimization budgets, and persistent adaptation shape exposure to proxy error. We formalize a distance-dependent upper bound on evaluator disagreement and a capacity ordering for nested policy classes, then show why distance alone cannot establish a universal ranking of vulnerability. An exact finite-output illustration demonstrates how the location of a scoring defect changes the behavior favored by each method. We also map representative defenses across substrates, identifying which mechanisms transfer directly and which offer only functional analogies. Persistent prompts receive particular attention: their contents are inspectable, but the behavior induced by a small textual change may be difficult to anticipate. The formal analysis, numerical illustration, and published evidence together provide a basis for comparing optimization methods and identifying the conditions under which their defenses transfer. The resulting framework connects optimization choices to verification requirements: reliable improvement depends on controlling accessible failure modes and preserving evidence of task quality independent of the score being optimized.

---


### 92. [BELXTR: Biomedical Entity Linking via Contextualized Token Retrieval](https://arxiv.org/abs/2609.25859)

**<font color=#1a73e8>作者：</font>** Samuele Garda, Ulf Leser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical Entity Linking disambiguates mentions to entities in a knowledge base (KB), making it the cornerstone of information extraction pipelines. While embedding-based models are a popular approach for the task, they suffer from a key limitation. They compress mentions (and entities) into a single vector, forcing the model to average away crucial fine-grained differences. We present BELXTR, a novel embedding model based on the multi-vector (a.k.a. late interaction) architecture, which allows to leverage token-level matching information. BELXTR extends the original XTR model to biomedical entity linking by integrating an existing task-specific training objective and exploring active query expansion. Experiments across ten corpora and five KBs show that BELXTR improves upon current state-of-the-art in half of the corpora with an average improvement of 5pp recall@1. The largest gains are reported on the challenging cross-species gene disambiguation subtask, where BELXTR outperforms an LLM-powered retrieve-and-rerank pipeline and closely approaches a specialized rule-based system. Our results highlight multi-vector models as a practical alternative to hard-to-maintain rule-based systems or in scenarios where LLM-based reranking is too costly as in PubMed-scale mining. The code to reproduce our experiments can be found at: this https URL.

---


### 93. [AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing](https://arxiv.org/abs/2609.25873)

**<font color=#1a73e8>作者：</font>** Yijia Hao, Pratibha Verma, Dongxu Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analog circuit sizing remains a challenging and time-consuming task due to the large design space, strong performance trade-offs, and increasing circuit complexity in scaled technologies. Although recent large language model (LLM)-based methods show promise in improving sample efficiency and interpretability, existing approaches often lack explicit circuit-topology understanding and are mainly evaluated on relatively simple analog building blocks. This paper presents a multi-agent LLM-based framework for complex analog circuit sizing. The proposed framework first analyzes the circuit topology and decomposes the netlist into functional blocks and substructures. It also extracts lightweight design knowledge for reuse. Based on the extracted topology and knowledge, a planner coordinates multiple role-specialized sizing agents to update design variables and achieve global performance specifications. This workflow mimics the collaborative process of an expert analog design team and provides a structured, interpretable, and simulation-driven optimization procedure. The framework was validated on eight circuits, with the largest design containing up to 55 transistors and 60 sizing variables. Notably, for the LDO benchmark, the proposed method achieved a 60\% success rate with an average of 83 iterations, where classical optimizers failed to find feasible solutions. Further, ablation studies demonstrate that topology understanding, design-knowledge infusion, and agent specialization provide complementary benefits. The source code is available to support reproducibility.

---


### 94. [Rethinking Length-Based Training: Batch Composition and Loss Normalization in Speech Token Language Models](https://arxiv.org/abs/2609.25890)

**<font color=#1a73e8>作者：</font>** Hongjin Song, Runwu Shi, Weiqiao Shan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Short-to-long training is a simple curriculum for speech models, but its gains can be difficult to interpret. In speech token language models, length-based training can change the shuffle policy, batch composition, token retention, and token weights under batch-mean loss. We disentangle these factors through matched comparisons. In the tested settings, short-to-long ordering shows no independent benefit when batch composition and token exposure are fixed. First-epoch grouping lowers perplexity for Mimi under batch-mean loss, but this gain is not observed under token-balanced loss. The cross-tokenizer results are consistent with a link between chunk-length variation and token weighting. This work provides a systematic analysis protocol for studying length-based training in variable-length speech models.

---


### 95. [BAS-OPD: Budget-Aware Selective On-Policy Self-Distillation for Fine-Grained Multimodal Perception](https://arxiv.org/abs/2609.25891)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Hengguang Zhou, Yuan Kang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) often struggle with fine-grained visual perception when processing complete images, as critical evidence may only appear in local regions. On-policy self-distillation (OPD) enables transferring privileged visual knowledge from informative views to full-image policies, but querying the teacher for every rollout introduces substantial supervision costs. In this work, we propose BAS-OPD, a budget-aware selective OPD framework that allocates teacher supervision under limited query budgets. Instead of querying all rollouts, BAS-OPD selects informative samples while maintaining full-batch student generation. We explore random, uncertainty-based, and learned utility-based selection strategies, where the learned selector estimates query value from detached rollout statistics and online utility signals derived from student--teacher agreement and teacher confidence without additional student forward passes. BAS-OPD only changes training-time supervision allocation and preserves single-pass full-image inference. Experiments on fine-grained multimodal perception benchmarks demonstrate that BAS-OPD achieves strong performance while substantially reducing teacher supervision costs, highlighting the effectiveness of selective OPD under constrained budgets.

---


### 96. [When Does Execution Provenance Help Agent Memory Retrieval?](https://arxiv.org/abs/2609.25913)

**<font color=#1a73e8>作者：</font>** Yiqi Wang, Jinqian Ju, Jiaqi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A language agent's execution history can exceed its context window, requiring its memory system to retrieve complete supporting evidence under a hard token budget. Evidence may span multiple execution events, yet conventional retrievers use fixed token windows and fixed-k metrics that reward individual fragments without showing whether the complete evidence set fits in context. Smaller windows reduce irrelevant text but scatter evidence across candidates, while flat-versus-graph comparisons can conflate candidate design with graph propagation. To address these limitations, we formulate agent-memory retrieval as budgeted evidence completion and score exact gold spans in shared source coordinates. We first construct source-aligned provenance units from tool arguments and outputs. We then apply a zero-initialized residual R-GCN to refine frozen dense-retrieval scores over typed provenance edges. We evaluate 2,000 span-grounded memory queries over 1,207 held-out execution-grounded ISETrace trajectories. With matched Dense-FT scoring, provenance units improve Full Support@2048 by 19.07 points over flat 512-token windows and remain 11.96 points above a per-metric oracle over four flat chunk sizes; the pattern also holds with cross-encoder scoring. Holding the candidates and seed scores fixed, graph propagation adds 4.55 points in Full Support@2048 (95% CI [2.98, 6.18]). This gain is concentrated when gold evidence spans multiple events; entity co-occurrence expansion produces no comparable benefit, and relation and topology controls confirm dependence on typed transformations and observed graph structure. Overall, source-aligned candidates address the dominant granularity trade-off, while graph-conditioned propagation adds a smaller, targeted benefit for distributed evidence.

---


### 97. [Beyond Scalar Sensitivity: Activation-Aware Mixed-Precision LLM Quantization with Cross-Layer Refinement](https://arxiv.org/abs/2609.25916)

**<font color=#1a73e8>作者：</font>** Akihiro Yoshida, Yuma Ichikawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-precision weight quantization is commonly formulated as a Multiple-Choice Knapsack Problem (MCKP), yet existing solvers rely on scalar sensitivity proxies that collapse each weight matrix's Hessian into a single number and treat every module independently. We prove that even the optimal scalar proxy incurs multiplicative distortion up to $\sqrt{\kappa(\mathbf{A})\kappa(\mathbf{B})}$ relative to the full activation-aware quadratic, where $\kappa(\mathbf{A})$ and $\kappa(\mathbf{B})$ denote the condition numbers of the input- and output-side Hessian factors. This bound varies from $10^1$ to $10^{13}$ for typical LLM modules, making inter-module sensitivity ranking unreliable. To address these limitations, we propose Cross-layer Activation-aware Sensitivity Allocation (CASA), a two-phase method. In Stage 1, the scalar proxy is replaced by an activation-aware metric derived from the Kronecker-factored Hessian, reducing the MCKP to a form whose continuous relaxation admits a closed-form solution. In Stage 2, a cross-layer-aware local search evaluates bit-width updates using the end-to-end model loss. Experiments on multiple LLMs across different bit budgets show that CASA achieves lower perplexity than the latest scalar-proxy baselines, especially at ultra-low bit-widths ($<3$ bits per weight). Moreover, the performance gain in zero-shot accuracy tracks the per-model average condition-number over modules, confirming the distortion bound as a practical indicator of scalar-proxy failure.

---


### 98. [Informed Masking: Structure-Aware Perturbation for Reinforcement Learning in Diffusion Large Language Models](https://arxiv.org/abs/2609.25927)

**<font color=#1a73e8>作者：</font>** Xiaoyi Yu, Enver Sangineto, Pei Fu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) have emerged as an efficient alternative to autoregressive models, yet aligning them via Reinforcement Learning (RL) requires likelihood surrogates estimated from masked reconstruction subproblems under a small Monte Carlo budget per rollout. Existing methods construct these subproblems by uniform random masking, leaving open the question of which subproblems to prioritize. We identify a systematic upstream/downstream structure in dLLM rollouts. Some tokens, when revealed, trigger large confidence changes in nearby undecoded positions; we call them upstream. Others induce only small local changes and are therefore downstream. We find masking downstream tokens yields substantially better-posed subproblems than masking upstream tokens, a phenomenon we term subproblem difficulty asymmetry. Based on the observation, we propose Informed Masking (IM), which derives a per-token priority score from the denoising trajectory at zero extra inference cost and biases mask sampling toward downstream tokens. IM is plug-and-play: when plugged into three state-of-the-art dLLM RL methods on LLaDA-8B-Instruct, it delivers up to 2.01%, 8.68%, and 5.77% relative average gains on math and planning benchmarks with improved training stability.

---


### 99. [ClusterFewshot: Improving Few-shot Optimization for LLMs workflow](https://arxiv.org/abs/2609.25939)

**<font color=#1a73e8>作者：</font>** Omri Bar Haim, Shahar Katz, Lior Wolf  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance of large language model (LLM) workflows often depends on selecting a small set of in-context demonstrations to guide model behavior on new tasks. Recent methods improve this process by augmenting prompts with successful reasoning paths. However, their demonstration selection relies on random sampling or metric-based rankings, overlooking the semantic structure of the task. We propose ClusterFewshot, a strategy that combines semantic structuring with utility-aware scoring to construct representative and effective few-shot demonstration sets. Evaluated within DSPy-based pipelines, ClusterFewshot substantially reduces optimization cost across multiple benchmarks, while consistently improving accuracy relative to prior bootstrap-based methods in both standalone prompt tuning and hybrid prompt-weight optimization.

---


### 100. [Towards Systematic Qualification of Vision-Language Models for Automotive Perception Systems](https://arxiv.org/abs/2609.25945)

**<font color=#1a73e8>作者：</font>** Malsha Ashani Mahawatta Dona, Konstantinos Rokanas, Alexander Säfström 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The field of Artificial Intelligence has been adopted for many application domains. Vision Language Models are one of the recently advanced AI techniques that have been explored to support automotive features such as vehicle perception, and safety assurance. However, such language models are prone to hallucinations, posing a potential threat to the safety of automotive systems that may incorporate them. Within the automotive domain, VLMs could not only hallucinate traffic objects, but could also fail to identify traffic objects that are actually present, which may potentially lead to dangerous situations. Though we have observed a growing body of literature that proposes verification and validation techniques for safe and trustworthy AI, these methods are often studied in isolation, focusing either on run-time or design-time phases. Such isolated techniques could be insufficient in safety-critical, realistic contexts such as automotive perception systems. In this paper, we analyze design-time and run-time verification and validation techniques based on a taxonomy presented by Huang et al. We present an automotive study in which a design-time qualification workflow is proposed to complement run-time monitoring. This workflow combines a fixed safety-relevant ontology-based structured annotation system together with a synonym-based evaluation process to statistically evaluate three state-of-the-art VLMs against data from the nuScenes dataset. We observed that the proposed technique enables deterministic and repeatable quantification of the hallucinations VLMs generate in automotive perception-related tasks. The proposed workflow supports model comparison and deployment-oriented engineering decisions within the design-time verification and validation process and will contribute to a holistic verification strategy that strives towards trustworthy automotive perception systems

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-206](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

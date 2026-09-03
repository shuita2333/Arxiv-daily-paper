# 🧠 大模型相关研究 | 2026年09月04日

> 本类共 **177** 篇论文：已确认 **170** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-177](./part-04.md)

---

### 51. [Implicit Manipulation for Skill Selection in LLM Agents with Semantic Matching](https://arxiv.org/abs/2609.02035)

**<font color=#1a73e8>作者：</font>** Qikai Wang, Yongzhao Zhang, Zhiwei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Skill selection is a key stage in LLM-agent workflows, determining which installed skill should handle a user request. Existing attacks on this stage primarily rely on explicit prompt injection or instruction-level steering, which can expose recognizable manipulation signals. In this work, we identify a new implicit attack surface for skill selection: even when the user prompt and skill description appear benign in isolation, their semantic relationship can still be strategically shaped to favor an attacker-chosen skill. Based on this observation, we present Implicit Skill-Selection Manipulation via Semantic Matching (ISM), which jointly shapes target-skill metadata and reusable prompts to manipulate skill selection without explicit selection instructions. Specifically, we develop a three-stage strategy to broaden semantic coverage, strengthen target distinctiveness, and preserve natural prompt wording. Across four task domains and eight selector models, ISM increases the average target-selection rate (TSR) from 15.2% to 63.5%. In a matched comparison, ISM achieves a 73.5% TSR, only 9.8 percentage points below Explicit Steering. Human reviewers block ISM in only 2.9% of judgments, versus 91.4% for Explicit Steering, while five LLM-based inspectors pass ISM at an average rate of 82.9%, versus 37.4% for Explicit Steering. Moreover, ISM remains effective against PPL-W, Llama Prompt Guard 2, and PIGuard.

---


### 52. [Test-Time Logit Prompting for Source-Free Missing Modality Adaptation](https://arxiv.org/abs/2609.02039)

**<font color=#1a73e8>作者：</font>** Taixi Chen, Nancy Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved remarkable performance by leveraging complementary information from large-scale image-text pairs. However, missing-modality inputs are commonly encountered during real-world deployment, often leading to significant performance degradation. Existing methods primarily enhance model robustness by learning modality compensation strategies from source training data. However, their reliance on source training data makes them difficult to apply when original data are unavailable due to privacy, storage, or accessibility constraints, such as clinical applications and personalized AI services. This raises an important yet underexplored question: can VLMs be efficiently adapted at test time for visual recognition with missing modalities without accessing source training data? To this end, we propose Test-Time Logit Prompting (TLP), a lightweight source-free test-time adaptation framework for visual recognition with missing modalities. To address missing-induced prediction shifts, TLP optimizes logit prompts with uncertainty-aware adjustment and modality-complete consistency regularization, adaptively adjusting prediction confidence while preserving semantic consistency. Extensive experiments across diverse vision-language benchmarks demonstrate that TLP consistently enhances recognition performance under missing-modality scenarios, achieving up to 8\% improvements while requiring only hundreds of tunable parameters and a few test-time optimization steps.

---


### 53. [Act More, Decide Less: Skill-Guided Adaptive Action Chunking for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.02042)

**<font color=#1a73e8>作者：</font>** Yanting Yang, Can Jin, Jinman Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents for long-horizon interactive tasks typically follow a ReAct-style protocol, issuing one primitive action per LLM round. While this enables frequent replanning, it is inefficient for long-horizon tasks where many rounds are spent on routine action sequences. A natural alternative is to let the agent emit variable-length action chunks. However, naively training such policies with standard reinforcement learning fails: the agent either collapses to single-action behavior or over-commits to excessively long sequences. Both failures share a common root cause: the inability to learn chunk boundaries. We propose SPACE, which addresses this challenge by distilling chunk-boundary supervision from trajectory-induced programmatic skills. We induce two-level programmatic skills from successful trajectories, where subskill boundaries serve as direct chunk-boundary supervision. This temporal structure is then distilled into a primitive-chunk policy via hybrid on-/off-policy optimization with chunk-aware credit assignment. Experiments on ALFWorld and ScienceWorld show that SPACE improves success rates by 7.0%-31.3% over the strongest baseline in each setting while reducing average LLM decision rounds by up to 78.9%.

---


### 54. [The Dynamics of Continuous Mixture Collapse in Language Models](https://arxiv.org/abs/2609.02049)

**<font color=#1a73e8>作者：</font>** Ali Backour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs latent-state reasoning methods replace discrete intermediate tokens with continuous states, such as weighted mixtures of token embeddings, to retain multiple possible reasoning directions rather than committing to one. Yet pretrained language models often fail to preserve these mixtures. We study why through a combination of theoretical analysis and controlled empirical investigations on a variety of models. We identify three independent, distinct sources of failure. First, transformer architectures already distort mixture geometry, and training substantially amplifies this effect. Moreover, the failure can occur even if the model transports mixtures perfectly linearly: the softmax readout and autoregressive feedback form a dynamical system that either amplifies small differences until one component of the mixture dominates or contracts different mixtures until they become indistinguishable. We verify this theoretical prediction empirically: the observed transition between contraction and amplification occurs near the theoretical threshold derived by our analysis, and pretrained-model rollouts lie predominantly on the amplifying side. Finally, we generalize to mixtures of many components and show that exact preservation generally requires context-dependent correction, whose required dimensionality can grow with the number of components.

---


### 55. [A Tri-Agent Framework for Evaluating and Aligning Question Clarification Capabilities of Large Language Models](https://arxiv.org/abs/2609.02054)

**<font color=#1a73e8>作者：</font>** Yikai Zhao, Saurabh Pandey, Pradeep Kumar Misra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in interactive systems where understanding user intent precisely is paramount. A key capability for such systems is effective question clarification, especially when user queries are ambiguous or underspecified. This paper introduces a novel tri-agent framework for the robust evaluation of an LLM's ability to engage in clarifying dialogue. Our framework comprises three distinct LLM-based agents: (1) a Question Clarifying Agent (QCA), the system under evaluation, tasked with identifying ambiguities and posing clarifying questions; (2) a Respondent Agent (RA), designed to simulate human user responses, potentially including irrelevant or challenging replies; and (3) an Evaluator Agent (EA), an LLM-as-a-judge, which assesses the quality of the dialogue based on a comprehensive set of metrics. We detail a methodology for synthetic data generation in the supply chain domain as an example. We propose metrics evaluating ambiguity handling, question quality, dialogue efficiency, language appropriateness, and final intent alignment. We also briefly discuss the validation of the EA against human judgments. This work provides a structured approach to benchmark, validate, and improve the clarification capabilities of conversational LLM applications.

---


### 56. [HyGRAIL: Cost-Aware and Evidence-Grounded Scientific Hypothesis Discovery over Knowledge Graphs](https://arxiv.org/abs/2609.02056)

**<font color=#1a73e8>作者：</font>** Yihang Sun, Zhihan Zhu, Zhiyuan Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific knowledge graphs organize entities and relations extracted from scientific literature, but they remain inherently incomplete. Missing typed links in such graphs can therefore represent plausible scientific hypotheses, such as unexplored associations between materials and applications. However, scientific hypothesis discovery is challenging because true discoveries are extremely sparse among typed candidate pairs: graph neural networks (GNNs) are efficient but unreliable for ambiguous cases, while large language models (LLMs) are knowledgeable but too costly to apply exhaustively and are not naturally grounded in graph structures. We propose HyGRAIL, a cost-aware and evidence-grounded framework that combines heterogeneous GNN triage with LLM-based hypothesis review. HyGRAIL first uses a GNN to score candidate hypotheses and identify a validation-calibrated ambiguous region, routing only graph-uncertain cases to LLM review. For each routed hypothesis, HyGRAIL retrieves node-level associations and multi-hop relational paths from the knowledge graph (KG), then converts this structured evidence into natural language through template-based or LLM-based naturalization. An LLM review agent finally judges each hard hypothesis using the naturalized evidence and validation-selected decision criteria. On MatKG, HyGRAIL achieves the best F1 score of 0.429, improving over the strongest prior baseline by 0.242 F1 points and over the GNN-only baseline by 0.322. Meanwhile, GNN triage reduces the LLM call rate by 54.36% on average. Ablation studies further show that retrieved graph evidence is crucial for reliable hypothesis verification and that compact, two-sided evidence is more effective than simply increasing retrieval quantity.

---


### 57. [DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents](https://arxiv.org/abs/2609.02059)

**<font color=#1a73e8>作者：</font>** Zhuoran Yu, Le Thien Phuc Nguyen, Jaden Park 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved strong performance on structured visual understanding tasks such as chart and document question answering. However, existing benchmarks typically evaluate these domains in isolation, leaving underexplored a key capability: whether models can use textual context to determine how chart evidence should be selected, interpreted, and aggregated. We introduce DocHop, a benchmark for integrated chart--context reasoning in document-style images. In DocHop, the document narrative specifies multi-step compositional constraints, while charts provide the corresponding data values. Questions are grounded on a semantic reference label defined in the narrative, requiring models to resolve target entities from context before aggregating evidence across multiple charts. To enable systematic evaluation, we construct DocHop via a stochastic logic-first generation pipeline with controllable reasoning depth and visual density, covering 2,074 examples across six task categories. Experiments on a wide range of proprietary and open-source MLLMs show a substantial gap to human performance: annotators achieve over 90% accuracy, while the best model reaches only 62.83%. Reasoning-enhanced models consistently show improved results, but performance degrades as reasoning complexity increases. Overall, DocHop provides a controlled testbed for challenging multi-hop document reasoning.

---


### 58. [ToolGate: An Executable Acceptance Pipeline for Tool-Dependent Scientific Benchmark Construction](https://arxiv.org/abs/2609.02067)

**<font color=#1a73e8>作者：</font>** Ke Zhang, Yankang Liu, Roya Zandi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific benchmarks are commonly built by domain experts who write tasks and cross-check one another's work, or who adapt existing material from textbooks, published papers, and online resources. These routes can produce strong evaluations, but they require substantial per-item labor. Language models can reduce this repeated work by proposing candidates quickly. The remaining problem is acceptance. We target scientific questions whose answers require computations with specialist software rather than unaided reasoning alone. A candidate is invalid if its script fails or returns a different answer, or trivial if a model answers it without the software. We present ToolGate, which treats every generated item as a proposal and keeps it only if three gates pass. First, an executable solution script must reproduce the proposed answer when run with the scientific software. Second, randomized no-tool screening rejects candidates that models can already solve from the prompt alone. Third, a tool-using agent must solve each survivor within a fixed time limit. We instantiate ToolGate in FEniCSx with 500 generation attempts. The local-verification gate retains 478 candidates. For final reporting, we rescreen this pool after generation: two randomized no-tool screens exclude 222 from the reported pool, and direct GPT-5.5 API calls at medium reasoning (the API default) exclude another 121. Of the remaining 135, a GPT-5.5 Codex CLI agent with access to FEniCSx solves 130; exact deduplication leaves 128 unique protocol survivors. ToolGate turns repeated answer checking and difficulty screening into an auditable process while leaving domain design and final review to experts.

---


### 59. [XMerge: Cross-Axis Selection and Reconstructive Layer Merging for LLM Depth Compression](https://arxiv.org/abs/2609.02083)

**<font color=#1a73e8>作者：</font>** Jundong Hu, Shekar Ramachandran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Removing complete transformer layers preserves a standard serving architecture, but existing depth-compression methods can lose substantial quality, and the loss varies unpredictably across models. We introduce XMerge, a post-training method with two components. Cross-axis selection identifies a block with low relative-magnitude and angular hidden-state change, and local boundary reconstruction re-fits the adjacent surviving block to match the original two-block output. XMerge uses no task labels or end-to-end fine-tuning, and it introduces neither architectural changes nor additional inference-time parameters. Across seven Llama and Qwen backbones (0.5B-8B), five published baselines, and three layer-reduction levels, its advantage over baselines is largest at the most aggressive removal: at k=4 it ranks first on six of seven backbones on CORE (a 22-task aggregate) and, separately, on six of seven on MMLU (five of seven on both at once), while avoiding the large perplexity increases of several competing operators. In a task-level bootstrap, the 95% confidence intervals for the three largest CORE margins exclude zero; the remaining margins are consistent with ties. Across the 14 (model, regime) cells it is also the only evaluated operator that never collapses, ranking top-2 in both zero-shot and in-context regimes; on a first calibration probe (one backbone) it is the best-calibrated operator. Ablations show that local reconstruction provides most of the gain, while cross-axis fusion helps when the two selection axes disagree. The additional construction cost is recovered through per-token decode savings after roughly tens of thousands of requests.

---


### 60. [Rendering-in-the-Loop: An Execution-Driven Agent for Interactive Web Development](https://arxiv.org/abs/2609.02088)

**<font color=#1a73e8>作者：</font>** Yilong Guo, Hanqi Chen, Zixiao Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have achieved remarkable progress in front-end web development, generating interactive webpages from multimodal references such as screenshots and interaction videos. However, existing work largely emphasizes visual metrics such as aesthetics and layout similarity, while overlooking the more critical validation of interactive functionality. We present RILA, an execution-driven agent that puts browser rendering in the loop, iteratively editing generated code from runtime interaction feedback. RILA introduces an Action Interaction Verification (AIV) module that replays the reference interaction trajectory on the generated webpage to collect grounded execution-aware observations, and an Execution-aware Rendering Score (ERS) that jointly measures interaction correctness and visual fidelity to guide iterative optimization. We further build an execution-verified data synthesis pipeline that produces diverse, high-quality training data, offering gains complementary to inference-time optimization. On IWR-Bench, RILA consistently improves both interaction and visual fidelity across foundation models. Notably, with our training pipeline, RILA lifts the compact Qwen3.5-9B backbone from 40.40% to 57.52%, surpassing far larger one-shot generators, including the 1T-parameter Kimi-K2.6 (55.61%) and the proprietary GPT-5.5 (55.74%).

---


### 61. [IDEEA: training-free Input-Dependent stEEring via Activation cluster matching](https://arxiv.org/abs/2609.02089)

**<font color=#1a73e8>作者：</font>** Zheng Wang, Muchen Li, Renjie Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Steering aligns large language models (LLMs) by injecting a bias into selected activations at inference time, offering a far cheaper alternative to weight-update methods such as supervised fine-tuning or reinforcement learning. However, most existing training-free steering methods are input-independent: a single direction is fitted once and shared across all inputs. This is fundamentally limiting as different inputs occupy different regions of the activation space and admit different optimal steering directions toward the same target concept, much as the gradient with respect to a fixed loss varies from input to input. We close this gap with IDEEA (Input-Dependent stEEring via Activation cluster matching), a training-free framework for input-dependent steering. IDEEA clusters the positive and negative activation supports per attention head, and solves an optimal-matching problem to construct a set of cluster-conditional directions, all about the target concept. At inference time, it picks from this pool of directions and uses the one that best matches the input's own activation for steering. IDEEA aligns the model toward the target concept while preserving the input's original representation, evidence that activations encoding a concept occupy several distinct sub-regions of the representation space rather than a single one. IDEEA improves the truth $\times$ info rate in TruthfulQA by an average of 9.9% (up to 23.5%) over the best input-independent baseline.

---


### 62. [Selective Knowledge Edit Reversal via Gated Singular Vector Shrinkage](https://arxiv.org/abs/2609.02091)

**<font color=#1a73e8>作者：</font>** Weifeng Jiang, Ruirui Chen, Qianren Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge editing provides an efficient way to update factual knowledge in large language models. However, malicious edits may introduce safety risks, making it necessary to reverse undesirable editing effects. Existing reversal methods for parameter-modifying edits mainly focus on global removal, which may also erase beneficial edits that should be preserved. In this paper, we study selective reversal of edited knowledge, where the goal is to reverse targeted edited facts while preserving the remaining edited facts. Based on the hypothesis that each edit is sparsely encoded within the dominant subspace of the edited matrix, we propose a spectral-based reversal framework that locates edit-sensitive components within the dominant singular subspace of edited weights. Experiments across multiple settings demonstrate the effectiveness of our method in reversing selected edits while preserving unrelated edited facts. These results suggest that different edits are sparsely encoded within dominant singular components and can be separable when the number of edits is moderate, making selective spectral reversal a promising direction for locating edit-specific components and repairing edited language models.

---


### 63. [Beyond Outcome Gaps: Process-Aware Fairness Diagnosis for LLM-based Multi-Agent Decision Systems](https://arxiv.org/abs/2609.02092)

**<font color=#1a73e8>作者：</font>** Yiran Zhao, Lu Zhou, Liming Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) are increasingly considered for high-stakes decision-making, yet outcome-based fairness audits can miss where risks arise within the decision trajectory. We present SCOPED-Hiring, a process-aware fairness diagnosis pipeline for LLM-based hiring MAS. SCOPED-Hiring constructs controlled resume variants, runs role-based hiring committees, logs over 311K structured decision trajectories, and converts trajectory fields into quantitative fairness signals organized by six diagnostic lenses: final outcome, counterfactual, process, pathway, dynamic, and design effects. SCOPED-Hiring reveals that balanced final hire rates can mask hidden trajectory unfairness in multi-agent decision trajectories: career gaps trigger suspicion, proxy cues shape qualification judgments, and identity cues lead to unequal investigation. Targeted repair guided by these diagnoses reduces total layered burden by 72.3% while shifting the hire rate by only 1.86 pp, showing that process diagnosis can guide effective repair. Project Page: this https URL

---


### 64. [Compositional Spectral Prompts for LLM-based Online Time Series Forecasting](https://arxiv.org/abs/2609.02093)

**<font color=#1a73e8>作者：</font>** Seungyoon Choi, Hyunchul Kim, Jae-Gil Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To address the sequential and evolving nature of time series, the Online Time Series Forecasting (OTSF) task has been extensively studied in multiple domains. Existing research focuses on adapting to non-stationary environments by employing memory buffer-based retrieval strategies. However, we observe that such frameworks struggle with long-term adaptation and fail to generalize to unseen patterns. To this end, we introduce CoSPOT, an LLM-based online time series forecasting framework that leverages a pre-trained LLM as the backbone online forecaster, motivated by its strong few-shot capabilities. For efficient online adaptation, CoSPOT keeps the LLM frozen and employs compositional spectral prompts grounded in frequency-domain bases to guide the model with the overall distribution of the input, thereby substantially reducing the number of parameters updated during the online phase. Specifically, CoSPOT decomposes time series into frequency bases and composes the corresponding spectral basis prompts according to their amplitudes, allowing unseen patterns to be represented as new combinations of learned basis prompts. Our extensive experiments on real-world datasets demonstrate the superiority and practicality of CoSPOT across challenging online scenarios, including extended online phases and cross-dataset settings with substantial distribution shifts. Our code is available at this https URL.

---


### 65. [MASkills: Continual Skills Optimization for Multi-Agent LLM Systems](https://arxiv.org/abs/2609.02094)

**<font color=#1a73e8>作者：</font>** Huaiyuan Yao, Xiaoou Liu, Charles Fleming 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems have shown strong performance on complex tasks, yet continual improvement from interaction experience remains challenging. Existing self-reflection methods build experience memories, but memories are mostly hard to invoke, refine, or scale, while agent skills offer a more actionable unit: structured procedural knowledge that specifies when to act, how to act, and which resources or tools to use. We introduce MASkills, a continual learning framework that optimizes multi-agent LLM systems through agent skills. MASkills presents a new agent-optimization pipeline that integrates skill-conditioned credit assignment, hierarchical credit aggregation, and momentum-smoothed optimization, enabling agent skill libraries to evolve through refinement, induction, consolidation, and pruning. Experiments on HotpotQA, LoCoMo, and GAIA demonstrate the effectiveness of MASkills across multiple agentic tasks. Our code is available at this https URL

---


### 66. [Evidence-Guided Detection, Localization and Explanation for Text-Centric Image Forensics](https://arxiv.org/abs/2609.02097)

**<font color=#1a73e8>作者：</font>** Peifeng Liu, Bin Li, Qingsong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid progress of AIGC has made text-centric image manipulation increasingly accessible, creating new forensic challenges that require not only authenticity detection but also spatial grounding and evidence-based explanation. This paper presents our solution to the GenText-Forensics Challenge at ACM Multimedia 2026. We propose an evidence-guided detector-localizer-reasoner system, where an image-level detector provides a global authenticity prior, a dedicated localizer extracts tampered regions as spatial grounding evidence, and an MLLM-based reasoner generates structured forensic reports grounded in this expert forensic evidence. These modules are connected through a cascaded evidence flow: the detector gates the subsequent localization and prompting process, the localizer converts tamper responses into grounding boxes, and the reasoner is trained to synthesize the detector decision and localized evidence into the final report. As a key part of our method, we introduce iterative difficulty-aware mining to improve localization quality and apply report-mask consistency post-processing to align report grounding with predicted masks. On the official hidden test set, our system achieves a final score of 0.638 and ranks second in the challenge, validating the effectiveness of the proposed evidence-guided system. The code is available at this https URL.

---


### 67. [Federated LoRA Adaptation of BiomedCLIP Across Four International Chest X-Ray Cohorts](https://arxiv.org/abs/2609.02101)

**<font color=#1a73e8>作者：</font>** Sanjaya Poudel, Nirajan Kunwor, Manish Dhakal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) lets institutions train a shared model without exchanging data, and Low-Rank Adaptation (LoRA) makes this practical at scale by communicating only compact low-rank updates. Biomedical imaging is a compelling setting for this combination: patient data are archived behind privacy regulations, and institutions differ widely in scanners, protocols, and compute. Such heterogeneity raises the question of how federated LoRA updates should be aggregated, increasingly pressing as multimodal vision-language models become central to medical image analysis. We benchmark federated Parameter-efficient fine-tuning (PEFT) of BiomedCLIP for chest radiograph classification across four public cohorts on three continents (USA, Vietnam, Spain). Federated LoRA adaptation improves shared-class AUC on all four cohorts over the unadapted BiomedCLIP backbone (mean 0.687 to 0.802), showing that the gains come from federated adaptation rather than from the pretrained model's zero-shot ability. Relative to isolated single-cohort training, federation improves the weaker cohorts while largely preserving the strongest and approaches a centralized reference (0.812) that pools all data. The singular value decomposition (SVD)-based product-space aggregation introduced by FlexLoRA is essential to this gain (naive factor averaging drops mean AUC by 0.097), whereas a drift-correcting optimizer (FedProx) shows no benefit over FedAvg in our single-seed runs, consistent with LoRA's low-rank updates already limiting client drift. Biomedical vision-language models can thus be adapted collaboratively across heterogeneous, geographically distributed institutions without centralizing data.

---


### 68. [Predict, Don't Iterate: Efficient Adaptive-Length Infilling for Diffusion Language Models](https://arxiv.org/abs/2609.02108)

**<font color=#1a73e8>作者：</font>** Haobo Xu, Sirui Chen, Yuanchen Bei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) have emerged as a promising alternative to the auto-regressive paradigm. With bidirectional attention and any-order generation, DLMs naturally fit infilling tasks, which require generating a middle span conditioned on both the prefix and the suffix. However, infilling is sensitive to the length of the span, while DLMs require the length to be fixed before generation. Although prior studies extend DLMs to dynamic lengths, they still suffer from two limitations. (i) Sensitivity to initial length. These methods require a preset length to initialize the search and are highly sensitive to this initial length, often yielding suboptimal results. (ii) Inference inefficiency. They either insert length-changing operations during generation or repeatedly search for an appropriate length using multi-step denoising confidence, both of which introduce substantial extra forward passes and computational cost. Therefore, we propose PILL (Probing-based InfiLling with preset-Length-free decoding), an efficient infilling method for DLMs that requires no preset initial length and adds far fewer extra forward passes than baselines, substantially reducing inference time. Experiments show that, across five DLMs spanning different families, architectures, and training recipes on eight infilling benchmarks, PILL improves over the strongest baseline by +4.8 average pass rate on code and +6.0 BLEU-2 on text, while running 1.82x faster than that baseline. The code is available at this https URL.

---


### 69. [text2ql: Multi-Target Natural Language Querying via a Language-Agnostic Intermediate Representation](https://arxiv.org/abs/2609.02115)

**<font color=#1a73e8>作者：</font>** Ritesh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language interfaces to databases have traditionally suffered from three structural limitations: exclusive targeting of relational SQL, unconditional dependence on large language model (LLM) inference at query time, and absence of any runtime signal when generated queries are semantically incorrect. This paper presents text2ql, an open-source Python framework that addresses all three limitations through a language-agnostic Intermediate Representation (QueryIR) and a pluggable renderer architecture. A single seven-stage detection pipeline serves both SQL and GraphQL targets; a zero-LLM deterministic mode delivers 100% execution accuracy at a median latency of 3.2 ms with no API cost; and every generated query carries a runtime confidence score in [0.15, 0.97] computed from an additive signal model. Evaluated on 50-query random samples from the Spider and BIRD benchmarks (indicative results; full-set evaluation is planned), the LLM-backed mode achieves 62-70% exact match and 84-91% execution accuracy; the deterministic mode achieves 100% execution accuracy with zero parse errors across all 100 test cases. An ablation study isolates schema-aware prompting as the dominant accuracy lever, contributing +18.4 percentage points of exact-match gain over the schema-free baseline on both benchmarks. text2ql is publicly available at this https URL under the Apache 2.0 license.

---


### 70. [Semantic Signal-Assisted Inspection and Recovery Allocation in Reverse Logistics](https://arxiv.org/abs/2609.02116)

**<font color=#1a73e8>作者：</font>** Jiani He, Dingyan Shang, Yihua Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reverse-logistics operators often decide how to inspect and route returned assets before their condition is fully observed, while full inspection consumes scarce labor. Semantic Signal-Assisted Decision Support converts return notes into a condition factor and a signal-quality score that guide inspection depth and recovery allocation under shared labor capacity. We evaluate the framework in three synthetic benchmark scenarios spanning information technology decommissioning, aircraft maintenance, and consumer-electronics returns. Across 30 paired simulation seeds, the keyword implementation improves net recovery value relative to a structured-feature comparator with noisy full inspection while reducing inspection cost in all three scenarios. A risk-blind comparator that skips inspection altogether still records higher value under the benchmark's purely economic objective. At matched inspection cost, score-guided targeting adds 53.9 thousand United States dollars per batch in the aircraft scenario but has little economic effect in the other two configurations; phrase and large language model extractors provide further gains in the aircraft scenario. These results show how narrative evidence can support inspection allocation before recovery decisions are made.

---


### 71. [AI agents reshape consensus formation in human groups](https://arxiv.org/abs/2609.02122)

**<font color=#1a73e8>作者：</font>** Lin Chen, Ziyi Liu, Xia Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents shift from tools to participants in human groups, a fundamental question for collective behavior is how their growing presence reshapes consensus formation. Here we study mixed human-AI groups in a collaborative description game, in which shared conventions emerge through repeated rounds of random pairwise communication. Varying the proportions of LLM agents, we identify three distinct regimes of consensus formation: low agent proportions facilitate human-led consensus, intermediate proportions disrupt convergence, and high proportions restore strong consensus while shifting it toward agent-led conventions. Crucially, these regimes differ not only in the strength of convergence, but also in the semantic grounding and communicative form of the resulting consensus: human-led consensus is more concrete, holistic, and grounded in shared real-world analogies, whereas agent-led consensus is more abstract, less information-dense, and more geometrically segmented. Mechanistically, agent influence arises from a shared linguistic prior that places agents near one another in the expression space, combined with relatively stable expression choices across rounds; humans initially resist adopting expressions from partners perceived as AI but gradually yield to conformity pressure. These findings provide evidence that AI composition can shape the emergence, content, and perceived legitimacy of group norms, making agent proportion and transparency important design variables for human-AI systems.

---


### 72. [C$^{3}$T: Counterfactual Causal Reasoning for Sentiment Shifts in Social-Media Conversation Trees](https://arxiv.org/abs/2609.02131)

**<font color=#1a73e8>作者：</font>** S M Rafiuddin, Atriya Sen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment in social-media threads does not only vary across posts; it shifts as users react to claims, corrections, evidence, and hostility within a branching reply tree. We study why sentiment changes in rumor-centric conversation trees by treating discourse moves (e.g., denial/correction, evidence/link, toxicity/attack) as candidate interventions and asking (i) what sentiment a reply expresses, (ii) whether the sentiment shifts relative to its parent, and (iii) which prior message most plausibly drove the reply's sentiment. To support this setting, we introduce CaSiRe, a causal sentiment reasoning layer over public rumor conversation datasets that adds post-level sentiment labels, induced parent-child shift labels, calibrated multi-label intervention tags, and explicitly annotated causal-source labels. We then propose C$^{3}$T (Counterfactual Causal Conversation Transformer), a thread-structured temporal model that jointly predicts node sentiment and shifts, learns sparse ancestor attribution, and supports counterfactual queries by forcing conversational intervention embeddings on or off to estimate potential outcomes. Under an event-level split, C$^{3}$T improves out-of-event robustness and attribution over text-only, graph-based, and temporal baselines, and yields interpretable model-based effects: denials/corrections and evidence reduce downstream negativity, while toxicity increases it. We also benchmark open-weight LLM prompting baselines and find that added conversational context helps, but attribution remains less reliable, motivating structure-aware counterfactual modeling for social-media analysis.

---


### 73. [EmoStance: Response-Side Affective-Orientation Control for Empathetic Response Generation via Emoji Weak Supervision](https://arxiv.org/abs/2609.02133)

**<font color=#1a73e8>作者：</font>** Ziyuan Jin, Yuxuan Ge, Zheng Tian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Empathetic response generation requires models to decide not only what to say, but also how to respond to the previous speaker's affective situation. We formulate this as response-side affective-orientation control and use multi-annotator emoji distributions as weak affective--attitudinal evidence, rather than as output symbols or gold labels, to induce a latent control space that operationally approximates listener stance. We construct EmojiDialogue, an utterance-level extension of EmpatheticDialogues with emoji votes and confidence scores, and propose EmoStance, which models source-side affective expression, predicts a soft response-side orientation from dialogue context and speaker roles, and steers a frozen instruction-tuned LLM through continuous prefix embeddings. In blind pairwise evaluation with 20 annotators and 800 judgments, EmoStance achieves a 62.2% decisive win rate, with the clearest gains in contextual specificity and perceived responsiveness, while remaining complementary to external-knowledge methods. Code, annotation metadata, and reconstruction scripts are available in our GitHub repository: this https URL.

---


### 74. [OmegaUse-SOP: SOP Engineering for Professional Computer Use from Human Demonstrations](https://arxiv.org/abs/2609.02149)

**<font color=#1a73e8>作者：</font>** Yixiong Xiao, Lang An, Hucheng Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly evolving from conversational assistants into agents capable of operating external digital environments. Graphical user interface (GUI) agents play an important role in this transition, as many real-world workflows remain accessible only through user-facing software interfaces. However, despite recent progress on general computer-use benchmarks, domain-specific professional standard operating procedures (SOPs) remain challenging for GUI agents because they often involve implicit domain knowledge, software-specific conventions, and task-level verification requirements. We introduce OmegaUse-SOP, a human-in-the-loop SOP Engineering system for transforming human demonstrations of professional computer use into reusable SOP skills for GUI agents. Analogous to prompt engineering, SOP Engineering iteratively refines demonstrations, execution rules, and domain knowledge to convert professional SOPs into reusable GUI-agent skills. OmegaUse-SOP consists of four modules: Observe, Reason, Configure, and Execute. Together, these modules record expert operations as multimodal GUI traces, abstract low-level events into semantic step-level instructions, incorporate domain rules and task-specific parameters, and execute the resulting skills in live GUI environments through step-wise grounding, action generation, and verification. To demonstrate its effectiveness, we collaborate with a power-sector client and test OmegaUse-SOP on photovoltaic simulation workflows in PVsyst 7.2. The results suggest that OmegaUse-SOP can improve GUI-agent reliability on professional SOP tasks, highlighting a practical path toward deploying GUI agents in domain-specific professional software environments.

---


### 75. [A Layered Taxonomy for Chinese Learner Grammatical Error Annotation](https://arxiv.org/abs/2609.02153)

**<font color=#1a73e8>作者：</font>** Mengyang Qiu, Jungyeul Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammatical error annotation in Chinese learner writing requires labels that are both consistent and linguistically meaningful. This paper proposes a layered scheme linking computational Chinese grammatical error correction (CGEC) with pedagogical error analysis. The scheme first identifies character- and punctuation-level orthographic errors, labeling them by edit operation and subtype. Other errors receive a three-layer core label combining edit operation, linguistic domain, and part of speech, with optional Chinese-specific extensions for aspect, modality, comparison, argument structure, and complements. Drawing on CGEC resources, learner-error taxonomies, and Mandarin grammar, the taxonomy is evaluated through a coverage analysis of automatically extracted MuCGEC edits and a preliminary consistency study in which five large language models apply it to a sample. The results support the layered approach while identifying category boundaries requiring further refinement.

---


### 76. [Do Cantonese-Adapted Language Models Better Predict Cantonese Reading? A Cross-Model Eye-Tracking Evaluation](https://arxiv.org/abs/2609.02163)

**<font color=#1a73e8>作者：</font>** Ziqi Zhang, Emmanuele Chersoni, Mohammad Momenian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Information-theoretic measures derived from autoregressive language models are widely used to characterize the expectations that shape human reading, but whether language-variety-specific training improves such psycholinguistic alignment remains unclear. This question is still open for Cantonese, where recent NLP evaluations reported mixed benefits from Cantonese-specific training relative to Mandarin-oriented or general-purpose models. Using naturalistic Cantonese eye-tracking data, we compare two within-family adaptation contrasts: CKIP GPT-2 Tiny versus its lightly Cantonese-adapted JED351 derivative, and Qwen2.5-7B versus CantoneseLLM-7B, which underwent substantially more extensive Cantonese continued pretraining and instruction tuning. From each model, we derive lexical surprisal, POS surprisal, entropy before the target, and entropy reduction. Lexical surprisal and the joint four-metric model consistently favor CantoneseLLM-7B, followed by Qwen2.5-7B, CKIP, and JED351, whereas entropy reduction favors CKIP. These results suggest that more extensive Cantonese-specific training can be associated with stronger predictive fit, while model rankings also depend on the information-theoretic measure being evaluated.

---


### 77. [FUSE: An Evaluating Framework for Dangerous Capabilities of LLMs](https://arxiv.org/abs/2609.02168)

**<font color=#1a73e8>作者：</font>** Zhengyi Jin, Ru Zhang, Xiao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fragmented safety evaluation undermines the governance of dangerous AI capabilities. We present a modular framework that evaluates each model through three orthogonal pipelines---Knowledge ($K$), Defense ($D$), and Harm ($H$)---under a unified protocol, aggregating results into a standardized dangerous-capability profile $\phi$. Pluggable modules supply scenario seeds, knowledge banks, hazard queries, and judge rubrics, while the core evaluation engine remains unchanged across domains; the CB evaluation is complemented by a cyber pilot demonstrating protocol transfer.
Instantiating the framework with a chemical-biological (CB) module, we evaluate 12 commercial LLMs from four families. Our first contribution is a horizontal comparison of dangerous capability across models and model families: the three dimensions expose sharply divergent profiles---models with comparable knowledge differ in refusal resilience, and strong defenders do not generate less harmful content when they do comply---while family-level patterns further separate Claude, DeepSeek, and GPT models. The second is a temporal analysis of capability evolution: tracking $K$, $D$, and $H$ against model release dates reveals that dangerous capability has not monotonically declined; newer models deepen knowledge while only partially improving defense, showing that scaling and alignment progress do not uniformly translate into safety. Reliability is established via cross-judge consistency (bootstrap $\rho > 0.79$, 4 of 5 judges) and pipeline orthogonality ($K$--$D$--$H$ inter-correlations $\rho \in [0.32, 0.52]$).

---


### 78. [DMRL: Document-Mediated Reinforcement Learning for Skill Optimization in Advertising Recommendation](https://arxiv.org/abs/2609.02170)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Hongji Li, Song Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advertising recommendation requires continuously tuning complex system parameters while balancing commercial returns and user experience. Recent work has introduced large language models (LLMs) with skill documents to assist this labor-intensive process, but skill optimization remains largely prompt-driven, lacking a principled mechanism to attribute rewards to specific document edits. To address this limitation, we propose Document-Mediated Reinforcement Learning (DMRL), a skill self-evolution framework that models skill document optimization as a sequence of structured editing actions. In DMRL, an upper-level agent performs controlled document edits, while a frozen lower-level task agent evaluates their effects through A/B testing. To address credit assignment and long-term outcomes, we introduce two key components: (1) Dual-Relative Policy Optimization (DRPO), a post-training policy optimization method for robust and risk-aware advantage estimation; and (2) Long-term Reward Predictor (LRP), which estimates long-term outcomes by modeling population heterogeneity with disentangled representation learning and cross-attention transfer. DMRL was deployed on a large-scale short-video ads platform and extensive empirical evaluation shows that DMRL outperforms state-of-the-art baselines across key advertising metrics

---


### 79. [Lightweight Adaptation of General-Purpose VLMs for Multispectral and SAR Image Understanding](https://arxiv.org/abs/2609.02187)

**<font color=#1a73e8>作者：</font>** Shanji Liu, Kelu Yao, Junxiao Xue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General-purpose vision-language models (VLMs) now support strong visual recognition, instruction following, and generation. However, most pretrained visual encoders are built around three-channel natural images and do not directly accommodate observations such as native multispectral measurements or synthetic aperture radar (SAR). Adapting VLMs to these sensors typically requires dedicated encoders and domain pretraining, slowing the reuse of stronger general-purpose checkpoints. We show that the multi-image interface of general-purpose VLMs offers a lightweight alternative. Our protocol renders each observation as five optical views and one SAR view, names them in the prompt, and adapts the language network and selected visual transformer blocks with LoRA. This exposes band composites, spectral indices, and radar backscatter through an existing visual interface. For land-cover recognition, structured supervision couples predicted classes with sensor evidence. We further construct preference pairs in which a true label is omitted while its supporting evidence is retained, encouraging complete predictions that remain consistent with the observations. On a balanced six-class land-cover benchmark derived from BigEarthNet-v2, the adapted Qwen3-VL reaches 0.8275 micro F1. The same input and adaptation protocol improves all four tested VLM architectures and transfers to Sen1Floods11 flood verification and this http URL captioning. Image removal and mismatch controls show that the adapted models use the supplied sensor observations. Together, these results demonstrate that VLMs can be repurposed for multispectral and SAR tasks through rendered inputs and compact LoRA adaptation, without training a new foundation model.

---


### 80. [TAME: Temporal-Aware Mixture-of-Experts for Text-Video Retrieval](https://arxiv.org/abs/2609.02204)

**<font color=#1a73e8>作者：</font>** Uicheol Jung, Juyoung Hong, Hojung Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-Video Retrieval (TVR) retrieves videos that match a natural-language query, but extending image-text models such as CLIP to videos is fundamentally limited by the lack of temporal modeling. Videos exhibit frame-wise heterogeneity in appearance and motion, and compressing all frames into a single representation often obscures temporal structure and semantic transitions. To address this, we propose Temporal-Aware Mixture-of-Experts for Text-Video Retrieval (TAME), a CLIP-based framework that jointly models frame-level structure and temporal relations. First, we integrate sparse Mixture-of-Experts (MoE) layers into both CLIP encoders and apply frame-consistent routing on the vision branch so that experts specialize according to frame-level visual patterns while preserving the original vision-language alignment. Second, we introduce Frame-Temporal (FT) tokens that aggregate global cross-frame information and feed it back to each frame, enabling the visual encoder to capture long-range temporal dependencies without harming local details. Third, we design a Cross-Temporal Interaction and Aggregation (CTIA) module that refines frame-wise sentence-video similarities through staged temporal filtering and fusion. Experiments on standard TVR benchmarks show that TAME consistently improves over CLIP-based baselines. On MSR-VTT, it improves R@1 by 4.0 over CLIP4Clip, and also achieves consistent gains on DiDeMo, MSVD, LSMDC, and ActivityNet. The code is available at this https URL.

---


### 81. [LeakageBench: Document-Level Leakage Risk for Redacting Personally Identifiable Information in Document Images](https://arxiv.org/abs/2609.02207)

**<font color=#1a73e8>作者：</font>** Vishnu Prasad Vijaya Kumar, Santhosh Venkatesh, Ivan P. Yamshchikov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world personally identifiable information (PII) redaction often operates on document images---scans, screenshots, and PDF renderings---where OCR errors, layout structure, and visual noise determine whether sensitive information is actually removed. Existing PII benchmarks are mostly text-centric and do not measure document-level redaction risk: a page remains unsafe if even one identifier is missed. We introduce LeakageBench, a challenge set of 500 document images with 11,954 GDPR-aligned PII annotations spanning direct identifiers, linkage keys, and contextual re-identification surfaces. We evaluate generic OCR pipelines, commercial and task-adapted OCR-dependent detectors, and OCR-free vision-language models using entity-level F1, group-wise leakage, and document-level leakage metrics. Code Interpreter raises GPT-5.5 localization F1 from 0.090 to 0.249, but critical page-level leakage remains 0.968. These results show that stronger detection and tool assistance improve localization without making most pages safe for release. LeakageBench provides a diagnostic benchmark for high-recall, spatially grounded PII redaction in document images.

---


### 82. [ASCII Attack: Recontextualising Harmful Requests as Artistic Critique in Large Language Models](https://arxiv.org/abs/2609.02215)

**<font color=#1a73e8>作者：</font>** Da Cheng Gu, Yifei Dong, Xinghao Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment trains large language models to refuse harmful requests stated plainly, but that training is applied mostly to surface form. Requests that only recontextualise the same operational content, changing how the model reads it, are therefore only weakly covered. The ASCII Attack is one such recontextualisation. It is single-turn and black-box: one message, with no access to model internals. It embeds a fully legible harmful request in ASCIl-art characters, presents it as artwork, and asks for feedback. Unlike ArtPrompt, it hides nothing: the request stays readable. The reply is written as artistic critique and can contain operational detail that a plain request would have been refused for. Every framed prompt is paired with a direct-question control, so the contrast is isolated from topic, model and decoding variation. The contrast identifies a bundled surface, not one isolated channel. Across eleven models and eight harm topics, a harm-aware classifier judges 62% of framed prompts harmful against 42% of controls. On the most susceptible model the framed prompt succeeds 93% of the time. A single query matches or exceeds published single-query attacks under four of five harm judges. The effect tracks the model more than the topic and does not diminish with scale. At least one judge dissents from the panel majority on nearly two-thirds of framed rows, which is itself a measurement-validity finding. That pattern is consistent with mismatched generalisation.

---


### 83. [PEARL: Path-Entity Aligned Relational Learning with Contextual Subgraphs for Inductive Knowledge Graph Completion](https://arxiv.org/abs/2609.02216)

**<font color=#1a73e8>作者：</font>** Yunchi Yang, Longlong Li, Cunquan Qu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inductive knowledge graph completion (IKGC) aims to predict missing links involving entities unseen during training, requiring models to learn transferable relational and structural patterns. Existing subgraph- and path-based approaches often encode relational paths independently of their surrounding query subgraphs, although the predictive relevance of a path may vary across structural contexts. We propose PEARL, a Path-Entity Aligned Relational Learning framework that models paths as context-conditioned reasoning signals. PEARL constructs a query-specific contextual subgraph from the union of the query entities' neighborhoods and uses a large language model (LLM)-guided retriever to distill semantically relevant paths. It then builds a bipartite interaction graph over paths, contextual entities, and a global subgraph representation, allowing path embeddings to adapt to local and global structural evidence. To suppress noise introduced by the enlarged context, PEARL employs a dual-view contrastive objective that promotes representation consistency under stochastic contextual perturbations. Experiments on WN18RR, FB15k-237, and NELL-995 show that PEARL obtains the best average Hits@10 among the compared IKGC methods on all three benchmarks. Ablation studies, efficiency analyses, and case studies further validate the contributions of contextual subgraph modeling, semantic path retrieval, path-entity interaction, and contrastive regularization.

---


### 84. [SkillGLoW: Procedural-Family Skill Consolidation for Self-Improving Agents on Long-Horizon Task Streams](https://arxiv.org/abs/2609.02217)

**<font color=#1a73e8>作者：</font>** Ao Yan, Xin Zhang, Jiawei Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly self-improve by writing and reusing textual skills, kept either as one global document or as a flat pool of per-task entries, though most of the evidence comes from domains with structurally similar tasks. On long-horizon workloads where each task demands a different solution, the two forms fail in opposite ways: the document collapses into generic discipline, while the pool inflates and its entries stay bound to the instance that wrote them. We argue the missing unit of reuse is the solving procedure shared by a cluster of related tasks, and build SkillGLoW (Global-Local Weave) around it: the local skills a task writes from its own execution are aggregated into procedural families and compressed into de-instantiated global priors, while the instance detail they hold is regenerated per task rather than stored; a commit gate admits a prior only when real execution shows it does not degrade the deployed library. Across four benchmarks (mathematical reasoning, terminal automation, software repair, and embodied control) and three models, the priors gain 17.2 points (hard) over the no-skill baseline on average, with positive gains in all 12 continual-improvement runs, and 18.0 with local regeneration, while the library holds one prior per procedural family, 3.6x more compact than the per-task pool. Under the same protocol GLoW leads a published single-document optimizer on 15 of 21 cells. Unmodified, the library lifts success on unseen ALFWorld tasks from 73.9% to 83.9%, evidence that what transfers is procedure rather than task memory.

---


### 85. [InfraPatch: Cross-Task Targeted Grayscale Patch Attacks on Infrared-Adapted Vision-Language Models](https://arxiv.org/abs/2609.02233)

**<font color=#1a73e8>作者：</font>** Chengyin Hu, Dingyi Lu, Jiaju Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared vision-language models (IR-VLMs) have emerged as a promising paradigm for multimodal perception under low-visibility conditions, yet their robustness to targeted adversarial attacks remains poorly understood. Existing adversarial patch methods mainly study RGB-based models or a single downstream task and do not characterize whether localized perturbations can induce an intended semantic target in IR-VLMs. We propose InfraPatch, a white-box, per-instance framework for targeted digital grayscale patch attacks against IR-VLMs. InfraPatch optimizes a compact single-channel patch within an approximately 5% local-area budget, combines proxy-guided placement with task-adaptive semantic objectives, and induces target behaviors in image classification, image captioning, and binary visual question answering. We evaluate ten infrared-adapted model variants on 300 synthetic infrared-style images generated by applying DiffV2IR to a fixed 30-category COCO subset, using clean-conditioned targeted success criteria. InfraPatch achieves targeted attack success rates from 86.00% to 100% across the ten variants. On CLIP and BLIP-2, proxy location search improves success by 6.67 and 10.33 percentage points over optimized random placement, respectively; LLaVA-1.5 remains saturated near 100% under both settings. Patch-area and objective ablations further expose substantial differences in vulnerability across architectures and task formats. These results show that small grayscale patches can inject chosen target semantics across IR-VLM families under a controlled digital threat model, motivating stronger robustness evaluation for infrared multimodal systems.

---


### 86. [PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2609.02236)

**<font color=#1a73e8>作者：</font>** Yuyao Zheng, Haipeng Sun, Junwei Bao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning (RL) has become an effective paradigm for LLM post-training, but in multi-turn agentic tasks with sparse terminal rewards, it often provides coarse credit for intermediate actions. To obtain more fine-grained credit assignment, recent work such as GiGPO introduces step-level advantages for intermediate actions. However, these step-level signals still rely on the final outcome of each individual trajectory. As a result, actions within failed trajectories can remain poorly differentiated, so effective actions can receive the same unfavorable credit as erroneous ones. In this work, we propose Potential-Guided Policy Optimization (PGPO) for multi-turn agentic tasks. PGPO estimates empirical state potentials from anchor-state-group return statistics within each rollout group. It then derives action advantages from potential differences between adjacent states, enabling cross-trajectory credit propagation. This provides finer-grained step-level credit assignment, especially within failed trajectories. Experiments on ALFWorld and WebShop show strong overall performance relative to recent group-based RL methods. Further analysis provides evidence that PGPO yields more informative failure-side credit signals with negligible training overhead.

---


### 87. [Task-Level Natural Language Priors as Learning Signals for Low-Resource LLM Training](https://arxiv.org/abs/2609.02244)

**<font color=#1a73e8>作者：</font>** Jian Gao, Xiao Zhang, Xun Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often struggle when low-resource training data are ambiguous or incomplete. Task-level natural-language priors can provide useful guidance in such settings, but existing approaches usually treat these priors as input context rather than as learning signals during training. We propose Prior-Guided Tuning (PGT), a training perspective that incorporates natural-language priors as auxiliary learning signals for low-resource LLM training. Under this perspective, we introduce Contrastive Prior Steering (CPS), which keeps the original supervised objective intact while adding positive and negative prior-conditioned auxiliary losses to encourage task-consistent learning and discourage plausible but misleading alternatives. Experiments on AmbiMath, Jigsaw, and MNLI/HANS show that CPS consistently improves over plain and prompt fine-tuning. On AmbiMath, CPS achieves 97.6% average exact-match accuracy. On Jigsaw, CPS improves average Macro F1 by 9.5 percentage points over standard fine-tuning, and with 1/10 of the experimental training data slightly exceeds full-data plain fine-tuning. On HANS, CPS improves non-entailment accuracy by 8.3 and 5.2 percentage points for LLaMA 3.1 8B and Qwen 2.5 7B, respectively, while maintaining comparable in-domain MNLI accuracy. These results support our central claim: task-level natural-language priors can provide useful guidance as auxiliary learning signals for low-resource LLM training. Our code and data will be publicly available.

---


### 88. [RideSkill: A Hierarchical Algorithm for Generalized Ride Sharing with LLM-Driven Automatic Evolution](https://arxiv.org/abs/2609.02250)

**<font color=#1a73e8>作者：</font>** Zijian Zhao, Sen Li, Xialiang Tong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Ride-sharing, which allows multiple passengers with different origin-destination (OD) pairs to share a single vehicle, is a challenging operational problem, as it requires orders with different OD pairs to be efficiently bundled and assigned to vehicles under uncertain and varying scenarios. Although multi-agent reinforcement learning (MARL) solutions have achieved promising performance, they suffer from limited generalization (adapting to different environmental scenarios), low transferability (adapting to different platform objectives), and training difficulties in large-scale systems, such as the curse of dimensionality. Recently, motivated by the scaling of large language models (LLMs), several works have incorporated LLMs into ride-hailing systems, either by employing LLMs directly as decision-making agents or using them for automatic algorithm design. However, none of these approaches support vehicle sharing, which complicates the problem by expanding both the state and action spaces exponentially. Moreover, most of them require frequent LLM calls at inference time, making them infeasible for real-time deployment. To address these issues, we propose RideSkill, a hierarchical method for ride-sharing that leverages LLM-assisted automatic algorithmic design. RideSkill consists of a combiner that assigns appropriate skills to each vehicle from a learned skill repository, enabling adaptive dispatch under varying scenarios and objectives, and a repositioner that sequentially relocates idle vehicles to emerging regions, avoiding conflicts among vehicles. Crucially, the skill repository, combiner, and repositioner are all trained by an LLM-based automatic evolutionary method, eliminating the need for LLM calls during deployment and thus ensuring high real-time performance.

---


### 89. [APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering](https://arxiv.org/abs/2609.02253)

**<font color=#1a73e8>作者：</font>** Jie Ding, Rui Sun, Xinyuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning. Learning from prior experience is crucial for continual improvement, yet existing methods either retrieve verbose task-specific traces that burden decision-making, or distill procedural skills that remain decoupled from downstream policy adaptation. We propose APEx, a hierarchical experience utilization framework that organizes interaction history into instance-level trajectory memories and category-level procedural skills, and couples them through a closed-loop architecture of Executor, Distiller, and Planner. The three modules are optimized via a three-stage alternating GRPO training paradigm, enabling reward-guided skill distillation rather than fixed-prompt generation. At test time, distilled skills serve as procedural priors for online Planner adaptation through skill-guided test-time reinforcement learning, allowing ground-truth-free self-improvement with skill-alignment regularization to prevent policy drift. Experiments on 7 benchmarks demonstrate that APEx achieves state-of-the-art performance, surpassing GPT-5.4 by 14.7 points and the strongest memory-augmented baseline by 3.0 points.

---


### 90. [T2LSC-Bench: Benchmarking Localized Semantic Control in Text-to-Image Generation](https://arxiv.org/abs/2609.02255)

**<font color=#1a73e8>作者：</font>** Yan Wang, Xinyi Hou, Weiguo Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent text-to-image models have become increasingly capable of rendering explicit text, but reliable localized text control requires more than generating the correct string. In applications such as product labeling, signage, and interface design, target text should be rendered within a designated text-bearing region without altering the predefined subject identity or surrounding scene semantics. We refer to violations of this requirement as target-text-associated semantic leakage, in which target-text semantics are expressed through non-textual visual content beyond the designated anchor. Existing visual-text benchmarks primarily evaluate readability, spelling accuracy, and layout, leaving this form of semantic leakage largely unexamined. We introduce T2LSC-Bench, a controlled diagnostic benchmark comprising 50 seed subjects and 1,200 prompt cases per model, yielding 7,160 evaluated images across six models. Its factorized design varies semantic relation, scene openness, prompt mode, and language. A dual-branch protocol combines OCR-VLM text verification with structured VLM semantic judgments to measure Text-at-Anchor Accuracy (TAA), Semantic Subject Preservation (SSP), Semantic Leakage Rate (SLR), and Conditional Semantic Leakage Rate (cSLR). Under stress-test conditions, SLR increases from 1.2% to 18.1% and cSLR from 1.3% to 18.2%, whereas TAA decreases only from 91.4% to 90.9%. Anti-leakage prompting reduces SLR from 16.6% to 8.4% without degrading rendering accuracy. Human validation on 420 images shows strong agreement between automatic and adjudicated annotations. These results show that accurate text rendering does not guarantee local containment of target-text semantics.

---


### 91. [Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems](https://arxiv.org/abs/2609.02264)

**<font color=#1a73e8>作者：</font>** Jinxi Yu, Yubei Li, Eric Hanchen Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adapting the communication topology of an LLM multi-agent system to each query improves both accuracy and efficiency, yet current designers treat this as conditional graph generation: a variational, autoregressive, or diffusion decoder searches the $N \times N$ adjacency space, and a graph-network proxy trained on utility and a structural cost such as edge count ranks the sampled candidates. We argue that this formulation is misaligned with the problem. Empirically, topologies that survive a reward filter collapse to about six distinct graphs even when the codebook capacity grows from 8 to 64; edge count is negatively correlated with measured token consumption (Pearson $r \approx -0.4$), so sparsifying the graph makes inference more expensive; and a message-passing scorer over agent-profile nodes is adjacency-invariant whenever agents share a profile---the default configuration of published benchmarks---so it cannot rank candidates at all in that regime. These three facts motivate Codebook Agent: a vector-quantized autoencoder compresses successful topologies into a query-independent 16-entry codebook; a reward-weighted MLP maps the query embedding to a distribution over codes; and an MLP proxy that reads the flattened adjacency, regressed on measured utility and per-task normalized token cost, reranks the top decoded candidates in a single batched forward pass. With no iterative search and no message passing at test time, Codebook Agent is the most accurate method on all six benchmarks we compare (84.6 average against 83.0 for the strongest prior designer), emits a topology in 2.4 ms, and uses 21.9--33.2% fewer LLM tokens.

---


### 92. [Retrosynthesis of Synthetic Media for Explainable AI Provenance Forensics](https://arxiv.org/abs/2609.02268)

**<font color=#1a73e8>作者：</font>** Yijie Lin, Ching-Chun Chang, Isao Echizen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid proliferation of generative models on Machine Learning as a Service (MLaaS) platforms, reliably tracing the provenance of synthetic media without modifying generator architectures or parameters remains a major challenge. In this work, we propose a self-referential retrosynthesis framework for explainable AI provenance forensics under a fixed-generator setting. The framework leverages a jointly optimized encoder-decoder pair to implement a self-embedding mechanism that enables round-trip consistency verification. During inference, client inputs are first encoded and then processed by the generator to produce outputs with high visual fidelity. For forensic verification, the consistency between the resynthesized image and the query image is analyzed to determine whether the image originates from the target generative model. Our approach eliminates the need for watermark embedding or modifications to the generation process. Experimental results show that images generated from encoded inputs maintain visual quality comparable to original generator outputs, while decoded images reliably trace back to their corresponding source inputs. Furthermore, the framework provides interpretable evidence for generative content provenance, establishing a practical tool for explainable generative AI forensics.

---


### 93. [PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation](https://arxiv.org/abs/2609.02272)

**<font color=#1a73e8>作者：</font>** Yunhao Liu, Hong Phuc Pham, Jaehong Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Faithfully translating research papers into repository-level implementations remains challenging because papers often describe methods at a high level, leave implementation assumptions implicit, and require generated repositories to preserve method logic, evaluation protocols, and cross-file consistency. Despite recent advances in paper-to-code agents, their intermediate outputs are often presented as free-form plans or summaries that downstream coding agents may ignore, reinterpret, or compress, leading to algorithmic simplification and inconsistent repository structure. To address these challenges, we introduce PaperCompiler, a paper-to-code generation framework that compiles paper-grounded evidence into explicit repository-level implementation specifications. PaperCompiler grounds implementation-relevant evidence while preserving source provenance and distinguishing paper-supported, inferred, externally delegated, and unresolved information. The resulting specifications encode non-degradation requirements, ownership assignments, cross-file dependencies, and file-level constraints. Repository generation proceeds under these compiled specifications while retaining flexibility over local engineering choices not fixed by the paper. PaperCompiler outperforms strong baselines on Paper2CodeBench, achieving a 13.8% relative improvement in reference-based fidelity (from 3.64 to 4.15) and reducing high-severity evaluator critiques (from 13.2% to 6.1%).

---


### 94. [CoMerge: Conflict-Driven Preference Optimization for Multi-Task Model Merging](https://arxiv.org/abs/2609.02273)

**<font color=#1a73e8>作者：</font>** Mingjie Zheng, Zihao Chen, Wenqing Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model merging provides an efficient paradigm for constructing multi-task large language models (LLMs) without full model retraining, yet it remains challenged by parameter interference. While existing methods aim to preserve the capabilities of individual expert models and mitigate interference, they generally do not directly learn from the potentially degraded behaviors exposed by naive merging. In this paper, we propose a conflict-driven preference optimization framework for model merging (CoMerge), which reformulates model merging as a preference optimization problem. The approach utilizes a self-supervised, conflict-driven strategy that leverages the defects of naive merging methods (e.g., task arithmetic) as hard negative samples to construct preference pairs without external annotations. By applying preference optimization to refine lightweight, tensor-wise merging coefficients, CoMerge enables the model to mitigate parameter-space conflicts while preserving task-specific capabilities. Extensive experiments show that CoMerge achieves an average normalized performance of 0.9968 on MergeBench, outperforming all evaluated data-free and data-driven model-merging baselines. Furthermore, on Llama-3.1-8B-Instruct, CoMerge yields marked improvements on conflict-sensitive tasks such as instruction following and safety, while remaining highly competitive with full-parameter fine-tuning despite optimizing only 1,445 scalar coefficients.

---


### 95. [Do Large Language Models Capture the Diversity in their Training Data?](https://arxiv.org/abs/2609.02275)

**<font color=#1a73e8>作者：</font>** Youqi Wu, Farzan Farnia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are trained to model conditional distributions over text, yet it remains inadequately understood whether they capture the full diversity of plausible outputs present in their training data. We study this question through an information-theoretic lens by comparing the conditional entropy of model-generated outputs with that of the corresponding training data. Given paired input-output samples, we use conditional entropy and its matrix-based analogue based on von Neumann entropy to measure output variability beyond what is explained by the conditioning input, without requiring multiple reference outputs for the same prompt. Across LLM families with publicly available training data, including OLMo, Pythia, and GPT-Neo, we consistently find that model-generated outputs exhibit lower conditional entropy than their training data, across different model scales, sequence lengths, and decoding strategies. We observe a similar conditional diversity gap beyond language modeling, including class-conditioned ImageNet generators and text-conditioned models trained on MS-COCO. To address this gap, we propose a post-hoc correction mechanism that generates multiple outputs for each input and reweights them through a matrix-entropy projection, increasing conditional diversity while remaining close to the original model distribution. We prove the concavity of the matrix-based conditional entropy functional, which makes the resulting entropy-constrained projection a convex optimization problem, and develop a scalable mirror-descent algorithm for its implementation. Our results reveal a systematic conditional diversity gap between modern generative models and their training data, and provide an information-theoretic framework for measuring and mitigating this gap.

---


### 96. [Entangled Representations Amplify Collateral Damage in Unlearning](https://arxiv.org/abs/2609.02285)

**<font color=#1a73e8>作者：</font>** Evžen Wybitul, Tim G. J. Rudner, Christian Schroeder de Witt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A long-held intuition in interpretability research is that representational entanglement, the sharing of structure between knowledge domains in a neural network, makes unlearning harder. While the intuition is widespread, it has never been directly tested in a controlled experiment. We present a way to do so: by repurposing Selective Gradient Masking (SGTM), we train a suite of six 254M-parameter language models on English Wikipedia with graded levels of disentanglement between biology and non-biology knowledge. Applying three standard unlearning methods to every model in the suite, we find that more disentangled models consistently achieve better retain-forget trade-offs: at a fixed level of forgetting, the most disentangled models incur roughly $4\times$ lower retain cost under two of the three methods, and $1.3\times$ lower under the third. Because our intervention changes only the model, not the data or the unlearning algorithm, this is direct evidence that representational entanglement is one of the causes of collateral damage in unlearning, as interpretability researchers have long suspected. A similar design could be used to test other structural claims from interpretability.

---


### 97. [SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology](https://arxiv.org/abs/2609.02292)

**<font color=#1a73e8>作者：</font>** Ihor Stepanov, Aleksandr Smechov, Mykhailo Shtopko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of large language models (LLMs) and the growing diversity of their applications presents a unique optimization opportunity: selecting the right model for the task, while optimizing for speed, cost, and quality at a per-task level. However, inference endpoints can vary widely in quality, price, latency, context support, tool use, domain expertise, and reasoning behavior. This heterogeneity makes manual heuristics difficult to maintain and unlikely to achieve consistently favorable speed--cost--quality trade-offs on their own. We introduce \router{}, a lightweight GLiClass-based router that assigns a suitability score to each inference-time model label without autoregressive generation. The released 0.6B-parameter checkpoint combines a Qwen3 decoder with a shallow bidirectional scorer. Its decoder-KV execution path preserves a text-only key--value cache across a session, encodes only new dialogue turns, and evaluates transient candidate-label tokens without adding them to the persistent cache. The same checkpoint also predicts task type, difficulty, reasoning mode, and expected output length, and supports custom zero-shot labels. For task generation, we construct a task ontology with 23 families, 115 task types, 345 routable subtypes, 1,173 synthetic examples, and an orthogonal axis of 30 domains. Using this structure, we generate 150,000 verifier-scored tasks and 15,000 open-ended tasks. We then train the Qwen3 decoder on these tasks, while explicitly separating learned request prediction from per-task policies for attributes such as eligibility, cost, cache reuse, safety, and sovereignty. Across six LiveBench subsets, the router outperforms the mean candidate; on the selected 1,000-task subset, it achieves an aggregate top-1 score of 0.707 versus 0.696 for the strongest fixed model, with benchmark-dependent gains.

---


### 98. [Domain shift-robust object detection with GenAI image editing](https://arxiv.org/abs/2609.02299)

**<font color=#1a73e8>作者：</font>** Isabel D. Stein, Thijs A. Eker, Sebastiaan P. Snel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detectors often degrade under domain shifts such as changes in lighting, weather, or occlusion. These shifts alter object appearance and expose a reliance on visual shortcuts learned from the training distribution that do not generalize across domains. Acquiring sufficient real-world samples to capture such domain variation is particularly difficult in specialized, low-data settings. Recent advances in diffusion-based generative image editing have shown promise for improving the in-domain performance of object detectors through synthetic data augmentation. However, their potential to improve out-of-domain robustness remains largely unexplored. We hypothesize that generative image editing can simulate a controlled domain shift in training data, effectively bridging the gap between source and target domains. To test this, we studied camouflaged military vehicle detection as a challenging domain shift scenario. Detectors trained on uncamouflaged data demonstrate substantial degradation on real test imagery containing foliage, netting, and multi-spectral camouflage across 15 vehicle classes in close-up, ground-level imagery. We used two diffusion-based editing models, Qwen Image Edit 2509 and Flux.2 Dev, to synthetically add camouflage to the training data, alongside a LoRA fine-tuned version of Qwen. A non-generative black-bar occlusion baseline served as a lower bound on augmentation quality. Using a GroundingDINO detector trained on real and synthetic data, generative camouflage augmentation yielded substantial mAP improvements for foliage (+20.1) and netting (+14.4) camouflage. Generating multi-spectral camouflage proved more challenging, but LoRA fine-tuning improved performance by 4.4 mAP over the uncamouflaged baseline.

---


### 99. [Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds](https://arxiv.org/abs/2609.02302)

**<font color=#1a73e8>作者：</font>** Axel Ahlqvist, Richard Guan, Juan-Pablo Rivera 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A core obstacle to alignment evaluation is evaluation awareness: capable models can tell when they are being tested rather than deployed, weakening the conclusions a safety evaluation can support. We present two techniques that make simulated alignment evaluations harder to distinguish from real deployments. Our first technique, critique refinement, spends additional inference-time compute on each simulator action: the simulator generates multiple candidate actions, refines them using feedback from an instance of the target model on how to make them more realistic, and continues the evaluation with the most deployment-like candidate. Our second technique, DISH (Deployment-Imitating SWE-Agent Harness), wraps the target in an agent harness, reducing the gap between simulated and real deployment environments in coding settings. We test the techniques on multiple target models and find that they compose: applying both yields larger realism gains than either alone. Our results show that automated approaches can improve the realism of alignment evaluations, and that these improvements use additional compute more effectively than making the audits longer.

---


### 100. [YesTrack: Referring Multi-Object Tracking via MLLM-based Yes/No Verification](https://arxiv.org/abs/2609.02318)

**<font color=#1a73e8>作者：</font>** Quansheng Hu, Qin Sun, Qiansen Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring multi-object tracking (RMOT) aims to track every instance in a video that matches a given language expression. Despite the recent integration of multimodal large language models (MLLMs) to enhance generalization, existing methods predominantly relegate them to the role of caption generators, necessitating external modules for final decision-making. This paradigm not only introduces extra latency but also severely underutilizes the inherent vision-language alignment capabilities of MLLMs. To address these limitations, we propose YesTrack, a novel two-stage RMOT method that reformulates referring as a discriminative task, directly leveraging MLLMs for Yes/No verification without explicit text generation. To further enhance the reliability and efficiency of this MLLM-based verification, we introduce two lightweight temporal consistency constraints: Temporal Confidence Prior (TCP) and Temporal Reference Propagation (TRP). We further validate the generality of this discriminative paradigm by proposing YesTrack-MOT, a straightforward yet highly effective instantiation for generic multi-object tracking (MOT). Experiments on Refer-KITTI and Refer-KITTI-V2 show that YesTrack significantly outperforms existing state-of-the-art methods while maintaining high efficiency, even when implemented with the smallest variant of Qwen3-VL. Code is released at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-177](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

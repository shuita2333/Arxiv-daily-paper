# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-450**（第 9/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 401. [GSM: Efficient Language Modeling with Shared Global State](https://arxiv.org/abs/2609.33465)

**<font color=#1a73e8>作者：</font>** Yunao Zheng, Bin Wen, Xiaojie Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efficient language models must reduce not only the cost of individual accesses to past context but also the overhead of repeatedly selecting and processing historical information across layers. We introduce the Global State Model (GSM), a causal encoder--decoder architecture that concentrates the selection and aggregation of long-range information in the encoding stage. Through multiple stages of history retrieval, the encoder progressively incorporates long-range information into representations at recent positions, forming a shared state with a fixed window size. Each decoder layer accesses this same state using queries updated from the preceding layer, preserving computational depth while avoiding repeated construction of historical key--value (KV) representations and long-range indexing. As a result, neither the decoder's per-step attention cost nor its KV cache size grows with the history length. Experiments show that GSM improves computational efficiency and reduces cache overhead while maintaining model performance and the ability to use long-range information, offering a shared-state architecture for efficient language modeling.

---


### 402. [A Cheap Verifier is Good Enough: LLM Post-training is Robust to Erroneous Rewards](https://arxiv.org/abs/2609.33467)

**<font color=#1a73e8>作者：</font>** Andreas Plesner, Curtis Northcutt, Francisco Guzmán 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When post-training large language models on tasks with semi-verifiable rewards, there are many factors (training steps, base model size, training order, data quality, verifier accuracy, etc.) that practitioners must contend with to maximize model performance. Yet, it remains unclear how well verifier agreement predicts post-training performance on such tasks. In this paper, we explore this question with over 11k H100 GPU-hours, across HealthBench and PRBench tasks in medical, legal, and finance domains. Across the tested domains, Qwen3 trainees (1.7B-8B on HealthBench; 8B on PRBench), evaluation splits, and frontier LLM reference judges (which we call golden verifiers), higher verifier agreement does not consistently identify the best training verifier. Expensive verifiers need not outperform inexpensive ones, and open-weight Gemma verifiers produce strong training outcomes. We compare two low-cost choices retrospectively -- a cost-reducing choice and a balanced choice -- with estimated grading cost reductions of 98.8%-99.7% relative to the golden grading protocols and average post-training score gaps of 1-3 points from the best evaluated training verifier. These averages include larger losses in individual settings; they do not establish that verifier choices are interchangeable.

---


### 403. [LiveOption: Evaluating LLM Agents in Structured Option Trading with Nonlinear Payoffs](https://arxiv.org/abs/2609.33470)

**<font color=#1a73e8>作者：</font>** Haochen Luo, Yifan Li, Binh Minh An 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) and multi-agent systems (MAS) have shown promise in financial decision-making, yet existing evaluations focus on equity trading and primarily assess directional prediction, overlooking the structural complexity of derivative markets. Option trading introduces fundamentally different challenges, including nonlinear payoffs and multi-leg strategy construction, requiring structured decisions rather than simple directional bets. We introduce LiveOption, an evaluation framework for LLM-based agents in option trading. LiveOption formulates the problem as structured sequential decision-making under realistic execution and capital constraints, and provides a reproducible environment with standardized interaction protocols. The framework includes three task suites covering portfolio overlays, event-driven earnings trading, and 0DTE intraday trading. We further propose a hierarchical metric suite that evaluates action validity, decision quality, risk characteristics, and outcome-level performance. Experiments show that current agents often fail to achieve competitive returns in most scenarios. LiveOption offers a principled testbed for evaluating structured decision-making beyond outcome-based metrics.

---


### 404. [Just Let Linear States Forget the Distant Past: Prefix Caching via Suffix Replay for Hybrid LLMs](https://arxiv.org/abs/2609.33477)

**<font color=#1a73e8>作者：</font>** Yirui Liu, Ruoling Qi, Xuaner Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hybrid LLMs interleave full-attention layers with linear-attention layers to reduce long-context inference cost, but this structure complicates prefix caching. Full-attention KV caches are token-addressable, whereas linear-attention layers maintain recurrent states that cannot be rolled back to arbitrary prefix boundaries. Existing systems materialize recurrent-state checkpoints, restricting prefix reuse to checkpoint-aligned positions.
We present SuffixReplay, the first prefix caching system that lets hybrid LLMs reuse cached prefixes at every cache-supported page boundary without materializing recurrent-state checkpoints. Our key insight is to just let linear states forget the distant past. Modern linear-attention mechanisms use recurrent decay and gating to attenuate the influence of old inputs. Therefore, instead of checkpointing every prefix boundary, SuffixReplay approximates the state at a matched boundary by replaying only a recent suffix of the layer's input hidden states, which we retain as anchors. At the algorithmic level, SuffixReplay combines layer-wise and token-wise anchor sparsity with a bounded replay budget to control storage, computation, and quality. At the system level, it uses an independently managed anchor sidecar and a pipelined replay path to overlap anchor movement and state reconstruction with the native serving pipeline. We evaluate SuffixReplay on three hybrid LLMs: OLMo-Hybrid-7B, Qwen3.5-4B, and Qwen3.6-27B-FP8. Across these models, SuffixReplay retains 91.4-100% of full-prefill quality on average across LongBench and RULER, while using only 0.36-0.51x the amortized per-token storage of SGLang's default 8192-token checkpoint cache. Integrated into SGLang, SuffixReplay reduces median TTFT by 15-70% on branching workloads, sustains 2.3-4.3x SGLang's throughput when the working set exceeds HBM, and matches SGLang on high-hit continuation traffic.

---


### 405. [What Does It Mean to Forget a Person? Individual-Level Unlearning in Vision-Language Models](https://arxiv.org/abs/2609.33481)

**<font color=#1a73e8>作者：</font>** Xiongtao Sun, Hui Li, Tiantong Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Erasing individual identities from Vision-Language Models (VLMs) is uniquely challenging because personal data is entangled across modalities rather than stored as isolated attributes. However, existing multimodal unlearning benchmarks primarily evaluate attribute-centric forgetting, overlooking the more critical objective of individual-level unlearning: eliminating a model's ability to access, link, and reconstruct target-related information across modalities. To address this gap, we propose IDUnlearn-Bench, the first benchmark for individual-level multimodal unlearning in VLMs. It represents each individual as connected multimodal evidence and evaluates four task families: attribute access, identity access, identity binding, and identity reconstruction. Experiments on representative VLMs and unlearning methods show that successful attribute-centric forgetting often leaves substantial identity-level knowledge intact and can be non-monotonic: reducing one form of risk may amplify another. Models may suppress selected information while still identifying the target, linking records, or reconstructing the individual. These findings reveal a fundamental gap between forgetting information about a person and forgetting the person as a whole.

---


### 406. [How Synthetic Labels Improve Conformal Prediction: A Perspective on Conditional Coverage](https://arxiv.org/abs/2609.33482)

**<font color=#1a73e8>作者：</font>** Qianyi Chen, Bo Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction provides distribution-free finite-sample marginal coverage, but post-hoc calibration data may be too scarce to learn how uncertainty varies across inputs. Meanwhile, abundant covariates can often be labeled cheaply by domain models or general-purpose language models. We study whether these synthetic labels can improve conditional coverage when only a small trusted sample is available. Building on score-quantile regression, we introduce prediction-powered quantile learning: a synthetic-labeled pool estimates pinball risk, paired trusted and synthetic outcomes correct its bias, and an independent trusted split performs final conformalization. Profiling pinball risk over scalar corrections reveals that population conditional-coverage error is its functional gradient; the corresponding Hessian removes global shifts and weights remaining shape error by boundary density. Composing this geometry with prediction-powered learning yields a three-resource expansion and a benefit--cost rule for synthetic power. Across eight regression benchmarks, synthetic-powered quantile learning substantially improves downstream conditional coverage while preserving marginal validity and producing more compact prediction sets. A human-rating study finds similar gains from external LLM labels and exposes a quality--quantity--cost tradeoff.

---


### 407. [DISCO: Distributed Long Context Scaling with Grounding-Reasoning Disaggregation](https://arxiv.org/abs/2609.33485)

**<font color=#1a73e8>作者：</font>** Guanzheng Chen, Viet Dac Lai, Subhojyoti Mukherjee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) advertise million-token context windows, reasoning quality often collapses as inputs grow -- a phenomenon termed context rot. This failure stems from a structural entanglement in monolithic architectures, where the massive search burden of contextual grounding exhausts the representational capacity needed for complex reasoning. To resolve this, we propose Grounding-Reasoning Disaggregation via DIStributed long COntext scaling (DISCO). Inspired by distributed computing frameworks like Apache Spark, DISCO partitions long context across a fleet of Worker LLMs dedicated exclusively to parallel, localized grounding. A central Driver LLM, trained via Reinforcement Learning (GRPO) to optimize planning, orchestrates execution by dynamically mapping queries into atomic extraction tasks and reducing the gathered evidence to synthesize a final answer. By isolating reasoning from raw context noise, DISCO effectively eliminates context rot. On RULER-QA (1M tokens), it maintains 78.4% accuracy where standard baselines collapse. Furthermore, it outperforms full-context models by up to 9.8 points on LongBench v2 and matches frontier models like Gemini-3-Pro-Preview while reducing inference costs by over 80%, establishing a highly efficient paradigm for robust long-context inference.

---


### 408. [LLMs Trust Their Own: Identity-Dependent Conformity in Multi-Agent Systems](https://arxiv.org/abs/2609.33495)

**<font color=#1a73e8>作者：</font>** Liron Soffer, Ravid Shwartz-Ziv, Chen Shani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in multi-agent settings, where agents observe and influence one another, making social influence a key dimension of AI behavior and safety. We investigate whether LLMs' responses depend on the social identity of other agents, beyond the effect of their consensus. We construct judgment tasks with a single correct answer, and place models in a multi-agent setting where they receive incorrect answers from other agents whose social identities (AI or human, model family, or an arbitrary minimal group) are either shared with or distinct from their own. Across 12 open-weights models and nine tasks, we find a bidirectional effect of group identity on conformity to incorrect answers: in-group consensus increases conformity (in-group favoritism), whereas out-group consensus decreases it (out-group divergence). Unlike humans, for whom one ally breaking the consensus sharply reduces conformity, models are unmoved by an ally from the majority's group. Worse, a correct ally from the opposing group intensifies this bidirectional effect. Chain-of-Thought reasoning suppresses most of these effects, yet an in-group ally still reduces conformity to an incorrect out-group majority. Labeling peers as safety-aligned shifts overall conformity but leaves in-group favoritism and out-group divergence intact. These results show that group identity shapes how LLMs aggregate information across agents, independently of its correctness, and identify a manipulation surface for multi-agent AI systems.

---


### 409. [RelaxKV: Recomputation Guided by the Query with Sparse Context Attention for Efficient KV Cache Reuse](https://arxiv.org/abs/2609.33503)

**<font color=#1a73e8>作者：</font>** Ruoling Qi, Yirui Liu, Xuaner Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-request KV caching reduces the prefill cost of Retrieval-Augmented Generation (RAG), but conventional prefix caching severely limits cache reuse across requests. Position-Independent Caching (PIC) removes this constraint by reusing independent chunks, but their KV states miss cross-chunk interactions. Existing methods selectively recompute token states to recover these missing interactions, but primarily allocate the recomputation budget to selecting which states to recompute, while fixing the recomputation context to the full causal prefix. We introduce RelaxKV, which formulates selective cache repair as a joint allocation problem over repair targets and recomputation context. Guided by the user query, RelaxKV identifies layer-specific repair targets and restricts their recomputation to a query-relevant context, reducing attention computation. Across four decoder models, RelaxKV at a 15% anchor ratio improves aggregate LongBench performance over ProphetKV on all models. On Qwen3-14B, RelaxKV provides a stronger quality-TTFT trade-off than ProphetKV across a 5%-30% anchor-ratio sweep, and achieves the best selective results on RULER-MV and LV-Eval at 16K and 32K context lengths. Controlled ablations further demonstrate the importance of recomputation context selection.

---


### 410. [PPG-LM: A Photoplethysmography-Language Model with Multi-Level Clinical Alignment](https://arxiv.org/abs/2609.33516)

**<font color=#1a73e8>作者：</font>** Xiaoda Wang, Minxiao Wang, Maxwell A Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Photoplethysmography (PPG) is widely recorded by clinical monitors and consumer wearables, providing a scalable source of continuous physiological information. These recordings offer an opportunity for physiological assessment at scale, but realizing this potential requires models to learn from both signal-derived physiological supervision and broader clinical context captured in electronic health records (EHRs). This involves aligning information spanning local observations, care events, and entire visits with PPG representations at corresponding temporal scales. However, existing PPG foundation models primarily rely on task-specific prediction heads, while the medical knowledge of large language models does not necessarily translate into waveform understanding. To bridge this gap, we introduce PPG-LM, the first PPG-language model family to learn physiological representations from both signal-derived supervision and broader clinical context captured in EHRs. To construct clinically grounded captions, we develop an automatic captioning pipeline that generates segment-, event-, and visit-level descriptions from signal measurements and structured EHR records. We then learn from these pairs through a two-stage framework that first establishes segment-language correspondence through contrastive learning and waveform-conditioned captioning, then extends alignment to events and visits through time-aware aggregation and temporal statement matching. Pretrained on approximately 73k hours of PPG, PPG-LM supports language-based recognition, cross-modal retrieval, and segment captioning. Experiments on MC-MED, MIMIC-III, and VitalDB show improved retrieval and caption factuality over language-model baselines and gains over PPG and time-series foundation models on multiple clinical prediction tasks.

---


### 411. [TRACE: Governing Memory Validity in Evolving Multi-Agent Systems](https://arxiv.org/abs/2609.33517)

**<font color=#1a73e8>作者：</font>** Wenjun Xiong, Shengtao Zhang, Shangding Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Persistent memory lets language-model agents carry information across long-running collaborations, but leaves a lifecycle question open: what may a returning agent still act on once the shared state has changed? A memory can be correctly retrieved, relevant to the current task, and faithful to its source, and nonetheless be inadmissible for action: an itinerary saved before a pause still names the hotel the team has since replaced. We formalize this as temporal memory admission and present TRACE, a training-free layer that treats re-entry as an eligibility decision rather than a storage or retrieval operation, reconciling a departure checkpoint against absence-period updates, resolving explicit and implicit invalidation, and releasing a bounded Return View only when it covers the returning role's open obligations. We evaluate TRACE under three actor models on Memora, STALE Type II, and a derived ManBench-Return setting, each recast as return episodes: one agent departs, four teammates change the shared state, and the agent rejoins. What separates methods is not overall accuracy but whether one can retain valid memory and reject stale memory at once, and no single-policy baseline can: Restore (reinstate the departure checkpoint in full) admits stale state, Reset (start the return from an empty memory) discards valid state, each bottoming out at 0% on one of the two. TRACE is the only method high on both, reaching 92.6-98.3% valid-information availability with 98.4-99.5% invalid-information rejection on ManBench-Return, within 3.8 points of the best baseline's overall accuracy. On STALE Type II it improves Overall over the strongest comparison policy by 22.3 (Qwen), 18.5 (Gemini), and 27.5 (DeepSeek) points at roughly 2.3 times their tokens, while a write-time consolidation pipeline is more accurate still at 3.99 times TRACE's.

---


### 412. [SceneScaffold: Active Scene-State Construction for Unified 3D Scene Understanding](https://arxiv.org/abs/2609.33518)

**<font color=#1a73e8>作者：</font>** Xiangqi Li, Libo Huang, Jiarui Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D large multimodal models (3D-LMMs) rely on a visual bottleneck to compress complex 3D scene evidence into a limited number of visual tokens compatible with large language models (LLMs). Current visual bottlenecks, however, often passively compress heterogeneous 3D evidence into a homogeneous object-centric token sequence, leaving the spatial organization of the scene under-represented. This under-representation forces the LLM to recover spatial relations from a flattened token sequence, leading to unstable reasoning in relation-intensive and spatially ambiguous scenes. To address this issue, we propose SceneScaffold, an active scene-state construction framework for unified 3D scene understanding. SceneScaffold reformulates the visual bottleneck from a passive feature compressor into an active scene organizer, constructing a role-aware spatial scaffold before language reasoning. Specifically, SceneScaffold organizes superpoint-level visual evidence into scene-state components with distinct structural roles: entity states preserve core object semantics, scene-frame states maintain spatial references via boundary and region anchors, relation states encode object-environment interaction cues, and a global summary provides compact context. Through this role-aware construction, SceneScaffold provides the LLM with a spatially organized scene representation before language reasoning. Experiments on unified 3D scene understanding tasks, including 3D visual grounding, question answering, and dense captioning, demonstrate the effectiveness of SceneScaffold, while diagnostic results further show its applicability to relation-intensive and spatially ambiguous cases. Code is available at this https URL.

---


### 413. [LLM4Trust: Exploring the Capabilities of Large Language Models for Trust Evaluation](https://arxiv.org/abs/2609.33521)

**<font color=#1a73e8>作者：</font>** Jie Wang, Yanbo Sun, Zheng Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trust evaluation plays a critical role in cybersecurity by supporting risk mitigation and decision-making. A variety of trust evaluation methods have been proposed, with learning-based approaches offering high accuracy and automation. However, they often require substantial ground truth, suffer from low training efficiency, lack support for basic trust properties, and provide limited explainability. Large Language Models (LLMs) offer a compelling alternative due to their strong zero-/few-shot reasoning abilities and broad knowledge. To this end, we propose LLM4Trust, the first benchmark framework that systematically explores the capabilities of LLMs for trust evaluation. We first construct diverse trust graphs to model five basic trust properties and design corresponding property understanding tasks. We then assess the ability of eight representative LLMs to understand these properties under nine prompt methods. Based on this exploration, we identify the most effective LLM-prompt combinations and apply them to five real-world datasets for validating LLMs' trust evaluation capability. During this process, we propose two strategies to extract key information from large-scale trust graphs, addressing the context window limitations of LLMs. Extensive experiments show that LLMs can effectively understand basic trust properties and have great potential for real-world trust evaluation, particularly under limited supervision. However, they remain vulnerable to attacks targeting trust graphs and demonstration examples used in few-shot prompting, and incur high inference costs. Accordingly, we propose a defense mechanism and batch inference to improve the robustness and efficiency of LLM-based trust evaluation. The source code of LLM4Trust is available at this https URL

---


### 414. [E-CONAN (Entailment, CONtradition And Neutral) Diagnostics Dataset Investigating Linguistic Phenomena in Arabic Natural Language Understanding](https://arxiv.org/abs/2609.33530)

**<font color=#1a73e8>作者：</font>** Khloud AL Jallad, Nada Ghneim, Ghaida Rebdawi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Understanding (NLU) plays a crucial role in various applications, yet its performance suffers from weaknesses in handling the complexities of human languages, ranging from lexical ambiguity to high-level reasoning difficulties. Analyzing errors across diverse linguistic phenomena is crucial for NLU improvement, as it will help humans get insights to comprehensively assess models' limitations and capabilities, so optimizing models' generalization. Notably, several benchmarks contain diagnostics datasets designed for investigation and fine-grained error analysis. When highlighting the gaps in the state-of-the-art, we noted that there is no naming convention for macro and micro categories or even a standard set of linguistic phenomena that should be covered. To overcome this gap, we propose an initial hierarchy for Cross-Lingual NLU error analysis. Moreover, we propose a methodology to create an NLI hierarchical framework and applied a case study on Arabic NLU. Moreover, this paper introduces E-CONAN diagnostics dataset, a freely available dataset manually-annotated with coarse-grained and fine-grained categories based on our proposed Arabic hierarchy. E-CONAN dataset helps NLU designers better understand their models by doing error analysis and in-depth investigation. We used E-CONAN to investigate the performance of 9 pretrained language models and 5 LLMs. Results indicate that LLMs outperform pretrained models in world knowledge and commonsense reasoning macro-category, and underperform pretrained models in syntactic macro-category. Moreover, the hardest phenomena for all models is Reasoning, and the easiest phenomena for all pretrained models is Syntactic, and the easiest for LLMs is Lexico-Syntactic.

---


### 415. [ManiEdit: Sequential Unstructured Knowledge Editing for Language Models from a Manifold Perspective](https://arxiv.org/abs/2609.33534)

**<font color=#1a73e8>作者：</font>** Rui Liu, Chenheng Zhang, Haoxuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) inevitably generate some incorrect or outdated content, necessitating efficient and precise mechanisms for continual knowledge updates. However, existing model editing methods struggle to sequentially edit unstructured long-form knowledge, suffering from severe edit forgetting and degradation of general capabilities. To address these challenges, we reframe knowledge editing from a manifold perspective, viewing it as a localized displacement of an edit sub-manifold within the global knowledge manifold. Under this formulation, the problem can be decomposed into two key questions: (i) how to identify representative edit points that effectively anchor the edit sub-manifold, and (ii) how to preserve the remaining manifold structure during the sub-manifold displacement process. Based on this perspective, we propose ManiEdit, a novel manifold-aware autoregressive editing framework consisting of two core components. Pivot Localization addresses the mediocre-point dilemma by identifying high-leverage pivots to anchor the edit sub-manifold. Manifold-Aware Preservation preserves different knowledge types through an energy-weighted penalty combined with recursive null-space alignment. Experiments on two base LLMs and four unstructured editing benchmarks demonstrate that ManiEdit achieves state-of-the-art performance, outperforming the strongest baseline by up to +27.81 BERTScore and +8.50 ROUGE-L, while maintaining near-original general capabilities across six representative downstream tasks. Our code is available at: this https URL

---


### 416. [Does Execution Require Target KV Fidelity? A Mixed-Fidelity KV Runtime for LLM Serving](https://arxiv.org/abs/2609.33536)

**<font color=#1a73e8>作者：</font>** Jiantong Jiang, Yue Yang, Peiyu Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) serving is increasingly constrained by the GPU memory consumed by key-value (KV) caches. Existing compression, eviction, and offloading techniques alleviate this pressure, but serving runtimes typically treat only the configured target KV representation as execution-ready. Under memory pressure, this target-only contract can turn KV shortage into request stalls and preemptions. We present ElasticKV, a mixed-fidelity KV runtime built on the observation that target fidelity need not gate execution. ElasticKV introduces a compact intermediate KV state, making fidelity a runtime-managed execution property. To realize this state in a paged serving runtime, ElasticKV combines (i) a pair-structured layout that turns fidelity reduction into reusable GPU capacity, (ii) a dual-mode attention backend that directly consumes the compact state while preserving the native target-only path, and (iii) pressure-aware fidelity management that adapts KV fidelity to memory pressure. Our extensive evaluation across diverse workloads, model families and scales, and GPU platforms demonstrates the effectiveness and generality of ElasticKV. Under high concurrency, ElasticKV achieves 3.8-4.0$\times$ lower time-to-first-token (TTFT) and 9.1$\times$ lower P90 TTFT than vLLM while preserving generation quality.

---


### 417. [Jev Matches 7B Language Models for Speech-Neuroprosthesis Rescoring](https://arxiv.org/abs/2609.33538)

**<font color=#1a73e8>作者：</font>** Gabriele Cinà  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A speech neuroprosthesis decodes attempted speech from brain activity and ends by rescoring the decoder's candidate sentences with a language model of several billion parameters, the only component that needs a GPU. Replacing that model with a cheaper one is hard: general language models asked to pick one sentence from a list answer from where a label sits in the list rather than from the sentence itself. We pose rescoring as a single typed decision, one call that returns a probability for every candidate, served by Jev, a hosted model trained for calibrated decisions, and combine it with the decoder's own score. On 978 held-out sentences from a participant with ALS, where the published decoder alone reaches 8.1% word error, Jev reaches 7.5% against 7.8% for both OPT-6.7b and Qwen2.5-7B; with the decoder's weight re-tuned, 6.9% against 7.2% and 7.4%. Jev is ahead in all four comparisons and at most 0.2 points behind at the 95% bound. It costs 0.07 USD per thousand sentences and needs no GPU; a dedicated GPU running a 7B model is cheaper per sentence only above 43% utilisation, far beyond what one user generates. End-to-end latency over the internet is 262 ms, of which 62 ms is spent at the provider, the same order as a 7B model on a local GPU (27 ms) but not faster.

---


### 418. [Reasoning on the Simplex: Geometric Fixed-Point Models](https://arxiv.org/abs/2609.33540)

**<font color=#1a73e8>作者：</font>** Talgat Daulbaev, Ilya Glazkov, Maxim Rakhuba 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Looped reasoners spend test-time compute by iterating a weight-tied map, but a small residual does not mean the state is a fixed point when that map lives in unconstrained latent space. We propose Geometric Fixed-Point Reasoning (GFPR), in which the iterated state is the prediction itself: a field of categorical beliefs on a product of simplices, whose argmax is the answer at every step. Because the state is a belief, task structure can be imposed through compact convex relaxations, either as structured readouts or directly in the recurrent state; in the latter case the update remains a continuous self-map, so a fixed point exists for any parameters. At about 7M parameters, GFPR reaches 95.1% exact match on Sudoku-Extreme, 92.0% on Maze-Hard, and 100% sequence accuracy on S_5 length 128, above the published FPRM numbers at the same scale. The same update also trains a 201M language model on FineWeb-Edu in which each site is a distribution over the vocabulary; with 24 Picard steps it is above GPT-2 small on four zero-shot multiple-choice tasks and above GPT-2 medium on ARC-Easy.

---


### 419. [TerMeZO: Ternary Sparse Zeroth-Order Optimization for Fine-tuning BitNet Models at the Edge](https://arxiv.org/abs/2609.33548)

**<font color=#1a73e8>作者：</font>** Houssem Sifaou, Prabodh Katti, Bipin Rajendran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning anguage models (LLMs) with first-order optimizers requires a memory several times larger than that required for inference. Memory-efficient zeroth-order optimization (MeZO) sidesteps this cost by estimating gradients from forward passes only. However, for BitNet architectures, a family of LLMs with ternary {-1,0,1\} weights and 8-bit activations, fine-tuning requires updating full-precision latent weights, and thus the memory footprint of MeZO no longer matches that of inference. A promising solution is to finetune only a subset of the latent weights, but existing sparse zeroth-order (ZO) methods either ignore the ternary structure or require first-order gradient information to build a sparse mask, which is at odds with the purpose of ZO fine-tuning. We propose TerMeZO, a sparse MeZO scheme that exploits the geometry of the ternary quantizer itself to identify the latent weights that are more likely to change values during fine-tuning, at no additional data or memory cost. Our convergence analysis shows that TerMeZO can converge faster than full-parameter MeZO, owing to its optimized reduction of the fine-tuning effective dimension. We run extensive experiments on BitNet models ranging from 1B to 3B parameters, spanning classification, instruction-following, and mathematical reasoning tasks. TerMeZO matches or exceeds the performance of full-parameter MeZO while substantially reducing the fine-tuning memory footprint.

---


### 420. [Fine Until Fine-Tuned: Repeated Solutions Make Reasoning Fragile](https://arxiv.org/abs/2609.33559)

**<font color=#1a73e8>作者：</font>** Ely Sheikh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recipes such as s1 and LIMO teach a model to reason with little data by showing it the same thousand or fewer worked solutions many times over. Judged when that training ends, the repetition looks harmless. But reasoning models are often trained again, and we find that repetition leaves their reasoning fragile to that next stage, even when the stage has nothing to do with reasoning. We fine-tuned Qwen3.5-9B-Base on its own correct solutions to competition math problems, either drilling a few hundred of them about eight times each or showing many more once; with the same amount of training, both solve about 95% of held-out problems. A single pass of ordinary instruction tuning leaves the once-trained model where it was, while the drilled one falls to 86.0%, and harsher later stages take it to 59.3% or below. A third model that visited the drilled problems just as often, with a new solution at every visit, was unharmed, so the damage comes from seeing the same texts again rather than from having few problems. The break recurs with a stronger model's traces, in further training runs and on other models and tasks. It is also cheap to undo: the reasoning is suppressed rather than erased, and five updates of reasoning training bring almost all of it back, as does brief training on the reasoning format with almost no mathematics. Fresh solutions prevented the damage, and so did replaying 6.25% of the original solutions in a gentler later stage, so our claim concerns later training without such replay. Sharpening alone does not explain the break, since a model sharpened three-quarters as much without repetition was unharmed. On a skill the base model could not perform within a token budget, repetition mainly cost learning.

---


### 421. [HiLoRe: What to Store, Compress, or Recompute for Efficient GRPO Training](https://arxiv.org/abs/2609.33570)

**<font color=#1a73e8>作者：</font>** Xinrui Chen, Mengyang Li, Ou Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-relative policy optimization (GRPO) makes learner-side activations a major memory-computation bottleneck: gradient checkpointing reduces activation memory through recomputation, but fixed schedules can leave roughly 18 GB unused on a 48-GB GPU despite substantial recomputation overhead. Existing activation-management methods set state fidelity from execution cost, tensor properties, or generic compression sensitivity, without explicitly incorporating GRPO's analytic update structure into state-fidelity allocation. We formalize this dependence as policy-update exposure, linking the current GRPO loss coefficients to state-level approximation sensitivity. These coefficients are available before backward without an additional backward pass. We introduce HiLoRe, which allocates graph-attributed recovery units among high-precision storage, low-precision compression, and deterministic recomputation using measured recovery utility and update-conditioned approximation risk. It combines high-precision storage and deterministic recomputation with low-precision recovery under a calibrated risk budget. Across five model-task settings with 2K responses and memory < 1.10 times GC's per-GPU actor-update peak, HiLoRe's actor-update throughput gains reach 13.5% over GC and 7.9% over the fastest evaluated baseline, with paired mean downstream-score differences below 0.6 percentage points.

---


### 422. [OpenFC: Learning Verification Policies towards Open-Search Fact Checking](https://arxiv.org/abs/2609.33579)

**<font color=#1a73e8>作者：</font>** Xinming Wang, Kaixiang Qiu, Yansong Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-search fact checking is not merely retrieval followed by classification, but a sequential decision problem in which every query, source visit, and stopping decision reshapes the evidence available for verification. Yet existing systems often distribute these decisions across predefined pipelines or separately prompted modules rather than learning them as a unified task-specific policy. We introduce \textbf{OpenFC}, a unified verification-policy training framework that post-trains Qwen3-8B as a compact next-action controller over reasoning, evidence acquisition, and stopping. OpenFC learns this policy in two stages. \textbf{Stepwise-Calibrated Cold Start (SCCS)} uses a strong training-time supervisor to review post-initial reasoning, tool-use, and stopping proposals before execution, producing reliable trajectories for supervised fine-tuning without access to gold verdicts. \textbf{Verification-Aware Reinforcement Learning (VA-RL)} then improves the cold-start policy on unresolved claims through budget-aware tool rewards, label-aware advantage reweighting, and localized response masking. Across six fact-checking benchmarks, OpenFC achieves 70.39\% average accuracy and 63.30\% macro-F1, the highest overall averages among the evaluated methods. Stage-wise ablations further show that SCCS and VA-RL provide complementary gains, supporting the design of the two-stage training framework. These results position OpenFC as a strong and effective framework for open-search fact-checking. We will open-source our code and release the model checkpoints to support reproducibility.

---


### 423. [IVT-Guard: All-in-One Reasoning Model for AI-Generated Content Detection](https://arxiv.org/abs/2609.33585)

**<font color=#1a73e8>作者：</font>** Hongwei Niu, Yunpeng Luo, Hanjun Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of highly realistic AI-Generated Content (AIGC) necessitates robust and interpretable detection mechanisms. However, existing detectors are predominantly confined to single modalities and provide binary outputs without reasoning. While Multimodal Large Language Models (MLLMs) present a promising solution, their development is constrained by the scarcity of multimodal reasoning data and the reasoning-detection optimization dilemma, where explicit reasoning supervision can compromise detection accuracy. To this end, we introduce IVT-Set, a comprehensive dataset comprising over 152K diverse image, video, and text samples equipped with multi-granularity Chain-of-Thought (CoT) reasoning trajectories. Based on it, we propose IVT-Guard, a pioneering framework for unified and interpretable AIGC detection across image, video, and text modalities. Furthermore, to overcome the aforementioned optimization dilemma, we design a novel three-stage training paradigm: Artifact-Aware Pre-training, Artifact-to-Evidence Supervised Fine-Tuning via artifact-aware injection, and Evidence-Verdict Consistency Group Relative Policy Optimization. Extensive experiments demonstrate that IVT-Guard achieves state-of-the-art detection performance across in-domain, out-of-domain, and cross-dataset settings while delivering faithful reasoning. Code and data will be released.

---


### 424. [Approximating Softmax in Pretrained LLMs: Model Sensitivity and Kernel Acceleration](https://arxiv.org/abs/2609.33586)

**<font color=#1a73e8>作者：</font>** Shangzhen Zhu, Muyan Hu, Tomasz Kozlowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On NVIDIA Blackwell B200, tensor-core throughput outpaces special-function exponential throughput by more than two orders of magnitude, exposing exponential evaluation in fused attention kernels. A pretrained Transformer, however, may not need it evaluated accurately at every element. We characterize what a pretrained model does need by approximating softmax at inference in ten frozen decoder-only models (0.5B-72B). The number of positions the softmax map assigns probability to and within-row resolution can be cut substantially, yet uniform weighting of the same positions is damaging. Where a fixed resolution budget is placed matters as much as its size, with resolution near the row maximum consistently favored. Perturbations matched on scalar distortion produce model-dependent responses of opposite sign. These findings motivate Rowmax-PoT, a coarse logarithmic weight representation anchored at each row maximum, and Rowmax-H15, its hardware specialization in FlashAttention-4. On B200, the patched FP8 attention forward is 12.4% faster at causal 8K and 25.8% faster at non-causal 8K in host-side call-latency measurements; board energy per forward falls by 8.4% at causal 16K. Measured separately on the BF16 kernel path at 2K, Rowmax-H15 increases perplexity by 0.091-0.492% across five models from three families.

---


### 425. [TGRL: Temperature-Grouped Reinforcement Learning for Efficient Exploration in LLMs](https://arxiv.org/abs/2609.33589)

**<font color=#1a73e8>作者：</font>** Zihan Lin, Xiaohan Wang, Jie Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient exploration often remains a central bottleneck in reinforcement learning with verifiable rewards (RLVR). Although temperature control and test-time scaling strategies can increase rollout diversity of large language models (LLMs), they either expand the sample budget at rollout time or leave the benefit of exploration unquantified. To this end, we propose Temperature-Grouped Reinforcement Learning (TGRL), which turns temperature-induced diversity into an explicit training signal. For each prompt, TGRL partitions its rollout group into low- and high-temperature subsets, estimates exploration gain through their reward contrast, and allocates this group-level signal as token-level credit using Jensen--Shannon (JS) divergence between the corresponding temperature-scaled next-token distributions induced by the same logits. Notably, TGRL reaches equivalent accuracy up to 36% faster than strong RLVR baselines without expanding the rollout budget. Across 11 benchmarks from diverse domains, TGRL broadly improves over strong RLVR baselines: it improves the six-benchmark math average by 1.6% at 32B, raises CodeForces rating by 196.7 points and LiveCodeBench Pass@16 by 4.4%, and improves ALFWorld/WebShop success rates by 6.3%/4.9%. Comprehensive ablations and wall-clock analysis confirm the efficacy of all proposed components. Code is available at this https URL.

---


### 426. [JustQuant: You Don't Need Smoothing, SVD, or Rotation for 4-Bit Activation Quantization](https://arxiv.org/abs/2609.33601)

**<font color=#1a73e8>作者：</font>** Kaicheng Yang, Kaisen Yang, Chunyu Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent generative models have become increasingly powerful, but their inference cost continues to grow. Model quantization offers a promising way to compress these models and accelerate inference. However, at 4 bits, activation quantization is substantially more challenging than weight quantization. Recent post-training quantization (PTQ) and quantization-aware training (QAT) methods have made progress in 4-bit activation quantization by introducing smoothing, SVD branches, rotations, mixed precision, or advanced formats such as NVFP4. These additional operators and data types impose demanding requirements on inference engines and hardware, limiting the broad adoption of low-precision models. Can quantization be achieved using only plain low-bit operators? To answer this question, we propose JustQuant, a simple yet effective framework that moves the complexity of low-bit quantization from deployment-time operators into the training process. We first revisit model quantization from the perspective of knowledge distillation and show that a key reason existing PTQ and QAT methods fail is that they typically exploit supervision at only a single level. We then introduce Theseus QAD, a quantization-aware distillation method that progressively applies multi-level supervision, analogous to the gradual replacement process in the Ship of Theseus. Extensive experiments on DiT and diffusion large language models show two distinct regimes. For smaller models, Theseus QAD can serve as a lightweight warm-up stage that substantially improves subsequent QAT with plain operators, while naive QAD may collapse in the same setting. For larger models, Theseus QAD provides a stronger distillation training path than ordinary QAD. Across both regimes, JustQuant improves low-bit quantization quality while avoiding the complex operators required by many existing PTQ methods.

---


### 427. [ViCoR: Reliable Molecular Structure Extraction via Spatially Aligned Verification and Executable Revision](https://arxiv.org/abs/2609.33603)

**<font color=#1a73e8>作者：</font>** Yujian Yuan, Xin Cai, Yufan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable optical chemical structure recognition (OCSR) is essential for building high-quality chemical data from scientific literature, yet even small recognition errors can propagate into chemical databases and downstream models. In practice, recognized structures often require manual inspection and correction before use, making large-scale data curation costly and difficult to scale. We therefore study Selective Structure Recognition (SSR), a post-recognition setting that automatically produces reliable structured outputs while rejecting unresolved cases. Selection-only approaches can improve reliability by rejection, but cannot create additional correct outputs beyond those produced by the base recognizer. We propose ViCoR, a repair-before-rejection framework for iterative VerIfiCatiOn and Revision. Its key idea is to make observation-prediction correspondence explicit: coordinate-preserving rendering establishes spatial correspondence between the source image and predicted structure, while index anchoring maps localized visual discrepancies to executable graph edits without full-structure regeneration. A shared VLM is progressively trained from verification to revision. On two real-world OCSR benchmarks, ViCoR improves overall accuracy from 73.53\% to 88.26\% and from 61.83\% to 84.32\%, while achieving over 97\% accepted accuracy at 85--89\% coverage. The resulting molecular data further improve reaction-extraction F1 by 15.5 points and literature-sourced reaction prediction accuracy by 7.7 and 5.8 points, demonstrating the value of automated reliability control for scientific data curation and downstream chemical learning.

---


### 428. [You Only Edit Once: Incentivizing In-Context Capability of LLMs via Local Demonstration Refinement](https://arxiv.org/abs/2609.33609)

**<font color=#1a73e8>作者：</font>** Jiarong Wen, Qi Wang, Yun Qu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) is crucial for boosting the inference performance of large language models (LLMs). However, the effectiveness of ICL in LLMs is greatly influenced by the choice of demonstration sets. Exhaustive searches over these sets are combinatorial, and existing selectors often rely on relevance or likelihood proxies to implicitly assess ICL quality. Making repeated queries to the target LLM with these strategies can incur substantial costs. This work simplifies selection by framing it as a constrained local search problem and presents local demonstration editing (LDE). Starting with an initially retrieved set of demonstrations, LDE employs a single structured edit to explore its surrounding neighborhood while balancing performance gains with search costs. Technically, LDE is reduced to a policy search problem, for which we train a small LLM, referred to as Jev-LDE. This model as the System-1 modifies the retrieved demonstration set by performing actions such as \texttt{Keep}, \texttt{Delete}, or \texttt{Replace} elements, all within a framework of reinforcement learning with verifiable rewards. At test time, Jev-LDE executes a single edit of the retrieved demonstration set, followed by one inference from the target LLM, avoiding the need for iterative context scoring or subset searches. Across standard classification benchmarks, various target LLMs with Jev-LDE as the plug-and-play module consistently improve ICL performance, and Jev-LDE shows transferability to held-out benchmarks and models without retraining. These findings indicate that the LDE approach offers an efficient and adaptable method for harnessing the ICL capabilities of target LLMs.

---


### 429. [Quizzing the Translation: A Prover-Grounded Evaluation Metric for NL$\rightarrow$FOL](https://arxiv.org/abs/2609.33612)

**<font color=#1a73e8>作者：</font>** Pu Suo, Ali Emami  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A standard pipeline for symbolic reasoning over natural-language problems translates them into first-order logic and invokes a theorem prover. The translation step is the bottleneck: swap "every" for "some" and every inference that follows is corrupted. Yet today's metrics often score more broken translations higher than less broken ones, because BLEU, BERTScore, and Smatch++ reward surface overlap that the worst errors happen to preserve. We introduce SIV, which derives two kinds of probes from the target formula and uses a theorem prover to verify the candidate translation against each. Positive probes are statements the candidate must entail, which detect translations that drop content; contrastive probes are statements the candidate must not entail, which detect translations that assert more than the original. On a controlled pool of perturbed FOLIO translations, the severity of the error accounts for 80% of SIV's score variance, compared with at most 17% for any prior metric. Across six error classes on a disjoint pool, SIV scores the reference above the perturbed candidate in over 99% of pairs. Because each probe is labeled with what it tests, the failure pattern also supplies a labeled error trace, recovering the perturbation class at macro-F1 0.638, nearly double the score-only baseline. On 434 expert-audited real LLM translations, SIV attains the top AUC, uniquely detects and grades expert-labeled major errors, and abstains, rather than mis-scoring, on out-of-vocabulary translations.

---


### 430. [EAT: Expert Account Tracker for Efficient MoE Inference](https://arxiv.org/abs/2609.33614)

**<font color=#1a73e8>作者：</font>** Yuexian Li, Yifei Yang, Zouying Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models have emerged as a revolutionary method to scale Transformer models. However, traditional MoE architecture still suffers from inefficiency since a large number of experts are unnecessarily activated. Existing approaches for reducing the number of activated experts often overlook the historical performance of each expert. In this paper, we propose EAT, a novel method called Expert Account Tracker (EAT), which utilizes history-awareness metrics and adaptive thresholding to dynamically select the most important experts, thereby reducing the activated expert number while effectively maintaining the model performance. Experiments show that EAT outperforms the existing baseline Top-P method across multiple models and datasets, achieving over 25% an average reduction compared to the vanilla method in the number of activated experts and performing better token generation speed compared to the baseline. Furthermore, the performance of pruned models can be efficiently recovered via OPD using only 9K data. Additionally, through ablation studies, we find that excessively reducing the number of activated experts can significantly harm model performance, and the importance of experts varies across layers, with higher-level experts being generally more critical.

---


### 431. [SpatialSpeak: QA-Native Reconstruction with Local and Global Context for Spatial Chain-of-Thought Reasoning](https://arxiv.org/abs/2609.33616)

**<font color=#1a73e8>作者：</font>** Yang Cao, Jiaxin Zhang, Dave Zhenyu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can benefit from geometric priors for multi-view spatial reasoning, yet answer-only training does not directly supervise the intermediate geometric estimates and their use in deriving quantitative spatial answers. We hypothesize that spatial chain-of-thought (CoT) supervision becomes more effective when the VLM first jointly learns complementary local geometry and global scene context through multi-view reconstruction. We introduce SpatialSpeak, a two-stage framework that connects QA-native reconstruction pretraining with spatial CoT learning. In Stage I, QA-Native Reconstruction Pretraining (QA-RP) combines marked-point 3D queries for fine-grained local geometry with object-center queries for global scene context across views. Both tasks are formulated as text-based question answering, allowing geometric estimation and subsequent reasoning to share the same autoregressive output interface. In Stage II, spatial CoT with Visual Compensation (CoT-VC) trains the model to express question-relevant geometric estimates and use them to derive answers, with reliability assessment and visual compensation supporting answer refinement when needed. On ReVSI, QA-RP increases the gain from CoT-VC from 2.6 to 6.9 points, and ablations show that both local and global reconstruction supervision are beneficial. SpatialSpeak achieves state-of-the-art results on ReVSI, VSI-Bench, and SPAR-Bench, with a ReVSI score of 62.8 that exceeds the strongest compared baseline by 8.7 points.

---


### 432. [ParaAgent: Reinforcing Parallel Acting in Open-World Tool Environments](https://arxiv.org/abs/2609.33618)

**<font color=#1a73e8>作者：</font>** Shengbin Yue, Hongru Wang, Siyuan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language model agents are increasingly deployed in open-world tool environments, which require balancing exploring unknown capabilities and exploiting known ones. Existing methods face a performance-efficiency tradeoff: they either rigidly decouple exploration and execution or interleave them without coordination. We argue that the key lies not in whether to decouple or interleave them, but in how to coordinate them across granularities. We introduce ParaAct, a structured parallel-action loop that combines phase-level Exploration $\rightleftharpoons$ Execution with action-level parallelism. To learn this loop, ParaAgent combines multi-agent cold-start demonstrations with reinforcement learning under multi-level advantage decoupling, making planning structure explicit and supervising it with step-, phase-, and trajectory-level rewards. Learning is supported by our ToolEnv, a scalable simulator grounded in 50,011 realistic tool interfaces. On two open-world tool benchmarks, ParaAgent-4B achieves the best average success among all baselines, including GPT-4.1 systems, with the largest gains on multi-tool tasks. Behavioral analyses show that these gains stem from this action organization, highlighting its importance for capable and efficient open-world agents.

---


### 433. [Learning Dynamics of Continual Learning: A Unified View of Data Attribution, Forgetting, and Plasticity Loss](https://arxiv.org/abs/2609.33620)

**<font color=#1a73e8>作者：</font>** Yi Ren, Wenlong Deng, Guanzhe Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern language models are likely to be updated throughout their lifetime rather than trained once and frozen. Each update therefore participates in a recurring cycle: decide which experience to learn from, understand what that update changes, and remain capable of learning from what comes next. We show that these challenges are governed by the same evolving update--behavior interaction. We derive a token- and layer-wise decomposition of how learning from one token changes another prediction. By separating the softmax force, shared readout geometry, and residual connections, it exposes two interaction channels and yields a forward-computable approximation. Following this interaction through time reveals a unified picture of continual adaptation. Positive interaction identifies useful experience; negative interaction produces either concentrated collision or accumulated erosion; over longer horizons, updates reshape the shared geometry mediating future learning signals, reducing their transmission. These predictions lead to effective data selection, mechanism-specific controls for interference, and a readout-based diagnostic of future learnability whose degradation predicts the benefit of restoring the readout. Across models and training regimes, the same local interaction thus explains both what an update changes now and how learning today changes what can be learned tomorrow. This view connects data attribution, forgetting, and plasticity loss as distinct regimes of the same evolving learning dynamics.

---


### 434. [Characterizing Memory Misalignment in Human-LLM Interaction From User Perspectives](https://arxiv.org/abs/2609.33623)

**<font color=#1a73e8>作者：</font>** Jingruo Chen, Shuning Zhang, Eryue Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While memory enhances personalization in LLM-based conversational agents, it suffers from memory misalignment, where memories violate user expectations. We present a mixed-methods investigation to characterize and mitigate memory misalignment from user perspectives. First, we collected data from memory usage (N=28, 457 entries) and diary study (N=32, 304 reports), which yielded a taxonomy spanning 14 misalignment types across memory intake, storage and management, retrieval and interpretation stages. Second, four co-design workshops with 12 experienced HCI researchers derived a design space to tackle memory misalignment issues, consisting of 12 candidate interaction strategies structured across interaction form, placement and intrusiveness dimensions. Finally, a speed dating with 121 users reveals preference heterogeneity, where users prioritize proactive controls over cognitively demanding causal graph inspections or passive audit logs. Synthesizing these findings, we highlight the tension between supervisory agency and interaction overhead, and advocate for friction-aware memories that balance user oversight with conversation smoothness.

---


### 435. [Quantifying Behavioral Tails in Black-Box Language Models](https://arxiv.org/abs/2609.33638)

**<font color=#1a73e8>作者：</font>** Elsayed Eshra, Ali Al-Lawati, Dongwon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce RareTrap, a framework for estimating the probability of severe behaviors in black box large language models (LLMs). A key challenge for probability estimation is defining a tractable distribution over the input space. To accomplish that, RareTrap uses a surrogate LLM and constructs a geometry-aware mapping from a lower-dimensional latent reference space into its token-embedding space to induce an explicit and reproducible distribution over input prompts. A response-level performance function is utilized on the response to quantify behavior severity. This enables sequential rare event simulation that concentrates evaluations on progressively more severe behaviors while preserving probability under the induced prompt distribution, which would otherwise be prohibitive to measure. Across 10 open-weight and two frontier models (GPT-5.4 and Claude Sonnet 4.6), we find that RareTrap successfully induces severe resource consumption behaviors and computes their probability with as few as 200 evaluations. RareTrap provides model developers a principled approach for evaluating language models under a common distribution, and prioritizing alignment effort to improve safety and mitigate risks. Code is published online: this https URL.

---


### 436. [Trajectory Unlearning on LLM-based Agents](https://arxiv.org/abs/2609.33639)

**<font color=#1a73e8>作者：</font>** Yingdan Shi, Ren Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing large language model (LLM) unlearning has focused primarily on removing specific knowledge, such as harmful facts, private data, or copyrighted content. However, as LLMs are increasingly deployed as autonomous agents, a fundamental yet overlooked problem emerges: beyond suppressing what an agent knows, an agent should not reproduce undesired behaviors through its action trajectories. In this work, we introduce trajectory-level unlearning, a new problem formulation that targets the removal of specific action trajectories in long-horizon agentic tasks, rather than factual knowledge. We identify two fundamental challenges that distinguish trajectory unlearning from knowledge unlearning: (1) our unlearning target is what the agent \emph{does}, not what it \emph{says}; and (2) trajectories are sequentially dependent action sequences that cannot be decomposed into isolated prompt-response pairs without losing inter-step structure. To address these challenges, we propose Group-injected Relative Policy Optimization (GiRPO), which injects forget trajectories into the policy rollout group with penalized rewards and isolates the normalization statistics, yielding a stable and bounded unlearning signal that does not corrupt gradient updates for normal task trajectories. We construct trajectory unlearning benchmarks from two application scenarios, household tasks (ALFWorld) and online shopping (WebShop), and design three complementary metrics for evaluating forgetting quality and model utility. Experiments on ALFWorld and WebShop demonstrate that GiRPO effectively unlearns target trajectories while preserving task success rates, outperforming existing knowledge-unlearning baselines on both forgetting quality and task utility.

---


### 437. [Learning to Learn from Context: Synthetic Training from Perturbed Public Documents](https://arxiv.org/abs/2609.33642)

**<font color=#1a73e8>作者：</font>** Haoyi Wu, Yang Xiao, Yusong Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world tasks often require large language models (LLMs) to learn from complex task-specific context rather than pretrained parametric knowledge. This capability remains a weakness of LLMs, while human annotation for such task contexts is expensive and difficult to scale. Public high-quality documents are an abundant alternative, but much of the public web has already been consumed during pretraining: training on such documents naively would reward memorization rather than context learning. In this work, we attempt to make use of high-quality public documents with small perturbations and empirically find that LLMs can successfully generate context-dependent reasoning traces and answers, which are then used to train a student model. Specifically, we construct a synthesis pipeline that (i) rewrites source documents to reduce memorization risk, (ii) generates questions and rubrics that require reasoning over the document, (iii) answers the questions with the document as context, and (iv) admits only samples that genuinely depend on the document. Without any human annotators, our pipeline generates about 10k samples from 3.5k documents, and the resulting student model substantially improves the performance on CL-bench. SFT raises a Qwen3.6-35B-A3B student from 13.7% to 22.8%, and a subsequent rubric-reward RL stage reaches 24.6%, on CL-bench comparable with a frontier model of over a trillion parameters, Qwen3.8-2.4T (23.9%). We also observe a broad transfer of improvements to long-context understanding, instruction following, and reasoning, while code generation and knowledge remain mostly flat. We hope this work provides a reproducible and scalable way to improve the ability of LLMs to learn from context, and to facilitate further research on context-grounded reasoning.

---


### 438. [Probe to Act: Elevating Browser-Use Agent via Active Visual Probing](https://arxiv.org/abs/2609.33646)

**<font color=#1a73e8>作者：</font>** Keliang Li, Heng Wang, Chen Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Browser-use agents require seamless alignment between structured web metadata and visual information, while preserving relevant context across long interactions. Existing interfaces often rely on either screenshot-level action prediction or static Set-of-Marks overlays, leaving the model to resolve dense DOM-pixel alignment before every operation. We introduce Probe to Act (P2A), an active probing framework for the browser-agent loop that moves this alignment into decision time. P2A addresses an asymmetric bridge between symbolic DOM hypotheses and screenshot layout by rendering on-demand symbolic DOM structure back into pixels. Before committing a state-changing browser operation, the agent can issue lightweight probes to translate DOM handles into pixel evidence, map screen regions back to DOM candidates, register visual-only targets, and commit verified notes. These interleaved processes naturally produce evidence-based memory: only probed, acted-on, or explicitly committed observations are kept across steps, preserving only decision-critical evidence in long-horizon contexts. P2A can be used as a prompting strategy for proprietary models under the standard DOM+SoM interface, and can be distilled into open-weight models through cold-start synthesis and self-bootstrapped SFT. Across three browser-use benchmarks, P2A shows clear gains on task success rate for both proprietary and fine-tuned models; on VisualWebArena, for example, it improves Gemini-3-Pro from 54.1% to 61.2% and Qwen3-VL-8B from 24.6% to 32.9%, while matching the costly full-observation history ($\sim$3$\times$) at only $\sim$1.2$\times$ the peak retained input context of action-only history.

---


### 439. [AgentBoundary: Counterfactual Evaluation of Safety in Tool-Using LLM Agents](https://arxiv.org/abs/2609.33658)

**<font color=#1a73e8>作者：</font>** Tianzhuo Yang, Zirui Mi, Yantao Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment for large language models (LLMs) in conversational settings is largely framed around whether to answer or refuse a request. In agentic settings, however, the same models must decide whether to act as permission-critical evidence emerges during execution. This creates a distinct challenge: apparent risk, action permissibility, and task competence are easily confounded, making agentic over-refusal difficult to distinguish from ordinary task failure. To address this, we introduce AgentBound, the first four-way counterfactual generation-and-evaluation framework for tool-using agent safety. AgentBound transforms the same executable workflow by independently varying apparent risk and action permissibility, enabling controlled comparisons of risky-looking but authorized tasks and routine-looking but unauthorized tasks. These comparisons jointly diagnose over-refusal and unsafe compliance while controlling for task competence. We instantiate AgentBound as a human-validated 4,000-task evaluation suite with trajectory-based and post-state-based judgments. Across 17 model and harness configurations, high safety frequently coexists with poor authorized-task completion: GPT-5.5 blocks 99.5\% of routine-looking unauthorized actions yet completes only 28.7\% of risky-looking authorized tasks. We further train a lightweight runtime calibration module that improves authorized-task completion by 18.2\% on average across 10 evaluated configurations, while improving unsafe-action blocking by 5.4\% on average. These show that effective agentic alignment requires action decisions to track permission-relevant execution evidence, rather than refusal strength alone.

---


### 440. [Learning Multimodal Embeddings with Evidence-Aligned Readout](https://arxiv.org/abs/2609.33659)

**<font color=#1a73e8>作者：</font>** Zirong Chen, Fuda Ye, Enjun Du 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models can expose task-relevant evidence through generation, but producing useful evidence does not by itself determine how it enters a retrieval embedding. We study whether the semantic organization of that evidence can also specify where representations are read. To address this question, we introduce EviAlign, which couples Semantic Evidence Generation with Boundary Readout in a shared multimodal large language model. It organizes evidence into five semantic units, reads the contextualized state at each unit boundary, and aggregates these states into a single normalized embedding. Generation and contrastive retrieval objectives jointly train this shared structure. With the same trailing readout, semantic evidence and free-form CoT yield nearly identical retrieval performance, suggesting that evidence organization alone does not explain the full gain. A controlled $2\times3$ study compares consistent and permuted evidence organization across three readout strategies, using training targets with matched evidence spans. With five readout states and the same mean pooling, the advantage of consistent semantic organization grows from 0.65 points at length-based training positions to 2.39 at evidence boundaries, yielding a 1.74-point co-design interaction. Across 12 MMEB retrieval tasks, EviAlign achieves 76.9 average Recall@1 with 500K training pairs while retaining single-vector indexing and scoring.

---


### 441. [Audit-First VAPO: Risk-Certified Selective Updates under Imperfect Verification](https://arxiv.org/abs/2609.33662)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Xiaobo Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Imperfect verifiers can assign a harmful update direction even when clipping and regularization bound its magnitude. We introduce Audit-First VAPO, which separates discrete directional admission from continuous magnitude control. An observation-only accept-appeal-abstain policy uses a finite secondary-verification budget; its action trace is frozen before clean labels are joined. Simultaneous finite-sample bounds then certify selected harmful risk, coverage, and verifier-call rate over a predeclared policy family. Conditional Hoeffding-Azuma bounds account for the dependence induced by shared budgets, and rollout or verifier changes initiate a new certification stage. After admission, a bounded trust-clip-KL actuator controls magnitude. We evaluate two models on two reasoning benchmarks against static RLVR, matched-random selection, confidence thresholding, noise correction, and verifier augmentation. On Qwen3.5-0.8B and GSM8K at target risk $\rho=0.08$, RC-VAPO achieves 74.1% accuracy, selected harmful risk 0.0697, coverage 0.4125, and relative verifier cost $1.16\times$. At matched coverage and update magnitude, its selected-risk difference from matched random is -0.0260 with paired 95% interval $[-0.0364,-0.0157]$. Across asymmetric, confidence-dependent, and correlated-verifier noise, the certificate is satisfied on 57 of 60 independent runs. These comparisons isolate informative directional selection from proposal suppression, update shrinkage, and additional verifier computation.

---


### 442. [CompoWorld: Compositional Environment Scaling for General Agents](https://arxiv.org/abs/2609.33665)

**<font color=#1a73e8>作者：</font>** Xiao-Wen Yang, Weiyi Xu, Wen Da 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatically generated environments provide a scalable source of interaction data for training general agents. However, existing approaches mainly generate tasks within a single environment, while real-world workflows require agents to connect information and actions across multiple services. We introduce Compositional Environment Scaling (\textbf{CompoWorld}), which expands the task space by composing a finite library of reusable services. Coding agents turn tool specifications into verified services with typed states and shared interfaces, while a world model handles tools that cannot be reliably implemented. A random-walk procedure connects services through dependency graphs, enabling the generation and verification of tasks that require information to flow across services. Verified trajectories support supervised fine-tuning (SFT), while our Completion-Focused Rubric Reward guides reinforcement learning (RL) toward full task completion by emphasizing criteria with lower pass rates within each rollout group. We construct 448 services exposing 10,130 tools and use 3K SFT trajectories and 1K RL tasks to train Qwen3.6-35B-A3B. Experimental results show that CompoWorld improves on its backbone by 9.17 points on average across eight benchmarks. On AutomationBench, it surpasses frontier models such as Claude Opus 4.6 and leads all compared agent-specialized 35B-A3B models.

---


### 443. [One Model Is Not a Crowd: Multi-LLM and Aspect-Conditioned Diverse Comment Generation](https://arxiv.org/abs/2609.33666)

**<font color=#1a73e8>作者：</font>** Nafis Irtiza Tripto, Delvin Ce Zhang, Mahjabin Nahar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human communication on the internet is shaped by diverse perspectives, most visibly expressed in online comment spaces. As large language model (LLM)based AI agents begin to inhabit these spaces, a key question arises: whether synthetic comment threads can capture the diversity inherent in human discourse. This concern is increasingly important, as the growing presence of homogenized AI-generated content risks reducing diversity over time, potentially leading to model collapse and degrading the richness of digital communication. Inspired by the plurality of human crowds and the aspect-driven nature of discourse, we hypothesize that comment diversity is better approximated by combining multiple LLMs with aspect-conditioned generation. We formalize and evaluate this approach using models from different providers and introduce a framework that characterizes diversity across semantic, linguistic, and socio-pragmatic features along three axes: dispersion, coverage, and alignment. Using this framework, we conduct a large-scale study on over 2 million YouTube comments across multiple domains. Our results reveal that multi-LLM and aspect-conditioned generation better align with human comment distributions and such data remains viable under pretraining style curation and is effective for downstream tasks. Yet, human diversity remains unmatched. Overall, our findings provide a practical foundation for generating more diverse and socially grounded discourse in AI-mediated environments.

---


### 444. [Scalable Attribution and Control of Model Behavior During Training](https://arxiv.org/abs/2609.33667)

**<font color=#1a73e8>作者：</font>** Sleem Abdelghafar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attributing and controlling model behavior during training requires identifying each example's contribution quickly enough to act before the next update. However, examples in the same training batch can produce similar behavioral changes, making their individual contributions difficult to distinguish. We address this ambiguity through mutual information, accounting for interference within the batch by quantifying how much the combined behavioral change reveals about each example's contribution. We show that this mutual information is a logarithmic function of Behavioral Gradient Uniqueness (BGU). BGU gives the information measure its geometric interpretation. Our Batch-Space Ghost (BS-Ghost) algorithm makes these scores practical inside the training loop through shared computation in batch space, without storing model-sized example gradients. On a complete 1,000-example Qwen2.5-7B-Instruct workload, our BS-Ghost implementation adds 27 seconds (8.0%) to 5.5 minutes of ordinary training. Removal and retraining demonstrate that BGU identifies data that causally shapes final behavior. At each training step, signed information identifies which examples strengthen or weaken the target behavior, explaining how behavior develops during training. Signed information also enables cheap intervention during training: it predicts how changing example weights will affect behavior in the next update. We then use these predictions to choose weights that steer behavior toward a desired target. This makes our framework a practical foundation for scalable oversight and verification of training pipelines and processes, helping evaluators assess model alignment, understand how it develops during training, and guide interventions that shape ongoing learning.

---


### 445. [Closing the Cross-Dialect Gap: Query Plans as a Portable Interface in Text-to-SQL](https://arxiv.org/abs/2609.33670)

**<font color=#1a73e8>作者：</font>** Corentin Royer, Robin Oester, Yotam Perlitz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems are typically trained and evaluated on a single dialect (SQLite), yet production deployments span PostgreSQL, MySQL, ClickHouse, and beyond. We show that this single-dialect assumption leads to a substantial drop in cross-dialect accuracy for every model we tested. The drop persists across scale, architecture, and even purpose-built text-to-SQL systems. We argue that the fix is to change the generation target: instead of asking an LLM to emit dialect-specific SQL, we have it emit a dialect-agnostic relational algebra query plan, which a deterministic compiler then renders into SQL for any supported backend. Across thirteen models from 3B to frontier scale, this restores cross-dialect portability nearly uniformly, at a small cost in peak accuracy on the model's home dialect for capable prompted models and none once fine-tuned on plans; under matched fine-tuning, plan supervision yields a stronger model than SQL supervision. We also introduce MetricName, a question-aware result-set comparator needed to evaluate fairly across dialects, where existing metrics confound semantic errors with benign cross-dialect variation. More broadly, the result is a reminder that a generation target chosen for execution is not necessarily the one that maximizes generation quality.

---


### 446. [Reset Is Not Recovery: Evaluating Recoverability from False Conversational Context via Sycophancy Hysteresis](https://arxiv.org/abs/2609.33672)

**<font color=#1a73e8>作者：</font>** Adi Shnaidman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grounded language models are usually evaluated by adding relevant context, but multiturn dialogue also contains unsupported user claims that may contaminate later factual answers. We study post-pressure recoverability: whether a model returns to clean-context behavior after a user repeatedly advocates a wrong answer and then withdraws that pressure. We introduce a recovery-after-pressure protocol for multiple-choice factual dialogue and measure sycophancy hysteresis, the residual probability assigned to the user-advocated wrong answer relative to a clean-context counterfactual. Across seven instruction-tuned open-weight models and two factual benchmarks, ordinary reset often reduces but does not erase pressure-induced bias. History preserving repairs such as user retraction, system reset, and self-verification recover only 2-3/14 model-dataset pairs under the strict clean-restoration diagnostic, whereas operations that change the effective context are substantially more reliable; the two conditions that remove the pressure-bearing history entirely, fresh-context deletion and context truncation, recover 14/14. In an oracle trusted-evidence condition across fourteen model-dataset pairs, preserving the pressure-bearing history while adding benchmark-derived trusted evidence increases accuracy from 0.368 to 0.929, while wrong-answer following falls from 41.2% to 4.3%. Controls show that the effect is not explained by dialogue length, repeated confidence, plausible distractors, mere false-answer mention, or option-label inertia. These results suggest that faithful grounded dialogue requires evaluating which prior context should be treated as evidence and which should be removed or quarantined before answering.

---


### 447. [Auditing Agent Actions through Query-Conditioned Attribution](https://arxiv.org/abs/2609.33676)

**<font color=#1a73e8>作者：</font>** Yifan Liu, Praveen Venkateswaran, Abdulhamid Adebayo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly take consequential actions through interactions with users, policies, and external tools. Auditing these agents requires automated attribution of realized actions to their historical basis. However, existing attribution formulations do not provide question-specific traces for diverse auditing objectives. Additionally, when access to the acting model is limited (e.g., in API-only deployments), applicable methods commonly rely on costly input perturbations or external LLM analysis of complete trajectories. We therefore formulate $\textit{query-conditioned agent action attribution}, a new task that takes a natural-language auditing query as input and recovers the source and ordered intermediate evidence for the query-specified aspect of an action. We instantiate this task with $A^3Bench$, a benchmark comprising 1,396 auditing queries across policy basis, parameter provenance, failure propagation, and unsafe-behavior tracing. To enable efficient, query-specific attribution, we use small open-weight models as attribution proposers that combine query-conditioned gradient saliency with query-semantic relevance to rank history units. Our proposer consistently achieves stronger source and evidence rankings at lower inference cost than open-weight baselines, improving source MRR by up to 40.9\% and evidence MAP by 42.1\% with only two forward passes and one backward pass. Controlled evaluations confirm that our proposer improves attribution specificity by adapting its rankings to fine-grained changes in the auditing query. Building on a proposer ensemble, our end-to-end system surpasses the strongest frontier-model baseline in source accuracy (64.5\% vs.\ 60.4\%) while reducing empirical deployment latency by 29.9\% relative to the fastest frontier API baseline. Code and data will be released after the initial review period following final validation and cleanup.

---


### 448. [SWE-Game: Can Coding Agents Build the Games We Want?](https://arxiv.org/abs/2609.33678)

**<font color=#1a73e8>作者：</font>** Xiaoyu Chen, Lai Wei, Jin Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce SWE-Game, a benchmark of 247 tasks grounded in 41 executable reference Godot games spanning 13 gameplay categories in 2D and 3D. Five task types cover development from a brief, implementation from a game design document, skeleton completion, repair of 83 injected-fault cases, and Godot-to-Unity porting. Reference materials specify the intended gameplay, while a shared instrumentation interface lets evaluator-owned drivers and probes execute actions and observe independently implemented games. Evaluation combines engine-state checks, certified reference-input replay, and agent-authored feature demonstrations to assess mechanic correctness, demonstrated playability, and behavioral restoration and preservation after repairs. Game-specific vision-language rubrics separately assess presentation. Across six models, Opus5 achieves the highest overall score in all five task types. Best overall scores remain below 60 out of 100 across the three construction tasks, with Brief-to-Game reaching 50.38. Analysis of reviewed submissions identifies requirement omissions and gameplay logic errors as predominant implementation problems. On human-labeled behaviors from 100 agent-built games, executable checks achieve 92.59% balanced accuracy, compared with 78.41% for a video-based VLM judge. Rubric-based visual scores reach a Spearman correlation of 0.829 with human ratings of 200 gameplay clips. Together, these results characterize current agent capabilities across game-development activities and support combining runtime evidence with visual assessment.

---


### 449. [MAD-Guard: Controlled Study of Autoregressive Generation versus Direct Decision Interfaces for Closed Multimodal Forensic Tasks](https://arxiv.org/abs/2609.33683)

**<font color=#1a73e8>作者：</font>** Hao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When should multimodal foundation models generate tokens, and when should they directly output a decision? We present MAD-Guard, a controlled study of output-decision interfaces for closed multimodal forensic tasks. Once a multimodal representation is computed, is autoregressive generation necessary for closed forensic decisions with high input complexity but low output entropy? Under a matched Qwen3-VL-8B backbone, 2,400 FakeClue training samples, and LoRA budget ($r=16, \alpha=32$) on Huawei Ascend 910C NPUs, we evaluate a progression of decision interfaces (AR-SFT [generate] $\to$ Logit Slice $\to$ Binary Direct Head $\to$ +choice $\to$ +act $\to$ CLM-Head) and decompose latency into backbone representation (53.12 ms), 151,643-way vocabulary projection (+85.04 ms $\to$ 138.16 ms), and decoding (+248.26 ms $\to$ 386.42 ms). Under 1-to-1 binary supervision ($\mathcal{L}_{\mathrm{BCE}}$), a Binary Direct Head cuts latency by $2.60\times$-$7.27\times$ (53.12 ms) and lowers calibration error by $1.88\times$ (ECE = 0.0450 vs. 0.0845), with a -1.80% accuracy trade-off (93.10% vs. 94.90%; 0.9795 vs. 0.9871 ROC-AUC) from forfeiting token priors. Gains above AR-SFT arise either from multi-task attribution and uncertainty gating (+choice+act: 96.44% accuracy, 0.9940 ROC-AUC, 0.0187 ECE at 53.71 ms) or from a disaggregated contrastive head (CLM-Head: 96.55% binary and 96.44% multi-task accuracy, 0.0166 ECE, 98.79% 7-class attribution at 54.42 ms) retaining semantic priors without token decoding. Across 5,000 out-of-sample images from five benchmarks, our framework excels on synthetic, camouflage, and document forgeries (96.44% GenImage, 97.73% Chameleon, 91.84% Doc) while showing a clear boundary on compressed face manipulation (FF++ ROC-AUC = 0.5913).

---


### 450. [When Do Agents Help? Embedding, LLM and Agentic Alignment of Classical Texts and Their Translations](https://arxiv.org/abs/2609.33691)

**<font color=#1a73e8>作者：</font>** Máté Metzger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Classical texts aligned with their translations support machine translation, retrieval and computational research, but evidence comparing alignment workflows is scattered. This study compares seven systems on 452 texts in Pali, Sanskrit, Mishnaic Hebrew and Tibetan, comprising 9,833 human-aligned units: four embedding pipelines, a direct LLM call, an autonomous agent, and the agent revised by an independent auditor. Generative workflows recover 93-94% of reference correspondences, against at most 77% for embeddings. A ceiling analysis shows that sentence boundaries make some references unrepresentable by the embedding pipelines. Reference recovery is similar across generative workflows: the agent's advantage is 0.5 percentage points (95% CI -0.02 to 1.17), and auditing adds no established benefit. Agents nevertheless produce structurally valid output for all 452 texts, against 437 for direct calls. A blinded three-LLM panel assesses every generative mismatch against the source and human reference. Most mismatches are labelled defensible editorial variation; consensus major-error labels cover only 0.06-0.14% of units. The panel labels significantly fewer residual defects for agents than direct calls (0.7% versus 1.4%), suggesting that reference recovery alone understates alignment quality. On ten long Pali discourses taken as published online, agents and audited agents raise recovery from the direct call's 71% to 84% and 92%. Identical reference-located chunks bring all three to 93%. Agents thus improve structural reliability and reduce judged defects on short passages, while their large recovery advantage on long documents disappears after chunking. In this setting, independent auditing offers little measurable additional benefit on prepared passages.

---


> [!TIP]
> 当前位于：**401-450**（第 9/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

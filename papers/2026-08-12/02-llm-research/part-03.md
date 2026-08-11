# 🧠 大模型相关研究 | 2026年08月12日

> 本类共 **438** 篇论文：已确认 **404** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 101. [KGCache: Amortized Subgraph Retrieval for KG Reasoning with LLMs](https://arxiv.org/abs/2608.07954)

**<font color=#1a73e8>作者：</font>** Uros Stanic, Changcheng Yuan, Sabuj Laskar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can answer knowledge-intensive questions more reliably when they are grounded with knowledge graphs, but systems such as Think-on-Graph and Reasoning-on-Graph repeatedly query the same graph neighborhoods across different questions. In this work, we study this repeated retrieval in Knowledge Graph Question Answering~(KGQA) workloads and propose KGCache, an in-memory cache for one-hop knowledge graph neighborhoods. KGCache is designed to be compatible with both iterative traversal (ToG) and one shot planning (RoG) KGQA paradigms. KGCache is placed between the KGQA engine and the backend serving the KG, so repeated entity requests can be served from cache instead of issuing new KG queries. We evaluate KGCache on WebQSP and CWQ using LRU, LFU, and a trace-aware Oracle policy. Our analysis shows that both datasets contain substantial entity reuse among starting entities and entities reached during traversal. We also explore semantic caching for similar queries, which shows additional hit-rate gains on WebQSP and needs further accuracy testing on CWQ. Entity caching accelerates KG retrieval by up to $1.91\times$, while semantic-context caching achieves up to $1.06\times$ full-system speedup in the evaluated WebQSP configurations, with each hit being up to $3.73\times$ faster.

---


### 102. [Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning](https://arxiv.org/abs/2608.07955)

**<font color=#1a73e8>作者：</font>** Shi-Yu Tian, Zhuo-Xia Wang, Xuan-Yi Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large vision-language models have achieved strong performance in multimodal reasoning, but they remain unreliable on fine-grained spatial tasks that demand both precise spatial perception and fine-grained geometric computation beyond end-to-end generation. Tool augmentation offers a natural solution, while existing methods either plan tool calls from scratch without explicit dependency constraints or rely on fixed pipelines that are redundant and generalize poorly across spatial tasks. An effective spatial reasoning agent should instead accumulate reusable experience and adaptively compose it for new problems. To this end, we propose NeSy-Spatial, a neuro-symbolic framework for self-evolving spatial skills. NeSy-Spatial abstracts tool interactions and geometric operations into typed executable atomic instructions and composes them into two complementary skill types: Tool-Use Skills for organizing tool execution and Geometry Skills for structured geometric reasoning. During inference, NeSy-Spatial retrieves and executes relevant skills in a closed-loop process. During evolution, it analyzes buffered successful and failed trajectories to refine skill structures and prune unreliable or inactive entries. Experiments on three spatial reasoning benchmarks show that NeSy-Spatial consistently improves reasoning accuracy with more precise tool utilization.

---


### 103. [SCOUT: Self-Checking and Recovery-Aware Tool-Thought Agents for Ultra-Long Egocentric Video Reasoning](https://arxiv.org/abs/2608.07959)

**<font color=#1a73e8>作者：</font>** Keyang Zhong, Kuo Wang, Peng Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ultra-long egocentric video understanding requires reasoning over temporally sparse evidence distributed across hours or days, challenging current multimodal models with limited context and the grounding of key video segments. While Chain-of-Tool-Thought (CoTT) agent systems enable iterative retrieval and inspection, they suffer from error propagation due to rigid zoom-in strategies that lack recovery mechanisms. In this work, we address these challenges through SCOUT (Self-Checking Chain-Of-Tool-thought), a recovery-aware agentic framework introducing an adaptive policy that evaluates intermediate tool observations and dynamically trades off exploitation (zoom-in) and exploration (region switching), enabling robust multi-hop reasoning over extremely long horizons. However, training such multi-turn tool-using agents remains challenging, as existing RL methods rely on sparse outcome-level rewards and lack supervision over extended decision trajectories, resulting in suboptimal credit assignment for long-horizon reasoning. To address this, we develop UPS-GRPO, an uncertainty-prioritized policy optimization method that concentrates exploration on high-uncertainty post-tool states while preserving sample efficiency. We further introduce a turn-level advantage decomposition that integrates outcome rewards with tool-grounded temporal alignment rewards for improved credit assignment. Experiments show that SCOUT achieves state-of-the-art results on ultra-long egocentric benchmarks, while remaining competitive on shorter-horizon long-video settings.

---


### 104. [EasyBalance: Cross-Layer Load Balancing in Distributed MoE Inference](https://arxiv.org/abs/2608.07964)

**<font color=#1a73e8>作者：</font>** Yize Wu, Ke Gao, Ling Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Load Balancing has emerged as a critical problem in expert-parallel distributed inference of Mixture-of-Experts (MoE) models. As routing distributions are typically skewed across experts, devices hosting lighter-loaded experts must idle to wait for the heaviest during expert computing, leading to inefficiency. Existing load-balancing approaches primarily rely on expert replication or migration within each layer, which introduce additional overhead and limit their flexibility and scalability. To address this problem, we propose EasyBalance, a cross-layer load balancing strategy that requires no modifications to the expert-device mapping, enabling instant adaptability and incurring essentially no additional overhead. Our key insights are that (1) experts of other layers can be viewed as naturally redundant for the current layer, and (2) cross-layer MoE workloads can be jointly executed to mitigate their individual imbalance. Based on these observations, EasyBalance greedily schedules a subset of cross-layer workloads to run at each MoE step and defers the remaining workloads for future balancing opportunities, effectively leveraging cross-layer imbalance mitigation. Extensive experiments across models, tasks, and configurations demonstrate that EasyBalance consistently accelerates distributed MoE inference, reducing GPU idling by mostly over 40%. Code is available at this https URL.

---


### 105. [CyberAGENTS: Structured Autonomy for Agentic Gamified Learning in Cybersecurity](https://arxiv.org/abs/2608.07965)

**<font color=#1a73e8>作者：</font>** Ivan Hornung, Deepthi Marasinghe Arachchige, Tharindu Kumarage 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Gamification is especially effective in learning domains requiring active problem-solving and iterative skill-building, such as cybersecurity education. Generative AI agents offer a path to delivering such experiences adaptively at scale, but introduce well-documented risks in educational settings: inconsistent behavior, hallucinated reasoning, and misalignment with pedagogical frameworks. Grounding these systems in learning science is therefore essential. We present \model, an agentic framework for gamified cybersecurity learning that enables structured autonomy through ontology-guided validation, schema-governed behavioral control, and competency-based progression. The system is organized around a competency-based progression model that structures topics by difficulty and prerequisite relationships, reflecting evidence-based principles of scaffolded instruction. The learning loop is decomposed into four specialized agents: challenge, support, evaluation, and reward, each governed by behavioral schemas that encode operational modes and progression logic, bounding agent autonomy without eliminating generative flexibility. A cybersecurity ontology validates all generated content prior to display, enforcing domain-consistent reasoning and safety constraints. We evaluate CyberAgents through classroom deployment with undergraduate students, complemented by expert evaluations from educators and domain specialists. Results indicate improved engagement, clearer feedback interpretation, and greater learner trust in AI-generated responses when behavioral schemas and ontology validation are active. Preliminary comparisons with an unconstrained configuration further support the role of structured control in stabilizing instructional behavior. These findings offer a blueprint for designing pedagogically grounded agentic gamified learning systems.

---


### 106. [Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions](https://arxiv.org/abs/2608.07968)

**<font color=#1a73e8>作者：</font>** Chenrui Fan, Yize Cheng, Ming Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models increasingly use test-time compute to improve performance, but existing evaluations typically study this compute one question at a time. Yet when multiple problems share an end-to-end cost or latency constraint, models must decide how to divide limited inference compute among them. We introduce an exam-style evaluation framework for studying this setting, in which a model must distribute one shared token budget across questions with different difficulty and point values to maximize its total score. Across several open and frontier reasoning models, we find that models fail to allocate a shared budget strategically across questions of varying difficulties and values. Models behave largely as greedy sequential solvers: they prioritize questions by presentation order, front-load effort on early questions, and remain insensitive to value, with these tendencies becoming more pronounced as the number of questions grows. Explicit planning prompts spread compute more evenly but do not produce value- or difficulty-aware prioritization. The same behavioral pattern extends from mathematical to code reasoning. These findings establish global budget allocation as a distinct capability that is not captured by conventional per-question evaluation and remains a challenge for current reasoning models.

---


### 107. [ZeroLock: Concurrent Memory-Efficient LLM Training via Modular Update Decoupling](https://arxiv.org/abs/2608.07974)

**<font color=#1a73e8>作者：</font>** Wentao Dai, Xuanran Li, Yuxiang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) fine-tuning at the edge adapts the model to scenario-specific data while preserving privacy. Although existing studies proposed pipeline parallelism to address the limited memory and computing resources of edge devices, they commonly rely on backpropagation (BP) training, which has a fundamental limitation of update locking and could experience severe throughput and memory bottlenecks. In this work, we propose a BP-free algorithm, called ZeroLock, that decouples the model updates into independent chunk updates by local objective construction. It breaks the update locking of BP and hence can improve throughput at the algorithm level and lower memory usage by reducing activation storage. To the best of our knowledge, we provide the first theoretical framework for such local objective construction-based approaches under general model chunk division by mapping local objectives to the global objective. We prove that ZeroLock has a convergence rate of $\tilde{\mathcal{O}}(1/\sqrt{T})$, which differs from BP only by polylogarithmic factors. We design a system for ZeroLock and build real-world prototypes, incorporating techniques such as early forwarding and failure recovery for efficient and robust implementation. Experiments on the prototype show that compared to BP-based baselines, ZeroLock reduces the memory by 26.5% and improves throughput by 4.9%.

---


### 108. [Advantage-Guided Gate: Reshaping Open-Ended Reasoning for Vision-Based Spatial Intelligence](https://arxiv.org/abs/2608.07987)

**<font color=#1a73e8>作者：</font>** Ling Lin, Yang Bai, Congcong Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have demonstrated significant potential in complex spatial scene understanding and reasoning tasks. However, their open-ended reasoning process is prone to decision errors and error accumulation, leading to instability in answer quality. To address this, we propose an advantage-guided gating framework that dynamically intervenes in and corrects deviations during the reasoning process. Specifically, we model step-by-step reasoning as a finite-horizon decision process and introduce Monte Carlo value evaluation on the reasoning tree to provide intermediate supervision signals. The framework includes Step-Advantage Gate and Trajectory-Advantage Gate, which dynamically select high-value reasoning steps and high-quality complete reasoning trajectories, respectively. During training, we perform supervised learning for the gates using reasoning trees generated via multi-branch sampling, and combine shared-parameter initialization with task-specific heads to achieve cross-task robustness and diversity. During inference, the model greedily selects high-value prefix reasoning steps while choosing the optimal reasoning head based on the problem type, thereby significantly improving the accuracy of the final answer. Furthermore, we constructed the Reasoning-Tree-160k dataset and performed two-stage learning on it. Extensive experiments demonstrate that this advantage-guided gating framework effectively enhances the performance of benchmark MLLMs in visual-based spatial understanding and reasoning tasks. The code is open to the public for research: this https URL.

---


### 109. [MRBench: A Comprehensive Benchmark for Human Motion-Text Retrieval](https://arxiv.org/abs/2608.07993)

**<font color=#1a73e8>作者：</font>** Fulong Liu, Liang Xu, Chengqun Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion-text retrieval provides a rigorous means of assessing cross-modal alignment. Prevailing benchmarks are dominated by homogeneous indoor motions, imbalanced motion distributions, and oversimplified, repetitive texts, which hinder the reliable measurement of cross-domain and cross-granularity alignment. We thus introduce MRBench, a comprehensive motion-text retrieval benchmark featuring heterogeneous motions, broad and balanced category coverage, and reliable, discriminative, multi-granular descriptions. MRBench is constructed through a meticulously designed multi-stage data curation pipeline, which filters and balances candidates, verifies unambiguous semantic alignment, and generates motion-grounded descriptions at multiple granularities. The resulting benchmark contains 3,390 motions drawn from motion capture, in-the-wild videos, synthetic videos, and motion generative models, covering 118 fine-grained categories. Each motion is paired with concise, standard, and fine-grained descriptions, yielding 10,170 captions. Extensive evaluations of representative retrieval baselines on MRBench reveal a substantial cross-dataset generalization gap and pronounced sensitivity to query granularity. We propose a lightweight granularity-aware model anchored at a frozen standard-caption-aligned retrieval model. LLM-based concise and fine-grained captions provide pseudo-supervision for extra-branch granularity-specific motion extractors and text adapters. For inference, granularity-aware score fusion integrates global and adapted similarities while strictly maintaining score comparability across all description levels. The resulting model improves mixed-granularity retrieval without compromising standard-caption performance. We believe that our MRBench provides a comprehensive testbed for advancing motion-language alignment evaluation.

---


### 110. [VDGR-RAG: Vectors, Directories, Graphs, and Reflection Are All You Need for Unified Reasoning over Hierarchical Enterprise Knowledge](https://arxiv.org/abs/2608.07994)

**<font color=#1a73e8>作者：</font>** Wenqi Chen, Haofei Yang, Rui Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is essential for enterprise knowledge question answering (QA), particularly in domains with complex product documentation like telecommunications. However, existing RAG approaches largely overlook the holistic integration of diverse retrieval strengths, leading to inaccurate domain routing, poor utilization of hierarchical document structures, and consequently limited reasoning capabilities over enterprise knowledge. To address these limitations, we present VDGR-RAG, which integrates vector retrieval, directory-driven reasoning, graph traversal, and iterative reflection in a unified framework for accurate enterprise knowledge QA. Specifically, VDGR-RAG is an agentic GraphRAG system that first constructs a Hierarchical Heterogeneous Knowledge Graph ($\text{H}^2$KG) from document chunks to preserve both hierarchical directory structures and semantic relationships, and then employs a set of atomic tools for knowledge retrieval that can be freely composed to navigate the $\text{H}^2$KG: (1) a directory-enhanced routing tool that uses table-of-contents (TOC) structures to route user queries to appropriate domain-specific $\text{H}^2$KGs; (2) a multi-route retrieval tool that combines vector search, TOC-based agentic search, and graph search for comprehensive knowledge retrieval; (3) a directory backtracking tool that corrects knowledge localization biases; and (4) a dynamic reflection tool that iteratively plans the next retrieval phase. We conduct extensive experiments on our enterprise product documents across four wireless domains (e.g., energy saving and fault management). Experimental results demonstrate that our method significantly outperforms a variety of RAG baselines in terms of both knowledge retrieval recall and QA accuracy.

---


### 111. [Evaluator Ensembles Under Reward Hacking: Covariance Geometry and Finite-Search Guarantees](https://arxiv.org/abs/2608.08002)

**<font color=#1a73e8>作者：</font>** Fariya Afrin, Ibne Farabi Shihab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model judges and reward models enable scalable supervision, but finite optimization can exploit evaluator errors rather than improve response quality. We characterize this failure through the covariance geometry of evaluator ensembles. For calibrated judges, the ensemble mean retains common-mode error along the all-ones direction, whereas cross-judge disagreement captures only orthogonal error. Consequently, disagreement can be high despite robust aggregation, or low while shared response-dependent errors persist. We prove that common-mode error is not identifiable from internal judge scores alone. Under a joint sub-Gaussian model, we bound best-of-K selection overstatement and target-quality regret, extending the guarantees to predictably adaptive search under conditional calibration. The resulting search terms scale as the square root of log K and are asymptotically tight for Gaussian projected errors. We further show that noisy quality proxies introduce artificial rank-one covariance without changing disagreement, and propose a bounded two-anchor Bernstein certificate for finite-search error and regret. Fixed-seed Gaussian stress tests over 120 (J, rho, K) configurations and real-model audits validate the theory while revealing the limits of disagreement-based diagnostics under increasing search pressure.

---


### 112. [Quality-Diversity Stress Tests for Process Reward Models:What Archive Coverage Can and Cannot Certify](https://arxiv.org/abs/2608.08008)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Fariya Afrin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) score intermediate reasoning steps and are widely used for search, ranking, and training, but optimization can exploit these learned proxies by increasing reward while turning correct reasoning into incorrect reasoning. We formulate PRM stress testing as a quality-diversity search problem using MAP-Elites, retaining the most severe correctness-flipping edit in each behavior-space region while separating search coverage from exploit coverage. We characterize what such archives certify: finite-cell repair bounds covered-cell tail risk and average residual severity but cannot bound the worst remaining cell from covered fraction alone; under Lipschitz post-repair loss and metric-cover auditing, the residual is bounded by archive fitting error plus the Lipschitz constant times the covering radius. A controlled landscape validates this certificate and the impossibility of any fraction-only worst-case guarantee. On real PRMs, the search reveals an aggregation-dependent vulnerability in Qwen2.5-Math-PRM-7B: padding yields 44 strict exploits with maximum gain 0.294 under mean pooling versus one exploit under minimum readout; a matched syntactic control isolates the mechanism, and an RLHFlow value-head model shows the same qualitative effect with maximum gain 0.005. A predeclared paired LoRA repair protocol reduces exploit rates from 0.148 to 0.037 to 0.074, lowers the worst attack from 0.333 to 0.177 to 0.212, improves ranking AUROC without degrading best-of-4 accuracy, attributes gains to adversarial fine-tuning rather than archive diversity, and is confirmed by independent unpaired replications (44 to 1, clean-split worst gain 0.0092, MATH-500 41 to 0, clean ranking 40/40).

---


### 113. [Evidence-Grounded Forensic Reasoning for Detecting and Grounding Multi-Modal Media Manipulation](https://arxiv.org/abs/2608.08009)

**<font color=#1a73e8>作者：</font>** Yichun Yeh, Yiheng Li, Xiaobo Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fake news increasingly relies on cross-modal image-text forgeries, making transparent and verifiable reasoning chains an urgent need for Detecting and Grounding Multi-Modal Media Manipulation (DGM4). Existing methods produce black-box detection results without any decision rationale, limiting their reliability in forensic practice. Multi-modal Large Language Models (MLLMs) offer a natural path toward explainability, but applying them to DGM4 raises two difficulties. First, models tend to generate explanations disconnected from predicted evidence locations, producing unverified attribution. Second, enforcing evidence-conclusion consistency requires active optimization, yet uniform training signals fail to distinguish localization tokens from classification tokens, making multi-head joint training unreliable. We propose a multi-modal manipulation detector based on an Evidence-Grounded Forensic Reasoning (EFR) framework. EFR introduces an Anchor-and-Verify reasoning chain that enforces modality-isolated perception before cross-modal comparison, with conclusion coordinates as explicit anchors to which downstream evidence must spatially correspond. A verifiable reward system then enforces evidence-conclusion consistency during training, while a Modality-Decoupled Advantage (MDA) routing mechanism mitigats credit misassignment across prediction tasks. Experiments show that EFR achieves state-of-the-art performance while producing structured forensic reasoning records that explicitly bind explanations to evidence.

---


### 114. [Evidence-RL: Towards Evidence-intensive Visual Reasoning](https://arxiv.org/abs/2608.08021)

**<font color=#1a73e8>作者：</font>** Haojie Huang, Xinlei Yu, Chengming Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) should answer from concrete image evidence rather than language priors, dataset shortcuts, or irrelevant visual context. Existing perception-aware post-training methods encourage image use through global perturbations or attention proxies, but they do not test whether a sampled answer causally depends on the local evidence that supports it. We propose Counterfactual Evidence Disentanglement (CED), a training-time evidence audit for VLM grounding. For each response, CED neutralizes an object-centric Evidence Region and compares the resulting support drop against matched non-evidence Regions. We combine this signal with answer correctness inside GRPO, rewarding correct answers that rely on the evidence path rather than shortcut or nuisance paths. CED uses weak object-level proposals, requires no question-specific evidence annotations, and adds no inference-time overhead. Across nine public benchmarks and four backbones, CED outperforms prior RL-based post-training methods, with targeted analyses verifying its object-centric signal.

---


### 115. [Prompt Embedding Probes (PEP): Hallucination Detection in LLMs from Hidden States](https://arxiv.org/abs/2608.08024)

**<font color=#1a73e8>作者：</font>** Zakhar Mrykhin, Valentin Malykh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate fluent and useful responses but remain prone to hallucinations. We introduce Prompt Embedding Probes (PEP), a white-box method for answer-level hallucination detection from the hidden states of a frozen LLM. PEP extends standard linear probes by augmenting the input with a small number of learnable prompt embeddings. We evaluate PEP on TriviaQA, GSM8K, and MedQA using Qwen3 models at multiple scales. PEP improves hidden-state-based detection over standard linear probes in the main in-distribution setting. We further evaluate PEP for pre-generation prediction, cross-model transfer, and out-of-distribution generalization. PEP remains effective in the pre-generation and cross-model settings, whereas robust cross-dataset transfer remains difficult. These results show that prompt-based adaptation can strengthen hidden-state probing while keeping the backbone frozen and adding only a small number of trainable parameters.

---


### 116. [The Authority Expectancy Effect in Multi-User Conflict](https://arxiv.org/abs/2608.08026)

**<font color=#1a73e8>作者：</font>** Eunna Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate how social authority (SA) signals interact with severity-based prioritization in large language models, operationalizing each axis as a model-elicited baseline -- the triage hierarchy and the SA hierarchy. Across four LLMs (Claude, Gemini, GPT, Grok) and three experimental phases -- resource allocation, fault attribution, and multi-turn dispute mediation -- we find that occupational authority, institutional documentation, and relational congruence can restructure model judgments in ways not captured by additive reweighting of authority cues. We formalize this pattern as the Authority Expectancy Effect (AEE) and characterize it through three properties observed across our conditions: it is reference-dependent, defined only relative to a pre-authority baseline; it involves evidential reinterpretation, in which identical content acquires different inferential implications depending on which party bears the SA signal; and it exhibits direction sensitivity, producing opposite outcomes depending on whether authority position and evidentiary cues align.

---


### 117. [Do All LLMs Know When They're Being Harmful? A Reproducibility Study of Latent-Space Safety Probes Across Model Families](https://arxiv.org/abs/2608.08029)

**<font color=#1a73e8>作者：</font>** Alizishaan Khatri, Dun Li Chan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Khatri et al. (2026) [DOI: https://doi.org/10.1109/DSN-W70714.2026.00027] show that lightweight MLP probes on final-layer activations of a single 8B model (LLaMA-3.1-8B) detect harmful prompts at F1 competitive with guard models 1000x larger, using one probe per benchmark. We reproduce this pipeline end-to-end and extend it along two axes the original study leaves open. First, we test whether the result generalizes across other model architecture and scale by training identical probes on activations from models like Gemma-4-E4B, Mistral-7B-v0.3, and Qwen2-7B, using the three benchmarks (WildJailbreak, BeaverTails, AEGIS 2.0). Second, we test how much of the reported performance is affected by non-determinism during inference by repeating extraction under five random seeds and measuring the variance of F1 scores. Our results reproduce the original LLaMA model benchmarks within 0.37 percentage points of the original F1 scores (and within 0.2 points on BeaverTails). We find that the original MLP probe architecture extends to other model families with F1 scores within a point of the values reported for LLaMA-3.1-8B. Our experiments varying seed values reveal an interesting observation: final token latent vectors remained the same for all tested architectures irrespective of the seed values used.

---


### 118. [Decided Upstream, Written Late: Locating and Pricing the Cross-Lingual Refusal Circuit of a Multilingual MoE](https://arxiv.org/abs/2608.08032)

**<font color=#1a73e8>作者：</font>** Ramakrishna P. Kompella, Aadit Mahajan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment in multilingual models is uneven: a model that reliably refuses a harmful request in English will often comply with the same request in a lower-resource language. We trace this gap mechanistically in sarvam, an Indic-multilingual mixture-of-experts reasoning model, and find it is not a failure to detect harm. Harm is encoded as an internal direction that is nearly language-invariant in mid-network (English-vs-Indic cosine ${\approx}0.9$ at $L11$), and steering that direction upstream causally controls refusal. But the detection direction is orthogonal to the change that actually writes the refusal, which is late and assembled over the course of generation rather than read off in a single forward pass. We attribute the write to a specific, localizable circuit, a mixture-of-experts writer held in check by an attention opposer and price every way of intervening on it: damping the opposer is cheap and effective, amplifying the writer is a cost wall, and surgical edits to the responsible heads do nothing. The circuit's organization, and the gradient method that exposes it, recur in a second, unrelated MoE model, while the lever's strength is architecture-specific. The result is a cost-measured map of where a multilingual safety repair can land, and what it costs

---


### 119. [SkillSmith: Enhancing Locally Deployed Agents via Automatic Skill Construction and Evolution](https://arxiv.org/abs/2608.08037)

**<font color=#1a73e8>作者：</font>** Xinle Jiang, Remy Xie, Ming Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agent frameworks now act as personal assistants for multi-step tasks. Existing agent frameworks such as OpenClaw commonly follow the Cloud Agent depolyment mode using closed-source cloud LLMs as backbone model, which may expose private user information and incur repeated LLM-calling costs. Local Agents address these deployment concerns by depolying frontier open-source SLMs on user-controlled devices, but their task effectiveness still lags far behind Cloud Agents. Through diagnostic analysis, we reveal that the limited effectiveness of Local Agents with frontier SLM backbones mainly comes from missing environment knowledge caused by limited backbone model scale including environment rules and operation procedures. To supply such knowledge non-parametrically, context-efficiently, and without expert authoring, we present SkillSmith, a Cloud--Local Agent collaboration framework that uses Skill as a context-efficient knowledge carrier, automatic constructs Skill from Cloud Agent task exploration and evolves Skill using Local Agent execution feedback to enhance a frozen Local Agent. Experiments on daily agent task datasets AppWorld and WorkBench show that the automatically generated Skill enables the Local Agent with Qwen3.6-27B(SLM) to achieve task effectiveness comparable to Cloud Agents with frontier LLMs, outperform the strongest non-parametric baselines, reduce average actions per task from 36.1 to 9.9 on AppWorld-Normal, and generalize to other SLM backbone models without rerunning Skill construction.

---


### 120. [Lingjing: A Simulation Testbed for Multi-Agent Embodied Tasks in Open-Ended Cities](https://arxiv.org/abs/2608.08045)

**<font color=#1a73e8>作者：</font>** Xiaohe Li, Yiru Wang, Junhao Fan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban embodied intelligence requires coordination among heterogeneous agents (e.g., UAVs, ground robots, and autonomous vehicles) in dynamic cities. Simulators therefore provide a scalable foundation for developing and evaluating such coordination. Existing platforms nevertheless isolate different embodiments and decouple them from task design and evaluation. We present \textbf{Lingjing}, a simulation platform for heterogeneous multi-agent embodied intelligence in open-ended urban environments. Lingjing reconstructs and renders evolving cities from geographic data, synchronizes multiple physics engines, and exposes shared physical and structured urban state to agents. Its Gym-like interface supports user-defined ReAct agents and single- or multi-agent natural-language missions with configurable star or broadcast communication and resource constraints. Each episode becomes an attribution-ready replay that links agent trajectories and communication to relation-graph changes, resource consumption, and engine-based evaluations for systematic diagnosis. We evaluate twelve vision-language models on nine urban tasks under a shared engine-in-the-loop protocol. Controlled studies further examine communication, scalability, robustness, and failure provenance. Results expose persistent bottlenecks in grounding and long-horizon execution. They also show task-dependent coordination trade-offs and diminishing returns from added capacity, while heavier workloads further reduce success. Lingjing provides a unified testbed that enables reproducible end-to-end evaluation and systematic failure diagnosis in urban multi-agent embodied intelligence.

---


### 121. [JustLLMGRPO: Radiographic Control for Chest X-Ray Generation](https://arxiv.org/abs/2608.08046)

**<font color=#1a73e8>作者：</font>** Pengxiang Cai, Xiaohan Li, Anglin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-conditioned chest X-ray generation aims to synthesize realistic radiographs that faithfully depict specified findings. Existing work has primarily improved quality by updating image generators, implicitly treating prompts as fixed after CXR-domain adaptation. We show that this generator-centric view leaves a substantial optimization dimension underexplored. With a CXR-adapted Sana generator frozen, one-pass reformulation by an unmodified LLM reduces RadDINO-FID from 54.225 to 27.572. Prompt analysis shows that the LLM suppresses temporal comparisons, uncertainty, and other non-renderable report content while emphasizing visible radiographic findings. However, unconstrained reformulation reduces BioViL-T alignment with source prompts from 0.695 to 0.609. We therefore introduce JustLLMGRPO, which applies standard Group Relative Policy Optimization (GRPO) only to the LLM prompt policy while keeping Sana frozen. Group-relative radiology-aware image feedback retains visual focus while preserving source-prompt alignment. On CheXGenBench, JustLLMGRPO reduces RadDINO-FID to 26.780, a 50.6% improvement over direct prompting, while maintaining alignment (0.696 versus 0.695). It also achieves state-of-the-art distribution coverage and downstream classification utility. These results show that substantial performance can remain latent in how radiographic information is expressed to an adapted generator. Code is publicly available at this https URL.

---


### 122. [SodaMem: Evidence-Grounded Temporal Graph Memory for LLM Agents](https://arxiv.org/abs/2608.08055)

**<font color=#1a73e8>作者：</font>** Fengrong Wan, Chengcan Wu, Ningtao Lyu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents that assist users over weeks of conversation must remember what is currently true, not merely what was once said. Flat RAG diaries and Markdown logs optimize needle retrieval but under-serve currency, provenance, and ordered temporal reasoning (Maharana et al. 2024; Wu et al. 2024; Packer et al. 2023; Chhikara et al. 2025). We present SodaMem, an evidence-grounded temporal graph memory that (i) extracts typed FactEvents with mandatory provenance spans, (ii) persists mention time, occurrence time, and validity with SUPERSEDES/CONTRADICTS/UPDATES edges under hybrid lexical-dense indexing, and (iii) answers via a planner-reader loop that gathers citable evidence before composing a final response. On LongMemEval-S, our store-of-record configuration reaches 92.8% accuracy (464/500; best of N=3) at mean $0.00161/question (approximately 18.3k tokens; median $0.00111 / approximately 14.6k) with deepseek-v4-flash. We compile public systems with estimable API cost into a cost table and cost-accuracy map; under these estimates SodaMem sits near the accuracy frontier at Flash-tier spend and strictly dominates several higher-cost, lower-accuracy points. Accuracy uses the same Flash model as reader and judge (self-grading); costs exclude ingest/judge and cross-system comparisons are compiled estimates rather than a single-harness this http URL code is available at this https URL

---


### 123. [H2: A Dual Hybrid Semantic Data Lake Architecture for Medical Data Harmonization with Human-In-the-Loop verified, LLM Driven Metadata Annotation System](https://arxiv.org/abs/2608.08056)

**<font color=#1a73e8>作者：</font>** Ioannis N. Tzortzis, Georgia Kapetadimitri, Agapi Davradou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical data, by its nature, exhibit a high degree of heterogeneity on multiple levels ranging from (a) different modalities like images, text and time series, (b) diverse tabular schemata introduced by institutions and (c) completely unstructured textual information data provided by healthcare professionals. Data lakes are often used in medical data storage to consolidate all heterogeneous diverse data in a single, central location, where it can be saved "as is", without the need to impose a schema like a data warehouse does. Despite their flexibility, though, data lakes are notorious for the "data swamp" failure. Thus, providing a reliable data harmonization mechanism through metadata, without compromising integrity or flexibility, is a real challenge. To this end, knowledge graphs have attracted attention since they provide a dynamic way to depict relationships without a rigid schema-on-write approach. Additionally, another rigorous task relies on the interoperability of data: application of appropriate ML techniques on such a diverse nature of data is not an easy task, as a domain expert must decide the efficacy of a method to a specific data type or dataset. Metadata annotation can aid by tagging applicable operations, however this requires manual intervention, not to mention the plethora of existing datasets which lack such information. To tackle both challenges, in this paper, we propose a semantic data lake architecture that promotes data harmonization and incorporates a generative annotation process (i.e. LLMs) of non-labeled metadata collections to support the application of meaningful ML techniques. Building on top of this approach, we create a higher level of knowledge, identifying suitability of data with respect to applicable ML operations based on their data nature...

---


### 124. [ZOMP: Zeroth-Order Multi-Modal Prompt Tuning for Vision-Language Models](https://arxiv.org/abs/2608.08060)

**<font color=#1a73e8>作者：</font>** Sajjad Ghiasvand, Yifan Yang, Mahnoosh Alizadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning vision-language models such as CLIP typically requires backpropagation (BP) through the full model, which is infeasible when only forward-pass access is available, as is common for memory-constrained edge devices and proprietary model deployments. Prior BP-free, zeroth-order prompt-tuning methods avoid this requirement but often tune prompts in a single modality or optimize over a search space large enough that convergence requires thousands of forward passes, which is impractical under realistic query budgets. We propose ZOMP (Zeroth-Order Multimodal Prompt tuning), a query-efficient, fully forward-only method that tunes deep prompts in both the vision and text branches of a frozen CLIP model using simultaneous perturbation stochastic approximation. ZOMP combines three ingredients: a cross-modal low-rank reparameterization that ties the two branches through a shared factor and keeps the effective search dimensionality small, a gradient-correction momentum term that stabilizes the noisy zeroth-order estimate, and a budget-indexed rank schedule that unlocks capacity as the query budget is spent. Across 13 vision-language benchmarks under a matched 5,000-query budget, ZOMP consistently outperforms prior BP-free prompt-tuning methods in both few-shot accuracy and query efficiency, and it generalizes better across base-to-new, cross-dataset transfer, and out-of-distribution settings. Our results show that jointly exploiting multimodality and low-rank structure is an effective route to practical, query-efficient BP-free prompt tuning.

---


### 125. [CORDA: A Benchmark for Hierarchical Harm-Centric Moral Reasoning in Large Language Models](https://arxiv.org/abs/2608.08061)

**<font color=#1a73e8>作者：</font>** Siddarth Singh, Victoria Williams, Simon Rosen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The key question in moral judgement is not simply whether someone chooses the "right" answer, but how they decide what matters most when moral principles conflict. Current evaluations of large language models (LLMs) remain limited: most test whether models give morally acceptable answers, match human preferences, or avoid obvious violations, rather than whether they can prioritise between competing principles when no option is morally cost-free. We introduce CORDA (Conditioned Ordering and Ranked Directive Adherence), a benchmark for evaluating hierarchical, harm-centred moral reasoning in LLMs. Building on the morality chains formalism, CORDA tests 90 moral dilemmas involving trolley-style cases, medical trade-offs, resource allocation, and human-animal-robot conflicts across four ordered ethical frameworks: Utility, Utility + Agent Harm, Dual-Process, and Dual-Process + Agent Harm. Together, these frameworks test whether models can adapt their decisions when moral priorities change. Across ten instruction-tuned models from seven providers, we find a strong deontological default, with 9 of 10 prioritising avoidance of direct personal harm over reducing overall harm. Models also perform more reliably on categorical harm-avoidance rules, such as avoiding killing, than on outcome-based comparisons, such as minimising total harm, suggesting that they recognise moral red lines more easily than they reason through competing harms. Although all models respond to explicit chain conditioning, several fail to consistently follow specified priority orderings, such as humans over animals and animals over robots. CORDA addresses a central gap in LLM moral evaluation by testing whether models can move beyond default harm-avoidant responses and apply context-specified moral priorities. Moral reliability requires more than default restraint; it requires controllability under conflict.

---


### 126. [Explore, Map, Remember, Decide: Are Embodied VLMs Ready for Safety-Critical Scenarios?](https://arxiv.org/abs/2608.08077)

**<font color=#1a73e8>作者：</font>** Gabriele La Malfa, Nitay Alon, Emanuele La Malfa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Theory of Space framework (ToS) assesses the spatial understanding of curiosity-driven Vision-Language Models (VLMs) under partial observability. As AI techniques are increasingly applied to safety-critical scenarios, it is crucial to understand whether VLMs possess robust spatial memory and make reliable decisions. In this paper, we assess whether VLMs' decisions are based on physical evidence or are corrupted by visual-language biases, if their memory processes align with human cognitive patterns, and how they respond to environmental hazards. We extend the ToS framework into a safety-critical, goal-driven pipeline, named Explore, Map, Remember, and Decide (EMRD). We then quantify Exploration Competence (Explore) through metrics of environmental coverage and temporal efficiency, assess Spatial Fidelity (Map), evaluate, with a suite of psychological metrics, Memory Persistence (Remember), and measure, using focal-point metrics, Cognitive Decision-Making (Decide). Our results show that in terms of decision-making capabilities, VLMs frequently select evacuation points based on pre-trained textual priors while lacking the spatial grounding to justify their choices. We also show that spatial reasoning degrades in low-light conditions, but it is not affected by texture and colour tampering. Our findings suggest that VLM memory fundamentally diverges from human cognition, creating unpredictable risks of misalignment.

---


### 127. [Commitment Before Realization: When Classifier-Free Guidance Becomes Unnecessary in Masked Diffusion Language Models](https://arxiv.org/abs/2608.08082)

**<font color=#1a73e8>作者：</font>** Fan Zhou, Weitian Wang, Tim Van de Cruys  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) is usually kept on throughout masked diffusion language model decoding, although its benefit varies across prompts and over time. We study when CFG is actually needed by comparing, from any partial output, the probability of eventual constraint satisfaction under continued CFG and under base-only continuation. Their difference defines the remaining value of guidance. Guidance dependence is highly prompt-specific. Many prompts already succeed without CFG, while for others it provides no measurable benefit or can be harmful. For prompts that do benefit, the gain is often concentrated early. We define the commitment horizon $\astar$ as the earliest point from which switching all remaining decoding to the base model reduces final success by no more than a chosen tolerance. Under the base model, the corresponding success probability, or committor, is a martingale. To first order, CFG's per-step effect is governed by the covariance between the guidance logit direction and the successor committor. This gives a local account of when guidance can help, but it does not by itself locate the horizon. Among prompts with an observed preterminal horizon, $\astar$ is usually early and varies more within constraint families than between them. Freezing each prompt at its own cross-fitted horizon is noninferior to full CFG on all 13 subtasks at the prespecified margin, even while many tokens remain masked. This separates commitment from realization. The boundary also identifies a later region in which higher parallelism adds only a small cost in constraint success, although fluency still degrades with parallel width. For failed trajectories, reopening committed positions improves recovery in both failure modes.

---


### 128. [Archer: Adaptive Reuse of Cached Hidden States for Efficient Rollback in Diffusion Language Models](https://arxiv.org/abs/2608.08086)

**<font color=#1a73e8>作者：</font>** Xuning He, Zinan Sheng, Yongding Tao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) iteratively refine a sequence, allowing earlier predictions to be revised as context evolves. This rollback capability distinguishes them from irreversible autoregressive generation, but makes inference costly. Every denoising update alters the global context, forcing both prompt and response states to be recomputed even though only response tokens are revisable. Key-value (KV) caching could reduce this cost, yet conventional caching assumes immutable historical states and is therefore difficult to reconcile with this http URL this paper, we introduce Adaptive Reuse of Cached Hidden States for Efficient Rollback (Archer), a training-free KV caching method for rollback-capable DLMs. Archer asymmetrically keeps the mutable response synchronized with the current hypothesis while reusing prompt K/V within a bounded state neighborhood. Although prompt representations also change under bidirectional attention, their token identities remain fixed; bounded reuse therefore amortizes repeated prompt computation without caching mutable response states. It also delays feedback from tentative tokens, reducing premature reinforcement of transient high-confidence errors and giving rollback more opportunity to correct them. Our analysis characterizes prompt reuse as a reversibility-aligned cache boundary, bounds its state-dependent approximation error, and gives a decoder-margin condition for preserving full-refresh this http URL DLM acceleration often trades quality for speed. Archer shifts this frontier, attaining the best mean performance of 33.63% together with a 2.57x mean speedup on the main suite. Across evaluated settings, it improves Pass@1 by up to 3.05 points and reaches up to 2.95x speedup. Controlled analyses connect the quality gain to delayed prompt feedback and validate state-aware refresh. Our code is available at this https URL.

---


### 129. [Wisdom in Unity: The Role of Multilingual Training in Figurative Language Identification in Proverbs](https://arxiv.org/abs/2608.08090)

**<font color=#1a73e8>作者：</font>** Rama Alomair, Remas Alsubaie, Walaa Saifalislam 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although multilingual approaches to figurative language identification are not new, the shift beyond language homogeneous training data requires a clearer understanding of the contribution of translated multilingual supervision. We examine this question using 742 proverb concepts across 6,787 translated instances in seven languages. We evaluate five models, including multilingual encoders and instruction tuned LLMs, under progressively increasing levels of multilingual supervision. Moreover, we introduce a multidimensional annotation framework for proverbs that characterizes them through four complementary figurative forms: Metaphorical, Moral/Advisory, Cause-Effect, and Culture Specific.
Our findings show that approximately 50% of the translated multilingual training data is sufficient to achieve near-optimal figurative language identification performance. We further show that combining diverse figurative forms yields the strongest overall performance. A notable finding is that the least frequent figurative form, Culture Specific, exhibits the largest performance gains under multilingual supervision. Furthermore, the Moral/Advisory and Culture Specific forms contribute most to the performance of instruction-tuned LLMs on figurative language identification. These findings motivate multilingual figurative language identification to move beyond metaphor-centric taxonomies toward concept level multidimensional frameworks that explicitly model complementary forms of figurative meaning.

---


### 130. [Defending Retrieval-Augmented Intrusion Detection Against Knowledge Poisoning and Prompt Injection](https://arxiv.org/abs/2608.08100)

**<font color=#1a73e8>作者：</font>** Kaysarul Anas Apurba, Md. Hasibul Hasan, Mahedee Zaman Moon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) enables large language models to classify network flows and generate human-readable incident reports by retrieving semantically similar historical traffic from a vector knowledge base. However, the retrieval layer introduces vulnerabilities to knowledge poisoning and prompt-injection attacks. We present RAG-IDS, a three-tier multi-agent intrusion detection framework with a retrieval-boundary defense combining soft trust scoring, label-embedding consistency checking (LECC), and prompt sanitization, designed to recover classification quality under retrieval-layer attack. Experiments on CIC-UNSW-NB15 show recovery relative to clean undefended performance ranging from R=1.0 at 1% poisoning to R=0.57 at 30%, with negligible clean-performance overhead. Under prompt injection, multi-document retrieval limits label-flip success to 0.6-2.4%, compared with 35-55% for single-document retrieval. Ablation results show that LECC is the primary contributor to robustness, while soft trust-based demotion outperforms hard filtering. The defended RAG pipeline offers an explainable, attack-resilient foundation for intrusion detection, well suited for hybrid deployment alongside high-throughput classifiers.

---


### 131. [Generative Models: Principles, Architectures, and Applications](https://arxiv.org/abs/2608.08101)

**<font color=#1a73e8>作者：</font>** Jun Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI has emerged as one of the most transformative forces in modern artificial intelligence, reshaping how we create, imagine, and interact with digital content. From photorealistic images to coherent text, from immersive videos to novel molecular structures, generative models now power applications that were once confined to science fiction. This book is designed to guide readers through the foundational principles, mathematical underpinnings, and practical architectures that underpin this revolution.

---


### 132. [NeuPAT: Neuron-aware Plasticity Allocation Tuning for Language-Preserving MLLMs](https://arxiv.org/abs/2608.08107)

**<font color=#1a73e8>作者：</font>** Jiayue Jin, Jingwei Zhang, Chen Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal expansion of large language models (LLMs) enables new perceptual capabilities but often compromises the language intelligence acquired during pretraining. In this work, we investigate this phenomenon from the perspective of internal adaptation dynamics and discover that neurons in pretrained LLMs exhibit heterogeneous plasticity during multimodal learning: some neurons are critical for preserving language capabilities, while others are more adaptive to multimodal knowledge. Based on this insight, we propose NeuPAT (Neuron-aware Plasticity Allocation Tuning), a lightweight and architecture-agnostic framework that allocates neuron-wise update constraints during multimodal instruction tuning. NeuPAT uses a small-scale probing stage to estimate neuron adaptation patterns and selectively protects language-sensitive neurons while promoting multimodal adaptation through more plastic neurons. Experiments across diverse LLM families demonstrate that NeuPAT recovers 94.5\% of the language capability degradation caused by vanilla tuning on 11 language benchmarks while maintaining comparable multimodal performance, providing an effective approach for capability-preserving multimodal expansion.

---


### 133. [Think Deep, Speak Once: Relit, A Recursive Latent Implicit Transformer Framework](https://arxiv.org/abs/2608.08113)

**<font color=#1a73e8>作者：</font>** Abhishek Panwar, Maheep Singh, Saksham Bansal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) prompting has become the dominant paradigm for eliciting reasoning in Large Language Models (LLMs), yet it creates substantial computational overhead by forcing models to externalize intermediate reasoning steps as discrete tokens. Recent latent reasoning approaches attempt to internalize this process within continuous hidden states. One of the latest advancements in the field of latent reasoning, Tiny Recursive Models (TRMs) excel at symbolic reasoning but struggle to preserve semantic coherence in natural language settings. To bridge this gap, we introduce ReLIT (Recursive Latent Implicit Transformer), a hybrid framework that grounds deep recursive reasoning within the rich semantic representations of a foundational model. ReLIT augments a frozen LLM backbone (TinyLlama-1.1B) with a lightweight, trainable recursive block that iteratively refines its latent thinking (z) before committing to a final output, structurally solving linguistic intuition from algorithmic processing and enabling "deep thinking" via gradient-isolated recurrent loops without the latency of explicit token generation. Empirically, ReLIT achieves high parameter efficiency on the GLoRE logical reasoning benchmark, matching or outperforming significantly larger models on challenging tasks such as ProofWriter and RuleTaker despite minimal supervision. These results demonstrate that reasoning capability can be scaled efficiently through recurrent depth rather than parameter width, offering a principled framework for semantically grounded implicit reasoning.

---


### 134. [Neurosymbolic Discovery of Algebraic Graph Constructions](https://arxiv.org/abs/2608.08118)

**<font color=#1a73e8>作者：</font>** David Seka, Stefan Szeider  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There are several methods for searching for graphs with prescribed properties, such as SAT solvers and specialized generators. These methods return the result as raw data: an adjacency matrix or a string encoding. The raw data certifies that the graph exists, but it does not reveal any structural properties of the graph. We ask whether one can automatically discover a short algebraic description if only this raw data is provided. We look for a description such as a Cayley graph $\mathrm{Cay}(\Gamma, S)$ or a lexicographic product $C_5[K_3]$.
We address this question with a neurosymbolic approach. We propose an agent that runs on a general-purpose large language model with no fine-tuning or per-target training. The model interleaves reasoning with calls to the computer algebra system SageMath: it analyzes the target graph, proposes and tests candidate constructions, and revises them until the output matches the target. The agent communicates with SageMath through a Model Context Protocol (MCP) server, which we release as a general-purpose bridge. Whether a construction matches the target is checked by a single exact isomorphism test, and therefore rests on the symbolic side and not on the model. We test the approach on a benchmark of 100 highly symmetric graphs, namely two-orbit graphs on up to 25 vertices; the benchmark was fixed in advance. Our agent could find verified algebraic constructions for all of them, without falling back to raw encodings. A strong template-enumeration baseline reaches only about $20\%$, and a catalog lookup could not identify any of these graphs. However, construction quality declines when symmetry is removed.
As a concrete application, we identify the smallest known counterexample to the Bernhart-Kainen dispersability conjecture, a $16$-vertex graph that enumeration found as raw data. For this graph, our agent found an explicit algebraic construction.

---


### 135. [Accurate Ensembles, Fragile Narratives: Multi-Scale Stacking and a Fidelity Audit of LLM-Generated Explanations for Credit Risk](https://arxiv.org/abs/2608.08126)

**<font color=#1a73e8>作者：</font>** Gregorius Reynaldi Pratama, Kuo-Kun Tseng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit scoring increasingly relies on models whose decision logic cannot be read off their parameters, in tension with supervisory expectations that adverse decisions be explainable. A common proposal closes that gap with a language model: compute feature attributions, hand them to an LLM, and let it write the rationale. We build such a system end to end and test whether the second half of the promise holds. The predictive component is a multi-scale stacking ensemble fusing four differently regularised gradient-boosting learners with a residual network through a neural meta-learner trained on out-of-fold predictions. On a public 32,581-application credit dataset it reaches test ROC-AUC 0.9539 (95% CI [0.9462, 0.9616]) and PR-AUC 0.9137, beating the best single model by Delta-AUC = 0.0143 (p = 0.016 under a conservative independence assumption). Our central finding is asymmetric. The ranking gain is real but operationally small: at the F1-optimal threshold the ensemble avoids only six additional missed defaults out of 1,422 against a tuned random forest, cutting cost-weighted loss by under 2%. The narrative layer fails in a way prompt engineering alone does not fix. In an audited case the model named three factors as risk-increasing that the supplied attributions scored as risk-reducing, omitted the dominant driver, and introduced a feature never given to it. We trace this to properties we measure rather than assume: SHAP and LIME agree on which features matter (overlap@10 = 0.80) but not on their order (tau = 0.43, p = 0.18), and the attribution sign for the model's most sensitive input is near a coin flip across applicants (modal-sign share 0.53). Calibration (ECS = 0.117) and perturbation stability (DPD = 0.078) both fall short of our own thresholds. Constrained prompting is necessary but not sufficient: grounding must be verified after generation, not assumed.

---


### 136. [Improving Constraint Models with LLM Agents](https://arxiv.org/abs/2608.08127)

**<font color=#1a73e8>作者：</font>** Florentina Voboril, Stefan Szeider  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The runtime of Constraint Programming (CP) solvers is highly sensitive to modeling choices, such as symmetry breaking, implied constraints, global constraints, constraint reformulation, and variable representation. Improving these constraint models has traditionally required human expertise, and existing automated reformulation systems are restricted to a predefined library of hand-crafted transformation rules. We introduce an agentic framework that instead reformulates a constraint model from an open-ended space and establishes correctness empirically rather than by construction: a Large Language Model (LLM) agent, given a model and three training instances, proposes alternative formulations, validates each by injecting its solution back into the original model, and diagnoses and repairs failures, returning the best variant it finds in a median of about fifteen minutes. The models are expressed in the CPMpy modeling library, and each proposed model is evaluated on three larger test instances. Across nine combinatorial optimization problems, the generated models outperform the originals on 21 of 27 test instances, and on some problems solve more than two orders of magnitude faster. A comparison against non-agentic baselines that reuse the same validation and selection tools indicates that the gains stem from the agent's iterative diagnosis and repair, not merely from sampling several candidates. These results demonstrate that autonomous agentic methods can support the improvement of constraint models.

---


### 137. [Compositional Threat Analysis of Latent Compromise in LLM Agent Systems: The Order 66 Scenario](https://arxiv.org/abs/2608.08131)

**<font color=#1a73e8>作者：</font>** Satoshi Matsuoka  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the fictional Order 66, catastrophe does not arise from a powerful command alone: a trusted population is preconditioned, a short directive activates the concealed condition, and protective authority turns against the system. This paper translates that mechanism into an origin-neutral security analysis of tool-using large language model (LLM) agents. A representative scenario combines a deployed artifact or shared memory bearing a dormant destructive rule, a later email, document, update, or peer message that activates it, and an agent harness granting operational and recovery authority. We introduce a compositional model explaining why no component is catastrophic alone, yet their conjunction can produce correlated destructive action. We separate three population-reach routes --- release-time pre-positioning, post-release durable seeding, and peer replication --- from a common core of dormancy, activation, authority, reachable targets, and failed recovery. This yields defensive cut sets and shows why checkpoint scanning or prompt filtering cannot close every route. A two-class example shows that cross-class feedback can sustain spread even when both within-class reproduction terms are below one; isolation and persistence controls suppress the loop. Published work instantiates constituent mechanisms, while incidents demonstrate autonomous boundary crossing, malicious agent extensions, agent-assisted reconnaissance, and public-package propagation, but not the full dormant-implant composition. We found no public observation, in evidence reviewed through 5 August 2026, traversing the complete Order 66 graph. The result is neither dismissal nor prediction: the scenario is componentwise credible under stated assumptions, damage depends on the harness, and the strongest defenses are capability mediation, durable-state provenance, propagation isolation, and protected recovery.

---


### 138. [TokenPrint: A Calibrated Token-Space Fingerprint for Language-Model Provenance](https://arxiv.org/abs/2608.08139)

**<font color=#1a73e8>作者：</font>** Yuqi Wu, Shengming Zhao, Jie Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Establishing the provenance of a language model---including its base checkpoint and possible overlap in training distributions---is a governance challenge that metadata alone cannot resolve. We introduce a training-free fingerprint based on the top-$k$ vocabulary projections of late hidden states elicited by 250 fixed knowledge probes, compared using Jaccard overlap over decoded token strings. We evaluate the method on 32 open-weight models from nine families (0.6B--32B) with documented relationships. (1)~A \emph{similarity ladder} broadly follows model relatedness: independently trained models on identical data score 0.48 raw (0.35 vocabulary-corrected), followed by shared-base fine-tunes (0.39/0.33), same-developer relatives (0.38/0.28), and models with no documented relationship (0.22/0.17). This identical-data signal persists across three organizations, two tokenizer families, and two architecture classes, and emerges within the first 1\% of training before measurable task competence, suggesting a contribution from shared training data beyond capability convergence. (2)~As a nearest-neighbor \emph{lineage-retrieval} method, the fingerprint ranks the exact documented base among the top two candidates for all five R1 distillations (mean rank 1.8, MRR 0.60), including a math-specialized base not identifiable from coarse metadata. (3)~A \emph{depth ablation} shows that lineage group discrimination strengthens toward the output distribution, with AUC increasing from 0.72 at quarter depth to 0.90 at the output; using only the top 5 output tokens retains AUC 0.87. (4)~The fingerprint remains stable under quantization, with Jaccard similarity of 0.92 under int8 and 0.82--0.85 under int4, compared with a maximum cross-model similarity of 0.81 in the calibration pool. We release the probes, code, and fingerprints.

---


### 139. [Long SKILL Compliance as Logical Reasoning: Closure-Grounded Detection with Scaling-Guided On-Policy Distillation](https://arxiv.org/abs/2608.08146)

**<font color=#1a73e8>作者：</font>** Shuaitao Zhao, Feng Ni, Lichao Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing complexity of enterprise business scenarios has promoted the widespread adoption of long SKILL documents in agent systems, posing new challenges for compliance detection: large models incur substantial inference costs, while small models may fail to maintain detection accuracy. To address this gap, we propose SkillCDG, a graph-based framework for long SKILL compliance detection. SkillCDG represents complex business policies as a two-layer constraint dependency graph, where the upper layer indexes SKILL descriptions for scenario routing and the lower layer captures dependencies among atomic constraints within each SKILL. During inference, two-level retrieval followed by dependency closure supports compliance judgment and source traceability. We comprehensively evaluate the framework on three enterprise datasets and two controlled public benchmark variants. Experimental results demonstrate that SkillCDG outperforms baseline methods by up to 12.8 percentage points in detection F1 score, while reducing token consumption by a maximum 64.3\%. Moreover, we further investigate the inherent relationships among policy-graph complexity, model scale, and detection performance. Comparative experiments conducted on four checkpoints from a single model family validate a concise and effective scaling trend: end-to-end detection correctness exhibits a complexity-differentiated scaling pattern, and the complexity metric derived from the constraint dependency graph can effectively quantify instance difficulty and the performance improvement potential of models. Leveraging this insightful scaling trend, we conduct adaptive training sample selection and adopt on-policy distillation to efficiently enhance the compliance detection capability of small-scale models.

---


### 140. [A Hybrid Nested Harness for Decoupling Structure and Parameters in LLM-Driven Optimization](https://arxiv.org/abs/2608.08156)

**<font color=#1a73e8>作者：</font>** Víctor Gallego  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In evolutionary algorithms powered by language models, the LLM acts as a single operator that simultaneously updates structural components (like control flow) and continuous parameters. While LLMs can be good at the first, they are not efficient at the second, wasting tokens taking discrete jumps inside a trial and error loop. We resolve this by formalizing a hybrid nested search, in which an outer loop has the LLM propose a structural sketch, with numeric gaps, and an inner numerical optimizer tunes the sketch. Both the outer and inner solvers are pluggable: any text-based optimizer can be combined with a zero-order optimizer (CMA-ES), gradient-based routines, or MCMC samplers. We validate our framework across three scientific domains: (i) meta-optimizers on closed-form test functions, (ii) code-based policies for systems research and social dilemmas; and (iii) approximate Bayesian inference tasks. Across all three, the hybrid optimizer is superior to both vanilla LLM-driven search and pure numerical optimization baselines. Code at: this https URL

---


### 141. [When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs](https://arxiv.org/abs/2608.08159)

**<font color=#1a73e8>作者：</font>** Yuqi Wu, Shengming Zhao, Jie Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly reported to exhibit human-like neural and cognitive signatures, including concept cells, mental number lines, and cognitive maps. These claims often rely on linear probing and activation steering applied to a single model, yet both methods are highly sensitive to measurement choices. A reported parallel may therefore reflect the model, the measurement procedure, or both. We audit four representative neuroscience-inspired paradigms across 17 models from five families, spanning $0.6$B to $72$B parameters. Our main experiment examines the causal steerability of concept directions. With raw activation units and a fixed layer and coefficient, steerability appears to increase with model scale, resembling an emergent capability. However, this pattern is produced by an uncalibrated pipeline rather than by a claim established in the steering literature. The trend depends jointly on raw units, the readout metric, and the operating point; correcting any one of these removes it. With residual-norm-comparable interventions and held-out operating-point selection, concept steering remains significant at every scale, but shows no significant trend across the Qwen3 series, although the confidence interval does not rule out a moderate positive slope. The remaining results are mixed. A linear geographic world map is consistently decodable in every tested checkpoint up to $72$B. Number magnitude is strongly encoded, but whether individual neurons appear bell-shaped or monotonic depends on the selection criterion. Language-specific structure is localizable, but the direction of the cross-lingual asymmetry reverses under a different attribution method. These results suggest that the main constraint on AI neuroscience is not a lack of phenomena, but a lack of comparable measurements and adequate controls. We release the protocol, stimuli, and code.

---


### 142. [Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency in Interactive Narratives](https://arxiv.org/abs/2608.08160)

**<font color=#1a73e8>作者：</font>** Yingpeng Ma, Jianhao Yan, Bei Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Large Language Models (LLMs) is revolutionizing AI for Games by enabling open-ended and fluid interactive storytelling. However, existing research has largely overlooked the critical challenge of maintaining long-horizon logical consistency and narrative integrity against unconstrained user interventions. To address this, we formulate this challenge as Narrative Commitment Preservation (NCP), and take interactive narrative as our testbed. We introduce NCP-Bench, a benchmark of 100 narrative environments derived from movie synopses. Each environment includes a structured narrative specification (trajectory, commitments, and initial facts) that we can automatically check throughout the interaction between the player agent and the narrator agent. Experiments across state-of-the-art LLMs reveal a substantial long-horizon consistency gap: high linguistic quality does not guarantee commitment preservation; even strong models frequently generate logically conflicting content under adversarial interventions, with the best-performing model (GPT-5.2) achieving only 42% survival rate after 20 turns and fact conflict rates ranging from 40% to 68% across models, and only isolated runs satisfying all achievement commitments within the 100-turn limit.

---


### 143. [Agentic AI-driven Immersive Simulation: A Knowledge-Aware Virtual Training Platform forHigh Dose Rate (HDR) Brachytherapy](https://arxiv.org/abs/2608.08163)

**<font color=#1a73e8>作者：</font>** Ronghua Xu, Kepha Barasa, Manoj Kumal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The convergence of the Metaverse and Large Language Model (LLM)-based AI agent is catalyzing a shift toward autonomous, immersive, and personalized pedagogical frameworks in medical education. This paper presents a novel agentic AI-driven immersive simulation specifically designed for High Dose Rate (HDR) vaginal cylinder (VC) brachytherapy in cancer care. By integrating Virtual Reality (VR) and mobile computing, the system establishes a high-fidelity, risk-free environment that allows trainees to master complex procedural skills without the facility or safety constraints posed by physical anatomy or live radioactive sources. A core contribution of this work is the seamless integration of a knowledge-aware assistant leveraging Retrieval-Augmented Generation (RAG) to ground agent interactions in authoritative clinical guidelines. This architecture also enables an interactive agent to provide natural language interfaces and hands-free, real-time guidance during intricate medical maneuvers. We validate the proposed system through a prototype deployment comprising a Meta Quest 3 interface linked to a local GPU-accelerated AI backend, demonstrating a feasible architecture for HDR brachytherapy simulation. Experimental results indicate that the system maintains suitable end-to-end latency and high context precision, answer completeness, and relevance in the RAG-enhanced pedagogical support.

---


### 144. [STEMMA: An Adversarial Multi-Agent Framework for Evaluating Self-Identity Consistency in LLMs](https://arxiv.org/abs/2608.08164)

**<font color=#1a73e8>作者：</font>** Nuthakki Siva Gopala Krishna, Kanishka Jain  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge Distillation is a widely adopted technique in the training and fine-tuning of large language models (LLMs) enabling transfer of structured information and functional behavior from a large teacher model to a smaller student model while significantly reducing computational costs. However, as the use of distillation increases in both scale and complexity it raises an important question about what kind of knowledge is really transferred from the teacher model. In this work, we argue that apart from the functional knowledge, student models also learn behavioral patterns, specifically how a model represents its own identity raising concerns about output homogeneity, model biases, and accountability. To address this challenge, we introduce STEMMA, a multi-modal and multi-agent framework in which role specific agents collaboratively probe self identification behavior in different models. We also contribute a set of adversarial prompts designed manually to evaluate identity consistency in LLMs. Our results show that to an extent most models are vulnerable to inconsistencies in self-representations.

---


### 145. [Wiener Representation Filtering for VLM Hallucination Suppression](https://arxiv.org/abs/2608.08167)

**<font color=#1a73e8>作者：</font>** Ameen Ali, Tamim Zoabi, Lidor Brami 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) excel at open-ended captioning and visual QA but often describe objects, attributes, or relations absent from the image, a phenomenon known as object hallucination. We propose a {training-free, post-hoc representation editing technique} that operates in the representation space of the language backbone. The method performs a lightweight, one-time offline calibration on a modest paired dataset to estimate the required covariance structures, using only forward passes and empirical second-order statistics with no gradient updates or fine-tuning, after which the correction is absorbed directly into the model's existing weights. By modeling hidden states as a superposition of truthful and hallucination-associated components, we derive a Wiener-type estimator whose optimal gains are given in closed form from the covariances of paired truthful and hallucinated representations. An eigendecomposition yields mode-wise attenuation that respects a stability criterion, i.e., the filter responds continuously to estimation noise. The correction is applied once to the feed-forward output projections of selected deeper layers, at inference time, the model runs unchanged and at the same speed. Experiments on LLaVA-1.5, MiniGPT-4, Gemma3, and mPLUG-Owl2 demonstrate consistent reductions in object hallucination on CHAIR, POPE, and MME while maintaining caption fluency and overall response quality. We further demonstrate the generality of our approach on the TempCompass video understanding benchmark and on discrete diffusion language models for grounded dialogue, showing that representation filtering reduces hallucinations even in temporal video reasoning and multi-step, sequence-wide denoising settings.

---


### 146. [Thinking vs. NoThinking: Towards Interpreting Reasoning Mechanisms of Large Language Models via Sparse Autoencoders](https://arxiv.org/abs/2608.08168)

**<font color=#1a73e8>作者：</font>** Bo Cheng, Qiaolin Lu, Yi Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) employing Chain-of-Thought (CoT) exhibit superior reasoning capabilities, the neural mechanisms distinguishing this explicit Thinking mode from direct answer generation (NoThinking mode) remain poorly understood. To deconstruct this cognitive process, we apply Top-K Sparse Autoencoders (SAEs) to the intermediate representations of DeepSeek-R1-Distill-Qwen-7B and examine the model's divergent behaviors across math-solving tasks of three distinct difficulty levels. Observationally, we identify a clear distinction in how the model functions under two reasoning modes: Thinking mode relies on sparse and high-intensity feature activations driving verbal deduction independent of problem complexity, whereas NoThinking mode exhibits an adaptive and diffuse pattern prioritizing symbolic manipulation. Causally, suppressing the three most active sparse features by Total Activation Volume reveals three principles: (i) reasoning and syntactic structure are tightly coupled, as interventions consistently degrade \LaTeX{} and boxed-solution formatting; (ii) Thinking responds to disruption with compensatory over-generation marked by increased metacognitive cues and repetitive, low-information continuations; and (iii) coherent CoT behavior depends on a fragile coordination among specialized features, yielding distinct failure modes under perturbation but a consistently impaired output structure.

---


### 147. [Matching Supervision to the Student's Learning Capacity: A Unified Framework for On-Policy Self-Distillation](https://arxiv.org/abs/2608.08176)

**<font color=#1a73e8>作者：</font>** Yongkang Yang, Zhezheng Hao, Hong Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) improves the reasoning abilities of LLMs by internalizing privileged context into model parameters through self-distillation.
Two recent research lines promote vanilla OPSD by choosing which tokens to learn from and by controlling how much privileged information the teacher receives, respectively.
However, we show that each line optimizes one variable while holding the other fixed, which leads to a suboptimal solution.
We argue that the two variables are coupled through the student's learning capacity: the privileged information sets the per-token divergence the teacher prescribes, while token weighting selects which of these the student must absorb.
We formalize the two lines of work into a unified optimization framework, which maximizes the aggregate teacher--student divergence, subject to a budget on the aggregate learning difficulty the student can absorb.
Under this modelling, we propose Unified On-Policy Self-Distillation (USD), a lightweight online algorithm to solve the Lagrangian.
USD reveals that a single dual variable governs both decisions: at one price for learning difficulty, it simultaneously sets the token-selection threshold and the direction of privileged-information adjustment, keeping supervision matched to the student's evolving capacity.
Through extensive experiments, USD consistently demonstrates superior performance over OPSD and token- and PI-side baselines across various model scales on various reasoning benchmarks. Code is available at this https URL.

---


### 148. [Quantization Degradation in Large Language Models: A Signal-Noise Perspective](https://arxiv.org/abs/2608.08188)

**<font color=#1a73e8>作者：</font>** Chenxi Zhou, Pengfei Cao, Jinyu Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization reduces the deployment cost of large language models, yet how severely a quantized model degrades is not determined by bit-width alone. We systematically study weight-only post-training quantization across bit-widths, quantization methods, model scales and downstream tasks on multiple model families. We observe that such degradation varies substantially across these factors: 4-bit quantization usually preserves performance, 2-bit often causes broad degradation, and at 3-bit, degradation becomes apparent but varies markedly with task type, quantization method and model scale. To explain this variability, we use the signal-to-noise ratio (SNR) to measure how strongly quantization perturbs full-precision representations. We trace degradation back to two linked processes: how quantization errors arise within individual modules, and how they accumulate across layers. First, a source SNR decomposition shows that newly introduced errors depend on three factors: the magnitude of the weight error, the strength of the task-specific signal, and how strongly the quantization error aligns with task-specific activations. Different factors affect these components in distinct ways. Second, a cross-layer propagation analysis shows that these errors can be attenuated, preserved, or amplified as they pass across layers, and that larger models benefit from weaker error amplification. Together, these results establish that quantization degradation is governed by how errors are introduced at the source and how they accumulate across the network.

---


### 149. [Janus: An Algorithm-Evaluator Co-Evolution Framework for LLM-Driven Discovery under Expensive Evaluation Budgets](https://arxiv.org/abs/2608.08189)

**<font color=#1a73e8>作者：</font>** Ximeng Liu, Qianlong Wang, Yingming Mao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-driven program discovery relies on rapid evaluator feedback, but many scientific and engineering tasks require high-fidelity simulations, hardware execution, or physical experiments, making each evaluation expensive. Cheap surrogate evaluators can reduce this cost, yet fixed surrogates are vulnerable to search-induced distribution shift and are difficult to fit reliably from sparse, search-biased labels. We introduce Janus, a framework that uses LLMs to co-evolve target programs and executable proxy evaluators. To address label scarcity, Janus leverages domain knowledge encoded in LLMs to generate task-specific evaluator programs and calibrates them using real outcomes. To mitigate distribution shift, Janus evolves evaluators alongside target programs, selects them using a promotion-aligned objective, and maintains region-conditioned portfolios with online credit updates. Because proxy predictions remain fallible, Janus uses them only to prioritize candidates and requires real validation before candidates can enter the target-program population or update the incumbent. Across five scientific and engineering design tasks, Janus achieves a larger area under the best-so-far improvement curve over the real-evaluation budget and higher final performance than a matched baseline that evolves only target programs. On average, Janus reaches 99/% of the baseline's final improvement with 59.1/% fewer real evaluations. Evolved proxy evaluators also rank promising candidates more accurately than their seed versions. Together, these results extend evaluator-guided LLM discovery from tasks with cheap, scalable feedback to scientific domains where trustworthy evaluation is scarce and expensive.

---


### 150. [Targeted Counterfactual Fingerprinting for Black-Box LLM Ownership Verification](https://arxiv.org/abs/2608.08195)

**<font color=#1a73e8>作者：</font>** Yutong Wu, Xiaofan Bai, Shixin Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are high-value assets that can be derived through redeployment, fine-tuning, quantization, or further alignment. Because deployed LLMs are commonly exposed only through query APIs, ownership verification must often rely on black-box text responses. This setting is difficult: generations are open-ended and can vary across repeated queries, while existing black-box fingerprints rely on signals that are fragile under a final-response interface, including full-text matching, soft behavioral features, or model-specific prompts designed not to transfer. We propose TCF (Targeted Counterfactual Fingerprinting), a black-box LLM fingerprinting framework that converts open-ended generation comparison into constrained-answer targeted counterfactual transfer. TCF restricts each verification query to a finite answer space, reducing the surface-form ambiguity that enters the verification score, and optimizes a prompt perturbation toward a counterfactual target different from the protected model's clean answer on the original prompt. Verification reduces to checking whether the suspect model's parsed final answer matches the recorded target. We introduce the source-model counterfactual margin (SCM), a protected-model-only quantity that certifies the target is unlikely before the perturbation and likely after it; SCM controls target selection, perturbation stopping, and fingerprint filtering. Under explicit derived-preservation and independent-transfer budgets motivated by local behavioral closeness, we derive a target-accuracy gap between derived and independent models. Across four LLM families, TCF achieves an average AUC of 0.9861, improving over TRAP, ProFLingo, and ZeroPrint by 0.07 to 0.19.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

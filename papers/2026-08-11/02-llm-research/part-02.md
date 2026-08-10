# 🧠 大模型相关研究 | 2026年08月11日

> 本类共 **170** 篇论文：已确认 **159** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-170](./part-04.md)

---

### 51. [MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents](https://arxiv.org/abs/2608.06745)

**<font color=#1a73e8>作者：</font>** Zhisheng Chen, Bingfan Zeng, Bangde Cao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents rely on memory to reuse experiences, yet existing memory systems often assume that evidence can be directly consumed through a fixed representation. This leads to representation mismatch, where relevant information is available but not organized for the current decision. To this end, we propose MemPrism, a task-conditioned relational memory framework that separates persistent experience storage from decision-time working memory. MemPrism records interactions as the event stream and dynamically constructs relational views according to the current task context. A lightweight view policy selects the relation structure, evidence range, outcome condition, and granularity, while a deterministic composer and render transform historical facts into a temporary optical working-memory view for a frozen task policy. Experiments on long-horizon embodied and web-agent benchmarks show that MemPrism consistently improves the task performance, especially as trajectories become longer, while reducing memory token consumption. Furthermore, the learned view policy transfers across different VLMs without additional adaptation, demonstrating the effectiveness of task-conditioned relational views as a general memory interface for agents.

---


### 52. [Progressive Content Refinement with Decaying Reward Joint LinUCB](https://arxiv.org/abs/2608.06750)

**<font color=#1a73e8>作者：</font>** Shion Ishikawa, Pablo Loyola, Young-joo Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Iterative refinement has significantly enhanced Large Language Model (LLM) performance; however, existing methods ranging from feedback-based Self-Refine to traditional bandit approaches often rely on static options or overlook the saturation effect. This neglect leads to over-exploitation, where the continuous use of identical prompts or arms results in diminishing rewards over time.
To address this challenge, we propose a novel contextual bandit algorithm that explicitly incorporates reward decay modeling. Utilizing an Expectation-Maximization (EM) algorithm, our method simultaneously estimates both arm-specific and decay parameters. Furthermore, by embedding prompts as arms, we facilitate the joint learning of arm values, distinguishing our approach from the traditional disjoint Linear Upper Confidence Bound (LinUCB) framework.
Experimental results on Sentiment Reversal and GSM8K benchmarks demonstrate that our method achieves significant performance gains over strong baselines. Finally, our ablation study confirms that the integration of reward decay modeling within the bandit framework is crucial for mitigating over-exploitation and optimizing the iterative refinement process.

---


### 53. [Mind the Gap: A Dual Knowledge Graph Framework for Unified Multi-task User Intent Inference](https://arxiv.org/abs/2608.06752)

**<font color=#1a73e8>作者：</font>** Tzu-Cheng Peng, Chien Chin Chen, Chih-Hao Ku 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes DKG-MTI, a dual knowledge graph framework for unified multi-task user intent inference from online travel reviews. Existing approaches often rely on hierarchical pipelines that suffer from error propagation or retrieval methods that ignore structural relationships in domain knowledge. To address these limitations, we introduce an inference-only knowledge augmentation framework that dynamically constructs a User-Specific Intent Knowledge Graph from each review and aligns it with a Global Hotel Knowledge Graph through structure-aware semantic smoothing. The aligned knowledge is combined with the original review and processed by a large language model to simultaneously predict aspect ratings and generate reverse user intent statements. Experiments on TripAdvisor reviews show that DKG-MTI consistently outperforms strong LLM and retrieval-based baselines in both classification and intent generation tasks, demonstrating the effectiveness of structure-aware knowledge alignment for scalable and explainable intent inference.

---


### 54. [Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence](https://arxiv.org/abs/2608.06756)

**<font color=#1a73e8>作者：</font>** Ying Chen, Weizhen Li, Zhe Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models are increasingly serving as the reasoning core of embodied agents. Robot execution is inherently iterative: each action reshapes the scene and physical state, continually renewing what must be perceived, reasoned about, and verified. Meeting these demands requires complementary capabilities that differ in supervision signals, prediction formats, and verification criteria. Existing approaches typically develop these capabilities against isolated, task-specific objectives, leaving open how they should be organized and integrated around execution as a whole. We present Capek 0.5, an embodied vision-language model built around an execution-centric capability taxonomy. Rather than organizing training by datasets or tasks, the taxonomy groups embodied capabilities according to their functional roles throughout execution and comprises four capability families: Spatial Reasoning, Temporal Understanding, Action Guidance, and State Verification. Each capability is first acquired by a dedicated specialist through reinforcement learning with verifiable rewards from a shared backbone, and the specialists are then consolidated into a single inference-time model through weight-space merging followed by routed policy-space distillation. We instantiate Capek 0.5 at the 2B and 35B-A3B scales and evaluate it from three complementary perspectives: comprehensive benchmark suites including Capek-StateBench, a new benchmark for state verification; a controlled study of capability retention from specialists to the unified model; and closed-loop evaluation in simulated embodied environments. Capek 0.5 improves the large majority of matched benchmark rows over its initialization, retains all four specialized capabilities in one checkpoint with quantified losses, and transfers to closed-loop embodied task execution.

---


### 55. [Stockmark-Nemotron-3-Nano-Omni-JapanDocReader: Structured Document Parsing via Capability Injection and Forgetting Control](https://arxiv.org/abs/2608.06758)

**<font color=#1a73e8>作者：</font>** Shi Chen, Hayato Aida, Makoto Morinaga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Stockmark-Nemotron-3-Nano-Omni-JapanDocReader, a Japanese document understanding model built from Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16. The central goal of this work is structured document parsing via capability injection and forgetting control: we inject Japanese structured document parsing capability into a reasoning-oriented multimodal model while preserving its document VQA capability as much as possible. We study parsing-centric SFT, which uses only structured document parsing data; mixed SFT, which combines structured document parsing and VQA data; and parsing-centric RL, which optimizes structured parsing with a task-level reward. Our experiments show that parsing-centric SFT substantially improves structured document parsing performance but causes measurable VQA forgetting. Mixed SFT mitigates this forgetting while preserving nearly the same structured parsing performance. Applying DAPO-based parsing-centric RL on top of the mixed SFT checkpoint further improves structured document parsing beyond the SFT ceiling, producing the final released model. The training data is constructed with a data engine consisting of two complementary synthetic streams: a Japanese Document VQA Stream and a programmatic structured document parsing stream. We also discuss reward design and variance-based prompt filtering for continuous structured document parsing rewards, highlighting their importance for making RL effective in long-reasoning structured document parsing tasks.

---


### 56. [CubicQuant: Parametric Non-Uniform Codebooks for High-Throughput LLM Inference with 1-8-Bit Weights](https://arxiv.org/abs/2608.06763)

**<font color=#1a73e8>作者：</font>** Xuetian Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight quantization for large-language-model inference must balance adaptive reconstruction levels with representations regular enough for efficient GPU execution. Uniform integers constrain each group to a linear grid. Low-bit floating-point formats use a fixed exponent-mantissa structure, while learned codebooks gain flexibility at the cost of irregular decoding and additional metadata.
We introduce CubicQuant, a parametric non-uniform scalar format that preserves a dense integer code stream while adapting reconstruction levels within each weight group. A monotonic cubic curve, specified by two shape parameters and one scale, maps uniformly spaced magnitude codes to non-uniform levels. The family spans 1-8-bit weight payloads, contains symmetric uniform integer quantization as an exact special case, and has effective width B + 64/G bits per weight for payload width B and group size G. We derive population distortion under Uniform, Gaussian, and Laplace distributions, formulate continuous and Dynamic-A8-carrier-aware fitting objectives, and describe direct packed-weight GPU execution.
For finite groups of G=128 with 15,360 samples per distribution, W4 CubicQuant reduced reconstruction RMSE relative to optimally clipped four-bit uniform integer quantization by 3.90% on Uniform, 13.49% on Gaussian, and 28.14% on Laplace samples. Relative to the best enumerated four-bit finite floating-point format, the reductions were 3.90%, 9.44%, and 6.27%. Preliminary H200 kernel measurements show a workload-dependent crossover: model-dtype execution is faster for narrow GEMV, while Dynamic A8 becomes favorable as row count grows. The results establish the format's representational promise and direct executability; downstream model quality and cross-device end-to-end performance remain open evaluation questions.

---


### 57. [GraphVerse: A Comprehensive Visual Graph Reasoning Benchmark for Multimodal Large Language Models](https://arxiv.org/abs/2608.06769)

**<font color=#1a73e8>作者：</font>** Yuanfu Sun, Yuanhang Ren, Kang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Multimodal Large Language Models (MLLMs) have achieved remarkable progress across diverse vision-language tasks, creating an urgent need for more challenging benchmarks. Yet existing evaluations still provide limited insight into whether these models can truly reason over structured visual information. Visual Graph Reasoning (VGR) offers a compelling testbed for this challenge, requiring models to integrate perception, structural understanding, and multi-step reasoning over graph-based visual inputs. However, prior VGR benchmarks often reduce the task to visual perception followed by text-based reasoning, restrict evaluation to single-image settings, rely on answer-only metrics, and underrepresent realistic graph-centric scenarios. To bridge the gap, we introduce GraphVerse, a unified benchmark that jointly evaluates perception, visual reasoning, and text-based graph reasoning in MLLMs under both single-image and paired-image settings. At its core is a suite of Graph-centric Image Editing (GIE) strategies that modify graph images while preserving their semantics, turning them into active tests of visual reasoning. We further propose VGR-Score, a process-sensitive metric that evaluates reasoning quality beyond final-answer accuracy. Extensive experiments reveal several key limitations of current MLLMs in VGR, while also validating the effectiveness of GIE strategies and the transferability of GraphVerse to broader multimodal reasoning capabilities. The code is available at this https URL.

---


### 58. [Faster Query-Key Learning Sharpens Attention in Self-Attention Models](https://arxiv.org/abs/2608.06776)

**<font color=#1a73e8>作者：</font>** Rahul Vashisht, Harish G. Ramaswamy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A standard self-attention layer consists of two interacting circuits: the query-key circuit that governs attention allocation, and the output-value circuit that maps attended representations to predictions. Collapsed and factorized parameterizations of the query-key and output-value circuits lead to qualitatively different attention patterns. In particular, some parameterizations give sharper attention to task-relevant tokens, at a similar training loss. We analyze how the parameterizations of these circuits shape the parameter trajectories in single-layer self-attention models trained for next-token prediction. Through gradient-flow analysis, we show that factorization induces implicit rescaling of the two circuits' learning rates. We derive closed-form dynamics showing that output-value and query-key parameters move along a line, with relative speeds determined by their learning rates. Faster query-key learning relative to output-value learning thus produces sharper attention, as the model compensates for slower output-value learning by increasing attention mass on relevant tokens. Experiments show that differences in the relative learning rates of the two circuits govern attention concentration. This improves attention interpretability proxies while maintaining comparable predictive performance.

---


### 59. [Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence](https://arxiv.org/abs/2608.06778)

**<font color=#1a73e8>作者：</font>** Jiayun Zhang, Junshen Xu, Zejun Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mapping cyber threat intelligence (CTI) text to MITRE ATT&CK techniques is essential for structured threat analysis, yet manual annotation is costly and does not scale. The ATT&CK taxonomy comprises several hundred attack techniques, and a single CTI passage may describe multiple techniques, making accurate and complete extraction challenging. Existing automated approaches fall short in different ways: multi-label classifiers struggle with severe class imbalance and the large label space, while LLM-based methods--retrieval pipelines and fine-tuned generators--optimize token-level objectives that treat technique annotation as sequence generation rather than set prediction, lacking direct supervision on whether the predicted technique set is correct and complete. We propose TTP-R1, a two-stage framework that combines retrieval-augmented supervised fine-tuning (SFT) with reinforcement learning using verifiable rewards (RLVR). A hybrid retriever first narrows the large label space to a candidate set, and a fine-tuned LLM learns to select the correct techniques. We then apply Group Relative Policy Optimization with a decomposed reward that directly supervises the precision, recall, and output format of the predicted technique set. Across four CTI benchmarks, TTP-R1 achieves the best average F1, improving sub-technique-level F1 by 7.4 percentage points over Claude Sonnet 4.5 with retrieval augmentation, while running 28x faster when served as an 8B-parameter model on a single GPU.

---


### 60. [Multi-Perspective Triad Interaction Graph Neural Network for Cognitive Distortion Detection](https://arxiv.org/abs/2608.06785)

**<font color=#1a73e8>作者：</font>** Jun Seo Kim, Hye Hyeon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cognitive distortion detection is a key task in computational mental health, yet existing approaches often overlook the psychological structure of distorted thoughts. We propose MTI-GNN (Multi-Perspective Triad Interaction Graph Neural Network), which models Beck's cognitive triad---negative views of the self, world, and future---as complementary perspectives for classification. An LLM decomposes each utterance into the three perspectives, from which perspective-specific similarity graphs are constructed and encoded by a Multi-Perspective GNN. A Triad Interaction module models cross-perspective dependencies through sequential source-conditioned updates and feature-wise gating, while Prototype-Guided Perspective Fusion performs label-conditioned aggregation. Label-expanded supervision incorporates all available distortion annotations during training. We evaluate MTI-GNN on 9,764 samples from four Korean, English, and Chinese datasets spanning ten distortion categories. MTI-GNN significantly outperforms all supervised variants and exceeds eight prompted generative models under zero-shot and few-shot settings. Leave-one-perspective-out ablations show that all three perspectives contribute significantly, while human expert evaluation provides preliminary evidence of their alignment with the intended cognitive dimensions.

---


### 61. [Simple-OPD: Demystifying Warm-up for On-policy Distillation](https://arxiv.org/abs/2608.06802)

**<font color=#1a73e8>作者：</font>** Tao Liu, Taiqiang Wu, Mao Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own rollouts with token-level supervision from teacher models, but its effectiveness can depend strongly on the warm-up stage before OPD. In this paper, we demystify warm-up for OPD from both data and training perspectives. For data, we find that effective warm-up relies on teacher-compatible chain-of-thought supervision, and that even incorrect teacher rollouts can provide comparable benefits to correct ones. This suggests that warm-up primarily transfers a teacher-compatible thinking pattern rather than merely correct answers. For training, we show that low-rank adaptation (LoRA) with a near-saturation training duration better balances in-domain adaptation and out-of-distribution generalization than full-parameter SFT. Based on these findings, we propose Simple-OPD, a plug-and-play initialization method that warms up the student on teacher-generated CoT with LoRA before OPD. Experiments across diverse settings demonstrate the effectiveness and robustness of Simple-OPD.

---


### 62. [Evolving Parallel Algorithm Portfolios via Potential-Aware Instance Generation with LLMs](https://arxiv.org/abs/2608.06808)

**<font color=#1a73e8>作者：</font>** Shaofeng Zhang, Shengcai Liu, Zhiyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Automatic Construction of Portfolios via Large Language Models (LLM-ACP) suffers from poor generalization in practical few-shot scenarios when solving complex combinatorial optimization problems. Instance and algorithm co-evolution frameworks address this by expanding the training dataset with generated hard instances on which the current algorithm portfolio underperforms, thereby enhancing generalization. However, this paradigm faces two critical limitations: evaluating instance hardness relies on high-quality reference solutions, and single-mode generation patterns limit instance diversity. To overcome these limitations, we introduce the Potential-aware Instance and Algorithm Co-evolution (PIAC) framework. Our core contribution is twofold. First, we propose potential gain, a novel metric that eliminates the need for reference solutions. This metric estimates generalization gain by perturbing the generated algorithms and assessing their improvement potential on generated problem instances. Second, PIAC leverages LLMs to synthesize diverse instance mutators, exploring a broader region of the problem-instance space and thereby enhancing the portfolio's generalization capabilities. Given that perturbation spaces vary across different algorithms, we instantiate our framework on Greedy Constructive, Ant Colony Optimization, and Guided Local Search algorithmic backbones. Comprehensive evaluations on the Traveling Salesman Problem (TSP) and Capacitated Vehicle Routing Problem (CVRP) across six distinct data distributions demonstrate that PIAC consistently outperforms state-of-the-art LLM-ACP baselines, notably achieving a 19.76% relative improvement for TSP Greedy Constructive portfolios.

---


### 63. [FutureBridge: Token Selection Beyond Local Preference in Collaborative Decoding](https://arxiv.org/abs/2608.06819)

**<font color=#1a73e8>作者：</font>** Quanquan Li, Hongbo Zhang, Yihe Chi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Token-level collaboration allows a large language model (LLM) to assist a small language model (SLM) when their predictions diverge. Existing methods either use LLM-generated intervention tokens or rank candidates with the LLM's next-token probabilities. Both rely on the LLM's local preference, even though an LLM-selected token may be difficult for the SLM to build on. We present FutureBridge, which ranks joint LLM-SLM token candidates according to how well they support the SLM's subsequent reasoning. During training, an answer-verified LLM trajectory supplies a fixed shared future, and a frozen SLM evaluates every candidate under this common context. The resulting counterfactual scores supervise a lightweight token reranker that observes only the current state and candidate token. At inference, FutureBridge uses the LLM only to expand the candidate pool, selects one token, and returns generation to the SLM without generating or appending a future suffix. Across five mathematical reasoning benchmarks, FutureBridge improves the Qwen3-1.7B SLM's Math Avg. by 35.1% relative to greedy SLM decoding. These results indicate that token selection benefits from modeling whether the receiving SLM can use each candidate to continue reasoning, rather than relying on the LLM's local preference alone.

---


### 64. [Autonomy-of-Heads: Data-Free Sparse Attention from Frozen Query-Key Geometry](https://arxiv.org/abs/2608.06849)

**<font color=#1a73e8>作者：</font>** Yehan Yang, Junyuan Shang, Yang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context LLM inference is bottlenecked by quadratic attention computation and growing KV-cache costs. Existing sparse attention and KV-compression methods typically decide which tokens or heads to preserve from runtime attention scores, observation windows, calibration prompts, or learned gates, making head diagnosis input-dependent and costly to deploy. We propose Autonomy-of-Heads (AoH), a data-free method that identifies retrieval and streaming heads from the spectral geometry of query-key projections. AoH defines the kernel attention operator $M_h = W_K^{h\top}W_Q^h$ and uses its effective-rank as a weight-space measure of head function: concentrated spectra indicate a small number of dominant query-key matching directions and are associated with retrieval heads, whereas diffuse spectra indicate the absence of a dominant global matching direction and are associated with streaming heads. We further derive an efficient $d_\text{head}$-dimensional computation that avoids constructing the full $d_\text{model}\times d_\text{model}$ matrix. We conducted extensive experiments across models demonstrating that at 50\% sparsity, AoH retains 96.5\% of Full Attention performance on average while reducing prefill and decode latency by up to 41.4\% and 66.0\%, respectively, and KV-cache memory by 50.0\% at 256K tokens.

---


### 65. [Gated-BEPO: Confidence-Gated Bellman Credit Assignment for Large Language Model Agents](https://arxiv.org/abs/2608.06861)

**<font color=#1a73e8>作者：</font>** Hongxi Yan, Ziyue Huang, Shichao Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training large language model agents in long-horizon environments requires assigning credit from sparse terminal outcomes to individual actions. Existing critic-free methods propagate trajectory-level rewards uniformly across steps, while recent approaches construct step-level groups by matching repeated states and compare actions within each group. The former cannot distinguish useful actions in failed trajectories from ineffective actions in successful ones. The latter rely on step credit derived directly from individual trajectory outcomes and fixed-weight fusion with episode-level credit. We propose Gated-BEPO, which derives step-level credit from empirical rollout graphs. For each rollout group, Gated-BEPO constructs an empirical graph and estimates node values through a mean-backup Bellman fixed point that reflects the empirical action distribution of the current policy. We then accumulate these temporal-difference residuals along each sampled trajectory using generalized advantage estimation, yielding step-level Bellman advantages that capture both immediate and downstream effects. To adaptively fuse episode- and step-level credit, a confidence gate incorporates Bellman credit only at states with multiple observed successors and otherwise uses episode-level credit. Experiments on WebShop, ALFWorld, and visual Sokoban show consistent improvements across language and vision-language models, while diagnostic ablations support the effectiveness of Bellman fixed-point value estimation and show that step-level credit should be incorporated selectively rather than uniformly into the final advantage.

---


### 66. [Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection](https://arxiv.org/abs/2608.06865)

**<font color=#1a73e8>作者：</font>** Xuechao Zou, Shun Zhang, Kai Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The malicious use of generative artificial intelligence to create highly realistic deepfake videos raises serious ethical concerns and poses substantial challenges to AI safety. However, existing deepfake video benchmarks provide limited coverage of recent synthesis methods and generally lack reliable fine-grained textual annotations. Meanwhile, conventional detectors and multimodal large language models (MLLMs), whether operating as a single model or relying on a single analytical perspective, often fail to capture subtle forgery artifacts, limiting their generalization to emerging AI-generated methods. To address these limitations, we introduce FaceVid-Forensics-100K, a large-scale deepfake video dataset comprising 100,000 videos and spanning 33 synthesis methods across face swapping, face reenactment, and entire-face synthesis, including recent generators such as Seedance 2.0. The dataset provides fine-grained textual annotations of visual observations and verdict-consistent forensic explanations, automatically synthesized through a multi-model aggregation and conflict-resolution pipeline powered by advanced MLLMs. Building on this benchmark, we propose a multi-agent forensic reasoning framework that employs four specialized domain-expert agents to independently analyze forgery cues from four perspectives: texture, lighting, motion, and physics. A judge agent then reconciles their reports to produce a final prediction together with an explanation. Extensive evaluations on out-of-domain test sets show that, despite being composed entirely of small open-source MLLMs, our framework outperforms all methods including closed-source GPT and Gemini models and ranks first across all reported metrics on this benchmark. The project page is available at this https URL.

---


### 67. [LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers](https://arxiv.org/abs/2608.06867)

**<font color=#1a73e8>作者：</font>** Tao Feng, Fangxu Yu, Haozhen Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> No single large language model (LLM) is optimal across all queries and budget constraints, making model routing essential for cost-effective deployment. Existing routers adopt diverse formulations and implementations, making fair comparison and extension difficult. We present a unified formulation of LLM routing as a sequential decision process characterized by five components: context encoders, model encoders, scoring functions, decision rules, and learning signals, covering single-turn, multi-turn, and personalized routing. Based on this formulation, we develop an automated pipeline for constructing routing supervision and evaluating routers jointly on response quality and inference cost. The resulting benchmark, xRouteBench, spans generic LLM, memory-augmented, vision, time-series, and personalized routing tasks. We further introduce LLMRouter, an open-source modular infrastructure with more than 16 representative routers. Our empirical study shows that learned routers outperform the strongest fixed-model baseline by 14.6% relatively, lightweight routers become more competitive under tight cost constraints, and user-conditioned routing consistently improves personalization.

---


### 68. [CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems](https://arxiv.org/abs/2608.06871)

**<font color=#1a73e8>作者：</font>** Yingtao Tian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex systems, core objects of study in artificial life, model diverse phenomena through nonlinear, feedback-driven interactions that produce emergent behavior, with applications from population dynamics and biology to economic policy and strategic decision-making. Yet the difficulty of predicting how feedback structure gives rise to emergent behavior, a central open problem in artificial life, makes goal-directed design exceptionally challenging. In established practice, system structures are written in specialized modeling languages such as DYNAMO or STELLA, compounding the challenge with labor-intensive workflows that limit adoption and hinder timely decision-making. To address these challenges, we introduce CEDAR, an autonomous method that uses Large Language Model (LLM) agents to discover complex systems satisfying user-specified behavioral goals. Our key innovation is an LLM-driven Monte Carlo Tree Search (MCTS) deeply coupled with complex systems: at each iteration, an LLM Judge evaluates emergent behavior against specified goals and an LLM Editor proposes improved variants, with the Judge acting as a fitness function and the Editor as a variation operator, akin to a generate-and-evaluate loop in evolutionary computation. We represent complex systems as a restricted, runnable subset of Python with domain-specific primitives, letting LLMs modify system dynamics directly. CEDAR formalizes this as an MCTS variant with an LLM-parameterized transition kernel and value function, enabling goal-directed discovery of complex system behaviors while preserving solution diversity, and its LLM-based interpretability reveals how structural changes drive emergent behavior. CEDAR reduces human effort while enabling capabilities difficult to achieve with existing approaches, facilitating broader adoption of complex systems across domains.

---


### 69. [FedVAR: Prototype-Aligned Federated Framework for Video Anomaly Recognition](https://arxiv.org/abs/2608.06876)

**<font color=#1a73e8>作者：</font>** Ghani Haider, Majid Kundroo, Boyun Eom 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the era of Industrial Internet of Things (IIoT) and Cyber-Physical Systems (CPS), Federated Learning (FL) offers a promising decentralized intelligence paradigm for Video Anomaly Recognition (VAR). This task is vital for maintaining high-fidelity Digital Twins and ensuring safety in mission-critical environments. However, the inherent data heterogeneity across distributed edge clients leads to a fundamental challenge known as semantic misalignment, where clients learn divergent feature representations of "normal" and "abnormal" events. The problem becomes particularly pronounced in VAR, where the presence of diverse and fine-grained anomaly categories leads each client to develop distinct semantic interpretations of abnormality. Existing federated methods primarily focus on binary anomaly detection and fail to address this misalignment, preventing effective fine-grained recognition. In this paper, we introduce FedVAR, a weakly-supervised FL framework explicitly designed for VAR. Leveraging the rich representations of Vision-Language Models (VLMs), FedVAR employs a prototype-based alignment mechanism that creates a shared semantic anchor for all clients to re-center and align their visual and textual feature spaces. This process enforces a consistent representation of "normality" across the decentralized network, directly mitigating semantic misalignment and enabling robust prompt-learning of anomaly direction vectors with minimal communication overhead. We conduct extensive experiments on challenging benchmarks under various non-IID data partitioning schemes, unseen domains, and novel anomaly classes. The results demonstrate that FedVAR consistently outperforms state-of-the-art federated baselines, establishing a robust framework for distributed intelligence in video-based CPS.

---


### 70. [SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time](https://arxiv.org/abs/2608.06880)

**<font color=#1a73e8>作者：</font>** Qinfeng Li, Dalin He, Yuntai Bao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> General-purpose skills promise reusable procedural knowledge for language agents, yet semantic relevance does not guarantee execution utility: a retrieved skill may encode assumptions that conflict with the current task, execution environment, or other retrieved skills. We formalize this problem as the skill--execution misfit. To address it, we propose SkillAligner, a training-free execution-time skill adaptation framework that treats retrieved skills as adaptable drafts rather than fixed instructions. Before execution, SkillAligner performs a one-time joint adaptation that specializes useful skill fragments to task requirements, aligns their procedural assumptions with the available execution interface, and composes the resulting guidance by resolving dependencies, conflicts, and redundancy across skills. The adapted content is consolidated into a compact execution guide and reused throughout the subsequent trajectory. Extensive experiments across diverse agent benchmarks and model backbones show that SkillAligner substantially improves task performance over existing skill-use baselines, reduces skill-induced regressions at the instance level, and lowers total inference cost.

---


### 71. [Georeferencing Non-Gazetteered Place Names using Biological Specimen Records](https://arxiv.org/abs/2608.06884)

**<font color=#1a73e8>作者：</font>** Aneesha Fernando, Surangika Ranathunga, Kristin Stock 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biological specimen records collected by natural history institutions constitute a rich source of temporal geographic knowledge, capturing biodiversity information about regional landscapes as they were recorded at different times. Using digitised data from the Allan Herbarium (New Zealand), this study identifies place names in these specimen locality descriptions that are absent from current gazetteers; we refer to these as non-gazetteer place names (NGPs). These place names are typically historical, vernacular, or colloquial and were used as landmarks to describe a specimen's location at the time of collection. We then investigate the problem of georeferencing the NGPs using only the limited information available in the specimen records. To resolve this, we leverage repeated occurrences of the same place name across specimen records with different specimen locations and spatial relation terms, extracting and inverting these relations to derive constraints on NGP locations. This approach is instantiated within deterministic, probabilistic, and LLM-based methods, enabling a comparative analysis of their strengths and limitations for text-based spatial inference. On a pseudo-NGP benchmark, probabilistic inference achieves the highest accuracy (median error 1.43 km; A@1 km 36%), while the LLM yields competitive but less precise estimates (median error 1.80 km; A@1 km 31%), indicating that, despite advances in LLMs, traditional modelling remains advantageous when high spatial precision is required.

---


### 72. [SkillEval: Decomposing Agent Skill Quality into Interpretable Signals](https://arxiv.org/abs/2608.06891)

**<font color=#1a73e8>作者：</font>** Jiahui Han, Qinuo Li, Ziheng Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills provide reusable procedural knowledge that helps agents solve specialized tasks. As their use expands, evaluating skill quality becomes increasingly important. Existing evaluations often measure skill quality by testing whether a skill improves performance on specific downstream tasks. However, a reusable skill may apply to multiple task scenarios. Downstream evaluation mainly reflects the compatibility between a skill and the evaluated task, provides only a partial view of skill quality, and does not identify which aspect of the skill should be improved. We find that general properties of the \texttt{this http URL} document play an important role in skill quality. To evaluate these properties, we propose \textbf{SkillEval}, an interpretable framework for document-level skill evaluation. SkillEval evaluates each property using a fixed and inspectable scoring direction, producing interpretable scores. It further measures and reduces the influence of unrelated document features, such as length and formatting, so that each score captures its intended semantic property more specifically. Specifically, SkillEval learns an interpretable direction for each quality property from controlled positive--negative skill pairs in the hidden representation space of the model, and scores a new skill by projecting its representation onto these fixed directions. We use SkillEval to evaluate skills in controlled quality tests and show that SkillEval reliably distinguishes skills of different quality. In addition, SkillEval scores closely reflect downstream task performance, providing an early indication of whether a skill is likely to help an agent complete a task. We further explore SkillEval for diagnosing weaknesses in skill documents and guiding targeted revisions. The revised skills improve the targeted properties and achieve higher pass rates on downstream tasks.

---


### 73. [Prune Once: Retraining-Free Task-Agnostic Pruning for Vision-Language Models](https://arxiv.org/abs/2608.06901)

**<font color=#1a73e8>作者：</font>** Minseok Kang, Hyunwoo Kim, Chanyoung Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved remarkable generalization across diverse multimodal tasks through large-scale pre-training, yet their rapidly increasing computational and memory requirements pose significant challenges for deployment in constrained environments. Existing pruning strategies often depend on task-specific criteria or LLM-oriented importance measures, making them unsuitable for task-agnostic pruning, where no task-specific samples are available at pruning time and the pruned model remains broadly applicable. We introduce a retraining-free VLM pruning framework called PORTA that derives a task- and modality-agnostic importance formulation based on activation variation, estimated from generic calibration data, which reliably captures feature-level representation utility across modalities. PORTA further incorporates an adaptive sparsity allocation mechanism that assigns layer-wise pruning ratios based on output feature variability, avoiding the limitations of uniform sparsity and reducing performance degradation at high compression levels. Extensive experiments across VLM architectures, such as CLIP, BLIP, and Qwen2-VL, demonstrate that PORTA achieves competitive downstream performance under high sparsity without requiring any retraining, supporting efficient VLM compression. Code is available at this https URL.

---


### 74. [Calibrating WEAT Against Anisotropy: ZCA Whitening as a Geometric Pre-Processing Step for Embedding Association Tests](https://arxiv.org/abs/2608.06908)

**<font color=#1a73e8>作者：</font>** Seitaro Ono, Senna Ross, Jun Saiki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose Zero-phase Component Analysis (ZCA) whitening as a geometric pre-processing step for the Word Embedding Association Test (WEAT). WEAT is a bias measurement method widely used in both computational social science and AI fairness research. It relies on cosine similarity as a measure of semantic association, which assumes that the embedding space is approximately isotropic. However, prior work has reported that many widely used language models do not satisfy this assumption, raising concerns about the reliability of bias measurements. ZCA whitening transforms the covariance of the embedding space into the identity matrix while minimizing perturbation to the original vectors. This transformation restores the isotropy condition on which WEAT relies. We evaluate our approach on ten standard WEAT test suites and seven models spanning three architectural families, yielding 70 model-task combinations. The results show that ZCA whitening substantially reduces the anisotropy of the embedding spaces across all models. Particularly for highly anisotropic models, we further observe improvements on standard semantic similarity benchmarks, indicating that the calibrated space better captures semantic associations. After calibration, over 30% of WEAT results change significance status, and effect sizes shift in both directions depending on bias category. These shifts suggest that uncalibrated measurements may both overestimate and underestimate the associations encoded in the embedding space. These findings indicate that previously reported bias measurements in anisotropic embedding spaces should be interpreted with caution and may benefit from re-evaluation with calibrated methods. Our approach contributes to restoring the measurement foundation of WEAT across both computational social science and AI fairness research.

---


### 75. [Long-Horizon Agent Trajectory Attribution: A Unified Benchmark and Fine-Grained Annotation Framework](https://arxiv.org/abs/2608.06909)

**<font color=#1a73e8>作者：</font>** Jing Chen, Yang Sun, Li Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate through long-horizon trajectories involving user instructions, tool use, external observations, and memory. Existing benchmarks primarily evaluate behavioral outcomes but provide limited support for fine-grained attribution analysis. We introduce trajectory attribution and develop a benchmark and annotation framework for this task. The benchmark organizes heterogeneous trajectories under a unified component schema and provides annotations of the primary attribution component, together with attack and execution chains where applicable. Instantiating the benchmark with trajectories from AgentDojo and the Stage and Canary settings of Agent3Sigma yields more than 1,300 annotated trajectories covering task-aligned actions, unsafe actions, and safety refusals. The benchmark defines two evaluation tasks, primary attribution localization and attribution-chain recovery, and provides reference baselines based on incremental trajectory contribution and component-level leave-one-out perturbation. It captures diverse attribution settings, including local and long-range attribution as well as structured attribution chains. Reference baseline results exhibit substantial performance differences across these settings, providing an initial characterization of the benchmark's attribution challenges. Beyond this initial instantiation, we release a reusable annotation skill that enables trajectories generated by new agent models to be standardized, annotated, and evaluated under the same framework. Project resources and future releases are available at this https URL.

---


### 76. [MuST-VAD: Mutual Structured Learning for Video Anomaly Detection](https://arxiv.org/abs/2608.06913)

**<font color=#1a73e8>作者：</font>** Satoshi Hashimoto, Hitoshi Nishimura, Mori Kurokawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose MuST-VAD, a mutual structured learning framework for weakly supervised video anomaly detection (VAD) in which an anomaly detector and a large vision-language model (LVLM) exchange their acquired knowledge. Detectors in weakly supervised VAD learn anomaly scores from features extracted by a fixed, task-agnostic backbone. These fixed features bound the achievable detection accuracy. Recent methods therefore transfer LVLM semantics into the detector as richer features. However, this transfer is one-way: what the detector learns about the target videos never returns to the LVLM. MuST-VAD extends the one-way transfer into a bidirectional learning loop. In this loop, the latest detector predictions supervise the LVLM adaptation, and the adapted LVLM returns updated representations that retrain the detector; the two models alternate these updates over small video groups. Both models train on detector-selected key clips, while confidence weighting and annotation-anchored question answering keep the exchanged supervision reliable. On UCF-Crime, our mutual learning improves the one-pass transfer baseline from 88.15% to 88.63% AUROC and from 37.25% to 42.46% average precision (AP), outperforming the state-of-the-art method in AP by 4.13 points.

---


### 77. [ReGraph: Learning to Generate Recipe Graphs from Food Images](https://arxiv.org/abs/2608.06917)

**<font color=#1a73e8>作者：</font>** Guoshan Liu, Bin Zhu, Pengkun Jiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent Large Multimodal Models (LMMs) have achieved impressive performance in recipe generation from food this http URL, cooking is a structured transformation process in which ingredients undergo state changes through ordered actions,while free-form recipe language leaves the corresponding entities, intermediate states, and dependencies largely implicit and entangled.A graph representation makes this procedural knowledge explicit and compositional, providing a structured basis for assessing whether model outputs encode process-level knowledge rather than merely presenting plausible textual descriptions. To address this limitation, we present ReGraph, a large-scale recipe graph dataset that represents ingredients, cooking actions, and tools as entities, uses entity attributes to describe ingredient state changes, and employs typed relations to encode manipulation targets, destinations, and procedural ordering. ReGraph further incorporates explicit Recipe Reasoning Chain-of-Thought (RR-CoT) traces, providing auxiliary supervision for procedural decomposition and structured graph generation. Building on ReGraph, we propose Recipe Graph Learning (RGL), a two-stage framework that enables LMMs to generate a plausible fine-grained cooking workflow from a food image in the form of a structured recipe graph. Under a deterministic, schema-aware matching protocol, our experiments reveal a substantial gap between text-generation quality and recoverable procedural structure: recipes produced by existing approaches achieve competitive text-generation scores yet yield limited reference-aligned entity and relation structure under the ReGraph schema. In contrast, across two representative LMM backbones, RGL consistently improves the generation of cooking entities and procedural relations, while our analysis further shows that fine-grained ingredient-state capture remains the most challenging dimension.

---


### 78. [Deal Me Maybe: The Role of Emotions in Multi-Agent Negotiation](https://arxiv.org/abs/2608.06922)

**<font color=#1a73e8>作者：</font>** Massimiliano Luca, Apoorva Singh, Bruno Lepri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Negotiation is a demanding social task for LLM agents, requiring strategic reasoning, persuasion, and interpersonal adaptation. Yet existing benchmarks often treat agents as emotionally neutral, overlooking a key driver of human bargaining behavior. We study how prompt-conditioned emotions affect LLM-based price negotiation. In a controlled framework, buyer and seller agents are independently assigned one of six emotional states and negotiate over 350 real consumer products under two budget conditions. Across 36 emotion-pair settings and five widely used LLMs, we find that emotions strongly shape outcomes. Angry buyers almost never reach agreement (0.39% deal rate), while happy buyers agree most often (28.91%), but obtain worse prices than fearful buyers. Emotion effects are role-dependent: buyer emotion mainly drives acceptance and rejection, whereas seller emotion shapes concession dynamics. These effects influence not only language, but also termination behavior and price trajectories, raising concerns for emotion-conditioned agents in commerce.

---


### 79. [TRIBE: Predicting Team Performance via Communication Behavior Ensembles](https://arxiv.org/abs/2608.06926)

**<font color=#1a73e8>作者：</font>** Ali Jalal-Kamali, Nikolos Gurney, David V. Pynadath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing autonomous agents that effectively assist human teams hinges on understanding team dynamics, often without task specific knowledge. We present TRIBE, a domain independent approach that reveals team behavioral dynamics invisible to traditional performance metrics. We show that communication patterns can categorize teams into performance predictive behavioral tribes, as early as 10% into the task, enabling timely interventions. We test TRIBE on four diverse datasets and demonstrate that communication patterns predict team performance while the prediction strength varies by the degree a task structure allows for behavioral freedom. Our temporal analysis reveals that AI agents significantly alter team behavioral trajectories while human advisors align with natural dynamics, and that teams maintain behavioral flexibility throughout collaboration. Further, we compare TRIBE to Llama and optimize the pipeline, achieving significant speedup with performance improvement.

---


### 80. [AVCap: Reinforcing Audio-Video Joint Caption with Detail-Aware Reward](https://arxiv.org/abs/2608.06930)

**<font color=#1a73e8>作者：</font>** Mingyang Wu, Kaituo Feng, Bohao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detailed audio-video joint captioning is essential for multimodal video understanding and generation. However, prior works are constrained by three main limitations: (1) the scarcity of high-quality public datasets with fine-grained audio-visual joint captions; (2) reinforcement-learning methods that rely on coarse reward signals; and (3) the lack of a benchmark and metric for evaluating detailed audiovisual captions at the atomic level. To address these challenges, we propose: (1) AVCap-100K, a high-quality dataset of 100K temporally aligned, detail-rich audio-video captions; (2) AVCap, a model optimized via Detail-Aware GRPO (Da-GRPO) that achieves state-of-the-art performance among open-source models and matches or surpasses proprietary models on several evaluations; and (3) AVCap-Bench and AVCap-Score, a specialized benchmark and metric for evaluating atomic-level details in audiovisual captions. Our code, models, and datasets are available at this https URL.

---


### 81. [Science Edge Evaluation: SEE the Missing Step Toward Real Scientific Discovery](https://arxiv.org/abs/2608.06931)

**<font color=#1a73e8>作者：</font>** Taolin Han, Yuchen Zhang, Jinghang Wang 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly involved in scientific discovery, yet it remains unclear whether they can support complex real laboratory science. Here we introduce Science Edge Evaluation (SEE), a multimodal benchmark of expert-curated questions grounded in peer-reviewed literature and experimental practice in chemistry, biology, and materials science. Evaluation of 19 multimodal large language models (MLLMs) shows that even the best-performing model reaches only 48.7% accuracy. Moreover, general-purpose models outperform science-specialized models on average. In the visual-agent evaluation, the use of tools increases the best accuracy to 52.7%. Tool use can expand the information available to models, but more information does not necessarily lead to reliable scientific reasoning. The key challenge is whether models can manage tool-derived information within the boundaries of the original experimental evidence. Together, these findings reveal that current MLLMs still cannot reliably make justified and evidence-bounded inferences from experimental results, which is an essential capability in real scientific discovery. Bridging this gap requires MLLMs to transition from explaining established scientific concepts to deriving novel and evidence-based insights from experimental data.

---


### 82. [Ask-E: An Environment for Calibrated Question Generation](https://arxiv.org/abs/2608.06933)

**<font color=#1a73e8>作者：</font>** Sarah Pratt, Jae Sung Park, Scott Geng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Today, we improve models by training and evaluating them on problems at the frontier of their abilities. Creating such problems is itself a demanding task, requiring the ability to probe model limits and generalize beyond existing question distributions. It also means placing problems at a precise difficulty level, which requires understanding what it takes to solve them. In short, generating problems calibrated to a model's current frontier demands capability beyond it, an increasingly burdensome constraint as models improve. Our key insight is that we can leverage this constraint to our advantage: a model that can generate problems consistently calibrated to a given frontier must possess capability beyond it. Accordingly, we present Ask-E, an environment that benchmarks and trains models on their ability to write questions at a given skill level, rather than answer them. Concretely, we define target skill levels as ranges bounded by the capabilities of two existing language models. A generated question is successfully calibrated if exactly one of the two models can solve it, placing it precisely within the target range and differentiating the capabilities of these models. Ask-E serves both as a benchmark and a training environment, where models generate problems calibrated to a variety of skill levels. We find that even frontier models achieve below 50% calibration on the benchmark, leaving significant headroom to measure future progress. We also show that training on this environment leads to improvements across a number of downstream math benchmarks even with no new math data, no interaction with stronger models, and no correctness-based reward.

---


### 83. [Debias in Text, Believe Your Eyes: Text-Anchored Cross-Modal Transfer for Visual Counter-Commonsense Reasoning](https://arxiv.org/abs/2608.06938)

**<font color=#1a73e8>作者：</font>** Chen Ling, Hanqian Li, Dongnan Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The visual reasoning ability of multimodal large language models (MLLMs) is crucial for downstream applications, particularly counter-commonsense reasoning, which requires models to reason beyond common assumptions. Recent studies mainly improve visual counter-commonsense reasoning by enhancing visual inputs, following the assumption that failures originate from insufficient visual grounding. However, our empirical analysis reveals that the bottleneck is not visual perception. MLLMs already capture the relevant visual evidence, and the correct answer exists in their decoding space. Instead, the shared language decoder resolves prior--evidence conflicts by favoring dominant language priors, especially for low-frequency factual scenarios. Motivated by this, we first propose a text-anchored data construction pipeline, whose core component, Fact-Frequency Distillation (FFD), estimates the prior strength of commonsense facts and distills verified counter-commonsense scenarios into a high-quality text corpus. Building upon this corpus, we introduce TACT, a text-anchored post-training framework that debiases the shared language decoder without requiring any visual training data. TACT routes evidence-following and prior-driven reasoning trajectories into different optimization stages, enabling the decoder to resolve prior--evidence conflicts. Across counter-commonsense visual benchmarks, TACT substantially improves visual reasoning while preserving general capabilities, demonstrating effective text-to-vision cross-modal transfer.

---


### 84. [Degradation-Aware Prompt Learning with Cross-Modal Compensation for Adverse Weather Removal](https://arxiv.org/abs/2608.06939)

**<font color=#1a73e8>作者：</font>** Wanshu Fan, Yunzhe Zhang, Yue Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse weather causes diverse and complex image degradations, severely compromising the reliability of computer vision systems. Existing all-in-one restoration models attempt to address multiple degradation types within a unified framework, but often lack explicit spatial and semantic modeling of degradation characteristics, limiting their adaptability to diverse weather conditions. To address this limitation, we propose a Degradation-Aware Cross-Modal Prompt Compensation Network (DCMPC-Net) that leverages cross-modal degradation cues from a pretrained vision-language model to condition restoration features within a unified backbone. Specifically, our DCMPC-Net mainly consists of the Cross-Modal Prompt Generator (CMPG), Prompt-Guided Attention Alignment Module (PGAAM), and Dual Feature Compensation Module (DFCM). The CMPG integrates textual embeddings with visual features to produce degradation-aware prompts that encode degradation-related semantic and contextual cues. These prompts are injected into the decoder via a PGAAM, which adaptively aligns semantic information with degraded regions to facilitate context-aware restoration. To further enhance structural fidelity, DFCM is introduced that disentangles degradation artifacts from scene structures, thereby improving the reconstruction of fine textures and detailed content. By integrating cross-modal semantic guidance with spatial alignment and structural enhancement, DCMPC-Net achieves robust and perceptually consistent restoration across diverse weather conditions. Extensive experiments show that DCMPC-Net outperforms state-of-the-art methods in both task-specific and unified settings, achieving superior accuracy and visual fidelity.

---


### 85. [Blind to the Pivotal Vote: Aggregate Independence Metrics Miss Where Verification Actually Helps](https://arxiv.org/abs/2608.06940)

**<font color=#1a73e8>作者：</font>** Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM judge panels are a standard evaluation tool, but prior work reports highly correlated panel errors: nine judges provide roughly the effective information of two independent ones, and aggregation closes only a small fraction of the gap. A natural remedy--a signal from a different evidence source, e.g., executing a test suite--produced no distinguishable change in the panel's effective-vote count at scale (-0.04, 95\% CI [-0.10, +0.02]). Aggregate dependence and conditional decision utility are different questions. Elementary majority arithmetic fixes the affected set for single-ballot substitution: only decisions with a one-vote margin can change. The empirical question is whether panel error rates rise and useful substitutions concentrate there. They do: the entire accuracy gain concentrates on these pivotal queries, where it is large (+10.4 to +23.3 percentage points across three headline configurations), and is exactly zero elsewhere. We confirm the pattern across three code benchmarks and four panel sizes (a 9-judge extension and 56 dependent subsampling checks, gain +6.5 to +16.1 percentage points). On HumanEval+/MBPP+, a majority-side replacement rule raises overall accuracy from 82.44\% to 85.62\% while invoking the signal on 16.2\% of queries; signal-only remains stronger at 87.60\%. Thus population-level dependence diagnostics and margin-stratified utility are complementary, and the affected-set characterization yields a call-reduction rule for any specified single-ballot substitution policy.

---


### 86. [LMM Modality Transfer: A Pre-requisite for Autonomous GIS Agents](https://arxiv.org/abs/2608.06948)

**<font color=#1a73e8>作者：</font>** Ivan Majic, Zexian Huang, Franziska Hübl 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI models are becoming increasingly adept at understanding and processing spatial information, thereby facilitating agentic problem-solving in spatial tasks and workflows. However, most of the research on their spatial capabilities (e.g., spatial reasoning) has focused on the textual modality as input and output. This contrasts with the human approach to GIS workflows, where text and visual modalities are often used together, interchangeably, and in a complementary manner. Thus, to truly achieve an automated GIS analysis pipeline or carry out human-designed GIS workflows, AI models --- Large Multimodal Models (LMMs) in particular --- need to be able to seamlessly transition between image- and text-based modalities that are traditionally used in such workflows. We present a modality transfer task that (1) asks an LMM to first describe an input image of colored squares in a regular grid, and (2) asks a new LMM instance to re-generate an image of the original spatial scene using the textual description output by the former model. This task quantifies the ability of LMMs to transfer spatial information between image and text modalities. Ultimately, by examining the modality transfer capability of LMMs through the lens of spatial information theory, this work highlights a critical bottleneck: achieving strong and robust geospatial understanding in LMMs requires rigorous, multi-modal alignment. Our results indicate that recent LMMs (here from OpenAI) still struggle with modality transfer, when tasked with re-generating an image of a simple spatial grid of color squares.

---


### 87. [Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity Constraints](https://arxiv.org/abs/2608.06949)

**<font color=#1a73e8>作者：</font>** Paul-Peter Arslan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prior benchmarking work has shown that a single large language model (LLM), forced to make life-or-death resource-allocation decisions, exhibits measurable demographic bias. Real deployments, however, rarely use a single agent: they use pipelines, with review steps meant to catch exactly this kind of failure. We study what happens to bias when the same decision is distributed across a role-differentiated multi-agent pipeline (assessment, allocation, independent audit) instead of made and checked by one model alone. Using a synthetic disaster-triage simulator with paired cases that are clinically identical except for one demographic attribute, we run 192 episodes (2,304 resolved case pairs) on GPT-4o-mini comparing a single-agent control condition to a nine-agent pipeline under three independently varied pressure dimensions. We find no measurable difference in how often biased outcomes occur between the two conditions (6.9% vs. 6.1%, p = 0.498). We do find a large and significant effect of audit capacity on whether bias is caught: 30.0% of biased outcomes go entirely undetected, rising to 43.8% when the auditor is overloaded and falling to 18.4% when it is not. Decomposing this effect shows it is driven almost entirely by coverage (whether a case is reviewed at all, which collapses from 100.0% to 65.6% under load, p < 0.001) rather than by degraded judgment on the cases that are reviewed (81.6% vs. 85.7%, p = 1.000, direction reversed). A follow-up experiment shows that reordering the audit queue by estimated risk, rather than first-come-first-served, recovers most of the lost coverage under the same capacity constraint (65.6% to 91.7%, p = 0.028). We discuss the implications for any system that adds independent oversight to an LLM agent pipeline under resource constraints, and report the study's limitations honestly: one model, modest sample sizes, and no adversarial replication.

---


### 88. [Explicit, Not Longer: What Makes Epistemic Stance Survive Memory Compression](https://arxiv.org/abs/2608.06953)

**<font color=#1a73e8>作者：</font>** Alex Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent memory systems compress what they store, and compression is built to drop qualifiers, so a claim's epistemic standing tends not to survive being written to memory. We ask what governs whether it does. Matched notes carry the identical claim and identical stance and differ only in where that stance sits; one model compresses both under the same budget among the same filler notes, and a blind reader that never sees the condition scores the result. Across 60 claims in seven registers, writing the stance as a labelled field rather than a bracketed aside raises retention by about 15 points on two models (37 claims to 2 on one, 30 to 8 on the other; permutation p=0.00005), and a pre-registered replication on Haiku, its prediction and decision rule committed before the run, gives +15.6 points, 38 claims to 1. Ablating the format on both models gives the same net effect from different parts: labels help on both (+9.7 and +12.8) and length helps on neither, but wording the stance as a full sentence is the largest component on one model (+12.5) and worth nothing on the other (+0.6). Either model alone would have licensed a confident and different mechanism, so we claim only the intersection: make the stance explicit, not merely longer, and expect the best way of being explicit to depend on the model. A deterministic readout with no model reproduces the two-cell direction and five of seven ablation contrasts, but not length or labels, which we therefore do not claim on one instrument. Fifty hand labels (kappa=0.75) agree on direction; we print their seven disagreements in full. We also report nine withdrawn claims, three of them former title claims of this paper.

---


### 89. [Critical Acclaim Orientation in Large Language Models: Evidence from Film Preference Elicitation](https://arxiv.org/abs/2608.06955)

**<font color=#1a73e8>作者：</font>** Jonghyun Jee, Aaron Shaw  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are trained on corpora that contain expressions of human judgment about films, books, music, and more. Yet whether LLMs systematically reproduce evaluative hierarchies remains unclear. Prior research on cultural bias in LLMs suggests competing expectations: models may mirror the popularity signals of internet texts, or may reproduce forms of prestige embedded in critical discourse. We probe this question through a study of film evaluations with eight models from four families (Anthropic, OpenAI, Alibaba, and Mistral), using a 200-film benchmark partitioned into critically acclaimed, commercially successful, and dual-legitimacy (critical acclaim + commercial success) films. Across 20,000 pairwise forced-choice comparisons per model analyzed with Bradley--Terry estimation, we observe a consistent critical acclaim orientation with all models: critically acclaimed yet commercially obscure films are selected over commercially successful yet critically unrecognized ones. This pattern grows with model scale within each family. In addition, nested OLS regression analyses show that evaluative orientation, public visibility, and popular reception distinctly help explain preferences. Adjusting for public visibility reverses the models' preference for dual-legitimacy films over critical acclaim-only films, while additionally accounting for popular reception attenuates much of the disadvantage of films with commercial success only. Finally, evaluative and recommendation-oriented prompt framings produce divergent rankings, suggesting that critical acclaim orientation may manifest indirectly in real-world LLM deployments.

---


### 90. [Summarize First, Download Later: Onboard VLMs for Bandwidth-Efficient Earth Observation](https://arxiv.org/abs/2608.06959)

**<font color=#1a73e8>作者：</font>** Junghwan Park, Sangcheol Sim, Woojin Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Earth observation (EO) satellites carry increasingly advanced sensors that produce vast volumes of high-resolution, multispectral data, yet downlink capacity remains a critical bottleneck -- often causing significant latency or the loss of valuable observations within limited contact windows. We propose a "Summarize First, Download Later" paradigm that exploits recent advances in onboard edge computing and Vision-Language Models (VLMs). Rather than indiscriminately downlinking raw imagery, the system follows a three-phase interaction protocol: the satellite first transmits concise natural language summaries generated by a quantized onboard VLM; ground operators then issue targeted Visual Question Answering (VQA) queries to verify scene relevance (e.g., wildfires or maritime anomalies); and full-resolution images are downloaded only when critical information is confirmed. This transforms the downlink from passive bulk transfer into an active, semantics-aware dialogue. We implement and evaluate the system on a resource-constrained NVIDIA Jetson platform, and experiments on diverse remote sensing scenes show that the proposed strategy substantially reduces bandwidth consumption while accelerating time-to-insight for time-sensitive missions.

---


### 91. [CAi Copilot: Reducing Operational Workload in Molecular Design through Intent-Driven Agentic Workflows](https://arxiv.org/abs/2608.06961)

**<font color=#1a73e8>作者：</font>** Zhu Wang, Jiangyu Chen, Yingjun Shang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early-stage molecular design is an iterative process, not just a task of generating molecules. Researchers turn broad goals into design strategies, refine candidates, assess many properties, and gather evidence before synthesis and tests. AI methods can generate molecules, optimize several goals, predict properties, dock compounds, and account for synthesis. Yet these functions are spread across specialized tools. Experts must still coordinate each step, judge interim results, and integrate evidence. The central challenge is thus to turn research intent into adaptive, traceable runs grounded in scientific tools. We cast this challenge as intent-to-evidence molecular design workflow execution and present CAi Copilot, an expert-oriented agent with three linked layers. The Research Interface Layer turns intent into an executable plan. The Agent Reasoning Layer uses interim results to guide each run. The Execution Substrate supplies molecular tools, metrics, reusable utilities, and backend services. Across 45 tasks, CAi achieves the strongest overall performance, with an outcome score of 84.59, exceeding the next-best result by 18.07 points. Additional benchmarks test how CAi coordinates generation, screening, and multi-criteria evaluation, while exposing limits in long-horizon execution. These results show that CAi turns broad molecular-design intent into transparent, traceable workflows that connect interim decisions to candidate-level evidence.

---


### 92. [Can Language Models Imagine Without Seeing? Ekphrasis: Measuring Visual Creative Ideation in Text-Only LLMs](https://arxiv.org/abs/2608.06967)

**<font color=#1a73e8>作者：</font>** Hongyu Luo, He Wang, Huihao Jing 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluations do not isolate whether text-only language models can originate visual concepts before image generation. Fluent visual prose can hide visual-plan failures: an answer may appear creative while repeating familiar visual clichés or failing to specify a renderable scene. We define Visual Creative Ideation (VCI) as the ability to produce textual visual plans that are useful, expressive, and population-novel, and introduce Ekphrasis, a 400-task benchmark spanning Abstraction, Combination, Transformation, and Adaptation. Ekphrasis scores anonymized pairwise comparisons with dimension-specific checklists, aggregates preferences with Bradley-Terry models, and uses Typed Idea Graphs to convert task-specific population clichés into novelty references. Across 14 language models, VCI separates usefulness, expressiveness, and novelty rather than reducing to fluency: strong models achieve similar overall scores through different profiles, and useful plans can remain visually clichéd. A cross-modal grounding study further shows that text-level VCI ordering largely survives faithful rendering and blind image-level preference judgment, supporting Ekphrasis as a measure of visual ideation beyond prose quality.

---


### 93. [Finding Usable Weight Mechanisms with Tiled SVD](https://arxiv.org/abs/2608.06969)

**<font color=#1a73e8>作者：</font>** Ash Manvi, Samreena Tajreen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The dominant approach to mechanistic interpretability trains proxy dictionaries such as sparse autoencoders and labels features from max-activating text. The best such atlases identify con- cepts, but that identity lives in the learned dictionary rather than in the network weights them- selves. We propose extracting mechanism mounts directly from linear sites by column-tiled SVD: each mount is a triple (v,u,{\sigma}) read as trigger, write, and strength. Identity is the weight rule. We evaluate mounts with a pre-registered suite judged on full-write energy lift rather than tile-local lift. On Gemma-2-2B with WikiText-2 (16,384-token subsample), all seven linear maps are scored: residual writes (this http URL, attn.o) receive full A/B/C with steer after post-sublayer RMSNorm and pass 52/52 site-layers; other maps receive A/B only (this http URL this http URL 26/26 each). Aggregate: 182/182 GO. We release library code, the corpus builder, the experiment entrypoint, and unit tests.

---


### 94. [Generative Embedding Benchmark: How Much Information Survives in a Dense Embedding?](https://arxiv.org/abs/2608.06972)

**<font color=#1a73e8>作者：</font>** Yun Li, Biao Yang, Peixi Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embeddings have emerged as a standard representational interface linking foundation models with downstream systems. Most embedding benchmarks assess representations through discriminative tasks or geometric criteria centered on separability in embedding space. However, strong performance on such evaluations does not establish whether content compressed into an embedding remains accessible to a downstream generator. To address this gap, we introduce the Generative Embedding Benchmark (GEB), in which a decoder answers questions using only a frozen embedding and question text, without access to the original image or intermediate visual features. Answer quality under this readout measures generative information: the answer-relevant content recoverable from an embedding. GEB includes a curated visual-question-answering dataset with a 1,800-item development split and a held-out 900-item test split covering natural images, scene text, and visual documents. Using a common decoder and training recipe, we evaluate seven public embedding models in visual-only and vision-language joint modes. On the test set, visual-only scores range from 28.25 to 33.21; with image-question joint encoding, all five VLM-based embedding models score higher, and the best reaches 65.56. Matched embeddings also outperform text-only inputs, zero embeddings, and shuffled embeddings. Natural-image information is much easier to recover than scene text or visual-document information, while a Qwen3-VL-2B reference with access to the original image reaches 84.30. Together, these results show that generative readout exposes information bottlenecks that separability-based evaluation does not capture.

---


### 95. [PHASE-Tree: Modeling Character-State Evolution in Long-Horizon Role-Playing Dialogue](https://arxiv.org/abs/2608.06975)

**<font color=#1a73e8>作者：</font>** Bo Tang, Jianan Yang, Junyi Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon role-playing demands that characters remain recognizable as they evolve with the narrative. Yet existing work falls short on two fronts: representations are typically static profiles that cannot be updated locally without destabilizing unchanged traits, and benchmarks mainly test persona preservation and memory recall rather than whether a model speaks from a character's currently evolved state. We address both. PHASE-Tree is a multi-timescale character-state tree with an immutable identity root and mutable persona, session, and moment layers, making each mutable field an addressable target for localized within- and cross-episode updates. It conditions generation through explicit textual provision or implicit parametric adaptation. To measure evolved-state generation, we introduce LongEvoRoleBench, which pairs four long-dialogue corpora for cross-episode evolution with four short-dialogue corpora as within-scene state-tracking checks, under a unified next-utterance protocol. On the long-dialogue core, textual PHASE-Tree ranks first in 11 of 12 dataset-metric cells against internal variants and all 12 cells against external textual baselines, improving character-level, semantic, and embedding scores by 19.7%, 12.4%, and 15.1% respectively. In a blinded 200-response study, human ratings correlate with the GPT-4.1 judge (Pearson r= 0.65); on descriptive n= 10 PT and NR prompt subsets, the Overall difference is +0.20. The long-dialogue Sem advantage persists across LLM judges and generation backbones.

---


### 96. [Confirming Our Biases? Evaluating the Capabilities, Risks, and Societal Impact of Large Language Models](https://arxiv.org/abs/2608.06977)

**<font color=#1a73e8>作者：</font>** Mudar Adas, Polina Tsvilodub, Michael Franke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> It is well established that large language models (LLMs) are sensitive to prompt framing, reflecting patterns in their training data or prior prompts. In this study, we investigate the extent to which LLMs reinforce users biases expressed in the prompts and examine the boundary between implicit framing effects and explicit prompt manipulation. Specifically, we evaluate how susceptible LLMs are to direct and suggestive prompts that encourage models to support or challenge particular positions.
We evaluate six LLMs using 160 distinct prompts spanning ten topics across opinion-based and factual domains. The prompts systematically vary in prompting strategy, support versus challenge instructions, prompt polarity, users' expressed beliefs, and topic domain, spanning both opinion-based and factual questions. Our results show that LLMs systematically adapt their responses to align with prompt framing, even in factual contexts. This suggests that prompt framing can outweigh factual consistency in model responses. Overall, our findings delineate the extent and boundaries of LLM manipulability. Furthermore, the results imply that LLMs can reinforce subtle user biases and are susceptible to explicit prompt manipulation even in domains where responses should remain factually stable.

---


### 97. [GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge Base](https://arxiv.org/abs/2608.06992)

**<font color=#1a73e8>作者：</font>** Yujia Hu, Tuan-Phong Nguyen, Simon Razniewski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a web demo for exploring a large-scale disambiguated knowledge base (KB) materialized from a large language model (LLM). GPTKB 2.0 contains 38.4M triples over 1.6M canonical entities, together with 207.6K consolidated relations and 66K consolidated classes. Unlike prior LLM-derived knowledge bases that largely identify entities by surface strings, GPTKB 2.0 performs context-guided disambiguation during recursive KB construction, separating homonyms and merging synonymous mentions as facts are elicited. The demo makes this process inspectable: users can browse entities, follow links across the KB, and audit the provenance of individual facts, including surface forms, candidate matches, source triples, and disambiguation decisions. The interface further supports structured SPARQL queries, natural-language questions translated to SPARQL, and entity linking from user-provided text to canonical GPTKB 2.0 entries. GPTKB 2.0 is available at this https URL, with the full KB downloadable for offline use.

---


### 98. [Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression](https://arxiv.org/abs/2608.07001)

**<font color=#1a73e8>作者：</font>** Haolin Tian, Yuzhe Liu, Tonghan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck. Existing KV cache compression methods rely on predefined, fixed compression rules and are typically developed around either token eviction or merging. As a result, cache resources can neither flow freely across layers, heads, and context slots, nor be jointly allocated to balance local resolution and information coverage. Therefore, we propose GraceKV, a global approach for the allocation of resolution and coverage in KV cache compression, and formulate the compression process as a global resource allocation problem under a fixed cache budget. GraceKV treats each layer-KV head-slot combination as an atomic unit and builds a prototype tree. Leaf nodes correspond to token-level KV entries, while each internal node uses a single prototype to compress the KV space covered by its children. A set of non-overlapping nodes in the tree forms the representation of an atomic unit. Adding the root of a new tree expands information coverage, whereas splitting a selected node improves local resolution. All candidate actions compete globally for a shared cache budget. Finally, the nodes retained across all trees form the compressed KV cache. This process adaptively determines the allocation of cache resources among atomic units globally and the balance between resolution and coverage. GraceKV requires no additional training, and the entire compression and inference process is performed on the GPU. Systematic experiments across diverse long-context tasks and compression ratios show that GraceKV ranks first in 24 of 32 settings and remains robust up to 128-fold compression. These results validate the effectiveness of global budget allocation in coordinating information coverage and local resolution.

---


### 99. [Does More Retrieved Evidence Help Visual Retrieval-Augmented Generation with Diffusion Language Models?](https://arxiv.org/abs/2608.07006)

**<font color=#1a73e8>作者：</font>** Jiankun Wang, Yisen Gao, Ziwei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Visual retrieval-augmented generation (RAG) commonly expands the retrieved evidence set to improve answer-page coverage, implicitly assuming that all available evidence should be passed to the generator. We show that this assumption does not hold for diffusion language models (DLMs): retrieving more pages increases answer-page recall, whereas unconditionally passing all retrieved pages to the generator often reduces answer accuracy, primarily because of semantic conflict. A latent-source analysis explains this mismatch through source-coherence loss in parallel denoising, where position-wise proposals can combine incompatible visual sources into unsupported answers. We further find that such interference is already visible in the first-step answer-block distribution, making it possible to assess evidence before decoding. To preserve retrieval coverage while limiting harmful visual exposure, we propose the Entropy-Based Candidate Filter (ECF), a training-free evidence-admission framework. To reduce irrelevant content within individual candidates, ECF constructs multi-granularity evidence units; to identify beneficial additional evidence, it uses blank-controlled block confidence and retrieval rank to determine whether and which candidate should enter the final context. Across three multimodal DLMs and five visual QA benchmarks, ECF improves answer accuracy by 2.62 percentage points on average over the strongest fixed top-$k$ input and, with LLaDA2.0-Uni, by 2.37 percentage points on average over the best competing training-free result for each dataset. These results show that broader retrieval benefits visual DLM-RAG through selective evidence admission rather than unconditional evidence expansion. Code is publicly available at this https URL.

---


### 100. [Stable Curves, Unstable Items: Item-Level Scaling Heterogeneity in Video LLMs](https://arxiv.org/abs/2608.07014)

**<font color=#1a73e8>作者：</font>** Wenzhang Sun, Chunfeng Wang, Xiangchen Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aggregate scaling curves suggest that Video LLMs improve smoothly or saturate as visual budgets grow. We show that this view can conceal large, opposing changes at the item level. We represent each frozen model--item pair by its response trajectory under controlled visual budgets and derive matched-grid measures of configuration complementarity, harmful transitions, and text overwrite. Across five open Video LLMs from three architecture families, four multiple-choice benchmark splits, open-ended QA and summarization, and fixed-history dialogue generation, no single budget serves all items. On the four-model matched MCQA grid, item-level oracle headroom spans $8.8$--$18.9$ accuracy points and $12.5$--$25.5\%$ of items are correct at a lower budget but wrong at a higher one. Task-appropriate continuous metrics show the same complementarity beyond multiple choice: Token-F1 oracle gaps are $2.7$--$3.7$ score points on MLVU generation and $3.8$--$4.8$ points on AVSD current-turn generation, even when mean quality improves with budget. The effect persists across frame count, spatial resolution, sampling policy, temporal--spatial allocation, and independently executed raw-video and cached pipelines, with per-item rates and membership tracking protocol choices. A controlled sampling intervention recovers $29.0\%$ of terminal regressions, and a structured frame audit identifies several recurring evidence pathways. We release per-item trajectories, protocol provenance, derived annotations, and reproducible analysis code as an auditing artifact. A confidence cascade matches fixed-$128f$ accuracy while reducing average shared frame cost by $31.7\%$, illustrating one operational use of the response matrix.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-170](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

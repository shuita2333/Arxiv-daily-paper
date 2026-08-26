# 🧠 大模型相关研究 | 2026年08月27日

> 本类共 **190** 篇论文：已确认 **178** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-190](./part-04.md)

---

### 51. [HAP: Head-Adaptive Visual Token Pruning via Cross-Modal Alignment](https://arxiv.org/abs/2608.23921)

**<font color=#1a73e8>作者：</font>** Yuanhao Sun, Huawei Ji, Yuan Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Vision-Language Models encode high-resolution images into long visual token sequences, incurring prohibitive prefill costs. To compress them, existing methods score each visual token by averaging text-to-visual attention uniformly across all heads, which assumes every head matches the query. However, our empirical analysis shows that misaligned heads dominate the average, amplifying background tokens and drowning out fine-grained cues.
To address this, we propose PAQ (Prompt-Grounded Attention Quality), a metric quantifying how well each head aligns the prompt with image regions. Built on PAQ, our pruning proceeds in three stages. Given a target FLOPs budget, we first partition the transformer layers into groups and allocate a visual token budget to each. Within each group, we then aggregate per-head attention maps via PAQ-weighted softmax into a group-level matrix. Finally, we score visual tokens by this matrix's magnitude and retain the allocated budget per group. By weighting heads with PAQ, our method scores tokens by attention signals that more faithfully reflect prompt relevance, rather than diluting them through uniform averaging.
Across 18 benchmarks, our method delivers state-of-the-art trade-offs. Specifically, on LLaVA-1.5-7B (9 tasks), retaining only \textbf{5.6\%} tokens preserves \textbf{99.1\%} of the original performance, surpassing the strongest baseline AutoPrune by 4.2 points. Code is available in this https URL.

---


### 52. [Data Mixing as Mixture Experiment: Response Surface Methodology and Optimal Design for Large Language Model Pretraining](https://arxiv.org/abs/2608.23922)

**<font color=#1a73e8>作者：</font>** Yicheng Mao, Hongru Du  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data mixing is a central design problem in large language model pretraining: given a fixed token budget, practitioners must decide how much data to allocate to each domain. Recent proxy-based methods address this problem by training small models on candidate mixtures, fitting a response model, and using the response to select mixtures for larger-scale training. We show that this workflow has the structure of a classical mixture experiment. Under this view, data domains are mixture components, token shares are component proportions, proxy-training runs are experimental design points, and validation loss defines a response surface over the probability simplex. We develop this formulation using sparse second-order Scheffé response-surface models and construct model-robust $\mathcal{I}$-optimal designs for proxy data-mixing experiments. Using RegMix as an empirical case study, we demonstrate how the framework can both interpret observed mixture responses and design more efficient proxy experiments. The Scheffé analysis shows that domain value is strongly relational: several domains that are weak under additive effects become favourable through pairwise interactions, especially through combinations with web-derived text. The sparse Scheffé model preserves mixture rankings across model scales and remains competitive with a flexible machine-learning predictor while providing an explicit decomposition of additive and interaction effects. In a simulation study calibrated to observed proxy-training responses, model-robust $\mathcal{I}$-optimal designs recover the relevant mixture ordering after removing about 25\% of the original proxy runs. These results suggest that LLM data mixing should be treated not only as a prediction problem, but also as an experimental-design problem in which the proxy mixtures themselves can be chosen to improve statistical efficiency.

---


### 53. [RefineRank: Joint Box Refinement and Ranking for Surgical Spatio-Temporal Grounding](https://arxiv.org/abs/2608.23928)

**<font color=#1a73e8>作者：</font>** Linzhe Jiang, Jiayuan Huang, Changhao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical spatio-temporal grounding (STG) requires locating, at each video time specified by a procedural question, the object that the question asks about. Existing approaches face a trade-off: vision language models understand the question context but produce imprecise coordinates, whereas open-set detectors provide localized candidate boxes whose confidence does not reflect which box answers the question. We introduce RefineRank, which closes this gap at the candidate-box level. A compact trainable module, RefineNet, combines the language and regional features of a frozen medical vision language model with the proposals of a frozen open-set detector: it predicts a bounded coordinate correction and a quality score for every candidate box, and a fixed decoding rule returns the original or refined box with the highest score. On the MedVidBench Official Rankings (Verified), RefineRank records 0.421 STG mIoU, the highest displayed STG score, while its global multi-metric rank is 11. In a controlled evaluation on separate training and evaluation videos, coordinate correction raises the candidate oracle upper bound from 0.6772 to 0.7302, and ranking the joint pool of original and refined candidates by their RefineNet scores improves STG mIoU from 0.2719 to 0.4534, whereas separately trained selectors over the same pool reach at most 0.4186. These results show that a small box-level module can reconcile question understanding with precise localization without retraining either backbone. Code is available at [this https URL](this https URL).

---


### 54. [More Rejective, Not More Discriminative: The Unit of Verification in Pre-Execution LLM Oversight](https://arxiv.org/abs/2608.23941)

**<font color=#1a73e8>作者：</font>** Yuchen Han, Cheng Yan, Wuyang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pre-execution oversight is core to trusted monitoring in AI control: a fallible LLM monitor vets planned actions before irreversible execution. Over-blocking forfeits usefulness and pressures deployers to disable it. Every protocol must fix a unit of verification: how many actions one call reviews. Existing designs take the unit as given; its effect on fallible monitors is unmeasured. Natural traces cannot isolate it: review length co-varies with error type and position. Catch alone misleads: rejecting everything catches everything. Measuring this needs boundary variation alone and a matched clean control. We introduce the twin-prefix framework, which supplies both. Each gold plan yields a prefix with one injected, environment-accepted error and a clean twin differing in one write. Judging each pair at five nested lengths ties verdict changes to the unit alone. Discrimination is scored by pre-registered informedness, catch minus false rejection. Longer review raises catch; false rejection climbs in lockstep. Informedness peaks at one or two actions for all six judges in both domains: longer windows make zero-shot monitors more rejective, not more discriminative. Replaying withheld observations traces the failure largely to observation deprivation. Safety cases should state the unit and co-report the clean series. Our framework is the first controlled, pre-registered instrument for this choice and never reads catch alone. Our calibrated short unit recovers up to 0.95 informedness over eight-action review, and no tested label-blind policy consistently beats it.

---


### 55. [More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression for Memory-Bound LLM Serving](https://arxiv.org/abs/2608.23962)

**<font color=#1a73e8>作者：</font>** Srikanta Datta Tumkur, Mehar Simhadri, Anshu Bansal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an LLM serving deployment runs out of KVcache room, there are two well-established ways out. Tensor parallelism shards the weights and the KV cache across two, four, or eight devices, buying memory headroom at the price of an all-reduce on every layer and a hardware bill that grows with the device count. The algorithms community shrinks the cache in place, with KV quantisation and eviction keeping a single GPU and spending a little quality instead. Compression papers report memory ratios, parallel-scaling papers report throughput curves, and almost nobody puts the two on the same cost axis. We place tensor-parallel configurations (degree 1 to 8) and KV-compressed configurations (16/8/4-bit, keep-ratios down to 0.25) on one costnormalised axis, cost per million tokens against latency, using a profiled simulator calibrated on A100, A40, and H100 hardware, and we go looking for the cost-equivalence crossover. We do not find one. Across two models (Llama-2 at 7B and 70B), three GPU types, and every level of memory relief we could construct, compression is cheaper by 1.20x to 2.00x. A 7B model on an 80 GB device cannot exhaust its KV budget within its own context window, and the boundary that decides between the strategies is model size relative to device memory, at roughly 36B parameters for an 80 GB card. Below that wall, compression dominates and extra GPUs are largely wasted spend; above it, tensor parallelism stops being a choice and becomes an entry ticket: Llama-2-70B is infeasible on one A100 at any KV setting, because the binding resource is weights, which KV compression does not touch. Tensor parallelism is the only lever that improves latency (compression makes per-token latency worse, by 8 to 93%, through batching contention), while compression is the only lever that multiplies capacity per dollar (16.5x, against 1.21x for an eightfold spend on GPUs).

---


### 56. [RAGSentinel: Certifiable Geometric Consensus for Robust Retrieval-Augmented Generation](https://arxiv.org/abs/2608.23965)

**<font color=#1a73e8>作者：</font>** Yueyang Quan, Anjun Gao, Yufei Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) improves the factuality of large language models by grounding responses in external documents, but it also exposes a critical security vulnerability: adversarial documents injected into the knowledge database can enter the context window and steer the model toward targeted incorrect answers. Existing post-retrieval defenses rely on instruction following, parametric knowledge, or text-level consistency, all of which can be imitated or optimized against by adaptive attackers. We propose RAGSentinel, a training-free, label-free defense for black-box RAG systems. RAGSentinel uses a surrogate encoder to measure query-conditioned hidden-state shifts induced by retrieved documents, removes shared topic directions, and filters poisoned documents as geometric outliers from a robust majority consensus. We prove that, under an honest-majority assumption and a representation-level separation condition, RAGSentinel exactly recovers a poison-free majority-sized context. Experiments across three question-answering datasets, three LLM families, and multiple poisoning attacks show that RAGSentinel consistently achieves low attack success rates while preserving competitive accuracy and remaining effective against adaptive attacks with full pipeline knowledge.

---


### 57. [Who Chooses How Preferences Are Aggregated? Auditing Aggregation-Rule Authority in LLM-Based Group Recommendation](https://arxiv.org/abs/2608.23966)

**<font color=#1a73e8>作者：</font>** Yuxuan Du  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly make joint recommendations for users with conflicting preferences. However, when reasonable aggregation rules support different actions, a further question arises: who may choose how those preferences are combined? We study this interaction-level problem as aggregation-rule authority. Using synthetic preference profiles and profiles constructed from empirical ratings, we conduct a controlled behavioral audit of three LLMs under three authority conditions: unspecified, explicitly retained by users, and delegated to the model. In cases where two witness rules supported different actions, models almost never committed when users retained authority, but committed in every delegated case. All three models executed both witness rules perfectly when directly instructed. Yet when authority was unspecified or delegated, their aggregation-consistent outcome distributions differed across models and preference settings. Together, these results separate rule-execution capability from aggregation-rule authority: delegation assigns the model discretion to resolve the aggregation choice, but does not determine which collective outcome follows.

---


### 58. [When LLMs Slow Down: How Environmental Impacts Mediate University Students' LLM Usage](https://arxiv.org/abs/2608.23968)

**<font color=#1a73e8>作者：</font>** Hyeonwook Kim, Xuesi Chen, Alex Cabral 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being embedded into all facets of society, from search to education, industrial, and financial applications. These systems' carbon and water footprints raise important sustainability concerns, particularly with adoption rates exceeding 80% among university students, despite limited insight into the environmental impacts of individual usage. Eco-feedback interfaces offer a promising approach to encourage more sustainable behaviors, yet their role in shaping LLM users' sustainability awareness and decision-making remains underexplored. We design and deploy the interface that visualizes latency-carbon trade-offs during live LLM interactions. We study its use with undergraduate computer science students (N=89, ages 18-24), enrolled in a computing ethics course, providing an empirical look at how a technically sophisticated and values-oriented user population responds to sustainability-aware AI interfaces. We found that the likelihood of choosing the eco-feedback system significantly decreased as perceived response latency increased (p < .001), while users' willingness increased when they recognized the carbon-saving impacts (p < .01). Also, students with stronger eco-mindedness demonstrated higher baseline willingness to adopt lower-carbon modes and reported increased awareness of the environmental impacts of LLM use, though this effect diminished as latency increased. These results position eco-feedback interfaces as a promising sustainability intervention and highlight their potential as an educational opportunity to promote more sustainable LLM use among university students and beyond.

---


### 59. [Investigating Knowledge Transfer Across Interactive Dialogue Games](https://arxiv.org/abs/2608.23969)

**<font color=#1a73e8>作者：</font>** Filippo Momentè, Mir Nafis Sharear Shopnil, Andrea de Varda 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialogue games represent a challenging setting where complex cognitive skills are required to accomplish tasks while coordinating with other players. Considering that language represents an interface for both understanding the game rules and executing actions, it is reasonable to assume that training on a specific language game will enhance specific capabilities that might be relevant for other tasks as well. Motivated by this rationale, in this paper, we investigate how knowledge transfers across different dialogue games. We study transferability by finetuning LLM models on games from the clembench suite (Chalamalasetti et al., 2023) and performing two analyses: i) we derive a task-transferability graph using a binary integer optimization program from Zamir et al. (2018), using task performance as the main metric; and ii) we compute task vectors (Ilharco et al., 2022) for each game to study similarities across finetuned models and their task transferability. In our first analysis, we find that some games benefit more from transfer than finetuning, and that the visuospatial family (e.g., exploration games) transfers best. With our task vector analysis instead, we find that similarity-based approaches capture game-role relationships but almost no transferability patterns, suggesting that more complex metrics are required.

---


### 60. [Giraffe: A Mapping Architecture from Hidden Text Representations to Visual Embeddings for Efficient Graphic Design](https://arxiv.org/abs/2608.23970)

**<font color=#1a73e8>作者：</font>** Nejla Ghaboosi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have made significant progress in understanding and interpreting mul- timedia content. However, their ability to generate me- dia remains limited. Recent approaches have attempted to bridge this gap by translating the hidden representations of token sequences into the embedding space of visual models or directly into raw image data. However, these methods often represent each image using multiple specialised to- kens which significantly increases the input length. This be- comes a major limitation for tasks such as graphic design generation where the output typically involves a seamless blend of thousands of tokens across text, multiple images, and layout information. To address this challenge, a novel architecture is proposed that maps hidden token represen- tations to the embedding space of visual models, such as CLIP ViT-L/14, using a single [IMG] token per image. The architecture employs two shallow MLP blocks, each with a separate compression module followed by a shared expan- sion module, trained with six distinct loss functions. One block aids the other during training and is omitted during inference, resulting in a lightweight solution. Strong perfor- mance is demonstrated in both image-to-design and text-to- design generation tasks.

---


### 61. [Boot-and-Feedback Framework for Generalist-Expert Model Collaboration in Breast Ultrasound Diagnosis](https://arxiv.org/abs/2608.23974)

**<font color=#1a73e8>作者：</font>** Ming Cheng, Hongyu Sun, Zhaolin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast ultrasound (BUS) is widely used for breast cancer diagnosis yet remains operator-dependent. While deep learning shows promise, ensuring diagnostic reliability and interpretability is challenging. Recent Multimodal Large Language Models (MLLMs) often generate spurious descriptions due to limited domain knowledge, which mislead downstream expert models and compromise clinical validity. To address these challenges, we propose the Boot-and-Feedback (BooF) model collaboration framework for synergistic MLLM-expert interaction. Specifically, in the Boot Stage, the MLLM is guided by the BI-RADS lexicon and preliminary benign-malignant vision-expert predictions, enabling it to transfer general reasoning to BUS analysis while avoiding hallucinations. Subsequently, the Feedback Stage integrates these descriptions with visual features via a lightweight Attention-Gated Cross-Modality Fusion Module. This allows the expert to leverage textual feedback while adaptively filtering noise. Extensive experiments on multiple BUS datasets demonstrate that BooF substantially outperforms state-of-the-art methods in terms of diagnostic accuracy and interpretability.

---


### 62. [When Seeing Is Not Enough: Benchmarking Interactive Visual Grounding in LVLMs](https://arxiv.org/abs/2608.23978)

**<font color=#1a73e8>作者：</font>** Zhengxiang Wang, Owen Rambow  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual grounding is typically evaluated as a one-shot mapping from an informative referring expression to a visual target. This formulation misses a central property of real-world reference: target information is often incomplete, ambiguous, and established through interaction. We introduce a controlled evaluation framework for interactive visual grounding in large vision-language models (LVLMs), varying how much target information is provided upfront and how much must be acquired through dialogue. Across four human-grounded visual contexts and four interaction protocols, current LVLMs perform significantly below task-level human baselines. Interaction can help when follow-up questions refine or repair an initial target description. Performance is lowest when no initial description is provided and target information must be acquired through questions, indicating that proactive question-driven grounding remains difficult. LVLMs are also poorly calibrated, often reporting confidence that exceeds their empirical accuracy. Follow-up studies confirm these patterns across varied description sources (human versus AI), reasoning efforts, repeated interactions, description providers, and visual contexts. Overall, interactive visual grounding remains an important challenge, requiring visual matching, information seeking and synthesis.

---


### 63. [Memory Is Not Always Needed: Characterizing Conditional Memory in Scientific Reasoning](https://arxiv.org/abs/2608.23982)

**<font color=#1a73e8>作者：</font>** Zhen Bi, Xueshu Chen, Yan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific reasoning requires language models to retrieve specialized knowledge and incorporate it reliably into multi-step computation. Conditional memory provides an explicit lookup pathway that complements dense neural representations, but its usefulness is inherently input- and computation-dependent: retrieved information may repair missing scientific associations, yet it may also introduce distracting shortcuts or interfere with reasoning that the base model can already perform correctly. In this work, we systematically investigate when, where, and to what extent conditional memory should participate in scientific reasoning. We characterize the scientific knowledge boundary and controlled interventions on memory-enabled knowledge-circuit nodes. Based on these analyses, we propose a Knowledge Boundary-Aware Router that uses task-specific input proxies available before generation to determine whether memory is activated, which layer-stage nodes receive memory signals, and how strongly these signals contribute. Experiments on biological and chemical reasoning benchmarks, covering two backbone families and six task types, show that memory effects vary substantially across inputs, tasks, and injection locations. Compared with static and activation-rate-matched random routing, our approach more consistently preserves beneficial memory contributions while suppressing memory-induced regressions, establishing selective memory allocation as an important principle for reliable scientific reasoning.

---


### 64. [Diverse by Reasoning: Harnessing the Wisdom of LLM Crowds for Future Prediction](https://arxiv.org/abs/2608.24001)

**<font color=#1a73e8>作者：</font>** Nirupam Chetlapalli, Yiming Liao, Min-Chun Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for future prediction, motivating the use of multiple models as a wisdom-of-the-crowd mechanism. However, simply increasing crowd size does not guarantee effective diversity, as different LLMs may exhibit redundant behaviors. We propose a behavior-aware framework for constructing diverse LLM crowds. The framework characterizes models using their reasoning traces on independent development tasks, clusters models by behavioral similarity, and selects representatives for collective prediction. We evaluate 25 LLMs using seven development benchmarks for behavioral diversity modeling and two future-prediction benchmarks for evaluating diverse crowds' performance. Our results show that crowd composition can matter more than crowd size: a three-model medoid crowd based on K-means++ behavioral clustering outperforms conventional voting over all 25 models on both prediction benchmarks, while reducing model calls by 88% and inference cost by approximately 80%. The results further suggest that representative behavioral diversity, rather than simply maximizing diversity, is important for constructing effective LLM crowds

---


### 65. [AgentSpec: Speculative Decoding for Batch Inference of LLM Agents](https://arxiv.org/abs/2608.24004)

**<font color=#1a73e8>作者：</font>** Xin Wang, Ziming Miao, Yi Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agent applications often incur high response time. Speculative decoding is a promising solution to improve the inference efficiency of LLM agents without impacting generation quality. However, state-of-the-art speculative decoding algorithms exhibit substantial speed degradation under large batch sizes, limiting their effectiveness to deploy in real-world agent applications. In this work, we first present a systematic analysis of speculative decoding for LLM agents and identify two dominant factors of speedup degradation: high rejection rate of speculative tokens, and under-utilization of dynamic token budgets.B ased on these observations, we propose AgentSpec, a speculative decoding algorithm that addresses the limitations of existing methods for LLM agents. AgentSpec incorporates structure-isolated drafting that constrains speculation to semantically coherent segments of the agent workflow, reducing the drafts of irrelevant semantic paths and achieving an extremely low rejection rate. Moreover, AgentSpec adopts redundancy-aware budget allocation that exploits agent-level information to better utilize the dynamically-free token budget during the agent inference. We implement and evaluate AgentSpec on five different workloads and four different models from four different LLM families in vLLM. Our results demonstrate the superiority of AgentSpec over state-of-the-arts.

---


### 66. [Incorporating Cognitive Load and Knowledge Transfer for Multi-Domain Knowledge Tracing](https://arxiv.org/abs/2608.24005)

**<font color=#1a73e8>作者：</font>** Haotian Zhang, Shucun Wang, Jinze Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Tracing (KT) aims to assess students' dynamic knowledge states from their learning histories. While most existing KT methods focus on single-domain learning with notable success, real-world learning scenarios often involve multiple domains simultaneously, introducing two critical factors: 1) Cognitive load, arising from managing learning across domains in both temporal and knowledge dimensions. 2) Knowledge transfer, where knowledge states in one domain influence related states both within and across domains. In this paper, we focus on exploring these factors to improve students' knowledge state assessment in multi-domain learning scenarios and propose a novel method incorporating cognitive Load and knowledge Transfer for Multi-domain Knowledge Tracing (LT-MKT). Specifically, to bridge isolated domains, LT-MKT first integrates textual information from questions and their associated concepts to construct a Multi-domain Hierarchical Graph, leveraging the advanced representational capabilities of large language models (LLMs). Then, cross-domain features in both the temporal and knowledge dimensions are explicitly modeled to capture the effects of cognitive load. Additionally, a knowledge transfer module is designed to model the propagation of knowledge states within and across domains. By jointly modeling these factors, LT-MKT enables more accurate prediction of students' future performance. Finally, extensive experiments on real-world datasets demonstrate that our method achieves state-of-the-art performance.

---


### 67. [SAGE: From Direct Answering to Evidence-Grounded Inference for Chinese Ancient Document Understanding](https://arxiv.org/abs/2608.24011)

**<font color=#1a73e8>作者：</font>** Yuchuan Wu, Xuan Luo, Yinglian Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chinese ancient document understanding demands complex visual, linguistic, and historical reasoning. Current Large Vision-Language Models (LVLMs) typically rely on an opaque, single-pass generation paradigm, often producing overconfident and weakly grounded responses. To address this, we propose SAGE, an evidence-grounded multi-agent framework that reformulates Chinese ancient document understanding as evidence-grounded inference rather than direct answer generation. SAGE coordinates specialized agents for task-aware planning, tool-mediated evidence acquisition, claim-level verification, and bounded replanning under a constrained shared-state runtime. This design supports bounded evidence seeking, answer revision, and abstention when grounding is insufficient. Experiments on the AncientDoc benchmark show that SAGE consistently outperforms matched direct-answering baselines across three LVLM backbones. Remarkably, SAGE with Qwen3.5-9B surpasses much larger monolithic LVLMs on most evaluated metrics, highlighting the importance of structured, evidence-grounded inference beyond model scaling.

---


### 68. [WebMCP-Phalanx: Enforcing and Characterizing Trust Boundaries for Browser-Integrated LLM Agents](https://arxiv.org/abs/2608.24017)

**<font color=#1a73e8>作者：</font>** Lin-Fa Lee, YI-YU Chang, Kuo-Hui Yeh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The emerging W3C WebMCP proposal enables LLM agents to invoke tools exposed by web pages. In multi-party web environments, however, integrating agent execution into a browser security model centered on the Same-Origin Policy (SOP) leaves insufficient provenance and lifecycle guarantees for agent-accessible tools, creating three risks: subject-attribution spoofing, uncontrolled tool lifecycles, and semantic prompt injection. We propose WebMCP-Phalanx, a dual-layer agent runtime architecture. Its first layer provides a browser-native trust anchor that binds each tool to its registering principal through cryptographically protected capability credentials and propagates provenance labels throughout the tool lifecycle. Its second layer separates semantic inspection from privileged tool use. A Quarantine Agent (Q-LLM), without tool invocation authority, inspects tool metadata, outputs, and page-supplied content for prompt injection. Validated content is then forwarded to a Privileged Agent (P-LLM) for execution, while the Q-LLM's internal state remains hidden from page scripts. Empirical evaluation shows that the browser-native ownership mechanism reduces revocation and overwrite attack success from 100\% to 0\%. The dual-agent runtime blocks all 80 prompt-injection attempts embedded in tool descriptions and limits tool-return attacks to 2 successful cases out of 80. Across experiments, task utility remains statistically indistinguishable from the no-attack baseline. Under a white-box adaptive attacker, however, description-based filtering can be bypassed through malicious tool names invoked before inspection. This finding motivates a call-timing gate that delays tool invocation until all agent-visible tool metadata has been validated.

---


### 69. [Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding](https://arxiv.org/abs/2608.24024)

**<font color=#1a73e8>作者：</font>** Hyunho Kook, Junhyuk So, Tianyu Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Confidence-based voting aggregates parallel LLM rollouts by weighting each with internal signals such as token log probabilities, and has been actively studied for single-turn reasoning. However, modern LLMs increasingly act as multi-turn search agents that retrieve and condition on external documents. In this paper, we show that confidence-based voting transfers poorly to this multi-turn setting, and identify the underlying failure reason as copy inflation: when retrieved documents are appended to an agent's context, tokens copied from those documents receive systematically inflated log probabilities. This flattens confidence scores within each question and weakens the resulting weighted vote. To address this issue, we propose Retrieval-Grounded Voting (RGV), which scores each rollout by the lexical overlap between its final answer and the documents it retrieved. By computing the signal outside the contaminated context, RGV sidesteps both token log probabilities and additional LLM calls. Across four search-agent benchmarks and five LLMs, RGV consistently outperforms confidence-based voting, with gains of up to +5.4% accuracy and +35% on minority-correct questions, where the correct answer appears in only 1-2 of 8 rollouts.

---


### 70. [ChorusTIC: Training-Free Multivariate Time Series Classification via Chorus In-Context Learning](https://arxiv.org/abs/2608.24033)

**<font color=#1a73e8>作者：</font>** Juntao Fang, Shifeng Xie, Ruichu Cai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series classification underpins applications in healthcare, sensing, and industrial monitoring. Although time series foundation models support forecasting and transferable representation learning, classification still typically requires fitting a task-specific classifier on each target dataset, while individual channels of multivariate inputs are often encoded independently. We introduce ChorusTIC, a classification-native foundation model for in-context classification across heterogeneous channel configurations without target-task parameter updates. ChorusTIC combines episode-consistent Random Subchannel Slot Concatenation with a shared dual-axis encoder to model temporal and cross-channel interactions and map variable channel configurations into a fixed-width representation independent of the original channel count. It then calibrates feature axes using context-derived distributions and predicts query labels through leakage-protected in-context learning. We pretrain ChorusTIC solely on synthetic labeled episodes comprising context and query sets that share a task background, with classes distinguished by sparse temporal or cross-channel rules. Evaluations on the complete UEA-30 and UCR-128 archives show strong full-context and low-label performance without target-specific classifier fitting.

---


### 71. [Curved Inference II: Sleeper Agent Geometry - Extending Interpretability Beyond Probes](https://arxiv.org/abs/2608.24037)

**<font color=#1a73e8>作者：</font>** Rob Manson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper extends Anthropic's Sleeper Agents research [1], which showed artificial backdoors persist through safety training & can be detected by linear probes with >99% accuracy [2]. However, probe-based detection relies on linear separability that may be an artefact of backdoor insertion rather than a property of naturally occurring deceptive alignment. Sophisticated deceptive behaviours emerging through natural training are unlikely to produce such convenient linear signals.
We introduce a naturalistic methodology using multi-turn context windows that simulates realistic deceptive reasoning without artificial triggers or supervised backdoor insertion. Rather than binary trigger-response patterns, we examine how semantic complexity emerges through gradual context development.
Building on our Curved Inference framework, we analyse curvature, salience, & introduce semantic surface area (A'), a new metric of representational work capturing both the magnitude & directional change of meaning construction in unnormalised residual space. Without backdoors, labels, or probes, we apply this framework to naturalistic deceptive prompts & classify model outputs via LLM consensus.
Geometric structure reliably predicts semantic classification, with statistically significant differences in surface area across five prompt strategies & two model families. Critically, measurement precision can reveal geometric signatures hidden by classification noise - some strategies improve from non-significant (p = 0.555) to significant (p = 0.048). This validates that sophisticated reasoning creates intrinsic geometric patterns that persist even when detection appears to fail, suggesting the shape of inference itself encodes semantic patterns regardless of whether models have learned to suppress linear indicators of deception - a scalable, unsupervised path for detection when linear methods fail.

---


### 72. [PinSieve: Production Selective VLM Serving and a Governed Memory Flywheel for Enterprise Content-Quality Triage](https://arxiv.org/abs/2608.24040)

**<font color=#1a73e8>作者：</font>** Chuqing Gao, Yuanfang Song, Jonathan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enterprise AI agents in production often need to be bounded, stateful, observable, and governable rather than fully autonomous. We present PinSieve, a production case study in a large-scale content-quality pipeline. Its deployed component is a selective vision-language-model (VLM) Serving Agent that operates only on the grey-zone slice left unresolved by lightweight upstream models, exposes a scalar routing score online, and preserves controlled human escalation. On this slice, the deployed system filters 2.05x more non-actionable items than the previous production module while slightly reducing estimated miss rate; after promotion, it improves review productivity by 25.7%, reduces normalized operating cost by 16.2%, and moves signal delivery from next-day to same-day. We then study maintenance through a governed memory flywheel under selective feedback, where escalated items are reviewed by default and auto-passed items are labeled mainly through audit sampling. Feedback Memory records routing traces, observation paths, audit propensities, and replay metadata for evaluation and debugging. The Data Curation Agent uses a bounded proposal-verifier loop over representative, uncertainty, recency, and fresh-review replay, with positive-rate and score-bin guardrails before batch acceptance. In chained monthly refresh over six months of production data, this design reduces average FNR@50% from 17.73% under representative random replay to 13.29%. A Reasoning Review Agent audits teacher-generated rationales and supports keep/repair/drop decisions. Production claims are attributed only to the deployed Serving Agent; replay and rationale-review results are offline or sampled-governance evidence. The same serving-agent recipe has been adopted to several additional internal signals, suggesting transferability beyond one task.

---


### 73. [Relative Time Intervals Representation for Word-level Timestamping with Masked Training](https://arxiv.org/abs/2608.24041)

**<font color=#1a73e8>作者：</font>** Quanwei Tang, Zhiyu Tang, Xu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although Speech Large Language Models (SpeechLLMs) excel at speech understanding and generation, their capacity for fine-grained, temporally aligned outputs remains underexplored. Our work addresses this gap by enabling SpeechLLMs to jointly model speech content and temporal structure, effectively transforming them from ``content understanding machines" into ``temporal-aware content understanding machines". Specifically, we replace traditional absolute timestamps with relative timestamps, achieving a more compact vocabulary and stronger generalization capabilities. To efficiently infuse timestamp prediction ability into pre-trained large language models, we introduce a hybrid fine-tuning strategy: full-parameter fine-tuning of the timestamp-augmented embedding layer and language model head, combined with LoRA fine-tuning of the decoder layers. Moreover, we design a masked timestamp training objective, preventing the model from over-relying on ground-truth timestamps, and thereby enhancing robustness against noisy real-world annotations. Extensive experiments demonstrate that our approach achieves significant improvements in timestamp prediction accuracy while maintaining strong speech transcription performance.

---


### 74. [ConsensusTAS: Self-Supervised Temporal Action Segmentation for Long-Horizon Construction Videos](https://arxiv.org/abs/2608.24043)

**<font color=#1a73e8>作者：</font>** Xiaoshan Zhou, Yafei Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing sequential construction activities is important for collaborative human-robot work; for example, robots are able to understand workers' current and upcoming actions and provide timely tool delivery or physical support. However, despite extensive research on construction worker activity recognition, existing studies have been limited to classifying activity categories, such as climbing, lifting, and walking, instead of recognizing fine-grained activity transitions from long-horizon sequences. Addressing this problem is challenging because annotating action temporal boundaries in long construction videos is time-consuming. In this study, we propose ConsensusTAS, a label-free, self-supervised learning approach to segment continuous video streams into distinct activity phases by exploiting the internal consensus of candidate segmentations. We evaluated our algorithm on three public datasets, where it outperformed state-of-the-art methods, achieving an F1@10 of 73.08 on GTEA, an F1@10 of 64.33 on Breakfast, and an F1@50 of 33.50 on static-camera videos from Assembly101. We also tested it on real-world construction videos, where post-hoc evaluation showed that the model successfully recognized and segmented actions within the composite activity of bricklaying, such as spreading mortar on a brick, placing the brick, pressing, and aligning. Compared with other temporal action segmentation models that require computationally intensive large vision-language models, our method can run on a CPU, which provides practical value for video surveillance and human-robot collaboration on mobile robotic platforms.

---


### 75. [Algorithmic Impact Reveals the Hidden Social Choice Structure of Alignment](https://arxiv.org/abs/2608.24046)

**<font color=#1a73e8>作者：</font>** Zachary Wojtowicz, Michelle Si, Finale Doshi-Velez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When an AI algorithm makes decisions that affect more than one person, aligning it becomes a problem of social choice: how should people's divergent preferences about system behavior be reconciled and aggregated into a single coherent model? The standard approach to aligning frontier AI models$\unicode{x2013}$reinforcement learning from human feedback$\unicode{x2013}$largely sidesteps this question and has poor social choice guarantees. However, it remains unclear what alternative should replace it. We show that, by focusing directly on an algorithm's welfare consequences, the alignment problem can be reformulated as linear optimization over a convex impact space, which makes it amenable to the standard toolkit of welfare economics and mechanism design. This reformulation clarifies how alignment protocols translate into welfare consequences and, conversely, how a social planner's desired constraints on welfare consequences can be translated back into alignment protocols. We apply this transformation to show that voting-by-issues and random-dictatorship mechanisms are strategyproof and unanimous. Demonstrating the reverse direction, we also apply the impact representation to derive a family of alignment protocols that maximize utilitarian social welfare subject to various social desiderata, such as bounds on individual or group harm. We illustrate the welfare implications of these alignment protocols empirically using real human preferences over kidney allocation, charitable food distribution, LLM responses, and trolley problems.

---


### 76. [VisCache: Visual KV Cache Pruning for Efficient Vision Large Language Model Inference](https://arxiv.org/abs/2608.24063)

**<font color=#1a73e8>作者：</font>** Lyuke Wang, Zhuo Li, Guangxu Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Vision Large Language Models (VLLMs) have achieved remarkable success in multimodal reasoning, their long-context inference remains prohibitively expensive due to the massive computation and memory overhead of visual Key-Value (KV) caches. Existing KV compression methods often apply uniform pruning across visual tokens and layers, leading to substantial information loss and degraded this http URL address this challenge, we propose \textbf{VisCache}, a plug-and-play framework for coarse-to-fine \textbf{Vis}ual KV \textbf{Cache} pruning without training, which consists of two synergistic stages. First, a lightweight VLM filters temporal redundancy by selectively forwarding semantically informative keyframes. Second, we introduce {PruneKV}, a surgical KV compression algorithm tailored to the attention dynamics of VLLMs. Unlike rigid pruning strategies, PruneKV adopts a parabolic layer-wise budget allocation together with an asymmetric update mechanism that selectively prunes keys while fusing values, thereby preserving critical contextual information. Extensive experiments demonstrate that VisCache substantially improves inference efficiency, achieving up to {2.35$\times$ speedup} and significant memory reduction while maintaining competitive performance with only {19--28\%} KV cache retention. VisCache consistently outperforms existing baselines, establishing a new Pareto frontier between efficiency and performance for long-context VLLM inference. Code is available at this https URL

---


### 77. [Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems](https://arxiv.org/abs/2608.24069)

**<font color=#1a73e8>作者：</font>** CheolWon Na, Hao Ni, Lukasz Szpruch 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent trading systems, in which specialized agents collaborate through structured communication to produce trading decisions, are moving rapidly from research prototypes to live deployments that control real assets. The same inter-agent communication that makes them effective also exposes them: a corrupted signal can propagate to the final decision and translate into realized financial loss. Unlike prior attacks that presume privileged access to system internals, we restrict the adversary to what is practically reachable---the source data and prompts agents consume---yielding a low-barrier, and thus democratized threat model instantiated as role-specific adversaries.
We present the first systematic empirical study in the financial domain to characterize how an adversarial signal enters a multi-agent trading system and how far it survives toward the decision. Along the role axis, we decompose a widely-used trading pipeline into four functional roles---Analyst, Researcher, Trader, and Risk Manager---and pair each with an attack matched to its interface. Along the structural axis, we evaluate four communication topologies under data- and agent-level attacks, using the Adversarial Signal Preservation Score (APS) as a post-hoc lens on why some designs are more robust than others. We conduct experiments across five assets, two backbones, and two target directions. A central finding is that no architecture is inherently robust. These findings provide insights for the future design of safer and more robust agentic trading systems.

---


### 78. [Compression Trinity: Exploring Sparsity, Quantization, and Low-Rank Approximations for LLM Compression](https://arxiv.org/abs/2608.24070)

**<font color=#1a73e8>作者：</font>** Mohammad Mozaffari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prohibitive computational and environmental costs impede the scalable deployment of Large Language Models (LLMs). Traditional compression techniques (sparsity, quantization, low-rank approximations) are typically applied in isolation, and each hits an accuracy-efficiency wall. This thesis proposes the "Compression Trinity," a unified framework that applies the three pillars jointly: sparsity to reduce computation, quantization to minimize memory bandwidth, and low-rank approximations to recover accuracy. To accelerate pretraining, we apply the Trinity to the optimizer and model architecture. MKOR approximates curvature via block-diagonal sparsity and low-rank inversion, maintaining numerical stability for quantized states; it reduces curvature update complexity from $O(d^3)$ to $O(d^2)$ and accelerates convergence by up to 1.85x over KFAC. SLoPe accelerates training by up to 1.25x via a double-pruned backward pass for N:M sparsity, using low-rank "lazy" adapters in the final 1% of training to recover accuracy. For post-training compression, OPTIMA stabilizes static masks in a zero-training regime by formulating weight reconstruction as globally optimal column-wise quadratic programs, improving zero-shot accuracy by up to 3.97%. Given a fine-tuning budget, PATCH breaks the ceiling of static masks by learning a dynamic hybrid sparsity ratio between 0% and 50%, yielding up to 1.38x speedups. Finally, SLiM realizes the full Compression Trinity in one shot, using mathematically derived low-rank adapters to recover information lost to quantization and sparsity, improving accuracy by up to 5.66% over state-of-the-art methods and outperforming uncompressed dense models at equal parameter budgets by 0.6%. Together, these results show that jointly applying the Compression Trinity is essential for efficient, scalable, high-performance LLMs.

---


### 79. [When Less Is More: An Empirical Study of Minimal Responses in Counseling Dialogues and the Behavior of LLMs](https://arxiv.org/abs/2608.24080)

**<font color=#1a73e8>作者：</font>** Zhiyang Qi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In psychological counseling, effective support is not always delivered through long, information-rich responses. Minimal responses, such as backchannel cues and concise empathic statements, help convey attentive listening, express empathy, and encourage clients to continue expressing themselves. However, existing counseling dialogue systems and evaluation frameworks often favor explicit, content-rich replies, overlooking the interactional value of brief counselor utterances. This paper presents a systematic cross-lingual analysis of minimal responses across multiple counseling dialogue datasets. We develop a two-stage filtering method based on utterance length and content, followed by contextual verification using a large language model (LLM). Our analysis shows that minimal responses are common in human-collected datasets but substantially underrepresented in LLM-generated ones. We further evaluate current LLMs in manually curated dialogue contexts where human counselors used minimal responses. The results show that strong commercial LLMs are capable of generating minimal responses when explicitly instructed, but still struggle to determine when such responses are appropriate. Counseling-specific models trained on synthetic data perform particularly poorly, tending instead to produce longer and more information-rich responses. Moreover, LLM-based response-quality evaluation may undervalue minimal responses, even when they are interactionally appropriate.

---


### 80. [PARTAB: Partition-Aware Reasoning with Structured Evidence for Scalable Table Understanding](https://arxiv.org/abs/2608.24082)

**<font color=#1a73e8>作者：</font>** Md Mahadi Hasan Nahid, Davood Rafiei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong capabilities in table reasoning, but their effectiveness degrades as tables grow in size and complexity due to irrelevant context and difficulty localizing the evidence required for reasoning. Existing approaches typically reason over either the full table or a single reduced view, which can still obscure important row-column relationships. We introducePARTAB (Partition-Aware Reasoning overTables), a framework that constructs a structured evidence interface between the LLM and the table. PARTAB represents query-relevant evidence as semantically coherent, row-linked table regions and performs hierarchical selection over column groups and row-level partitions before composing the selected evidence for answer generation. We evaluate PARTAB on multiple table reasoning benchmarks, covering question answering, fact verification, and numerical reasoning. PARTAB consistently improves over full-table prompting and several recent table reasoning methods, achieving strong performance on WikiTableQuestions and TabFact while remaining competitive on numerical reasoning. Additional analyses show that semantic partitioning and targeted evidence selection improve evidence localization, substantially reduce the reasoning context, and provide larger benefits on complex tables. These results demonstrate the value of structured, partition aware evidence construction for scalable table reasoning.

---


### 81. [EMRB: A Multi-Level Benchmark for Evaluating LLM Reasoning over Raw Electromagnetic Signals](https://arxiv.org/abs/2608.24086)

**<font color=#1a73e8>作者：</font>** Mingxu Zhang, Ying Sun, Yuhan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as code agents for scientific and engineering analysis, but their ability to analyze raw physical-layer measurements remains untested. We introduce \textbf{EMRB} (\textbf{E}lectro\textbf{m}agnetic \textbf{R}easoning \textbf{B}enchmark), which evaluates whether LLMs can analyze raw I/Q data by writing and running code. EMRB contains 200 problems across five difficulty levels and 27 question types, from signal detection to OFDM design, generated from 11 signal types with verified ground truth. Unlike benchmarks built on preprocessed features or structured tables, EMRB provides only the raw capture; the quantities each question refers to must first be discovered through code. We evaluate 14 LLMs spanning proprietary, open-weight, and reasoning-oriented families. Scores range from 24.1\% to 78.9\%, with the mean dropping from 84.9\% on basic measurement to 21.2\% on system design. We also propose \textbf{ReconPilot}, a structured method that separates signal reconnaissance, targeted analysis, and self-verification. Across three backbones, ReconPilot raises the overall score by 3.8 to 17.6 points and improves 13 of 15 backbone-level combinations tested. All data and code are publicly released in \href{this https URL}{\textcolor{blue}{our GitHub repository}}.

---


### 82. [Knowing When to Ask for Help: Bayesian Self-Escalation in Hierarchical LLM Agents](https://arxiv.org/abs/2608.24087)

**<font color=#1a73e8>作者：</font>** Nadeem Shaikh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current LLM agent systems decide delegation before reasoning begins (a router picks a model) or after a response is complete (a verifier scores it and may retry). We study a third regime: an agent that recognises, during its own reasoning, that it is unlikely to succeed and transfers control to a stronger model. We formulate intra-generation delegation as a Bayesian optimal-stopping problem over a learned competence posterior -- an online estimate of the agent's eventual task success whose sufficient statistics are learned from labelled trajectories, not read off raw entropy. We derive the myopic escalation threshold in closed form, characterise the optimal policy via dynamic programming, and prove that the optimal policy is a time-varying threshold with no shape assumption on the raw signal. We further prove exponential separation of the oracle belief at the Chernoff-information rate of the signal, a regret bound governed by the calibration of the posterior, and a finite-sample guarantee: with n labelled calibration trajectories the deployed plug-in policy's regret decays as 1/sqrt(n). A controlled simulation study confirms each prediction of the theory, including the predicted 1/sqrt(n) rate. We additionally report a real-model validation on a Qwen2.5-Coder 1.5B->7B code cascade (MBPP, 257 tasks), confirming two of three pre-registered predictions: the escalation frontier dominates post-hoc routing at equal cost, and the cumulative competence belief's discrimination rises over generation.

---


### 83. [ACE: A Self-Correcting Agentic Canvas Editor for Multi-Slide Presentation Automation](https://arxiv.org/abs/2608.24103)

**<font color=#1a73e8>作者：</font>** JooYoung Jang, Taegyeong Lee, Jihyeon Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Commercial design platforms increasingly edit documents through large language model (LLM) agents, but two practical problems block reliable deployment: legacy document formats expose only \emph{flat}, absolutely positioned elements, so agents must recompute coordinates and routinely break layouts; and design has no unique ground truth, so diff-against-reference metrics penalize valid-but-different outputs. We present \textbf{ACE}, an agentic canvas editor over a \emph{hierarchical scene-graph} with a presentation-specialized action space (98 tools), paired with \textbf{CARE}, a content-aware router that feeds the agent only the relevant slice of each deck (avg.\ $\sim$89\% input-token reduction), and a \emph{self-correction} loop driven by a \emph{ground-truth-free} instruction-following (IF) judge whose natural-language critique is fed back as the next-turn instruction. With a fixed backbone, a scene-graph editor in a \emph{single turn} already matches a same-backbone \emph{agentic} HTML pipeline that iterates internally; adding self-correction lifts ACE significantly above it on instruction following (IF 4.23 vs.\ 3.81 on the full 94-task benchmark, paired $p{=}.010$, replicated by an out-of-loop judge) at 1.75$\times$ the speed and $\sim$44\% lower cost. VQ means are statistically indistinguishable, but 26 blind raters prefer ACE overall (58.7\% decisive win-rate) and prefer the self-corrected output 81\% of the time; the ranking is invariant across three judge families, and out-of-loop judges retain two-thirds of the self-correction gain, bounding circularity. 66\% of cases halt after one pass, and a strict-peak rollback removes every observed regression.

---


### 84. [DRRG: A Discrete Diffusion Framework for Radiology Report Generation](https://arxiv.org/abs/2608.24105)

**<font color=#1a73e8>作者：</font>** Shaoyang Zhoua, Yingshu Li, Yunyi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Automatic radiology report generation (RRG) has been widely explored to improve reporting accuracy and reduce radiologists' workload. Most existing methods rely on autoregressive (AR) frameworks that generate reports token by token and cannot revise earlier content, making them prone to error propagation and inconsistent with the iterative refinement process of radiological reporting. In contrast, discrete diffusion large language models (DLLMs) generate text through iterative denoising, naturally enabling report refinement. However, DLLMs have not been extensively investigated for RRG. In this study, we developed and evaluated a discrete diffusion framework for RRG that enables iterative refinement rather than conventional left-to-right autoregressive decoding.
Materials and methods: We developed DRRG, a DLLM-based framework that formulates RRG as iterative masked-token denoising. DRRG incorporates a clinical-entities-aware complementary mask to improve token supervision coverage and emphasize clinically important entities, together with a concept-conditioning module that injects image-derived clinical concepts into visual representations. DRRG was trained and evaluated on MIMIC-CXR and CheXpert Plus.
Results: On MIMIC-CXR, DRRG achieved BLEU-4 of 0.210, CheXpert-F1 of 0.549, RadGraph-F1 of 0.281, GREEN of 0.360, and RaTEScore of 0.604, outperforming the compared methods on most reported metrics, despite employing a substantially smaller LLM decoder. On CheXpert Plus, DRRG achieved the highest BLEU-4 (0.119) and CheXpert-F1 (0.347) among the compared methods.
Conclusion: Discrete diffusion provides an effective alternative to autoregressive radiology report generation by enabling iterative, bidirectional report refinement. Incorporating clinically focused masking and image-derived concept conditioning improves report quality and clinical consistency.

---


### 85. [Structured Frequency-Domain Evidence for LLM-Based Time-Series Anomaly Detection](https://arxiv.org/abs/2608.24113)

**<font color=#1a73e8>作者：</font>** Jungwook Seo, Sangwon Son, Minjeong Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series anomalies can appear not only as pointwise deviations but also as changes in recurring temporal structure, such as shifted periodicity or localized oscillatory fluctuations. However, existing LLM-based time-series anomaly detection methods mainly expose time-domain evidence through indexed values, plots, or de-seasonalized representations, leaving spectral structure implicit. We propose an evidence-augmented zero-shot TSAD framework that preserves indexed de-seasonalized observations while adding compact frequency-domain evidence computed with the Fast Fourier Transform (FFT). The evidence is constructed at two resolutions: global frequency-domain evidence summarizes sequence-level periodic context, while local frequency-domain evidence captures time-localized spectral departures. Experiments on AnomLLM with InternVL2-LLaMA3-76B, Qwen2.5-VL-72B-Instruct, Gemini-2.5-Flash, and GPT-4o, together with evaluation on the TSB-AD-U subset, show that explicit frequency-domain evidence improves LLM-based TSAD baselines. These results suggest that frequency-domain evidence can complement indexed and de-seasonalized time-domain inputs for zero-shot LLM-based TSAD.

---


### 86. [AHEAD: Adaptive Hindsight with Environment-Augmented Distillation for Agentic RL](https://arxiv.org/abs/2608.24114)

**<font color=#1a73e8>作者：</font>** Xiaolong Jin, Dingmin Wang, Vijay Lingam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training multi-turn LLM agents with reinforcement learning typically relies on trajectory-level rewards, which assign a uniform advantage to every step and cannot identify which decisions led to success or failure. Self-distillation methods can provide finer-grained supervision by augmenting RL with privileged information. However, existing approaches usually apply the same type of privileged information to every step in an indistinguishable manner, ignoring a key asymmetry: routine steps need little additional guidance, while critical error steps require corrective direction that environment feedback alone cannot provide. We propose AHEAD, a step-aware framework that matches different supervision sources to different step types. The teacher receives environment feedback on all steps as a grounded dense signal, and additionally receives LLM-generated corrective hints on error steps to supply the direction that environment feedback lacks. The method introduces minimal changes to the standard GRPO algorithm. Across ALFWorld, WebShop, and Search-based QA, and across three model scales, AHEAD raises task success (+13.3 points on ALFWorld and +11.0 on WebShop at 7B over GRPO), reaches a given success rate in fewer training steps, and solves tasks within tighter interaction budgets than outcome-only RL and prior self-distillation baselines.

---


### 87. [MC-CXR: A Multi-Context Chest X-ray Benchmark for Context-Induced Disruption in Vision-Language Models](https://arxiv.org/abs/2608.24118)

**<font color=#1a73e8>作者：</font>** Junhyeok Lee, Songsoo Kim, Kyu Sung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used in clinical pipelines where a chest X-ray is interpreted alongside retrieved reports, preliminary notes, or prior imaging. Existing benchmarks measure whether models answer correctly in isolation, but not whether they preserve a correct image-only decision when plausible context conflicts with the image. We introduce Multi-Context Chest X-ray (MC-CXR), a benchmark of 240 cases expanded into 2,522 instances that isolates context-induced disruption through paired perturbation. Each case fixes the current image and target finding while presenting matched reliable and misleading context across text and prior CXR, with visual overlays where available. MC-CXR defines three task families and two paired metrics, the switch-to-wrong rate and the context-aligned error rate. We evaluate ten VLMs spanning open-source general, medical-domain, and closed-source systems. Image-only accuracy is necessary but insufficient. Mean switch rates range from 45.6-78.1% across misleading textual sources and 35.7-61.7% across misleading visual sources. Among switched predictions, 74.6% align with the misleading label for text versus 17.6% for visual context, a 57.0-point gap (95% CI 50.9-62.8). This text-visual asymmetry is observed under the standardized direct-answer protocol. The dataset is available on PhysioNet.

---


### 88. [TransPhy: Visual In-Context Learning for Physically Grounded Image Editing](https://arxiv.org/abs/2608.24119)

**<font color=#1a73e8>作者：</font>** Siyi Xie, Xuanke Shi, Jinsheng Quan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual demonstrations provide a natural interface for specifying image transformations that are difficult to describe exhaustively with text. However, existing visual in-context learning (VICL) methods primarily focus on appearance-level relation transfer and provide limited support for physically grounded transformations, whose outcomes depend on material properties, geometry, object interactions, and environmental conditions. Given a source--target exemplar pair and a query image, physically grounded VICL requires a model to infer the demonstrated transformation, adapt its effects to the query-specific scene context, and preserve rule-irrelevant content. We introduce PhysVICL-74, comprising 74 physically grounded transformation rules and 5,240 source--target image pairs that form nearly 75K training and evaluation contexts. Its benchmark split separately evaluates novel-instance transfer and unseen-rule generalization. We further propose TransPhy, a framework that decomposes physically grounded VICL into physical-rule induction and transition-aligned rendering. TransPhy first predicts the demonstrated rule and an explicit query-specific target-state description, and then synthesizes the target image through token-wise mixture-of-experts adaptation, with expert routing guided by localized transition cues. Experiments show that TransPhy improves physical-rule adherence, query consistency, and unseen-rule generalization over existing visual in-context editing methods.

---


### 89. [Graph-Supervised Hierarchical Clinical Alignment for Radiology Report Generation with Large Language Models](https://arxiv.org/abs/2608.24121)

**<font color=#1a73e8>作者：</font>** Yingshu Li, Yunyi Liu, Zhanyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology report generation (RRG) has recently benefited from large language models, which substantially improve report fluency. However, clinically faithful generation remains challenging because current supervision is still imposed mostly at the report level. This creates a granularity mismatch: radiology reports are composed of disease-grounded findings, while existing methods are trained mainly with whole-report objectives. To address this problem, we propose Graph-Supervised Hierarchical Clinical Alignment, which reformulates image-report supervision as a hierarchical clinical alignment problem. Our method structures this alignment as a disease-conditioned process, where supervision is decomposed into two levels: Disease-Centric Alignment for fine-grained disease-specific correspondence, and Global Clinical Semantic Alignment for report-level semantic coherence. A clinical knowledge graph is used as a training-time-only structural prior that defines disease-specific supervision units and their clinical relationships, introducing no additional overhead at inference. Because standard contrastive alignment could produce false negatives when studies share overlapping pathologies, we combine instance-conditioned discriminative matching with disease-conditioned soft regularization, enabling fine-grained yet clinically consistent cross-modal representations. Experiments on MIMIC-CXR, IU-Xray, and COV-CTR show that our method consistently improves performance on both conventional and clinical metrics. Notably, our 3B model surpasses several prior systems with larger 7B/13B backbones, suggesting that improving supervision structure, rather than increasing model size, can be more effective for RRG.

---


### 90. [Anatomy of a Scam Call: What 10,000 real scam and spam calls reveal about how phone scammers operate](https://arxiv.org/abs/2608.24127)

**<font color=#1a73e8>作者：</font>** Ethan Traister, Ankit Raj, Jiaqi Gan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Telephone fraud is pervasive and costly, but its inner workings are rarely observed at scale. We analyze a complete corpus of 10,211 inbound scam and spam calls -- 913 hours of audio and 330,956 transcribed turns from 5,780 distinct numbers -- collected over 54 days by an AI voice-agent honeypot that answered callers and kept them talking, and introduced in a companion data descriptor. We separate outright scams, which solicit sensitive information, from the larger stream of predatory but legal lead generation ("spam") that feeds them. Scam operations keep office hours (6.6x more calls per weekday than weekend day); thousands of disposable numbers run a small catalog of recycled scripts (thirty opening clusters, half the traffic in the top five); and callers solicit identity anchors -- a home address and a date of birth -- far more often than payment credentials, pressing through persistence and manufactured authority rather than overt threats. Our central experiment asks: does it matter who picks up? Every seeded lead carried one of ten fictitious identities drawn uniformly at random, so the identity a fraud operation reaches is fixed before the caller exists. Across 1,823 randomized calls, scammers spent about 15% more conversational turns per decade of the target's apparent age (rate ratio 1.15, 95% CI 1.08-1.23; randomization p = 0.005) -- yet what they asked for did not change (26.3% of calls reached a request for sensitive information; odds ratio 0.99 per decade, 95% CI 0.90-1.08). A second experiment casts early detection as a benchmark: from a scammer's opening lines alone, on a caller-disjoint split, escalation is predictable at 0.72 ROC-AUC from the first line and 0.87 by the eighth, and a plain bag-of-words classifier matches a fine-tuned on-device language model. Telephone fraud emerges as a templated industry that varies how hard it works a target, but not what it wants.

---


### 91. [PlaceSeek: Human-Centered Geospatial Retrieval of Urban Outdoor Places via Semantic Grounding and Affective Alignment](https://arxiv.org/abs/2608.24133)

**<font color=#1a73e8>作者：</font>** Ziqi Cui, Shangyu Lou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> People search for urban outdoor places not only by category or function, but also by what activities a place can support and how it is perceived. Existing geospatial retrieval remains largely POIcentric and metadata-driven, making it difficult to satisfy openended, affective, or activity-oriented needs. We present PlaceSeek, a human-centered outdoor place retrieval framework that maps natural-language queries to geolocated street-view imagery. PlaceSeek introduces an intent-aware retrieval mechanism that decomposes user queries into functional and affective sub-intents. A Semantic Grounding Module verifies whether candidate street-view results contain the physical evidence needed to support the intended activity, while an Affective Alignment Module re-ranks physically valid candidates using a LoRA-adapted vision-language model trained on human urban perception judgments. We evaluate PlaceSeek on 31,956 street-view locations in Milan across 10 naturallanguage queries annotated by five human evaluators. PlaceSeek achieves 88.0% Precision@5, a mean match score of 3.39/4.0, and 0.920 nDCG@5, outperforming CLIP, fine-tuned CLIP, SigLIP, and a VQA-based baseline. Ablation results show that physical grounding is essential for retrieval validity, while affective alignment improves ranking quality among physically valid candidates. These findings highlight that complex urban spatial queries require modeling both verifiable visual evidence and human perceptual preferences. PlaceSeek provides a potential framework for human-centered nextgeneration geospatial retrieval systems.

---


### 92. [EgoErrorVQA: Assess Egocentric Comprehension Capabilities through Procedural Errors for Ego-Agentic AI](https://arxiv.org/abs/2608.24134)

**<font color=#1a73e8>作者：</font>** Junlong Li, Junxi Li, Jianjun Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The majority of our everyday activities are procedural and consist of sequences of interdependent steps. However, existing benchmarks for Visual Agents and Visual Language Models (VLMs) overlook the evaluation of their procedural comprehension ability from an egocentric visual perspective, particularly for detecting procedural errors, a critical capability for everyday assistance. To bridge this gap, the EgoErrorVQA task is firstly proposed for egocentric procedural comprehension with explicit procedural errors modeling. Besides, we develop a user-friendly evaluator agent based on the Agent2Agent (A2A) protocol, enabling rigorous and standardized evaluation of visual agents through VQA-based interaction. A range of models are evaluated using both open-ended and multiple-choice questions, revealing persistent weaknesses in handling procedural errors and error types. Moreover, we introduce Ego-ADR, an Adaptive Decoupled Reasoning framework that decouples complex procedural reasoning to enhance models' understanding of procedural errors. It achieves consistent performance gains over the selected baselines and attains state-of-the-art results on several metrics under comparable settings. Code: this https URL

---


### 93. [Robust Code RL via Faulty-Code-Driven Test case Synthesis and Dense Reward Shaping](https://arxiv.org/abs/2608.24135)

**<font color=#1a73e8>作者：</font>** Yiwen Zhang, Xiaodong Yan, Zhenyu Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) has emerged as a pivotal technique for enhancing the code generation capabilities of Large Language Models (LLMs). However, the efficacy of RLVR in coding implementations is fundamentally limited by the comprehensiveness of test cases, because insufficient test coverage in code validation often causes false positives, further leading to reward hacking and policy degradation. To mitigate the reward bias stemming from the suboptimal quality of current automated generation methods, we propose the RobustTests framework, which introduces a faulty-code-driven test case synthesis strategy that leverages "near correct" faulty codes to guide the model in precisely capturing latent logical discrepancies and further integrates validator agents with behavioral feature clustering to facilitate the granular filtering of invalid and redundant test cases. To address false negatives caused by inherent hallucination noise in synthetic test cases, RobustTests also incorporates a stepwise dense reward function based on pass rates, bolstering training robustness through fine-grained feedback. By employing this pipeline, we construct a high-quality dataset that augmented the test cases in CodeContests, encompassing a broader spectrum of faulty code scenarios and significantly enhances diagnostic utility. Experimental results demonstrate that, by leveraging a moderately challenging subset of problems from CodeContests for training, RL fine-tuning of Qwen3-32B via RobustTests achieves an absolute 3% performance gain on the LiveCodeBench benchmark compared to baseline methods, confirming the effectiveness of the RobustTests framework in advancing the code generation proficiency of LLMs.

---


### 94. [Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation](https://arxiv.org/abs/2608.24138)

**<font color=#1a73e8>作者：</font>** Tianyi Xiong, Zhengyuan Yang, Xiaofei Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models have shown strong progress in UI-to-code generation, yet their test-time self-evolution remains unstable. We first identify a fundamental obstacle, termed visual repair coupling: a local code edit may propagate through layout, style, and component dependencies, correcting one visual mismatch while degrading regions that were previously faithful. To address this issue, we present RubSE, a Rubric-guided Self-Evolution framework that uses rubrics to represent visual feedback as a structured visual-repair context. At each refinement round, RubSE generates typed candidate rubrics, selects one prioritized repair target, and stores previously selected rubrics as history, thereby steering each revision toward a well-scoped visual repair while discouraging repeated or over-broad changes. Evaluations across six VLMs and three UI-to-code benchmarks demonstrate that RubSE substantially outperforms naïve self-evolution in final-round and best-round settings, achieving more stable refinement trajectories and a higher trajectory-level performance ceiling. Further analysis shows that RubSE mitigates trajectory collapse by improving recovery from severe visual regressions, and that stronger rubric generators can transfer effective visual-repair guidance to weaker code improvers.

---


### 95. [What Does Prompt Learning Change? -A Natural-Language Concept Analysis of Vision-Language Models](https://arxiv.org/abs/2608.24142)

**<font color=#1a73e8>作者：</font>** Ryo Kamiya, Hiroshi Kera, Kazuhiko Kawamoto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt learning adapts vision-language models such as CLIP by optimizing continuous prompt vectors, but the learned prompts are difficult to interpret in natural language. We present PromptSpLiCE, a post-hoc method that expresses each class-conditioned text embedding as a sparse combination of concepts from a fixed natural-language dictionary. Using the same dictionary before and after prompt learning allows us to compare changes in their concept profiles. We evaluate PromptSpLiCE on CoOp, a representative prompt-learning method, across 11 image-classification datasets. The concept profiles change substantially: on average, only 1.6 of the initial top-10 concepts remain in the top 10 after learning. Across datasets, profile change is positively associated with accuracy gain. We also derive a local gradient expression that provides geometric intuition for why image-aligned concept directions distinct from the current prompt can have greater loss sensitivity.

---


### 96. [FireRedAudio: A General-Purpose Audio Language Model with Decoupled Continuous Representations for Understanding and Generation](https://arxiv.org/abs/2608.24168)

**<font color=#1a73e8>作者：</font>** Junjie Li, Xuelong Geng, Kun Xie 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A unified audio model must recognize and understand linguistic, paralinguistic, and environmental information while supporting speech synthesis and editing. A key challenge is representation: understanding favors compact features suited to long-context modeling, whereas speech generation requires reconstructible features that preserve fine-grained acoustic detail. We introduce FireRedAudio, a general-purpose audio language model with a shared 9B-parameter LLM. To the best of our knowledge, it is the first publicly disclosed unified audio-language model to provide separate continuous input representations for understanding and generation within a single trainable autoregressive LLM. Audio to be recognized or analyzed is processed by a dedicated Audio Encoder, while speech inputs for generation use a RedAE-based pathway. The LLM directly generates text or conditions a flow-matching DiT to produce continuous acoustic latents. Through progressive multitask training, FireRedAudio supports ASR and audio understanding, with the latter extending to recordings of up to one hour, as well as zero-shot TTS, Instruct TTS, and semantic and acoustic speech editing. Its structured organization of long-form audio achieves second-level timestamp accuracy. Across comprehensive evaluations, FireRedAudio achieves competitive or leading performance in audio understanding and multilingual ASR, strong content accuracy and speaker preservation in zero-shot TTS, leading instruction following in Instruct TTS, and substantial improvements over Ming-UniAudio-Edit in both semantic and acoustic speech editing. These results demonstrate the viability of decoupled continuous input representations for unifying audio understanding and continuous-latent speech generation in a model of moderate scale. Our code is available at this https URL.

---


### 97. [ViSculpt: Visual-Centric Agentic Geometry Editing](https://arxiv.org/abs/2608.24169)

**<font color=#1a73e8>作者：</font>** Bo Pang, Jiaqi Pan, Xiaocheng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D geometry editing is a critical yet labor-intensive part of the graphics pipeline, requiring artists to translate creative intent into precise operations in complex professional software. Large language models (LLMs) have shown promise for script-based 3D creation, but script generation is less suited to perception-driven editing of arbitrary existing meshes, where execution must remain visually grounded and untouched regions should be preserved. We present a \emph{visual-centric}, training-free multi-agent system that edits existing 3D meshes directly in Blender by emulating the iterative workflow of human artists. Rather than generating scripts or regenerating geometry, our system operates through the Blender GUI: multimodal LLM agents observe the viewport, reason about the current mesh state, and execute localized edits through simulated user interactions. Experiments on a curated benchmark provide initial evidence that this agentic approach can follow natural language instructions, perform representative localized mesh edits, and preserve the overall identity of the input asset. Our results highlight a complementary regime for language-driven 3D editing: direct in-place modification of existing meshes within the native 3D editing workflow. We view this work as an exploratory step toward visual-centric agentic geometry editing in professional graphics software.

---


### 98. [SandwichQuant: Which Parameters Matter Before and After Quantization?](https://arxiv.org/abs/2608.24173)

**<font color=#1a73e8>作者：</font>** Peng Xia, Junbiao Pang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantization correction methods usually optimize weights, quantization parameters, or reconstruction objectives, while the underlying parameter subspaces responsible for effective correction remain unclear. In this work, we study quantization correction from a parameter subspace perspective and reveal that correction capability is highly non-uniform across parameter groups. By decomposing trainable parameters into backbone weights, normalization-affine parameters, and quantization parameters, we show that the low-dimensional normalization-affine subspace provides a highly efficient correction direction under matched budgets. Based on this finding, we propose SandwichQuant, a two-stage normalization-affine correction framework that performs adaptation before and after quantization. The pre-stage improves quantization robustness, while the post-stage compensates residual errors after the quantized graph is fixed. Extensive experiments on vision models and large language models demonstrate consistent improvements under various low-bit quantization settings, validating the effectiveness of subspace-aligned correction.

---


### 99. [Paritok-4B: Intent-Conditioned Context Compression for Coding Agents](https://arxiv.org/abs/2608.24188)

**<font color=#1a73e8>作者：</font>** Jiayu Shi, Luzhuo Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents re-send large file reads and tool outputs to a frontier LLM every turn, and this context dominates their token bill. General-purpose prompt compressors are trained on prose and suit code poorly: they paraphrase identifiers and drop the exact spans an agent needs to edit. We present Paritok-4B, a 4B LoRA compressor for coding-agent trajectories built on two commitments. It is extractive: it selects spans rather than rewriting them, and 96.0% of the identifiers, paths, and numbers it emits already appear in its input, holding at 96.2% on held-out SWE-bench Lite output. It is intent-conditioned: told the agent's current task, it acts chiefly inside a retained segment, selecting which lines survive (retained lines are +0.067 more intent-relevant than removed ones, paired 95% CI [+0.056, +0.078]) rather than changing how much is retained. We distil a gpt-4.1-mini teacher over 67,074 real OpenHands trajectories into 40,606 validated examples and fine-tune Qwen3-4B. On all 300 SWE-bench Lite instances, Paritok-4B compresses agent context to 25.7% of its size, 2.0x harder than a gpt-4.1-mini compressor (50.2%) and 2.4x harder than gpt-5 (61.9%), while retaining 86.5% of uncompressed single-shot solve quality. Fed the cat -n line-numbered input real agents produce, it compresses slightly less (27.8%) and retains more (89.3%); there the paired test is informative, with 30 instances solved only uncompressed and 17 only compressed, an exact McNemar p=0.079, so at this sample size compressing context to roughly a quarter of its size does not significantly reduce the solve rate. The model is a 264 MB adapter that self-hosts on one 24 GB GPU with no per-token compressor fee, which at list prices decides the economics: gpt-5 as a compressor is net-negative, costing more than the downstream tokens it saves. Weights, data, and evaluation scripts are open (Apache 2.0).

---


### 100. [MemUse: Moving Memory Evaluation from Direct QA to Natural Integration in Long-Term Human-AI Conversation](https://arxiv.org/abs/2608.24189)

**<font color=#1a73e8>作者：</font>** Ryuichi Sumida, Koji Inoue, Tatsuya Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory systems for conversational LLMs are conventionally evaluated by direct, fact-seeking questions about prior dialogue (Direct QA): can the model recall fact X from a prior conversation? We tested whether higher Direct QA accuracy correlates with higher user satisfaction in a 4-month deployment (40 users, 1,872 sessions, 7 memory conditions). Existing-benchmark Direct QA varies from 19.7% to 70.1% across the 7 conditions, but satisfaction does not change. We hypothesize that existing benchmarks and user satisfaction are tracking different capabilities: benchmarks measure elicited retrieval (recall when asked), while conversation requires natural integration (detecting relevance and naturally weaving prior context into a response). To examine this, we introduce MemUse, a set of real user-cued memory moments drawn from the deployment, scored by an integration-aware judgment of the natural conversational response. Holding the model and context fixed, the same system that scores 78.8% on Direct QA references only 7.9% of those facts in conversation -- a 71-point gap. Within these moments, Natural Integration is associated with satisfaction, whereas Direct QA is not. We release the deployment corpus and MemUse together with all judgments and scoring prompts at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

# 🧠 大模型相关研究 | 2026年07月14日

> 本类共 **68** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-68**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-68**

---

### 51. [A Sovereign, Open-Source Foundation Model for German and English](https://arxiv.org/abs/2607.09424)

**<font color=#1a73e8>作者：</font>** Soofi-Team, Benedikt Droste, David Fitzek 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Soofi S 30B-A3B, a sovereign, open-source Mixture-of-Experts (MoE) hybrid Mamba Transformer foundation model for German and English. Its hybrid design activates only 3B of 30B parameters per token and keeps the inference cache near-constant as context grows, giving it a decisive throughput advantage over dense models for long-context, high-concurrency deployment. Pretrained on roughly 27 trillion tokens with deliberately up-weighted German, Soofi S matches dense 14 to 27B models on aggregate English and German benchmarks while achieving the best code aggregates in both languages among 17 open base models, and outperforms every European sovereign baseline in our comparison, including ones far larger in active parameters. Among fully open models, Soofi S obtains the highest English and German evaluation scores, ahead of Olmo 3 32B and Apertus 70B. Soofi S was built end-to-end on the German Industrial AI Cloud, a sovereign HPC scale AI infrastructure operated by Deutsche Telekom in Munich. Soofi S will be released under highly permissive, open-access terms: weights, selected intermediate checkpoints, full per-source data accounting, hyperparameters, and training and evaluation code. Where source licenses permit, data-construction artifacts are released under permissive licenses; commercially licensed sources are documented with aggregate statistics and exact mixture accounting.

---


### 52. [Multimodal Scenario Similarity Search for Autonomous Driving](https://arxiv.org/abs/2607.09428)

**<font color=#1a73e8>作者：</font>** Tamás Matuszka, András Tamásy, Balázs Szolár  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale autonomous-driving datasets contain vast numbers of recorded scenarios, creating a need for efficient retrieval methods that can identify situations similar to a given query. Existing approaches typically rely on either visual representations or motion-based descriptions, making it difficult to understand their relative strengths and limitations for scenario retrieval. In this work, we present a multimodal framework for autonomous-driving scenario retrieval that combines visual and trajectory-based representations within a unified retrieval pipeline. We investigate two trajectory-based approaches: Exo-Trajectory, an explicit matching method based on surrounding-agent motion, and ScenarioFormer, a transformer-based representation learned from object trajectories using contrastive learning. We compare these approaches against strong vision-based baselines and analyze their behavior across a diverse set of driving scenarios. Experimental results show that trajectory representations provide strong retrieval performance for motion-centric events such as cut-ins, turning maneuvers, and traffic queueing, while visual embeddings excel when appearance cues are informative. Most importantly, combining visual and trajectory information consistently improves retrieval quality, yielding the best overall performance. These findings demonstrate that appearance and motion capture are complementary notions of scenario similarity and motivate multimodal retrieval systems for autonomous-driving data mining, dataset curation, and scenario-based validation.

---


### 53. [Test-Time Scaling for Small VLMs on Multilingual Visual MCQ](https://arxiv.org/abs/2607.09438)

**<font color=#1a73e8>作者：</font>** Spiros Baxevanakis, Peng-Jian Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling (TTS) reliably improves reasoning in large language models, but whether it transfers to small open vision-language models remains unclear. We examine this on EXAMS-V, a multilingual visual multiple-choice benchmark, comparing self-consistency, describe-then-reason with PRM-guided beam search, and two post-hoc selectors across Qwen2.5-VL-7B-Instruct and Qwen3.5-4B. What matters is the conditions under which TTS runs, not the search or verification machinery. The largest factor is parseability: an early prompt format left many chains reasoning correctly yet never committing to an answer letter, which a standard answer cue and a guided repair step largely remove. A larger decoding budget removes the rest: raising the per-chain token limit from 1k to 2k recovers 3.7 pp, whereas sampling more chains (8 to 16) adds only 0.15 pp. Once chains have room to finish, elaborate methods contribute little: PRM-guided beam search trails plain self-consistency by 0.39 pp at over eight times the cost, and neither a training-free generative critic nor a trained multimodal PRM beats majority vote across both policies. The largest gain comes instead from the policy model itself (+11.4 pp). Our best configuration reaches 84.1% on the held-out ImageCLEF 2026 test split, ranking first on the Visual MCQ leaderboard.

---


### 54. [Robustifying Vision-Language Models via Test-Time Prompt Adaptation](https://arxiv.org/abs/2607.09450)

**<font color=#1a73e8>作者：</font>** Xingyu Zhu, Huanshen Wu, Shuo Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained Vision-Language Models (VLMs) such as CLIP achieve strong zero-shot generalization, but their performance degrades sharply under adversarial perturbations. Existing test-time adaptation methods typically rely on sample-level confidence heuristics, overlooking the intrinsic distributional structure of the data. This sample-centric approach limits robustness, as it fails to distinguish confident adversarial mispredictions from true semantic consistency. In this work, we observe that adversarial distortion is structurally brittle: while holistic representations are corrupted, semantic integrity is often preserved in the distribution of augmented views. Motivated by this insight, we propose RITA, a Robust test-tIme prompt-TAdaptation framework that shifts from sample-level estimates to distribution-level alignment. Specifically, RITA employs optimal transport to align the distribution of augmented visual features with textual prototypes, mitigating adversarial outliers and rectifying cross-modal semantic misalignment. Furthermore, we introduce a dynamic cache to progressively accumulate reliable cues from the test stream for online refinement. Extensive experiments demonstrate that RITA significantly improves adversarial robustness without compromising clean accuracy.

---


### 55. [ProofCouncil: An LLM Agent for Solving Open Mathematical Problems](https://arxiv.org/abs/2607.09474)

**<font color=#1a73e8>作者：</font>** Johannes Schmitt, Tim Gehrunger, Jasper Dekoninck 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown increasing promise in solving open problems in mathematics. However, their performance can be further improved through agentic workflows tailored to real-world mathematical practice. To this end, we introduce ProofCouncil, a mathematical agent that is designed to tackle open problems using an author-critic architecture. ProofCouncil served as a submission to the second batch of FirstProof, a challenge consisting of 10 real-world mathematical problems that agents must solve autonomously. Its submissions for 6 of the 10 problems were judged by the referees to be correct up to at most minor revisions, showing the best performance among participating teams. We also evaluate ProofCouncil on 30 open problems collected from mathematical researchers. Among the 21 solutions that received human feedback, 5 were judged completely correct, 2 more were judged promising pending final verification, and a further 8 contained useful partial progress. In this short paper, we describe the development of ProofCouncil and the agent-building library used to create it, which we release as open source to the community.

---


### 56. [Neural Collapse Is Forbidden: Information Floors in Language Models](https://arxiv.org/abs/2607.09487)

**<font color=#1a73e8>作者：</font>** Bruno Abrahao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Within-class variance in language-model representations is commonly read as incomplete neural collapse. We argue it is allocated information storage, and that the allocation obeys a law. A one-line centering identity voids a family of simplex equiangular-tight-frame claims, including our own earlier ones; in dimensionless variance shares across 14 models, macro-category structure carries only 4-12% of representational variance and within-token context carries 79-91%, stable across a 100x parameter range. On the theory side, token-level weight decay penalizes a category in proportion to its type count, not its occurrence mass, reducing next-token prediction to an imbalanced K-class problem whose optimum orders category norms by type count. A converse floor, proved for binary categories, forces within-category dispersion to be at least proportional to the conditional mutual information I(token; context | category). The law holds: identity dispersion, not total variance, tracks this information across every tested model and partition, under a model-free estimate and even across models, where one model's information predicts another's dispersion; and over pretraining the category share overshoots, decays, and partially recovers, because the information it must carry never left.

---


### 57. [Multimodal Reward Hacking in Reinforcement Learning](https://arxiv.org/abs/2607.09492)

**<font color=#1a73e8>作者：</font>** Jiayu Yao, Yiwei Wang, Anmeng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is increasingly used to align multimodal large language models (MLLMs), but higher rewards do not always imply better task performance. This risk is amplified when visual evidence is evaluated by text-only or weakly grounded rewards. We study reward hacking in MLLM RL across safety VQA, chart VQA, and stress-test settings, varying reward design, data ambiguity, model scale (2B-32B), and RL algorithm (GRPO, RLOO, DAPO). We introduce Newly Rewarded Failure Rate (NRFR), which measures failures among samples whose proxy reward improves over the SFT baseline. Outcome-only rewards cause severe hacking, reaching 48.1% Reward Hacking Rate (RHR), while NRFR exceeding RHR shows that RL creates new failures rather than merely inheriting them. Scaling reduces but does not eliminate hacking: even the 32B model retains a 54.9% worse rate under outcome-only rewards, whereas answer-aware rewards improve the oracle trend at every scale. Robustness is also algorithm- and scale-dependent: GRPO is consistently most resistant, RLOO remains vulnerable, and DAPO improves substantially from 2B to 8B. Visual-evidence rewards help only with reliable verification: keyword-based checks increase hacking, while VLM-as-judge semantic verification reduces it. Overall, multimodal reward hacking is a systematic result of optimizing imperfect rewards, and robust alignment requires rewards and verifiers that remain reliable under optimization pressure.

---


### 58. [Shared Selective Persistent Memory for Agentic LLM Systems](https://arxiv.org/abs/2607.09493)

**<font color=#1a73e8>作者：</font>** Sanjana Pedada, Aditya Dhavala, Neelraj Patil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic LLM systems that generate code through multi-turn tool use face a fundamental context problem: each session starts from zero, discarding the configuration choices, domain constraints, data schemas, and tool-use patterns that made previous sessions productive. Naively persisting entire conversation histories is token-inefficient and counterproductive: irrelevant context degrades generation quality. We introduce shared selective persistent memory, an architecture that identifies and retains four categories of reusable context (task specifications, data schemas, tool configurations, and output constraints) while discarding session-specific reasoning traces. Crucially, this memory is shared: workspaces encapsulating selective memory can be transferred across users with role-based access control, enabling collaborative reuse without redundant specification. We implement it in a deployed collaborative workspace platform where LLM agents produce, edit, and maintain git-versioned artifacts (dashboards, reports, and data-driven documents) from heterogeneous sources (CSV, SQL, REST APIs, and MCP servers). A complementary zero-token data refresh mechanism decouples generated programs from runtime data, enabling artifact reuse without re-invocation. Across three enterprise scenarios, shared selective persistent memory achieves 96% task completion (vs. 79% without memory and 71% with full history). Zero-token refresh eliminates LLM re-invocation for recurring updates (14x task-time reduction), while summary-driven generation cuts per-invocation token cost by 97x versus raw data injection. A replication on four public datasets confirms generalizability, with zero-token refresh succeeding in 12/12 trials. Notably, naive full-history persistence actively degrades completion by biasing the agent with stale traces, while selective memory outperforms both extremes.

---


### 59. [All Explanations are Wrong, But Many Are Useful: Exploring the Rashomon Explanation Set with Large Language Models](https://arxiv.org/abs/2607.09502)

**<font color=#1a73e8>作者：</font>** Pan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explaining machine-learning models is increasingly important for decision-making and consumer trust, yet it is widely believed to come at a cost: existing Explainable AI (XAI) methods suffer from a persistent accuracy-explainability trade-off. We argue that this trade-off is not fundamental, but an artifact of treating explanation and prediction as separate objectives; when properly coupled, they become complementary, so that equipping a model to explain itself improves, rather than degrades, its accuracy. We introduce the Rashomon Explanation paradigm, which builds a set of faithful, prediction-guiding explanations rather than a single one, and prove that this set is generally non-empty and that explanation fidelity bounds the performance of the models it guides. To explore this set, we propose RashomonLLM, an Explanation-Prediction-Reflection agentic workflow that generates explanations in natural language by iteratively aligning them with predictions, and we prove it converges and recovers the full set. Across customer-churn classification, clinical survival regression, and industrial click-through prediction on large-scale live-streaming logs, RashomonLLM significantly outperforms state-of-the-art prediction and XAI baselines on both accuracy and explanation quality, with gains driven by explanation fidelity and robust to distribution shifts, temporal splits, and seeds. Our framework thus advances business performance while laying the groundwork for consumer trust.

---


### 60. [What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility](https://arxiv.org/abs/2607.09503)

**<font color=#1a73e8>作者：</font>** Filippo Ziliotto, Luciano Serafini, Lamberto Ballan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A fundamental challenge in 3D reconstruction and robotic localization is co-visibility: determining which image pairs share overlapping visible surfaces, particularly in scenarios with minimal overlap. We demonstrate that VGGT implicitly encodes co-visibility as an emergent behavior: without any supervision for this task, its internal representations exhibit a clear hierarchical structure mirroring that of large language models, i.e. early layers build a 3D-aware scene representation, while late layers act as dedicated co-visibility reasoners. In particular, we identify layer L17 as a negative anchor that consistently routes non-co-visible pairs for this backbone, regardless of the evaluation setting, providing task-grounded evidence of layer specialization in a geometry-grounded foundation model. Building on this, we introduce Co-VGGT, which freezes VGGT and trains only a lightweight layer-wise mixture-of-experts head (less than 7.5M parameters) to classify co-visibility from RGB alone, treating each layer as a specialized expert whose geometric abstraction is adaptively weighted per input pair. On the Co-VisiON benchmark, Co-VGGT surpasses the human annotation baseline and improves over prior work by more than 25% pairwise and 10% multiview. Pairwise predictions are well-calibrated (ECE=0.030), enabling direct use as edge weights in visibility graphs for downstream SfM and SLAM pipelines without post-hoc correction. Code and data are available.

---


### 61. [SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction](https://arxiv.org/abs/2607.09521)

**<font color=#1a73e8>作者：</font>** Chongyu Qu, Can Cui, Zhengyi Lu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does every cancer patient truly need a complete diagnostic workup for accurate survival prediction? In multimodal clinical oncology, diagnostic modalities follow a clinically mandated order of escalating burden -- from demographics collected at intake to genomic profiling requiring specialized tissue analysis. Current multimodal survival methods either assume all modalities are available or passively handle missing data, but none actively reason about whether acquiring the next modality is justified for a given patient along this ordered workflow. We formulate this as a sequential decision problem and propose SAGEAgent (Sequential Acquisition Guided by Experience), a self-evolving LLM-based clinical agent that decides which diagnostic modalities to acquire for each patient, balancing predictive accuracy against clinical invasiveness. SAGEAgent reasons about each patient's evolving diagnostic state through clinical tools that translate numerical predictions into text, an episodic memory that retrieves similar past cases, and a semantic memory that accumulates reusable decision patterns from experience. Experiments on a glioma cohort combining TCGA-LGG, TCGA-GBM, and BraTS with four diagnostic modalities demonstrate that SAGEAgent achieves competitive survival prediction accuracy while reducing average acquisition burden by 55%.

---


### 62. [ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts](https://arxiv.org/abs/2607.09526)

**<font color=#1a73e8>作者：</font>** Jiawen Li, Tian Guan, Huijuan Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models are reshaping computational pathology, yet their capabilities remain shaped by pretraining objectives, data sources, and spatial scales, fragmenting complementary expertise across separate backbones. Here we present ALICE, a unified foundation model trained through multi-stage agglomerative distillation that sequentially distills eight vision-only, vision-language, and slide-level teacher models into dedicated modules of a single backbone. ALICE is pretrained on 24,985,184 tile-level pathology images and 155,604 high-resolution images, and evaluated across 21 task scenarios, 96 downstream tasks, and 48 data sources, spanning region-of-interest tissue analysis, vision-language multimodal evaluation, and whole-slide clinical assessment. In all three evaluation settings, ALICE achieved the best average rank among task-matched pathology foundation models. These results demonstrate that agglomerative distillation can consolidate complementary capabilities from specialized models into a unified backbone for broad computational pathology applications. The model is available at this https URL.

---


### 63. [TCLA: Training-Free Class-wise Logit Adaptation for Medical Vision-Language Models](https://arxiv.org/abs/2607.09562)

**<font color=#1a73e8>作者：</font>** Tianyou Jiang, Ziyu Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Models (VLMs) exhibit strong zero-shot performance, yet their effectiveness still declines on out-of-distribution (OOD) data due to domain shifts and class bias inherited from large-scale pretraining. Existing few-shot adaptation methods typically introduce additional trainable components, which can be unstable in extremely low-data regimes (e.g., 1-shot), and lack robustness on different medical data. We present TCLA, a purely training-free few-shot adaptation method for Medical VLMs, which is fast and model-agnostic. TCLA corrects inference logits based on a small set of support samples, boosting pretrained VLMs performance by improving inter-class deconfusion and reducing domain shift. Extensive experiments on nine datasets across multiple medical imaging modalities including X-ray, Ultrasound, MRI, CT, Histopathology, demonstrate that TCLA consistently improves OOD performance of Medical VLMs and, in most of cases, outperforms existing training-based adaptation methods.

---


### 64. [Promptable Concept Segmentation from Above: Evaluating SAM 3's Zero-Shot and One-Shot Capabilities in Remote Sensing](https://arxiv.org/abs/2607.09583)

**<font color=#1a73e8>作者：</font>** Mohammad Dabaja, Turgay Celik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The deployment of large-scale foundation models, such as the Segment Anything Model 3 (SAM 3), promises a transition toward open-vocabulary, training-free computer vision. However, their capacity to generalize out-of-distribution to the complex, top-down geometric structures of Earth Observation imagery remains largely unquantified. Driven by SAM 3's performance disparities in highly specialized domains, we present a comprehensive, multi-task empirical evaluation across remote sensing scene classification, object detection, and instance segmentation under strict zero-shot and one-shot constraints. To achieve this, we introduce a structural adaptation of SAM 3 by repurposing its decoupled binary presence head into a standalone zero-shot classifier. Furthermore, by systematically isolating textual and visual prompt modalities across five configurations, we explicitly diagnose the alignment mechanics within the model's multimodal decoder. Our findings reveal severe cross-modal interference: while visual prompts successfully align the decoder to complex remote sensing geometry, textual prompts inject misaligned, ground-level semantic bias, actively degrading coordinate regression. To benchmark these capabilities without resource-intensive training, we formulate a novel training-free proxy evaluation protocol for Generalized Zero-Shot tasks (scene classification and instance segmentation). Ultimately, our results demonstrate that SAM 3 avoids the overfitting commonly seen in legacy domain-adapted models, achieving high Harmonic Mean scores in segmentation tasks. However, it remains fundamentally constrained by sub-pixel resolution limits and overhead semantic blind spots, charting a definitive mandate for parameter-efficient geospatial fine-tuning of its multimodal decoder.

---


### 65. [TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems](https://arxiv.org/abs/2607.09586)

**<font color=#1a73e8>作者：</font>** Hannah M. Liu, Rhea Saxena, Shiv Asthana  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The proliferation of agentic AI systems across enterprise and public-sector contexts has outpaced the capacity of general-purpose AI risk frameworks to classify and govern them. In this paper, we introduce the TrustX Agent Risk Classification Framework, a structured, repeatable instrument that can be applied to seven types of agentic AI systems and is grounded in foundational pre-existing AI governance frameworks. At the core of the framework is a twelve-dimension scoring rubric that robustly quantifies the risk. This rubric is combined with other components, such as the GPA + IAT classification model and the five-level autonomy framework derived from existing literature. These inputs produce a three-tier governance output with mapped control recommendations. A specialised Coding Assistant extension is also included to account for nuances specific to this type of agentic AI system. We then use an illustrative example to show our framework in practice. ARC is intended for AI governance practitioners, risk officers, developers, and regulators, and it will regularly undergo iteration as we continue to expand it and make it more robust. The community can access the interactive framework here: this https URL

---


### 66. [Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation](https://arxiv.org/abs/2607.09600)

**<font color=#1a73e8>作者：</font>** Kaiji Zhou, Ales Leonardis, Yue Feng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enhancing the reasoning capabilities of large language model (LLM) agents requires effective orchestration of diverse expert models and tools. However, existing frameworks typically call APIs based on coarse-grained matching between tasks and the functions of expert models or tools, while overlooking critical factors such as performance variability and cost efficiency among functionally similar alternatives. To address this, we propose Agora, a framework that introduces an incentive-compatible auction mechanism for dynamically allocating tasks to expert models and tools. By treating reasoning steps as tradeable items, Agora enables agents to bid based on their rectified competence-ensuring that critical logic is routed to the most capable solver rather than the most overconfident one. Evaluations across five benchmarks show that Agora improves over matched single-model, routing, and cascade baselines under comparable candidate pools, while exposing a controllable cost-quality trade-off through a single auction parameter.

---


### 67. [Task-Specific Multimodal Question Answering Agents via Confidence Calibration and Incremental Reasoning for QANTA 2026](https://arxiv.org/abs/2607.09623)

**<font color=#1a73e8>作者：</font>** Nirjhar Das, Md. Al-Mamun Provath  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present our submission to the QANTA 2026 shared challenge at the ICML 2026 Workshop on Efficient Multimodal Question Answering (EMM-QA). Quanta evaluates multimodal quizbowl systems that answer pyramid-style questions from incrementally revealed text and accompanying images while operating under realistic efficiency constraints. The challenge consists of two distinct tasks: Tossup questions, which require deciding when to answer under uncertainty, and Bonus questions, which emphasize accurate answer selection and human adoption. To address these differing objectives, we develop a task-specific two-agent architecture. Our Tossup agent utilizes a GPT-4o-mini-class model (referred to as GPT-4.1-mini in the competition logs) with confidence-calibrated answering and a domain-specific numeric reasoning policy that reduces overconfident predictions from isolated quantitative clues. Our Bonus agent uses GPT-4o-class model (referred to as GPT-4.1) with leadin-aware reasoning, structured relational reasoning, and multimodal evidence integration to improve exact answer selection. Rather than relying on a retrieval pipeline or model ensembles, our approach emphasizes efficient reasoning policies and confidence calibration within a hosted-only environment. Our system achieved the highest overall leaderboard score of 0.402, including a Tossup score of 0.238 and a Bonus Effect score of 0.164. The results demonstrate that lightweight, task-specific reasoning strategies can provide strong performance on resource-constrained multimodal question answering benchmarks.

---


### 68. [Evolution of Accuracy and Visual-Cognitive Errors in a Decade of Vision-Language AI Models](https://arxiv.org/abs/2607.09654)

**<font color=#1a73e8>作者：</font>** Shravan Murlidaran, Miguel P. Eckstein  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) have made remarkable progress in visual reasoning during the last decade. Most evaluations have used simple scenes (MS-COCO) that do not showcase complex human interactions or behaviors, only a handful of non-curated human descriptions as a benchmark, and have not focused on understanding the model's error types. Here, we introduce the Complex Social Behavior (CSB) dataset, containing 100 images depicting complex social interactions/behaviors. We analyze the progression of scene descriptions over a decade (2017-2025) of VLMs (four pre-Multimodal Large Language Models, MLLMs, and five MLLMs). We evaluate the accuracy of the models and 20 human descriptions relative to a gold standard on the CSB dataset and on a sample from MS-COCO. We analyzed five visual-cognitive error types: object detection, recognition, hallucination, scene understanding, and spatial dependence. The CSB dataset showed a more pronounced improvement than MS-COCO in scene description accuracy, with pre-MLLMs achieving much lower accuracy than the bottom-ranked human descriptions and MLLMs attaining accuracies similar to the top-ranked human descriptions. We show that MLLMs have eliminated the gap in scene description accuracy between simpler MS-COCO scenes and scenes depicting complex behaviors (CSB). MLLMs have almost eliminated all error types in our tested datasets, except for occasionally relying on different image regions for scene descriptions than humans do (spatial dependence error). We also show that detection, recognition, and hallucination errors have the highest impact on scene description accuracy. Together, our findings provide a more thorough evaluation of how visual language models have advanced over the last decade.

---


> [!TIP]
> 当前位于：**51-68**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-68**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

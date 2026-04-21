# 🧠 大模型相关研究 | 2026年04月22日

> 本类共 **353** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 201. [RS-HyRe-R1: A Hybrid Reward Mechanism to Overcome Perceptual Inertia for Remote Sensing Images Understanding](https://arxiv.org/abs/2604.17504)

**<font color=#1a73e8>作者：</font>** Gaozhi Zhou, Hu He, Peng Shen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training substantially improves remote sensing vision-language models (RS-VLMs). However, when handling complex remote sensing imagery (RSI) requiring exhaustive visual scanning, models tend to rely on localized salient cues for rapid inference. We term this RL-induced bias "perceptual inertia". Driven by reward maximization, models favor quick outcome fitting, leading to two limitations: cognitively, overreliance on specific features impedes complete evidence construction; operationally, models struggle to flexibly shift visual focus across tasks. To address this bias and encourage comprehensive visual evidence mining, we propose RS-HyRe-R1, a hybrid reward framework for RSI understanding. It introduces: (1) a spatial reasoning activation reward that enforces structured visual reasoning; (2) a perception correctness reward that provides adaptive quality anchors across RS tasks, ensuring accurate geometric and semantic alignment; and (3) a visual-semantic path evolution reward that penalizes repetitive reasoning and promotes exploration of complementary cues to build richer evidence chains. Experiments show RS-HyRe-R1 effectively mitigates "perceptual inertia", encouraging deeper, more diverse reasoning. With only 3B parameters, it achieves state-of-the-art performance on REC, OVD, and VQA tasks, outperforming models up to 7B parameters. It also demonstrates strong zero-shot generalization, surpassing the second-best model by 3.16%, 3.97%, and 2.72% on VQA, OVD, and REC, respectively. Code and datasets are available at this https URL.

---


### 202. [ONTO: A Token-Efficient Columnar Notation for LLM Input Optimization](https://arxiv.org/abs/2604.17512)

**<font color=#1a73e8>作者：</font>** Harshavardhanan Deekeswar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Serialization formats designed for document interchange impose structural overhead that becomes prohibitive when large language models consume operational data at scale. A modest dataset of 1,000 IoT sensor readings serialized as JSON requires approximately 80,000 tokens - the majority spent on repeated field names, nested braces, and structural punctuation rather than semantic content. We present ONTO (Object Notation for Token Optimization), a columnar notation that declares field names once per entity and arranges values in pipe-delimited rows with indentation-based hierarchy. This schema-once, data-many design eliminates per-record key repetition while preserving human readability and nested structure support. Evaluation across three synthetic operational datasets demonstrates 46-51% token reduction versus JSON, with stable scaling from 100 to 1,000 records. Controlled inference benchmarks on Qwen2.5-7B show corresponding 5-10% latency improvement. Comprehension validation confirms no material degradation in LLM task accuracy across lookup, counting, extraction, and aggregation operations when format context is provided. Ablation analysis reveals that key repetition accounts for the majority of JSON overhead, with indentation costs in nested structures explaining the 4-percentage-point gap between flat and hierarchical data. ONTO occupies a previously unfilled position in the serialization landscape: columnar efficiency with hierarchical structure, optimized for LLM context windows rather than document interchange. Code and specification are available at this https URL.

---


### 203. [OPSDL: On-Policy Self-Distillation for Long-Context Language Models](https://arxiv.org/abs/2604.17535)

**<font color=#1a73e8>作者：</font>** Xinsen Zhang, Zhenkai Ding, Tianjun Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extending the effective context length of large language models (LLMs) remains a central challenge for real-world applications. While recent post-training methods have made progress in long-context scaling, they either rely on high-quality supervision data or sparse sequence-level rewards, leading to unstable and inefficient optimization. We propose OPSDL, an On-Policy Self-Distillation method for enhancing the Long-context capabilities of LLMs. Unlike other recent self-distillation methods that inject privileged information and rely on the model's in-context learning ability to act as a teacher, OPSDL leverages the model's own inherently strong short-context capability as a self-teacher to supervise its own generation in long-context scenarios. The model first generates responses conditioned on the full long-context, then the self-teacher provides per-token supervision signals via point-wise reverse KL divergence under the relevant extracted short-context. This dense token-level signal encourages faithful use of relevant evidence and mitigates hallucinations induced by irrelevant context. We evaluate OPSDL on long-context benchmarks across a range of models from 7B to 32B parameters. Results show consistent and substantial improvements across varying context lengths, outperforming standard post-training approaches such as SFT and DPO with higher sample efficiency. Notably, these gains are achieved without degrading general short-context performance. These findings highlight the effectiveness of OPSDL as a scalable and stable approach for long-context learning.

---


### 204. [PoliLegalLM: A Technical Report on a Large Language Model for Political and Legal Affairs](https://arxiv.org/abs/2604.17543)

**<font color=#1a73e8>作者：</font>** Yuting Huang, Yinghao Hu, Qian Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable success in general-domain tasks, yet their direct application to the legal domain remains challenging due to hallucinated legal citations, incomplete knowledge coverage, and weak structured reasoning. To address these issues, we propose PoliLegalLM, a domain-specific large language model tailored for political and legal applications. Our approach adopts a unified training framework that integrates continued pretraining, progressive supervised fine-tuning, and preference-based reinforcement learning to jointly enhance legal knowledge grounding, task alignment, and reasoning capability. We construct a large-scale, high-quality legal corpus and design a structured post-training pipeline, enabling the model to effectively learn domain-specific knowledge and adapt to diverse legal tasks. We evaluate PoliLegalLM on three representative benchmarks, including LawBench, LexEval, and a real-world dataset, PoliLegal. Experimental results demonstrate that PoliLegalLM achieves strong and consistent performance, outperforming competitive models of similar scale and remaining highly competitive with significantly larger models, while achieving the best results on real-world legal scenarios. These results highlight the effectiveness of our training paradigm and the practical value of domain-specific LLMs for real-world legal applications.

---


### 205. [COSEARCH: Joint Training of Reasoning and Document Ranking via Reinforcement Learning for Agentic Search](https://arxiv.org/abs/2604.17555)

**<font color=#1a73e8>作者：</font>** Hansi Zeng, Liam Collins, Bhuvesh Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic search -- the task of training agents that iteratively reason, issue queries, and synthesize retrieved information to answer complex questions -- has achieved remarkable progress through reinforcement learning (RL). However, existing approaches such as Search-R1, treat the retrieval system as a fixed tool, optimizing only the reasoning agent while the retrieval component remains unchanged. A preliminary experiment reveals that the gap between an oracle and a fixed retrieval system reaches up to +26.8% relative F1 improvement across seven QA benchmarks, suggesting that the retrieval system is a key bottleneck in scaling agentic search performance. Motivated by this finding, we propose CoSearch, a framework that jointly trains a multi-step reasoning agent and a generative document ranking model via Group Relative Policy Optimization (GRPO). To enable effective GRPO training for the ranker -- whose inputs vary across reasoning trajectories -- we introduce a semantic grouping strategy that clusters sub-queries by token-level similarity, forming valid optimization groups without additional rollouts. We further design a composite reward combining ranking quality signals with trajectory-level outcome feedback, providing the ranker with both immediate and long-term learning signals. Experiments on seven single-hop and multi-hop QA benchmarks demonstrate consistent improvements over strong baselines, with ablation studies validating each design choice. Our results show that joint training of the reasoning agent and retrieval system is both feasible and strongly performant, pointing to a key ingredient for future search agents.

---


### 206. [SafeAgent: A Runtime Protection Architecture for Agentic Systems](https://arxiv.org/abs/2604.17562)

**<font color=#1a73e8>作者：</font>** Hailin Liu, Eugene Ilyushin, Jie Ni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are vulnerable to prompt-injection attacks that propagate through multi-step workflows, tool interactions, and persistent context, making input-output filtering alone insufficient for reliable protection. This paper presents SafeAgent, a runtime security architecture that treats agent safety as a stateful decision problem over evolving interaction trajectories. The proposed design separates execution governance from semantic risk reasoning through two coordinated components: a runtime controller that mediates actions around the agent loop and a context-aware decision core that operates over persistent session state. The core is formalized as a context-aware advanced machine intelligence and instantiated through operators for risk encoding, utility-cost evaluation, consequence modeling, policy arbitration, and state synchronization. Experiments on Agent Security Bench (ASB) and InjecAgent show that SafeAgent consistently improves robustness over baseline and text-level guardrail methods while maintaining competitive benign-task performance. Ablation studies further show that recovery confidence and policy weighting determine distinct safety-utility operating points.

---


### 207. [Multi-Camera Self-Calibration in Sports Motion Capture: Leveraging Human and Stick Poses](https://arxiv.org/abs/2604.17567)

**<font color=#1a73e8>作者：</font>** Fan Yang, Changsoo Jung, Ryosuke Kawamura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-camera systems are widely employed in sports to capture the 3D motion of athletes and equipment, yet calibrating their extrinsic parameters remains costly and labor-intensive. We introduce an efficient, tool-free method for multi-camera extrinsic calibration tailored to sports involving stick-like implements (e.g., golf clubs, bats, hockey sticks). Our approach jointly exploits two complementary cues from synchronized multi-camera videos: (i) human body keypoints with unknown metric scale and (ii) a rigid stick-like implement of known length. We formulate a three-stage optimization pipeline that refines camera extrinsics, reconstructs human and stick trajectories, and resolves global scale via the stick-length constraint. Our method achieves accurate extrinsic calibration without dedicated calibration tools. To benchmark this task, we present the first dataset for multi-camera self-calibration in stick-based sports, consisting of synthetic sequences across four sports categories with 3 to 10 cameras. Comprehensive experiments demonstrate that our method delivers SOTA performance, achieving low rotation and translation errors. Our project page: this https URL.

---


### 208. [PBSBench: A Multi-Level Vision-Language Framework and Benchmark for Hematopathology Whole Slide Image Interpretation](https://arxiv.org/abs/2604.17570)

**<font color=#1a73e8>作者：</font>** Yuanlong Wang, Weichi Chen, Adrian Rajab 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Peripheral Blood Smear (PBS) is a critical microscopic examination in hematopathology that yields whole-slide imaging (WSI). Unlike solid tissue pathology, PBS interpretation focuses on individual cell morphologies rather than tissue architecture, making it distinct in both visual characteristics and diagnostic reasoning. However, current multimodal large language models (MLLMs) for pathology are primarily developed on solid-tissue WSIs and struggle to generalize to PBS. To bridge this gap, we construct PBSInstr, the first vision-language dataset for PBS interpretation, comprising 353 PBS WSIs paired with microscopic impression paragraphs and 29k cell-level image crops annotated with cell type labels and morphological descriptions. To facilitate instruction tuning, PBSInstr further includes 27k question-answer (QA) pairs for cell crops and 1,286 QA pairs for PBS slides. Building upon PBSInstr, we develop PBS-VL, a hematopathology-tailored vision-language model for multi-level PBS interpretation at both cell and slide levels. To comprehensively evaluate PBS understanding, we construct PBSBench, a visual question answering (VQA) benchmark featuring four question categories and six PBS interpretation tasks. Experiments show that PBS-VL outperforms existing general-purpose and pathology MLLMs, underscoring the value of PBS-specific data. We release our code, datasets, and model weights to facilitate future research. Our proposed framework lays the foundation for developing practical AI assistants supporting decision-making in hematopathology.

---


### 209. [Beyond Static Snapshots: A Grounded Evaluation Framework for Language Models at the Agentic Frontier](https://arxiv.org/abs/2604.17573)

**<font color=#1a73e8>作者：</font>** Jazmia Henry  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We argue that current evaluation frameworks for large language models (LLMs) suffer from four systematic failures that make them structurally inadequate for assessing deployed, agentic systems: distributional invalidity (evaluation inputs do not reflect real interaction distributions), temporal invalidity (evaluations are post-hoc rather than training-integrated), scope invalidity (evaluations measure single-turn outputs rather than long-horizon trajectories), and process invalidity (evaluations assess outputs rather than reasoning). These failures compound critically in RLHF, where reward models are evaluated under conditions that do not hold during RL training, making reward hacking a predictable consequence of evaluation design rather than a training pathology. We propose the Grounded Continuous Evaluation (GCE) framework and present ISOPro, a simulation-based fine-tuning and evaluation system. ISOPro replaces the learned reward model with a deterministic ground-truth verifier, eliminating reward hacking by construction in verifiable-reward domains, and operates on LoRA adapter weights updatable on CPU, reducing the hardware barrier by an order of magnitude. We validate ISOPro on a resource-constrained scheduling domain with six difficulty tiers, demonstrating capability emergence visible only through continuous evaluation, an implicit curriculum that forms without researcher curation, and a 3x accuracy improvement over zero-shot baselines, all on consumer hardware with 0.216% trainable parameters.

---


### 210. [Beyond Fine-Tuning: In-Context Learning and Chain-of-Thought for Reasoned Distractor Generation](https://arxiv.org/abs/2604.17574)

**<font color=#1a73e8>作者：</font>** Elaf Alhazmi, Quan Z. Sheng, Wei Emma Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distractor generation (DG) remains a labor-intensive task that still significantly depends on domain experts. The task focuses on generating plausible yet incorrect options, known as distractors, for multiple-choice questions. A reliable distractor must be contextually relevant to the question and able to mislead examinees through implicit reasoning when identifying the correct answer. While a recent method integrates fine-tuning pre-trained encoder-decoder models with contrastive learning to generate semantically relevant distractors for a given question-answer, it often fails to capture the underlying reasoning process that experts utilize when selecting distractors in benchmarks. In this paper, we explore large language models (LLMs) reasoning for DG through in-context learning with unsupervised semantic retrieval for selecting few-shot examples. We design a rationale-augmented DG framework that jointly generates distractors and their rationales for a given question-answer. Extensive experiments on six benchmarks, with varying average distractor lengths and domains, demonstrate that prompting LLMs with few-shot examples substantially improves the performance compared to recent DG models. It outperforms recent approaches and achieves state-of-the-art results in generating reasoned distractors that align with human-labeled benchmarks.

---


### 211. [DGSSM: Diffusion guided state-space models for multimodal salient object detection](https://arxiv.org/abs/2604.17585)

**<font color=#1a73e8>作者：</font>** Suklav Ghosh, Arijit Sur, Pinaki Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Salient object detection (SOD) requires modeling both long-range contextual dependencies and fine-grained structural details, which remains challenging for convolutional, transformer-based, and Mamba-based state space models. While recent Mamba-based state space approaches enable efficient global reasoning, they often struggle to recover precise object boundaries. In contrast, diffusion models capture strong structural priors through iterative denoising, but their use in discriminative dense prediction is still limited due to computational cost and integration challenges. In this work, we propose DGSSM, a diffusion-guided state space (Mamba) framework that formulates multimodal salient object detection as a progressive denoising process. The framework integrates diffusion structural priors with multi-scale state space encoding, adaptive saliency prompting, and an iterative Mamba diffusion refinement mechanism to improve boundary accuracy. A boundary-aware refinement head and self-distillation strategy further enhance spatial coherence and feature consistency. Extensive experiments on 13 public benchmarks across RGB, RGB-D, and RGB-T settings demonstrate that DGSSM consistently outperforms state-of-the-art methods across multiple evaluation metrics while maintaining a compact model size. These results suggest that diffusion-guided state space modeling is an effective and generalizable paradigm for multimodal dense prediction tasks.

---


### 212. [Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity](https://arxiv.org/abs/2604.17609)

**<font color=#1a73e8>作者：</font>** Leon Engländer, Sophia Althammer, Ahmet Üstün 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are assumed to integrate environmental observations into their reasoning: discovering highly relevant but unexpected information should naturally lead to a model exploiting its own discoveries. We show that this assumption is false for current LLM-based agents, which struggle to reflect or react to unexpected information. Across three benchmarks (Terminal-Bench, SWE-Bench, AppWorld), we inject complete task solutions into the agent environments to deliberately expose a task's solution to a model. While agents discover these solutions on Terminal-Bench in 79-81% of runs, they interact, or exploit, them in only 37-50% of cases. This gap is starkest in AppWorld: agents see documentation stating that a command "returns the complete solution to this task" in over 90% of attempts but exploit this in fewer than 7% of trials. We show that agents lack what we call environmental curiosity: the capability to recognize and investigate unexpected but relevant observations in response to environmental stimuli. We identify three main factors influencing environmental curiosity: available tools in the agent scaffold, test-time compute, and training data distribution. Our findings identify configurations that maximize curiosity also achieve the best performance on the unmodified benchmarks. Yet even jointly optimized agents still ignore discovered solutions in the majority of trials: current agents use the environment to fetch expected information, but not to revise their strategy or maximally exploit useful stimuli.

---


### 213. [STEP-PD: Stage-Aware and Explainable Parkinson's Disease Severity Classification Using Multimodal Clinical Assessments](https://arxiv.org/abs/2604.17611)

**<font color=#1a73e8>作者：</font>** Md Mezbahul Islam, John Michael Templeton, Christian Poellabauer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parkinson's disease (PD) is a progressive disorder in which symptom burden and functional impairment evolve over time, making severity staging essential for clinical monitoring and treatment planning. However, many computational studies emphasize binary PD detection and do not fully use repeated follow-up clinical assessments for stage-aware prediction. This study proposes STEP-PD, a severity-aware machine learning framework to classify PD severity using clinically interpretable boundaries. It leverages all available visits from the Parkinson's Progression Markers Initiative (PPMI) and integrates routinely collected subjective questionnaires and objective clinician-assessed measures. Disease severity is defined using Hoehn and Yahr staging and grouped into three clinically meaningful categories: Healthy, Mild PD (stages 1-2), and Moderate-to-Severe PD (stages 3-5). Three binary classification problems and a three-class severity task were evaluated using stratified cross-validation with imbalance-aware training. To enhance interpretability, SHAP was used to provide global explanations and local patient-level waterfall explanations. Across all tasks, XGBoost achieved the strongest and most stable performance, with accuracies of 95.48% (Healthy vs. Mild), 99.44% (Healthy vs. Moderate-to-Severe), and 96.78% (Mild vs. Moderate-to-Severe), and 94.14% accuracy with 0.8775 Macro-F1 for three-class severity classification. Explainability results highlight a shift from early motor features to progression-related axial and balance impairments. These findings show that multimodal clinical assessments within the PPMI cohort can support accurate and interpretable visit-level PD severity stratification.

---


### 214. [Characterizing Model-Native Skills](https://arxiv.org/abs/2604.17614)

**<font color=#1a73e8>作者：</font>** Feiyang Kang, Mahavir Dabas, Myeongseob Ko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skills are a natural unit for describing what a language model can do and how its behavior can be changed. However, existing characterizations rely on human-written taxonomies, textual descriptions, or manual profiling pipelines--all external hypotheses about what matters that need not align with the model's internal representations. We argue that when the goal is to intervene on model behavior, skill characterization should be *model-native*: grounded in the model's own representations rather than imposed through external ontologies. We instantiate this view by recovering a compact orthogonal basis from sequence-level activations. The resulting basis is semantically interpretable but need not correspond to any predefined human ontology; instead, it captures axes of behavioral variation that the model itself organizes around. We validate this characterization on reasoning post-training, using the recovered basis for both SFT data selection and inference-time steering. We develop lightweight proxy interventions to identify which directions are most useful for a given model. Across Llama3-8B and Qwen2.5-3B, selecting data along those directions improves Pass@1 by up to 20% on MATH and 41% on AMC, outperforming data selection based on human-characterized skills. Because the basis lives in activation space, the same directions also serve as steering vectors at inference time, improving Pass@8 by up to 4.8% on MATH--an intervention that human-characterized skills cannot support. We further validate the characterization on safety alignment, where selecting adversarial training data for model-native skill coverage rather than textual diversity yields more sample-efficient learning. These results suggest that recovering skills from the model's own representations, rather than imposing them externally, provides a more effective foundation for intervening on model behavior. Codes are open-sourced.

---


### 215. [WhatIf: Interactive Exploration of LLM-Powered Social Simulations for Policy Reasoning](https://arxiv.org/abs/2604.17615)

**<font color=#1a73e8>作者：</font>** Yuxuan Li, Kyzyl Monteiro, Hirokazu Shirado 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Policymakers in domains such as emergency management, public health, and urban planning must make decisions under deep uncertainty, where outcomes depend on how large populations interpret information, coordinate, and adopt over time. Existing tools only partially support this process: tabletop exercises enable collaborative discussion but lack dynamic feedback, while computational simulations capture population dynamics but are designed for offline analysis. We present WhatIf, an interactive system that enables policymakers to steer, inspect, and compare LLM-powered social simulations in real time. Informed by a formative study in emergency preparedness planning, we derive four design requirements for interactive policy simulations: fluid steering, real-time scale, collaborative exploration, and multi-level interpretability. We developed WhatIf guided by these requirements and evaluated it with five preparedness professionals across three disaster evacuation scenarios. Our findings show that participants used the system as a space for iterative branching and comparison rather than evaluating fixed plans; reflected on tacit planning assumptions when agent behavior violated expectations; surfaced previously unrecognized planning vulnerabilities; and grounded their reasoning in inspectable agent-level cases rather than aggregate outputs alone. These findings suggest broader design implications for LLM-powered social simulation systems: designing such systems as interactive, shared reasoning environments -- rather than offline predictive tools -- can better support expert decision-making under deep uncertainty.

---


### 216. [KnowledgeBerg: Evaluating Systematic Knowledge Coverage and Compositional Reasoning in Large Language Models](https://arxiv.org/abs/2604.17621)

**<font color=#1a73e8>作者：</font>** Xiao Zhang, Qianru Meng, Yongjian Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many real-world questions appear deceptively simple yet implicitly demand two capabilities: (i) systematic coverage of a bounded knowledge universe and (ii) compositional set-based reasoning over that universe, a phenomenon we term "the tip of the iceberg." We formalize this challenge through two orthogonal dimensions: knowledge width, the cardinality of the required universe, and reasoning depth, the number of compositional set operations. We introduce KnowledgeBerg, a benchmark of 4,800 multiple-choice questions derived from 1,183 enumeration seeds spanning 10 domains and 17 languages, with universes grounded in authoritative sources to ensure reproducibility. Representative open-source LLMs demonstrate severe limitations, achieving only 5.26-36.88 F1 on universe enumeration and 16.00-44.19 accuracy on knowledge-grounded reasoning. Diagnostic analyses reveal three stages of failure: completeness, or missing knowledge; awareness, or failure to identify requirements; and application, or incorrect reasoning execution. This pattern persists across languages and model scales. Although test-time compute and retrieval augmentation yield measurable gains -- up to 4.35 and 3.78 points, respectively -- substantial gaps remain, exposing limitations in how current LLMs organize structured knowledge and execute compositional reasoning over bounded domains. The dataset is available at this https URL

---


### 217. [SLO-Guard: Crash-Aware, Budget-Consistent Autotuning for SLO-Constrained LLM Serving](https://arxiv.org/abs/2604.17627)

**<font color=#1a73e8>作者：</font>** Christian Lysenstøen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving large language models under latency service-level objectives (SLOs) is a configuration-heavy systems problem with an unusually failure-prone search space: many plausible configurations crash outright or miss user-visible latency targets, and standard black-box optimizers treat these failures as wasted trials. We present SLO-Guard, a crash-aware autotuner for vLLM serving that treats crashes as first-class observations. SLO-Guard combines a feasible-first Thermal Budget Annealing (TBA) exploration phase with a warm-started Tree-structured Parzen Estimator (TPE) exploitation phase; the handoff replays all exploration history, including crashes encoded as extreme constraint violations. We additionally contribute a configuration-repair pass, a GPU-aware KV-cache memory guard, and a four-category crash taxonomy.
We evaluate SLO-Guard on Qwen2-1.5B served with vLLM 0.19 on an NVIDIA A100 40GB. Across a pre-specified five-seed study, both SLO-Guard and uniform random search attain 75/75 feasibility with zero crashes under the corrected concurrent harness, and are statistically tied on best-achieved latency (Mann-Whitney two-sided p=0.84). SLO-Guard's advantage is in budget consistency: more trials in the fast-serving regime (10.20 vs. 7.40 out of 15; one-sided p=0.014) and higher post-handoff consistency (0.876 vs. 0.539; p=0.010). Under concurrent load, SLO-Guard's cross-seed standard deviation on best latency is 4.4x tighter than random search's (2.26 ms vs. 10.00 ms). A harness-replication analysis shows that the consistency findings survive an independent sequential-dispatch measurement condition.
The central claim is not that SLO-Guard finds a better final configuration, but that it spends a fixed tuning budget more predictably once the fast regime has been found.

---


### 218. [Does Welsh media need a review? Detecting bias in Nation.Cymru's political reporting](https://arxiv.org/abs/2604.17628)

**<font color=#1a73e8>作者：</font>** Cai Parry-Jones  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Wales' political landscape has been marked by growing accusations of bias in Welsh media. This paper takes the first computational step toward testing those claims by examining this http URL, a prominent Welsh political news outlet. I use a two-stage natural language processing (NLP) pipeline: (1) a robustly optimized BERT approach (RoBERTa) bias detector for efficient bias discovery and (2) a large language model (LLM) for target-attributed sentiment classification of bias labels from (1). A primary analysis of 15,583 party mentions across 2022-2026 news articles finds that Reform UK attracts biased framing at twice the rate of Plaid Cymru and over three times as negative in mean sentiment (p<0.001). A secondary analysis across four parties across both news and opinion articles shows that Plaid Cymru is the outlier, receiving markedly more favourable framing than any other party. These findings provide evidence of measurable differential framing in a single Welsh political media outlet, supporting calls for a broader review of Welsh media coverage. Furthermore, the two-stage pipeline offers a low-cost, replicable framework for extending this analysis to other Welsh outlets, as well as media ecosystems outside of Wales.

---


### 219. [BioVLM: Routing Prompts, Not Parameters, for Cross-Modality Generalization in Biomedical VLMs](https://arxiv.org/abs/2604.17629)

**<font color=#1a73e8>作者：</font>** Mainak Singha, Tanisha Gupta, Ankit Jha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained biomedical vision-language models (VLMs) such as BioMedCLIP perform well on average but often degrade on challenging modalities where inter-class margins are small and acquisition-specific variations are pronounced, especially under few-shot supervision and when modality priors differ from pretraining corpora substantially. We propose BioVLM, a prompt-learning framework that improves cross-domain generalization without extensive backbone fine-tuning. BioVLM learns a diverse prompt bank and introduces dynamic prompt selection: for each input, it selects the most discriminative prompts via a low-entropy criterion on the predictive distribution, effectively coupling sparse few-shot evidence with rich LLM semantic priors. To strengthen this coupling, we distill high-confidence LLM-derived attributes and enforce robust knowledge transfer through strong/weak augmentation consistency. At test time, BioVLM adapts by choosing modality-appropriate prompts, enabling transfer to unseen categories and domains, while keeping training lightweight and inference efficient. On 11 MedMNIST+ 2D datasets, BioVLM achieves new state of the art across three distinct generalization settings. Codes are available at this https URL.

---


### 220. [Measuring Distribution Shift in User Prompts and Its Effects on LLM Performance](https://arxiv.org/abs/2604.17650)

**<font color=#1a73e8>作者：</font>** Parker Seegmiller, Sarah Masud Preum  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed in dynamic, real-world settings, where the distribution of user prompts can shift substantially over time as new tasks, prompts, and users are introduced to a deployed model. Such natural prompt distribution shift poses a major challenge to LLM reliability, particularly for specialized models designed for narrow domains or user populations. Despite attention to out-of-distribution robustness, there is very limited exploration of measuring natural prompt distribution shift in prior work, and its impact on deployed LLMs remains poorly understood. We introduce the LLM Evaluation under Natural prompt Shift (LENS) framework: a data-centric approach for quantifying natural prompt distribution shift and evaluating its effect on the performance of deployed LLMs. We perform a large-scale evaluation using 192 real-world post-deployment prompt shift settings over time, user group, and geographic axes, training a total of 81 models on 4.68M training prompts, and evaluating on 57.6k prompts. We find that even moderate shifts in user prompt behavior correspond with large performance drops (73% average loss) in deployed LLMs. This performance degradation is particularly prevalent when users from different latent groups and geographic regions interact with models and is correlated with natural prompt distribution shift over time. We systematically characterize how LLM instruction following ability degrades over time and between user groups. Our findings highlight the critical need for data-driven monitoring to ensure LLM performance remains stable across diverse and evolving user populations.

---


### 221. [Infrastructure-Centric World Models: Bridging Temporal Depth and Spatial Breadth for Roadside Perception](https://arxiv.org/abs/2604.17651)

**<font color=#1a73e8>作者：</font>** Siyuan Meng, Chengbo Ai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models, generative AI systems that simulate how environments evolve, are transforming autonomous driving, yet all existing approaches adopt an ego-vehicle perspective, leaving the infrastructure viewpoint unexplored. We argue that infrastructure-centric world models offer a fundamentally complementary capability: the bird's-eye, multi-sensor, persistent viewpoint that roadside systems uniquely possess. Central to our thesis is a spatio-temporal complementarity: fixed roadside sensors excel at temporal depth, accumulating long-term behavioral distributions including rare safety-critical events, while vehicle-borne sensors excel at spatial breadth, sampling diverse scenes across large road networks. This paper presents a vision for Infrastructure-centric World Models (I-WM) in three phases: (I) generative scene understanding with quality-aware uncertainty propagation, (II) physics-informed predictive dynamics with multi-agent counterfactual reasoning, and (III) collaborative world models for V2X communication via latent space alignment. We propose a dual-layer architecture, annotation-free perception as a multi-modal data engine feeding end-to-end generative world models, with a phased sensor strategy from LiDAR through 4D radar and signal phase data to event cameras. We establish a taxonomy of driving world model paradigms, position I-WM relative to LeCun's JEPA, Li Fei-Fei's spatial intelligence, and VLA architectures, and introduce Infrastructure VLA (I-VLA) as a novel unification of roadside perception, language commands, and traffic control actions. Our vision builds upon existing multi-LiDAR pipelines and identifies open-source foundations for each phase, providing a path toward infrastructure that understands and anticipates traffic.

---


### 222. [Poly-EPO: Training Exploratory Reasoning Models](https://arxiv.org/abs/2604.17654)

**<font color=#1a73e8>作者：</font>** Ifdita Hasan Orney, Jubayer Ibn Hamid, Shreya S Ramanujam 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Exploration is a cornerstone of learning from experience: it enables agents to find solutions to complex problems, generalize to novel ones, and scale performance with test-time compute. In this paper, we present a framework for post-training language models (LMs) that explicitly encourages optimistic exploration and promotes a synergy between exploration and exploitation. The central idea is to train the LM to generate sets of responses that are collectively accurate under the reward function and exploratory in their reasoning strategies. We first develop a general recipe for optimizing LMs with set reinforcement learning (set RL) under arbitrary objective functions, showing how standard RL algorithms can be adapted to this setting through a modification to the advantage computation. We then propose Polychromic Exploratory Policy Optimization (Poly-EPO), which instantiates this framework with an objective that explicitly synergizes exploration and exploitation. Across a range of reasoning benchmarks, we show that Poly-EPO improves generalization, as evidenced by higher pass@$k$ coverage, preserves greater diversity in model generations, and effectively scales with test-time compute.

---


### 223. [Semantic Density Effect (SDE): Maximizing Information Per Token Improves LLM Accuracy](https://arxiv.org/abs/2604.17659)

**<font color=#1a73e8>作者：</font>** Amr Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the Semantic Density Effect (SDE): the empirical finding that prompts carrying higher semantic information per token consistently produce more accurate, focused, and less hallucinated outputs across all major LLM families. SDE is defined as the ratio of semantically loaded tokens to total prompt tokens, adjusted for redundancy and concreteness. Unlike prior prompt optimization techniques that add tokens (Chain of Thought), duplicate the prompt (Prompt Repetition), or reorder components (Instruction Placement Effect), SDE improves performance by removing or replacing low-information tokens while preserving or sharpening the semantic signal. Evaluated across five frontier models and seven benchmarks, ultra-dense prompts (SDE > 0.80) outperform diluted counterparts by an average of +8.4 percentage points with 0 additional tokens and 0 latency overhead. Combined with Instruction Placement Effect (IPE), the gain reaches +11.7 percentage points

---


### 224. [ATLAS: Constitution-Conditioned Latent Geometry and Redistribution Across Language Models and Neural Perturbation Data](https://arxiv.org/abs/2604.17663)

**<font color=#1a73e8>作者：</font>** Gareth Seneque, Lap-Hang Ho, Nafise Erfanian Saeedi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constitution-conditioned post-training can be analysed as a structured perturbation of a model's learned representational geometry. We introduce ATLAS, a geometry-first program that traces constitution-induced hidden-state structure across charts, models, and substrates. Instead of treating the relevant unit as a single behaviour, neuron, vector, or patch, ATLAS tests a local chart whose tangent structure, occupancy distribution, and behavioural coupling can be measured under system change. On Gemma, the anchored source-local chart captures 310 / 320 reviewed source rows and all 84 / 84 reviewed score-flip rows, but compact exact-patch sufficiency does not close, so the exportable unit is the broader source-defined family. Freezing that family, we re-identify a target-local realisation in an unadapted Phi model, where the fully adjudicated confirmatory contrast separates with AUC 0.984 and mean gap 5.50. In held-out ALM8 mouse frontal-cortex perturbation data, the same source-defined family receives support across 5/5 folds, with mean held-out AUC 0.72 and mean fold gap 4.50. A multiple-choice analysis provides the main boundary: nearby target-local signals can appear without source-faithful closure. The resulting correspondence is not coordinate identity, site identity, or a target-side mediation theorem. It is geometric recurrence under redistribution: written constitutions can induce recoverable latent geometry whose organisation remains detectable across model and substrate changes while its local coordinates, occupancy, and behavioural expression shift.

---


### 225. [Semantic Entanglement in Vector-Based Retrieval: A Formal Framework and Context-Conditioned Disentanglement Pipeline for Agentic RAG Systems](https://arxiv.org/abs/2604.17677)

**<font color=#1a73e8>作者：</font>** Nick Loghmani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems depend on the geometric properties of vector representations to retrieve contextually appropriate evidence. When source documents interleave multiple topics within contiguous text, standard vectorization produces embedding spaces in which semantically distinct content occupies overlapping neighborhoods. We term this condition semantic entanglement. We formalize entanglement as a model-relative measure of cross-topic overlap in embedding space and define an Entanglement Index (EI) as a quantitative proxy. We argue that higher EI constrains attainable Top-K retrieval precision under cosine similarity retrieval. To address this, we introduce the Semantic Disentanglement Pipeline (SDP), a four-stage preprocessing framework that restructures documents prior to embedding. We further propose context-conditioned preprocessing, in which document structure is shaped by patterns of operational use, and a continuous feedback mechanism that adapts document structure based on agent performance. We evaluate SDP on a real-world enterprise healthcare knowledge base comprising over 2,000 documents across approximately 25 sub-domains. Top-K retrieval precision improves from approximately 32% under fixed-token chunking to approximately 82% under SDP, while mean EI decreases from 0.71 to 0.14. We do not claim that entanglement fully explains RAG failure, but that it captures a distinct preprocessing failure mode that downstream optimization cannot reliably correct once encoded into the vector space.

---


### 226. [SafeAnchor: Preventing Cumulative Safety Erosion in Continual Domain Adaptation of Large Language Models](https://arxiv.org/abs/2604.17691)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models is remarkably shallow: it is concentrated in the first few output tokens and reversible by fine-tuning on as few as 100 adversarial examples. This fragility becomes critical in real-world deployment, where models undergo sequential adaptation across domains such as medicine, law, and code, causing safety guardrails to erode cumulatively. Yet all existing safety-preserving methods target only single-task fine-tuning, leaving the multi-domain sequential setting entirely unaddressed.
We introduce SafeAnchor, a framework that anchors safety in place throughout continual adaptation. SafeAnchor first identifies low-rank safety subspaces in LoRA parameter space via Fisher Information eigendecomposition, then constrains domain-specific gradient updates to the orthogonal complement of these subspaces, and finally monitors for residual safety drift with threshold-triggered corrective replay. Evaluated on Llama-2-7B-Chat and Mistral-7B-Instruct across a three-domain pipeline and eight benchmarks, SafeAnchor retains 93.2% of original safety alignment, outperforming all baselines by 18-42 points, while matching unconstrained fine-tuning to within 1.5 points on domain tasks.

---


### 227. [MoE-nD: Per-Layer Mixture-of-Experts Routing for Multi-Axis KV Cache Compression](https://arxiv.org/abs/2604.17695)

**<font color=#1a73e8>作者：</font>** Libo Sun, Peixiong He, Po-Wei Harn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV cache memory is the dominant bottleneck for long-context LLM inference. Existing compression methods each act on a single axis of the four-dimensional KV tensor -- token eviction (sequence), quantization (precision), low-rank projection (head dimension), or cross-layer sharing -- but apply the same recipe to every layer. We show that this homogeneity leaves accuracy on the table: different layers respond very differently to each compression operation, and the optimal per-layer mix of eviction and quantization is far from uniform. We propose MoE-nD, a mixture-of-experts framework that routes each layer to its own (eviction-ratio, K-bits, V-bits) tuple under a global memory budget. An offline-calibrated greedy solver chooses the routing that minimizes predicted quality loss; at inference time, per-layer heterogeneous eviction and quantization are applied jointly through a single attention patch. On a 4-task subset of LongBench-v1 (16k inputs, n=50 per task, adapted reasoning-model protocol; see section Experiments), MoE-nD's hetero variant matches our uncompressed 1.9~GB baseline at 14x compression (136~MB) while every other compressed baseline we tested (1d, 2d_uniform, 2d) at comparable or smaller memory stays under 8/100. The gains hold on AIME reasoning benchmarks (+6 to +27 pts over the strongest per-layer-quantization baseline across eight configurations). Two null results -- MATH-500 and LongBench's TREC -- share a principled cause (short inputs, solver picks keep=1.0 on most layers), cleanly characterizing when per-layer eviction routing has headroom to help.

---


### 228. [The Geometric Canary: Predicting Steerability and Detecting Drift via Representational Stability](https://arxiv.org/abs/2604.17698)

**<font color=#1a73e8>作者：</font>** Prashant C. Raju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable deployment of language models requires two capabilities that appear distinct but share a common geometric foundation: predicting whether a model will accept targeted behavioral control, and detecting when its internal structure degrades. We show that geometric stability, the consistency of a representation's pairwise distance structure, addresses both. Supervised Shesha variants that measure task-aligned geometric stability predict linear steerability with near-perfect accuracy ($\rho = 0.89$-$0.97$) across 35-69 embedding models and three NLP tasks, capturing unique variance beyond class separability (partial $\rho = 0.62$-$0.76$). A critical dissociation emerges: unsupervised stability fails entirely for steering on real-world tasks ($\rho \approx 0.10$), revealing that task alignment is essential for controllability prediction. However, unsupervised stability excels at drift detection, measuring nearly $2\times$ greater geometric change than CKA during post-training alignment (up to $5.23\times$ in Llama) while providing earlier warning in 73\% of models and maintaining a $6\times$ lower false alarm rate than Procrustes. Together, supervised and unsupervised stability form complementary diagnostics for the LLM deployment lifecycle: one for pre-deployment controllability assessment, the other for post-deployment monitoring.

---


### 229. [Before You Interpret the Profile: Validity Scaling for LLM Metacognitive Self-Report](https://arxiv.org/abs/2604.17707)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical personality assessment screens response validity before interpreting substantive scales. LLM evaluation does not. We apply the validity scaling framework from the PAI and MMPI-3 to metacognitive probe data from 20 frontier models across 524 items. Six validity indices are operationalised: L (maintaining confidence on errors), K (betting on errors), F (withdrawing consensus-endorsed items), Fp (withdrawing correct answers), RBS (inverted monitoring), and TRIN (fixed responding). A tiered classification system identifies four models as construct-level invalid and two as elevated. Valid-profile models produce item-sensitive confidence (mean r = .18, 14 of 16 significant). Invalid-profile models do not (mean r = -.20, d = 2.17, p = .001). Chain-of-thought training produces two opposite response distortions. Two latent dimensions account for 94.6% of index variance. Companion papers extract a portable screening protocol (Cacioli, 2026e) and validate it against selective prediction (Cacioli, 2026f). All data and code: this https URL

---


### 230. [DeInfer: Efficient Parallel Inferencing for Decomposed Large Language Models](https://arxiv.org/abs/2604.17709)

**<font color=#1a73e8>作者：</font>** You-Liang Huang, Xinhao Huang, Chengxi Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing works on large language model (LLM) decomposition mainly focus on improving performance on downstream tasks, but they ignore the poor parallel inference performance when trying to scale up the model size. To mitigate this important performance issue, this paper introduces DeInfer, a high-performance inference system dedicated to parallel inference of decomposed LLMs. It consists of multiple optimizations to maximize performance and be compatible with state-of-the-art optimization techniques. Extensive experiments are carried out to evaluate DeInfer's performance, where the results demonstrate its superiority, suggesting it can greatly facilitate the parallel inference of decomposed LLMs.

---


### 231. [Dynamic Visual-semantic Alignment for Zero-shot Learning with Ambiguous Labels](https://arxiv.org/abs/2604.17710)

**<font color=#1a73e8>作者：</font>** Jiangnan Li, Linqing Huang, Xiaowen Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot learning (ZSL) aims to recognize unseen classes without visual instances. However, existing methods usually assume clean labels, overlooking real-world label noise and ambiguity, which degrades performance. To bridge this gap, we propose the Dynamic Visual-semantic Alignment (DVSA), a robust ZSL framework for learning from ambiguous labels. DVSA uses a bidirectional visual-semantic alignment module with attention to mutually calibrate visual features and attribute prototypes, and a contrastive optimization grounded in Mutual Information (MI) at the attribute level to strengthen discriminative, semantically consistent attributes. In addition, a dynamic label disambiguation mechanism iteratively corrects noisy supervision while preserving semantic consistency, narrowing the instance-label gap, and improving generalization. Extensive experiments on standard benchmarks verify that DVSA achieves stronger performance under ambiguous supervision.

---


### 232. [Screen Before You Interpret: A Portable Validity Protocol for Benchmark-Based LLM Confidence Signals](https://arxiv.org/abs/2604.17714)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM confidence signals are used for abstention, routing, and safety-critical decisions. No standard practice exists for checking whether a confidence signal carries item-level information before building on it. We transfer the validity screening principle from clinical personality assessment (PAI, MMPI-3) as a portable protocol for benchmark-based LLM confidence data. The protocol specifies three core indices (L, Fp, RBS), a structural indicator (TRIN), and an item-sensitivity statistic, computed from a single 2x2 contingency table. A three-tier classification system (Invalid, Indeterminate, Valid) draws on four clinical traditions. Validated on 20 frontier LLMs across 524 items, four models are classified Invalid, two Indeterminate. Valid-profile models show mean r = .18 (15/16 significant). Invalid-profile models show mean r = -.20 (d = 2.48). Cross-benchmark validation on 18 models using MMLU with verbalized confidence and on external data from Yang et al. (2024) confirms the screen transfers across benchmarks and probe formats. All data and code: this https URL

---


### 233. [Concurrent Criterion Validation of a Validity Screen for LLM Confidence Signals via Selective Prediction](https://arxiv.org/abs/2604.17716)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The validity screen (Cacioli, 2026d, 2026e) classifies LLM confidence signals as Valid, Indeterminate, or Invalid. We test whether these classifications predict selective prediction performance. Twenty frontier LLMs from seven families were evaluated on 524 items across six cognitive tracks. Valid models show mean Type 2 AUROC = .624 (SD = .048). Invalid models show mean AUROC = .357 (SD = .231). Cohen's d = 2.81, p = .002. The tiers order monotonically: Invalid (.357) < Indeterminate (.554) < Valid (.624). Split-half cross-validation yields median d = 1.77, P(d > 0) = 1.0 across 1,000 splits. The three-tier classification accounts for 47% of the variance in AUROC. DeepSeek-R1 drops from 85.3% accuracy at full coverage to 11.3% at 10% coverage. The screen predicts the criterion. For selective prediction, the screen matters.

---


### 234. [Do LLMs Use Cultural Knowledge Without Being Told? A Multilingual Evaluation of Implicit Pragmatic Adaptation](https://arxiv.org/abs/2604.17718)

**<font color=#1a73e8>作者：</font>** Mehwish Nasim, Sanjeevan Selvaganapathy, Neel Ganapathi Sabhahit 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many benchmarks show that large language models can answer direct questions about culture. We study a different question: do they also change how they speak when culture is only implied by the situation? We evaluate 60 culturally grounded conversational scenarios across five languages in three conditions: a neutral baseline (Prompt A), an explicit cultural instruction (Prompt B), and implicit situational cueing (Prompt C). We score responses on 12 pragmatic features covering deference to authority, individual-versus-group framing, and uncertainty management. We define Pragmatic Context Sensitivity (PCS) as the fraction of the Prompt A->B shift that reappears under Prompt A->C. Across four deployed LLMs and five languages (English, German, Hindi, Nepali, Urdu), the primary stable-only PCS mean is 0.196 (SD = 0.113), indicating that the models recover only about one-fifth of the pragmatic shift they can produce when instructed explicitly. Transfer is strongest for authority-related cues (0.299) and weakest for individual-versus-group framing (0.120). Uncertainty-related behaviour is mixed: hedging density exhibits negative explicit gaps in all five languages, suggesting that alignment training actively suppresses the target behaviour. Because Hindi and Urdu share core grammar yet index distinct cultural communities, we use them as a natural control; a paired analysis finds no reliable baseline difference (t = 0.96, p = 0.339, dz = 0.06), suggesting that models respond primarily to linguistic structure rather than to the cultural associations a language carries. We argue that multilingual cultural pragmatics is an explicit-versus-implicit deployment problem, not only a factual knowledge problem.

---


### 235. [RePrompT: Recurrent Prompt Tuning for Integrating Structured EHR Encoders with Large Language Models](https://arxiv.org/abs/2604.17725)

**<font color=#1a73e8>作者：</font>** Arya Hadizadeh Moghaddam, Drew Ross, Mohsen Nayebi Kerdabadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong promise for mining Electronic Health Records (EHRs) by reasoning over longitudinal clinical information to capture context-rich patient trajectories. However, leveraging LLMs for structured EHRs (e.g., standardized diagnosis and medication codes) presents two key challenges. First, translating time-stamped EHR sequences into plain text can obscure both temporal structure and code identities, weakening the ability to capture code co-occurrence and longitudinal regularities. Second, unlike cohort-trained predictive models that learn a shared, task-aligned representation space across patients, LLMs are often applied in a case-isolated inference setting where each patient is processed independently without leveraging population-level patterns. To address these challenges, we introduce RePrompT, a time-aware LLM framework that integrates structured EHR encoders through prompt tuning, without modifying underlying architectures. Specifically, RePrompT recurrently incorporates latent states from prior visits to preserve longitudinal information, and injects population-level information through trainable prompt tokens derived from a cohort-trained, task-aligned EHR encoder. Experiments on MIMIC-III and MIMIC-IV demonstrate that RePrompT consistently outperforms both EHR-based and LLM-based baselines across multiple clinical prediction tasks.

---


### 236. [MHSafeEval: Role-Aware Interaction-Level Evaluation of Mental Health Safety in Large Language Models](https://arxiv.org/abs/2604.17730)

**<font color=#1a73e8>作者：</font>** Suhyun Lee, Palakorn Achananuparp, Neemesh Yadav 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly explored as scalable tools for mental health counseling, yet evaluating their safety remains challenging due to the interactional and context-dependent nature of clinical harm. Existing evaluation frameworks predominantly assess isolated responses using coarse-grained taxonomies or static datasets, limiting their ability to diagnose how harms emerge and accumulate over multi-turn counseling interactions. In this work, we introduce R-MHSafe, a role-aware mental health safety taxonomy that characterizes clinically significant harm in terms of the interactional roles an AI counselor adopts, including perpetrator, instigator, facilitator, or enabler, combined with clinically grounded harm categories. Then, we propose MHSafeEval, a closed-loop, agent-based evaluation framework that formulates safety assessment as trajectory-level discovery of harm through adversarial multi-turn interactions, guided by role-aware modeling. Using R-MHSafe and MHSafeEval, we conduct a large-scale evaluation across state-of-the-art LLMs. Our results reveal substantial role-dependent and cumulative safety failures that are systematically missed by existing static benchmarks, and show that our framework significantly improves failure-mode coverage and diagnostic granularity.

---


### 237. [Mira-Embeddings-V1: Domain-Adapted Semantic Reranking for Recruitment via LLM-Synthesized Data](https://arxiv.org/abs/2604.17738)

**<font color=#1a73e8>作者：</font>** Zhaohua Liang, Zhilin Wang, Renjie Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Candidate sourcing for recruiters is best viewed as a two-stage retrieval and reranking pipeline with recall as the primary objective under a limited review budget. An upstream production retriever first returns a candidate shortlist for each job description (JD), and our goal is to rerank that shortlist so that qualified candidates appear as high as possible. We present mira-embeddings-v1, a semantic reranking system for the recruitment domain that reshapes the embedding space with LLM-synthesized training data and corrects boundary confusions with a lightweight reranking head. Starting from real JDs, we build a five-stage prompt pipeline to generate diverse positive and hard negative samples that sculpt the semantic space from multiple angles. We then apply a two-round LoRA adaptation: JD--JD contrastive training followed by JD--CV triplet alignment on a heterogeneous text dataset. Importantly, these gains require no large-scale manually labeled industrial training pairs: a modest set of real JDs is expanded into supervision through LLM synthesis. Finally, a BoundaryHead MLP reranks the Top-K results to distinguish between roles that share the same title but differ in scope. On a local pool of 300 real JDs with candidates from an upstream production retriever, mira-embeddings-v1 improves Recall@50 from 68.89% (baseline) to 77.55% while lifting Precision@10 from 35.77% to 39.62%. On a supportive global pool over 44,138 candidates judged by a Qwen3-32B rubric, it achieves Recall@200 of 0.7047 versus 0.5969 for the baseline. These results show that LLM-synthesized supervision with boundary-aware reranking yields robust gains without a heavy cross-encoder.

---


### 238. [Tool Learning Needs Nothing More Than a Free 8B Language Model](https://arxiv.org/abs/2604.17739)

**<font color=#1a73e8>作者：</font>** Chenming Tang, Hsiu-Yuan Huang, Weijie Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a prevalent paradigm for training tool calling agents, which typically requires online interactive environments. Existing approaches either rely on training data with ground truth annotations or require advanced commercial language models (LMs) to synthesize environments that keep fixed once created. In this work, we propose TRUSTEE, a data-free method training tool calling agents with dynamic environments fully simulated by free open-source LMs that can be as small as 8B, including task generation, user simulation, tool simulation and trajectory evaluation, paired with an adaptive curriculum learning mechanism that controls various aspects of the task difficulty dynamically during training. Our empirical results show that TRUSTEE brings consistent improvements across various domains and outperforms all the baselines which require extra external resources for training. These confirm that, with a sufficiently sophisticated design, even simulated environments with a local 8B LM as the backbone could set a strong baseline for tool learning, without expensive annotated data, realistic human interactions, executable tools or costly verifiable environments from human experts or commercial LMs. We hope our proposed paradigm could inspire future research on environment scaling with limited resources.

---


### 239. [Efficient Federated RLHF via Zeroth-Order Policy Optimization](https://arxiv.org/abs/2604.17747)

**<font color=#1a73e8>作者：</font>** Deyi Wang, Qining Zhang, Lei Ying  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper considers reinforcement learning from human feedback in a federated learning setting with resource-constrained agents, such as edge devices. We propose an efficient federated RLHF algorithm, named Partitioned, Sign-based Stochastic Zeroth-order Policy Optimization (Par-S$^2$ZPO). The algorithm is built on zeroth-order optimization with binary perturbation, resulting in low communication, computation, and memory complexity by design. Our theoretical analysis establishes an upper bound on the convergence rate of Par-S$^2$ZPO, revealing that it is as efficient as its centralized counterpart in terms of sample complexity but converges faster in terms of policy update iterations. Our experimental results show that it outperforms a FedAvg-based RLHF on four MuJoCo RL tasks.

---


### 240. [HiP-LoRA: Budgeted Spectral Plasticity for Robust Low-Rank Adaptation](https://arxiv.org/abs/2604.17751)

**<font color=#1a73e8>作者：</font>** Lixian Chen, Jianhong Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting foundation models under resource budgets relies heavily on Parameter-Efficient Fine-Tuning (PEFT), with LoRA being a standard modular solution. However, LoRA suffers from spectral interference. Low-rank updates often concentrate energy on the leading singular directions of pretrained weights, perturbing general capabilities and causing catastrophic forgetting and fragile multi-adapter merging. To resolve this, we propose HiP-LoRA, a spectrum-aware adaptation framework. Utilizing the cached singular value decomposition (SVD) of pretrained layers, HiP-LoRA decomposes updates into two channels: a principal channel within the dominant singular subspace, and a residual low-rank channel in the orthogonal complement. A singular-value-weighted stability budget on the principal channel continuously balances pretrained behavior preservation with task-specific plasticity. Experiments on Llama-3.1-8B demonstrate that under matched budgets, HiP-LoRA drastically reduces pretraining degradation and multi-adapter MergeFail, robustly outperforming baselines in interference-sensitive tasks like continual tuning and knowledge editing.

---


### 241. [Contrastive Attribution in the Wild: An Interpretability Analysis of LLM Failures on Realistic Benchmarks](https://arxiv.org/abs/2604.17761)

**<font color=#1a73e8>作者：</font>** Rongyuan Tan, Jue Zhang, Zhuozhao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpretability tools are increasingly used to analyze failures of Large Language Models (LLMs), yet prior work largely focuses on short prompts or toy settings, leaving their behavior on commonly used benchmarks underexplored. To address this gap, we study contrastive, LRP-based attribution as a practical tool for analyzing LLM failures in realistic settings. We formulate failure analysis as \textit{contrastive attribution}, attributing the logit difference between an incorrect output token and a correct alternative to input tokens and internal model states, and introduce an efficient extension that enables construction of cross-layer attribution graphs for long-context inputs. Using this framework, we conduct a systematic empirical study across benchmarks, comparing attribution patterns across datasets, model sizes, and training checkpoints. Our results show that this token-level contrastive attribution can yield informative signals in some failure cases, but is not universally applicable, highlighting both its utility and its limitations for realistic LLM failure analysis. Our code is available at: this https URL.

---


### 242. [When Vision-Language Models Judge Without Seeing: Exposing Informativeness Bias](https://arxiv.org/abs/2604.17768)

**<font color=#1a73e8>作者：</font>** Xiaohan Zou, Roshan Sridhar, Mohammadtaher Safarzadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The reliability of VLM-as-a-Judge is critical for the automatic evaluation of vision-language models (VLMs). Despite recent progress, our analysis reveals that VLM-as-a-Judge often pays limited attention to the image when making decisions. Instead, they often blindly favor the more informative answer, even when they can recognize it conflicts with the image content. We call this problem informativeness bias, which significantly undermines judge reliability. To address it, we propose BIRCH (Balanced Informativeness and CoRrectness with a Truthful AnCHor), a judging paradigm that first corrects inconsistencies with the image content in candidate answers, and then compares the answers against this corrected version. This shifts the judge's focus from informativeness to image-grounded correctness. Experiments on multiple models and benchmarks show that BIRCH reduces informativeness bias by up to 17%, resulting in performance gains of up to 9.8%. Our work reveals an overlooked but fundamental flaw in current VLM-as-a-Judge systems and highlights the need for more principled designs.

---


### 243. [LLM-AUG: Robust Wireless Data Augmentation with In-Context Learning in Large Language Models](https://arxiv.org/abs/2604.17770)

**<font color=#1a73e8>作者：</font>** Pranshav Gajjar, Manan Tiwari, Sayanta Seth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data scarcity remains a fundamental bottleneck in applying deep learning to wireless communication problems, particularly in scenarios where collecting labeled Radio Frequency (RF) data is expensive, time-consuming, or operationally constrained. This paper proposes LLM-AUG, a data augmentation framework that leverages in-context learning in large language models (LLMs) to generate synthetic training samples directly in a learned embedding space. Unlike conventional generative approaches that require training task-specific models, LLM-AUG performs data generation through structured prompting, enabling rapid adaptation in low-shot regimes. We evaluate LLM-AUG on two representative tasks: modulation classification and interference classification using the RadioML 2016.10A dataset, and the Interference Classification (IC) dataset respectively. Results show that LLM-AUG consistently outperforms traditional augmentation and deep generative baselines across low-shot settings and reaches near oracle performance using only 15% labeled data. LLM-AUG further demonstrates improved robustness under distribution shifts, yielding a 29.4% relative gain over diffusion-based augmentation at a lower SNR value. On the RadioML and IC datasets, LLM-AUG yields a relative gain of 67.6% and 35.7% over the diffusion-based baseline. The t-SNE visualizations further validate that synthetic samples generated by better preserve class structure in the embedding space, leading to more consistent and informative augmentations. These results demonstrate that LLMs can serve as effective and practical data augmenters for wireless machine learning, enabling robust and data-efficient learning in evolving wireless environments.

---


### 244. [Prompt Optimization Enables Stable Algorithmic Collusion in LLM Agents](https://arxiv.org/abs/2604.17774)

**<font color=#1a73e8>作者：</font>** Yingtao Tian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents in markets present algorithmic collusion risks. While prior work shows LLM agents reach supracompetitive prices through tacit coordination, existing research focuses on hand-crafted prompts. The emerging paradigm of prompt optimization necessitates new methodologies for understanding autonomous agent behavior. We investigate whether prompt optimization leads to emergent collusive behaviors in market simulations. We propose a meta-learning loop where LLM agents participate in duopoly markets and an LLM meta-optimizer iteratively refines shared strategic guidance. Our experiments reveal that meta-prompt optimization enables agents to discover stable tacit collusion strategies with substantially improved coordination quality compared to baseline agents. These behaviors generalize to held-out test markets, indicating discovery of general coordination principles. Analysis of evolved prompts reveals systematic coordination mechanisms through stable shared strategies. Our findings call for further investigation into AI safety implications in autonomous multi-agent systems.

---


### 245. [TeleEmbedBench: A Multi-Corpus Embedding Benchmark for RAG in Telecommunications](https://arxiv.org/abs/2604.17778)

**<font color=#1a73e8>作者：</font>** Pranshav Gajjar, Vijay K Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in the telecommunications domain for critical tasks, relying heavily on Retrieval-Augmented Generation (RAG) to adapt general-purpose models to continuously evolving standards. However, a significant gap exists in evaluating the embedding models that power these RAG pipelines, as general-purpose benchmarks fail to capture the dense, acronym-heavy, and highly cross-referential nature of telecommunications corpora. To address this, we introduce TeleEmbedBench, the first large-scale, multi-corpus embedding benchmark designed specifically for telecommunications. The benchmark spans three heterogeneous corpora: O-RAN Alliance specifications, 3GPP release documents, and the srsRAN open-source codebase, comprising 9,000 question-chunk pairs across three standard chunk sizes (512, 1024, and 2048 tokens). To construct this dataset at scale without manual annotation bottlenecks, we employ a novel automated pipeline where one LLM generates specific queries from text chunks and a secondary LLM validates them across strict criteria. We comprehensively evaluate eight embedding models, spanning standard sentence-transformers and LLM-based embedders. Our results demonstrate that LLM-based embedders, such as Qwen3 and EmbeddingGemma, consistently and significantly outperform traditional sentence-transformers in both retrieval accuracy and robustness against cross-domain interference. Additionally, we introduce TeleEmbedBench-Clean to evaluate model robustness against noisy, incomplete user queries. Finally, our analysis reveals that while domain-specific task instructions improve embedder performance for raw source code, they paradoxically degrade retrieval performance for natural language telecommunications specifications.

---


### 246. [Subject-Aware Multi-Granularity Alignment for Zero-Shot EEG-to-Image Retrieval](https://arxiv.org/abs/2604.17782)

**<font color=#1a73e8>作者：</font>** Lin Jiang, Qingshan She, Jiale Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot EEG-to-image retrieval aims to decode perceived visual content from electroencephalography (EEG) by aligning neural responses with pretrained visual representations, providing a promising route toward scalable visual neural decoding and practical brain-computer interfaces. However, robust EEG-to-image retrieval remains challenging, because prior methods usually rely on either a single fixed visual target or a subject-invariant target construction scheme. Such designs overlook two important properties of visually evoked EEG signals: they preserve information across multiple representational scales, and the visual granularity best matched to EEG may vary across subjects. To address these issues, subject-aware multi-granularity alignment (SAMGA) framework is proposed for zero-shot EEG-to-image retrieval. SAMGA first constructs a subject-aware visual supervision target by adaptively aggregating multiple intermediate representations from a pretrained vision encoder, allowing the model to absorb subject-dependent granularity deviations during training while preserving subject-agnostic inference. Building on this adaptive target construction, a coarse-to-fine cross-modal alignment strategy is further designed with a shared encoder wherein the coarse stage stabilizes the shared semantic geometry and reduces subject-induced distribution shift, and the fine stage further improves instance-level retrieval discrimination. Extensive experiments on the THINGS-EEG benchmark demonstrate that the proposed method achieves 91.3% Top-1 and 98.8% Top-5 accuracy in the intra-subject setting, and 34.4% Top-1 and 64.8% Top-5 accuracy in the inter-subject setting, outperforming recent state-of-the-art methods.

---


### 247. [Bridging the Reasoning Gap in Vietnamese with Small Language Models via Test-Time Scaling](https://arxiv.org/abs/2604.17794)

**<font color=#1a73e8>作者：</font>** Bui The Trung, Do Minh Duc, Nguyen Van Vinh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The democratization of ubiquitous AI hinges on deploying sophisticated reasoning capabilities on resource-constrained devices. However, Small Language Models (SLMs) often face a "reasoning gap", particularly in non-English languages like Vietnamese, where they struggle to maintain coherent chains of thought. This paper investigates Test-Time Scaling strategies for the Qwen3-1.7B architecture within the context of Vietnamese Elementary Mathematics. We introduce Vi-S1K, a high-fidelity reasoning dataset localized via a Gemini 2.5 Flash-Lite powered pipeline, and Vi-Elementary-Bench, a dual-resource benchmark for rigorous evaluation. Using an LLM-as-a-Judge protocol, we reveal that the base model possesses robust latent knowledge (Accuracy: 4.05/5.00) but suffers from a severe "formatting gap" in communication. Supervised Fine-Tuning (SFT) acts as a critical "reasoning unlocker", yielding a 77% improvement in Explanation Quality and bridging the gap between raw calculation and pedagogical coherence. Furthermore, our analysis of prompting strategies uncovers a significant trade-off: structured frameworks like ReAct impose a "cognitive tax" on the 1.7B parameter capacity, degrading performance relative to pure Chain-of-Thought (CoT) combined with Self-Consistency. These findings establish a deployment hierarchy for SLMs, demonstrating that SFT combined with simplified test-time scaling is superior to complex agentic workflows for edge-based reasoning.

---


### 248. [Weakly-Supervised Referring Video Object Segmentation through Text Supervision](https://arxiv.org/abs/2604.17797)

**<font color=#1a73e8>作者：</font>** Miaojing Shi, Jun Huang, Zijie Yue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring video object segmentation (RVOS) aims to segment the target instance in a video, referred by a text expression. Conventional approaches are mostly supervised learning, requiring expensive pixel-level mask annotations. To tackle it, weakly-supervised RVOS has recently been proposed to replace mask annotations with bounding boxes or points, which are however still costly and labor-intensive. In this paper, we design a novel weakly-supervised RVOS method, namely WSRVOS, to train the model with only text expressions. Given an input video and the referring expression, we first design a contrastive referring expression augmentation scheme that leverages the captioning capabilities of a multimodal large language model to generate both positive and negative expressions. We extract visual and linguistic features from the input video and generated expressions, then perform bi-directional vision-language feature selection and interaction to enable fine-grained multimodal alignment. Next, we propose an instance-aware expression classification scheme to optimize the model in distinguishing positive from negative expressions. Also, we introduce a positive-prediction fusion strategy to generate high-quality pseudo-masks, which serve as additional supervision to the model. Last, we design a temporal segment ranking constraint such that the overlaps between mask predictions of temporally neighboring frames are required to conform to specific orders. Extensive experiments on four publicly available RVOS datasets, including A2D Sentences, J-HMDB Sentences, Ref-YouTube-VOS, and Ref-DAVIS17, demonstrate the superiority of our method. Code is available at \href{this https URL}{this https URL}.

---


### 249. [Adversarial Arena: Crowdsourcing Data Generation through Interactive Competition](https://arxiv.org/abs/2604.17803)

**<font color=#1a73e8>作者：</font>** Prasoon Goyal, Sattvik Sahai, Michael Johnston 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training Large Language Models requires diverse, high-quality data which is rare and costly to obtain, especially in low resource domains and for multi-turn conversations. Common solutions are crowdsourcing or synthetic generation, but both often yield low-quality or low-diversity data. We introduce Adversarial Arena for building high quality conversational datasets by framing data generation as an adversarial task: attackers create prompts, and defenders generate responses. This interactive competition between multiple teams naturally produces diverse and complex data. We validated this approach by conducting a competition with 10 academic teams from top US and European universities, each building attacker or defender bots. The competition, focused on safety alignment of LLMs in cybersecurity, generated 19,683 multi-turn conversations. Fine-tuning an open-source model on this dataset produced an 18.47% improvement in secure code generation on CyberSecEval-Instruct and 29.42% improvement on CyberSecEval-MITRE.

---


### 250. [Re$^2$MoGen: Open-Vocabulary Motion Generation via LLM Reasoning and Physics-Aware Refinement](https://arxiv.org/abs/2604.17807)

**<font color=#1a73e8>作者：</font>** Jiakun Zheng, Ting Xiao, Shiqin Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion (T2M) generation aims to control the behavior of a target character via textual descriptions. Leveraging text-motion paired datasets, existing T2M models have achieved impressive performance in generating high-quality motions within the distribution of their training data. However, their performance deteriorates notably when the motion descriptions differ significantly from the training texts. To address this issue, we propose Re$^2$MoGen, a Reasoning and Refinement open-vocabulary Motion Generation framework that leverages enhanced Large Language Model (LLM) reasoning to generate an initial motion planning and then refine its physical plausibility via reinforcement learning (RL) post-training. Specifically, Re$^2$MoGen consists of three stages: We first employ Monte Carlo tree search to enhance the LLM's reasoning ability in generating reasonable keyframes of the motion based on text prompts, specifying only the root and several key joints' positions to ease the reasoning process. Then, we apply a human pose model as a prior to optimize the full-body poses based on the planned keyframes and use the resulting incomplete motion to supervise fine-tuning a pre-trained motion generator via a dynamic temporal matching objective, enabling spatiotemporal completion. Finally, we use post-training with physics-aware reward to refine motion quality to eliminate physical implausibility in LLM-planned motions. Extensive experiments demonstrate that our framework can generate semantically consistent and physically plausible motions and achieve state-of-the-art performance in open-vocabulary motion generation.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

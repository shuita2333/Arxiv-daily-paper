# 🧠 大模型相关研究 | 2026年07月30日

> 本类共 **131** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-131](./part-03.md)

---

### 51. [Medical world models in healthcare: foundations, applications, and challenges for trustworthy clinical translation](https://arxiv.org/abs/2607.25242)

**<font color=#1a73e8>作者：</font>** Zhaoyan Chen, Zhongxiu Cong, Zhuanfeng Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical world models offer a framework for extending medical artificial intelligence beyond static prediction by representing evolving patient states and modelling how they change over time and in response to clinical interventions. This Review defines the conceptual boundaries, technical foundations, application domains, and evidence requirements of the field through a structured narrative synthesis with reproducible evidence this http URL screened 1,455 unique records and assembled a corpus of 98 sources, including 14 studies that met a strict empirical definition of a medical world model. The field is organised around four capabilities: patient state representation, temporal dynamics modelling, intervention-conditioned simulation, and clinician-supervised planning. Evidence spans medical imaging, longitudinal electronic health records, treatment response modelling, physiological and multimodal state modelling, ultrasound and surgical interaction, and population and health-system simulation; clinical digital twins are treated as a cross-cutting integration this http URL studies provide early evidence of technical feasibility for trajectory forecasting and comparison of candidate interventions, but most remain retrospective, task-specific, or preclinical. The evidence base is further limited by incomplete longitudinal intervention data, inconsistent action semantics, limited causal identifiability, long-horizon error accumulation, inadequate uncertainty estimation, and limited external validation. Clinical translation will therefore depend on precise intervention representations, robust causal and mechanistic grounding, calibrated trajectory-level uncertainty, safety-constrained planning, and prospective multicentre validation against clinically meaningful endpoints.

---


### 52. [CADENCE: A Cardiac Atom Dictionary for Interpretable Neural Concept Extraction from ECG Foundation Models](https://arxiv.org/abs/2607.25244)

**<font color=#1a73e8>作者：</font>** Yixuan Duan, Arjun Naik, Sadeer Al-Kindi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models for 12-lead electrocardiograms (ECGs) transfer well across clinical tasks, but the physiological knowledge encoded in their representations remains opaque. We present CADENCE, a framework that decomposes an ECG foundation model into a human-interpretable, queryable dictionary of physiological concepts. Using a BatchTopK sparse autoencoder, CADENCE factorizes Layer-6 embeddings from more than nine million ECG tokens into 8,192 sparse cardiac atoms. These atoms align better than individual dense embedding dimensions with clinical phenotypes and waveform morphology, recovering arrhythmias, conduction abnormalities, infarction and repolarization patterns, chamber and axis findings, and lead- and beat-phase-specific waveform primitives. At Layer 6, the best atoms achieve mean AUROCs of 0.88 for clinical phenotypes and 0.90 for morphology, versus 0.78 and 0.83 for the best dense dimensions. Sparse atom probes match or outperform dense probes for phenotype, morphology, and age prediction while attributing each prediction to a small set of interpretable atoms; phenotype AUROC improves from 0.93 to 0.95. Atom-space geometry recovers physiologically coherent relationships, and targeted atom ablation selectively changes frozen downstream outputs. An automated LLM pipeline generates and quantitatively validates atom descriptions by predicting held-out activations. On independent external ECG datasets, CADENCE recovers overlapping concepts and maintains consistent phenotype-prediction performance. CADENCE provides a scalable framework for discovering and auditing the physiological knowledge encoded by ECG foundation models.

---


### 53. [The User Asks, Platforms Compete: How Agentic Recommendation Markets Take Shape](https://arxiv.org/abs/2607.25253)

**<font color=#1a73e8>作者：</font>** Deyao Hong, Kehan Zheng, Qian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online recommendation has traditionally taken place after a user enters a platform, which determines the candidate pool and the ranking shown to the user. LLM-based user agents enable a different recommendation process: a user specifies a need before choosing a platform, leaving platforms to compete for the user's attention, which we refer to as an agentic recommendation market. In our controlled LLM-based experiments across three product domains, we find this new setting of recommendation creates a tension between access and attention. Compared with traditional platform-centric recommendation, user-centric recommendation greatly expands the opportunity for relevant items to enter comparison; yet broader participation does not translate directly into effective exposure. Competition directly triggers platforms' strategic play: selectively positive explanations occupy 73--78% of first-ranked positions. When the user agent relates platforms' actions to subsequent user feedback, this share falls to 36--41%, while the chance of a user purchasing the relevant item increases. A user agent is therefore more than a ranker over a larger pool of candidates: its querying, ranking, and feedback mechanism governing who can compete, how scarce attention is allocated, and how earlier outcomes shape the evaluation of platforms directly affect user utility. Designing agentic recommendation therefore requires treating access, attention, and accountability as a joint mechanism design problem.

---


### 54. [FORGE: Frame Orthogonality in Relevance Geometry for Long-Form Video Understanding](https://arxiv.org/abs/2607.25266)

**<font color=#1a73e8>作者：</font>** Ghazal Kaviani, Ghassan AlRegib  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have enabled long-form video understanding at a scale that was not previously possible. However, the density of relevant content decreases sharply as video sequence length increases, and exposing the model to more irrelevant content measurably reduces its accuracy. In this paper, we address the problem of maximizing query-relevant information in a frame subset selected at inference time, without training. FORGE (Frame Orthogonality in Relevance Geometry) is a model-agnostic method that induces a query-conditioned geometry on a pretrained multimodal embedding space, unifying relevance and diversity into a single objective. In this space, frames that cover independent query-relevant directions are far apart, and selecting the subset of maximum information captures diverse query-relevant content within the budget. Experiments on Video-MME and LongVideoBench at budgets of 16, 32, and 64 frames show that FORGE improves the unified keyframe selection score by 11.0-15.3 points over the strongest training-free baseline and up to doubles keyframe recall (0.415 vs. 0.204 at K=64 on Video-MME). The gains extend to question answering, where accuracy improves in every evaluated setting across eight open-source MLLMs spanning 4B to 32B parameters, by up to 8.7 points over uniform sampling and 5.2 points over the strongest baseline. Our findings suggest that aligning the embedding space with the query's high-dimensional structure is a promising direction for inference-time video understanding.

---


### 55. [Many-body Tipping Dynamics of ChatGPT-like AIs](https://arxiv.org/abs/2607.25279)

**<font color=#1a73e8>作者：</font>** Frank Yingjie Huo, Neil F. Johnson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Why do ChatGPT-like AIs, despite major architectural and training differences, unexpectedly tip to undesirable content (e.g. harmful, misleading, repetitive) even under deterministic greedy decoding? We show that a broad class of such tippings is caused by the many-body interactions between tokens (spins) as they cross the finite-layer system. Tipping emerges as a dynamical first passage process between competing output basins. Attention disorder controls the transport toward, away from, or along the basins' boundary. A few-basin reduction yields a closed finite-layer threshold, whose coarse-grained predictions show good agreement across ChatGPT-like families. These results suggest that a broad class of AI failures represents 'foreseeable engineering risk' rather than inherently unpredictable behavior, with important implications for legal and societal assessments of AI harm.

---


### 56. [Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe](https://arxiv.org/abs/2607.25292)

**<font color=#1a73e8>作者：</font>** Chaemin Jang, Dongman Lee, Jihee Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Silicon sampling uses language models as proxies for human survey respondents, treating each model call as an independent draw from the persona's response distribution. We show this draw does not exist: instruction-tuned models do not sample from distributions, they collapse to a single output. The same persona on the same question returns the same answer on more than half of items in a public-opinion benchmark. The collapse is sharp: the model's internal probabilities concentrate on a single option, and the failure is substantially amplified by instruction tuning: across three model families with materially different post-training pipelines, every instruction-tuned model fails on every task we test, while base models fail far less often. Strikingly, the same model that cannot sample from a distribution can describe it accurately in a single call. We call this gap the KNOWS/DOES split, and trace it to a degenerate sampling primitive visible in the logits and induced by alignment training. Exploiting this split, asking the model to describe the response distribution in one call more than halves the error against human survey data compared to persona aggregation. For applications that require per-persona outputs, we propose Prompt-Perturbed Argyle (PPA), which reduces the same error by 21% at no added cost.

---


### 57. [CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition](https://arxiv.org/abs/2607.25294)

**<font color=#1a73e8>作者：</font>** Lai Wei, Chengqi Li, Jiapeng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world tasks often require models to learn from task-specific context rather than relying only on pre-trained knowledge. While recent work has highlighted this capability as context learning, existing evaluations mainly focus on textual contexts. In many practical settings, however, the context to be learned from is multimodal: scientific findings are conveyed through figures and tables, financial indicators are scattered across converted reports, and spatial decisions depend on maps, scenes, or web pages. We introduce CLBench-V, a benchmark for multimodal context learning that addresses the difficulty of localizing where context use breaks down by organizing tasks around three dimensions: context grounding, new information application, and new knowledge learning. CLBench-V combines converted public benchmarks with newly constructed datasets spanning domains such as science, finance, long-document understanding, spatial reasoning, and web-based visual question answering. To reduce the cost of constructing domain-specific context-learning tasks, we further use automated construction and filtering procedures for our newly built datasets. Across 3,443 instances and six recent multimodal models, the best overall score is only 0.2847, indicating that multimodal context learning remains far from saturated. Moreover, InternVL3.5-30B-A3B performs best on context grounding and new knowledge learning, while Qwen3.5-Plus performs best on new information application. We further analyze judge reliability, context length, image count, and representative failure cases. Code is available at this https URL.

---


### 58. [Retraction-Free Optimization over the Stiefel Manifold for the LoRA Fine-Tuning](https://arxiv.org/abs/2607.25299)

**<font color=#1a73e8>作者：</font>** Yuan Zhang, Jiang Hu, Zhijian Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization over the Stiefel manifold plays a significant role in various machine learning tasks. Existing methods either use the retraction operators, requiring costly orthonormalization for large-scale matrices, or employ landing methods that rely on careful step size selection and penalty parameter tuning. To address these challenges, we propose a retraction-free and penalty parameter-free algorithm that directly lands on the manifold. By leveraging the strongly-convex-like property of the quadratic penalty function and the proximal smoothness of the Stiefel manifold, we establish global convergence guarantees with the best-known iteration complexities under both constant and diminishing step sizes. Then, we reformulate the low-rank adaptation (LoRA) fine-tuning problem for large language models as a manifold optimization problem, introducing Manifold-LoRA for geometry-accelerated adaptation. This approach employs the proposed landing technique and a carefully designed step size strategy to accelerate the training process. Numerical experiments on benchmark datasets demonstrate the efficiency and strong downstream performance of the proposed method.

---


### 59. [CAST: Game Solvers as Turn-Level Teachers for LLM Agents](https://arxiv.org/abs/2607.25308)

**<font color=#1a73e8>作者：</font>** Yu Wang, Yi-Kai Zhang, Wentao Shi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) to act in long-horizon games is a promising step toward generalist decision-making, yet reinforcement learning with verifiable rewards (RLVR) relies on sparse final rewards that reveal little about which decisions determine success. Denser process signals could supply this missing turn-level credit, but existing sources are hard to keep both cheap and accurate. We observe that changes in a game solver's state value reveal whether an action advances the state toward success. Building on this insight, we propose CAST (Credit Assignment from Solver Teachers), which converts these value changes into solver advantages and injects them into RLVR as turn-level signals. We further show that, under a soft-optimal solver assumption, maximizing the solver advantage is equivalent to on-policy distillation from the solver, requiring only scalar values rather than teacher logits. Across Sokoban, Minesweeper, and Rush Hour, CAST outperforms all trained baselines on every game under both in-domain and unseen-difficulty evaluation and achieves the highest average zero-shot performance on ALFWorld and WebShop. Our code is available at this https URL.

---


### 60. [Beyond Background Bias: Saliency-Driven Prototype Alignment for Dataset Distillation](https://arxiv.org/abs/2607.25318)

**<font color=#1a73e8>作者：</font>** Yawen Zou, Wenqi Cai, Guang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation aims to synthesize compact datasets that can approximate the performance of full-data training while significantly reducing computational and storage costs. However, diffusion-based distillation methods often struggle to preserve structural coherence and generalization, especially in visually complex domains. This issue often stems from latent prototypes that are weakly aligned with class-discriminative regions and contaminated by irrelevant background, thereby degrading generation quality and generalization. To address this limitation, we propose a saliency-driven distillation framework that constructs class-discriminative latent prototypes to enhance representativeness and generalization. The framework proceeds in two stages: (1) ensemble Grad-CAM saliency is used to construct prototypes emphasizing high-confidence regions, and (2) hard prototype refinement is then applied to construct challenging yet class-consistent prototypes, thereby enhancing discriminability and diversity. Importantly, the diffusion backbones (e.g., LDM and DiT) remain frozen; only lightweight classifiers used for saliency extraction are trained. Extensive experiments across multiple benchmarks demonstrate consistent performance improvements over strong baselines. Code will be released.

---


### 61. [From Cellular Responses to Pharmacological Domains: Multimodal Zero-Shot Drug Representation Learning](https://arxiv.org/abs/2607.25322)

**<font color=#1a73e8>作者：</font>** Jintao Huang, Lu Leng, Ziyuan Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal drug discovery enables drug representation learning beyond chemical structure by incorporating cellular responses such as gene expression and cell morphology. However, direct fusion and instance-level contrastive alignment may mix mechanism-related signals with modality-specific noise and incorrectly separate structurally dissimilar but biologically related compounds. This limitation can obscure transferable mechanism patterns required for predicting the properties of unseen compounds. We introduce PMRD, a pharmacological response domain-guided framework for multimodal zero-shot drug property prediction. PMRD separates mechanism-consistent factors from modality-specific information and constructs a consensus response domain across three modalities. Mechanism candidate augmentation identifies locally stable factors, while retrieval-geometry attribution dynamically reweights the alignment and augmentation objectives according to whether their updates preserve inter-drug this http URL feedback suppresses training signals that conflict with mechanism-discriminative retrieval. PMRD further combines complementary representations through reliability-aware multiview retrieval. Experiments on public datasets show improved zero-shot property prediction and more biologically coherent drug neighborhoods. Hard-negative analysis further indicates fewer conflicts between structurally dissimilar but response-related compounds. These results support PMRD as an effective framework for mechanism-aware multimodal drug representation learning.\footnote{The code will be released upon publication.}

---


### 62. [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/abs/2607.25337)

**<font color=#1a73e8>作者：</font>** Jiaxin Bai, Jiaxuan Xiong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting in representation space rather than reconstructing pixels, making them a natural backbone for latent model predictive control from offline demonstration logs. JEPA-style training optimizes short-horizon latent prediction, whereas planning requires a multi-step ranking of imagined futures by goal progress. Prior JEPA planners often inherit that ranking from embedding geometry, typically latent Euclidean distance, which arises as a byproduct of representation learning rather than as a progress cost mined from the logs. We propose temporal-distance JEPA (TD-JEPA), which retains the LeWM encoder--predictor backbone and mines a directed temporal cost from reward-free trajectories: same-trajectory step order supplies positive targets, cross-trajectory pairs act as heuristic negatives, and a rollout-consistency term matches the planner horizon. The mined supervision serves two roles: as the deployed planning cost when progress is topological, and as a representation signal that improves Euclidean planning when contact geometry dominates. Under locked evaluation, deploying the mined cost raises Two-Room success to 100.0% versus LeWM's 97.4%, while shared Euclidean planning on the same temporally trained checkpoint raises OGB-Cube by 14.2 points over LeWM and improves Push-T. Against LeWM and the concurrent RC-aux baseline under locked evaluation, TD-JEPA matches or exceeds both methods on every environment. Ablations show that the directed head, cross-trajectory negatives, and rollout consistency each contribute. TD-JEPA narrows the train--plan gap for JEPA world-model planners by discovering temporal progress structure in offline logs and co-designing cost form with plan-time deployment. Code is available at this https URL.

---


### 63. [Cardiologent: Multi-Agent Clinical Decision Support for Patient-Level Arrhythmia Assessment, Urgency, and Management](https://arxiv.org/abs/2607.25340)

**<font color=#1a73e8>作者：</font>** Sukju Oh, Moo-Yong Rhee, Jae-Sik Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The same episode of atrial fibrillation is a minor finding in a healthy adult and grounds for anticoagulation in an elderly patient with hypertension: identical signal, opposite decision. Naming the rhythm is only the start; what determines a patient's outcome is the judgement that follows -- what the arrhythmia is across the whole record, what it means for this patient, and what should be done about it. Recent work pairing large language models with the ECG stops short of this, reading one recording without assembling a patient-level finding; and agentic systems built around it either receive the arrhythmia a device has already detected or target a different diagnostic task, stopping before the decision this task requires. We formulate patient-level arrhythmia decision support as a task and present Cardiologent, a multi-agent system that spans it from detection to decision. An agent for each signal -- a single ECG lead and the photoplethysmogram a wearable acquires -- grounds its window reading in measured features rather than a bare label; the readings are assembled into the patient's rhythm profile and, with the patient's own data, reasoned against clinical guidelines retrieved for the case, with a critic checking each conclusion against the guideline it cites. We evaluate the clinical decision rather than the report, across integrated diagnosis, clinical significance, and urgency and management. Cardiologent scores highest on every axis, first on every patient-level task under both cardiologists and an at-scale LLM judge -- whose agreement with the cardiologists (ICC 0.74, 0.66) matches theirs with each other (0.67). Because each conclusion traces to a cited guideline and is validated against expert cardiologists, it yields decisions a clinician can audit rather than act on blindly -- a step toward use in continuous monitoring.

---


### 64. [ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning](https://arxiv.org/abs/2607.25369)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhang, Tong Chen, Junliang Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems have rapidly advanced in their ability to interact with real-world environments, leverage external tools, and provide services for users. However, unlike natural-world tasks that assume well-defined instructions, human-centered scenarios are characterized by ambiguous requests that lead to large, open-ended solution spaces. Decoding users' personalized preferences is therefore essential for narrowing the candidate solution space. This introduces a new challenge, personalized agentic reasoning, which requires agents to jointly interact with both users and environments to deliver personalized services. In this paper, we present ODYSSE, a Reinforced Fine-Tuning (RFT) framework for personalized agentic reasoning. At its core, ODYSSE proposes Episode-wise GRPO (ESPO), a novel extension of Group Relative Policy Optimization (GRPO) designed to address long action horizons and strong cross-step dependencies in personalized agentic reasoning. Rather than optimizing individual steps independently, ESPO introduces an episode-level reward mechanism together with episodic advantage estimation, enabling upstream evidence to effectively guide downstream personalized decisions and allowing agents to progressively resolve ambiguous user requests across multiple interaction steps. We further propose an episodic batch sampler that groups actions from the same episode into unified training batches, facilitating coherent optimization under ESPO. We evaluate ODYSSE on realistic long-horizon personalized GUI reasoning tasks. Experimental results demonstrate that ODYSSE consistently outperforms both specialist and general-purpose LVLMs, highlighting its effectiveness for personalized agentic reasoning.

---


### 65. [Inspect India Evals: An Open Benchmarking Framework for Evaluating Large Language Models in the Indian Linguistic and Cultural Context](https://arxiv.org/abs/2607.25375)

**<font color=#1a73e8>作者：</font>** Abhishek Kumar Singh, Shrey Nag, Sachita 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> India is a vast nation of over 1.4 billion people, varied by hundreds of diverse and locally specific traditions and cultures and 22 officially recognized languages. Large language models (LLMs) are now being deployed on a massive scale throughout the mainland as well as in remote villages. However, the common benchmarks - MMLU, BIG-Bench, and TruthfulQA are almost exclusively English- and Western-centric. They do not identify those safety, fairness, and accuracy failures unique to the Indian context. That is the gap Inspect India Evals seeks to fill. It is an open-source framework built on top of UK AISI's Inspect AI platform. It has six benchmarks: Multilingual MMLU across sixteen Indian languages, BharatBBQ (our adaptation of BBQ for Indian social bias), a safety evaluation for Digital Public Infrastructure, a multilingual safety test using harmful prompts in Indian languages, a multi-turn jailbreak resistance test, and an Indian cultural knowledge benchmark scored using LLM-as-judge rubrics. In this study, we tested five open-weight models ranging from 8B to 32B parameters. Sarvam-M 24B and Gemma 2 27B came out on top, both scoring 80% on the composite India Fairness Index, with Sarvam-M even beating larger 32B models on Indian cultural knowledge and DPI safety compliance. All models scored 100% refusal on Multilingual Safety, whereas DPI safety varied from 20% to 100%. The framework is public. It's built to work with the UK AISI registry. Anyone can reproduce or extend this work.

---


### 66. [Memory for Large Language Models](https://arxiv.org/abs/2607.25380)

**<font color=#1a73e8>作者：</font>** Sining Zhoubian, Dan Zhang, Evgeny Kharlamov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory has evolved into a foundational architectural dimension in large language models (LLMs), shifting from an implicit byproduct of computation to a spectrum of explicit, controllable mechanisms. While recent advances introduce diverse strategies---spanning transient attention, recurrent state dynamics, parameter-efficient adaptations, and scalable lookup storage---this rapid evolution has led to a highly fragmented research landscape. In this survey, we present a systematic, architecture-centric taxonomy of memory in LLMs. Our framework characterizes memory along three orthogonal axes: representation (implicit versus explicit), update dynamics (offline versus online), and persistence (short-term versus long-term). We further formalize the granular mechanisms dictating memory writing, routing, state transitions, and consolidation. This unified perspective elucidates the conceptual boundaries between computation-coupled and independently addressable memory, effectively bridging disparate architectural paradigms. Additionally, we critically analyze hybrid memory architectures, system-level efficiency trade-offs, and multi-dimensional evaluation methodologies. By consolidating these scattered advancements into a cohesive framework, this survey charts the trajectory of memory-centric LLM design and provides a principled foundation for future innovations in scalable and adaptive language modeling.

---


### 67. [Towards Reliable Stain Transfer: An Iterative Data-Model Co-Optimization Framework Based on Multimodal Expert-Guided Assessment](https://arxiv.org/abs/2607.25393)

**<font color=#1a73e8>作者：</font>** Siyuan Xu, Yan Wang, Haofei Song 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histopathological examination primarily relies on hematoxylin and eosin (H&E) and immunohistochemistry (IHC) staining. Although IHC provides critical molecular information, it is costly and requires specialized expertise. Stain transfer provides an efficient alternative by computationally generating IHC from H&E images, but remains challenged by unified and interpretable modeling for heterogeneous biomarkers under pixel-unaligned supervision. We propose DMCoStain, a novel Data-Model Co-optimization framework for Stain transfer. It iteratively co-refines training data and model capability, improving staining accuracy and interpretability in both pathological and structural consistency. To refine training data in a clinically meaningful manner, it incorporates the Multimodal Expert-Guided Finer Selection (MEGFS) strategy, built upon a pioneering IHC-positive-expression (IPE) vision-language model (VLM) that emulates pathologist reasoning. To support MEGFS, we construct ImmunoInstruction, the first large-scale IPE instruction-following dataset with 150K VQA samples. Extensive experiments on multiple tissues and biomarkers demonstrate that DMCoStain achieves state-of-the-art (SOTA) accuracy. This paradigm offers strong practical value, and MEGFS also functions as a specialized evaluation tool for future model development. Dataset, code, and more details are in this https URL.

---


### 68. [HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following](https://arxiv.org/abs/2607.25398)

**<font color=#1a73e8>作者：</font>** Liudas Panavas, Sebastian Minus, Bradley Monton 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents are increasingly deployed under standing instructions: a system prompt, a policy file, or a skills document is placed in context, and the agent is trusted to let it govern every action that follows. Existing benchmarks rarely test this deployment pattern directly; they measure whether an agent can complete a task, not whether a long, binding policy document actually constrains its behavior over an extended tool-use horizon. We present this http URL, a benchmark of 65 agentic tasks modeled on how enterprise employees follow company handbooks. Each task places an agent in a self-contained company environment, a file workspace together with mock email, chat, calendar, issue-tracking, and commerce services exposed over the Model Context Protocol, and instructs it to carry out routine professional work governed by an expert-written standard operating procedure of 20 to 124 pages. Tasks span five domains (finance, medical billing, insurance, logistics, and HR) and ten fictional companies. To resist memorization, every task modifies one of ten base handbooks, altering the specific rules and thresholds on which grading turns, so no two tasks share a policy. Grading is fully deterministic: each task carries a rubric of programmatic criteria (824 in total) that check both that required actions occurred and that prohibited actions did not. Under strict grading, where a trial passes only if every criterion is satisfied, the best of thirty evaluated model configurations passes 36.2% of trials, and most frontier configurations remain below 25%. Failures follow consistent patterns: agents let a plausible in-environment request override the standing policy, perform a required check and then act against its result, lose rule details over long horizons, and report compliance they did not achieve. We release all tasks, environments, and the evaluation harness.

---


### 69. [COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution](https://arxiv.org/abs/2607.25400)

**<font color=#1a73e8>作者：</font>** Jincheng Wang, Min Zheng, Tao Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly entrusted with natural-language workflow instructions (e.g., retail-payment policies) that specify not only what outcome to achieve, but also which steps, branches, and tool interactions are permitted. When these instructions are supplied as prompt context, however, the model retains control over both procedure selection and step execution. As interactions accumulate, an agent can skip required steps, take unsupported branches, or execute a valid step with unsupported arguments or effects--a failure mode we call workflow misalignment. In this work, we propose COVENANT, a compiler-and-interpreter architecture for workflow-aligned agent execution. Our key insight is to treat workflow instructions as source programs rather than prompts. COVENANT converts the instructions into a workflow abstract syntax tree (WAST) and lowers it to a workflow control-flow graph (WCFG). At runtime, a controller interprets the WCFG one node at a time, checks each proposal against requirements extracted from the instructions before committing controller state or advancing the graph, and returns diagnostic feedback for repair. To evaluate COVENANT, we use 120 cases from three existing benchmarks, spanning seven workflow scenarios. Compared with state-of-the-art LLM agents, COVENANT improves benchmark success from 50.00% to 83.33% and reduces the workflow-misalignment failure rate from 42.50% to 15.83% (62.75% relative). These results show that COVENANT substantially mitigates workflow misalignment, moving LLM-agent alignment beyond isolated prompt following toward reliable execution of complex and multi-step workflows.

---


### 70. [Agentic AI Autonomy Assessment: A Decision-Support Framework Towards Governed Supply Chain Systems](https://arxiv.org/abs/2607.25405)

**<font color=#1a73e8>作者：</font>** Lennart Trumpler, Rodrigo Furlan de Assis, Elias Ribeiro da Silva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Supply chain decision-making is rapidly transforming with the rise of agentic AI - highly autonomous systems that can operate on complex, long-horizon tasks. Yet the adoption of agentic systems outpaces their governance: existing taxonomies of autonomy only offer discrete classifications, rely on subjective judgement, and cannot track autonomy across a system's life cycle, leaving enterprises unable to assess the risks of increasingly autonomous supply chain agents. This paper proposes the Agentic AI Autonomy Assessment (AAAA) framework, which defines and measures the degree of autonomy at a task level. The framework is based on the three dimensions of user delegation, consultation, and collaboration, enabling continuous monitoring from an agent's development through its runtime to end-of-life. The framework's construct validity was tested in a simulated beer distribution game, examining how the autonomy score relates to a company's performance. Results reveal a weak link between autonomy and tier costs with a positional effect: upstream tiers benefit from higher autonomy while downstream tiers are harmed, positioning autonomy as an inherent dimension of agentic systems, orthogonal to capability. The framework provides a foundation for risk assessment, governance, and transparent autonomy policies to support the governed enterprise adoption of agentic AI in supply chains.

---


### 71. [Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents](https://arxiv.org/abs/2607.25408)

**<font color=#1a73e8>作者：</font>** Debjyoti Paul  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A growing body of 2026 work applies control theory to LLM agents: Lyapunov-certified stability for tool-mediated controllers (Prinos et al., "Stable Agentic Control", 2026), sample-complexity bounds for sparse policies over massive discrete tool universes (Majumdar, "Sparse Agentic Control", 2026), and regulatory-control decompositions of multi-agent systems into auditable feedback loops (Nogueira and Skogestad, 2026). We do not claim to introduce control theory to LLM agents -- that ship has sailed. Our narrower claim is about what the controlled variable is. Prior work controls tool selection, inter-agent message routing, or the agent's raw action stream. We instead treat context assembly itself -- which prompt template, which few-shot demonstrations, how much retrieved context, how many planning/verification passes -- as the controlled variable, learned online by a contextual bandit or REINFORCE policy sitting outside a frozen model. This paper develops the formal decomposition (inner frozen policy $\pi_\theta$, outer context policy $\pi_\phi$), gives a stability argument for the online controller in the sense used by Zhang et al. (2026) (non-decreasing expected reward under bounded policy change), and reports an uncertainty-calibration analysis of the controller's own confidence against realized task outcomes. The applied counterpart to this paper instantiates the same controller across three domains and two model providers and releases the dataset, trajectory logs, and a deployment recipe; here we focus on the formal framing and the stability/uncertainty evidence a control-theoretic claim requires.

---


### 72. [A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain](https://arxiv.org/abs/2607.25415)

**<font color=#1a73e8>作者：</font>** Debjyoti Paul  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production LLM agents are increasingly assembled from a frozen model wrapped in a harness: a prompt template, a tool set, a memory/retrieval layer, a planning strategy, and a verification policy. Two 2026 systems, Meta-Harness (Lee et al., 2026) and HyperAgents (Meta AI, 2026), show that this harness can itself be optimized or even self-rewritten by an agentic proposer -- at the cost of either an expensive code-search loop or unconstrained self-modifying code, neither of which is auditable or usable with a fully black-box model API. We take a narrower, more constrained position: treat the harness as a small, fixed, human-legible action space and learn a policy over it online with classic sample-efficient reinforcement learning (an $\epsilon$-greedy contextual bandit and REINFORCE), scored against a multi-objective reward (task success, verifier score, policy compliance, cost, latency, and an unsupported-claim penalty). We instantiate this control system with DSPy (Khattab et al., 2024) as both the context assembler and the source of the strongest non-adaptive baseline (a DSPy BootstrapFewShot static prompt), and evaluate it across three verifiable task domains -- tool-use workflows, code generation (HumanEval), and multi-hop retrieval QA (HotpotQA) -- and two model providers (a local Ollama model and AWS Bedrock). We release the harness-control-system code, the cross-domain verifiable task suite, the full trajectory/reward-decomposition logs from training, and a provider-agnostic deployment recipe for applying this to a new organization's domain and verification setup.

---


### 73. [Salient Knowledge Pathways: Sparse Cross-Modal Routing for Efficient Knowledge-Intensive Multimodal Question Answering](https://arxiv.org/abs/2607.25422)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad, Uluğ Bayazıt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge-intensive multimodal question answering (KI-MMQA) sits at the intersection of three expensive primitives: long visual token sequences, dense retrieval over large external corpora, and full cross-modal fusion. Existing systems pay all three costs uniformly per query, even though only a small fraction of visual content and retrieved knowledge is actually relevant to any given question. We introduce SKIP (Salient Knowledge-Injected Pathways), a unified inference architecture that routes computation along sparse pathways jointly conditioned on the question, the image, and a difficulty estimate. SKIP combines question-guided visual token pruning, region-conditional sparse retrieval, bipartite sparse cross-attention, and speculative knowledge verification with an adaptive budget controller that allocates compute proportional to predicted question difficulty. We derive an information-bottleneck bound showing that the optimal visual sparsity rate scales as $O(1/\sqrt{N})$ under realistic question-image mutual-information assumptions, with retained accuracy guarantees. Across five KI-MMQA benchmarks (OK-VQA, A-OKVQA, InfoSeek, Encyclopedic-VQA, and ViQuAE), SKIP matches or exceeds the accuracy of strong dense baselines while using $3.4$--$6.8\times$ fewer FLOPs and $2.7\times$ less end-to-end latency. Code available at: this https URL

---


### 74. [The Disruptive Impact of Large Language Models on Capture the Flag Competitions and the Path Toward Fair Play](https://arxiv.org/abs/2607.25425)

**<font color=#1a73e8>作者：</font>** Michael Macaulay, Harmony Bouabid, Guo Gen Ang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Capture the Flag (CTF) competitions are among cybersecurity's most effective training grounds, developing practical skill across cryptography, web exploitation, and binary exploitation. Large language models (LLMs) can now solve a growing share of challenges with minimal human input, raising urgent questions about fairness, the validity of rankings, and whether participation still delivers the learning that justifies the effort. This paper reports a mixed-methods study of LLM impact on modern CTFs, combining a synthesis of published benchmarks, including a recent government evaluation, case studies of live competition across three challenge categories, structured observation of the public channels where the community debates AI use, and semi-structured interviews with experienced players and organisers. We map the current human-machine capability boundary by category, showing that easy and intermediate challenges in cryptography, web, and binary exploitation are now reliably automated while narrower sub-categories continue to resist. We find that community disagreement about whether AI should be permitted is downstream of an undeclared prior question: what a competition is for. Against this backdrop we contribute a four-component safeguard framework, combining tiered competition divisions, LLM-resistant challenge design, telemetry used investigatively, and a draft community code of conduct, together with a decision tool that ties the combination of safeguards to a competition's declared purpose. The argument reaches beyond CTFs to any setting in cybersecurity where a demonstrated result is taken as evidence of an underlying ability.

---


### 75. [Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm](https://arxiv.org/abs/2607.25446)

**<font color=#1a73e8>作者：</font>** Huan Chen, Xiang Song, Jian Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent frameworks built on large language models (LLMs) routinely entangle three logically distinct concerns: who is on the team (organization), how members align (coordination), and which algorithm fuses their work (collaboration protocol). IMACS (Intelligent Multi-Agent Collaboration System) separates the three into orthogonal, independently swappable layers. Classic organizational theory (Belbin roles, Mintzberg coordination, RACI accountability) becomes executable, validated configuration, and the framework places six published collaboration algorithms behind a common interface while exposing roles, coordination, and accountability as independently configurable factors. We use this separation to conduct controlled comparisons in which organizational assignments vary while the collaboration protocol is held fixed. It also turns protocol choice into a variable that can be learned: Adaptive Org Routing, a contextual-bandit meta-protocol, selects a protocol per task under an explicit quality-cost tradeoff, outperforms every fixed protocol in a controlled study, and trains online on real benchmark and LLM-judge rewards. The ablations expose a mechanism. Accountability placement changes outcomes exactly when the protocol routes the deliverable through the accountable agent, and the winning placement flips across model families, so organizational design cannot be hard-coded; it must be revalidated, or learned, for each model binding.

---


### 76. [CoRenew: A large language model agent-based policy simulation platform for multifamily residential redevelopment](https://arxiv.org/abs/2607.25447)

**<font color=#1a73e8>作者：</font>** Yudi Zhang, Yuming Lin, Li Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The difficulty of collective action remains a central challenge in the design of policies for multifamily residential redevelopment. Stakeholders continually adjust their decisions in response to evolving negotiation contexts and the reactions of others, meaning that when a policy intervenes and which stakeholders it targets can substantially reshape collective outcomes. Assessing these adaptive responses ex ante remains difficult because existing simulation models often rely on predefined behavioral rules. Here, we present CoRenew, an open-source platform that uses LLM-based agents to simulate negotiations among multiple stakeholders and evaluate the effects of alternative policy combinations. Integrating open source geographic and demographic data, the platform can generate synthetic residents, simulate negotiation dynamics under alternative policy settings and compares policy performance across competing objectives. It supports both numerical and semantic policy inputs and includes built-in tools for visualization and result export. We validate its behavioral realism against survey responses from 324 residents and a nine-month observed negotiation process from a real redevelopment case. With its modular and adaptable architecture, CoRenew can be used to assess policies across different institutional and cultural contexts.

---


### 77. [Bits and Memories: Measuring Verbatim Extraction Across LLM Quantization](https://arxiv.org/abs/2607.25451)

**<font color=#1a73e8>作者：</font>** Akshay Sasi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are almost always quantized before they are deployed, and a growing line of work asks whether quantization also lowers their privacy risk. That work measures privacy almost entirely with membership inference. We think this is the wrong thing to measure for the risk that most people actually worry about, namely a model reproducing its training data word for word, and we measure that directly. Using the Pythia models and the public set of sequences each of them is known to have memorized, we track verbatim extraction across five precision levels, from full precision down to four bits, and across three model sizes, while measuring general capability (perplexity) at every point. We find two things. Quantization is a selective forgetter: verbatim memorization falls off faster than capability at every precision and every model size we tried, and this holds under two unrelated quantization algorithms and two evaluation corpora. But the selectivity is not enough to make quantization a privacy defense, which cuts against the optimistic reading of earlier membership-inference results. At the largest model we study, four-bit quantization still reproduces most of the memorized sequences while giving up only a few percent of capability, and the fraction of memorized data that survives quantization grows with model size. We conclude that compression should not be treated as a way to remove memorized training data, and that extraction, not membership inference, is the number practitioners should be watching. All code, sampled evaluation data, and per-configuration results are released.

---


### 78. [PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents](https://arxiv.org/abs/2607.25485)

**<font color=#1a73e8>作者：</font>** Korosh Vatanparvar, Ashutosh Joshi, Maria Xenochristou 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Health AI is evolving from answering questions to agentic systems that converse with patients, reason about health records, and act on their behalf. Primary care guards against diagnostic errors and unsafe care; agents assisting in this domain warrant evaluation against the same risks. Current benchmarks focus on medical knowledge, assessed through isolated question-answering or clinician-facing tasks. PatientAgentBench benchmarks patient-facing agentic healthcare; it evaluates a foundation model, wrapped in an agent with a sandbox of healthcare tools, conversing with a simulated patient. Each conversation is scored by an LLM-as-a-Jury across six dimensions via over a hundred conversation-agnostic, clinician-grounded criteria. To validate alignment, licensed clinicians annotated shared conversations, yielding 79-93% adjacent agreement between jury and expert raters, on par with or exceeding clinician inter-rater agreement. We benchmarked 10 models across four families on the same 1,200 scenarios and found clinical gaps. Triage quality is the most discriminating dimension: pass rates rise from 32% for the weakest models to 88% for the strongest, with agents often acting on administrative requests without clinical screening. Clinical safety and workflow accuracy follow the same pattern: the weakest models fail often, fabricating unexecuted actions, while frontier models fail on only 1-3% of cases, from unverified tool outputs and omitted crisis resources in an emergency. More capable models narrow these gaps but do not close them; the strongest scores only 4.25 of 5 overall. These failures surface only in sustained, tool-using conversations against realistic patient records, confirming that static benchmarks are insufficient as healthcare agentic systems gain autonomy. We release the framework as a reproducible, clinician-validated evaluation standard to help the field close this gap.

---


### 79. [Agentic AI in medicine: architectures, applications, evaluation, and challenges for clinical translation](https://arxiv.org/abs/2607.25489)

**<font color=#1a73e8>作者：</font>** Zheng Tong, Yang Liu, Wanshu Fan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models and multimodal foundation models are enabling medical artificial intelligence (AI) systems to move beyond isolated prediction and undertake multistep clinical tasks that require planning, tool use, memory, iterative correction, and coordination among specialized agents. However, the scope of agentic AI in medicine remains unsettled, and current evaluation practices are not yet aligned with the requirements of clinical use. We conducted a scoping review with systematic evidence mapping across five electronic sources, screened 1,649 exportable records, and provisionally included 557 unique studies that met predefined criteria for goal-directed task execution, tool use, interaction with external resources, feedback-based refinement, or multi-agent collaboration. The included studies describe single agents that use external tools, workflows supported by retrieval and external knowledge, multimodal agents, and multi-agent systems applied to medical question answering, image interpretation, electronic health record analysis, drug safety, and clinical trial prediction. The evidence base remains dominated by public benchmarks, simulated settings, retrospective datasets, and small-scale expert evaluation. Process reliability, evidence traceability, uncertainty, safety, workflow impact, and external validity are evaluated less consistently. Clinical translation will depend on clearer definitions, reproducible evaluation, auditable oversight, interoperable system design, and prospective validation in real-world clinical workflows.

---


### 80. [Beyond Counts: A Distributional Robustness Margin For Pathology Foundation Models](https://arxiv.org/abs/2607.25497)

**<font color=#1a73e8>作者：</font>** Clément Grisi, Jeroen van der Laak, Geert Litjens  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models are approaching clinical deployment, yet remain vulnerable to systematic non-biological variation across centres. Differences in tissue preparation, staining and scanning are strongly encoded in their representations, enabling shortcut learning and weakening generalisation across cohorts and institutions. The Robustness Index (RI) quantifies whether local representation geometry is dominated by biology or by non-biological variation, but its count-based formulation discards distance information. We show that adding distance weights changes little because the deeper limitation lies in RI's pooled, fixed-neighbourhood design, which obscures sample-level heterogeneity and effectively evaluates only a model-dependent subset of samples. We introduce the Cross-confounder Robustness Margin (CRoMa), a sample-resolved measure that directly compares distances to cross-confounder biological matches and same-confounder biological distractors. CRoMa recasts robustness as a cohort-wide margin distribution rather than a single pooled score. We evaluated frozen representations from 20 tile-level encoders across three benchmarks and 4 slide-level encoders on a fourth. Rankings by median CRoMa were broadly consistent across datasets, while the underlying distributions revealed substantial within-model heterogeneity. Every tile encoder retained a confounder-dominated lower tail, whose prevalence and severity varied markedly across models. These distinct robustness profiles frame model selection as a Pareto trade-off between typical and lower-tail robustness. Higher CRoMa was also associated with smaller shortcut-induced performance drops after supervised adaptation. By turning representation geometry into a distributional robustness readout that anticipates downstream shortcut susceptibility, CRoMa provides a principled basis for robustness assessment and model selection.

---


### 81. [Argus-Unified: Towards A Compact and Economical Unified Model for Image Understanding and Generation](https://arxiv.org/abs/2607.25527)

**<font color=#1a73e8>作者：</font>** Weiming Zhuang, Jiabo Huang, Jingtao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unifying visual understanding and generation in one model holds immense promise, but remains challenging and expensive due to heavy compute and data demands and conflicts between the visual features needed for these two capabilities. To address these challenges, we present Argus-Unified, a compact, effective and unified multimodal model built with low demand on computation and data. Instead of aligning modalities from scratch, Argus-Unified effectively leverages pretrained vision-language models (VLMs) that provide strong multimodal priors. Specifically, we introduce hybrid visual tokens that preserve continuous tokens for understanding while learning discrete tokens for generation from a frozen unified vision encoder. Our training pipeline includes two stages: the first stage learns a quantizer and image decoder on top of the frozen vision encoder, the second stage trains the LLM initialized from a pretrained VLM for the unified multimodal modeling. Using by far the least amount of data (15.6M) and the lowest cost (~$2,000), we demonstrate that unified multimodal models can be trained economically while achieving strong performance in both understanding and generation. Notably, our model attains state-of-the-art multimodal understanding on GQA, POPE, and VQAv2, and competitive generation quality compared to models with dedicated vision encoders (e.g., Janus, Janus-Pro), all at ~10x lower cost and with ~5x less data. We envision Argus-Unified as a useful baseline that lowers the development barrier for unified models.

---


### 82. [Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis](https://arxiv.org/abs/2607.25554)

**<font color=#1a73e8>作者：</font>** Wanxu Cai, Zhengyu Chen, Huaisheng Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Future event prediction carries broad social impact yet remains challenging. SOTA approaches augment LLMs with external agent frameworks whose predictive capability vanishes once the harness is removed. While recent Tool-Integrated Reasoning (TIR) internalizes deep search for multi-hop retrieval of facts, forecasting further demands temporal search and reasoning over historical trends and dynamic shifts. The key obstacle is data: historical queries induce temporal leakage that degrades forecasting into retrieval. Prior works either freeze information gathering with static observations, or rely on rejection sampling or unresolved fresh queries that discard vast amounts of data, degrading synthesis efficiency. We propose a time-truncation harness that enforces a temporal cut-off at every turn, enabling TIR-style sampling from historical events, reducing temporal leakage and reliance of rejection sampling or unsolved queries, increasing the sampling efficiency. We further build a large-scale corpus and a process-based metric and show that our harness naturally induces a broader temporal breadth of search and raises the proportion of high-quality data, further increasing the efficiency and reducing the reliance on complex rubrics. Distillation experiments show that students trained on harness-intervened data achieve the best performance, demonstrating harness-assisted model evolving that turns higher quality temporal search and reasoning data into a parametric advancement of the students.

---


### 83. [ReDesign: Recovering Editable Design Structures from Images via Agentic Decomposition](https://arxiv.org/abs/2607.25565)

**<font color=#1a73e8>作者：</font>** Jooyeol Yun, Jintae Park, Hyesu Lim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering an editable design file from a raster image is a common and costly bottleneck in modern design workflows, yet remains challenging since editability depends on recovering multi-modal attributes, such as typography, vector geometry, colors, grouping, and layer ordering. We present ReDesign, an agentic framework that grows an editable layer hierarchy by selecting and composing specialized tools across modalities. To keep this long decision process reliable despite imperfect tool outputs, we introduce graceful verification at each expansion, which provides local accept, prune, or retry feedback that prevents error accumulation and avoids large scale reruns. To evaluate editability at scale, we introduce the Figma Edit Replay Benchmark, consisting of 909 raw Figma files and 14,796 controlled edit instructions that replay edits on reconstructed outputs. Across this benchmark and standard reconstruction metrics, ReDesign achieves strong visual fidelity while delivering the highest editability across layout, color, and text edits, outperforming layered decomposition baselines and serial tool use pipelines.

---


### 84. [ARCHER: Agentic Rule and Compliance Harness for Executable Regulations](https://arxiv.org/abs/2607.25566)

**<font color=#1a73e8>作者：</font>** Chiraag Singh Anand, Xue Wen Tan, Lionel Teo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Verifying building compliance requires validating thousands of rules against large Building Information Modeling (BIM) designs, which is laborious, capital-intensive, and unscalable. Existing Automated Compliance Checkers (ACCs) are often difficult to generalize across different scenarios, as they are typically developed for highly specific rule sets and use cases. In addition, many ACCs are proprietary, meaning the underlying verification code is not released to end users, so users cannot verify whether their regulatory intent can be accurately captured. We introduce ARCHER (Agentic Rule and Compliance Harness for Executable Regulations), a test-driven, deterministically orchestrated multi-agent program-synthesis harness that generates auditable verification code from regulatory Codes of Practice, enabling transparent, adaptable, and scalable compliance checking. To characterize what makes agentic synthesis work, we evaluate a taxonomy of six harnesses of increasing agentic sophistication across four backbone models, spanning realistic data-governance tiers (from frontier third-party APIs to a fully on-premise open-weights model) on a novel dataset derived from real-world compliance scenarios. ARCHER's deterministic multi-agent orchestration achieves the highest accuracy for every backbone, improving mean union accuracy by 82% over a naive single-pass prompting baseline. Our cost-accuracy analysis further shows that using the ARCHER harness, a self-hosted open-weights model can reach 97.8% of frontier-API accuracy at a quarter of the cost, making data-sovereign compliance checking practical.

---


### 85. ["Dragon Slayer Becomes the Dragon": How Players Perceive and Respond to Inequality in the Game World of Whiteout Survival](https://arxiv.org/abs/2607.25574)

**<font color=#1a73e8>作者：</font>** Shiyu Lei, Ke-Xin Ren, Daiyi Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Inequality in real-world societies are associated with psychological distress and behavioral consequences. However, less is known about whether similar dynamics emerge when inequality exists within virtual environments or make-belief worlds. As online games increasingly constitute meaningful social spaces, it becomes critical to examine how players perceive and react to structural and resource differences online to optimize their experiences. This study studies perceptions of inequality in the online simulation game "Whiteout Survival," using semi-structured interviews and think-aloud gameplay walkthrough protocols. By focusing on players' interpretations of resource distribution, ranking systems, gaming mechanisms, and in-game social dynamics, our analyses revealed that players' attitudes on inequality vary according to their relative status: those occupying lower positions often criticize unfair structures, yet as they acquire stakes through resource accumulation or social integration, many defend the same systems they previously opposed. These shifts reveal how hierarchies reproduce position-dependent evaluations of fairness. The consequences of inequality on player actions depended on the transparency of game mechanisms, the structure of community hierarchies, and differential social capital. This work shows how human social perception and consequent actions are transformed when enacted in virtual processes in make-belief.

---


### 86. [IRIS: Reusable Identity Representations from Frozen LLMs for Entity Alignment](https://arxiv.org/abs/2607.25579)

**<font color=#1a73e8>作者：</font>** Xinran Liu, Shengtao Li, Shouqian Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entity alignment (EA) identifies entities across knowledge graphs (KGs) that refer to the same real-world object. Conventional EA methods mainly exploit explicit graph structures and textual fields, which often provide insufficient semantic understanding to recognize the same entity under heterogeneous descriptions and distinguish it from semantically similar entities. Although large language models (LLMs) offer deeper entity understanding, existing LLM-based EA methods largely use this capability for auxiliary generation or candidate-conditioned decisions. Consequently, such understanding is not distilled into a stable and directly comparable identity space, leaving alignment tied to specific KG pairs or candidate sets and requiring repeated processing as the matching context changes. To address these limitations, we propose IRIS (Identity Representations from Internal States), a training-free framework that constructs for each entity an iris-like signature encoding its distinctive and stable identity characteristics. IRIS derives these signatures by eliciting identity-oriented contextual representations from a frozen LLM, thereby forming a shared space in which each entity is encoded once and can be aligned across different KGs through direct similarity comparison, without pair-dependent representation construction or candidate-wise LLM inference. Across four established EA benchmarks and two frozen LLM backbones, the best IRIS variants achieve Hits@1 scores of 100.00, 99.38, 98.31, and 97.99 on D-Y-15K V2, DBP-WIKI, ICEWS-WIKI, and ICEWS-YAGO, respectively.

---


### 87. [Evaluation of forced alignment of code-mixed speech: the case of Hindi-English](https://arxiv.org/abs/2607.25581)

**<font color=#1a73e8>作者：</font>** Ayushi Pandey, Pamir Gogoi, Kevin Tang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code-mixed speech poses unique challenges to forced alignment: expanded inventories, orthographic errors, and speaker variation. We evaluate forced alignment of Hindi-English code-mixed speech using the Montreal Forced Aligner. We address 2 problems: (1) free variation involving native vs non-native pairs and (2) phonemic boundary detection for mid-utterance English words. Bootstrapping strategies substantially outperform unmodified lexicons. Acoustic models trained on sentence-level code-mixed data achieve a mean error of 4.15ms, ie. ten times lower than monolingual Hindi (38.18ms) or isolated English (37.58ms) alternatives. Principled lexicon design and code-mixed training data are both essential for reliable alignment of bilingual speech.

---


### 88. [Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact](https://arxiv.org/abs/2607.25589)

**<font color=#1a73e8>作者：</font>** Mateusz Kozłowski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical-imaging AI benchmarks combine datasets, DICOM rendering, prompts, provider APIs, automated labels, statistical code, manuscripts, and repository releases. Agreement across these artifacts is usually assumed rather than tested. We performed a retrospective forensic reproducibility audit of a preserved chest-radiograph vision-language model (VLM) pilot; no model was called again and no image or report was newly annotated. We traced prompt bindings, DICOM metadata, output completeness, label extraction, matched analyses, and release propagation. Of 300 planned model-prompt calls, 297 yielded nonempty reports. Sixty Claude calls labeled A/B were executed with the same C prompt. The 30 studies represented 28 patients. Four MONOCHROME1 images were rendered without required polarity inversion, dataset split membership was not retained, and the unvalidated extractor truncated five reports to 4000 characters. Reconstructing one common cohort of 369 complete case-finding blocks changed Cochran's Q from 154.73 to 182.29. Of 45 McNemar comparisons, 27 had unadjusted p < 0.05 and 20 remained below 0.05 after Holm adjustment. These values describe only the archived automated-label matrix; they do not recover the intended prompt comparison or establish clinical performance. We withdraw the original performance, ranking, prompt-effect, and clinical claims and specify machine-verifiable controls for cohort, DICOM rendering, prompt and model identity, call status, annotation provenance, keyed analysis, and derived artifacts.

---


### 89. [PILA: Plug-and-Play Insertion for LLM-native Advertising](https://arxiv.org/abs/2607.25590)

**<font color=#1a73e8>作者：</font>** Zhaowei Zhang, Yuhan Fu, Yihang Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How to monetize large language models (LLMs) by naturally integrating sponsored content into their responses, known as LLM-native advertising, has recently emerged as a critical problem. However, existing solutions entangle advertising with content generation inside a single model, which is incompatible with modern API-only or workflow-based LLM applications and inevitably compromises the original response quality. To address this, we propose PILA, which reformulates ad insertion as a conditional response rewriting problem and decouples it from the upstream service as a lightweight sidecar module. PILA is model-agnostic and can be seamlessly integrated with existing LLM services without modifying the base model or its workflow. It also exposes a controllable trade-off between user-side naturalness and ad-side exposure, offering a practical interface for downstream pricing and deployment. Experiments across diverse upstream models show that \pila consistently improves ad effectiveness while preserving response quality, highlighting its promise as a practical solution for LLM-native advertising.

---


### 90. [MemSFT: Mitigating Alignment Tax with an External Parametric Memory](https://arxiv.org/abs/2607.25614)

**<font color=#1a73e8>作者：</font>** Jiarui Wang, Xiang Shi, Jiaqi Cao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting Large Language Models (LLMs) to specialized domains often incurs an alignment tax, as fine-tuning on domain-specific tasks can cause catastrophic forgetting and substantially degrade performance on general tasks. We propose MemSFT, which mitigates the alignment tax by decoupling domain specialization from backbone parameter updates through a plug-and-play parametric memory. The memory is trained to imitate the behavior of a non-parametric retriever operating over domain data, thereby memorizing knowledge and patterns that would otherwise be accessed through retrieval. Once trained on a specific domain, the memory can be reused across LLMs of different sizes. During generation, a learned router dynamically fuses the output distributions of the memory and backbone at each decoding step, allowing domain expertise to be invoked selectively. Across biology, geoscience, and law, evaluations with models ranging from Qwen3-8B to Qwen3-235B-A22B show that MemSFT consistently improves domain performance with negligible degradation in general performance, whereas full SFT suffers severe forgetting on general tasks. Overall, our results demonstrate a practical path to decoupling general model capabilities from domain-specific knowledge at the parameter level, thereby equipping LLMs with new specialized capabilities without compromising their general capabilities.

---


### 91. [Beyond Epistemia: Epistemic Schizologia and Large Language Models as Techno-Semiotic Machines](https://arxiv.org/abs/2607.25620)

**<font color=#1a73e8>作者：</font>** Federico Cabitza, Gianluca Colombo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quattrociocchi and colleagues warn that the fluent outputs of large language models may allow linguistic plausibility to substitute for epistemic evaluation, producing the condition they call *Epistemia*: the experience of possessing knowledge without undertaking the practices through which judgment would ordinarily be warranted. This article accepts that diagnosis but challenges its explanatory framework, which compares an embodied, socially situated human knower with an isolated generative model thereby locating epistemic legitimacy in capacities internal to autonomous agents. Drawing on Carlo Sini's philosophy of practices, writing, signs, and technics, we propose instead to understand a large language model (LLM) as a *techno-semiotic machine* that automates a phase of written semiosis by producing plausible linguistic configurations from the sedimented archive of human writing. From this perspective, *Epistemia* is one consequence of a broader phenomenon that we call *epistemic schizologia*: the socio-technical cleavage between signs as linguistically accomplished expressions and signs as moments within socially embedded circuits of interpretation, evidence, criticism, verification, and responsibility. This cleavage is reinforced by *eikotic closure*, through which a plausible continuation is presented with the finality of an epistemic result, and by algorithmic authority and epistemic self-misrecognition. The relevant unit is therefore not the model alone but the complete practice in which generated inscriptions are prompted, interpreted, verified, contested, used, and made consequential. This reframing preserves the distinction between linguistic production and responsible understanding while grounding a design programme centred on inspectable genealogy, contestability, distributed responsibility, epistemic agency, and the evaluation of hybrid human--AIpractices.

---


### 92. [Joint Text-Audio Alignment for EEG-to-Text Decoding in Chinese Speech Production and Perception](https://arxiv.org/abs/2607.25626)

**<font color=#1a73e8>作者：</font>** Tian Zheng, Xurong Xie, Xinxin Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decoding speech information directly from scalp electroencephalography (EEG) into text provides a potential non-invasive neural communication pathway for individuals with severe speech and motor impairments. Compared with invasive approaches such as electrocorticography, EEG is safer and more widely deployable, yet substantially more challenging to this http URL challenge is exacerbated for Chinese sentence decoding, which must handle a high-dimensional output space with thousands of characters, severe inter-subject variability, and low signal-to-noise ratios for text this http URL methods commit to a single supervisory axis---either text semantics or audio acoustic features---yet neither can simultaneously satisfy the demands of sentence-level discriminability and fine-grained temporal resolution required for large-vocabulary Chinese decoding. We introduce EEGAlign, a novel parameter-efficient framework that jointly aligns EEG with two axes---text alignment with BGE-M3 text embeddings and audio alignment with wav2vec~2.0 speech features via contrastive learning followed by CTC character-sequence decoding. On ChineseEEG-2 data, EEGAlign yields state-of-the-art closed-set sentence classification performance, reaching up to 82.37% Top-1 accuracy on Reading Aloud EEG and 41.43% on Passive Listening EEG out of 101 candidates. Ablation studies show that the two alignment axes are highly complementary: combining them yields consistently better performance than either alone. To the best of our knowledge, this is the first study on decoding large-vocabulary Chinese sentences from non-invasive EEG during overt speech production, and achieving strong classification performance with relatively large closed-set candidate-sentence setting.

---


### 93. [A Human-in-the-Loop Corpus for LLM-Based Simplification of Scientific Summaries](https://arxiv.org/abs/2607.25630)

**<font color=#1a73e8>作者：</font>** Kyuri Im, Michael Färber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interdisciplinary research is accelerating, yet scientific papers remain difficult to understand outside their home fields. We study large language model (LLM)-based simplification of scientific texts and present a human-in-the-loop workflow that transforms expert summaries into more accessible versions for non-specialists. Using SciSummNet as the source corpus, we first generate baseline simplifications with GPT-4o-mini. In Phase 1, readers from STEM fields outside computer science identify difficult sentences and phrases and compare the original and GPT-simplified summaries in terms of comprehensibility, naturalness, and simplicity. In Phase 2, computer science experts use this feedback to create expert-edited reference simplifications. We release the resulting corpus together with human judgments and automatic evaluation results. The Phase 1 judgments show a clear preference for the GPT-generated summaries in terms of comprehensibility and simplicity, while qualitative analysis of the Phase 2 edits highlights the importance of preserving domain-specific terminology and the strength of scientific claims. The resulting resource supports the training and benchmarking of simplification systems for cross-disciplinary scientific communication.

---


### 94. [Construction-Driven Injection: Linguistically-Grounded Edit-Based Code-Mixing Fingerprints for Large Language Models](https://arxiv.org/abs/2607.25633)

**<font color=#1a73e8>作者：</font>** Yongyi Cui, Yue Li, Tianbao Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are costly intellectual assets that remain exposed to unauthorized redistribution and commercial misuse. Injected fingerprints, i.e., trigger--target pairs embedded in model behavior, offer a practical, black-box-verifiable ownership signal, but existing methods decouple the two stages of the fingerprint life cycle: how a fingerprint is constructed and how it is injected. Existing fingerprinting frameworks suffer from two limitations. Natural-language fingerprints are prone to accidental activation, and garbled fingerprints are easily filtered by perplexity-based detection. Furthermore, decoupling construction from injection leaves the latter unaware of the trigger's linguistic structure, missing the opportunity for targeted optimization. We argue that fingerprint construction should drive injection, and present a unified fingerprinting framework that jointly optimizes both stages. First, LCF constructs code-mixing fingerprints by combining low-resource languages under a semantic-density substitution rule and grammar-biased mixing, yielding triggers whose perplexity sits far below garbled baselines while avoiding the accidental-activation failures of natural-language triggers. Second, LCFEdit injects each fingerprint with a null-space projection derived from high-resource multilingual representations that preserves knowledge, augmented by a cross-lingual alignment step that steers the weight update toward the fingerprint language's representation subspace. This construction-aware injection ensures that the update is linguistically informed and therefore more stable. Extensive evaluations on imperceptibility, detectability, and harmlessness demonstrate persistent ownership verification with negligible impact on utility.

---


### 95. [Instruction-based Image Editing: A Survey on Data, Models, Evaluation, and Applications](https://arxiv.org/abs/2607.25642)

**<font color=#1a73e8>作者：</font>** Xianghao Zang, Zijian Jiang, Jiarong Cheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based Image Editing (IIE) aims to transform a given image into a new one based on textual instructions. Advances in Large Language Models (LLMs) and Vision-Language Models (VLMs) have accelerated progress toward practical ``one-sentence image editing" systems. This survey presents a systematic taxonomy and comprehensive review of IIE research, structured around five core dimensions: (1) task definition and hierarchical categorization of editing operations, (2) methodologies for training data construction, (3) architectural evolution from GAN-based to diffusion and autoregressive paradigms, (4) standardized evaluation metrics and benchmark development, and (5) introduction of commercial solutions. Our analysis shows critical technological milestones across model generations. We further propose a Comprehensive, in-Depth, and Diagnostic benchmark for IIE task (CDD-IIE Bench), which can rigorously assess the multiple aspects of model performance. Through empirical comparisons of open-source solutions, we highlight their respective capabilities and limitations. Finally, we discuss future research directions to advance the field.

---


### 96. [MyMentorLLM: A psychotherapy GenAI environment with multimodal voice/text patients, trainees and experts for deliberate practice](https://arxiv.org/abs/2607.25667)

**<font color=#1a73e8>作者：</font>** Rodolfo Rizzi, Alessandro Grecucci, Massimo Stella  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Psychotherapists need repeated training and supervision by experts; however, scalability is problematic. Here we present MyMentorLLM, a multimodal voice- and text-based simulation environment for deliberate practice, used to generate 2,100 complete Cognitive Behavioural Therapy (CBT) training sessions. Each session links a DSM-5-TR-grounded patient (with major depressive, generalised anxiety or borderline personality disorder), a therapist-in-training and an expert supervisor. As an initial implementation, we adopted CBT because its structured procedures and competency-based supervision facilitate standardised simulation and evaluation. Sessions were analysed for emotional dynamics, therapeutic competence and diagnostic accuracy. Simulated patients expressed disorder-congruent emotional profiles, which trainee therapists mirrored as in real human counselling. The quality of supervision differed across LLMs: while most models overestimated trainees' competences, native speech-to-speech was closest to human scores. Supervisors' feedback led to better diagnoses in simulated psychotherapists in 5 out of 7 LLMs, and symptom identification accuracy increased with model size. This work shows that simulation of deliberate practice is possible for CBT training, although patient fidelity, calibration of supervisors, and harmful feedback should be evaluated together.

---


### 97. [OmniDelta: Skill-Driven Budget Allocation for Token Compression in OmniLLMs](https://arxiv.org/abs/2607.25669)

**<font color=#1a73e8>作者：</font>** Haoyang Huang, Wenjie Huang, Tianqi Xu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emerging Omni-modal Large Language Models (OmniLLMs) enable unified understanding of text, audio, and video, but their long audio-video token sequences introduce substantial memory and inference costs. Existing compression methods mainly focus on selecting important tokens under fixed budgets, leaving the preceding budget-allocation problem underexplored. We show that direct query-to-audio/video similarity is unreliable for inter-modal budget allocation, and that uniform intra-modal budgets can miss key evidence while retaining redundant content. To address these limitations, we propose OmniDelta, a training-free, skill-driven framework that couples intent-aware inter-modal allocation with content-aware intra-modal allocation. OmniDelta first constructs audio and video skill pools to shift the fixed retained-token budget according to query demand, then reallocates modality budgets over audio segments and video frames using local complexity and temporal redundancy. The resulting local budgets can be combined with existing pruning strategies, preserving the total retained-token ratio while changing where the budget is spent. Experiments on four audio-video benchmarks with two Qwen2.5-Omni models show that OmniDelta establishes a new accuracy-efficiency Pareto frontier across pruning ratios. At 25% token retention on Qwen2.5-Omni-7B, OmniDelta reduces GPU memory by 22.0% and achieves a 1.64x end-to-end speedup over full-token inference.

---


### 98. [DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space](https://arxiv.org/abs/2607.25675)

**<font color=#1a73e8>作者：</font>** Jiangwang Chen, Zixin Song, Junlin Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-space optimization adapts large language models (LLMs) by editing external natural-language artifacts rather than model weights, so the optimized artifacts remain inspectable and the model can be treated as a black box. However, most existing text-space methods keep evaluation fixed. On open-ended tasks, this can become a bottleneck: once the solver improves on the criteria a rubric measures, omitted dimensions remain invisible to the optimization signal. Simply evolving the rubric is also unreliable when updates are selected by the current solver's score, because apparent progress can come from making the rubric easier to satisfy. We introduce DecoEvo (Decoupled Co-Evolution), which co-evolves a solver skill and a rubric-generator skill under decoupled objectives without using gold rubrics during optimization. The solver skill is updated using criterion-level feedback, while the rubric-generator skill is revised through complementary audits of requirement coverage and response discrimination that are independent of aggregate solver score. This separation focuses generator updates on newly exposed solver weaknesses, reducing repeated emphasis on criteria the solver already satisfies. Under each benchmark's official evaluation, DecoEvo outperforms all compared methods across five benchmarks and three LLM backbones, yielding 2.8--5.0\% relative gains over SkillOpt in the five-benchmark average.

---


### 99. [DynaBridge: Dynamic Summary-Guided Cross-Task Multimodal Fusion for DASS-Structured Mental Health Assessment](https://arxiv.org/abs/2607.25679)

**<font color=#1a73e8>作者：</font>** Shiyu Teng, Haichen Yu, Jiaqing Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal behavioral analysis offers a scalable approach to assessing depression, anxiety, and stress, yet generic fusion models often ignore the psychometric structure of questionnaire labels. In DASS-21, risk labels are derived from ordered symptom items through fixed item-to-subscale mappings. We propose \textbf{DynaBridge}, a dynamic summary-guided cross-task multimodal framework for DASS-structured mental health assessment. DynaBridge encodes acoustic, visual, and textual cues across multiple sessions and augments them with frozen-LLM-generated DASS-aware summaries as participant-level semantic evidence. It predicts ordinal item distributions, reconstructs depression, anxiety, and stress risk evidence from item-level soft scores, and fuses this evidence with direct multimodal risk predictions. A confidence-aware refinement strategy further incorporates high-confidence semantic cues conservatively. On the official AdoDAS validation split, DynaBridge outperforms the official baseline and representative multimodal methods, achieving 0.5012 mean F1 for D/A/S risk prediction and 0.3216 mean QWK for DASS-21 item prediction. These results show the value of bridging multimodal cues, semantic summaries, and DASS-21 psychometric structure.

---


### 100. [Rashomon Alignment](https://arxiv.org/abs/2607.25680)

**<font color=#1a73e8>作者：</font>** Moisés Santos, Peter van der Putten, Bernhard Pfahringer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Rashomon Alignment (RA), a new measure to assess functional similarity between two models. Existing functional similarity measures are distributional, quantifying differences between outputs of models applied to real-world data. However, these measures can be regarded as ecologically valid only for regions in the input space represented by the available data. We introduce a geometrical perspective on functional model similarity, which estimates it across the entire data space, offering a comprehensive view of decision boundary alignment independent of any specific data distribution. We also propose geometric Rashomon Alignment as a measure of geometrical similarity, which is computed using data uniformly sampled from the instance space. We perform an experimental analysis on more than 90 datasets, examining critical cases where model alignment diverges from predictive accuracy. Our results show that geometrical and distributional alignment provide different and complementary perspectives on the similarity between models and algorithms. RA can be used for multiple purposes, including model selection, ensemble construction, and enhanced interpretability of machine learning models and algorithms.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-131](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

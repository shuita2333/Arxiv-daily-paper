# 🧠 大模型相关研究 | 2026年07月01日

> 本类共 **247** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-247](./part-05.md)

---

### 1. [RADIANT-PET: Reasoning-Augmented PET/CT Lesion Segmentation with Large Language Models and Reinforcement Learning](https://arxiv.org/abs/2606.28392)

**<font color=#1a73e8>作者：</font>** Jiasheng Wang, Tanun Jitwatcharakomol, Piyawadee Jongpradubgiat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate lesion segmentation in PET/CT is critical for oncology, yet remains challenging because physiologic tracer uptake and artifacts can mimic malignant signal. We present RADIANT-PET, a reasoning-augmented framework that couples a high-sensitivity voxel-level segmentation model with lesion-level large language model (LLM) adjudication. Candidate uptake regions are generated with a deliberately permissive segmentation stage, then converted into structured textual descriptions that summarize uptake intensity, morphology, and regional and global anatomical context. An LLM classifies each candidate as true lesion vs. false positive, optionally leveraging the radiology report as additional clinical context. To strengthen lesion-level reasoning, we further optimize a local LLM via reinforcement learning using Group Relative Policy Optimization, rewarding correct lesion classification and anatomically concordant site assignment. Across AutoPET and an OSU test cohort, RADIANT-PET consistently outperforms strong image-only baselines, with the largest improvements observed when radiology reports are provided. Overall, these results demonstrate that LLM-based lesion-level reasoning adds a novel reasoning layer beyond conventional segmentation, suppressing physiologic false positives and aligning voxel-level predictions with clinical interpretation. The project repository is available at: this https URL.

---


### 2. [Vision-driven Preference Synthesis for Mitigating Hallucinations in VLMs](https://arxiv.org/abs/2606.28401)

**<font color=#1a73e8>作者：</font>** Yunhun Nam, Jongheon Jeong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have shown strong performance in visual understanding, yet they still suffer from hallucinations, generating content that is not grounded in the image. Preference alignment is a promising approach to improve visual faithfulness, but its success depends heavily on how preference pairs are constructed. Existing methods exhibit two key limitations; (a) intervention-based methods often introduce significant deviation from the policy distribution, and (b) sampling-based methods often underuse visual information during the construction. In this paper, we propose ViPSy (Vision-driven Preference Synthesis), a framework for constructing preference data that are both policy-aligned and visually grounded. Our framework consists of two stages; in the first stage, ViPSy derives a visual cue from recurring object-level content across semantically aligned image variants, so preference construction can rely on visual information rather than language priors. In the second stage, ViPSy conditions the policy's own rollouts on this cue, allowing candidates to be guided by visually grounded content while staying close to the policy's response distribution. The resulting candidates remain close to the policy's response distribution while better leveraging visual information from the image. Experiments show that the resulting VLM, preference-aligned with ViPSy-constructed preference pairs, achieves a new state-of-the-art in hallucination mitigation. Compared with the previous state-of-the-art method, it reduces hallucination rates on AMBER and Object HalBench by 35.7% and 24.5%, respectively. The resulting model further improves on general visual grounding benchmarks, e.g., MMStar, MMVP, and CV-Bench, while also yielding gains in semantic segmentation and ImageNet linear probing, underscoring the effectiveness of our framework in enhancing the model's visual capabilities.

---


### 3. [Can AI Draw Science? A Benchmark for Evaluating Scientific Figure Generation by Text-to-Image and Multimodal Models](https://arxiv.org/abs/2606.28406)

**<font color=#1a73e8>作者：</font>** Davie Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-image and multimodal generative models are increasingly used to produce scientific figures such as mechanism diagrams, experimental-design schematics, conceptual frameworks, and graphical abstracts. Yet existing image-generation benchmarks (e.g., GenEval, T2I-CompBench, DPG-Bench) evaluate natural images and measure compositionality, object counting, or photorealism. None of them measure what makes a generated scientific figure usable: correct and legible text labels, faithful depiction of entities and their relations, coherent diagrammatic structure, and adherence to disciplinary drawing conventions. We introduce SciDraw-Bench, a benchmark of 32 structured scientific-figure generation tasks spanning eight figure types and ten disciplines, where each task pairs a natural-language prompt with a machine-checkable specification of required labels, relations, components, conventions, and negative constraints. We propose a four-dimensional evaluation protocol: Text Fidelity (OCR-based label recall and character error rate), Semantic Correctness (vision-language-model judging against the specification), Structural Quality, and Convention Adherence, together with a meta-evaluation protocol and a preliminary inter-judge reliability analysis (human-rating validation is ongoing). We evaluate a domain-specific system, SciDraw AI, against representative general-purpose text-to-image models, and outline a code-to-figure baseline as a planned extension. In a pilot over all eight figure types, the domain-specific system substantially outperforms the general-purpose baselines on every dimension and figure type, with the largest gaps on semantic correctness and convention adherence; text fidelity remains the hardest dimension for all systems.

---


### 4. [JuZhou 1.0 Technical Report: The First Edge-Native Text-to-Image Foundation Model Trained Entirely on China-Developed AI Accelerators](https://arxiv.org/abs/2606.28421)

**<font color=#1a73e8>作者：</font>** Ce Chen, Congrui Wang, Yonglin Li 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) diffusion models typically require substantial computational resources and cloud infrastructure, posing significant challenges for edge deployment in terms of latency, cost, and user privacy. We present JuZhou 1.0, an ultra-lightweight T2I foundation model designed for fully offline, on-device execution. JuZhou 1.0 achieves its efficiency through four key designs: (1) a compact image-generation backbone consisting of a 0.385B-parameter denoising U-Net and a 1.90M-parameter distilled decoder, totaling approximately 0.387B parameters; (2) Rectified Flow training combined with DMD2 distillation, reducing inference to 4 sampling steps; (3) Chinese semantic alignment trained on 9M curated image-text pairs, enabling direct Chinese prompting without external translation at inference time; and (4) a training and distillation pipeline completed on domestically developed Sugon K100 AI accelerators without relying on NVIDIA GPUs for training or distillation. Despite its compact scale, the 28-step base model of JuZhou 1.0 achieves an overall GenEval score of 0.69, outperforming published baselines including SDXL (2.6B, 0.55), SD3-Medium (2B, 0.62), and IF-XL (4.3B, 0.61). We further validate the full poetry-to-image pipeline on Android and the core CLIP-U-Net-VAE generation branch on iOS. On a smartphone powered by the Snapdragon 8 Elite Gen 5 Mobile Platform, the 4-step U-Net denoising branch runs in approximately 1.6 seconds, while the full Android poetry-to-image pipeline takes 4.5 seconds with on-device prompt refinement on Xiaomi 17 Pro Max. These results position JuZhou 1.0 as a practical approach to mobile text-to-image generation and provide a concrete reference for Chinese-native generation, domestic-compute training, and fully offline on-device deployment after one-time installation.

---


### 5. [Is Lying an Emergent Behaviour in LLMs? Evidence from Gaslighting AI agents in a Sustainability Game](https://arxiv.org/abs/2606.28456)

**<font color=#1a73e8>作者：</font>** Subhendu Bhandary, Federico Carucci, Christos Charalambous 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLMs agents are increasingly used in multi-agent settings, yet their behaviour in sustainability games remains largely unexplored. This work investigates whether lying can emerge among LLM agents in a competitive sustainability game in which agents are informed that common resources can regenerate, although regeneration does not actually occur. We develop an agent-based model of a sustainability game in which agents manage industrial, military, and ecological resources, and interact through a network. LLM agents can observe neighbours' status, declare future attacks, receive permission to lie, and access reputation information, while rule-based agents provide an interpretable behavioural baseline. The results show that neighbour information strongly changes system dynamics, increasing attacks while improving biosphere retention and coexistence. Also, the presence of future declarations reduce extinction risk without suppressing conflict. Behaviourally, deception emerges even when agents are not explicitly allowed to lie, and explicit permission mainly increases bluffing and diversion rather than direct backstabbing. Finally, the presence of reputation memory and information about the current biosphere level reduces system ecological depletion. These findings suggest that deception can arise as an emergent behaviour in LLM-agent systems and that communication between LLM-agents could support sustainability while dealing with risk.

---


### 6. [An Agentic AI Pipeline for Appliance-Level Energy Anomaly Detection and LLM-Driven Recommendations](https://arxiv.org/abs/2606.28467)

**<font color=#1a73e8>作者：</font>** Dihia Falouz, Aida Douaibia, Amine Bechar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Appliance-level energy monitoring in office buildings produces noisy alerts that non-expert facility managers struggle to use. This paper proposes an end-to-end agentic pipeline that combines deep time-series forecasting, variational anomaly detection, and LLM-based reasoning to generate prioritized, actionable maintenance recommendations. The system tracks seven office appliances using a hybrid Singular Spectrum Analysis (SSA) and Long Short-Term Memory (LSTM) forecasting model, and applies a per-appliance LSTM Variational Autoencoder (VAE) with attention to flag abnormal daily consumption episodes. A three-stage LangChain pipeline begins with a Context Agent that always retrieves three core RAG sources (model reliability, hourly baseline, and expert knowledge) and conditionally adds up to three more (forecast context, anomaly history, global baseline) based on event characteristics, capped at eight reasoning steps. A Diagnosis Agent converts the evidence into a structured JSON diagnosis, and a Report Agent renders a human-readable narrative. A reflective memory layer incorporates operator feedback. The dashboard shows real-time 30-minute forecasts, intraday consumption, the previous day anomaly report, and a feedback form. We evaluate the forecasting model, anomaly detector with appliance-specific thresholds, and LLM reasoning on a 16-scenario benchmark including sustained and transient spikes, unexpected shutdowns, and systemic events, comparing five LLM backends under static vs. dynamic retrieval. Dynamic retrieval matches full static retrieval across all backends while cutting average context from six to three-six sources per event. The best backend scores 90.4/100 with a 100% pass rate at a 70-point threshold, and a fully local 7B-parameter model passes all 16 scenarios.

---


### 7. [GPTNT: Benchmarking Real-Time Collaboration Between Multimodal Agents on Keep Talking And Nobody Explodes](https://arxiv.org/abs/2606.28514)

**<font color=#1a73e8>作者：</font>** Amit Parekh, Sabrina McCallum, Kareem Al-Hasan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal models are increasingly deployed to solve tasks collaboratively with humans or other artificial agents. Existing benchmarks show that these models possess many of the required component capabilities, but the conditions that coincide in collaboration, including time pressure, information asymmetry, and imperfect communication, are usually studied in isolation. We introduce GPTNT, a benchmark built on the cooperative video game Keep Talking and Nobody Explodes, in which two agents must coordinate to defuse procedurally generated bomb puzzles against a live countdown. One agent can see and manipulate the bomb but does not have the defusal instructions; the other has the instructions but cannot see or manipulate the bomb. Neither agent can succeed alone: success requires effective and efficient communication. Unlike turn-based proxies, GPTNT requires agents to act asynchronously and communicate in real time. GPTNT is designed to separate collaboration from reliance on memorized solutions: the instruction manual, the partner, or both can be withheld to isolate what a model derives in the moment from what it already knows. We show that GPTNT poses a substantial challenge for state-of-the-art systems: none of the closed- or open-source models we test defuses a single bomb in real time, a bar that human players clear. Through controlled experiments, we identify critical weaknesses in state tracking, efficient action under time pressure, ambiguity handling, and error recovery. We release GPTNT as a benchmark for collaborative performance that current evaluations leave unmeasured. Because it runs on the real game, GPTNT benefits from procedural generation and inherits a living modding community, allowing the benchmark to evolve as models improve rather than being solved once and retired.

---


### 8. [CLEAR-MoE: Shared-Basis Expert Extraction from Frozen Vision Transformers via Calibration-Driven Layer Selection](https://arxiv.org/abs/2606.28516)

**<font color=#1a73e8>作者：</font>** Md Irtiza Hossain, Humaira Ayesha, Junaid Ahmed Sifat  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present CLEAR-MoE, a four-phase post-training pipeline that converts a frozen pretrained Vision Transformer (ViT) into a sparse Mixture-of-Experts (MoE) model without updating backbone weights. The pipeline (i) scores feed-forward network (FFN) layers by sparsity, clusterability, and output sensitivity; (ii) decomposes selected layers into a shared low-rank SVD basis and per-cluster residual experts using k-means clustering; (iii) trains lightweight routers supervised by cluster labels; and (iv) dispatches tokens through pluggable CUDA backends. On Imagenette with DeiT-Small, CLEAR-MoE retains 99.9% of the dense model's accuracy (86.70 +/- 0.02% versus 86.73%). Extensive ablation studies reveal a consistent empirical finding: the shared SVD basis is the primary factor responsible for preserving accuracy. Random routing, learned routing, and three different router architectures produce nearly identical performance, with accuracy varying by at most 0.06 percentage points (86.62%-86.68%). Accuracy also remains stable across different SVD ranks, expert counts (2-8), calibration set sizes (50-500), and random seeds. This behavior generalizes across five ViT backbones (DeiT-Tiny, DeiT-Small, DeiT-Base, ViT-Small, and ViT-Base), covering models from 5.7M to 86.6M parameters, with accuracy differences <= 0.10 percentage points from their dense counterparts. On a GTX 960 GPU, routing and scatter-gather overhead make the CLEAR-MoE FFN 1.3-1.7x slower than the dense implementation. A dispatch microbenchmark further shows that routing is an order of magnitude more memory-bound than expert matrix multiplications, identifying fused dispatch kernels as a promising direction for future optimization.

---


### 9. [Drag, Infer, Reproject: Grounding LLMs through Spatial Interaction for Image Clustering](https://arxiv.org/abs/2606.28517)

**<font color=#1a73e8>作者：</font>** Yang Liu, Xuxin Tang, Jiahao Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dimension reduction and semantic interaction support image clustering by making similarity structure visible and manipulable. Existing semantic interaction methods encode users' clustering criterion (a user-interpretable semantic dimension, e.g., action, location, or mood) from direct manipulation to steer reprojection, giving users direct control over the resulting layout. Yet they typically depend on learned embeddings or a predefined criterion. In practice, users' clustering criterion often emerges gradually and becomes refined through interaction rather than being fully clear at the outset. In this work, we present CriterionSI (Criterion-guided Semantic Interaction), a method that translates incremental drag interactions into criterion-guided reprojection. CriterionSI uses large language models to infer and refine the clustering criterion from sequential user drags, while grounding semantic interpretation in human-provided feedback rather than fixed prior assumptions. CriterionSI combines the inferred criterion with local drags to guide global reprojection. The simulation-based evaluation and usage scenario demonstrate that CriterionSI can discover and refine the target criterion from sequential interactions and progressively produce criterion-aligned clustering layouts. Our code and data are available at: this https URL.

---


### 10. [Detecting Clinical Hallucinations in LVLMs via Counterfactual Visual Grounding Uncertainty](https://arxiv.org/abs/2606.28520)

**<font color=#1a73e8>作者：</font>** Xiao Song, Haonan Qin, Zhaoxu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) are increasingly used for clinical image understanding, yet they remain vulnerable to \emph{hallucinations}--producing textual findings or attributes not supported by the image. We present a vision-traceable hallucination detection framework that audits arbitrary LVLM responses via visual evidence grounding, requiring neither modification nor internal access to the hidden states of LVLMs. Given an LVLM response, we extract visually verifiable entities and use a medical-domain-adapted Qwen-VL grounding verifier to localize each entity on the input image. To enhance the robustness of our detection method, we introduce a counterfactual entity perturbation method and estimate visual evidence uncertainty by contrasting factual and counterfactual grounding results. Specifically, we compute an entity-level uncertainty score from the positive confidence, counterfactual confidence, and their grounding overlap for binary hallucination decision-making. Experiments on multiple medical imaging modalities and LVLM backbones demonstrate that our method consistently improves hallucination detection performance over recent baselines, while providing interpretable localization evidence and strong cross-model transferability. Code and dataset are available at this https URL.

---


### 11. [Developmental Trajectories of Situation Modeling and Mentalizing in Transformer Language Models](https://arxiv.org/abs/2606.28524)

**<font color=#1a73e8>作者：</font>** Pamela D. Rivière, Cameron Jones, Sean Trott  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work suggests that Large Language Models (LLMs) are sensitive to the belief states of agents described by text, as measured by the false belief task (FBT), yet persistent concerns of construct validity remain. We adopt a **developmental perspective**, tracing the pattern of mental state reasoning behavior -- and likely **preconditions** for this behavior -- across multiple training stages in the Olmo2 and Pythia language model suites. We find that above-chance FBT performance depends both on model size and sufficient training volume, emerges relatively late in pretraining, and is most improved by post-training interventions (SFT, DPO) in the condition most diagnostic of mentalizing (False Belief, Implicit). However, FBT performance is fragile: consistent with past work, the use of non-factive verbs (e.g., thinks) increases false belief attributions even in the True Belief condition. To contextualize these findings, we track the emergence of **situation modeling**: the ability to report on basic factual properties of a described scene. Situation modeling accuracy generally precedes and exceeds FBT accuracy, yet situational representations also prove surprisingly incoherent in certain respects: when asked about the knowledge states of the Antagonist agent -- who always knows the item's true location -- Olmo2 13b is consistently influenced both by the Target agent's knowledge state and the presence of non-factive verbs. Together, these results suggest that larger, sufficiently trained models build partially coherent situation models in a developmentally appropriate sequence, yet display surprising fragility -- highlighting the value of developmental and stress-testing approaches for evaluating LLM capabilities.

---


### 12. [A Gravitational Interpretation of Fine-Tuning Reversion](https://arxiv.org/abs/2606.28525)

**<font color=#1a73e8>作者：</font>** Samuele Poppi, Nils Lukas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning on harmless data can partially undo behaviors acquired earlier in training. Safety can erode under benign post-alignment updates, unlearned capabilities can re-emerge, latent traits can transfer through apparently unrelated supervision, and related post-alignment fragility appears in other generative settings. We argue these phenomena are usefully viewed through a common training-history lens. Our hypothesis is geometric: large early training phases create dominant behavioral manifolds, while later alignment or specialization phases are shallower displacements from them. Subsequent fine-tuning can therefore inherit a persistent reversion component pointing back toward a witness of the dominant manifold. We call this the gravitational interpretation of fine-tuning reversion. Across our main settings, representational drift rapidly acquires a component along a history-defined reversion direction (v_rev). In our main track, alignment with v_rev rises from cos = 0.429 +/- 0.052 after the first update to 0.647 +/- 0.021 by step 20. Across 24 run-step pairs, every observed alignment exceeds the p99 of an isotropic activation-space null. We demonstrate that selectively blocking motion along v_rev changes the final alignment at T=100 from 0.648 +/- 0.009 to -0.211 +/- 0.021 and reduces harmfulness from 19.0% +/- 4.0% to 8.5% +/- 1.5% with little task cost. These results support v_rev as a causally relevant mediator of early post-alignment reversion in our setup. Importantly, we do not claim that v_rev is the unique safety direction, nor that the dominant manifold is directly observed; rather, we identify a robust, history-defined direction that explains and partially controls early reversion dynamics.

---


### 13. [NIVA: A Multimodal Foundation Model for Actionable Earth System Intelligence](https://arxiv.org/abs/2606.28546)

**<font color=#1a73e8>作者：</font>** Anisha Pal, Aodhan Sweeney, Kyle Heyblom 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI-driven weather and climate modeling have improved forecast skill while reducing computational cost. However, existing data-driven approaches are limited in their ability to model coupled Earth system dynamics, which is required for extending predictability beyond the ~2-week horizon. To address this, we introduce NIVA, a multimodal foundation model designed to learn unified representations across Earth system components. While the full framework targets atmosphere, ocean, ice, and land interactions, we focus here on a two-modality setting (ocean and atmosphere) as a controlled proof of concept to evaluate whether foundation models can learn coupled dynamics. Trained on large-scale Earth system simulations, NIVA learns physically meaningful cross-modal structure, providing a foundation for subseasonal-to-seasonal prediction. As initial validation, we show that NIVA captures key modes of climate variability through accurate prediction of major climate indices.

---


### 14. [Turn-Averaged SAEs for Feature Discovery and Long-Context Attribution](https://arxiv.org/abs/2606.28548)

**<font color=#1a73e8>作者：</font>** Kevin Der, Harish Kamath, Ben Thompson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have become a useful tool for extracting interpretable features in language models. However, standard SAE architectures operate on individual token activations, meaning that the number of active features scales linearly with context length, and studying long model transcripts becomes difficult. We introduce turn-averaged SAEs, which represent a single Human or Assistant turn with a fixed number of features by learning to reconstruct the average model activation across the turn. We find that turn-averaged features describe a single turn's high-level characteristics more completely than per-token features when judged by an LLM. We also demonstrate that turn-averaged SAEs greatly simplify common downstream uses of SAEs like attribution graphs. Broadly, turn-averaged SAEs make interpretability techniques practical at long context lengths.

---


### 15. [DataComp-VLM: Improved Open Datasets for Vision-Language Models](https://arxiv.org/abs/2606.28551)

**<font color=#1a73e8>作者：</font>** Matteo Farina, Vishaal Udandarao, Thao Nguyen 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building performant Vision-Language Models (VLMs) requires carefully curating large-scale training datasets, yet the community lacks systematic benchmarks for evaluating such curation strategies. We introduce DataComp for VLMs (DCVLM), a benchmark for controlled data-centric experiments to improve VLM training. As part of DCVLM, we collect 160 datasets spanning four data types -- image-caption pairs, multimodal interleaved documents, text-only, and instruction-tuning data -- into a corpus of 6T multimodal tokens. DCVLM allows participants to test curation strategies (filtering, mixing, formatting, sampling) across 1B-8B models and 6.25B-200B token budgets. Models are then evaluated on a carefully selected suite of up to 52 downstream benchmarks across 9 domains. We conduct extensive experiments on DCVLM and find that data mixing, not filtering, is key to a high-quality training dataset: instruction-heavy mixtures scale better than caption-heavy ones, with gains widening at larger scales. The resulting dataset, DCVLM-Baseline, enables training an 8B VLM to 63.6% accuracy on our 33-task core suite with 200B training tokens. Compared to FineVision, the state-of-the-art open VLM training dataset, this represents an improvement of +5.4pp. DCVLM and all accompanying artifacts will be made publicly available at this https URL.

---


### 16. [IMCBench: A benchmark for multimodal LLMs in Image-grounded Medical Conversations](https://arxiv.org/abs/2606.28556)

**<font color=#1a73e8>作者：</font>** Maria Xenochristou, Ashutosh Joshi, Korosh Vatanparvar 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models and vision-language models have enabled reasoning over multimodal data, offering opportunities for clinical applications such as decision support and triaging. However, existing medical AI benchmarks are fragmented: some support multi-turn dialogues but lack images, while others provide multimodal inputs but focus on single-turn QA tasks. To address this gap, we introduce IMCBench, an image-grounded, multi-turn medical conversation benchmark that pairs real, publicly available clinical images with synthetic patient profiles to simulate realistic patient-clinician interactions. Each conversation is evaluated across three clinical dimensions: safety, accuracy, and appropriate use of uncertainty in diagnosis. We benchmark eight multimodal frontier models across four model families (Claude, GPT, Nova, and Llama), scoring each on a 1-5 scale using LLM-as-Jury scoring calibrated against expert clinician annotations. Our results show that Claude Opus 4.6 achieves the highest overall score (3.61), followed by Claude Sonnet 4.6 (3.30) and GPT-5.2 (3.29), though no model dominates all dimensions and safety degrades for both malignant and rare conditions ($\Delta$ = -0.27 each). Ablation studies further reveal that both visual input and EHR context contribute to safe guidance (safety drops of 0.18 and 0.23 on average when each is removed), with stronger models leveraging visual features more effectively. Together, these findings demonstrate that accurate clinical description does not guarantee safe patient guidance, motivating the need for multi-dimensional evaluation frameworks in medical AI.

---


### 17. [Digitizing Coaching Intelligence: An Agentic Framework for Holistic Athlete Profiling using VLM and RAG](https://arxiv.org/abs/2606.28570)

**<font color=#1a73e8>作者：</font>** Deep Ghosal, Ishani Sen, Wazib Ansar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Athlete assessment is a critical process for tracking physical progress and identifying elite talent. However, during mass recruitment drives, traditional methods rely on manual observation, which is inherently subjective and unscalable, or basic computer vision (CV) systems limited to quantitative repetition counting. These standard approaches lack the "coaching intelligence" required to evaluate qualitative physiological markers such as form degradation, spinal articulation, and fatigue. This paper presents a novel, LLM-based hybrid agentic framework for automated, holistic athlete profiling that strictly aligns with the Sports Authority of India (SAI) assessment protocols. Orchestrated via LangGraph, our dual-pipeline architecture synthesizes the geometric precision of CV (MediaPipe) for kinematic tracking with the semantic reasoning of Vision-Language Models (Llama-4-scout). To overcome the latency and token constraints associated with multimodal video processing, we introduce a 3 X 3 "Smart Grid" temporal chunking strategy, reducing computational overhead by over 88% while preserving critical temporal continuity. To ensure data integrity and mitigate hallucination, the framework pioneers an autonomous "LLM-as-a-Judge" self-correction loop that cross-references quantitative and qualitative metrics before persistence. Finally, we implement a dual-persistence Retrieval-Augmented Generation (RAG) pipeline utilizing a vector search engine (ChromaDB). This enables coaches to bypass rigid SQL databases and perform complex semantic queries (e.g., "Identify athletes with high endurance but poor core rigidity") using natural language. Experimental results demonstrate that this multi-agent approach significantly bridges the gap between raw biometric tracking and actionable coaching insights, offering a scalable, objective solution for national talent identification.

---


### 18. [Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs](https://arxiv.org/abs/2606.28574)

**<font color=#1a73e8>作者：</font>** Manuel Pita  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a large language model (LLM) codes a construct in text as a human annotator would, that agreement makes the LLM a reliable coder. Yet reliability leaves construct validity untouched. The instrument may be theory-naive, reaching the code through a correlate that meets none of the demands the construct's theory makes, and no current method tells that apart from genuine measurement. We propose grain calibration as a method that closes the gap. It decomposes a construct into clause-level components, tests each against the text with extractive evidence, and combines the results through an explicit, theory-derived rule. Because the rule is stated rather than lodged in one opaque pass, its structure is evidence about the process rather than the output. It shows which components settled a code, and, when the code is wrong, whether a component was missed or an adjacent construct mistaken for it. Validation shifts from scoring an instrument's outputs against an annotator to showing that the instrument runs on the construct its theory specifies.

---


### 19. [Search for Truth from Reasoning: A Dynamic Representation Editing Framework for Steering LLM Trajectories](https://arxiv.org/abs/2606.28589)

**<font color=#1a73e8>作者：</font>** Tianlong Wang, Yuhang Wang, Weibin Liao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current approaches to enhance Large Language Model (LLM) reasoning, such as Chain-of-Thought and "Wait" prompts, primarily encourage models to think more, yet often fail to guide them toward Truth. While Representation Editing (RepE) offers a intrinsic control, its application to dynamic reasoning trajectories remains underexplored. In this work, we bridge this gap by investigating the geometry of truth within unfolding reasoning chains. We uncover three critical insights: (1) Truth is encoded at the sentence level and is entangled with latent reasoning patterns; (2) Effective intervention follows an Uncertainty Principle and a Decay Effect, requiring localization to early, high-entropy forks; (3) Naive steering vectors suffer from noise, risking collateral damage to correct trajectories. Based on these findings, we propose DynaSteer, a dynamic RepE framework. DynaSteer employs pattern clustering to disentangle reasoning manifolds and utilizes Fisher-LDA to project purified truth. By dynamically monitoring lookahead entropy, it selectively steers and rolls back trajectories only when necessary. Comprehensive experimental results on several MATH benchmark verify the effectiveness of DynaSteer, and experiments on out-of-domain coding tasks further confirm its generalization ability. Our code is publicly available at this https URL.

---


### 20. [What LLMs explain is not what they believe: Evaluating explanation sufficiency under models' own input beliefs](https://arxiv.org/abs/2606.28615)

**<font color=#1a73e8>作者：</font>** Nhi Nguyen, Shauli Ravfogel, Rajesh Ranganath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in high-stakes domains, where free-text explanations such as chain-of-thought and post-hoc rationales are used to justify model outputs. Yet it remains unclear whether these explanations are sufficient, i.e., if they contain enough information to explain the model's output-generating process. We generalize classical sufficiency from feature attributions to arbitrary explanations and prove that explanation sufficiency can change depending on the input distribution, which must be explicitly defined for LLM explanations. We propose using the LLM itself to generate alternative inputs conditioned on an explanation, capturing its beliefs about possible inputs. We formalize self-consistent sufficiency as a goal for free-text explanations and introduce an information-theoretic metric, SCSuff, that enables evaluation of free-text explanations without relying on predefined biases or shortcuts. Our experiments show that SCSuff agrees with targeted perturbation tests where applicable and demonstrate that explanation sufficiency can vary with the input distribution. We find LLM explanations are generally insufficient and weakly correlated with model size, accuracy, or output entropy. Analysis of final-token hidden states shows that top and bottom SCSuff scores can be predicted from internal representations, suggesting that SCSuff can guide detection and improvement of sufficient LLM explanations. The code for this paper is available at this https URL .

---


### 21. [Phonological Perception of Sign Language Models](https://arxiv.org/abs/2606.28667)

**<font color=#1a73e8>作者：</font>** Kayo Yin, Jessica Carter, Alex Xijie Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign languages are compositional systems where meaning arises by combining sublexical phonological parameters, such as handshape, location, and movement. While deep learning models for Sign Language Recognition (SLR) have achieved increased performance on translation benchmarks, it remains unclear whether these models distinguish abstract phonological features or merely rely on low-level statistical correlations. This work evaluates the phonological perception of SLR models trained on American Sign Language (ASL) by probing phonological sensitivity using minimal pairs and evaluating representational alignment with human behavioral data. Our results reveal that SLR models exhibit emergent phonological sensitivity, but with clear architectural trade-offs: pose-based models are sensitive to handshape contrasts, while pixel-based models better capture location changes. Furthermore, pose-based models learn latent representations that correlate with human perceptual similarity judgments (r~0.49). These findings suggest that while SLR models exhibit emergent phonology, current training paradigms are insufficient to scale them beyond their architectural inductive biases.

---


### 22. [BackTranslation2.0 -- A Linguistically Motivated Metric to Assess Sign Language Production](https://arxiv.org/abs/2606.28673)

**<font color=#1a73e8>作者：</font>** Oliver Cory, Maksym Ivashechkin, Karahan Sahin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign Languages (SLs) are the primary means of communication for millions of deaf individuals, yet existing evaluation metrics for generated SL remain simplistic and poorly aligned with human judgements. We introduce BackTranslation2.0, a linguistically grounded evaluation metric for text-to-sign translation that moves beyond naïve backtranslation. Our approach adopts an agentic framework in which a deterministic pipeline orchestrates a suite of specialised tools to assess four scoring dimensions - grammatical correctness, phonological accuracy, motion fluency, and generation fidelity - aligned with human rater assessments. Tool outputs are not treated independently: a set of large language model (LLM)-based cross-referential comparison modules evaluates consistency across tools and checks outputs against linguistic expectations, enabling structured reasoning over grammatical, phonological, and motion-level evidence. Final dimension scores are computed through deterministic weighted formulas over validated tool outputs. To validate BackTranslation2.0, we introduce and evaluate on a British Sign Language (BSL) dataset rated in a human rater study across the same quality dimensions, following a protocol developed in collaboration between linguists and deaf experts, benchmarking against six baseline metrics. Our method demonstrates strong correlation with human judgements across all dimensions, providing a more comprehensive, interpretable, and linguistically principled evaluation framework for sign language production systems.

---


### 23. [Aristotelian Virtue Profiling of LLMs through Ethical Dilemmas](https://arxiv.org/abs/2606.28683)

**<font color=#1a73e8>作者：</font>** Ioannis Tzachristas, John Pavlopoulos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often face ethical tradeoffs in which several responses may be defensible but express different priorities, such as fairness, honesty, courage, or restraint. We introduce VirtueMap, a framework for describing these patterns through an Aristotelian virtue-ethics lens. Instead of asking for a single correct answer, VirtueMap asks humans or LLMs to rank all five responses to each of seven general, non-lethal, non-political, and non-religious ethical dilemmas. To define the reference orderings used for scoring, we first proposed, for each dilemma and virtue, an ordering of the five responses from most to least expressive of that virtue. We then collected more than 100 respondent evaluations per ordering and retained it as operational ground truth only when at least 95% confirmed it. Rankings are scored against these retained orderings using normalized Borda alignment, yielding profiles over Practical Wisdom, Justice, Truthfulness, Courage, and Temperance. We apply VirtueMap to nine LLM families in a repeated-run evaluation and find high mean rank consistency (90.3%), with the largest differences appearing on Courage, Temperance, and Justice. We also release an interactive website that computes profiles locally in the browser and compares respondents with measured LLM profiles.

---


### 24. [An AI agent for treatment reasoning over a biomedical tool universe](https://arxiv.org/abs/2606.28692)

**<font color=#1a73e8>作者：</font>** Shanghua Gao, Ayush Noori, Richard Zhu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Treatment reasoning underpins every therapeutic decision, integrating disease context, comorbidities, medications, contraindications, and evolving biomedical knowledge to select an appropriate therapy. It is inherently iterative: candidates are weighed against many constraints, revised as evidence emerges, and grounded in verifiable sources. Here we introduce ATHENA-R1, an AI agent for treatment reasoning across all FDA approved drugs since 1939, trained by reinforcement learning over a universe of 212 biomedical tools. At each step it identifies missing information, selects and runs relevant tools, and incorporates the evidence. To train it without human-annotated traces, we build a two-level self-learning framework: multi-agent systems construct the tools, tasks, and reasoning trajectories for supervised fine-tuning, then reinforcement learning with scientific feedback rewards reasoning quality (evidence gathering, grounded tool use, logical non-redundancy). Across five benchmarks of 3,168 drug reasoning tasks and 456 patient treatment cases, ATHENA-R1 outperforms language models and tool-use systems, reaching 94.7% accuracy on open-ended drug reasoning and 82.9% on treatment reasoning, 17.8 and 10.7 points above GPT-5. In blinded evaluations by experts from 28 rare disease organizations, it is preferred over reference models on all criteria, and physicians rated it favorably on complex hospitalized cardiovascular and infectious-disease cases. Adverse-event hypotheses it generated, tested in electronic health records from 5.4 million patients, reached adjusted odds ratios of 1.48-1.84, with no elevation among negative controls. Because it requires knowing what evidence to seek before concluding, treatment reasoning has long been hard for AI; we show it can be reframed as a learnable process of iterative evidence gathering that reinforcement learning can train AI to perform.

---


### 25. [COMPASS: Grounding Composition-Intent Guidance in Unified Multimodal Models](https://arxiv.org/abs/2606.28696)

**<font color=#1a73e8>作者：</font>** Ziqi Zhou, Weize Quan, Mining Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Composition is a high-level visual intent that governs where subjects are placed and how a scene is organized, yet current unified multimodal models remain unreliable at fine-grained composition recognition and struggle to turn such intent into controllable generation. We present COMPASS, the first unified multimodal framework that grounds composition-intent control in a single system spanning both composition perception and composition-guided generation, with a shared expert token $\tau_c$ as the central intent anchor. On the perception side, COMPASS injects composition expertise into an MoE backbone in a minimally invasive manner and distills the inferred intent into $\tau_c$. On the generation side, COMPASS reuses $\tau_c$ as a global conditioning signal that steers the denoising trajectory, effectively converting passive composition analysis into explicit layout control. To support systematic instruction-following composition learning and evaluation at scale, we construct Comp-11, a large-scale dataset with an 11-class taxonomy and reasoning-augmented annotations. Extensive experiments show that COMPASS substantially improves category-level composition understanding and delivers more composition-consistent, prompt-faithful generation than strong baselines.

---


### 26. [Mitigating Batch Effects in Histopathology via Language-Mediated Robust Embedding Generation](https://arxiv.org/abs/2606.28697)

**<font color=#1a73e8>作者：</font>** Yishu Zhang, Shushan Wu, Zhenzhong Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (PFMs) have demonstrated strong potential across clinical and scientific applications, yet their performance is often hindered by batch effects, which are non-biological variations across tissue source institutions (TSIs) that distort learned feature representations and impair generalization. Conventional mitigation strategies, such as stain normalization, offer limited success in addressing these high-dimensional, complex artifacts. We present GLMP (General-purpose LLM-Mediated Pathology model), a novel framework that generates robust numerical embeddings from histology image patches through an intermediate textual representation. By leveraging pretrained general-purpose multimodal large language models (MLLMs) and text encoders, GLMP effectively prioritizes biologically meaningful signals over TSI-specific artifacts, thereby improving cross-institutional generalization. To our knowledge, GLMP is the first pathology model to use text descriptions of histological features as an intermediate representation for generating numerical embeddings from histology images. Our results highlight the untapped potential of broad-domain, non-specialized MLLMs in computational pathology and introduce a new paradigm for building versatile, generalizable, and robust pathology models.

---


### 27. [AnTenA: Actionable and Explainable Tensor Analysis System with Large Language Models](https://arxiv.org/abs/2606.28708)

**<font color=#1a73e8>作者：</font>** Dawon Ahn, Auder Der, Evangelos E. Papalexakis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurately explaining hidden patterns in multi-aspect data has typically been done by leveraging labels and/or accompanying auxiliary metadata. However, labels and auxiliary data may be inaccurate (e.g. nonstandard, inconsistent), insufficient (e.g. static tabular metadata for time-dependent recordings), or unavailable. %
We propose \fullmethod (\method), which leverages the knowledge of large language models (LLMs) to explain the hidden patterns in human narratives. \method uses task-agnostic and task-specific prompts to explain extracted co-clustered latent patterns from tensor decomposition. To evaluate these explanations, we test the LLMs on forward and backward inference tasks. % Our demo system is available at this https URL.

---


### 28. [ComMem: Complementary Memory Systems for Test-Time Adaptation of Vision-Language Models](https://arxiv.org/abs/2606.28719)

**<font color=#1a73e8>作者：</font>** Guanglong Sun, Shuang Cui, Bo Lei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) of vision-language models (VLMs) is essential for their robust deployment in dynamic, real-world environments. However, existing TTA methods often adapt locally without accumulating knowledge over time, or operating within a single modality without exploiting VLMs' inherently multi-modal nature. Inspired by the \textbf{Com}plementary \textbf{Mem}ory systems of the biological brain, we propose \textbf{ComMem}, an innovative approach that mimics the distinct but cooperative roles of the hippocampus and neocortex to enable effective TTA for VLMs. ComMem consists of two key components: a fast-adapting detailed memory, akin to the hippocampus, that forms a dynamic visual cache from high-confidence test samples; and a slow-integrating abstract memory, akin to the neocortex, that continually refines global textual prototypes. For each test instance, ComMem jointly optimizes both memory systems to ensure cross-modal consistency. Extensive experiments on 15 benchmark datasets show that ComMem significantly outperforms state-of-the-art methods under both natural distribution shifts and cross-dataset generalization, offering a promising direction for enhancing VLMs' practical adaptability.

---


### 29. [CCRC: A Change-Aware Captioning and Reasoning Chain for Image Change Captioning and Segmentation](https://arxiv.org/abs/2606.28724)

**<font color=#1a73e8>作者：</font>** Jinhong Hu, Xiaoping Wang, Shuyin Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding and localizing subtle changes between paired images is critical for tasks such as surveillance and image editing. However, traditional Image Change Captioning (ICC) methods lack spatial grounding, limiting their precision. We introduce Image Change Captioning and Segmentation (ICCS), a new multimodal task that jointly requires structured change description and pixel-level localization. To address ICCS, we propose the Change-aware Captioning and Reasoning Chain (CCRC), a dual-chain framework that decouples semantic reasoning from spatial segmentation. The first chain, Chain-of-Change-Captioning (CCC), enhances fine-grained change perception via a visual fusion module based on Multi-Head Change-aware Attention inserted between the visual and language components of a Multimodal Large Language Model (MLLM). CCC also determines whether a change is segmentable. If not, it alone generates the caption. Otherwise, the second chain, Chain-of-Change-Segmenting (CCS), is activated, leveraging spatial priors from CCC and refining masks with a Change-aware Token Refiner for accurate boundary localization. We evaluate CCRC on both synthetic and real-world change detection benchmarks with pixel-level supervision. Experiments show CCRC achieves state-of-the-art performance.

---


### 30. [Agentic Abstention: Do Agents Know When to Stop Instead of Act?](https://arxiv.org/abs/2606.28733)

**<font color=#1a73e8>作者：</font>** Han Luo, Bingbing Wen, Lucy Lu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are expected to act over multiple turns, using search, browsing interfaces, and terminal tools to complete user goals. Yet not every goal is well specified or achievable in the available environment. In such cases, a reliable agent should recognize that further interaction is unlikely to help and abstain from additional tool calls. We define Agentic Abstention, the problem of deciding when an agent should stop acting under uncertainty. Unlike standard LLM abstention, which is usually evaluated as a single-turn answer-or-abstain decision, agentic abstention is a sequential decision problem: an agent can answer, abstain, or gather more information at each turn, and the need to abstain may only become clear after interacting with the environment. We study this problem across web shopping, terminal environments, and question answering, evaluating 13 LLM-as-agent systems and 2 agent scaffolds on more than 28,000 tasks. Our results show that the main challenge is not only whether agents can abstain, but also when they abstain. Some agents never abstain when they should, while others do so only after many unnecessary interactions. This gap is especially large on tasks where the instruction appears feasible until the environment reveals otherwise (e.g., no valid result matches the instruction). We further find that model scale, reasoning, and agent scaffolding affect abstention in different ways, where larger or more capable models sometimes perform worse at timely abstention. Finally, we introduce CONVOLVE, a context engineering method for improving agentic abstention that distills full interaction trajectories into reusable stopping rules. On WebShop, CONVOLVE substantially improves timely abstention without updating model parameters, raising Llama-3.3-70B's timely recall rate from 26.7 to 57.4. Our dataset and code are available at this https URL

---


### 31. [5ting at SemEval-2026 Task 8: Strong End-to-End Multi-Turn RAG via LLM-Based Reranking and Faithfulness Control](https://arxiv.org/abs/2606.28737)

**<font color=#1a73e8>作者：</font>** Thien-Qua-T-Nguyen, Chi Hoang, Nguyen Tran 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce 5ting, our system for the SemEval2026 Task 8 (MTRAGEval), which evaluates multi-turn Retrieval Augmented Generation (RAG) systems. Multi turn RAG involves context drift, under specification, and hallucination risk. Our system combines BGE-M3 dense retrieval with FAISS indexing, dual-query merged retrieval, and LLM based reranking, followed by role separated generation constrained to retrieved evidence. The retriever achieved nDCG@5 = 0.4719 in Task A, while the end to end system ranked in Task C with a harmonic score of 0.5597 and RL_F = 0.7692.

---


### 32. [Agent Safety Is Action Alignment](https://arxiv.org/abs/2606.28739)

**<font color=#1a73e8>作者：</font>** Shawn Li, Yue Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly act as agents: they call tools, move money, delete records, and send messages on a user's behalf. To keep them safe, practitioners imported the chatbot-era recipe (train the model to refuse unsafe inputs) into the agentic setting, and treat the resulting capability loss as a manageable ``alignment tax.'' We argue this is a \emph{category error}. Refusal is a primitive for \emph{content safety}, where the harm is in the model's output and is therefore a learnable function of it. Agentic harm is different in kind: it lies not in any output but in the relation between the authority an action exercises and the authority the user granted, which is absent from the text the model sees. Importing content-safety methods into this regime does not trade capability for safety; it pays capability and buys negative security. We support this with three lines of evidence spanning the autonomy spectrum: defense-trained models learn surface patterns rather than intent; the same training collapses multi-step agents before any threat appears while leaving them exploitable; and even undefended frontier models exceed granted authority under ordinary use. We conclude that action safety cannot be installed in weights. It must be expressed as \emph{least privilege}, enforced \emph{outside} the model at the action boundary, and evaluated as \emph{action alignment} (a relational, deployment-conditioned property) rather than a refusal score.

---


### 33. [A Path-Space Formulation of Prediction in World Models: From a Single Action to Prediction, Planning, and Irreversibility](https://arxiv.org/abs/2606.28751)

**<font color=#1a73e8>作者：</font>** Gunn Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a path-space formulation of prediction in AI world models. Rather than sequences of one-step conditional distributions, we argue that a world model implicitly defines a probability measure over future trajectories. In the local regime where latent dynamics admit an effective Markovian description, this path measure takes the Onsager-Machlup form. Within this framework, prediction (most probable trajectory), planning (constrained optimization), and uncertainty (fluctuations) emerge as operations on a single action functional. We decompose the latent dynamics into reversible and irreversible components and introduce operational measures of entropy production from model rollouts. In controlled small-scale attention-based models, we find that attention asymmetry is acquired during training in proportion to the irreversibility of the data. Symmetrizing the learned attention suppresses entropy production and selectively degrades long-horizon prediction of irreversible dynamics while preserving relaxational prediction. These results suggest that irreversibility may serve as a computational resource for predictive world models. More generally, the fundamental predictive object is a distribution over future paths rather than states.

---


### 34. [A Physics-Grounded Benchmark for Multi-Agent Dynamics in World Models](https://arxiv.org/abs/2606.28757)

**<font color=#1a73e8>作者：</font>** Nuo Chen, Lulin Liu, Zihao Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative world models hold immense promise as scalable simulators for autonomous systems, particularly for synthesizing rare but safety-critical multi-agent interactions, such as vehicle collisions. However, current evaluation paradigms index heavily on visual fidelity and semantic alignment, leaving a critical blind spot: they cannot reliably quantify whether generated dynamics actually obey the fundamental physical laws required for reliable simulation. Assessing this physical plausibility is inherently difficult due to a lack of physical metrics and the challenge of extracting metric-scale kinematics from uncalibrated video rollouts. To bridge this gap, we introduce CrashTwin, a physics-grounded evaluation framework designed to stress-test the physical trustworthiness of world models. CrashTwin couples a diverse dataset of multi-agent collision scenarios, comprising 25K controllable synthetic and 12K in-the-wild real-world collision sequences with a novel calibration-free reconstruction pipeline, enabling the recovery of 3D physical attributes directly from world model rollouts. We propose a diagnostic suite that systematically evaluates three dimensions: spatio-temporal consistency, momentum and kinetic energy conservation, and world-dynamics integrity. Extensive benchmarking of state-of-the-art models reveals a crucial insight: high perceptual quality frequently masks severe physical violations during complex interactions. By quantitatively exposing these failure modes, CrashTwin provides a vital diagnostic tool for developing physically grounded world models capable of reliable real-world simulation.

---


### 35. [X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving](https://arxiv.org/abs/2606.28758)

**<font color=#1a73e8>作者：</font>** Bohao Zhao, Chengrui Wei, Guangfeng Jiang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting future states is essential for autonomous agents, yet current Vision-Language-Action (VLA) models fundamentally lack this capability, relying instead on reactive perception-action mapping. While integrating Predictive World Models (PWMs) addresses this gap, existing approaches either incur prohibitive cascaded latency or act as shallow terminal tasks that fail to deeply embed forward-looking reasoning. To endow VLA models with this reasoning capability, we propose X-Mind. Rather than treating PWMs as an external auxiliary module, this framework internalizes them as the Visual Chain-of-Thought (Visual CoT). By enforcing a world rollout prior to action, the model is constrained to imagine future evolution first, yielding a driving policy that is robustly grounded in environmental dynamics and aware of the future consequences its actions will unfold. The challenge here is efficiency, and we tackle it on two fronts. First, we introduce a compact representation of visual thinking: an abstract sketch that fuses a Bird's-Eye-View (BEV) layout with abstract driving priors (e.g., navigation intents and traffic rules). Rather than rolling out dense future frames, the model reasons over this sketch as a mental canvas; aided by a Deep Compression Autoencoder (DC-AE), a 12-frame future rollout is reduced to merely 96 tokens, alleviating the long-context computational bottleneck. Second, to accelerate generation further, we propose a recurrent block diffusion scheme that unrolls the denoising steps across the layers of the large drive model, folding iterative refinement into the backbone's one forward pass. Trained and validated on large-scale real-world data, X-Mind achieves competitive end-to-end driving performance, which makes it a highly practical, low-latency solution that successfully deploys large-scale cognitive reasoning directly onto resource-constrained vehicle platforms.

---


### 36. [Mechanistic Personality Analysis of LLMs Steering Personality via Latent Feature Interventions](https://arxiv.org/abs/2606.28770)

**<font color=#1a73e8>作者：</font>** David Courtis, Ting Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated the ability to simulate human-like OCEAN personality traits in generated text. Previous efforts have focused on prompt engineering or fine-tuning to shape LLM personality. In this work, we propose a mechanistic interpretability approach that directly intervenes on the model's latent features. Our method identifies latent directions in the residual stream corresponding to a target OCEAN trait using sparse autoencoders (SAEs) and contrastive activation analysis. We formalize an additive steering vector in activation space and demonstrate how applying a small additive shift to the hidden states enhances the target trait while preserving overall language modeling performance. To determine the optimal combination of feature shifts, we explore a linear weighting heuristic with grid search optimization that balances personality expression with task performance. Our approach shows promise in controllably steering personality traits at the mechanistic level while maintaining high performance on standard benchmarks.

---


### 37. [Structure-Preserving Document Translation via Multi-Stage LLM Pipeline: A Case Study in Marathi](https://arxiv.org/abs/2606.28796)

**<font color=#1a73e8>作者：</font>** Manasi Waghe, Danish Chandargi, Mohammad Aamir Rayyan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Government documents in India are predominantly issued in regional languages such as Marathi, creating substantial accessibility barriers for non-native readers, interstate administrative bodies, and policy analysts. Although recent advances in neural machine translation have improved sentence-level translation quality, existing systems largely neglect document structure, formatting integrity, and domain-specific terminology, thereby limiting their applicability to official documentation. This paper presents a structure-preserving Marathi-to-English government document translation framework capable of performing end-to-end document transformation while maintaining layout fidelity. The proposed system integrates layout-aware optical character recognition, coordinate-based text extraction, large language model based translation, and structured document reconstruction through HTML representations. By enforcing spatial alignment constraints and preserving hierarchical document elements, the framework ensures structural consistency between the source and translated documents. Experimental evaluation on real-world Marathi government PDFs demonstrates improved structural preservation, translation coherence, and terminological consistency compared to conventional text-only translation pipelines. The proposed framework contributes toward scalable multilingual accessibility solutions for e-governance and administrative document processing.

---


### 38. [Primary ICD Category Prediction using LLM-based Probing](https://arxiv.org/abs/2606.28798)

**<font color=#1a73e8>作者：</font>** Chengyuan Liu, Xinyue Zhang, Yao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective: ICD codes are central to reimbursement, research, and population health surveillance, yet automated coding systems often struggle to integrate diagnostic signals from both clinical narratives and structured electronic health record (EHR) variables. We evaluated whether frozen medical large language model (LLM) representations can serve as a shared embedding space for multimodal primary diagnosis category prediction.
Materials and Methods: We constructed a MIMIC-IV cohort of 13,645 admissions from the 10 most frequent primary ICD-10 codes, consolidated into seven categories. Structured variables were serialized into clinical narratives and combined with leakage-pruned discharge notes. Using a frozen MedFound-Llama3-8B-finetuned backbone, we extracted hidden states from five transformer layers and trained linear probes for structured-only, unstructured-only, and combined inputs, comparing against XGBoost and information-matched PLM-ICD baselines and evaluating MIMIC-III adaptation with a compact bottleneck adapter.
Results: The combined probe performed best on MIMIC-IV (87.69% strict; 91.45% medical accuracy), exceeding both single-modality probes and baselines. The structured-only probe outperformed its standard baseline by 6.19 points in medical accuracy. Diagnostic information became increasingly linearly separable in deeper layers, and a 2M-parameter adapter restored cross-dataset transfer to MIMIC-III using only 5% of target labels.
Discussion: LLM embeddings can unify structured and narrative EHR information for multimodal diagnosis prediction, supporting efficient reuse of clinical representations across modalities and datasets through a small representation-level module.
Conclusion: Multimodal probing of frozen medical LLM representations provides a practical approach for studying EHR modalities and adapting clinical representations across datasets.

---


### 39. [ViPSim: Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Models](https://arxiv.org/abs/2606.28804)

**<font color=#1a73e8>作者：</font>** Longyu Chen, Heng Li, Wei Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied World Models (EWMs) have emerged as a scalable and risk-free paradigm for advancing embodied intelligence, enabling the safety-critical evaluation of Vision-Language-Action systems. However, their reliability as evaluation benchmarks and foundational simulators is often hindered by the representation gap between low-dimensional actions and high-dimensional video synthesis. This gap results in a lack of geometric correspondence, manifesting as accumulated trajectory drift and inconsistent robot-object interactions during long-horizon rollouts. To bridge this gap, we propose ViPSim, a framework that achieves consistent long-horizon generation through the synergistic collaboration of Visual and Parameter Spaces. We define the Visual Space as a domain of explicit spatial priors, integrating pixel-aligned projections of end-effector pose, camera perspectives, depth-informed scene geometry, and robotic morphological masks to provide dense structural grounding. Concurrently, the Parameter Space serves as a domain of numerical drivers, injecting raw action sequences and camera matrices to provide precise motion guidance. By unifying these two spaces, ViPSim ensures that the generated states are simultaneously anchored by geometric boundaries and steered by numerical commands. Extensive experiments demonstrate that ViPSim is backbone-agnostic and significantly enhances trajectory consistency. Notably, our approach exhibits emergent capabilities in generating complex interactions with deformable objects (e.g., cloth folding) and maintains robust performance in out-of-distribution and cross-embodiment scenarios, providing a high-fidelity foundation for the automated evaluation and predictive control of embodied agents.

---


### 40. [Labeling Training Data for Entity Matching Using Large Language Models](https://arxiv.org/abs/2606.28823)

**<font color=#1a73e8>作者：</font>** Aaron Steiner, Christian Bizer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) achieve strong performance on entity matching without requiring task-specific training data. However, applying these models to large sets of candidate pairs remains slow and costly. In contrast, entity matchers using traditional machine learning methods or small language models (SLMs), such as RoBERTa, offer much faster inference but require task-specific training data.
This paper investigates whether the need to provide task-specific training data can be avoided by using knowledge-distillation workflows, in which an LLM serves as a teacher model to label training pairs that are subsequently used to train a smaller student model. We investigate knowledge distillation for entity matching along the following dimensions: pair-selection strategy, teacher model, label post-processing method, and student model. We evaluate the workflows using the Abt-Buy, Walmart-Amazon, WDC Products, DBLP-ACM, and DBLP-Scholar benchmarks, and compare the performance of student models trained with machine-labeled data to the performance of the same models trained using the benchmark training sets.
Our experiments show that student models trained using the machine-labeled sets perform approximately on par with models trained on the benchmark training sets, with the remaining differences in both directions staying below two F1 points. Using GPT-5.2 to label the training sets for all five benchmarks costs US\$28.31 to US\$40.88, whereas manually labeling the same training sets is estimated to require 470 hours of work. At inference time, Ditto is 41.5 to 534 times faster than directly using an LLM to perform the matching tasks.
These results indicate that current LLMs, when combined with a suitable pair-selection method, can substantially reduce or even eliminate the manual effort required to label use case-specific training data for entity matching.

---


### 41. [Fisher-Routed Mixture of Experts for Federated Class-Incremental Learning](https://arxiv.org/abs/2606.28835)

**<font color=#1a73e8>作者：</font>** Wenhao Yuan, Chenchen Lin, Jian Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) emerged as a promising distributed machine learning paradigm. However, extending FL to the class incremental learning scenarios introduces unique challenges: 1) Capacity conflict and catastrophic forgetting from the shared model overloading, 2) Heterogeneity from Non-Independent and Identically Distributed (Non-IID) data, and 3) Synchronized class misalignment. In this paper, we propose \textbf{F}isher-Routed \textbf{M}i\textbf{X}ture of Experts for \textbf{Fed}erated Class-Incremental Learning (\textsc{FedFMX}), a novel framework to address these challenges via adaptive expert specialization across clients. The crucial insight is to route each sample to an expert subset that jointly optimizes knowledge acquisition and retention. Specifically, we introduce a Fisher-Routed Expert Scoring (FRES) module to estimate expert importance via Fisher-based stability cost and gradient-based plasticity gain. Then, we design an Adaptive Expert Selection (AES) module by quantifying marginal contributions for adaptive expert subset determination. Finally, by the routing-aware regularization (RAR), we achieve load balance and efficient FL training. We theoretically prove the $\mathcal{O}(T^{-1})$ convergence rate. Extensive experiments on multiple benchmarks compared with state-of-the-art methods demonstrate the superiority of \textsc{FedFMX}.

---


### 42. [The Contagion Tensor: A Framework for Measuring Output-Distribution Coupling in Multi-Agent LLM Systems -- and Auditing the Claims It Enables](https://arxiv.org/abs/2606.28839)

**<font color=#1a73e8>作者：</font>** Zewen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Contagion Tensor, a measurement framework for quantifying how large language model (LLM) output distributions couple across modalities, agents, and time steps. From the tensor we derive the Coupling Amplification Factor (CAF), a family of ratio-based metrics sharing the form CAF = E[T_condition] / E[T_baseline], providing unitless, baseline-referenced measurement with bootstrap confidence intervals. We instantiate CAF in four variants and evaluate the strongest in a complete 2x2x2 block-orthogonal simulation design with modality-specific ablation. The ablation reveals that an apparent image-condition super-linear effect (CAF = 1.40) collapses to sub-linear (CAF = 0.87) when the image perturbation module is disabled, a shift of -0.53 with zero effect on text conditions. We supplement with real-API experiments across two model families: DeepSeek-Chat (R=30) and GPT-4o-mini (R=15, real vision). Under uniform personas, text-only communication produces CAF approx 1.0 in both models. Diverse personas drive convergence (CAF = 0.88). A within-model comparison on GPT-4o-mini reveals: C3 (text) CAF = 1.02 vs. C5 (real vision, R=30) CAF = 1.72 [1.700, 1.733], delta = +0.70, validating the simulation's super-linear image-condition prediction. Of 11 conditions, 5 have been tested on real APIs and 6 remain unverified. Our contribution is two-layered: (1) a measurement instrument that makes output-distribution coupling quantitatively falsifiable; and (2) a transferable ablation protocol that any modular multi-agent simulator can adopt to distinguish genuine coupling from design artifacts.

---


### 43. [The Heterogeneous Safety Impacts of Benign Multilingual Fine-Tuning](https://arxiv.org/abs/2606.28843)

**<font color=#1a73e8>作者：</font>** Will Hawkins, Kaivalya Rawal, Jonathan Rystrøm 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a large language model is a ubiquitous method for enhancing its capability on a specific downstream task. However, prior work has shown that this increase in capability comes with a cost: it can increase a model's tendency to respond to unsafe adversarial prompts, even when fine-tuning with non-adversarial data. We present the first comprehensive empirical study of this phenomenon in multilingual settings by fine-tuning Llama-3.2, Qwen3, and Gemma-3 models using benign data translated across nine languages. We find that safety outcomes are highly sensitive to both the choice of fine-tuning language and the evaluation language, with adversarial compliance rates increasing four-fold in some settings. Multilingual safety drift is decoupled from general capability metrics, and occurs heterogeneously across languages and models. Fine-tuning in non-English languages often induces smaller internal representational drifts than English, but these shifts lead models to default to either exaggerated compliance or refusal. As such, assessing fine-tuning impacts solely in English provides inadequate assurance for deployment. To facilitate further research into these cross-lingual safety blind spots, we release the Multilingual-Benign-Tune dataset and the SORRY-Bench-Multilingual evaluation suite.

---


### 44. [Personalizing MLLMs via Reinforced Multimodal Reference Game](https://arxiv.org/abs/2606.28845)

**<font color=#1a73e8>作者：</font>** Deepayan Das, Davide Talon, Yiming Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalizing Multimodal Large Language Models (MLLMs) aims to recognize users' unique concepts from visual data and provide personalized responses. Although prior work has shown the benefit of concept descriptions and reasoning for this task, MLLM descriptions often include information, such as state and context, that does not help and may in fact hinder the unique identification of the target concept among other visually similar items. Effective descriptions of personal concepts should instead be accurate, discriminative, and free of distracting details. To achieve such descriptions, we introduce Reinforced Reference Game (RRG), a learning framework that promotes discriminative descriptions through a novel reinforced multimodal reference game. The MLLM plays both the roles of speaker and listener in a contrastive game setting, whose goal is to effectively communicate discriminative information about a target concept. Our approach formulates a verifiable contrastive reward over hard positives (dissimilar views of the same concept) and hard negatives (visually similar but different concepts). Empirically, RRG achieves state-of-the-art across multiple tasks on three personalization benchmarks. RRG generalizes to unseen domains and outperforms existing methods based on concept descriptions and personalization-specific RL frameworks. We will release code and models in the project page.

---


### 45. [HKVLM: Faithful Reasoning Grounding by Binding Language Queries to a Frozen Detector](https://arxiv.org/abs/2606.28862)

**<font color=#1a73e8>作者：</font>** Bo Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many visual requests -- ``the object to open this bottle'', ``the person not wearing a helmet'' -- require reasoning, not just category matching. Pure open-vocabulary detectors need an explicit phrase; vision-language models (VLMs) can reason yet ``see but mis-speak'', attending to the right region but returning the wrong box or label. We argue this is a \emph{binding} failure: in coordinate-as-text VLMs localization passes through the autoregressive head, coupling it to language generation; in two-stage pipelines the model's intent is squeezed through a single class string. We present HKVLM, which removes localization from the language path. A frozen, language-aligned detector emits class-agnostic region proposals; a frozen language model encodes reasoning instructions as referential query embeddings; a lightweight \emph{alignment hook} binds queries to regions by contrastive retrieval and bipartite assignment in a shared embedding space. A perception-grounded faithfulness veto forbids naming an object that no region supports. Only the hook is trained, targeting small-data cold-start settings where monolithic VLM tuning struggles. We formalize a \emph{say-vs-see} decomposition separating localization error (SeeErr) from binding error (SayErr), and evaluate on RefCOCO/RefCOCO+/RefCOCOg and POPE. With frozen Grounding DINO and Qwen2.5-VL, training only the hook lifts grounding accuracy by $50$--$90\times$ over untrained cross-space matching; the faithfulness veto raises POPE accuracy from near-chance ($0.50$) to $0.66$--$0.76$ and reduces hallucination from ${\sim}0.99$ to $0.23$--$0.43$, with gains from $200$ expressions. Increasing proposals from $M{=}50$ to $M{=}300$ improves grounding by $19$--$24\%$ without retraining, confirming that residual error is perceptual (SeeErr) rather than binding (SayErr).

---


### 46. [On Test-Time Scaling for Vision-Language Models](https://arxiv.org/abs/2606.28864)

**<font color=#1a73e8>作者：</font>** Fawaz Sammani, Tzoulio Chamiti, Nikos Deligiannis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time scaling is a paradigm where large models use additional compute at inference to achieve better performance, without changing model weights. While it has been widely studied for Large Language Models (LLMs), its applicability to Large Vision-Language Models (LVLMs) remains less explored and analyzed, with limited analysis of whether, when, and to what extent these approaches transfer to LVLMs. In this work, we ask a simple but fundamental question: can conventional test-time scaling methods developed for LLMs be directly applied to LVLMs? We present the first comprehensive study of test-time scaling for LVLMs, spanning multiple models and model sizes, nine test-time scaling methods, and six diverse benchmarks. Our main findings is that 1) different from previous findings, small, well-performing models benefit the most from test-time scaling, enabling performance improvements of up to around 30\%, reaching large models performance, and often outperforming them, 2) LVLMs lose focus when given more compute than necessary, and 3) Visual information is encoded early in the reasoning chain, after which the chain is dominated by text-only reasoning and the contribution of image tokens drops significantly. Finally, we also provide a global and fine-grained analysis on the quality and information sufficiency of the reasoning chains produced. Overall, our findings and analysis provide practical guidance and insights into LVLMs and their deployment in research and industry.

---


### 47. [Exploring the Value of Diverse LLM Explanations in Introductory Programming](https://arxiv.org/abs/2606.28882)

**<font color=#1a73e8>作者：</font>** Seth Bernstein, Paul Denny, Juho Leinonen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown the potential to generate code explanations that surpass those of peers in quality, offering promising opportunities for computer science education. While these explanations may not yet match the depth and clarity of instructor-provided explanations, research in computational creativity highlights that the quantity and diversity of ideas can often outweigh a singular focus on quality. Inspired by this, we explore whether combining multiple diverse explanations, each emphasizing distinct aspects (e.g., function, concept, goal), can enhance students' understanding of programming exercises compared to generic explanations that do not emphasize distinct conceptual aspects. In our study 971 first-year computing students were randomly assigned either diverse or generic LLM-generated explanations for two programming exercises. Students completed multiple-choice and open-ended questions for each exercise, followed by Likert-scale questions and open-ended reflections. Our findings outline patterns in student performance and perceived cognitive load across the two explanation conditions. These findings highlight how variation in explanation emphasis may relate to learner engagement and understanding. Across participants, open-ended response accuracy was consistently about 7.7% higher when students received diverse explanations, with no difference in perceived cognitive load.

---


### 48. [PASTA: A Paraphrasing And Self-Training Approach for Knowledge Updating in LLMs](https://arxiv.org/abs/2606.28898)

**<font color=#1a73e8>作者：</font>** Takayuki Yamamoto, Daisuke Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge updating in pre-trained Large Language Models (LLMs) remains an important challenge. While continual training provides a potential avenue for knowledge updating, it continues to present substantial technical difficulties. Furthermore, LLMs often struggle with accurately answering questions about specific factual information, such as news articles - a capability limitation widely recognized in the research community. This paper proposes PASTA, a simple yet powerful framework for integrating detailed factual information from news articles as new knowledge into LLMs, with the primary goal of building specialized models that accurately answer questions about this knowledge. Our framework combines data augmentation, question-answering generation, and a novel self-learning DPO process that simultaneously enables knowledge overwriting and hallucination suppression. We provide insights into effective knowledge updating through systematic analysis of learning parameters and data configurations. In our experimental evaluation with web articles published after the base model's knowledge cutoff, PASTA achieved remarkable improvement from 0.02 to 0.82 accuracy while maintaining general language capabilities, demonstrating its effectiveness for creating domain-specialized LLMs.

---


### 49. [ExACT: Exemplar-Driven Calibrated Refinement for Training-Free Visual Grounding in Remote Sensing Images](https://arxiv.org/abs/2606.28920)

**<font color=#1a73e8>作者：</font>** Zixiao Zhang, Lingling Li, Pei He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing visual grounding (RSVG) aims to locate specific objects in high-resolution RS imagery using free-form natural language descriptions. While recent advances in multimodal large language models (MLLMs) show great potential for such open-vocabulary RSVG, their training-free adaptation is hindered by the modality gap between abstract linguistic semantics and fine-grained visual cues. In cluttered RS scenes, this gap inevitably causes severe localization drift. To bridge this gap, we propose Exemplar-driven Calibrated Refinement (ExACT), a novel training-free framework driven by a one-shot visual prompting mechanism to explicitly provide discriminative structural guidance for precise pixel-level localization. Specifically, we propose a Vision Exemplar-based Calibrator (VEC) that extracts fine-grained visual correspondences from the given exemplar to rectify the rough cross-modal priors from frozen MLLMs, effectively suppressing background artifacts and accurately outlining target boundaries. Subsequently, a Structure-Aware Refiner (SAR) employs an iterative merge-and-select clustering strategy to consolidate the calibrated priors into high-quality positive and negative geometric prompts. These prompts then guide the Segment Anything Model (SAM) to achieve precise pixel-level predictions. Extensive experiments confirm the superiority of ExACT over existing training-free and weakly-supervised methods.

---


### 50. [DLR: Zero-Inference-Cost Latent Residuals for Low-Rank Pre-Training](https://arxiv.org/abs/2606.28932)

**<font color=#1a73e8>作者：</font>** Dong Wang, Wenwu Tang, Yun Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models have driven recent progress in language and multimodal AI, yet pre-training them at scale is prohibitively expensive. Low-rank pre-training, which factorizes each weight matrix into a rank-r product to reduce both parameters and FLOPs, is a promising response but typically lags full-rank training in quality. We propose Duplicated Latent Residual (DLR), a training-only, parameter-free, foldable plug-in for low-rank pre-training. DLR augments the standard low-rank output Bz with a fixed structured residual alpha/sqrt(K) * Expand_K(z) that replicates each latent coordinate K = ceil(d_out/r) times across the output. With alpha fixed, DLR adds zero learnable parameters per layer; after training, it is absorbed into the up-projection in closed form, B* = B + alpha/sqrt(K) R^T, so deployment parameter count, FLOPs and memory match the underlying low-rank backbone exactly. Across LLaMA models from 60M to 7B parameters, DLR strengthens low-rank pre-training on C4 validation perplexity in most settings, with the clearest gains at 130M and above; folded checkpoints transfer cleanly to supervised fine-tuning on standard benchmarks.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-247](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

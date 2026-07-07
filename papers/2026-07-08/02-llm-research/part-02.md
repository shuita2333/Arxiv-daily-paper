# 🧠 大模型相关研究 | 2026年07月08日

> 本类共 **248** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-248](./part-05.md)

---

### 51. [OmniFocus: Query-Guided Modality-Balanced Token Compression for Omni-Modal Large Language Models](https://arxiv.org/abs/2607.03050)

**<font color=#1a73e8>作者：</font>** Shijie Cao, Qingyu Zhang, Boxi Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Omni modal large language models (OmniLLMs) have attracted wide attention for their ability to jointly process audio and video, but they generate large token sequences under audio-visual inputs, leading to substantial inference cost. Existing audio-visual token compression methods often rely on unimodal guidance, overlooking the temporal locality of query-relevant evidence in audio-visual inputs and implicitly assuming that the two modalities share a temporally aligned information density distribution. We propose \textbf{OmniFocus}, a training-free query-guided token compression method for OmniLLMs that performs independent importance estimation for video and audio, enabling a modality-symmetric compression design that preserves modality-specific salient evidence while maintaining audio-visual alignment, thereby mitigating the modality bias issue that can arise from unimodal-guided compression. Experiments on the Qwen2.5-Omni model family across four audio-visual benchmarks show that OmniFocus maintains strong compressed performance at low token retention ratios and outperforms existing baselines on several major benchmark scores at 25\% token retention. On DailyOmni with Qwen2.5-Omni-7B at 25\% token retention, OmniFocus maintains 59.40 accuracy while delivering up to 1.38$\times$ prefill speedup relative to the full-token baseline, highlighting a favorable practical accuracy-efficiency trade-off.

---


### 52. [LACE-SVD: Loss-Aware SVD with Cumulative Error Correction for LLM Compression](https://arxiv.org/abs/2607.03057)

**<font color=#1a73e8>作者：</font>** Zhuowen Liu, Longkun Hao, Shiyu Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid growth in the parameter scale of large language models (LLMs) has created a strong demand for efficient compression techniques. As a hardware-agnostic and highly compatible approach, low-rank compression has been widely adopted to reduce both memory footprint and computational cost. However, existing SVD-based methods are still largely driven by local reconstruction objectives, overlooking two critical limitations: rank budgets are often allocated without explicitly considering layer-wise loss sensitivity, and local approximation errors can propagate and accumulate through the residual stream, leading to amplified global deviations from the original model. To address these issues, we propose LACE-SVD, a Loss-Aware SVD framework with Cumulative Error correction for LLM compression. LACE-SVD first estimates the calibration negative-log-likelihood increase induced by candidate layer-wise compression ratios and solves a budget-constrained allocation problem to assign rank budgets. It then refines the compressed model with closed-form local updates and introduces a propagation-aware correction for residual-stream output modules, reducing layer-output discrepancy as a proxy for cumulative error propagation. Experimental results demonstrate that at a high compression ratio (0.6), the WikiText-2 PPL of our method on LLaMA-7B (32.57) is significantly better than that of Dobi-SVD (46.18).

---


### 53. [Spectral Rewiring for Exploration, Purification, and Model Merging](https://arxiv.org/abs/2607.03065)

**<font color=#1a73e8>作者：</font>** Zhilong Zhang, Hongli Yu, Huan-ang Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a standard post-training recipe for large language models, but dense full-parameter updates create two deployment-relevant bottlenecks: suppressed reasoning performance, often reflected by premature saturation of test-time scaling, and interference when consolidating multiple capabilities through multi-domain training or model merging. We show that the reasoning-effective component of these updates is largely concentrated in the base model's spectral space, motivating Subspace-Aligned Rewiring (SAR), a post-hoc editing method that retains this spectral core while removing orthogonal components. SAR therefore preserves reasoning gains and filters residual update directions that suppress performance or amplify cross-domain interference. Across several model families and scales, SAR extracts compact reasoning cores using as little as approximately 0.58% of total parameters: it preserves over 99% of post-training performance and improves high-k exploration in mathematical reasoning, and generalizes to agentic coding by improving six of seven open benchmarks on an in-house model. SAR also purifies mixed-domain training updates by releasing suppressed coding capability while maintaining math reasoning and instruction following. It further enables model merging across experts, yielding cross-domain generalization that surpasses previous merging baselines and even the best single-domain experts. Overall, SAR shows that extracting reasoning-effective updates from parameter geometry can serve as a training-free mechanism to improve reasoning and multi-domain performance.

---


### 54. [STELLA: Efficient Sensor-to-LLM Translation for On-Device Human Activity Recognition](https://arxiv.org/abs/2607.03089)

**<font color=#1a73e8>作者：</font>** Nirhoshan Sivaroopan, Albert Zomaya, Kanchana Thilakarathna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> HAR is increasingly expected to run continuously on edge devices, yet recent LLM-based methods remain hard to deploy: raw sensor prompts are long, cloud inference adds latency and privacy risk, and fine-tuned LLM pipelines turn general-purpose models into task-specific classifiers. We present STELLA, an efficient sensor-to-LLM translation framework for on-device HAR that shifts the burden from LLM adaptation to sensor tokenization. A lightweight hierarchical tokenizer compresses an entire multi-channel inertial window into a fixed set of compact latent sensor tokens, which are projected into the embedding space of a frozen pretrained LLM and combined with a natural-language prompt for label scoring. This preserves activity-relevant temporal and cross-channel structure while keeping LLM-side computation predictable across sensor configurations. STELLA also supports on-device personalization, adapting only the lightweight tokenizer on small amounts of user-specific labelled data and augmenting inference with a local retrieval context, keeping the LLM, user data, and retrieval on device. Across seven public HAR datasets and eight benchmark settings, STELLA achieves new state-of-the-art performance, improving over prior methods by up to 11.83% F1; on-device personalization yields up to a further 21.91% F1 as user data accumulates after deployment. STELLA also outperforms representative time-series tokenizers under the same LLM pipeline and achieves real-time inference under practical mobile and edge budgets, showing that efficient sensor tokenization is a practical path toward accurate, private, and personalized LLM-based HAR on edge devices.

---


### 55. [Silicon Sampling via Cross-Survey Transfer](https://arxiv.org/abs/2607.03091)

**<font color=#1a73e8>作者：</font>** Chan-Tung Ku, Chan Hsu, Pei-Cing Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Silicon sampling-using large language models (LLMs) to simulate human survey respondents-has emerged as a promising approach for augmenting traditional survey research. However, most evaluations rely on distributional comparisons rather than individual-level prediction, which risks conflating pattern matching with coherent respondent-level prediction. We propose cross-survey transfer, a more rigorous evaluation framework in which an LLM is given a respondent's answers to one set of questions and must predict their answers to entirely different questions from the same survey. Using data from the Taiwan Election and Democratization Study (TEDS) 2024, three open-weight LLMs (27B-120B parameters), and supervised machine learning baselines, we find that: (1) zero-shot LLMs achieve 52% accuracy on genuinely unseen items, closing to within 6 percentage points (pp) of a supervised random forest trained on same-population data; (2) a stable construct predictability hierarchy emerges, from 67% for partisan attitudes to 23% for sovereignty; and (3) variance collapse and safety alignment effects-two commonly cited LLM limitations-turn out to be more nuanced than previously reported, with variance collapse affecting supervised models as well and alignment effects varying dramatically across model families. These findings clarify both the promise and boundaries of silicon sampling.

---


### 56. [Stacked LoRA for Subject-Adaptive EEG Foundation Models in Motor Imagery Decoding](https://arxiv.org/abs/2607.03094)

**<font color=#1a73e8>作者：</font>** Aymen Sarhane, Fouad Lbakali, Mouad Souissi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) decoding for brain-computer interfaces (BCIs) faces a major challenge: substantial inter-subject variability limits effective cross-subject generalization. Consequently, practical systems still rely largely on subject-specific models trained from scratch and requiring individual recalibration. EEG foundation models have recently emerged as a promising alternative; however, even large pretrained models cannot simply be used as fixed feature extractors and still require additional adaptation before they can be reliably applied to downstream tasks. In this work, we address this challenge through targeted adaptation strategies. Building on recent EEG foundation models such as REVE, LaBraM, and LUNA, we examine the impact of different low-rank adaptation strategies on motor imagery classification. We propose a framework that structurally decouples subject-invariant knowledge from subject-specific neural signatures: the low-rank update at each adapted layer is split into a Global adapter, trained jointly across all subjects, and Subject-Specific adapters, each absorbing individual variability. To assess the contribution of each path, we compare three adaptation strategies: (i) subject-specific LoRA (ii) global LoRA and (iii) stacked LoRA, combining both Global and Subject Specific adapters. Experiments on BCI Competition IV-2a, PhysioNet Motor Imagery, and the clinical Zuo2025 benchmark show that Stacked LoRA effectively mitigates inter-subject variability, achieving the best accuracy in the large majority of backbone and dataset combinations. Our analysis further reveals that the optimal balance between the global and subject-specific paths depends on the target population: a shared adapter is sufficient for large, diverse cohorts, whereas subject-specific adaptation is decisive under the high inter-session variability of clinical recordings.

---


### 57. [ACPO: Adaptive Credit Policy Optimization via Fine-Grained Surrogate Entropy](https://arxiv.org/abs/2607.03126)

**<font color=#1a73e8>作者：</font>** Zijun Xie, Yuyang You, Yongzhi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has substantially improved the reasoning ability of large language models (LLMs), but sparse outcome rewards still make token-level credit assignment difficult. Existing scalable RL methods typically assign trajectory-level rewards uniformly across tokens, while recent entropy-aware approaches either rely on coarse detached heuristics or directly optimize true entropy, which can introduce non-local gradient components misaligned with sampled-token policy updates. We propose Adaptive Credit Policy Optimization (ACPO), a token-level credit assignment framework based on a mode-local surrogate entropy. ACPO asymmetrically modulates policy updates by emphasizing uncertain decisions in successful rollouts and overconfident tokens in failed rollouts. We show that the surrogate admits deterministic entropy bounds and, under modal alignment and proximal updates, preserves the policy-gradient direction to leading order. Experiments on mathematical reasoning and coding benchmarks, including AIME 2025 and HumanEvalPro, show that ACPO consistently improves over strong RL baselines such as DAPO, GTPO, and SAPO.

---


### 58. [Text as Partial Constraint: Core-Residual Alignment for Robust Vision-Language Learning](https://arxiv.org/abs/2607.03143)

**<font color=#1a73e8>作者：</font>** Chengzhen Yu, Canran Xiao, Siyuan Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language alignment powers open-vocabulary recognition, retrieval, and LVLM grounding, yet natural captions are often underspecified, making similarity brittle and overly confident under paraphrase and omitted details. We aim to learn representations whose matching is stable across caption views and whose confidence reflects how strongly text constrains an image. We propose Text as Partial Constraint (TPC), a core-residual alignment framework that treats multi-view captions as incomplete supervision. It distills a consensus semantic core as the alignment target, learns a single-view core predictor for standard inference with one query, and explicitly discourages vision-language similarity from depending on the orthogonal unsaid residual. An uncertainty-aware contrastive objective further softens alignment when caption views disagree, reducing overconfident updates under weak language constraints. Across zero-shot recognition and adversarial robustness, TPC achieves 81.42/64.05 Top-1 clean/robust accuracy on ImageNet and 76.19/52.03 on an Avg-14 transfer suite, while improving LVLM transfer with 85.16 POPE F1 and 59.57 OKVQA accuracy under an LLaVA-1.5-7B stack. These results suggest that modeling text as a partial constraint is a practical and principled route to more reliable vision-language representations under underspecified language supervision.

---


### 59. [The Role of Prompt Language and Translation-Theory-Driven Prompts in Large Language Models: A Case Study on Spanish-Chinese Journalistic Translation](https://arxiv.org/abs/2607.03160)

**<font color=#1a73e8>作者：</font>** Haohong Lai, Weijia Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines how prompt language and translation theory-driven prompt design influence the quality of Spanish-Chinese journalistic translations generated by GPT-5.2. A parallel corpus of four editorials from El Pais was translated under 48 experimental conditions (4 prompt types, 3 prompt languages, and 4 articles). Translation quality was assessed using BLEU and BERTScore-F1 for automated evaluation, alongside human evaluation based on the Multidimensional Quality Metrics (MQM) framework. Automated metrics identified the baseline prompt (BASE) as the best-performing condition, whereas human evaluation ranked the brief-oriented prompt (BRIEF) highest (MQM: 8.66 vs. 7.84), a reversal likely attributable to the single-reference constraint inherent in automated measures. Sub-error type analysis revealed that translation theory-driven prompts selectively reduced Awkward style errors, while Unidiomatic style errors persisted across conditions. Prompt language had a negligible impact under both evaluation paradigms. These results indicate that translation theory-driven prompts can yield measurable quality gains under expert evaluation of journalistic translations, although their pedagogical implications for language learners remain suggestive and require validation through user-based studies.

---


### 60. [APeB: Benchmarking Personalization Ability of Large Language Model Agents](https://arxiv.org/abs/2607.03162)

**<font color=#1a73e8>作者：</font>** Garry Yang, Zizhe Chen, Xinru Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-powered agents struggle with personalization when users issue raw, underspecified queries. In this setting, agents must infer latent intent, extract preferences from noisy interaction histories, and select among competing alternatives. Existing benchmarks rarely test this capability, as they often rely on user-refined queries or simplified histories. We introduce personalized product search (PPS), a testbed for agentic personalization under raw queries and diverse histories. We construct Agent Personalized Benchmark (APeB) from action logs, pairing underspecified intents with rich histories and user-viewed candidate items. Evaluating state-of-the-art LLMs with multi-step agent workflows, we find that models handle explicit queries well but struggle with early-stage queries requiring intent and preference discovery. Rubric analysis attributes this gap mainly to ineffective history use. A simple history-aware query-refinement pipeline, VQRA, yields consistent gains, highlighting the need for dedicated history-utilization modules in personalized agents.

---


### 61. [KARMA: Knowledge graph-based Automated Reasoning Materialization and Alignment](https://arxiv.org/abs/2607.03166)

**<font color=#1a73e8>作者：</font>** Jinkyeong Choi, Chaebin Jeong, Donghyeon Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Template-based contrastive synthesis is scalable, but its candidates often differ only in a few entity-slots while sequence-level optimization spreads supervision over mostly shared templates. We formalize this as the Resolution Mismatch Problem and propose KARMA, which enumerates schema-constrained paths over domain knowledge graphs and verbalizes them into slot-aligned contrastive candidates. Slot-Parallel Alignment (SPA) then applies a decoupled slot-level objective to route preference supervision to discriminative entity-slots, with slot-aware masked attention serving as an optional packed-evaluation implementation. Across biomedical, computer-science, and chemistry benchmarks, KARMA outperforms base LLM and same-data SFT baselines, and compares favorably with sequence and token-level preference methods.

---


### 62. [BVS: Bayesian Visual Search with Multimodal Large Language Model for Fine-grained Perception](https://arxiv.org/abs/2607.03184)

**<font color=#1a73e8>作者：</font>** Geng Li, Yuxin Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) demonstrate impressive general capabilities, they struggle with fine-grained perception in ultra-high-resolution (UHR) images, particularly for tiny objects in cluttered scenes. Existing methods face a dilemma: they either rely on inefficient prior-free scanning, or depend on static prior-driven heuristics that lack posterior correction to rectify initial model biases. To address this, we propose BVS (Bayesian Visual Search), a framework that formulates perception as a global optimization problem over a continuous spatial-scale manifold. Specifically, BVS bridges prior guidance with posterior correction: it utilizes an early-stop attention rollout of MLLM to construct reasoning-aware priors, while employing a scale-aware non-stationary kernel and GP-UCB to dynamically rectify noise and recover missing information in the prior through iterative local observations. We provide theoretical guarantees via sub-linear regret bounds, and extensive experiments demonstrate that BVS significantly outperforms state-of-the-art baselines with a superior trade-off between accuracy and efficiency.

---


### 63. [Reduced-Order Models: The Mother of World Models](https://arxiv.org/abs/2607.03198)

**<font color=#1a73e8>作者：</font>** Rajat Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models -- compressed latent representations of an environment that support action-conditioned prediction and planning -- are typically presented as a product of modern self-supervised learning. This paper argues that the functional anatomy of a world model was independently developed, deployed, and formally analyzed decades earlier in the model-order-reduction (MOR) and control literature, under different names and for a different purpose: the real-time operation of physical systems. We trace the anatomy across three communities. Low-dimensional models of turbulence built on proper orthogonal decomposition (POD) supplied latent dynamics learned from data of a chaotic environment; eigenface methods in early computer vision supplied the encoder-decoder half, including a primitive runtime validity check; and measurement-based POD frameworks for facility thermal control assembled the complete loop -- POD coefficients as latent state, parametric dependence on actuator setpoints as action conditioning, modal reconstruction as decoding, and, critically, a priori analytical error bounds as a verification layer that certified when the model's predictions could be trusted in closed loop. We then examine what each tradition possesses that the other lacks: MOR contributes verification, physical grounding, and extreme data efficiency; learned world models contribute nonlinear representation, transferability, and horizon. We argue that the outstanding obstacle to deploying world models in systems that cannot fail -- power, thermal, process control -- is not predictive fidelity but verifiability, and we outline a research agenda for physics-grounded, verifiable world models that unifies the two lineages.

---


### 64. [Fast 3D Foundation Model Initialized Gaussian Splatting](https://arxiv.org/abs/2607.03209)

**<font color=#1a73e8>作者：</font>** Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces a fast method for high-quality 3D Gaussian Splatting (3DGS) reconstruction without traditional Structure-from-Motion (SfM). The proposed approach leverages 3D Foundation Models (3DFMs) for camera pose and point-cloud initialization, then jointly optimizes both camera poses and Gaussian primitives using a depth-guided loss function. This enables fast convergence even from rough initialization with as few as 50-60 input views. To further improve reconstruction quality in sparse-view scenarios, an MLP-based pose refinement module is introduced alongside depth-guided supervision from the foundation model. Extensive experiments on Mip-NeRF 360, Tanks and Temples, and RobustNeRF demonstrate that the proposed method achieves competitive reconstruction quality (23.61 dB PSNR, 0.19 LPIPS) while reducing training time to approximately three minutes per scene. The proposed method produces ready-to-use 3DGS models at a fraction of the time required by existing pipelines, making it suitable for near real-time applications in robotics, VR, and autonomous navigation.

---


### 65. [OpenGlass: A Sensing-Computing Split Architecture for Local MLLM-Driven Real-Time Visual Assistance](https://arxiv.org/abs/2607.03213)

**<font color=#1a73e8>作者：</font>** Mengzhang Li, Yuan Yao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present OpenGlass, an open-source, privacy-oriented, local-first system for low-latency multimodal visual assistance, with a primary focus on blind and low-vision users. Cloud MLLM assistants offer strong visual understanding, but often require uploading first-person visual data and can suffer multi-second network delays; wearable glasses are ideal for sensing, but cannot host large models under tight compute and power budgets. OpenGlass addresses this gap with a sensing-computing split: an ESP32-based glasses-side unit captures visual context, while a nearby consumer-grade device performs local MLLM inference and local speech output, reducing cloud reliance and keeping raw egocentric visual data on user-controlled devices by default. We evaluate response quality, query-ready-to-audio latency, safety-aware abstention, and auditable logs. Under real ESP32 Wi-Fi capture, OpenGlass reaches 993 ms median user-to-audio latency with resized payloads and 1625 ms with raw 1280 x 720 payloads; 97.5% and 93.3% of trials fall below 2 s, respectively. OpenGlass is a user-initiated visual-assistance reference platform for obstacle/hazard awareness, sign/object queries, and image-quality self-checking, rather than a certified navigation aid. We release source code, hardware instructions, prompts, evaluation data, and logs.

---


### 66. [Organizational Memory for Agentic Business Process Execution](https://arxiv.org/abs/2607.03228)

**<font color=#1a73e8>作者：</font>** Lukas Kirchdorfer, Adrian Rebmann, Christian Warmuth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents offer new opportunities for automating business process execution beyond the limits of rule-based systems. However, general-purpose LLMs lack the organization-specific knowledge required for reliable execution, which is typically fragmented across human-oriented artifacts such as policies, process models, and standard operating procedures. While such knowledge can technically be encoded in individual prompts or agent-specific retrieval setups, this approach does not scale in enterprises, as it gives rise to knowledge silos and rule duplicates, and makes consistent updates and learning across agents difficult. We argue that this calls for an organizational memory for agentic business process execution: a shared, governed, and agent-consumable reference layer of evolving organization-specific procedural knowledge about how work should be executed. We derive requirements for such a memory, propose an architecture for its curation and consumption, and demonstrate its effectiveness in a proof-of-concept based on a procurement scenario.

---


### 67. [TACG: Trajectory-Aware Commit Gating for Diffusion Language Model Decoding](https://arxiv.org/abs/2607.03236)

**<font color=#1a73e8>作者：</font>** Chengcheng Wang, Tingzhang Luo, Wenhao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLLMs) generate text by iteratively denoising masked positions, exposing a trajectory of predictive distributions rather than a single instantaneous belief. Most existing decoders ignore this trajectory and commit tokens from the current snapshot alone, conflating confidence with commitment readiness: a transient top-1 peak under incomplete context can be locked in, while candidates with consistent cross-step support are delayed. We propose Trajectory-Aware Commit Gating (TACG), a training-free gate-level decoder that anchors token identities to the base posterior and uses trajectory-aware signals only to decide whether the current proposal is ready to commit. TACG combines Temporal Implicit Logits Guidance (TILG), which keeps an exponential moving average of past logits as a self-reference and contrasts the current logits against this reference in natural-parameter space, with a History Gate (HG) that enforces short-term proposal persistence before commitment. Together with a capped extra-promotion budget, these components yield a stability-constrained commit rule without auxiliary networks or extra forward passes. We evaluate TACG on LLaDA, Dream, and LLaDA2-Mini across code (HumanEval, MBPP) and math (GSM8K, MATH500) benchmarks; it typically improves or preserves accuracy while reducing denoising steps and increasing tokens per forward (TPF). The code is publicly available at this https URL.

---


### 68. [PhenoNEST: A Neuro-Symbolic Framework for Ontology-Aware Multimodal Plant Phenotyping and Trait Discovery](https://arxiv.org/abs/2607.03245)

**<font color=#1a73e8>作者：</font>** Jayant Ghadge, Soumyashree Kar, Surya S. Durbha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-throughput plant phenotyping generates valuable data that often remains trapped in unstructured text and isolated RGB images. To bridge this semantic gap, we propose a framework for constructing a multimodal granular Knowledge Graph (KG) to monitor genotype-phenotype interactions across time and experiments. In this work, we focus on wheat Triticum aestivum as a representative target crop to validate our methodology across complex canopy environments. Our pipeline first distills noisy field notes to extract entities and relations, dynamically constructing the KG by converting unique instances into hierarchical class entities via RDF-typing. These graph nodes are then aligned with standardized ontologies (PO, RO, WTO) using PlantDeBERTa. To visually ground the constructed graph, a Vision-Language Model paired with a wheat-segmentation ViT generates attention-based softmaps, linking specific KG entities directly to image pixels. We introduce a central observation node Plant_Obs_Id to connect these multimodal subgraphs temporally. Evaluated on 500 curated WisWheat samples using Pointing Game accuracy, Visual Word Sense Disambiguation (VWSD), and rank-based metrics, our neuro-symbolic approach successfully maps complex field observations to a structured graph. This enables automated field note auditing, temporal stress monitoring, and precise spatial trait localization for wheat breeders.

---


### 69. [Unbiased Alignment for Large Language Models with Noisy Preferences](https://arxiv.org/abs/2607.03248)

**<font color=#1a73e8>作者：</font>** Jialiang Wang, Xianming Liu, Xiong Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The alignment of large language models with human preferences is commonly achieved through Reinforcement Learning from Human Feedback or Direct Preference Optimization. However, these methods are vulnerable to the significant noise prevalent in real-world preference datasets. To address this critical issue, we present a theoretical framework for unbiased alignment, introducing the Unbiased Reward Model (URM) loss and the Unbiased Direct Preference Optimization (UDPO) loss. By mathematically correcting the distortion induced by preference noise, our novel objectives enable unbiased model training directly from noisy datasets, without requiring clean ground-truth supervision. We provide rigorous theoretical analyses demonstrating that our methods are noise-tolerant, parameter downward compatible, and classification-calibrated. Comprehensive experiments across diverse datasets demonstrate that our approaches outperform state-of-the-art baselines. Code available at: this https URL.

---


### 70. [OmniLayout: A Schematic-Coupled Multimodal Benchmark for Constraint-Aware Geometric Reasoning in PCB Layout](https://arxiv.org/abs/2607.03261)

**<font color=#1a73e8>作者：</font>** Taiting Lu, Kaiyuan Lin, Mingjia Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent large language models (LLMs) have demonstrated remarkable progress in 3D spatial reasoning, spatial grounding, and fine-grained geometric understanding. However, their ability to reason about densely packed object placement under strict spatial and functional constraints remains largely unexplored, despite being a fundamental challenge in practical electronic design automation (EDA) workflows. To bridge this gap, we introduce OmniLayout, the first benchmark designed to evaluate LLMs on printed-circuit-board (PCB) layout placement reasoning under real-world geometric, routing, and connectivity constraints. OmniLayout contains 1,681 industrial-grade schematic-coupled PCB layouts and includes four tasks: (1) geometric reasoning for IC physical placement, with 77.24K placement instances constrained within PCB board boundaries; (2) routability-aware placement reasoning, generating physically valid component placements; (3) electrical functionality, preserving schematic-specified connectivity and electronic functional correctness; and (4) tool-augmented agentic reasoning for invoking external tools to accomplish tasks (1)-(3). Our results reveal substantial limitations of current LLMs in PCB layout placement, including weak geometric reasoning, poor routability optimization, and inconsistent preservation of electrical functionality.

---


### 71. [From Global to Local: Efficient Regional Weather Downscaling with Global Weather Foundation Model](https://arxiv.org/abs/2607.03279)

**<font color=#1a73e8>作者：</font>** Wiktor Kamzela, Jakub Kubiak, Adam Dobosz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate regional weather prediction requires resolving fine-scale structure while remaining consistent with global dynamics. Traditional limited area models rely on computationally expensive simulations, while many learning-based approaches frame the problem as super-resolution, overlooking statistical and physical mismatches across scales. We propose a foundation-model-driven downscaling framework that learns regional refinements of global forecasts by augmenting a pretrained weather model backbone with lightweight, multi-scale prediction heads operating directly in its latent space. Despite being trained on substantially coarser inputs, the pretrained backbone supports regional adaptation at resolutions corresponding to a two-order-of-magnitude increase in grid-cell resolution, without the need for retraining. The proposed approach uses regional numerical simulations as training targets and is evaluated not only against gridded datasets but also against ground-based weather station observations, enabling analysis of systematic biases between global reanalysis, regional simulations, and in-situ weather station observations. Our experiments show improved accuracy in comparison to NWP on most of the metrics at the fraction of computational cost. Moreover, we observe that building on a latent space of globally pre-trained weather foundation model offers better downscaling capabilities than the standard image-based super-resolution approaches.

---


### 72. [A harmonised dataset for Earth system foundation models](https://arxiv.org/abs/2607.03298)

**<font color=#1a73e8>作者：</font>** Carlos Rodriguez-Pardo, Massimo Tavoni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models for Earth systems have so far been trained primarily on physical climate and weather data, with limited representation of the human systems that both drive and respond to environmental change. The lack of a unified global training resource that combines climate, land, ocean, cryosphere, infrastructure, hazards, and socioeconomic data on a common grid hinders progress toward truly multimodal Earth system foundation models. We present WorldTensor, a harmonised global dataset that aligns hundreds of environmental and socioeconomic variables to a standardised 0.25$^\circ$ spatial grid and annual temporal framework. WorldTensor integrates reanalysis products, remote sensing, emissions inventories, land use reconstructions, hydrological observations, infrastructure and hazard datasets, and socioeconomic indicators within a single representation designed for machine learning workflows. To build the dataset, we regridded inputs across heterogeneous native resolutions and projections, rasterised point and vector datasets into spatially meaningful gridded fields, and reconciled temporal coverages ranging from daily observations to sparse multiyear socioeconomic snapshots. All outputs are distributed as NetCDF files with standardised coordinates, variable metadata, and a common CF metadata convention. WorldTensor provides a reproducible resource for training and evaluating foundation models that learn coupled dynamics across environmental and human systems at planetary scale.

---


### 73. [Reflective Dialogue or Prompt Refinement? Effects of Tutor Scaffolding on Students' Independent LLM Use for Programming](https://arxiv.org/abs/2607.03303)

**<font color=#1a73e8>作者：</font>** Jerome Brender, Laila El-Hamamsy, Kim Uittenhove 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) can provide personalized support in learning, several studies have raised concerns regarding their use in education. Importantly, learning depends on how students engage with LLMs. This study examined how two types of LLM-based tutors shape students' prompting practices, learning, and subsequent LLM-use: a Socratic-Guidance (SG) tutor, which structures interaction through dialogic questioning, and a Prompt-Refinement (PR) tutor that guides the formulation of effective prompts. We conducted a two-phase study in a graduate-level mobile robotics course: 66 students used either the SG or PR tutor during a 6-week intervention, followed by 52 students using an unconstrained LLM during a 3-week course project. Results show that while the SG- and PR tutors led to similar task performance and prompting patterns during guided use, they differ in learning outcomes and later LLM-use. SG-students, relative to PR-student, achieved higher learning gains in later sessions, and were more likely to adopt understanding-driven prompting strategies, which are predictive of higher understanding, when using an unconstrained LLM. Although learners perceived the SG tutor as less efficient, the findings suggest that Socratic guidance supports the development of students' capacity to learn with LLMs over time, highlighting its importance for LLM tutor design.

---


### 74. [From Judgments to Issues: Structured Extraction of Legal Reasoning with Citation-Hallucination Control](https://arxiv.org/abs/2607.03325)

**<font color=#1a73e8>作者：</font>** Giovanni Piccioli, Alessia Fidelangeli, Piera Santin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present an automated pipeline that decomposes Italian tax-court judgments into individual legal issues and extracts, for each issue, a structured XML representation grounded in the IRAC framework and the legal syllogism. The pipeline targets a corpus of approximately $330{,}000$ first- and second-instance decisions of the Italian tax courts and is built around a capable yet cost-efficient general-purpose model (DeepSeek V3), a choice driven by the need to process several hundred thousand documents at a sustainable cost. To address the well-documented unreliability of large language models on legal citations, we couple the extraction step with an automatic hallucination-detection filter that compares the references produced by the model with those identified in the judgment text by a dedicated parser (Linkoln), normalised to standard identifiers (URN-NIR, ECLI, CELEX). We validate the pipeline on $50$ judgments annotated by two PhDs in tax law, computing inter-annotator agreement and LLM-vs-expert agreement on both issue extraction and legal citations, together with a stand-alone evaluation of the hallucination filter. To the best of our knowledge, this is the first issue-level, expert-validated structured extraction pipeline with hallucination control for Italian tax-court decisions, and it provides a concrete starting point for downstream applications such as issue-level retrieval, citation-network analysis, and the construction of large-scale datasets of legal reasoning.

---


### 75. [PedestrianDiffusion: Multimodal Generative Denoising and Dense State Estimation for Inertial Navigation](https://arxiv.org/abs/2607.03349)

**<font color=#1a73e8>作者：</font>** I-Hao Lu, Dongsoo Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The accuracy of consumer-grade inertial navigation is bottlenecked by the stochastic noise of Micro-Electro-Mechanical Systems (MEMS). Traditional deterministic neural architectures often succumb to ``estimation jittering,'' sacrificing high-frequency kinematic fidelity for numerical stability. We propose PedestrianDiffusion, a multimodal spectral-domain generative framework reformulating dense 6D state estimation as a continuous conditional denoising process. By operating in the frequency domain, our formulation bounds the spectral covariance, acting as a mathematical preconditioner to stabilize the reverse diffusion trajectory. Furthermore, we introduce a zero-shot semantic conditioning mechanism leveraging vision-language embeddings as categorical priors to generalize across heterogeneous sensor noise profiles. To address the computational intractability of generative tracking, we deploy a single-step deterministic probability flow ODE solver ($T=1$). This yields high-capacity asynchronous batch trajectory refinement, establishing the viability of generative architectures for asynchronous batch trajectory refinement on edge hardware. Extensive evaluations on the OxIOD, RIDI, RoNIN, and TLIO benchmarks demonstrate that PedestrianDiffusion achieves state-of-the-art performance, exhibiting unprecedented robustness to impulse perturbations and coupled 6D kinematic drift. This work provides a rigorous algorithmic blueprint for next-generation Neural Inertial Measurement Units (N-IMUs).

---


### 76. [Pathways of Visual Information Flow in Vision-Language Models](https://arxiv.org/abs/2607.03358)

**<font color=#1a73e8>作者：</font>** Israfel Salazar, Stella Frank, Dan Oneata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study how visual information is routed in vision-language models (VLMs). Using causal patching on controlled synthetic and natural datasets, we find that models rely on two distinct pathways to solve visual tasks: A direct pathway, where visual information is retained in image token representations and read out by the final token at later layers, and a text-mediated pathway, where visual information is first transferred to the query tokens and then read out by the final token. Across three visual tasks, we show that pathway selection is task-dependent, and that data distribution and prompt design can also modulate which pathway is used to solve the image-based query. Moreover, using attention knockouts and corrupted-input patching, we find that these pathways are flexible, under certain interventions, models can rely on the text-mediated pathway as a fallback when the usual pathway is ablated. This behavior unifies findings in prior work and shows that ablation-based interventions can reveal what models could do rather than what they normally do. Together, our results provide a mechanistic characterization of visual information flow in VLMs and highlight the flexibility of their internal mechanisms under intervention.

---


### 77. [Brand-as-Memory: Vision-Language Models Encode Causal, Mechanistically Localizable Credibility Priors for News Sources](https://arxiv.org/abs/2607.03365)

**<font color=#1a73e8>作者：</font>** Chih-Ting Liao, Xin Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly read news and web content as images, where the publisher's identity is visually present. We show that VLMs carry a strong source-credibility prior keyed on outlet identity, and study it along three axes. (i) Cross-model benchmark. We introduce CueTrust, a cross-model diagnostic that measures which surface source cue overrides an article's content evidence via a Source-Override Index (SOI). Across seven VLMs and five cues, the vulnerability profile is model- and scale-dependent, and the override is outlet-identity-specific and encoding-invariant, firing from the masthead name, the logo image, or the bare domain, but not from a named author, in-text authority, or page layout (clean negative controls). (ii) Mechanistic account. For the brand cue, we give a full mechanistic account: swapping only the masthead moves credibility across an approximately 11 log-odds range that tracks professional ratings (rho = 0.88 with Media Bias/Fact Check). The prior is dual-coded (name and logo), strengthens with scale, is causally formed at layers 19-21, carried by interpretable seed-stable sparse-autoencoder features, and recurs at the same relative locus in a second model family. It overrides content (about 1.8x) as a signal-magnitude effect within a shared pathway, not a privileged route. Steering the localized direction selectively reduces the override (41% reduction) and generalizes to held-out outlets, confirming the prior is causally used, not merely decodable. Deployed VLMs may thus defer to source identity over the evidence in front of them, a reliability failure we can measure across models, localize, and causally probe. We release the stimulus suite and CueTrust.

---


### 78. [Spectral Signatures of Large Language Models](https://arxiv.org/abs/2607.03377)

**<font color=#1a73e8>作者：</font>** Zhuoying Zhang, Ishan V. Prasad, Yuanzhe Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapidly growing repository of publicly available large language models (LLMs) presents significant challenges for systematic management and quantification at scale, such as model lineage tracing, licensing, and evaluation. However, task-specific benchmarks are insufficient for this setting, as LLMs differ widely in architectures, scales, and training procedures. To address this challenge, we adopt spectral shape-based metrics for managing and quantifying LLMs based on Heavy-Tailed Self-Regularization theory. Our approach uses the shape information of the weight empirical spectral density as a compact spectral signature of each model. This signature captures intrinsic properties of pretrained models and remains robust during post-training, making it suitable for model-level analysis. In addition, this metric is data-free, computationally-efficient, and scale-invariant, enabling large-scale analysis in practice. Moreover, we curate a large and diverse model corpus consisting of major open-source LLM families, and use it to systematically benchmark spectral and non-spectral metrics across models and downstream tasks. We show that our spectral signature supports the tracking of the model lineage, the unsupervised clustering of similar models, and the quantification of the model performance. Overall, the proposed spectral signature provides a meaningful proxy for broad performance trends across LLMs, enabling efficient organization, comparison, and analysis of large model collections.

---


### 79. [When Aggregate Alignment Misleads: Auditing Policy Repair Without Per-State Expert Actions](https://arxiv.org/abs/2607.03386)

**<font color=#1a73e8>作者：</font>** Peiying Zhu, Sidi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems are increasingly used to edit, refine, and repair decision policies, but evaluating these edits is difficult when per-state expert action labels are unavailable. We study this problem in a hotel-pricing simulator where an agentic policy editor receives only region-level diagnostic feedback: summaries of how its price distribution differs from a benchmark policy across time, inventory, and market regions. The editor cannot observe benchmark actions, benchmark source code, reward numbers, or held-out outcomes, and may only propose constrained edits to a target-action table. On 5,000 held-out episodes, a multi-restart LLM editor reaches RevPAR 108.47 (95% CI 107.61 - 109.34), close to the benchmark policy's 108.75 (107.81 - 109.68), with paired gap (LLM minus benchmark) -0.276 and 95% CI [-0.692, 0.146]. A cheap diagnostic projection already recovers much of the revenue (107.90), so the LLM editor's distinctive gain is not raw revenue lift alone: it also reduces episode composition distance from 1.153 to 0.609. This is the strongest non-benchmark repair result. This profile is not explained by restart search alone: non-semantic proposers with up to 2,500 evaluations fall 8.77 - 14.57 RevPAR points short. Nor is it explained by plausible prompt format: a shuffled-diagnostic control breaks region-error correspondence and falls to RevPAR 94.30. The match is genuine but partial. A tree editor achieves stronger pooled alignment, 0.214 versus 0.266, and stronger reference-state D1, 0.328 versus 1.197, yet revenue falls to 98.91. These results show that agentic policy repair should be evaluated by whether diagnostic feedback becomes reliable closed-loop outcome, not by a single behavioral distance.

---


### 80. [The Classics at SemEval-2026 Task 3: Combining Transformer Models and LLM-Generated Annotations for Dimensional Aspect-Based Sentiment Analysis](https://arxiv.org/abs/2607.03414)

**<font color=#1a73e8>作者：</font>** Rafif Alshawi, Amit Raj, Aleksey Kudelya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents an approach to the SemEval-2026 Task 3: Dimensional Aspect-Based Sentiment Analysis. We investigate methods for moving beyond traditional categorical sentiment (e.g., positive or negative) to predict fine-grained, real-valued scores for sentiment "valence" (positivity) and "arousal" (intensity). We participate in two subtasks: predicting these scores for given aspects (Subtask 1) and extracting full sets of sentiment details, including aspects, categories, and opinions alongside their scores (Subtask 3). Our approach for the regression task involves a weighted ensemble of transformer-based encoder models. For the Russian language, we further enhance the input by using a large language model (LLM) to generate synthetic sentiment descriptions. For the extraction task, we fine-tune a decoder LLM to perform structured prediction, allowing the system to identify sentiment elements and estimate their numerical scores simultaneously.

---


### 81. [Amortising Bayesian Experimental Design for Sequential Information Gathering in LLMs](https://arxiv.org/abs/2607.03426)

**<font color=#1a73e8>作者：</font>** Jakob Hartmann, James Harvey, Jhonathan Navott 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit strong reasoning and world-knowledge capabilities, yet often struggle to gather information effectively across the multi-turn interactions required in sequential decision-making settings. We introduce Amortised Sequential Information Gathering (ASIG), a fine-tuning approach that amortises Bayesian Experimental Design (BED) into LLM policies via a multi-turn extension of Group Relative Policy Optimisation with an Expected Information Gain reward. Evaluated on the 20 Questions task, ASIG more than doubles the success rate of the 7B base model and reduces inference cost by over $25\times$ relative to BED-LLM, a competitive inference-time baseline. Applied to MediQ, a medical diagnosis benchmark unseen during training, ASIG improves information-seeking performance at the 7B scale, suggesting that the learned strategies can transfer out of distribution. Our findings show that amortising BED into LLM policies provides an effective and computationally efficient approach to sequential information gathering.

---


### 82. [No Time Like the Present: Agentic Test-Time Training for LLM Agents](https://arxiv.org/abs/2607.03441)

**<font color=#1a73e8>作者：</font>** Yanbo Wang, Jinhua Hao, Yuze Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents often degrade over long episodes: as trajectories grow, they revisit explored states, repeat failed actions, and lose strategies that previously worked. Test-time training (TTT) offers a way to adapt model weights to the evolving task state, but existing LLM TTT methods largely adapt once to a fixed input. We study continuous TTT in multi-turn agent episodes, where each update changes the policy that generates later training text. This creates a self-training loop that helps when new trajectory information appears, but can amplify drift when the agent gets stuck and repeatedly trains on similar text. We find that update-text repetition distinguishes these regimes and introduce Agentic Test-Time Training (aTTT), a token-level reweighting method that downweights the loss on tokens appearing in repeated $n$-grams from prior updates while leaving novel tokens fully weighted. To run such updates inside live episodes, we build a concurrent serving system using vLLM's runtime LoRA API, limiting overhead to 1.9$\times$ the no-TTT cost. aTTT improves success by up to 5.0 points on ALFWorld and 4.9 points on SWE-bench Lite. The gains concentrate where models already have task competence but drift over long trajectories, suggesting that aTTT mainly preserves existing competence rather than teaching new abilities.

---


### 83. [Best-of-Better-$N$: Generating Pre-Aligned Responses with In-Context Learning](https://arxiv.org/abs/2607.03453)

**<font color=#1a73e8>作者：</font>** Eric Lei, Hsiang Hsu, Chun-Fu Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time alignment methods, such as Best-of-$N$, offer a flexible alternative to training-based alignment by using reward models to select high-quality responses generated by a reference LLM. However, the efficacy of these methods is inherently limited by the response quality: if the reference LLM assigns negligible probability to high-reward responses, no selection strategy will succeed in finding aligned outputs. In this work, we propose Best-of-Better-$N$ (BoBN), an in context learning-based generation framework to address this challenge. Our method utilizes retrieval from high-reward examples relevant to the input query and task. Crucially, we introduce a restyling step where retrieved responses are rewritten by the reference LLM to align with the target task's format and style. These restyled examples are used in-context to shift the sampling distribution toward the high-reward region. We analytically characterize how in-context learning shifts the output distribution of pretrained transformers toward the high-reward region, resulting in provable benefits on the target task. We then evaluate BoBN on safety alignment and mathematical reasoning benchmarks across several reference LLMs. BoBN's higher-quality responses enable better performance to be achieved when the number of responses $N$ is fixed, and smaller $N$ required to achieve a target performance.

---


### 84. [WorldBagel: Uncovering the Power of Unified Multimodal Models for Vision-Language-Action-World Modeling](https://arxiv.org/abs/2607.03461)

**<font color=#1a73e8>作者：</font>** Zelin Zhao, Min Shi, Bo Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models aim to capture environment dynamics in ways that support perception, reasoning, and action, and have recently become a central direction in Vision-Language-Action-World (VLAW) modeling. Meanwhile, unified vision-language models have demonstrated strong multimodal generation capabilities, yet their potential as world models remains underexplored. In this work, we introduce \texttt{WorldBagel}, a unified VLAW framework built on BAGEL, a modern multimodal unified model, and use it to systematically investigate the role of unification in world modeling. Across multi-task robotic manipulation and cross-domain experiments, \texttt{WorldBagel} consistently outperforms task-specific alternatives and learns action representations that are more structured and semantically aligned with visual and linguistic context. Experiments on LIBERO, Language Table, and Franka show that unification is not only an architectural convenience, but also a key factor in learning effective VLAW models, leading to consistent empirical gains and deeper insights into multimodal world modeling. Code and model checkpoints will be released upon acceptance.

---


### 85. [Demonstrating Generalization Failures via Mixtures of Conditional Policies](https://arxiv.org/abs/2607.03478)

**<font color=#1a73e8>作者：</font>** Jou Barzdukas, Jack Peck, Julian Schulz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training of frontier language models is conducted on curated task suites, and inevitably leaves a distribution shift between training and deployment environments. This exposes developers to generalization failures, which are relatively poorly understood. To better understand such generalization failures, we believe the community should construct clean demonstrations under simplified conditions. To facilitate this, we propose a simple and flexible way to construct language models which fail to generalize in controllable ways when subsequently trained with Reinforcement Learning (RL) on a given distribution of training tasks. Our construction uses Supervised Fine-Tuning on a dataset of a mixture of transcripts corresponding to a collection of 'conditional policies', which can each independently be assigned certain behaviors on each different task distribution, to obtain a model that is then well approximated as a 'mixture of conditional policies.' We observe that RL training then selects for policies that obtain the highest reward on the training distribution. This can produce striking behaviors: in a controlled setting with two distributions containing identical questions prepended with two different 'trigger strings', RL training on either distribution actively degrades performance on the other to zero, even though the underlying task is identical. We also use our construction to illustrate two novel ways in which generalization may fail in future language models, corresponding to distribution shifts of task coverage and temporal context respectively. While our construction is deliberately simple and may not closely resemble 'natural' generalization failures, the resulting 'model organisms' are of interest for alignment stress-testing and generalization science, and can be used as existence proofs that training success and generalization can come apart in structured ways.

---


### 86. [Aligning Language Models with Selective Prediction](https://arxiv.org/abs/2607.03528)

**<font color=#1a73e8>作者：</font>** Gaoxiang Luo, Yifan Wu, Sinian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as critical decision-making components in high-stakes real-world AI systems, rendering LLM reliability a foremost practical concern. In this paper, we focus on enhancing LLM reliability through selective prediction (SP), a strategy that allows an LLM to only predict for inputs where it is likely to be correct (i.e., coverage) and hence reduce the error rate (i.e., risk) on that portion of inputs -- flagging the remaining inputs for future human discretion. In other words, SP improves LLM reliability by balancing the risk-coverage trade-off and enabling seamless human-AI collaboration. To integrate SP into LLMs, we focus on the LLM post-training alignment stage and propose to align LLMs with SP performance metrics, in contrast with existing LLM alignment methods that focus primarily on correctness or calibration metrics. Specifically, we propose a novel alignment framework, Reinforcement Learning for Selection Reward (RLSR), which targets the area under the risk-coverage curve (AURC) -- a popular SP performance metric -- as its alignment objective. RLSR achieves substantially better risk-coverage trade-off compared to multiple alignment baselines on both in-domain and out-of-domain tasks.

---


### 87. [MentalThink: Shaping Thoughts in Mental SVG World](https://arxiv.org/abs/2607.03530)

**<font color=#1a73e8>作者：</font>** Kangheng Lin, Jisheng Yin, Dingming Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce MentalThink, a visual-symbolic reasoning paradigm that equips Multimodal LLMs (MLLMs) with an executable mechanism for "mental" visualization. The core of MentalThink is a think-with-SVG pipeline, where the model learns to generate, render, and interpret scalable vector graphics (SVG) code as an intermediate visual representation for multi-turn reasoning. By creating structured vector sketches, the model can externalize spatial hypotheses, inspect them through deterministic rendering, and reason within a constrained geometric space, effectively mimicking the human process of mental imagery. We instantiate this paradigm through a two-stage training framework, combining Supervised Fine-Tuning (SFT) for SVG syntactic alignment with multi-turn Reinforcement Learning (RL) to encourage iterative inspection, revision, and refinement of intermediate visual hypotheses. Extensive evaluations demonstrate that MentalThink achieves superior performance on spatial understanding and reasoning benchmarks (e.g., 55.1% on VSIBench, 76.0% on MindCube), showing that executable vector graphics provide a verifiable visual workspace for dynamic perspective taking, visual reflection, and compositional scene construction.

---


### 88. [Modular Foundation Models for Time-Series Perception in Digital Twins](https://arxiv.org/abs/2607.03585)

**<font color=#1a73e8>作者：</font>** Quang Hung Pham, Ryad Zemouri, Martin Gagnon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Engineering Digital Twins and Prognostics and Health Management (PHM) systems rely on robust perception modules to extract actionable information from heterogeneous and non-stationary time-series data. However, most existing approaches remain task-specific, data-hungry, and difficult to integrate into scalable monitoring and decision-making pipelines. Moreover, purely data-driven models often lack robustness and transferability across varying operating conditions. To address these challenges, this paper proposes a modular foundation model for time-series perception based on a collection of pretrained representation encoders. The framework leverages self-supervised learning on heterogeneous datasets to learn transferable and task-agnostic representations, which can be reused across multiple PHM tasks. A gating mechanism is introduced to dynamically select relevant encoders for a given target dataset, enabling conditional computation and adaptive model composition. The selected representations are projected into a shared latent space and aggregated using a Transformer-based self-attention module that explicitly models cross-encoder interactions. The resulting architecture supports multiple downstream tasks, including imputation, long-term forecasting, and few-shot learning, through lightweight task-specific heads, while keeping pretrained encoders frozen during adaptation. Extensive ablation studies demonstrate the complementary roles of self-supervised pretraining, encoder selection, representation alignment, and adaptive aggregation. Experimental results on the ETT benchmark show competitive performance across tasks, while a real-world industrial case study on virtual sensing for hydro-generator rotor temperature highlights the practical relevance of the approach.

---


### 89. [Responsibility Distribution Estimation in Ego-View Accident Videos with Multimodal Large Language Models](https://arxiv.org/abs/2607.03591)

**<font color=#1a73e8>作者：</font>** Ryosei Tamura, Andrew Shin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent studies on multimodal traffic accident understanding have mainly relied on infrastructure-camera footage, satellite imagery, or structured crash records. However, such data sources are costly to deploy and maintain at large scale, and they cannot objectively capture what the driver was actually able to observe before the accident. In contrast, ego-view accident videos directly represent the driver's visual perspective, making them suitable for reasoning about avoidability and driver responsibility. In this paper, we introduce responsibility distribution estimation for ego-view traffic accident videos, a new task in which a model predicts the percentage of responsibility assigned to each involved agent. We construct an LLM-assisted responsibility annotation pipeline and fine-tune multimodal large language models under multiple input settings, including raw frames, segmentation-enhanced input, and textual descriptions. Experimental results establish a strong initial benchmark, demonstrating that multimodal LLMs can effectively perform this nuanced, constraint-based reasoning task. Our findings suggest that ego-centric accident videos provide a promising foundation for socially and legally meaningful multimodal reasoning beyond conventional accident classification and explanation tasks.

---


### 90. [Token-Based Affordance Grounding with Large Vision-Language Models](https://arxiv.org/abs/2607.03595)

**<font color=#1a73e8>作者：</font>** Seung Il Lee, Qinqian Lei, Daguang Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Affordance grounding aims to localize image regions that support a specific action, serving as a core capability for physical intelligence and embodied perception. Previous studies have primarily relied on weakly supervised learning with action labels from exocentric images. However, these methods often struggle with visually ambiguous exocentric images containing co-occurring actions; moreover, they fail to distinguish semantically similar actions because existing methods typically rely on brief action phrases that lack rich semantic details for action-specific localization. Although large vision-language models (LVLMs) encode rich action semantics and their action-conditioned textual outputs implicitly contain spatial cues, they do not directly provide action-specific spatial localization. To address these problems, we propose TokAG, a zero-shot affordance grounding framework that exploits the token-level semantic-spatial signals in LVLMs to localize action-relevant regions without external supervision. We observe that attention maps associated with different LVLM output tokens vary significantly, with many attending to irrelevant regions such as the background. Thus, we introduce a spatial-aware token-selection mechanism to systematically evaluate each output token and select the one whose attention maps exhibit dominant activation over the target object, instead of relying on arbitrary attention maps. By extracting these object-focused attention maps, we transform the LVLM's implicit semantic signals into zero-shot affordance heatmaps. Our zero-shot framework consistently outperforms prior weakly supervised approaches across multiple benchmarks, improving NSS by 10.7% on the unseen split of AGD20K and by 29.7% on HICO-IIF. The code and models will be made publicly available.

---


### 91. [A Step Towards Robust Unsupervised Domain Adaptation via Fine-Tuning and Reinforcement Learning](https://arxiv.org/abs/2607.03600)

**<font color=#1a73e8>作者：</font>** Sushant Dagaji Desale, Rahul Mishra, Ashutosh Kumar Sinha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial robustness in Unsupervised Domain Adaptation (UDA) remains a significant challenge due to noisy pseudo labels and inherent distributional shifts between the clean source and adversarially perturbed target domains. Existing approaches often fail to achieve an optimal trade-off between robustness and accuracy, as pseudo-labels generated by domain-adapted models tend to introduce classification errors under adversarial attacks. In this work, we propose \textbf{SFT+RL}, a two-stage robust UDA framework that integrates Supervised Fine Tuning (SFT) and Reinforcement Learning (RL) on top of CLIP's pre-trained visual encoder. In the SFT stage, we adversarially fine-tune a linear classifier using PGD-based perturbations over the labelled source domain while partially unfreezing CLIP's projection layer. It allows adaptation to adversarial noise while preserving CLIP's rich semantic priors. We introduce a confidence-guided pseudo-labeling strategy in the RL stage to annotate unlabeled target samples progressively. Pseudo labels are filtered using a decaying confidence threshold to balance quality and coverage, and the model is trained on a composite dataset formed by combining clean source samples with high-confidence target samples. Adversarial training is applied to mixed batches of clean and adversarial examples to enhance cross-domain robustness. Comprehensive evaluations on three benchmark datasets OfficeHome~\cite{tomm-ude}, PACS~\cite{pacs}, and VisDA~\cite{visda} demonstrate the effectiveness of our approach. Notably, \textbf{SFT+RL} achieves average improvements of \textbf{10.2\%} in clean accuracy and \textbf{15.8\%} in adversarial robustness across all three datasets, outperforming existing state-of-the-art methods.

---


### 92. [A Vision Based System for Guided and Collaborative Reconstruction of Fragmented Documents](https://arxiv.org/abs/2607.03621)

**<font color=#1a73e8>作者：</font>** Oliver Krumpek, Diana Leo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the development and evaluation of a collaborative system for real-time reconstruction of fragmented paper documents in the context of cultural heritage preservation. The developed system includes a collaborative robot, or cobot, that can fully manage the positioning of paper fragments using a specially designed vacuum-based suction attachment. This attachment enables gentle and precise positioning, ensuring the preservation of fragile materials. With this device, we are able to achieve a positioning repeatability of 0.57mm for fragments of 8cm^2. The system offers users the flexibility to choose between manual positioning, with visual guidance, or fully automated positioning performed by the cobot. To further improve the reconstruction process, AI methods for image interpretation, specifically for segmentation and positioning tasks, were applied and evaluated for their applicability to template-based reconstruction of damaged paper fragments. Our investigation provides critical insights into the performance of different local feature matching methods under different document types, taking into account rotation, scale robustness, and the degree of damage to the fragments. With a focus on the reconstruction of damaged and optically altered archival material, SE2-LoFTR, a detector-free local feature matching method, was chosen as the preferred method for the system due to its robust performance in our experiments.

---


### 93. [RADIO1D: Elastic Representations for Condensed Vision Modeling](https://arxiv.org/abs/2607.03624)

**<font color=#1a73e8>作者：</font>** Greg Heinrich, Mike Ranzinger, Collin McCarthy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper challenges the assumption that vision-language models (VLMs) require fixed patch-based 2D vision features. Analyzing fine-tuned vision encoders, we find that representations become increasingly abstract and less spatially coherent during VLM training. Notably, models trained with image-text alignment (such as SigLIP2) develop a small number of specialized tokens that effectively summarize global image content. Building on this, we introduce RADIO1D, which compresses images into a compact, variable-length 1D token sequence using multi-teacher knowledge distillation and an autoencoder design. The resulting representations exhibit strong hierarchical summarization, enabling accurate scene understanding - even with a single token - and support improved composition-aware image retrieval. In VLMs, RADIO1D provides flexible accuracy-efficiency tradeoffs through adjustable token counts, delivering competitive performance on diverse multimodal benchmarks with lower computational overhead and better accuracy.

---


### 94. [Moonstone: A Multimodal Foundation Model and Benchmark for Lunar Remote Sensing](https://arxiv.org/abs/2607.03644)

**<font color=#1a73e8>作者：</font>** Ayush Prasad, Swarnalee Mazumder  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decades of orbital missions have produced multi-modal remote sensing data for the Moon, spanning optical imagery, spectroscopy, thermal emission, radar, gravity, and elemental composition. Yet these datasets remain fragmented across archives, and no benchmark exists for evaluating machine learning on lunar data. We introduce Moonstone, the first multi-modal foundation model benchmark for lunar remote sensing. Our contributions are: (1) a 28-channel, 128 pixels-per-degree (~237 m) global lunar pretraining dataset from seven instrument families across five missions, (2) MG-MAE, a modality-grouped masked autoencoder with per-group convolutional tokenizers, a shared Vision Transformer encoder, attention masking for missing modalities, coverage-adaptive masking for heterogeneous spatial coverage, and spectral continuity regularization for physically plausible reconstructions, and (3) a benchmark of six downstream tasks covering classification, regression, and segmentation. MG-MAE pretrained features outperform scratch baselines on all tasks and surpass both ImageNet-pretrained and vanilla MAE baselines by large margins. Data and code are available at this https URL and this https URL .

---


### 95. [Do Medical Vision Language Models Actually See? A Counterfactual Grounding Framework and Hard-Negative Contrastive Training for Visually-Reliant Medical VLMs](https://arxiv.org/abs/2607.03647)

**<font color=#1a73e8>作者：</font>** Anas Zafar, Leema Krishna Murali, Siddhant Bharadwaj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision language models (VLMs) report strong accuracy on medical question-answering, yet it remains unclear whether they reason from visual evidence or exploit textual shortcuts. We introduce a counterfactual evaluation framework that decouples visual and textual contributions by substituting input images with controlled surrogates blank, pixel-shuffled, image-absent, and CLIP-retrieved hard negatives and derive a suite of grounding metrics including the Visual Reliance Score (VRS) and Visual Hallucination Rate (VHR). We further introduce CORAL (COntrastive Retrieval-Augmented Learning), a 7B-parameter LoRA fine-tune of Qwen2.5-VL-7B trained with a Contrastive Grounding Objective (CGO) that penalises answer invariance under hard-negative image swaps. On a paired controlled evaluation across four closed-form medical VQA benchmarks (PathVQA, PMC-VQA, SLAKE, VQA-RAD; n=400 total), CORAL improves macro accuracy by +6.7 pp (P(Delta>0)=0.988) and reduces VHR by 8.0 pp (P<0.001) over the matched Qwen2.5-VL-7B base; neither MedVLThinker RL variant achieves a significant gain on either metric. Cross-domain diagnostics further reveal that image substitution costs only <=6.5 pp on medical benchmarks versus 48-61 pp on general-domain tasks, situating the grounding gap that CGO targets. We discuss evaluation limitations openly including train/eval benchmark overlap and underpowered secondary metrics and release our framework, training code, and model weights to support reproducible grounding audits of medical VLMs.

---


### 96. [LLM-Guided Transportation Hub Capacity Planning with Textual Business Inputs](https://arxiv.org/abs/2607.03651)

**<font color=#1a73e8>作者：</font>** Xiaoyue Liu, Zheng Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While traditional hub capacity planning models optimize effectively for quantitative inputs, they often fail to digest qualitative business context. We propose a novel framework where a large language model (LLM) agent iteratively proposes hub capacity decisions guided by natural-language business context descriptions. The key mechanism is a chain-of-thought reasoning protocol: the LLM constructs a structured decision table that maps each contextual item to specific capacity adjustments based on the implied direction and magnitude of changes. The new capacity decision is then validated through a feedback loop with an optimization model, which provides routing-based performance metrics to guide the agent's selection. On a real-world 13-hub freight network in the southeastern US, our framework achieves a 2.8% optimality gap relative to the hidden ground-truth, a significant improvement over the 11.0% gap produced by the traditional optimization model without textual business inputs. This demonstrates that LLMs can serve as a contextual bridge, integrating qualitative business insights into Operations Research workflows.

---


### 97. [ViPo-MLLM: Visual-Pose Multimodal LLM for Gloss-Free Sign Language Translation](https://arxiv.org/abs/2607.03657)

**<font color=#1a73e8>作者：</font>** Ahmed Abul Hasanaath, Bicheng Xu, Mir Rayat Imtiaz Hossain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gloss-free Sign Language Translation (SLT) translates sign language videos into spoken-language sentences without gloss annotations, avoiding costly labeling but requiring fine-grained modeling of hands, body, and facial cues. Existing methods often use single-modality or weakly fused features, limiting performance. We propose ViPo-MLLM, a framework that integrates spatio-temporal RGB and human pose features. Dedicated encoders model intra-modal dynamics and cross-modal attention captures long-range dependencies. The fused representation is conditioned with a structured prompt and processed by an LLM trained with contrastive and language modeling objectives. The proposed model was evaluated on the PHOENIX14T and CSL-Daily datasets and achieved new state-of-the-art results on both datasets. Moreover, the ViPo-MLLM model attained competitive performance compared to gloss-based recognition approaches, confirming the effectiveness of the proposed pose cues and cross-modal attention mechanisms.

---


### 98. [From Geometric Labels to Semantic Understanding of Indoor Building Components Using Multimodal Large Language Models](https://arxiv.org/abs/2607.03661)

**<font color=#1a73e8>作者：</font>** Shuju Jing, Chao Yin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud-based understanding has become an important enabler for facility operation and maintenance involving indoor building components. However, existing methods output only discrete labels without explaining component functions or natural language interactions. This paper proposes Building-MLLM, a point cloud-centered multimodal large language model (MLLM) for indoor components, which models point clouds and instructions to generate responses across Simple Recognition, Complex Captioning, and Multi-Engineering Question Answering tasks. Building-MLLM addresses semantic concentration through four domain-specific mechanisms: Point Information Enhancer for task-relevant semantics, Geometry-Preserving Regularization preventing geometric erosion, fixed textual prefix for domain stabilization, and multi-dimensional LoRA balancing recognition with reasoning. A multi-constraint progressive instruction-generation engine is developed to compile a synthetic point cloud-text dataset with 4198 objects, 37,782 instruction-following pairs, and 47 categories. Experiments show that Building-MLLM achieves 88.00%, 65.10%, and 68.14% on the three task types, respectively, demonstrating superior indoor component language understanding and providing initial generalizability in transfer inference on other real-world datasets.

---


### 99. [Social Networks of LLM Agents](https://arxiv.org/abs/2607.03695)

**<font color=#1a73e8>作者：</font>** Kaixuan Liu, Guojun Xiong, Weinan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly deployed in interacting populations, raising the question of what such populations come to believe collectively. Whether a population aggregates genuine knowledge or collapses into a false consensus directly affects how much such systems can be trusted. Classical social-network models assume that the network itself determines how beliefs combine. This assumption breaks down for LLM agents, whose limited attention takes in only part of what they are exposed to, so these models overstate how much information a population actually pools and cannot tell genuine consensus from herding. We introduce SNLA, a framework that models how much each agent actually influences others, rather than merely how the network connects them. This influence depends on each agent's position in the network and on how sharply attention focuses. Theoretically, we show on a tractable proxy that narrow attention causes herding, where the effective sample size stays bounded regardless of population size, while wide attention recovers wisdom-of-crowds behavior only when the exposure graph is undirected and degree-regular. Empirically, a controlled testbed validates these predictions directly, and the herding-wisdom transition reproduces on operator-controlled variants of three multi-agent LLM benchmarks.

---


### 100. [Agent Reinforcement Learning via Pivotal-Aware Self-Feedback Retry](https://arxiv.org/abs/2607.03702)

**<font color=#1a73e8>作者：</font>** Weiyang Guo, Zesheng Shi, Longhui Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have shown strong decision-making capabilities in long-horizon interactive tasks, yet they still struggle to effectively leverage failed trajectories: full retries incur high interaction costs, while experience retrieval tends to dilute critical experience signals. To address this, we propose PivoARL, a self-feedback retry framework for experience exploitation in LLM agents. PivoARL identifies the pivotal erroneous turn through structured reflection and performs local retry only from the corresponding pivotal state, thereby reusing the correct prefix and reducing redundant interactions. From an information-gain perspective, we further show that pivotal retry concentrates useful experience signals near the error boundary, mitigating the signal dilution caused by state-agnostic experience utilization. Based on this insight, we design a pivotal-aware credit assignment mechanism that rewards correct prefixes while isolating erroneous suffixes, and optimize reflection quality through implicit reflection returns. We conduct a systematic evaluation on 4 agent tasks and 7 search-based QA benchmarks. Results show that PivoARL achieves significant improvements on Pass@2/3 across all tasks, with an average gain of about 11.5\% over MetaRL. Moreover, benefiting from contrastive preference signals induced by pivotal turns, PivoARL also consistently improves Pass@1 on over 80\% of the tasks. On Minesweeper environment, PivoARL improves over GiGPO by more than 45\% and reduces interaction turns by about 42\% on average compared with full-retry methods. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-248](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

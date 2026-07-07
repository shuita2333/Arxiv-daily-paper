# 🧠 大模型相关研究 | 2026年07月08日

> 本类共 **248** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-248](./part-05.md)

---

### 101. [Optimizing Large Language Models for Causality Assessment in Pharmacovigilance: Developing a Performance Metric as Objective for Bayesian Hyperparameter Optimization](https://arxiv.org/abs/2607.03704)

**<font color=#1a73e8>作者：</font>** Nicole Sonne Heckmann, Arnault-Quentin Vermillet, Søren Norlin Mølgaard 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Growing individual case safety report (ICSR) volumes have intensified demand for scalable automated causality assessment. Large Language Models (LLMs) show promise, yet performance on clinically demanding tasks remains suboptimal and inference-time hyperparameter optimization has not been investigated. Objective: To develop a Gaussian Process (GP)-compatible optimization objective and investigate whether temperature optimization improves LLM-expert agreement on Naranjo causality assessment of FAERS ICSRs. Methods: Expert causality assessments were performed on 723 stratified FAERS cases. OpenAI's GPT-5.2 was evaluated using chain-of-thought (CoT) prompting. Four composite metrics were developed: Weighted Cosine Similarity (WCS), Information-Weighted Agreement Score (IWAS), Entropy-Weighted Agreement and Cosine Similarity Score (EWACS), and Consensus-Weighted Cosine Similarity (CWCS) and Bayesian optimization using a GP surrogate with Probability of Improvement (PoI) acquisition was applied across temperature [0, 2]. Results: GPT-5.2 outperformed prior biomedical LLMs at baseline (T = 0), achieving 74.1% agreement on question 5 and 65.4% on question 10 of Naranjo algorithm. Entropy analysis identified these as the sole informative optimization targets. Temperature showed no systematic population-level effect (\b{eta} = 0.002, p = 0.959). EWACS-guided Bayesian optimization improved causality classification agreement from 45.0% to 72.0% (+27 pp), with the largest gain in Doubtful cases (+42.9 pp). Conclusion: EWACS was identified as the optimal GP-compatible metric. The absence of a universal temperature optimum indicates LLM performance is driven primarily by ICSR content, yet case-specific temperature selection produced meaningful improvements, supporting temperature optimization for LLM-assisted pharmacovigilance.

---


### 102. [Leveraging Pathology Co-occurrence for Test-Time Adaptation in Chest X-Ray Diagnosis](https://arxiv.org/abs/2607.03715)

**<font color=#1a73e8>作者：</font>** Woojin Jeong, Yujin Choi, Dongbin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical imaging models often degrade when deployed at new clinical sites due to differences in imaging equipment, protocols, and patient populations. Test-time adaptation (TTA) addresses this by updating a pretrained model using only unlabeled target data, without access to source data. However, existing TTA methods were designed for single-label classification on natural image benchmarks, minimizing entropy uniformly across all samples without considering label dependencies. This overlooks a key property of multi-label medical imaging: pathologies do not occur independently but exhibit structured co-occurrence patterns. In this work, we propose Co-occurrence Weighted Adaptation (CoWA), which leverages disease co-occurrence patterns as a reliability signal for adaptation. CoWA estimates label co-occurrence structure from model predictions and downweights samples that deviate from expected patterns, enabling adaptation to rely more on consistent predictions while reducing the impact of noisy ones. We evaluate CoWA on chest X-ray benchmarks under domain shifts and demonstrate consistent improvements over established baselines.

---


### 103. [CoGen3D: An Agentic Human-AI Co-Design Pipeline for 3D Asset Generation for Virtual Reality](https://arxiv.org/abs/2607.03731)

**<font color=#1a73e8>作者：</font>** Weiwei Jiang, Wanyu He, Zheyu Tan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creating 3D assets for virtual reality requires modeling expertise, which restricts the authorship of immersive experiences. Existing generative AI tools rely on unconstrained, command-driven prompting, lacking the conversational scaffolding needed for users to articulate their intent and validate designs prior to rendering. To address this, we introduce CoGen3D, an agentic human-AI co-design pipeline that proactively guides users through conversational intent elicitation, a concept image confirmation, and image-to-3D generation that directly deploys to immersive scenes. We evaluated this system through a user study (N=120) across six affectively diverse immersive scenes, observing 60 Design group participants who co-created 3D assets for the scenes, and 60 Validation group participants who experienced the scenes with generated assets. Our findings show that co-designed assets are associated with higher scene engagement and shifted affective responses, while participants generally preferred concept images over the final 3D assets, with no increased leniency toward degradation in their own creations. Analysis of the human-AI conversations further shows that target environments shape users' conversational patterns. Our results suggest that our staged, intent-based co-design can democratize virtual reality authoring and shift immersive content creation from technical execution toward collaborative spatial design.

---


### 104. [Attending to Multimodal Generation One Token at a Time](https://arxiv.org/abs/2607.03738)

**<font color=#1a73e8>作者：</font>** Varun Gupta, Vineet Gandhi, Makarand Tapaswi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) generate responses autoregressively, integrating visual and linguistic information in an evolving context. Prior work on interpretability has focused on individual layers and circuits (where), leaving the token-level dynamics of multimodal computation during generation (when) underexplored. We address this gap and study attention shifts as per semantic role; tracking model attention to image, text, instruction, and previously generated tokens, One Token at a Time (OTaT). We introduce multimodal tasks that require explicit switching between visual and textual context within a single response. Across two mainstream model families and four open-weight MLLMs of varying sizes, we establish consistent patterns: attention to image peaks at tokens requiring image-derived information, instruction tokens are revisited during task transitions, and attention to previously generated tokens increases as the generation progresses. Causal attention blocking interventions validate the functional role of these trends. We profile model behavior under disrupted attention and observe responses falling back to language priors, or exhibiting cross-modal leakage, denial, or recovery. Finally, informed of the attention dynamics through our novel analysis, we propose a simple test-time intervention to boost attention to the relevant modality at the right time, significantly improving multimodal task performance.

---


### 105. [GeoSAM-Lite: A Lightweight Foundation Model for Onboard Remote Sensing Segmentation](https://arxiv.org/abs/2607.03760)

**<font color=#1a73e8>作者：</font>** Yongcong Wang, Jie Zhang, Rui Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The deployment of large-scale foundation models like Segment Anything Model (SAM) on resource-constrained Earth observation platforms is hindered by prohibitive computational costs and the domain shift between natural and remote sensing imagery. To address these challenges, we propose \textit{Geo}spatial \textit{S}egment \textit{A}nything \textit{M}odel-Lite (GeoSAM-Lite), a lightweight, prompt-free segmentation framework designed for efficient onboard remote sensing segmentation. GeoSAM-Lite incorporates two core innovations: (1) Geospatial-Domain Initialization (Geo-Init), a domain-aware pre-training strategy that distills geospatial priors from a specialized teacher to bridge the domain gap; and (2) Feature Fusion Layers (FFL), which recalibrate spatial features and restore high-frequency boundary cues to overcome the capacity bottlenecks of lightweight backbones. Experiments across representative datasets, with a primary focus on cloud scenarios to evaluate performance under extreme scale variations and complex boundaries, demonstrate that GeoSAM-Lite achieves competitive accuracy while reducing parameters by 92.8\% compared to the heavyweight RSAM-Seg. By establishing a superior Pareto frontier between efficiency and fidelity, GeoSAM-Lite offers a practical solution for real-time segmentation on edge devices.

---


### 106. [Punching Above Their Weight: Classification-Head Fine-Tuning of Tiny Language Models (TLMs) for Verifiable Multiple-Choice Tasks](https://arxiv.org/abs/2607.03801)

**<font color=#1a73e8>作者：</font>** Bhavesh Sood, Jaromir Savelka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We define Tiny Language Models (TLMs) as models below roughly 3B parameters that fit on mainstream consumer devices. We study how to adapt them for and use them on verifiable multiple-choice tasks. We compare three LoRA-based fine-tuning paradigms (label generation, gold only, and our discriminative classification head) on a unified setup across several Qwen3 models from 0.6B to 8B and five benchmarks: HellaSwag, WinoGrande, PIQA, SciQ and ARC-C. Classification-head fine-tuning reliably outperforms label generation (+2-3%) at the 0.6B and 1.7B scales. Further, TLMs fine-tuned using the discriminative method are competitive to zero-/few-shot GPT-3 (175B), PaLM (540B) and GPT-4. The performance we report for Qwen3-0.6B and Qwen3-1.7B are SOTA on HellaSwag, WinoGrande, and PIQA.

---


### 107. [Stable Global Weighting of Flow Mixtures using Simplex Exponential Moving Average](https://arxiv.org/abs/2607.03809)

**<font color=#1a73e8>作者：</font>** Benjamin Wiriyapong, Oktay Karakus, Can Eyupoglu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Normalising flows provide a powerful variational family for approximate inference, yet individual architectures often fail to generalise across heterogeneous posterior geometries. We revisit mixture-based flow formulations and introduce \emph{AMF\mbox{-}VI\mbox{-}sEMA}, a two-stage framework featuring a \emph{stable global weighting} mechanism based on a \emph{Simplex Exponential Moving Average} (sEMA) update. In Stage~1, a heterogeneous set of experts (\textsc{RealNVP}, \textsc{MAF}, \textsc{RBIG}) are trained independently to specialise in distinct structural regimes. In Stage~2, expert parameters are frozen and global mixture weights are learned through a temperature-controlled softmax of average log-likelihoods, followed by a smooth EMA update on the probability simplex. This design produces a tractable, data-agnostic gating mechanism (without per-sample gating or gradient backpropagation through weights) that adaptively reallocates capacity while avoiding component collapse. We evaluate the framework on ten posterior benchmarks: six canonical 2D synthetic families (Banana, X-Shaped, Bimodal, Multimodal, Two-moons, Rings) and four real/low-dimensional Bayesian targets (BLR, BPR, Weibull, Real-GMM2), with stronger baselines (\textsc{NICE}, \textsc{ResFlow}, and EM-Mixing). Comprehensive evaluation covers NLL, KL divergence, Wasserstein-2 distance, and MMD, together with diagnostics of mixture dynamics, hyperparameter sensitivity, and cross-seed robustness. Empirically, \emph{AMF\mbox{-}VI\mbox{-}sEMA} achieves consistent NLL improvements over its predecessor \emph{AMF\mbox{-}VI} and avoids the catastrophic transport failures of single-flow baselines, while maintaining stable weight trajectories ($N_{\mathrm{eff}}{>}1.4$ on all datasets) with minimal computational overhead.

---


### 108. [TestMate: Test-Time Domain Adaptation Aided by Lightweight Vision Foundation Model](https://arxiv.org/abs/2607.03810)

**<font color=#1a73e8>作者：</font>** Dimitrios Fotiou, Vasileios Mygdalis, Ioannis Pitas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-Time Domain Adaptation (TTDA) aims to adapt Deep Neural Networks to distribution shifts using only streaming, unlabeled test data in real time. Current methods for semantic segmentation tasks suffer from critical limitations. Entropy minimization techniques require costly backpropagation, risking catastrophic forgetting and producing noisy segmentation boundaries. Memory-bank methods, while backpropagation-free, exhibit slow adaptation, requiring numerous samples to converge and struggle to handle continuous domain shifts. We introduce TestMate, a novel, real-time, and backpropagation-free TTDA framework that overcomes these issues. TestMate leverages generalization capability of a lightweight Visual Foundation Model to guide the adaptation. We use a zero-shot instance segmentation YOLOv8-seg based model to generate unlabeled mask proposals for objects and their parts at multiple scales in real time. These proposals are fused with the primary model via a heuristic, size-ordered competitive scheme, where small, high-confidence regions dominate and refine predictions in surrounding larger, less certain areas. This paremeter-free mechanism enables immediate adaptation from the first frame, inherently avoids catastrophic forgetting and effectively preserves fine object details and boundaries, even for small objects. TestMate can be used as a standalone, efficient refinement module or seamlessly integrated into existing TTDA methods to significantly boost their performance. We demonstrate state-of-the-art results across two benchmark datasets, proving TestMate's effectiveness in three distinct adaptation tasks: TTDA, Source-Free Domain Adaptation (SFDA), and online-TTDA. Code is available.

---


### 109. [Global Logic and Local Search: Dual-Stream Multimodal In-Context Learning for Verifiable Industrial Anomaly Detection](https://arxiv.org/abs/2607.03817)

**<font color=#1a73e8>作者：</font>** Runzhi Deng, Yundi Hu, Yiming Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) show strong few-shot generalization, but industrial anomaly detection remains difficult because defects are small, input resolution is limited, and textual standards are not always grounded in visual evidence. Recent optimization-based methods improve alignment through fine-tuning, but they often require many defective samples, which are unavailable in early deployment. We present Global Logic and Local Search (GLLS), a training-free framework for reference-guided multimodal in-context verification. GLLS uses a Part-Aware Visual-Logical Atlas to organize normal references and structured specifications in the inference context. It combines a Global & Logic Stream, where SAM 3 extracts partially checkable visual facts, with a Fine-Grained & Actions Stream, where MCTS selects local evidence crops under a fixed budget. Experiments on MMAD-QA and additional anomaly detection datasets show consistent gains over matched and general-purpose baselines, while keeping the final diagnostic decision traceable to explicit visual evidence throughout the inspection trace.

---


### 110. [Beyond Static Rules: Automated Discovery of Latent Vulnerabilities in Text-to-SQL](https://arxiv.org/abs/2607.03833)

**<font color=#1a73e8>作者：</font>** Hanqing Wang, Yongdong Chi, Jian Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have achieved remarkable success in Text-to-SQL tasks, their deployment in real-world environments is hindered by latent reliability issues. Identifying these latent weaknesses is critical for building trustworthy database interfaces, yet current diagnostic approaches rely heavily on static, expert-defined rules, which lack the capability for systematic and automated exploration. To bridge this gap, we propose SAGE (Systematic Automated Guided Exploration), a novel framework designed to autonomously uncover latent failure patterns in LLM-based Text-to-SQL generation. Specifically, SAGE generates vulnerability hypotheses for given samples and references a continuously evolving Vulnerability Codex to design targeted perturbations, thereby iteratively verifying and documenting potential defects. Extensive experiments on state-of-the-art open-source LLMs demonstrate that SAGE uncovers a substantial number of failure cases, highlighting the significant fragility of current models. Furthermore, our analysis reveals that the Vulnerability Codex exhibits strong cross-model transferability, indicating that the discovered patterns represent generalized structural weaknesses. Finally, we explore SAGE's potential for remediation. Although preliminary, lightweight fine-tuning on the generated samples yields promising improvements, suggesting a scalable pathway for closing the reliability loop in future work.

---


### 111. [Rethinking Scientific Discovery in an Agentic Era](https://arxiv.org/abs/2607.03863)

**<font color=#1a73e8>作者：</font>** Yining Zheng, Yuxin Wang, Jiahao Lu 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence has advanced scientific discovery, but most AI4Science systems remain fragmented tools that rely on humans to coordinate problem formulation, literature grounding, model use, simulation, validation, and knowledge reuse. This paper presents \textbf{SCION (Scientific Collaborative Innovation with Agentic Organizational Nexus)}, an agentic scientific operating system that acts as an \textbf{organizational nexus}. Through a Science Agent serving as a \textbf{Meta-Harness}, SCION connects scientific tasks, tools, agents, artifacts, and memory, transforming research into an executable, auditable, and reusable operational process. At its core is the \textbf{Research Execution Plan (REP)}, which compiles high-level scientific intent into staged objectives, dependencies, verification checkpoints, tool requirements, expected artifacts, and fallback conditions. SCION further integrates hierarchical multi-agent execution, profile-driven specialization, selective context construction, governed delegation, and layered epistemic memory to support long-horizon scientific work. We formulate discovery under SCION as \textbf{Target-conditioned Inverse Search} and extend it to hidden-target settings through batch active search under finite experimental budgets. Applications in materials analysis, molecule design, and protein or antibody screening, together with experiments on scientific reading, idea generation, molecule generation, and antibody screening, show that SCION outperforms existing autonomous research-agent baselines, especially in decomposition, verification, refinement, and memory reuse. Overall, SCION shifts AI from isolated tools toward a coordinated operational layer for traceable and reusable scientific innovation.

---


### 112. [Evaluating LLM Uncertainty in Long-Form Generation Using Deterministic Ground Truth](https://arxiv.org/abs/2607.03870)

**<font color=#1a73e8>作者：</font>** Ido Amit, Ido Galil, Ran El-Yaniv  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLMs generate increasingly long outputs, effective uncertainty estimation must identify errors at fine-grained levels rather than discard entire responses. While such methods exist, evaluating uncertainty at any resolution (token to an entire generation) is challenging and highly sensitive to label imperfections, making zero-noise benchmarks essential; yet, long-form generation benchmarks tend to rely on fallible labels rather than deterministic ground truth. We introduce Single-answer Atomic Long-form Target (SALT), a benchmark of six procedurally generated tasks with single deterministic long textual ground truths, enabling unit-level evaluation of correctness, calibration, and ranking without external judges. Equipped with SALT, our analysis of 50+ LLMs reveals key insights: We identify which confidence functions dominate each uncertainty aspect and show that confidence ranking largely breaks at atomic resolution, even when clearer separability emerges at coarser line-level units. SALT further enables controlled atom-level interventions throughout generation, revealing two separable drivers of future errors: propagation from corrupted prefixes, dominated by global context correctness, and bounded degradation from increasing answer-context length. Finally, we demonstrate that reasoning, via Chain-of-Thought prompting or internalized through training, introduces a trade-off, improving accuracy while degrading confidence ranking. These findings directly impact risk-critical applications requiring reliable error identification and mitigation.

---


### 113. [AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative Decoding Framework with Multi-Policy Orchestration for CPU-Constrained LLM Inference](https://arxiv.org/abs/2607.03876)

**<font color=#1a73e8>作者：</font>** Sadra Saremi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rise of small quantized GGUF-based language models and their increasing use for on-device inference tasks, we have seen the growing need for an approach capable of reliably delivering these models at scale even under severe memory bandwidth constraints such as those imposed by pure CPU implementations. Fixed-depth speculative decoding has emerged as one promising technique, but in practice, it often leads to performance degradation due to either bandwidth saturation, instability, or even catastrophic resource exhaustion resulting in system failure. To overcome this problem, we introduce AdaptiveSD, a fully runtime-adaptive speculative decoding framework aimed at ensuring robust, reliable execution across the spectrum of model types and workloads. Our solution consists of four tightly-coupled components working together in a continuous feedback loop: a Runtime Monitoring Engine tracking multiple signals relevant to ongoing computation, an Adaptive Draft Controller enforcing an eleven rule policy hierarchy prioritizing system resource preservation over raw draft count, a Dynamic Policy Engine employing a suite of heuristic and reinforcement learning techniques to dynamically modify policies depending upon workload behavior, and finally, a KV Cache Coordination Layer managing cache states with fine-grained control through INT8 shadow buffers and position aware evictions. While conventional approaches focus solely on maximizing throughput, we instead assess the effectiveness of our approach based on several key metrics including wasted drafted compute and inter-token latency dispersion alongside standard measures of speculative efficiency.

---


### 114. [Consistent but Miscalibrated: Evaluating LLM Limitations for Risk Communication in Natural Language](https://arxiv.org/abs/2607.03882)

**<font color=#1a73e8>作者：</font>** Diego Cerda-Mardini, Sarath Chandar, Sreenath Madathil  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly deployed as post-hoc explainers of AI-generated outputs, yet it remains unclear whether they can reliably communicate probabilistic information in natural language. For this role to be viable, models must produce identical verbal descriptions for identical inputs, and select descriptions that accurately reflect the magnitude of the underlying numerical quantities. We evaluate whether nine LLMs meet these requirements within a two-stage prediction pipeline, in which an upstream model has produced probabilistic outputs characterized by their likelihood and uncertainty, and LLMs are tasked with selecting an appropriate verbal descriptor for each. We simulate predictions from an upstream model by taking samples from a Beta distribution parameterized by its mode and prior sample size. We then prompt LLMs to explain these predictions under six domain contexts and with ten temperature settings, and repeating each experiment ten times. We find that LLMs are generally consistent but miscalibrated, with substantially weaker performance on uncertainty than on likelihood tasks. Providing models with precomputed summary statistics (mode and prior sample size) reduced sensitivity to contextual framing but did not resolve the underlying miscalibration, suggesting that the bottleneck resides in the verbalization step itself. These findings indicate that current LLMs do not yet constitute reliable zero-shot standalone risk communication tools for probabilistic predictions.

---


### 115. [NeuroOnline: Bridging Pretraining and Online Adaptation for EEG Foundation Models](https://arxiv.org/abs/2607.03925)

**<font color=#1a73e8>作者：</font>** Weibin Li, Wendu Li, Yushan You 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models have shown strong potential in learning generalized representations across subjects and tasks. However, most existing approaches follow a pretraining-static deployment paradigm, which suffers from two key limitations: (1) misalignment between pretraining objectives and downstream tasks, and (2) limited adaptability to distribution shifts in online settings. We propose Online Neural Adaptation (NeuroOnline), a unified framework that enables continuous adaptation in online scenarios. NeuroOnline integrates two complementary mechanisms: (1) multi-view consistency learning, which enforces cross-view alignment to promote consistent and task-relevant representations, and (2) context-aware representation modulation, which leverages a learnable context prompt with cross-attention to dynamically adapt representations to evolving data distributions. Together, these mechanisms unify representation alignment and dynamic adaptation. Experiments on multiple EEG benchmarks show that NeuroOnline consistently outperforms strong baselines in online settings, achieving better performance under distribution shifts. Ablation and sensitivity studies further validate the necessity of each component and the effectiveness of the overall design.

---


### 116. [Probe, Don't Prompt: A Hidden-State Probe for Metadata Filtering in Multi-Meta-RAG](https://arxiv.org/abs/2607.03929)

**<font color=#1a73e8>作者：</font>** Mykhailo Poliakov, Nadiya Shvai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-Meta-RAG improves retrieval for multi-hop question answering by filtering a vector store on metadata (the news source) that it extracts from each query by prompting gpt-3.5-turbo. We show this proprietary, free-form extractor can be replaced by a local, deterministic probe trained on the hidden states of a small open-source language model. On all 2556 MultiHop-RAG queries the probe reaches 90.9% set-exact accuracy against 88.0% for a model-free substring baseline and 80.9% for GPT-3.5, a margin that comes entirely from null queries, on which GPT-3.5 never abstains; on non-null queries all three stay within about a point. Because the probe's output space is exactly the fixed 49-source vocabulary, it cannot drift outside the allow-list as the prompted model does. Three design choices make it work: selecting a shallow layer, mean pooling, and class-imbalance-aware multi-label training over the long tail of sources. A 135M-parameter model lands within ~1.5 points of a 1.5B one, so the filter is cheap to output: a partial forward pass through the first few layers plus one linear head, with no API. The code is available at this https URL.

---


### 117. [MPSelectTune: Prompt-type Selection for Fine-tuning improves Concept Unlearning in LLMs](https://arxiv.org/abs/2607.03932)

**<font color=#1a73e8>作者：</font>** Shubhadip Nag, Srinjoy Das, Agniva Saha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs can be conveniently adapted to a diverse set of tasks, e.g, prediction, question-answering tasks, etc, using appropriate prompts with few-shot examples. Biased or harmful concepts, e.g. gender or bio-weapons, present in pre-trained LLMs can lead to unsafe or unethical responses for many such prompts. Removing such undesirable concepts robustly across different prompt types remains a challenging problem, since existing unlearning methods typically ignore the impact of prompt variation. In this paper, we explore a novel adversarial approach to use a joint prompt for the main task and concept task prediction. We show that fine-tuning using the ``worst prompt type'' for concept prediction (with the highest concept accuracy) improves the average unlearning performance over a fine-tuning method that uses a combination of all prompt types. Our proposed method, MPSelectTune, is a two-stage approach that minimizes the concept accuracy of the highest accuracy-prompt type, after fine-tuning using a novel multi-task loss using multiple prompt types. Experimental results on four benchmarks show $2 - 15\%$ main task accuracy improvements over recent baselines and while reducing the worst-case concept accuracy by up to $17\%$ compared to recent baselines.

---


### 118. [EgoInertia-MI: A Multimodal Egocentric Vision and IMU Benchmark for Motor Impairment Assessment](https://arxiv.org/abs/2607.03934)

**<font color=#1a73e8>作者：</font>** Fatemah Alhamdoosh, Pietro Pala, Abduallah Mohamed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motor impairments, including tremor, bradykinesia, gait abnormalities, and postural instability, are common across many neurological and movement-related conditions. Conventional clinical assessments are often intermittent and may fail to capture subtle temporal variations in motor behavior. While wearable IMUs and third-person video have shown promise for objective motor assessment, third-person recordings raise privacy concerns and require constrained acquisition setups. In contrast, egocentric vision provides a more naturalistic and privacyaware alternative. In this work, we introduce EgoInertia-MI, a multimodal benchmark dataset combining synchronized egocentric video and wearable IMU signals for motor impairment analysis. The dataset contains 19 upper- and lower-body activities performed by healthy volunteers simulating varying levels of motor impairment severity levels: no impairment, mild impairment, and severe impairment. We establish two benchmark tasks: action recognition and motor impairment severity estimation, and evaluate multiple unimodal and multimodal baselines. Experimental results show that egocentric video provides strong cues for motor impairment assessment, while multimodal fusion achieves the best overall performance, reaching 0.78 Macro-F1 for severity estimation and 0.93 Macro-F1 for action recognition. These findings highlight the potential of combining egocentric vision and wearable sensing for ecologically valid and privacy-aware motor assessment. Code and data are available at:this https URL.

---


### 119. [Harness-Aware Self-Evolving: Co-Evolving Model Weights, Harness, and Task Solutions](https://arxiv.org/abs/2607.03935)

**<font color=#1a73e8>作者：</font>** Haochen Luo, Yi Huang, Sichun Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving frameworks usually optimize task solutions while treating the surrounding harness as fixed. We introduce Harness-Aware Self-Evolving (HASE), an agentic reinforcement-learning framework in which a single model can generate task solutions or edit selected harness components in a multi-turn action space. HASE enables a single Qwen3-8B model to match the text-classification performance of a GPT-OSS-120B model that uses Claude Code as the harness proposer. In alpha factor mining, HASE outperforms the reported GPT-OSS-120B baseline. HASE also repairs imperfect evaluation components and converges to state-of-the-art performance in circle-packing algorithm discovery. These results show that HASE improves the harness and the solution through one unified agentic process.

---


### 120. [Can Dialects Be Steered Like Languages? Sparse Neurons and Distributed Directions in Arabic LLMs](https://arxiv.org/abs/2607.03936)

**<font color=#1a73e8>作者：</font>** Kareem Elozeiri, Mervat Abassy, Omar Kallas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A key challenge in Arabic NLP is the scarcity of dialectal data relative to Modern Standard Arabic (MSA), causing LLMs to overproduce MSA and struggle with dialectally accurate generation. From an interpretability perspective, this raises a fundamental question: where and how are dialectal features encoded within model internals, and can these representations be leveraged to improve dialect generation without fine-tuning? This study investigates two complementary inference-time approaches that serve simultaneously as interpretability probes and control mechanisms. First, we conduct a neuron-level analysis, identifying sparse neuron populations that encode dialect-specific features and showing that amplifying or suppressing these neurons can steer model outputs toward target dialects. Second, motivated by the entanglement of dialectal features at the single-neuron level, we apply a vector-steering approach that extracts dialect-specific activation directions and injects them during inference. Together, these methods illuminate the geometry of dialectal knowledge in Arabic LLMs and offer a principled, interpretability-grounded framework for dialect control without requiring dialect-specific fine-tuning.

---


### 121. [Online Linear Programming for Multi-Objective Routing in LLM Serving](https://arxiv.org/abs/2607.03948)

**<font color=#1a73e8>作者：</font>** Zixi Chen, Yinyu Ye, Zijie Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the online routing problem in large language model serving, where requests arrive sequentially and must be dispatched to parallel decode workers under tight batch-size and KV-cache constraints. Unlike widely used routing heuristics that are not tied to explicit service-level objectives (SLOs) and offer limited control over latency-throughput trade-offs, we introduce a multi-objective optimization framework that formulates routing as an online linear programming with interpretable decision rewards. We apply an efficient bid-price control policy based on the online linear programming that admits requests when their SLO-weighted benefit exceeds their shadow prices. To meet millisecond decision requirements, we develop a warm-started, projected first-order updates that track the evolving dual shadow prices online with predictable runtime. We integrate our router into the Vidur simulator and demonstrate substantial improvements over standard baselines across multiple SLO regimes, including end-to-end latency, time-to-first-token, throughput, and tail performance. A big picture from our result: a science-based approach outperforms others based on heuristics.

---


### 122. [TESSERA v2: Scaling Pixel-wise Earth Foundation Models](https://arxiv.org/abs/2607.03949)

**<font color=#1a73e8>作者：</font>** Zhengpeng Feng, Sadiq Jaffer, Ira Shokar 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-wise Earth-observation (EO) foundation models are now achieving state-of-the-art performance via generated spatial embeddings. However, how these models scale and how best to spend a pretraining budget remain poorly understood. We present the largest controlled scaling study for EO to date: 395 training runs on 1,024 GH200 superchips within a fixed pixel-wise Barlow Twins family, each evaluated on 15 downstream tasks. We find that pretraining loss barely predicts downstream performance (|Pearson r| < 0.2), so selecting models by loss wastes a large share of the compute. We also find that, as the training budget grows, the encoder and the data should grow together while the projector stays fixed, which gives a simple rule for allocating compute. Using this rule, we train a family of pixel-wise models (0.5B and 1B, with a 2B model in training) and distill them into compact students for embeddings-as-data deployment. The 21-million-parameter distilled TESSERA v2-1B-M in aggregate outperforms all open and proprietary models tested, some of which are orders of magnitude larger. These students produce Matryoshka representations that are inexpensive to serve: a 16-dimensional prefix keeps 92% of the full 128-dimensional performance at 1/8 of the storage. Upon completion of training we plan to release v2 global embeddings covering 2017-2025. Together, these results give a concrete, empirically grounded recipe for scaling pixel-wise EO foundation models: train large encoders, select by downstream performance, and distil into flexible student models. All code will be released at this https URL.

---


### 123. [The Remarkable Effectiveness of Providing AI Agents with Natural Language Tools: A Replication Study Validating NLT Performance Across 14 Models](https://arxiv.org/abs/2607.03953)

**<font color=#1a73e8>作者：</font>** Alexander Somma, Isabelle Plante, Fred Premji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study independently replicates and extends the Natural Language Tools (NLT) framework of Johnson et al.~(2025), which questions the use of structured tool calling in large language model (LLM) agentic systems. We evaluated NLT across 14 models and 8,560 trials, adding newer frontier, reasoning, and open-weight models to the original set. The results confirm the core findings and add detail. NLT improves tool-calling accuracy by 14.9 percentage points overall (62.3\% versus 47.4\% structured) and reduces critical errors by 93\% (51 versus 755 errors). The gains depend on model capability: models without native tool calling, reasoning models, and smaller models gain substantially (+24.0pp to +43.1pp), while heavily optimized frontier models (GPT-5, Gemini 2.5 Pro) show smaller or reversed advantages. This matches recent analyses of reinforcement-learning-optimized tool use (Martinez, 2025). NLT also cuts token usage by 25.2\%. The reliability and efficiency advantages compound in recursive agentic workflows, where agents chain many tool calls across sub-agents: a structured failure triggers retries, fallback routing, and coordination overhead, while NLT avoids most of that cost at the source. This work makes three contributions: (1) the first independent validation of NLT using open-source tooling, (2) evidence that model capability moderates NLT's advantages (Chen et al., 2025; Zhang et al., 2025), and (3) a measurement of NLT's reliability benefit (93\% fewer errors), its most deployment-relevant property given the known fragility of structured tool calling. NLT is a practical alternative to structured tool calling, especially for production systems that value reliability over parseability.

---


### 124. [NormWorlds-CF: Solver-Verified Counterfactual Normative Reasoning with Metamorphic-Relation GRPO](https://arxiv.org/abs/2607.03957)

**<font color=#1a73e8>作者：</font>** Xinqi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can reach the right normative verdict for the wrong reason. We introduce NormWorlds-CF, a solver-verified environment for counterfactual normative reasoning in executable rule worlds. Its deterministic solver produces final answers, proof and falsification certificates, argument statuses, support sets, and paired-world change labels, enabling supervision and evaluation without LLM judges. The benchmark contains staged SFT diagnostics and a compact paired-world task with 270 root families and 1080 canonical-to-variant pairs. The SFT diagnostics show that final-answer supervision is an unsafe proxy: answer-only SFT reaches perfect accuracy on answer tasks but scores zero on falsification, while proof-plus-falsification training with targeted replay reaches strong all-task accuracy. For the structured-change task, we introduce metamorphic-relation GRPO (MR-GRPO), a class-conditioned reward for GRPO that gives partial credit for relation families and solver-visible change fields. In matched 1.7B continuation experiments, MR-GRPO improves held-out relation accuracy and relation-family correctness, and reduces wrong-family error, compared to sparse and answer-only GRPO. In Qwen3-4B three-seed validation, answer-only reward improves answer-change fields but weakens relation-family structure, sparse reward preserves coarse relation labels best, and MR-GRPO delivers the strongest balanced performance across answer-change, support-change, status-change, and soft root-level metamorphic-relation metrics. These results show that verified counterfactual structure can shape post-training beyond final answers, while exact full change-record generation, invariant subtype recognition, and out-of-distribution (OOD) transfer remain open problems.

---


### 125. [BanglaMemeEvidence: A Multimodal Benchmark Dataset for Explanatory Evidence Detection in Bengali Memes](https://arxiv.org/abs/2607.03981)

**<font color=#1a73e8>作者：</font>** Fatema Tuj Johora Faria, Mukaffi Bin Moin, Md. Mahfuzur Rahman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memes have become influential communication tools on social media, combining viral visuals with concise messaging to convey impactful ideas. While substantial research has examined the affective dimensions of memes, key challenges such as detecting harmful content, identifying cyberbullying, and performing accurate sentiment analysis remain critical, largely due to the need for deeper contextual understanding. In this paper, we introduce MemeEvidenceDetect, a hybrid task aimed at analyzing a meme and its contextual information to identify specific sentences that explain or elucidate its meaning and humor. To support this task, we present BanglaMemeEvidence, a curated dataset of 2,917 Bengali memes, emphasizing its significance as a resource for the Bangla language. Each meme is annotated with natural language explanations, including Meme OCR, Meme Context, and Evidence Sentences, alongside relevance scores that reflect the relationship between a meme and its corresponding annotations. To address the gap in dynamically inferring a meme's context, we propose BengaliMemeEvidenceNet, a hybrid multimodal framework that integrates textual and visual features for comprehensive meme representation. Our experiments demonstrate the effectiveness of BengaliMemeEvidenceNet, achieving an F1 score of 0.74. To the best of our knowledge, this is the first study to focus on evidence detection in Bengali memes, marking a notable step forward in the analysis of memes in low-resource languages.

---


### 126. [Candidate-Constrained Retrieval-Augmented Generation for LongEval-RAG: System Design and Empirical Analysis](https://arxiv.org/abs/2607.04008)

**<font color=#1a73e8>作者：</font>** Yingdong Yang, Haijian Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a candidate-constrained retrieval-augmented generation system for LongEval-RAG, where each query is associated with an organizer-provided candidate set and all retrieved evidence and final citations must remain within that set. The system combines deterministic provenance tracking with passage-based retrieval, deterministic query expansion, pseudo-relevance feedback (PRF), reciprocal rank fusion (RRF), lightweight evidence reranking, citation-aware evidence aggregation, and optional MiniLM sentence reranking. We evaluate ten pipeline variants using a primary organizer evaluation and a supplementary self-generated diagnostic protocol. The primary evaluation shows that the strongest balanced variant is rule-minilm: a rule-based chunking pipeline with query expansion, PRF, RRF, reranking, citation prior, and late MiniLM sentence selection. This variant obtains the highest BERTScore, retrieval precision, nugget coverage, and average grade among our submissions. The result suggests that the main gain does not come from more complex semantic or topic-shift chunking, but from pairing stable rule-based evidence units with sentence-level neural selection before generation. The supplementary LLM-judge evaluation remains useful for early diagnosis and additional analysis, but it emphasizes different systems than the primary gold-answer and nugget-based evaluation, highlighting the need for multi-metric RAG evaluation.

---


### 127. [Explainable AI for Screening Abuse-Related Trauma in Bangladeshi Children: A Training-Free Multimodal Framework Evaluated on Noise-Aware Synthetic Data](https://arxiv.org/abs/2607.04010)

**<font color=#1a73e8>作者：</font>** Salma Hoque Talukdar Koli, Fahima Haque Talukder Jely  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bangladesh has an estimated 1.17 mental-health professionals per 100,000 population and only six child psychiatrists nationwide. No Bengali-language, culturally adapted tool exists for early screening of abuse-related psychological trauma in children. We present ShishuRaksha AI, a decision-support (not diagnostic) framework that fuses four screening modalities: validated questionnaires (SDQ, CPSS), Bengali narrative text, House-Tree-Person (HTP) drawing features, and facial affect. The fusion is training-free and clinically weighted, uses cross-modal attention, and includes a single-modality override rule. Every risk score is explained through clinically weighted, perturbation-based additive attribution and rendered as a bilingual (Bangla/English) report with referral routing to national child-protection services (OCC, DSS, NMHH) under the Children Act 2013. No clinical dataset of abused children can be collected ethically at this stage, so we introduce a noise-aware synthetic benchmark (500 cases, 116 positive [23.2%], four deliberate noise layers, literature-grounded HTP priors) and evaluate tree-ensemble surrogates of the fusion design (facial channel excluded) under 5-fold stratified cross-validation. The fused model reaches an AUC of 0.874 [0.834-0.908], against 0.756 [0.705-0.803] for an SDQ-only baseline, with ablation, operating-point, subgroup, and calibration analyses. We state all limitations openly, including synthetic-only data, no held-out set, text-feature circularity, and an urban-rural subgroup gap. This work is a feasibility study and a design contribution toward ethically deployable child-protection screening in low-resource settings.

---


### 128. [When Does Small Data Work? Accuracy and Efficiency Trade-offs Between Tabular Foundation Models and Conventional Methods for Crowd-State Classification at Hajj and Umrah](https://arxiv.org/abs/2607.04013)

**<font color=#1a73e8>作者：</font>** AlJawharh S. AlOtaibi, Mohamed Eltahir, Jude AlSubaie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from few labeled examples is a central challenge in tabular machine learning, and it becomes the binding constraint in domains where labeling is costly, such as crowd monitoring during Hajj and Umrah. Tabular foundation models, which predict from only a handful of examples without task-specific training, were recently introduced to address this very-few-label regime. In this study we test them on crowd-state classification to assess how much they help when labels are scarce, and we compare them against standard machine learning methods to characterize the accuracy and efficiency trade-offs between the two approaches. Using three real datasets we evaluate different machine learning models, in untuned and tuned forms, against three foundation models. Results show that no single family is best everywhere. The right choice depends on the label budget. When labels are very few, foundation models lead. As labels grow, tuned conventional models catch up and significantly surpass the foundation models on the more structural geometry target. Efficiency separates them further where tuned machine learning models incur a large tuning cost that foundation models avoid, although foundation models reprocess their context at every prediction. We summarize these results as a practical map of which approach to prefer under a given label budget and computational budget.

---


### 129. [Paired Uterine Whole-Slide Images and Pathology Reports for Multimodal Computational Pathology](https://arxiv.org/abs/2607.04020)

**<font color=#1a73e8>作者：</font>** Han Li, Jingsong Liu, Ayako Ura 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uterine diseases represent an important category of gynecologic pathology and require accurate histopathological assessment for diagnosis and treatment planning. Whole-slide images (WSI) have enabled the digital transformation of pathology workflows and provided new opportunities for artificial intelligence (AI) in computational pathology. In particular, multimodal models that jointly analyze histopathology images and pathology reports have shown promising potential for automated pathology report generation and AI-assisted diagnosis. However, the development of such systems remains limited by the scarcity of datasets that pair whole-slide images with clinically meaningful pathology reports. Instead, existing pathology datasets focus on patch- or slide-level annotations of a single endpoint (e.g., disease class), which do not fully capture the rich information in full clinical diagnostic workflow reports. Here, we introduce TUM-Uteria, a uterine pathology dataset comprising WSIs paired with diagnostic pathology reports at both the case and slide levels, collected from a tertiary medical center. The dataset contains 216 clinical cases, comprising 455 slide-level WSI-report pairs. The dataset underwent a structured multi-stage validation procedure involving board-certified pathologists to ensure reliable annotations. TUM-Uteria supports research in computational pathology, including whole-slide image analysis, multimodal learning, and automated pathology report generation.

---


### 130. [CrossHallu: Do Hallucination Signals Generalize Across Languages and Domains in Large Language Model's Internals?](https://arxiv.org/abs/2607.04029)

**<font color=#1a73e8>作者：</font>** Aisha Alansari, Malak Alkhorasani, Hamzah Luqman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent hallucination detection techniques in large language models (LLMs) focus on directly extracting features from a model's internal representations and training a classifier on these features to detect hallucinations, demonstrating promising results. Notwithstanding this advancement, most internal-state hallucination detection techniques have been explored predominantly in English, raising the question of whether such internal signals generalize across different languages and domains. To address this gap, we present CrossHallu, the first study to evaluate the cross-lingual and cross-domain generalization of hallucination detection using internal representations from six LLMs on the generative question-answering task. We conduct a systematic Arabic <-> English evaluation using TruthfulQA, an Arabic translated version of TruthfulQA, and HalluScore. This evaluation encompasses monolingual training and testing, cross-lingual transfer, cross-domain transfer, and combined cross-lingual and cross-domain transfer. The results reveal that internal-state hallucination signals in LLMs transfer across languages and domains for most models, with cross-lingual performance highly dependent on both class separability and language alignment in the feature space, whereas cross-domain transfer within Arabic varies depending on the training and testing datasets used for the hallucination detector. The code is publicly available at this https URL.

---


### 131. [Telescope: Improving Zero Shot Detection of LLM Generated Content By Measuring Token Repetition Probability](https://arxiv.org/abs/2607.04061)

**<font color=#1a73e8>作者：</font>** Christopher Nassif, Josh F. Cooper  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distinguishing Large Language Model (LLM) generated text from human writing is a critical and difficult challenge. While LLMs are trained to write like humans, we hypothesize that this training leaves an indelible mark. LLMs develop a particularly strong aversion to token repetition very early in training. This bias persists as a ''Vestigial Heuristic'' (a developmental artifact) that is activated in LLM-generated text, separating LLM from human writing. To probe this phenomenon, we introduce Telescope Perplexity, a metric that evaluates the token repetition of the model, $P(s_i | s_{1:i})$ . Our empirical investigation reveals that the Telescope Perplexity signature emerges early in pre-training, and Telescope Perplexity empirically enables highly effective zero-shot LLM detection. We show state-of-the-art or competitive performance across diverse datasets (including modern evaluation sets we introduce), reference models, and perturbation schemes with greater efficiency than other methods.

---


### 132. [Beyond Multilingual Averages: MTEB-PT, a Benchmark for Portuguese Sentence Encoders](https://arxiv.org/abs/2607.04071)

**<font color=#1a73e8>作者：</font>** Lucas Hideki Takeuchi Okamura, Alexandre Alcoforado, Anna Helena Reali Costa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Portuguese remains underrepresented in text embedding evaluation, despite being one of the most widely spoken languages in the world. As a result, embedding models are often selected based on English or multilingual metrics, while their effectiveness in Portuguese remains unclear. We present MTEB-PT, a Portuguese benchmark constructed from a subset of MMTEB, comprising 14 existing datasets across Semantic Textual Similarity (STS), classification, retrieval, and reranking. We use this benchmark to evaluate 17 open- and closed-source embedding models under a unified protocol. Our results show that Portuguese performance is strongly task-dependent: multilingual rankings do not reliably predict Portuguese-specific performance across task families, no single model dominates all settings, and models with stronger long-context capacity are particularly advantageous on longer-input tasks such as retrieval and reranking. The benchmark also shows that language-specific fine-tuning still improves model performance in Portuguese, especially on task types that match the adaptation data most closely. To examine this effect, we fine-tune three representative backbone models with Portuguese contrastive supervision and Matryoshka Representation Learning (MRL). These benchmark-informed baselines yield their strongest gains on STS, consistent with the predominantly symmetric supervision used during training, while also improving retrieval and remaining competitive under dimensional truncation. We release the MTEB-PT benchmark, the fine-tuned models, and the training and evaluation code.

---


### 133. [Seeing Once is Enough? Online Geometry-Aware Token Pruning for 3D Question Answering](https://arxiv.org/abs/2607.04079)

**<font color=#1a73e8>作者：</font>** Ruei-Chi Lai, Bolivar Solarte, Chin-Hsuan Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Multi-modal Large Language Models (MLLMs) have demonstrated remarkable performance on 2D question answering tasks. However, extending these models to the 3D question answering remains challenging, as they typically require multiple views of the scene, which incurs substantial computational cost at inference. To mitigate this issue, existing solutions rely on strategic frame selection or token-merging algorithms that require preprocessing in advance all frames of the scene, i.e., an offline fashion. In contrast, we propose the first online token-pruning method that can be integrated seamlessly with current MLLM models for 3D question answering tasks, without additional training and with lower memory this http URL key insight is to project each input frame into a shared voxel space using depth information and camera pose, identifying spatially-overlapped regions across frames and selectively pruning redundant image tokens before they enter the language model. Our method enables efficient online processing while reducing up to 50% of token usage. We apply this approach to Qwen2.5-VL-7B and Qwen3-VL-8B, demonstrating improved performance on the ScanQA, SQA3D, and OpenEQA-HM3D benchmarks.

---


### 134. [A Unified Framework for In-Context Learning with Causal and Masked Language Models](https://arxiv.org/abs/2607.04081)

**<font color=#1a73e8>作者：</font>** Chenrui Liu, Chuanlong Xie, Falong Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) has emerged as a central capability of pretrained language models, yet its theoretical analysis has focused primarily on causal language models trained by left-to-right autoregressive prediction, such as GPT-style models. Masked language models instead recover masked tokens from bidirectional context, and their role in ICL remains less understood. We develop a statistical learning framework that represents the context examples by their empirical measure and models prediction as a function of the context and the query. This formulation places autoregressive and masked pretraining objectives within a common excess-risk analysis. Under Wasserstein-type regularity conditions, we relate pretraining with T tasks and N samples per task to k-shot excess risk at inference, obtaining same-order upper bounds for masked and autoregressive objectives. We also study task-distribution shift, where pretraining tasks are sampled from P and inference tasks from Q; the resulting bound contains an additional term controlled by the lifted Wasserstein distance between P and Q. The bounds further imply an order-optimal allocation under a fixed pretraining data budget and refined rates under intrinsic low-dimensional structure. Experiments on controlled function-learning tasks show that the Masked Pair Encoder (MPE) can achieve performance comparable to GPT-2-style causal Transformers, suggesting that ICL behavior is not specific to causal language models.

---


### 135. [Forethought: Verifiable Reasoning from Neurosymbolic Primitive Programming](https://arxiv.org/abs/2607.04096)

**<font color=#1a73e8>作者：</font>** Vishvesh Bhat, Jay Vaghasiya, Emmanuel Anaya Gonzalez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current agentic workflows usually involve decomposing user requests into sequences of tool calls with correctly resolved parameters, the results of which are processed through reasoning traces in the language model's context window. The prevailing route to improve such reasoning is test-time scaling, which trains models to search over long chains of thought; but the resulting capability is entangled in model weights, is not verifiable step-by-step, and is costly at inference. We present Forethought, a neurosymbolic reasoning system that instead treats reasoning as an explicit, verifiable program, that builds from a library of symbolic and neural primitives which are composed through a domain-specific language. The result are reasoning programs, which are concrete representations of the model's work, and as such can be inspected and modified before deployment. Instantiated as a tool-calling execution kernel and evaluated across five benchmarks, Forethought improves base-model accuracy by about 30% relative and outperforms vanilla prompting, reinforcement learning scaffolds, and prompt-evolution methods, enabling small models to match or exceed frontier models capabilities. In a direct comparison, a non-reasoning model augmented with Forethought competes with a dedicated reasoning model while requiring roughly three orders of magnitude less post-training investment, and remains model-agnostic and auditable.

---


### 136. [Dictionaries, Not Darwin: Set-Level Selection Beats LLM Evolution in Scientific Equation Discovery](https://arxiv.org/abs/2607.04108)

**<font color=#1a73e8>作者：</font>** Pan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as evolutionary engines for scientific discovery: generate candidates, select winners, feed them back as parents, and repeat. We audit whether this loop actually compounds discovery in scientific equation discovery, a setting where finite samples make structure underdetermined and interpolation easy. Under matched LLM-call budgets, parent-conditioned evolution is indistinguishable from fresh independent sampling: median OOD NMSE is 0.045 vs. 0.049, instructed multi-parent crossover is worse, final success is predicted by initial proposal quality, and multiple iteration schemes fail to add solved problems. Operationally, the loop reduces to what it produces: a dictionary of candidate terms. We turn that diagnosis into PTB-Search, a one-generation method for componentized scientific discovery. PTB-Search samples independent LLM proposals once, extracts reusable terms into a per-problem dictionary, and performs train-only set-level sparse selection with least-squares coefficients. Its central principle is that underdetermined data identifies the joint behavior of term sets, not reliable per-term credit. On identical dictionaries and zero additional LLM calls, set-level selectors solve 165--169 of 717 cells, while single-term reductions solve only 74--78. On the official 239-problem LLM-SRBench split, PTB-Search reaches 73.2% Acc0.1 with Llama-3.1-8B and 77.0% with a single-seed DeepSeek-V4 anchor, versus 49.2% for the best reported baseline, using one tenth of the standardized call budget. A program-domain stress test gives a scoped boundary: generation count remains unreliable, while retained external state can help in harder non-linear spaces. Across these results, LLMs are best understood as material suppliers; discovery is carried by external set-level selection over reusable components.

---


### 137. [DynaVieW: Schema-Guided World Modeling for Understanding Hierarchical Visual Dynamics](https://arxiv.org/abs/2607.04112)

**<font color=#1a73e8>作者：</font>** Silin Gao, Hao Zhao, Zeming Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs struggle to systematically model the temporal evolution of visual scenes in videos or multi-image sequences. Such inputs require models to predict or simulate multiple levels of dynamic constituents, such as actions taken in the visual sequence, and the associated changes to the visual environment that result. To address this challenge, we propose a dynamic schema-guided world model, DynaVieW, optimized for visual dynamic prediction and simulation. DynaVieW achieves an in-depth understanding of visual dynamics by learning interleaved state-transition sequences, where states cover broad visual scenes from video keyframes, and transitions capture comprehensive dynamic constituents within a hierarchical schema. DynaVieW jointly models transition prediction and state simulation under a mixture-of-experts architecture, with a cross-expert selective attention and a schema token re-weighted loss, to ensure effective and robust learning. DynaVieW's understanding of visual dynamics boosts its downstream performance in visual narrative creation and world simulation, showing improved consistency, controllability, and instruction-following.

---


### 138. [HCSU: A Dataset and Benchmark for Fine-Grained Historical Calligraphy Style Understanding](https://arxiv.org/abs/2607.04147)

**<font color=#1a73e8>作者：</font>** Yinsheng Yao, Yan Liu, Chen Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated fine-grained perception of calligraphy styles--a task vital to cultural heritage preservation--remains a critical challenge for Large Vision-Language Models (LVLMs), largely constrained by existing datasets that suffer from modal mixture and flattened labels. To bridge this gap, we introduce HCSU, the first comprehensive dataset tailored for fine-grained Historical Calligraphy Style Understanding. HCSU comprises 39,307 meticulously curated character images from 49 historically prominent calligraphers across 10 dynasties, systematically decoupling authentic ink manuscripts (Tie) from stone rubbings (Bei) to resolve the long-standing modal mixture problem. Moving beyond conventional flattened labels, HCSU provides hierarchical expert-written aesthetic descriptions, enabling two rigorous evaluation protocols: fine-grained style discrimination and interpretable aesthetic reasoning. Extensive evaluations reveal a persistent gap between calligraphy-related knowledge and visually grounded style perception: state-of-the-art LVLMs show non-trivial performance but remain sensitive to script-level, textual, and source-specific cues, and often struggle to ground aesthetic judgments in fine-grained brushwork evidence. Ultimately, the HCSU benchmark exposes fundamental limitations in current multimodal architectures, aiming to inspire the evolution of expert-level visual reasoning for cultural heritage preservation. The dataset is available at this https URL.

---


### 139. [Beyond Scene Priors: Fine-Grained Traffic Scene Reasoning with Benchmarking and Query-Guided Small-Object Focus](https://arxiv.org/abs/2607.04149)

**<font color=#1a73e8>作者：</font>** Waikit Xiu, Qiang Lu, Zian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In safety-critical traffic scenarios, answering complex questions relies on minute, localized visual cues. However, standard Multimodal Large Language Models (MLLMs) tend to over-attend to backgrounds, overwhelming crucial small objects during visual-language alignment, a failure mode we term 'critical evidence dilution.' Furthermore, existing visual question answering (VQA) datasets rarely expose this flaw, as they lack large-scale, distractor-heavy evaluations that require pinpointing local evidence. To bridge this evaluation and architecture gap, we introduce the Fine-Grained Traffic Reasoning Benchmark (FGTR-Bench) and the Text-Guided Small-Object Reasoning MLLM (TSR-MLLM). FGTR-Bench comprises 40,236 single-image Multiple-Choice Questions (MCQs) created via multi-agent generation, consistency checks, and expert audits, alongside a disjoint 4,947-sample blind test split. To resolve evidence dilution, TSR-MLLM, built on Qwen3-VL-4B, uses a query-conditioned Text-Guided Small-Object Focus (TG-SOF) map. Applied once at the decoder boundary, the map adds sparse Top-K gated residuals to the most question-relevant vision slots while leaving text tokens unchanged. Together with lightweight decoder adaptation, TSR-MLLM preserves single-pass inference without external detectors or image re-encoding. Under matched settings, TSR-MLLM outperforms the strongest 4B baseline by 2.1 points on FGTR-Bench (74.1% overall), with larger gains on evidence-local tracks. Furthermore, it remains competitive on DriveQA-V (CARLA Signs) under greedy decoding without task-specific fine-tuning.

---


### 140. [Language models guide symbolic equation discovery by controlling search](https://arxiv.org/abs/2607.04156)

**<font color=#1a73e8>作者：</font>** Zikai Xie, Wenmei Li, Man Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific equation discovery must combine broad domain priors with strict numerical testing. Symbolic regression supplies numerical grounding but faces a combinatorial search space, whereas many language-model systems ask the model to propose or select formulas directly. We test a different division of labour. We compare role specifications in which the language model acts as equation author, candidate decider or search controller, alongside end-to-end language-model and purely numerical baselines. In the controller setting we propose here, implemented as LLM-PySR, language models specify variables, operators, transformations and search depth; symbolic regression enumerates and fits expressions; and deterministic metrics govern retention. Across 74 AI-Feynman equations and seven complex formula-recovery tasks, search control achieved the strongest observed balance of accuracy, complexity, stability and cost. On an independent battery dataset, LLM-PySR identified a compact piecewise-linear relation between early voltage-curve displacement and cycle life. The results suggest that language models should shape hypothesis exploration rather than decide which equations survive.

---


### 141. [SeeMe: Mitigating Hallucinations in Large Vision-Language Models through Effective Visual Token Engineering](https://arxiv.org/abs/2607.04163)

**<font color=#1a73e8>作者：</font>** Kai Tang, Jinhao You, Bohua Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved remarkable progress in visual understanding tasks such as image captioning and visual question answering. However, they remain susceptible to hallucinations, generating content that is inconsistent with the actual visual input. Existing methods primarily intervene at the decoding stage, while overlooking a critical source of hallucinations: irrelevant or noisy visual tokens that mislead the decoding process. To address this issue, we propose SeeMe, a training-free framework that introduces the concept of feature engineering from traditional machine learning into LVLMs. SeeMe restructures visual tokens through a three-stage token engineering process to suppress hallucination sources while preserving informative visual evidence. Experiments on MME, POPE, and AMBER benchmarks across four LVLMs demonstrate that SeeMe consistently reduces hallucinations and improves output consistency, providing a novel perspective for mitigating hallucinations in LVLMs.

---


### 142. [Geometry of Ordinal Representations in Language Models](https://arxiv.org/abs/2607.04167)

**<font color=#1a73e8>作者：</font>** Saksham Bassi, Sharvi Tomar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work showed that language models represent character counts on curved 1D manifolds, with attention heads performing geometric transformations to enable computation. We test whether this generalizes across four ordinal tasks (bracket depth, indentation, table position, numeric magnitude) in Gemma-2-2B, Gemma-2-9B, and Qwen3-4B. We find that 1D manifolds with place-cell feature tiling emerge for tasks where the ordinal variable is locally computable from token identity, while tasks requiring cross-position integration or semantic extraction produce higher-dimensional or incoherent representations. Geometric computation is architecture-dependent: Qwen3-4B shows substantially stronger twisting than Gemma models for indentation, and its twisters preserve ordinal order, unlike its numeric twisters. Activation patching confirms that the identified manifold subspaces concentrate task-relevant information, with manifold-direction ablation causing dramatically larger probe accuracy drops than random-direction controls.

---


### 143. [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](https://arxiv.org/abs/2607.04179)

**<font color=#1a73e8>作者：</font>** Zhaohong Liu, Hao Ye, Xianlin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving. However, standard Supervised Fine-Tuning (SFT) often suffers from reasoning hallucinations and conservative biases. While traditional tool-augmented frameworks and Chain-of-Thought (CoT) approaches mitigate these issues, they incur exorbitant token consumption and unacceptable latency, rendering real-time deployment impractical. To resolve this reliability-efficiency trade-off, we propose CritiqueDriveVLM, a novel unified three-stage framework internalizing reasoning directly into the VLM. First, we introduce Critique-Driven Multi-Turn Reinforcement Learning (RL) guided by a multi-dimensional verifier. By providing granular scalar feedback and a multi-turn penalty, we force the policy to internalize logical deduction, cultivating a robust System-2 Teacher that achieves high accuracy without fragile external tools. Subsequently, we propose Latent Thought Distillation to overcome the latency bottleneck. By aligning the Student's latent representations with the Teacher's fully converged reasoning states, we compress deep logical capabilities into a fast, CoT-free System-1 Student. Extensive experiments on the widely-used DriveLMM-01 benchmark demonstrate remarkable improvements. Compared to the base model, our tool-free Teacher significantly boosts Multiple Choice Quality (MCQ) from 55.54% to a state-of-the-art 76.54%. Crucially, our distilled Student preserves competitive reasoning depth while drastically minimizing generation length to an average of merely 28 tokens. This slashes inference latency by 88% (from 3482 ms to 416 ms), paving a highly robust pathway for low-latency autonomous this http URL source code is available at this https URL.

---


### 144. [Topology-Driven Transferability Estimation for 3D Medical Vision Foundation Models](https://arxiv.org/abs/2607.04199)

**<font color=#1a73e8>作者：</font>** Jiaqi Tang, Shaoyang Zhang, Fandong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing number of medical vision foundation models highlights the need for effective model selection. However, mainstream selection methods rely on exhaustive fine-tuning, which is computationally expensive. Most of the existing Transferability Estimation (TE) metrics are primarily designed for image-level classification. They fail to preserve spatial relationships and fine-grained boundary details, which are crucial for the segmentation task. Additionally, while image-level tasks typically process a single feature vector per input, dense prediction tasks in 3D medical imaging require voxel-wise evaluation against dense annotations. To bridge these gaps, we propose a \textit{non-parametric, topology-driven} framework that estimates transferability directly from the alignment between the sparse 1-skeleton graph of dense features and semantic labels via Minimum Spanning Trees (MST). We decouple the alignment into two complementary geometric scales: Local Boundary-Aware Topological Consistency (LBTC) to assess boundary separability, where we prove that the MST leakage rate serves as a finite-sample lower bound on the Bayes error; and Global Representation Topology Divergence (GRTD) to evaluate the overall anatomical layout. Crucially, we formally justify a counterintuitive mechanism: Although without fine-tuning, the randomly initialized segmentation decoder acts as a topology-preserving spatial projector, reducing the variance of pairwise distance estimates and stabilizing global alignment evaluation. Fused via a task-adaptive gating mechanism, these dual metrics adapt to diverse clinical complexities. Evaluated on a large-scale benchmark of 114,000 3D medical volumes across diverse anatomical tasks, our topological framework achieves state-of-the-art transferability estimation with an average weighted Kendall (outperforming by 0.36) while accelerating evaluation by 56 times.

---


### 145. [Agentic IoT: Architectures, Applications, and Challenges Toward the Internet of Agents](https://arxiv.org/abs/2607.04219)

**<font color=#1a73e8>作者：</font>** Rümeysa Hilal Sevinç, Bahaeddin Türkoğlu, İbrahim Kök  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of AI into Internet of Things (AIoT) systems has gradually transformed them from passive data collection infrastructures into intelligent systems capable of anomaly detection, predictive maintenance, classification, forecasting, and optimization. However, most existing solutions still rely on task-specific models that infer from sensor data; thus, system-wide capabilities such as real-time reasoning, adaptive planning, autonomous coordination, learning, tool use, and contextual decision-making remain limited. This paper examines Agentic IoT as a next-generation cognitive IoT paradigm that integrates the perception, reasoning, planning, learning, and action capabilities of autonomous AI agents with cyber-physical systems. Agentic IoT aims to transform IoT from data-centric sensing and inference infrastructures into distributed cognitive agent ecosystems operating across the device/edge-fog-cloud continuum. The paper first grounds this transition as a paradigm shift and positions Agentic IoT in relation to AIoT, edge intelligence, multi-agent systems, and the Internet of Agents. It then systematically reviews current studies, presents a holistic architectural framework, discusses domain-specific application potential, and identifies key technical, operational, and research challenges together with future research directions.

---


### 146. [Detecting Hallucinations in Retrieval-Augmented Generation through Grounding-Aware Sensitivity by Perturbation (GASP)](https://arxiv.org/abs/2607.04223)

**<font color=#1a73e8>作者：</font>** Mohamed Aly Bouke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) reduces but does not eliminate hallucination, and existing detectors return a single answer-level score that does not indicate which sentence is unsupported, or why. To close this gap, we introduce Grounding-Aware Sensitivity by Perturbation (GASP), a span-level detector that scores each answer sentence by how strongly its likelihood depends on the retrieved evidence, a quantity we term grounding sensitivity. GASP holds the answer fixed and re-scores it under the full context, under no context, and with each chunk removed, then measures the log-likelihood drops and Jensen-Shannon divergences (JSD). The likelihood of a grounded sentence collapses once its supporting passage is removed, whereas a hallucinated sentence is almost unaffected, a contrast we interpret by casting decoding as a random nonlinear iterated function system (RNIFS). We evaluate GASP on three benchmarks (RAGTruth, TofuEval, RAGBench) with three instruction-tuned scorers from two model families (Qwen2.5-0.5B, Qwen2.5-1.5B, and SmolLM2-1.7B) under a leakage-clean protocol. On RAGTruth it reaches a response-level area under the ROC curve (AUC) of about 0.73 and a span-level AUC of about 0.67, improving significantly over perplexity and by clear margins over length, whole-context natural language inference (NLI), and self-consistency baselines. The only baseline competitive at the span level is a well-configured chunk-level entailment verifier, which requires a separate model, whereas a training-free threshold on the grounding features matches the trained classifier without labeled data and serves as the default detector. Beyond RAGTruth, the signal transfers to TofuEval but not to short-answer question answering in RAGBench, showing GASP is best suited to outputs constructed from the retrieved context rather than answers recoverable from parametric knowledge.

---


### 147. [Spinning Straw into Gold: Relabeling LLM Agent Trajectories in Hindsight for Successful Demonstrations](https://arxiv.org/abs/2607.04235)

**<font color=#1a73e8>作者：</font>** Zichao Li, Gang Wu, Zichao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents operate in partially observable, long-horizon settings where obtaining supervision remains a major bottleneck. We address this by utilizing a source of supervision overlooked in existing post-training methods: unintended yet successful goals embedded within agent rollouts. Specifically, we introduce Hindsight Supervised Learning (HSL), where an auxiliary LLM reviews each completed trajectory and relabels it with all of the natural-language goals the agent actually achieved. HSL then pairs the trajectory with its relabeled goals and uses these pairs for additional fine-tuning. To mitigate suboptimality in the relabeled data, we propose two learning techniques for HSL, irrelevant-action masking and sample reweighting. Our experiments show that HSL is flexible and compatible with existing post-training pipelines. It improves both SFT and DPO, with larger gains on long-horizon tasks with more diverse goal spaces. Moreover, HSL is sample-efficient: on ALFWorld, it surpasses baselines trained on the full dataset while using only one quarter of the ground-truth demonstrations.

---


### 148. [Biological Motifs for Agentic Control](https://arxiv.org/abs/2607.04240)

**<font color=#1a73e8>作者：</font>** Bogdan Banu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The transition of Large Language Models (LLMs) from passive generators to autonomous agents has introduced significant challenges in reliability, security, and state management. Current agentic architectures are often constructed ad-hoc, prone to hallucination cascades, infinite loops, and prompt injection attacks. This paper argues that many of these failure modes can be analyzed using control motifs long studied in systems biology, provided the comparison is made at the level of typed interfaces and coordination structure rather than literal biological mechanism.
We develop a typed interface correspondence between Gene Regulatory Networks and agentic software systems using polynomial functors and wiring diagrams. Five biological motifs are mapped to composable software design patterns: Coherent Feed-Forward Loops for noise suppression, Adaptive Immunity for layered security, Mitochondrial Signaling for resource governance, Endosymbiosis for neuro-symbolic integration, and Morphogen Diffusion for spatially varying coordination. An epistemic topology layer derives Kripke-style knowledge operators from the wiring diagram's observation structure and proves four predictive theorems for multi-agent scaling.
The core contributions are: (1) the Agentic Operad, a typed syntax for agent composition with provable error suppression bounds for feed-forward topologies; (2) an epistemic topology with four theorems (error amplification, sequential penalty, parallel acceleration, and tool density scaling) whose qualitative predictions are consistent with published multi-agent benchmarks; and (3) a six-layer progression from structure through development, grounded in autonomous learning frameworks and convergence proxies from the empirical literature. A reference implementation with 1,813 tests and 116 examples illustrates practical feasibility.

---


### 149. [Progress- and Reliability-Oriented Group Policy Optimization for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.04242)

**<font color=#1a73e8>作者：</font>** Mingxuan Fan, Peiyang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning (RL) has become an effective paradigm for improving large language model agents on long-horizon interactive tasks. To obtain finer-grained policy updates than trajectory-level optimization, recent work has moved toward step-level group-based RL, where intermediate steps are grouped and compared within a rollout batch. However, step-level advantage estimation is sensitive to how groups are formed: grouping by broad state keys improves coverage but may compare actions taken under different histories, while enforcing historical consistency yields fairer comparisons at the cost of fragmented groups and missing peer-comparison signal. In this paper, we propose ProGPO (Progress- and Reliability-Oriented Group Policy Optimization), a learned-critic-free method for context-consistent step-level learning. ProGPO keeps exact-prefix action comparison, and complements sparse peer comparisons with transition credit derived from rollout-based state potentials. To estimate these potentials reliably, ProGPO combines semantic expansion with inverse-variance fusion across history depths. We evaluate ProGPO on two challenging agentic tasks, ALFWorld and WebShop, with Qwen2.5-1.5B-Instruct. Results show that ProGPO improves over matched agentic RL baselines under comparable computational overhead, and additional Qwen2.5-3B-Instruct experiments further test the scalability of the proposed method.

---


### 150. [Quantize the Target, Quantize the Drafter: Efficient Inference with Qwen3.5-4B](https://arxiv.org/abs/2607.04244)

**<font color=#1a73e8>作者：</font>** Jaeyeon Kim, Jewon Lee, Bo-Kyeong Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This report describes our approach to the Efficient Qwen Competition, where the goal is to enable low-latency serving of Qwen3.5-4B on a resource-constrained NVIDIA A10G GPU. Our system combines a quantized target model with speculative decoding. To recover accuracy, we apply quantization-aware distillation to the target model while retaining the original quantization grid. To speed up decoding, a block-diffusion drafter specialized for the quantized target model is trained using a two-stage procedure: first learning from the high-precision target and then adapting to the low-precision target. Because the drafter is invoked at every speculative decoding step, we further reduce its overhead with quantization and sliding-window attention, preserving draft-token acceptance while improving long-context decoding latency. As a result, our submission achieves a 6.978$\times$ average speedup over the baseline while satisfying the required quality thresholds, ranking 3rd overall. We hope these results provide useful insights for practical LLM inference. The code and resources are available at this https URL

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-248](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

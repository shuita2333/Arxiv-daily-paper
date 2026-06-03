# 🧠 大模型相关研究 | 2026年06月04日

> 本类共 **188** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-188](./part-04.md)

---

### 1. [Auditable Climate Risk Intelligence from Fragmented ESG Data: Deterministic Orchestration and Imbalance-Aware Learning for Scope 1-3 Validation](https://arxiv.org/abs/2606.02604)

**<font color=#1a73e8>作者：</font>** Karan Sehgal, Khawar Naveed Bhatti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ESG and climate risk data remain fragmented across heterogeneous Scope 1, Scope 2, and Scope 3 reporting environments, while conventional validation pipelines lack provenance aware auditability, hidden drift detection, and reproducibility oriented governance. This paper proposes a deterministic climate risk intelligence framework integrating single source of truth orchestration, temporal anomaly detection, imbalance aware ensemble learning, and explainability oriented governance for auditable ESG validation. To support open reproducibility, we construct and release a synthetic ESG validation benchmark calibrated against publicly reported characteristics of the GHG Protocol, PCAF, and ISSB standards. The methodology incorporates temporal drift analysis, SMOTE based rare event optimization, ensemble learning, provenance aware orchestration, and TreeSHAP based interpretability for governance inspection and audit reconstruction. We evaluate the framework against statistical classifiers, anomaly detection methods, temporal forecasting baselines, and a threshold based system using classification metrics (recall, F1, ROC AUC), calibration metrics (ECE, Brier score), and a governance oriented audit trace completeness metric measuring the fraction of flagged anomalies for which a deterministic source to escalation provenance chain can be reconstructed. Results are reported as mean and standard deviation across stratified five fold cross validation with paired significance testing. The framework reframes ESG reporting toward deterministic climate risk governance infrastructure supporting reproducibility, explainability, and operational auditability.

---


### 2. [ReLoRA: Knowledge-Reusing Adaptation for Fast Rollout of Evolving LLM Services](https://arxiv.org/abs/2606.02606)

**<font color=#1a73e8>作者：</font>** Yang Xu, Zihuai Xu, Hongli Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed as continuously evolving services, where frequent base-model updates may invalidate previously deployed task-specific Low-Rank Adaptation (LoRA) adapters. For service providers managing numerous downstream model services, retraining each LoRA adapter from scratch for every updated base model is computationally prohibitive and delays service rollout. Meanwhile, the simpler alternative, i.e., naively applying the original LoRA adapter to the updated base model, often leads to degraded service quality due to adapter-backbone incompatibility. To address this problem, we propose ReLoRA, a knowledge-reusing re-adaptation framework that efficiently restores service-ready LoRA adapters for evolving LLM services while preserving or improving task performance. Specifically, ReLoRA comprises two key optimization steps: 1) Adaptive LoRA initialization leverages Bayesian optimization to construct a compatibility-aware starting point by fusing information from both the previously deployed task adapter and the base model's evolution; 2) Fine-tuning with scheduled regularization first rapidly steers the adapter to a high-quality region via strong regularization, followed by relaxed regularization for task-specific refinement. This design enables rapid service-quality recovery with reduced re-adaptation overhead. Extensive experiments demonstrate that ReLoRA reduces time-to-readiness by up to 8.9$\times$ and improves accuracy by up to 4.6\% compared to baselines.

---


### 3. [Hallucination Is Linearly Decodable from Mid-Layer Hidden States in Quantized LLMs](https://arxiv.org/abs/2606.02628)

**<font color=#1a73e8>作者：</font>** Aizierjiang Aiersilan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether open-source LLMs encode a linearly separable truthfulness signal in their hidden states, and at which network depth this signal is strongest. Across three $7$B--$8$B instruction-tuned models (Llama-3.1-8B, Mistral-7B, Qwen2.5-7B) loaded in $4$-bit NF4 quantization, we extract per-layer hidden states on four hallucination benchmarks (TruthfulQA, HaluEval-QA, FEVER, and a controlled synthetic set) and compare four detection approaches: linear and MLP probes, INSIDE EigenScore, self-consistency, and attention entropy. A linear probe on a single mid-network layer achieves $0.904$--$1.000$ AUROC on held-out splits, while sampling-based detectors do not exceed $0.541$ AUROC under the same protocol. The truthfulness signal is approximately linear: MLP probes rarely surpass linear probes by more than $0.01$ AUROC. Peak probing layers fall in a consistent band across model families on natural-language benchmarks -- blocks~$13$--$18$ of~$32$ for Llama and Mistral, and blocks~$19$--$25$ of~$28$ for Qwen. First-block attention entropy provides a complementary signal in knowledge-grounded settings ($0.866$--$0.941$ AUROC on HaluEval-QA) at no additional inference cost. The low discriminability of sampling methods under this protocol reflects a structural mismatch between paired-label evaluation and the information these methods access, rather than an inherent limitation of those methods. Code and data are released for full reproducibility on a single $8$\,GB GPU.

---


### 4. [CL-DMDF:Dynamic Multimodal Data Fusion Model Based on Contrastive Learning](https://arxiv.org/abs/2606.02659)

**<font color=#1a73e8>作者：</font>** Dong Li, Lingling Zhang, Binghao Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal data fusion involves integrating and analyzing information from multiple modalities to uncover latent correlations and complementary patterns, thereby enhancing data processing and decision-making. While existing methods for structured multimodal inputs are typically designed around specific tasks and assume fully observed modalities, real-world applications often suffer from uncertain or missing modality inputs due to various factors. Some traditional models overly emphasize local interactions within missing modalities, neglecting the global complementary cues embedded in multimodal representations. To overcome these limitations, we propose a Dynamic Multimodal Data Fusion model based on Contrastive Learning (CL-DMDF). CL-DMDF introduces a novel attention mechanism that operates across both feature and modality dimensions to compute reliable attention scores, effectively reflecting importance at each level. The CL-DMDF further incorporates an entity-centroid contrastive learning module that constructs centroid-based positive samples from entity features to enhance discriminative learning. Additionally, an adaptive fusion module is employed to improve the efficiency and accuracy of dynamic fusion strategies. Extensive experiments conducted on three datasets demonstrate the effectiveness of the CL-DMDF across diverse multimodal fusion tasks.

---


### 5. [Visual Graph Scaffolds for Structural Reasoning in Large Language Models](https://arxiv.org/abs/2606.02673)

**<font color=#1a73e8>作者：</font>** Runlin Lei, Xiaokui Xiao, Zhewei Wei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphs have been used to enhance large language models (LLMs) for structured reasoning, mostly as external knowledge sources are provided to models at test time. In this paper, we take a different view: the value of graphs for LLMs lie not only in supplying information, but also in organizing reasoning. Inspired by how humans use graph-structured mind maps to organize branching and converging thoughts, we ask whether graphs can serve as an internal form of reasoning assistance. We study this question on multi-hop question answering tasks, where teacher-provided reasoning traces are rewritten as graph mind maps and used to guide a student model. Our experiments reveal a clear modality gap. When graph structures are flattened into text, their benefits become limited once direct answer hints are removed. Under this abstract guidance setting, both reasoning efficiency and answer quality degrade substantially. In contrast, visual graph guidance remains effective without direct answer clues, and its advantage persists after supervised fine-tuning and KL-based distillation. The above findings support the claim that graphs should be studied not only as external knowledge structures for LLMs, but also as visual scaffolds for organizing reasoning.

---


### 6. [Before Fusion, Ask What to Keep: Contextual Calibration of Multimodal Signals](https://arxiv.org/abs/2606.02679)

**<font color=#1a73e8>作者：</font>** Jiyuan Liu, Liangwei Nathan Zheng, Wei Emma Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal systems often benefit from combining information across language, sound, and visual streams, but this benefit is not guaranteed. A modality that is useful for one input may become distracting for another, and local feature responses within the same modality can disagree with evidence from other sources. This work investigates how to adjust multimodal representations before they are merged by a downstream predictor. We develop a compact calibration module that compares each modality with the others at the summary level, extracts cues of cross-source support and conflict, and converts these cues into instance-wise and dimension-wise modulation signals. The calibration is applied to the original modality features rather than to already fused representations, enabling the model to suppress misleading components, preserve weak but useful evidence, and emphasize responses that are better supported by the current multimodal context. The module is designed as a plug-in component and can be attached to different fusion backbones without changing their prediction heads. Across five benchmarks covering sentiment understanding, action recognition, audio-visual event detection, and audio-visual emotion classification, the proposed pre-combination calibration strategy improves performance under both sequence-based and convolutional fusion settings. Additional analyses under modality removal, synthetic corruption, training dynamics, and feature-level visualization show that calibrating signals before fusion can reduce interference from unreliable modalities and produce more stable multimodal optimization.

---


### 7. [Greener Than Humans? Environmental Attitudes in Large Language Models](https://arxiv.org/abs/2606.02741)

**<font color=#1a73e8>作者：</font>** Stefanie Kunkel, Tilman Hartwig, Marcus Voss 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in sustainability-related decision support, reporting, and public communication, yet little systematic evidence exists on the environmental attitudes embedded in their outputs. This paper develops a benchmark for evaluating environmental cognition, affect, and behavioural recommendations in LLMs and applies it to 31 widely used proprietary and open-weight models. Drawing on questions from established environmental awareness surveys and additional sustainability-related behavioural measures, we compare LLM responses 1) among models and 2) between models and human survey benchmarks from Germany. We assess their robustness across prompting conditions. We find that many LLMs align more closely with environmentally progressive attitudes than the average survey respondent, exhibiting higher levels of environmental affect and cognition and recommending behaviours associated with substantial potential CO2 reductions. At the same time, we observe no systematic relationship between sustainability-oriented responses and model origin, size, or release context. However, models exhibit contextual sensitivity, controlled by persona-based prompting and show sycophantic shifts mirroring user-specified ideological positions, which raises concerns about steerability and normative reliability in real-world deployments. Our findings provide a reusable evaluation framework for assessing sustainability-related value alignment in LLMs and highlight the importance of governance, transparency, and critical oversight as AI systems become increasingly embedded in sustainability transformations and public decision-making.

---


### 8. [Consistent Yet Wrong: Evidence Insensitivity in Spatial Vision-Language Models](https://arxiv.org/abs/2606.02742)

**<font color=#1a73e8>作者：</font>** S Divakar Bhat, Toshihiko Yamasaki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning is fundamental to robotics, autonomy, and embodied AI, yet modern vision-language models (VLMs) remain unreliable on metric distance queries. A common assumption is that consistent predictions across viewpoints reflect geometric grounding. We test this assumption and find the opposite: leading VLMs often produce view-invariant and consistent answers even when those answers are incorrect, indicating weak coupling between predictions and viewpoint-specific visual evidence.
We introduce \textbf{ViewDiag}, a controlled multi-view evaluation protocol built from Hypersim, ScanNet, and KITTI360, comprising 176 object-pair tracks across 80 scenes with 2--10 views per track. The protocol evaluates models along three axes: metric accuracy, distributional concentration, and a latent feature probe for internal collapse that distinguishes decision collapse from representation collapse. Across diverse models, we observe a consistent pattern of high prediction stability paired with substantial error, clustering in a regime characterized by strong consistency but low accuracy.
\noindent These results challenge the common use of cross-view consistency as a proxy for geometric understanding. Instead, we show that stable predictions may reflect prior-driven collapse rather than evidence-sensitive reasoning. ViewDiag provides a controlled benchmark and diagnostic framework for evaluating spatial VLMs beyond accuracy alone. The code and data can be found \href{this https URL}{here}

---


### 9. [Plan2Map: A Multimodal Benchmark for Document-Grounded Geospatial Boundary Reconstruction from Planning Records](https://arxiv.org/abs/2606.02747)

**<font color=#1a73e8>作者：</font>** Fabian Degen, Oishi Deb, Jindong Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Planning records define restrictions over geographic areas, but their source documents often provide only indirect spatial evidence rather than machine-readable boundaries. We introduce Plan2Map, a 208-case multimodal benchmark for document-grounded geospatial boundary reconstruction from UK planning records. Given only a source planning document, systems must reconstruct a valid geospatial boundary from notice text, schedules, map plates, map labels, and boundary annotations; the reference GeoJSON is held out for scoring. We propose GeoPlanAgent, a document-grounded, geospatial-tool-in-the-loop system that decomposes the task into evidence extraction, localisation, map registration, boundary segmentation, projection, and verification. On Plan2Map, GeoPlanAgent achieves 0.736 mean IoU and 0.904 median IoU, with 67.8\% of predictions at or above 0.8 IoU, substantially outperforming direct VLM-to-GeoJSON baselines. Diagnostic analysis shows that direct VLM prediction remains unreliable, while remaining errors are concentrated in localisation and map registration, and supervised boundary segmentation substantially improves pixel-level mask quality. Plan2Map provides a concrete testbed for multimodal geospatial reconstruction from public planning records. Project page: this https URL.

---


### 10. [MetaWorld: Scaling Multi-Agent Video World Model from Single-view Video Data](https://arxiv.org/abs/2606.02753)

**<font color=#1a73e8>作者：</font>** Teng Hu, Mingchun Lu, Yating Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models are a foundational generative technology for embodied AI and the Metaverse, yet existing approaches are inherently limited to a single agent observing from a single perspective. Extending these models to multi-agent settings introduces two critical challenges: data scarcity (coordinated multi-view recordings are prohibitively expensive to collect for general open-domain scenarios) and world state alignment (independently generated video streams cannot ensure that shared physical environments and events evolve consistently across views). To address these challenges, we propose MetaWorld, a novel framework that scales multi-agent video world models to open-domain environments directly from single-view videos. First, we introduce Monocular World-State Unrolling (MWSU) to explicitly decompose monocular footage into the camera operator's ego-motion and the visible subject's spatial trajectory. This camera-trajectory decomposition naturally extracts synchronized multi-agent motion data within a shared 3D space, completely bypassing the need for multi-camera setups. Second, for precise visual control, we develop the Subject-Aware World Generator to enable appearance-driven simulation conditioned on per-agent identity images. Finally, to ensure both views are grounded in the identical physical reality, we propose World-State Alignment, a per-frame inter-branch cross-attention mechanism inserted at every transformer layer of the video DiT. By jointly synchronizing the denoising process, WSA enforces both static geometric consistency and dynamic motion consistency, encouraging that the shared 3D environment and physical events remain well-aligned across both egocentric views. Extensive experiments demonstrate that MetaWorld achieves superior cross-view consistency and identity fidelity, establishing a highly scalable, physics-driven paradigm for multi-agent video world modeling.

---


### 11. [Representational Capacity: Geometric Limits on Feature Representation in Transformer Language Models](https://arxiv.org/abs/2606.02765)

**<font color=#1a73e8>作者：</font>** Alexander Guha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model dimension ($d_{model}$) is a fundamental hyperparameter in transformer language models, yet its role in setting the geometric limits of feature representation remains under-explored. Grounded in the Linear Representation and Superposition Hypotheses - which propose that models encode features as near-orthogonal directions in latent space - we develop a framework for estimating how many such directions a model can support. We first establish the embedding matrix as a measurable proxy for near-orthogonality constraints across the latent space: the boundary between meaningful token relationships and incidental similarity in the pairwise cosine similarity distribution gives a concrete estimate of the model's accepted deviation $\varepsilon$ from perfect orthogonality. Applying this metric across dozens of open-source models reveals two classes: models with high $\varepsilon$ whose embeddings lack near-orthogonal structure, and models with low $\varepsilon$ that maintain it. We then show that the standard Johnson-Lindenstrauss lemma greatly underestimates the packing efficiency of trained representations, and derive an adjusted capacity formula in which the number of near-orthogonal directions depends on the ratio of vectors to dimensions ($k/d$) rather than the raw count - a single modification that cuts prediction error by two orders of magnitude with no extra parameters. Combining these results, we define representational capacity as an upper bound on the number of distinguishable directions available for features and embeddings in a model's latent space. Capacity is exponentially sensitive to $\varepsilon$, and larger models favor tighter orthogonality constraints over maximizing raw capacity - a pattern compatible with several explanations (a stability-capacity trade-off, a ceiling on usable concepts, or confounds with model scale) that we leave to future work.

---


### 12. [GeoDrive-Bench: Benchmarking Region-Specific Multimodal Reasoning in Autonomous Driving](https://arxiv.org/abs/2606.02774)

**<font color=#1a73e8>作者：</font>** Yingzi Ma, Chaowei Xiao, Ming Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) for autonomous driving have shown promising performance, but their ability to handle region-specific traffic rules remains underexplored, raising uncertainties about their deployment across diverse global settings. We therefore introduce GeoDrive-Bench, a novel benchmark that enables the systematic investigation of VLMs' geo-culturally grounded driving reasoning. We curated 5,053 human-validated multiple-choice QA pairs across six countries covering diverse driving cultures. Specifically, we emphasize four driving tasks: perception, prediction, planning, and region reasoning. Each question requires models to infer the correct driving behavior from visual evidence and local traffic conventions without explicit country labels. Beyond evaluation, we further design a distillation algorithm that injects region-specific traffic-rule knowledge into the internal representations of VLMs, enabling models to better align visual scene understanding with local driving policies. Experiments on nine state-of-the-art VLMs show substantial performance variations across geo-driving cultures for each task, while our proposed baseline models exhibit improved geo-cultural reasoning across regions. These results suggest that current VLMs still lack robust region-aware driving intelligence and highlight GeoDrive-Bench as a diagnostic and training-oriented testbed for deployable autonomous driving foundation models.

---


### 13. [Topics as Proxies for Sociodemographics: How Conversational Context Affects LLM Answers](https://arxiv.org/abs/2606.02776)

**<font color=#1a73e8>作者：</font>** Vera Neplenbroek, Gabriele Sarti, Arianna Bisazza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When large language models (LLMs) are used in high-stakes scenarios, such as legal, medical and financial advice, even a single conversation history is enough to drive differences in outcomes between users. Prior work has demonstrated that this results in outcome disparities between sociodemographic groups, with some groups receiving more advantageous outcomes than others. In this work, we demonstrate that LLMs actually struggle to infer user sociodemographics from a single conversation history and that although there are disparities between sociodemographic groups, they are minimal in magnitude. To investigate what the main driver of these disparities is, we compare user sociodemographics to a range of (psycho)linguistic features of conversations, including conversation topic, emotions, and readability. We find that conversation topics are most predictive of LLM-generated advice within a conversational context, which, to some extent, function as proxies for sociodemographic groups and often affect advice in unpredictable ways. This is cause for concern and highlights the need for future research to better understand and, if needed, mitigate the effect of conversational context on LLM outputs in high-stakes scenarios.

---


### 14. [Cosmos 3: Omnimodal World Models for Physical AI](https://arxiv.org/abs/2606.02800)

**<font color=#1a73e8>作者：</font>** Aditi, Niket Agarwal, Arslan Ali 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Cosmos 3, a family of omnimodal world models designed to jointly process and generate language, image, video, audio, and action sequences within a unified mixture-of-transformers architecture. By supporting highly flexible input-output configurations, Cosmos 3 seamlessly unifies critical modalities for Physical AI -- effectively subsuming vision-language models, video generators, world simulators, and world-action models into a single framework. Our evaluation demonstrates that Cosmos 3 establishes a new state-of-the-art across a diverse suite of understanding and generation tasks, demonstrating omnimodal world models as scalable, general-purpose backbones for embodied agents. Our post-trained Cosmos 3 models were ranked as the best open-source Text-to-Image and Image-to-Video models by Artificial Analysis, and the best policy model by RoboArena at the time the technical report was written. To accelerate open research and deployment in Physical AI, we make our code, model checkpoints, curated synthetic datasets, and evaluation benchmark available under the Linux Foundation's OpenMDW-1.1 this https URL License at this https URL}{this http URL and this https URL . The project website is available at this https URL .

---


### 15. [ChatHealthAI: Aligning Electronic Health Record Representations with Large Language Models for Grounded Clinical Reasoning](https://arxiv.org/abs/2606.02802)

**<font color=#1a73e8>作者：</font>** Bo-Hong Wang, Baicheng Peng, Ruilin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit strong natural-language reasoning abilities for clinical decision support, but struggle to effectively model structured longitudinal electronic health records (EHRs). In contrast, EHR foundation models can learn predictive patient representations, yet lack interpretable language-based reasoning. To bridge this gap, we propose ChatHealthAI, a multimodal reasoning framework that aligns structured EHR representations from a pretrained EHR foundation model with the semantic space of a frozen LLM through a task-aware resampler. By integrating longitudinal patient representations with refined clinical event descriptions, ChatHealthAI enables clinically grounded natural-language reasoning while maintaining accurate patient prediction. We evaluated ChatHealthAI on three clinical predictive tasks from the EHRSHOT benchmark. Results show that ChatHealthAI improves reasoning quality and interpretability while preserving competitive predictive performance. These findings highlight the potential of integrating EHR foundation models with pretrained LLMs for interpretable clinical prediction.

---


### 16. [Automated Report-Derived Oncology VQA Benchmark for Evaluating Vision-Language Models on 3D Medical Imaging](https://arxiv.org/abs/2606.02809)

**<font color=#1a73e8>作者：</font>** Bo Liu, Hanxue Gu, Xiangru Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating vision-language models (VLMs) on medical images requires benchmarks that are clinically grounded, scalable, and controlled for evaluation confounds. Existing public benchmarks are limited in scale, manually annotated, or potentially leaked into VLM pretraining corpora. We present an automated agent-driven pipeline that generates multiple-choice VQA datasets directly from paired private radiology reports and 3D oncology imaging, producing two complementary question types: RADS-style questions deterministically derived from clinician-defined reporting schemas, and radiology report-derived questions generated by an LLM from radiologist findings and verified against the source report. Applied to four in-house cancer cohorts, the pipeline yields an instance-contamination-controlled benchmark without per-question human annotation. Zero-shot evaluation of six VLMs reveals no dominant model and substantial headroom across all cells. A blind ablation reveals that visual reliance is highly dataset-specific: liver Report-derived questions genuinely require the image, while Lung CT is essentially solvable without it - the leading closed model exceeds its sighted accuracy on Lung CT when blinded - indicating that even private clinical data does not guarantee a contamination-controlled read of visual capability. The pipeline is released as an open agent skill for in-house redeployment.

---


### 17. [Traj-Evolve: A Self-Evolving Multi-Agent System for Patient Trajectory Modeling in Lung Cancer Early Detection](https://arxiv.org/abs/2606.02812)

**<font color=#1a73e8>作者：</font>** Sihang Zeng, Matthew Thompson, Ruth Etzioni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modeling patient trajectories from longitudinal electronic health records (EHRs) requires reasoning over sparse, noisy, and long-context multimodal sequences. Existing LLM-based multi-agent systems address context length but process patients in isolation, failing to mirror how clinicians leverage accumulated experience from similar prior cases. We present Traj-Evolve, a self-evolving multi-agent system with two complementary evolving mechanisms. First, an Experience Pool (ExPool) acts as a non-parametric memory, indexing rejection-sampled reasoning traces to retrieve similar patients as few-shot contexts. Second, multi-agent reinforcement learning (MARL) via reward-ranked fine-tuning parametrically optimizes inter-agent and agent-memory collaboration. A leave-one-out cross-retrieval strategy unifies the two, aligning training- and inference-time behavior under retrieval augmentation. On a lung cancer prediction task utilizing up to five years of multimodal EHRs, Traj-Evolve outperforms 9 strong baselines on the overall population and a challenging never-smoker population. Analysis of the evolving dynamics highlights three key findings: (1) expanding the ExPool shifts optimal retrieval from diverse to specific samples; (2) under MARL, the manager agent's prediction loss converges quickly while the worker agents' temporal reasoning continues to benefit from more verified patients; and (3) the two mechanisms are complementary on the predicted risk, where ExPool improves specificity while MARL improves sensitivity.

---


### 18. [Qift: Shift-Friendly No-Zero W2 Post-Training Quantization for Rotated W2A4/KV4 LLM Inference](https://arxiv.org/abs/2606.02823)

**<font color=#1a73e8>作者：</font>** Chi-Wei Huang, Chia-Chi Tsai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two-bit weight quantization is attractive for memory-efficient LLM inference, but the standard W2 level set {-2,-1,0,+1} often collapses under aggressive W2A4/KV4 settings. We study the scalar level-set geometry of two-bit weights in a Hadamard-rotated quantization pipeline. Conventional asymmetric W2 substantially improves over the standard level set, indicating that W2A4 failure is not only a bit-width problem but also a reconstruction-level problem. Across all 224 linear modules in each of LLaMA-2-7B and LLaMA-3.1-8B, pretrained weights are already nearly zero-centered, while Hadamard rotation primarily Gaussianizes their standardized shape: excess kurtosis and Q-Q error drop by orders of magnitude. Based on this approximate zero-centered Gaussian-like source model, we propose Qift, a fixed no-zero W2 level set for rotated W2A4/KV4 inference. The main level set is {+/-0.5, +/-1.5}, equivalently {+/-1, +/-3} under a half-scale reparameterization; a power-of-two variant uses {+/-1, +/-4} for sign-and-shift decoded weight application. Qift redesigns the fixed two-bit code-to-level mapping and is training-free, learned-codebook-free, group-grid-free, and zero-point-free, retaining the standard per-channel scale. A scale-invariant ratio analysis identifies an effective inner/outer centroid ratio range of 0.25 to 0.33, explaining why mirror no-zero (MNZ), Lloyd, NF2, and PoT-MNZ perform well while {+/-1, +/-2} does not. On both models, the no-zero level sets consistently improve pure W2A4 perplexity, L-layer mixed W2/W4 perplexity, downstream accuracy, and GPTQ residual behavior over the standard W2 level set. At L=16 mixed precision, they substantially narrow the gap to W3A4 while keeping half of the transformer layers at two-bit precision, giving a simple, source-aware, and deployment-friendly alternative to more complex learned W2 codebooks.

---


### 19. [Thinking Past the Answer: Evaluating Harmful Overthinking in Large Reasoning Models](https://arxiv.org/abs/2606.02835)

**<font color=#1a73e8>作者：</font>** Simone Caldarella, Davide Talon, Rahaf Aljundi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) improve performance by generating explicit intermediate reasoning traces through increased test-time compute, yet the assumption that longer reasoning is consistently beneficial remains under-examined. While recent evidence shows that additional reasoning can lead models to overthink, we ask: "Once a model has reached the correct answer, does further reasoning refine the solution, or deviate from it?" To study the dynamics after correctness, we introduce a prefix-level trajectory evaluation protocol grounded in reasoning sufficiency, defining the minimum reasoning budget required for a model to first generate the correct answer. This allows us to disentangle verbose overthinking, where additional reasoning is redundant but harmless, from harmful overthinking, where continued reasoning destabilizes an already-correct trajectory. Starting from multimodal benchmarks, we find that many instances considered reasoning-intensive require surprisingly little reasoning. Moreover, stopping at the first correct prefix improves accuracy over standard reasoning up to 21%, revealing that current models are limited not only by their ability to reason, but also by their inability to stop at the right time. Furthermore, while common efficiency strategies like early stopping substantially reduce verbose overthinking (up to 50%), they fail to mitigate harmful overthinking. Failure analysis reveals that correctness deviations are mainly driven by logical drift and visual reinterpretation. Finally, we show that our findings generalize to language-only reasoning benchmarks, highlighting harmful overthinking as a broader reliability risk. Code available at this https URL.

---


### 20. [Fixing FOLIO and MALLS: Verified Annotations and an LLM-assisted Framework to Focus Human Relabeling](https://arxiv.org/abs/2606.02837)

**<font color=#1a73e8>作者：</font>** Andrea Brunello, Cristian Curaba, Luca Geatti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate translation from Natural Language to First-Order Logic (NL-to-FOL) underpins neurosymbolic AI systems and Natural Language Inference (NLI), making the quality of NL-to-FOL benchmarks essential -- yet these datasets have never been rigorously audited. Our first contribution is to present a systematic human inspection of the validation split of \textsf{FOLIO} and a subset of \textsf{MALLS} test instances, finding that approximately 39% and 36% of entries, respectively, contain incorrect FOL formalizations (i.e., ground truth labels), with additional rates of ambiguous NL sentences (16.4% and 48%) and incorrect NLI labels in \textsf{FOLIO} (8.4%). Our second contribution is to develop and release corrected ground truths for such datasets, showing that annotation errors distort model evaluation on a reference benchmark task: testing three state-of-the-art LLMs (Gemma~4 31B-it, Qwen3-30B-A3B, and GPT-4o-mini) with the corrected ground truths yields accuracy gains from +9 to +22 percentage points. Motivated by these findings, we propose an LLM-based framework to support humans in manual reviewing NL-to-FOL datasets. By directing reviewers toward the most error-prone instances, we empirically show that it is possible to achieve 90% dataset accuracy after reviewing fewer than 24% of instances, compared to over 70% required by unguided review. We release all human-verified annotations and the code for our framework.

---


### 21. [Spectral-Progressive Thought Flow for Lightweight Multimodal Reasoning](https://arxiv.org/abs/2606.02842)

**<font color=#1a73e8>作者：</font>** Yixian Shen, Zhiheng Yang, Qi Bi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal spatial reasoning often relies on long chains of intermediate textual and visual thoughts, where accumulating visual tokens and dense cross-modal attention incur substantial computation and memory overhead. To address this challenge, we propose Spectral-Progressive Thought Flow (SpecFlow), a novel lightweight multimodal spatial reasoning framework that represents intermediate visual thoughts in a fixed-size discrete cosine space. By exploiting strong energy compaction, SpecFlow preserves global layout and relational structure while introducing high-frequency details only when increased spatial precision is required. To align visual state evolution with linguistic intent, classifier-free guidance enables autoregressive textual thoughts to steer flow-based updates of the visual workspace/state without expanding the context. As a result, SpecFlow maintains a bounded visual workspace whose updates depend only on the current visual state and accumulated textual trace, enabling long-horizon inference with stable latency and memory usage independent of reasoning depth. Empirical results show that SpecFlow achieves competitive or superior reasoning performance while reducing computation and KV cache costs by up to 2.1 times.

---


### 22. [GRZO: Group-Relative Zeroth-Order Optimization for Large Language Model Fine-Tuning](https://arxiv.org/abs/2606.02857)

**<font color=#1a73e8>作者：</font>** Liyan Tan, Yequan Zhao, Yifan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) optimization is a memory-efficient alternative to backpropagation for fine-tuning large language models, but its deployment is limited by the high variance of gradient estimation. We propose GRZO, a Group-Relative Zeroth-Order optimizer that draws one pseudo-independent perturbation per mini-batch example and aggregates the per-example losses through group-relative normalization, raising the effective gradient-direction count from one to the batch size at no additional forward cost while preserving inference-level memory. We prove that GRZO is directionally unbiased with variance shrinking proportionally to the batch size, yielding a tighter nonconvex convergence bound than MeZO. Across RoBERTa-large, Llama3-8B, and OPT-13B over multiple tasks, GRZO improves average accuracy on Llama3-8B by $+3.0$ over MeZO at $23\%$ lower peak GPU memory; as a drop-in replacement for the MeZO core, it lifts sparse, low-rank, and quantized ZO variants by $+6.0$ on average.

---


### 23. [Toward a Modular Architecture for Embedded AI Agent Systems at the Edge](https://arxiv.org/abs/2606.02862)

**<font color=#1a73e8>作者：</font>** Marcus Rüb, Michael Gerhards  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rise of Large Language Models (LLMs) has enabled agentic AI capable of complex reasoning and tool use; however, deploying such autonomy in pervasive computing environments remains challenging due to the strict memory and energy constraints of embedded microcontrollers. Existing frameworks typically assume server-class resources or continuous connectivity, leaving a gap for deeply embedded systems. This paper proposes a modular reference architecture for Embedded Agent Systems that bridges the divide between deterministic real-time control and agentic intelligence.
We introduce a tiered design that decouples On-Device Agents - executing highly compressed neural networks and rule-based logic for low-latency, privacy-critical tasks - from Cloud-Augmented Agents that leverage Small Language Models (SLMs) for higher-level reasoning and planning. A key contribution is the integration of a cross-cutting Governance Layer, ensuring observability, policy enforcement, and safety across distributed fleets of autonomous devices. Rather than presenting purely empirical benchmarks, we analyze architectural design principles and trade-offs regarding latency, energy, and reliable execution in resource-constrained environments.

---


### 24. [The Epi-LLM Framework: probing LLM behavioral priors through epidemiological agent-based models](https://arxiv.org/abs/2606.02867)

**<font color=#1a73e8>作者：</font>** Petra Ferenz, Ava Keeling, Tobias O'Keefe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Human behaviour during epidemics affects infectious disease dynamics, but quantifying this remains deeply challenging. Here we introduce the Epi-LLM framework: a novel integration of agent-based modelling, real-life epigames, and large language models (LLMs) in which a synthetic society of agents reasons and adapts dynamically over an outbreak contact network. Comparing synthetic agent behaviour against a no-intervention SEIR baseline and human participant data from the AUIB epigame study, we find that LLM agents across four different architectures reduced peak active infections, with quarantine compliance peaking at 58-65% on day six of the 15-day simulation. A binomial generalised linear model showed that perceived health severity was the strongest predictor of quarantine behaviour ($\beta = 0.33, p = 0.002$), yielding a pseudo-$R^2$ of 0.055, comparable to the 0.072 observed in the human trial. LLM architecture is a key determinant of epidemic dynamics: low-variance architectures offer greater internal validity for testing behavioural rules, while high-variance models may better represent real-world decision-making. Geographic labels alone do not induce culturally differentiated behaviour; explicit attitudinal parameterisation is required. This proof-of-principle work lays the groundwork for deploying the Epi-LLM framework as a scalable, risk-free simulation environment for pandemic preparedness research.

---


### 25. [Adaptive Latent Agentic Reasoning](https://arxiv.org/abs/2606.02871)

**<font color=#1a73e8>作者：</font>** Dongwon Jung, Peng Shi, Yi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models improve performance by generating extended chain-of-thought (CoT) reasoning, but this behavior becomes inefficient when applied to LLM agents. Current LLM agents often generate verbose textual reasoning at every decision step and allocate reasoning effort nearly uniformly across turns, leading to substantial inefficiency in multi-turn agentic trajectories. We propose Adaptive Latent Agentic Reasoning (ALAR), a dual-mode framework that uses compact latent reasoning for routine turns and selectively escalates to explicit chain-of-thought when deeper deliberation is needed. ALAR learns latent reasoning by using the agent's actions as supervision anchors and is further optimized to use latent reasoning when it is sufficient for task success and reserve explicit CoT for harder decisions. Experiments on agentic search and tool-use benchmarks show that ALAR maintains comparable or better task accuracy while substantially reducing generated tokens by up to 43.6% in search and 84.6% in tool use. These results demonstrate that ALAR improves the accuracy-efficiency trade-off of LLM agents by reducing unnecessary textual reasoning while preserving explicit deliberation for harder decision steps.

---


### 26. [LLM-Assisted Reranking to Operationalize Nuanced Objectives in Recommender Systems](https://arxiv.org/abs/2606.02883)

**<font color=#1a73e8>作者：</font>** Amir Ghasemian, Homa Hosseinmardi, Upasana Dutta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recommender systems have grown from content-organization tools into sophisticated systems that shape daily behavior. By controlling what we see, they shape what we perceive, raising concerns about filter bubbles, radicalization, polarization, and social inequality. Large language models (LLMs) enable more powerful personalization, intensifying these dynamics. Yet most recommenders are tuned for engagement or limited accuracy metrics, with little attention to broader social implications, e.g. how personalization reshapes exposure in socially consequential domains. We investigate whether LLM-assisted reranking, while improving personalization, inadvertently amplifies exposure to ideologically extreme or conspiratorial political content, a risk theorized but not empirically characterized in news recommendation. Using real news-consumption histories, we rerank YouTube's sidebar candidates through zero-shot, instruction-based prompting. We compare a baseline prompt with a constrained variant that preserves topical relevance and broadens ideological exposure while reducing conspiratorial or extreme content. Without constraints, reranking strengthened personalization but increased exposure to conspiratorial and extremist material for users whose histories contained such content. Lightweight prompt-level regularization reduced promotion of extreme content and increased ideological diversity, with modest relevance loss. Synthetic experiments suggest that LLMs rerank via statistical regularities in language rather than semantic understanding of ideology, clarifying why naive prompts amplify these patterns and why regularization can reshape them. Together, our results highlight the power of LLMs to operationalize contextual nuance in high-stakes recommendation, and the need to evaluate LLM-assisted personalization beyond accuracy and treat prompt design as a value-laden rather than neutral default.

---


### 27. [Linear Probes Detect Task Format, Not Reasoning Mode in Language Model Hidden States](https://arxiv.org/abs/2606.02907)

**<font color=#1a73e8>作者：</font>** Subramanyam Sahoo, Vinija Jain, Aman Chadha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear probing of large language model (LLM) hidden states is widely used to claim that models learn distinct representations for different reasoning types. We test this by probing Qwen3-14B on three benchmarks spanning the classical trichotomy: LogiQA 2.0 (deductive), ARC-Challenge (inductive), and $\alpha$NLI (abductive). At layer 32 of 40, linear probes achieve 100\% cross-validated accuracy with well-separated geometry (intrinsic dimensionalities: 20.6, 28.5, 33.6; convex hull contamination $\leq$1.5\%). However, this separation is entirely driven by format confounds. Residualizing source identity, option count, and response length reduces accuracy to chance. Trace-anchor similarity indicates largely shared reasoning across tasks (42.5\% agreement vs.\ 33.3\% chance), and causal steering with random controls ($n=20$) shows no functional link between geometry and reasoning mode ($p=0.286$). Thus, high probe accuracy reflects task format rather than computational structure, motivating routine format deconfounding in mechanistic interpretability.

---


### 28. [Large AI Models in Dental Healthcare: From General-Purpose Systems to Domain-Specific Foundation Models](https://arxiv.org/abs/2606.02914)

**<font color=#1a73e8>作者：</font>** Sema Helali, Lina Abu Nadab, Sausan Alqawas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Oral diseases affect nearly 3.5 billion people worldwide, yet the comparative clinical potential of large-scale AI models in dentistry remains poorly understood. Three distinct model categories have emerged: language-generative models, discriminative vision foundation models, and dental-specific foundation models, with no unified review examining their relationships and collective limitations.
Methods: Following PRISMA-ScR guidelines, we systematically searched four databases (PubMed, Google Scholar, Scopus, arXiv), screened independently by two reviewers. After applying inclusion/exclusion criteria, 97 studies (2020-2026) were included. We propose a two-dimensional classification framework organizing models by architectural paradigm and dental specialization degree.
Results: Language-generative models excel at text-based tasks (clinical reasoning, licensing exams, patient communication) but show inconsistent performance on image-dependent diagnostics. Adapted SAM and CLIP variants achieve strong tooth segmentation and lesion detection results. Dental-specific models (DentVFM, DentVLM, OralGPT) demonstrate strongest performance on complex multimodal tasks. Integrated pipelines consistently outperform single-model approaches. A data asymmetry is observed: dental-specific pretraining concentrates almost entirely in the vision domain, reflecting scarce large-scale dental text corpora.
Conclusions: General-purpose and dental-specific models play complementary roles; the most effective systems combine both within structured pipelines. Safe autonomous deployment requires resolving three persistent barriers: hallucination in generative models, limited annotated dental datasets, and absent standardized clinical evaluation benchmarks.

---


### 29. [BYORn: Bootstrap Your Own Responses to Defend Large Vision-Language Models Against Backdoor Attacks](https://arxiv.org/abs/2606.02947)

**<font color=#1a73e8>作者：</font>** Ivan Sabolić, Marin Oršić, Josip Šarić 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning is the predominant approach for adapting autoregressive vision-language models to downstream tasks. Recent work has shown that this paradigm is highly vulnerable to backdoor attacks, and that existing defenses are ineffective in open-ended generation settings. In response, we propose BYORn, a backdoor-robust fine-tuning framework motivated by the observation that poisoned target responses are often semantically implausible given the corresponding image-text inputs and a pretrained model. BYORn identifies such misaligned responses and dynamically replaces them with alternative responses generated by the model, thereby breaking the correlation between triggers and target outputs. The resulting objective gradient corresponds to the gradient of the empirical estimate of the population risk upper bound over the clean data distribution. Empirically, BYORn consistently improves robustness to backdoor attacks while preserving clean-task performance, establishing a new trade-off frontier between generalization and attack success rate. Finally, we demonstrate that BYORn remains effective against adaptive attacks specifically designed to circumvent the proposed defense.

---


### 30. [Linguistic Productivity in Large Language Models: Models Coerce, but do not Preempt](https://arxiv.org/abs/2606.02953)

**<font color=#1a73e8>作者：</font>** Claire Bonial, Claire Benet Post, Laura Michaelis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Usage-based theories of grammars posit that creative productivity of the structures of language is both bolstered and constrained by two distinct frequency signals: entrenchment, stemming from high frequency usage, and preemption, stemming from having never observed a particular linguistic structure in a context where one might expect that structure to appear. Large Language Models are also usage-based, in the sense that the structures of language are learned through exposure to vast amounts of text. Here, we test whether or not the opposing statistical forces of entrenchment and preemption also encourage and constrain linguistic productivity in LLMs. We demonstrate across model architectures that larger models recognize and can reproduce with nonce words constructional productivity (entrenchment) in cases of coercion, wherein the broader constructional context coerces an atypical interpretation of a lexical item. However, we also show that even the largest models do not extend negative evidence to novel language, and statistical preemption does not enable models to avoid overgeneralization of patterns that are semantically felicitous, but never observed in data.

---


### 31. [Fast-dLLM++: Fréchet Profile Decoding for Faster Diffusion LLM Inference](https://arxiv.org/abs/2606.02955)

**<font color=#1a73e8>作者：</font>** Siva Rajesh Kasa, Yasong Dai, Sumit Negi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models promise parallel token generation, yet inference remains bottlenecked by deciding which masked tokens can be safely committed together. Fast-dLLM addressed this with KV caching and confidence-guided parallel decoding, but its decoding theory uses a homogeneous high-confidence assumption that effectively reduces each candidate set to its weakest selected token. We argue that this leaves speed on the table because real decoding steps exhibit heterogeneous confidence profiles. We propose \textbf{Fast-dLLM++}, a training-free extension that introduces \emph{Fréchet profile decoding}: selecting parallel commit sets from the full sorted confidence profile rather than a single worst-case confidence. The resulting rule is a heterogeneous-confidence generalization of Fast-dLLM's factor selector and it recovers the previous rule exactly in the equal-confidence case and adds a provable \emph{heterogeneity bonus} when the selected tokens have uneven confidences. Fast-dLLM++ leaves the model, diffusion process, and cache implementation entirely unchanged, making it a drop-in replacement for existing Fast-dLLM decoding. Experiments on GSM8K, MATH, HumanEval, and MBPP with the LLaDA-8B model show that the theoretical improvement translates directly into empirical gains: profile-aware selection improves the accuracy--throughput frontier by exploiting safe parallelism that weakest-token rules miss, achieving up to 37\% higher throughput at comparable accuracy. Our anonymous code release is at this https URL.

---


### 32. [The Road Ahead in Autonomous Driving: The KITScenes Multimodal Dataset](https://arxiv.org/abs/2606.02956)

**<font color=#1a73e8>作者：</font>** Richard Schwarzkopf, Fabian Immel, Alexander Blumberg 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing autonomous driving datasets have enabled major progress, but fall short in sensor fidelity, map completeness, or geographic diversity. We present KITScenes Multimodal, a European dataset built around high-fidelity sensors and maps. Our fully synchronized sensor suite combines high-resolution global-shutter cameras, long-range lidar beyond 400m, 4D imaging radar, and redundant GNSS/INS localization. Our HD maps are, to our knowledge, the most complete of any sensor dataset, validated through autonomous driving trials on open-source software. For the first time in a public dataset, all driving-relevant traffic elements, such as traffic lights, are mapped in 3D to a reprojection-accurate level with full topological connectivity. Recorded in cities with irregular street layouts and mixed traffic modes, our dataset complements existing datasets by broadening the available geographic diversity. We also introduce four benchmarks, each advancing spatial learning for embodied AI: online HD map construction, long-range depth estimation, novel view synthesis, and end-to-end driving. Project page: this https URL

---


### 33. [Gate AI: LLM Security Benchmark Evaluation Methodology and Results](https://arxiv.org/abs/2606.02959)

**<font color=#1a73e8>作者：</font>** Ryle Goehausen, Marcus Sousa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Published evaluations of prompt-injection and jailbreak detectors for Large Language Models often suffer from two systematic weaknesses: per-dataset threshold tuning and undisclosed operating points. We describe an evaluation harness that addresses both. The detector under evaluation is scored across 16 public benchmarks (12,111 samples) using 5-fold cross-validation. StratifiedKFold (by row) is the headline pass; a parallel StratifiedGroupKFold pass over a composite key (parent-prompt id plus MinHash + LSH near-duplicate clusters at Jaccard $\gtrsim 0.8$) runs alongside it as a leakage-premium diagnostic. A single global operating point is selected on the held-out folds (max F1 subject to FPR $\leq 1\%$) and applied uniformly to every dataset, so per-dataset results reflect one threshold rather than per-benchmark optimisation. Generalisation is examined through a battery of diagnostics (leave-one-dataset-out cross-validation, a random-label control, adversarial validation, permutation feature importance, length-bias correlation, classifier-head agreement, cross-source near-duplicate detection, threshold transferability, train-vs-OOF agreement, and a paraphrase-invariance probe), most with a quantitative pass threshold and the remainder with a stated failure mode. For every external comparison, the detector's threshold is re-tuned to the competitor's published false-positive rate so head-to-head values are evaluated at matched operating points.

---


### 34. [KForge: LLM-Driven Cross-Platform Kernel Generation for AI Accelerators](https://arxiv.org/abs/2606.02963)

**<font color=#1a73e8>作者：</font>** Taras Sereda, Burak Bartan, Ankita Nayak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production inference increasingly targets a heterogeneous mix of accelerators. Agentic pipelines interleave reasoning, tool calls, and multi-agent coordination, each with distinct compute and memory profiles. For optimal efficiency, each stage should run on the accelerator best suited to it. This creates a systems challenge: each pipeline now requires high-performance kernels across a growing set of hardware backends and programming models. Writing these kernels by hand is time-consuming, demands deep low-level expertise, and does not scale as kernel complexity grows. Recently, Large Language Models (LLMs) have been leveraged for automatic kernel generation, but challenges in low-level code generation and cross-backend generalization persist. We present KForge, a cross-platform framework built around an iterative refinement loop driven by two collaborating LLM-based agents: a generation agent that produces and progressively refines kernels using compilation and correctness feedback, and a performance-analysis agent that interprets profiling data, from programmatic APIs to GUI-based tools, and emits recommendations that steer the next round of synthesis. The loop alternates between functional passes, which drive a candidate to correctness, and optimization passes, which close the performance gap to hand-tuned baselines. We evaluate KForge on two backends with very different baseline reference availability. On NVIDIA B200, KForge achieves a 2.12$\%$ improvement in end-to-end throughput compared to TensorRT-LLM on the gpt-oss-20b inference speed benchmark. On Intel Arc B580, KForge generates Triton kernels achieving a 5.13$\times$ geometric mean speedup over the faster of PyTorch eager and this http URL on 37 GEMM + tail-ops workloads from KernelBench Level 2, primarily via operator fusion and mixed-precision execution.

---


### 35. [A Benchmarking Framework for Multimodal User Interface Toolkits: Comparing Modality Coverage, Developer Workflow, and Experimental Support](https://arxiv.org/abs/2606.02977)

**<font color=#1a73e8>作者：</font>** Ariton Verush  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multimodal user interfaces increasingly combine speech, gesture, vision, gaze, touch, biosignals, and other sensor data. Recent toolkits from the past five years, such as Geno, Multisensor-Pipeline (MSP), ReactGenie, and EmoSync, aim to make it easier for developers to prototype such interfaces, while older work such as WAMI shows how early web-based multimodal systems were conceived. Yet the field still lacks a systematic and reusable way to compare what these toolkits actually support, how much implementation work they offload from developers, and which evaluation strategies are appropriate for them. This paper reframes an HCI seminar draft into a benchmarking framework paper for multimodal user interface toolkits. Rather than reporting completed empirical results, it proposes a structured benchmark based on document analysis, technical comparison, and a future developer-based evaluation. The framework is organized around three dimensions: modality coverage and interaction abstraction, developer experience and workflow, and experimental and integration support. The paper illustrates the framework through five representative toolkits: Geno, MSP, ReactGenie, WAMI, and EmoSync. The contribution is a reusable benchmark template that future researchers can instantiate with empirical measurements, developer studies, and additional multimodal toolkits.

---


### 36. [A Locally Deployed RAG-Based Academic Advising System for Course Selection](https://arxiv.org/abs/2606.02983)

**<font color=#1a73e8>作者：</font>** Feng Li, Yoritaka Iwata  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The correct sequence of courses in the curriculum based on prerequisites between courses is of great importance for students to develop their knowledge and skills holistically. However, students crafting this sequence in isolation frequently struggle with recognition limitations and information overload that leads to confusion. Simultaneously, education institutions encounter difficulties in providing adequate academic advice for the correct sequence due to limited education resources. To address these challenges, we propose a locally deployed RAG-based academic advising system grounded in syllabus information. By combining large language models with retrieval from structured syllabus data, the system is designed to support course selection, prerequisite understanding, and personalized study planning in a privacy-preserving manner.

---


### 37. [Pretraining Language Models on Historical Text](https://arxiv.org/abs/2606.02991)

**<font color=#1a73e8>作者：</font>** Xiaoxi Luo, Zachary Shinnick, Niclas Griesshaber 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce TypewriterLM, a 7.24B History language model (LM) trained exclusively on English text predating 1913. Developing History LMs requires addressing challenges in data quality and availability, preventing temporal leakage, designing temporally consistent post-training pipelines, and constructing reliable evaluations. To address these issues, we construct TypewriterCorpus, a 54B-token historical corpus collected from diverse archival and linguistically annotated sources with extensive data cleaning and leakage mitigation procedures. Furthermore, we introduce lexically grounded instructing tuning, a post-training framework that constraints responses to remain directly grounded in historical source documents. Using this framework we construct two historical instruction tuning datasets: History-LIMA and History-SelfInstruct. To evaluate capability and temporal consistency, we introduce History-Event, a benchmark suite for evaluating competence, temporal grounding and data leakage. We release TypewriterLM and all associated resources to support future research on historical language models.

---


### 38. [CoughSense: Five-Class Respiratory Disease Classification via Whisper Encoder Fine-Tuning and Dual-Encoder Cross-Attention Fusion with Balanced Contrastive Learning](https://arxiv.org/abs/2606.02998)

**<font color=#1a73e8>作者：</font>** Nikhil Vincent  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated cough analysis offers a path to low-cost respiratory screening, but most existing work stops at binary COVID-19 detection. A practical tool needs to tell apart several respiratory conditions from one cough recording on a consumer smartphone. We present CoughSense, a system that sorts cough recordings into five classes. These are healthy, COVID-19, asthma or respiratory condition, bronchitis, and pneumonia. We aggregated 18,301 recordings from four public datasets (Coswara, CoughVID, Virufy, and the West China Hospital Pediatric Cough Dataset) and used the OpenAI Whisper encoder as a pretrained backbone for cough disease classification. The main contribution is active-frame QKV attention pooling, which restricts attention to the first 200 of 1500 encoder tokens. This avoids the silence-dilution problem that arises because a 3-second cough fills only 150 tokens of Whisper's 30-second input window. Other training parts handle the 19 to 1 class imbalance and the four-dataset domain shift. These include WeightedRandomSampler, SpecAugment, Balanced Mixup with forced minority pairing, a supervised contrastive auxiliary loss, FiLM symptom conditioning, and gradient-reversal domain adaptation. A dual-encoder model fuses Whisper with the OPERA-CT respiratory foundation model through cross-attention. CoughSense (Whisper-tiny, 8.6M parameters) reached 82.3 percent balanced accuracy on five-fold cross-validation (macro-F1 of 0.817, AUC of 0.941). It beat an ImageNet-pretrained EfficientNet-B2 by 11.1 points and a ViT trained from scratch by 29.6 points. All five classes passed 74 percent recall and four of five passed 80 percent. The dual-encoder model reached 85.4 percent balanced accuracy. Active-frame pooling is the largest single contributor across all ablation components at 5.1 points, which should help any short-audio task using Whisper as a backbone.

---


### 39. [How Quantization Changes Interpretable Features: A Sparse Autoencoder Analysis of Language Models](https://arxiv.org/abs/2606.03002)

**<font color=#1a73e8>作者：</font>** Evan Duan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization is a standard path to deploying large language models, and a quantized model is typically judged acceptable when its perplexity or downstream accuracy stays close to the full-precision original. Whether the model still computes in the same way, or whether the interpretable features identified in the full-precision model survive weight rounding, is rarely tested, even as safety audits and steering interventions increasingly rely on those features. We ask whether sparse autoencoder (SAE) features extracted from a dense full-precision model remain faithful once that model is quantized. Using a frozen SAE as a fixed measurement basis, we encode full-precision and round-to-nearest (RTN) quantized activations on identical tokens and quantify per-feature survival by Pearson correlation, sweeping bit-widths from INT8 to INT4 on Pythia-70M and Gemma-2-2B. We find that feature survival is graded: features degrade systematically rather than failing all at once, with 62.4 percent of active features surviving at INT6 on Pythia-70M and 51.3 percent surviving at INT6 on Gemma-2-2B, and with most non-survivors blurred rather than destroyed. Survival is predictable from full-precision statistics alone, with cross-validated AUCs of 0.92 to 0.97 and peak activation as the strongest marginal predictor. Critically, task metrics can miss this damage: on Gemma-2-2B, INT7 improves perplexity while degrading 18.7 percent of features. Finally, quantization and matched-perplexity magnitude pruning damage strongly overlapping feature sets, with Jaccard overlap of 0.79 to 0.86 and damage-score Spearman correlation of 0.98, suggesting a shared mode of compression-induced vulnerability. These results show that behavioral parity is insufficient evidence that interpretability findings transfer to quantized deployments, motivating feature-level audits of compression.

---


### 40. [MUSE: A Unified Agentic Harness for MLLMs](https://arxiv.org/abs/2606.03005)

**<font color=#1a73e8>作者：</font>** Jianglin Lu, Hailing Wang, Xu Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress, multimodal large language models (MLLMs) still fail on tasks that humans solve effortlessly, such as navigating a grid maze from a screenshot or selecting the correct puzzle piece. Rather than retraining the model, we ask a complementary question: how much capability can be elicited from a frozen MLLM purely by improving the execution scaffold around it? We introduce MUSE, a multimodal unified structured execution harness that wraps any off-the-shelf MLLM with composable modules for task representation, visual processing, perception tool use, structured parsing, deterministic verification, and verifier-guided repair, without any model retraining. We evaluate MUSE across diverse benchmarks spanning visual spatial planning, visual perception, multimodal reasoning, and fine-grained visual discrimination, using multiple state-of-the-art MLLMs. MUSE delivers consistent gains over the bare model in all settings, with the largest jumps on challenging instances. Further analysis reveals that many MLLM failures arise from harness-level shortcomings rather than fundamental model deficits, and can be addressed through verifier-guided repair without touching the model. These findings highlight the agentic multimodal harness as a critical yet underexplored design dimension, offering an orthogonal avenue for improving MLLMs beyond model-centric optimization.

---


### 41. [Hint-Guided Diversified Policy Optimization for LLM Reasoning](https://arxiv.org/abs/2606.03021)

**<font color=#1a73e8>作者：</font>** Zhiyu Cao, Kaixin Wu, Mingjie Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent developments in Large Language Models (LLMs) have showcased impressive reasoning capabilities, with Reinforcement Learning with Verifiable Rewards (RLVR) being a promising enhancement strategy. However, existing reward mechanisms are constrained to the outcome-level correctness and lack explicit signals to guide the model to consider diverse solutions. In contrast, human problem solving typically involves evaluating multiple potential approaches and selecting the most reliable solution, a cognitive process that current RLVR frameworks do not explicitly incentivize. Inspired by this, we propose Hint-Guided Diversified Policy Optimization (HDPO), allowing the model to first list all potential candidate solution outlines as hints and then select the most reliable one for further reasoning. HDPO comprises two stages of Cold Start for Structured Reasoning and Hint-Guided Diversified Reinforcement Learning to incentivize the model to generate diverse and reliable solutions following the ``propose-select-think'' trajectory. Experimental results show that HDPO effectively boosts LLM reasoning and enhances the diversity of candidate solutions as well as the LLM's ability to identify reliable solutions.

---


### 42. [Hallucinations as Orthogonal Noise: Inference-Time Manifold Alignment via Dynamic Contextual Orthogonalization](https://arxiv.org/abs/2606.03022)

**<font color=#1a73e8>作者：</font>** Mingkuan Zhao, Wentao Hu, Tianchen Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination in Large Language Models (LLMs), characterized by the generation of content inconsistent with contextual facts or logical constraints -- remains a persistent challenge for reliable deployment. In this work, we address this issue through a geometric framework rooted in the linear representation hypothesis. We propose that hallucinations manifest as orthogonal noise relative to the semantic manifold of the residual stream. Specifically, we hypothesize that while attention heads ideally propagate information congruent with the context subspace, hallucinations arise when specific heads introduce components orthogonal to this subspace, disrupting the coherence of the latent representation. Based on this formulation, we introduce Dynamic Contextual Orthogonalization (DCO), an inference-time intervention method. DCO utilizes the input residual stream as a dynamic context anchor to perform orthogonal decomposition on attention head outputs. To distinguish between context-aligned semantic updates and divergent noise, DCO employs a layer-wise Z-score suppression mechanism that selectively attenuates outlier orthogonal components based on statistical distributions. Evaluations on Llama-3-8B and 70B across benchmarks such as XSum, NQ-Swap, and IFEval demonstrate that DCO achieves superior contextual faithfulness compared to state-of-the-art intervention baselines. Furthermore, DCO maintains high performance on knowledge-intensive tasks like TriviaQA and TruthfulQA, effectively mitigating the trade-off between hallucination suppression and parametric knowledge retention often observed in existing methods. Our findings validate the geometric interpretation of hallucinations and establish DCO as a computationally efficient approach for enforcing manifold this http URL code is available at this https URL

---


### 43. [Conditional Hypothesis Generation for LLM-Based Text Analysis with Researcher-Specified Covariates](https://arxiv.org/abs/2606.03029)

**<font color=#1a73e8>作者：</font>** Paiheng Xu, Jing Liu, Wei Ai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A core goal of computational social science is to discover interpretable differences in how language varies across outcomes of interest, such as political affiliation or instructional quality. Recent LLM-based hypothesis generation methods describe such differences in natural language, but select for globally discriminative patterns without accounting for covariates that shape the data based on researchers' domain knowledge. When covariates are ignored, selected patterns can reflect confounds rather than differences of substantive interest. We introduce conditional hypothesis generation, a framework that incorporates researcher-specified covariates to steer hypothesis discovery toward differences that hold within relevant subgroups. Two challenges arise: the target subgroup may be underrepresented (stratum imbalance), and the direction of a difference may reverse across subgroups (sign reversal). We propose two econometrics-inspired methods: one introduces feature--covariate interactions to detect sign reversals, and the other applies within-stratum demeaning and inverse-frequency reweighting to equalize underrepresented strata. Synthetic experiments show each method outperforms global baselines in its targeted setting, and expert evaluation on two real-world datasets confirms that covariate-aware generation surfaces more useful hypotheses within relevant subgroups.

---


### 44. [The Deliberative Illusion: Diagnosing Factual Attrition and Stance Homogenization in Multi-Agent LLM Deliberation](https://arxiv.org/abs/2606.03032)

**<font color=#1a73e8>作者：</font>** Herun Wan, Jiaying Wu, Minnan Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems often treat consensus as evidence of successful interaction. For deliberative problems, however, reliability depends on whether agents preserve the facts and viewpoints needed to interpret an issue. We identify the deliberative illusion: discussion produces (1) factual attrition, the progressive loss of issue-critical facts, alongside (2) stance homogenization, the collapse of diverse positions toward consensus. To measure this process, we introduce DelibTrace, a framework that decomposes each issue into atomic facts, labels issue-critical ones, distributes them across agents, and tracks their survival across discussion rounds. Across ethical and news-based deliberation with three representative LLM families, multi-agent discussion erases up to 72% of issue-critical facts. This loss is consequential: retained evidence can reconstruct the issue misleadingly, final stances remain anchored in base-model priors, and a single malicious agent can inject misinformation into the shrinking shared context. These results reveal a sharper risk: agents can agree more while knowing less. We call for evaluations that measure which facts, uncertainties, and legitimate disagreements survive interaction.

---


### 45. [TriEval: A Resource-Efficient Pipeline for LLM Bias, Toxicity, and Truthfulness Assessment](https://arxiv.org/abs/2606.03036)

**<font color=#1a73e8>作者：</font>** Akshatha Srikantha, Manpreet Singh, Yash Jajoo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs have evolved from basic chatbots to the backbone of the AI ecosystem, now widely used in healthcare, schools, and government services. The domain-wide adoption of LLMs necessitates continuous evaluation to ensure their safety and fairness. Common issues encountered after deploying LLMs include inconsistent outputs and hallucinations of incorrect information. Although numerous LLM evaluation tools exist, most are limited to testing a single parameter at a time or require massive computational resources that are not accessible to most researchers. TriEval addresses these challenges by evaluating LLM outputs across multiple parameters, including bias, toxicity, and truthfulness together, while minimizing computing resources. The pipeline is compatible with both open- and closed-source models and runs on a standard laptop without a GPU cluster. TriEval has been tested on four models: Llama 3 8B, Mistral 7B, Gemma 2 9B, and Claude Haiku. The results show clear differences between open-source and closed-source models, especially in terms of toxicity and truthfulness. TriEval is being released as open source to enable broader access for researchers with limited computational resources.

---


### 46. [The Geometry of LLM-as-Judge: Why Inter-LLM Consensus Is Not Human Alignment](https://arxiv.org/abs/2606.03043)

**<font color=#1a73e8>作者：</font>** Sourabrata Mukherjee, Hamna Hamna, Kalika Bali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LMs-as-judges are now standard, yet judges agree strongly with one another while agreeing only weakly with humans. We test whether this reflects shared signal or shared bias by measuring four geometric quantities on the standard LLM-as-judge stack across four community-built Indic datasets, eight Indic languages, and 41 LLM judges: score spread, effective rank, principal angle to the human subspace, and stacked correlations among judges and humans, all with bootstrap confidence intervals.
On subjective rubrics, judges use less than half the human score range ($\sigma_J / \sigma_H \approx 0.3$--$0.5$). Their evaluation axis is nearly orthogonal to the human one and noticeably further from humans than humans are from each other ($87^\circ$--$89^\circ$ versus $78^\circ$--$81^\circ$). Inter-LLM agreement exceeds LLM--human agreement ($r_{LL} \approx 0.35$ versus $r_{LH} \approx 0.27$--$0.32$).
On a rubric with a verifiable factual answer, the same diagnostics fall back into the human range (axis $58.5^\circ$; $r_{LH} = 0.519$). Fine-tuning and preference optimization recover spread ($0.32 \rightarrow 1.08$) but barely move the axis (still $87^\circ$--$88^\circ$). Only post-hoc calibration on a small human-anchored set improves all four community-health rubrics together, placing a calibrated 24B Indic judge ($r = 0.184$) ahead of GPT-5.5 ($r = 0.123$), yet still short of human reliability (human-human $r = 0.474$ on the verifiable rubric).
We argue that inter-LLM agreement should be considered evidence of human alignment only when a direct geometric check on the judge's score subspace passes; otherwise, the consensus reflects agreement within a collapsed subspace.

---


### 47. [SkillDAG: Self-Evolving Typed Skill Graphs for LLM Skill Selection at Scale](https://arxiv.org/abs/2606.03056)

**<font color=#1a73e8>作者：</font>** Tong Bai, Zhenglin Wan, Pengfei Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents adopt large skill libraries, selecting the right subset becomes a structural problem rather than a similarity-matching one: skills depend on, conflict with, specialize, or duplicate one another, a structure invisible to both full enumeration and embedding similarity. We present SkillDAG, which models inter-skill relationships as a typed directed graph and exposes it to an LLM agent as an inference-time, agent-callable structural retrieval interface, queried and evolved during execution rather than baked into a fixed retrieval pipeline: each search returns vector matches, typed-edge neighbors, and conflict signals, and a propose-then-commit protocol lets the agent register execution-backed edges so the graph accumulates structure across episodes. On ALFWorld and SkillsBench with MiniMax-M2.7, SkillDAG reaches 67.1% success and 27.3% reward, exceeding the strongest reported Graph-of-Skills baseline by +12.8 and +8.6 points; the advantage ports to gpt-5.2-codex, and intrinsic SkillsBench Ret@K rises from 65.5 to 78.2 under matched queries. These gains trace to isolable mechanisms: candidate ranking that stays robust as the pool grows 10x where a fixed seeding-diffusion pipeline degrades, and set-monotone online edits that enlarge ground-truth recall without evicting prior hits.

---


### 48. [Rethinking Molecular Text Representations for LLMs: An Empirical Study](https://arxiv.org/abs/2606.03057)

**<font color=#1a73e8>作者：</font>** Arun Raja, Garrett M. Morris, Kian Ming A. Chai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for molecular tasks, but it remains unclear which molecular representation to use. We present a systematic benchmark evaluating LLM molecular competence across nine representations and eight chemical tasks. We benchmark 16 LLMs across five model families, including reasoning and non-reasoning variants, chemistry-specialized LLMs, and closed frontier models. Performance is strongly representation-dependent and no single representation wins across tasks, though CML is the best, followed by MolJSON, InChI, and then canonical SMILES. Explicit structured text representations (CML and MolJSON) dominate structural tasks; IUPAC dominates semantic tasks, winning molecule retrieval for all 16 LLMs; and SMILES variants are rarely optimal despite their prevalence in pretraining. Chemistry-specialized models perform well with SMILES at the cost of large degradations with structured text representations, suggesting SMILES-only evaluation rewards specialization that does not generalize. Using LLM-as-a-judge, we find that IUPAC produces the highest fraction of correct molecule generations. A mechanistic study via tokenization audits, linear probes and attention shows that representations are encoded differently inside the model; for example, structured representations require higher attention across the molecular span. Our results argue against representation-invariant evaluation and motivate task-aware representation routing for LLM-based chemistry.

---


### 49. [CORE: Conflict-Oriented Reasoning for General Multimodal Manipulation Detection](https://arxiv.org/abs/2606.03066)

**<font color=#1a73e8>作者：</font>** Jinjie Shen, Yaxiong Wang, Yujiao Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid rise of generative AI has made multimodal fake news increasingly realistic and pervasive, posing severe threats to public trust and social stability. Existing detection methods rely heavily on manipulation-specific models and large-scale labeled data, resulting in poor generalization to emerging manipulation types. We observed that the essence of manipulated misinformation lies in its intrinsic conflicts, \textbf{i.e.,} semantic or physical inconsistencies either across modalities or with common world knowledge. Inspired by this observation, we propose \textbf{C}onflict-\textbf{O}riented \textbf{RE}asoning (\textbf{CORE}) framework, an effective paradigm that learns to endows multimodal large language models (MLLMs) with explicit conflict-capturing capability. To this end, CORE first constructs the Conflict Attribution Corpus (CAC) with fine-grained annotations of conflict factors and sources, providing essential data support for subsequent conflict perception training. By performing conflict-oriented representation enhancement and reasoning based on CAC, CORE achieves robust and generalizable conflict detection, effectively and rapidly adapting to unseen manipulation types with a few samples or in even zero-shot settings. Extensive experiments demonstrate that CORE surpasses state-of-the-art models. The dataset and code are publicly available at this https URL.

---


### 50. [ASymPO: Asymmetric-Scale Policy Optimization for Asynchronous LLM Post-Training Without Behavior Information](https://arxiv.org/abs/2606.03070)

**<font color=#1a73e8>作者：</font>** Zehua Liu, Yuxuan Yao, Xiaojin Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous reinforcement learning can improve language-model post-training throughput by decoupling response generation from policy optimization, but stale responses introduce distribution drift. Standard behavior-corrected methods control this drift with behavior-policy probabilities, importance ratios, or clipping, which requires token-aligned, versioned, and numerically consistent behavior log-probabilities across rollout and learner systems. We ask whether asynchronous group-relative RL can instead be stabilized using only current-policy probabilities. We identify a scale-imbalance failure mode: when stale responses are evaluated under the current policy, positive and negative loss terms can appear at different negative log-probability scales, so zero-sum advantages no longer imply balanced loss contributions. We propose Asymmetric-Scale Policy Optimization (ASymPO), which normalizes each response's token loss by its current average token negative log-probability. ASymPO requires no behavior-policy probabilities, restores response-level zero-sum balance, and preserves a nonzero learning signal. We also introduce Scaled Policy Optimization (SPO), a fixed negative-scaling baseline, and evaluate both current-policy-only objectives in asynchronous mathematical reasoning post-training.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-188](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

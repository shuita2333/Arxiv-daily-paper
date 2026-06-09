# 🧠 大模型相关研究 | 2026年06月10日

> 本类共 **331** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-331](./part-07.md)

---

### 251. [HDRAgent: An Agentic Framework for Multi-Exposure HDR Imaging](https://arxiv.org/abs/2606.09110)

**<font color=#1a73e8>作者：</font>** Weiyu Zhou, Tao Hu, Yijian Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing multi-exposure HDR methods follow a fixed feed-forward reconstruction paradigm, making them prone to ghosting artifacts in complex dynamic scenes. To address this issue, we propose HDRAgent, the first agent-driven framework for HDR imaging, which adaptively selects reconstruction strategies according to the current scene conditions. Specifically, to provide scene-specific prior knowledge, we introduce a fine-grained contextual knowledge matching (FCM) module. This module leverages multimodal large language model (MLLM)-derived scene perception to retrieve relevant historical cases and tool knowledge, organizing them into structured evidence for MLLM-based adaptive tool scheduling. In addition, we propose a perception--distortion feedback mechanism that transforms post-execution quality assessment and artifact diagnosis into structured feedback, which is accumulated in historical memory to help subsequent contextual knowledge refinement and strategy selection. Furthermore, considering that extreme motion can invalidate alignment methods, we design an agent-guided generative alignment strategy that uses MLLM-based dynamic-region parsing to reconstruct unreliable contents in non-reference frames under reference-frame guidance. Experiments demonstrate that HDRAgent effectively reduces ghosting and local artifacts while achieving competitive or superior objective performance and visual quality.

---


### 252. [A Regret Minimization Framework on Preference Learning in Large Language Models](https://arxiv.org/abs/2606.09124)

**<font color=#1a73e8>作者：</font>** Suhwan Kim, Taehyun Cho, Geon-Hyeong Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has enabled progress on reasoning-intensive tasks by relying on task-specific verifiers that provide automated correctness signals. However, many realistic language tasks are difficult to equip with reliable verifiers, motivating a growing reliance on reinforcement learning from human feedback (RLHF). In this setting, we argue that a closer examination of how human feedback should be interpreted is essential. We introduce Regret-based Preference Optimization $(\textbf{RePO})$, which reframes RLHF through $\textit{regret minimization}$ rather than reward maximization. Human preferences are often shaped by $\textit{prospective}$ anticipation of outcomes and $\textit{counterfactual}$ comparisons to alternative behaviors, rather than by immediate, outcome-independent utility. $\textbf{RePO}$ captures this structure by modeling preferences as behavior-conditioned assessments of relative suboptimality. Experiments on mathematical reasoning benchmarks and human preference datasets demonstrate consistent performance gains, indicating that $\textbf{RePO}$ is an effective and human-aligned approach for training large language models.

---


### 253. [Late-Layer Fusion is Enough: Dual-Path Vision Token Routing for Multimodal Large Language Models under Visual Saturation](https://arxiv.org/abs/2606.09131)

**<font color=#1a73e8>作者：</font>** Siyuan Liu, Jinyang Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) commonly inherit the deep, symmetric Transformer backbone designed for unimodal text modeling, and apply the same computation uniformly to image and language tokens. This design overlooks a key modality asymmetry: image and text tokens differ substantially in information density, redundancy, and required reasoning depth. Through a layer-wise analysis of LLaVA-1.5, we observe that vision tokens tend to saturate in the middle layers. Specifically, text-to-image attention decreases from 0.68 at layer 0 to 0.07 by layer 4, and stabilizes near 0.04 after layer 18, whereas text tokens continue to benefit from deep semantic processing. These findings suggest a mismatch between architectural symmetry and depth-asynchronous modality evolution, resulting in redundant visual computation and possible drift in perceptual representations during deep task-specific adaptation. Motivated by this, we propose Dual-Path Vision Token Routing (DPVR), a modality-asymmetric routing framework for efficient MLLMs. Its core instantiation, DPVR-LF (Late-Layer Fusion), routes vision tokens at the saturation point into a one-layer trainable side branch, runs a thirteen-layer text-only forward that skips image positions in the deep stack, and re-fuses the visual and textual streams only at the final layer. With approximately 3% trainable parameters, DPVR-LF preserves competitive multimodal performance on standard benchmarks while reducing visual computation in the deep Transformer stack. The results challenge the conventional assumption that vision tokens must traverse all deep language-model layers, and indicate that a single late fusion layer can be sufficient for maintaining strong perceptual competence in LLaVA-style MLLMs.

---


### 254. [Vision Language Model Helps Private Information De-Identification in Vision Data](https://arxiv.org/abs/2606.09132)

**<font color=#1a73e8>作者：</font>** Tiejin Chen, Pingzhi Li, Kaixiong Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual Language Models (VLMs) have gained significant popularity due to their remarkable ability. While various methods exist to enhance privacy in text-based applications, privacy risks associated with visual inputs remain largely overlooked such as Protected Health Information (PHI) in medical images. To tackle this problem, two key tasks: accurately localizing sensitive text and processing it to ensure privacy protection should be performed. To address this issue, we introduce VisShield (Vision Privacy Shield), an end-to-end framework designed to enhance the privacy awareness of VLMs. Our framework consists of two key components: a specialized instruction-tuning dataset OPTIC (Optical Privacy Text Instruction Collection) and a tailored training methodology. The dataset provides diverse privacy-oriented prompts that guide VLMs to perform targeted Optical Character Recognition (OCR) for precise localization of sensitive text, while the training strategy ensures effective adaptation of VLMs to privacy-preserving tasks. Specifically, our approach ensures that VLMs recognize privacy-sensitive text and output precise bounding boxes for detected entities, allowing for effective masking of sensitive information. Extensive experiments demonstrate that our framework significantly outperforms existing approaches in handling private information, paving the way for privacy-preserving applications in vision-language models. Our dataset and code can be found here.

---


### 255. [Claw-R1: A Step-Level Data Middleware System for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.09138)

**<font color=#1a73e8>作者：</font>** Daoyu Wang, Mingyue Cheng, Qingchuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) has become an important post-training paradigm for turning LLMs from static chatbots into interactive agents, giving rise to representative applications such as OpenClaw. Existing work mainly focuses on policy optimization algorithms and training frameworks, but pays less attention to the full data lifecycle of agent-environment interactions, from data production to training consumption. To bridge this gap, we present Claw-R1, an interactive step-level data middleware system for agentic RL. Claw-R1 connects heterogeneous agent runtimes with RL training backends through two core components: a Gateway Server and a Data Pool. The Gateway Server captures multi-turn interaction steps through a unified LLM API entry point, while the Data Pool organizes them into step-level records consisting of prompt IDs, response IDs, rewards and other metadata. In our demo, users can interactively inspect live trajectories, examine the state, action, and reward of each step, curate data by quality and readiness, and configure training-ready batches for different downstream RL algorithms. Overall, Claw-R1 treats agent interaction traces as managed data assets rather than temporary runtime logs. Through this demonstration, we hope to encourage the community to recognize the importance of data management in agentic RL. Our code is available at this https URL and the demonstration video can be found at link this https URL.

---


### 256. [Decoding Pedestrian Crossing Intention from Egocentric Vision via Vision Language Models](https://arxiv.org/abs/2606.09142)

**<font color=#1a73e8>作者：</font>** Danya Li, Xiang Su, Yan Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric vision offers a first-person view of human perception and decision making, yet its potential for traffic-safety prediction remains underexplored. In this work, we study the decoding of pedestrian crossing intentions from short egocentric video clips. We approach this by formulating the task as a closed-ended visual question answering (VQA) problem and leveraging vision language models (VLMs) to predict the pedestrians' intent. We first benchmark three families of state-of-the-art VLMs in a zero-shot setting, finding that they achieve moderate gains over random guessing but exhibit limited higher-level traffic reasoning. Motivated by these findings, we further adapt VLMs to the target task using parameter-efficient fine-tuning. Our results show that the fine-tuned models substantially outperform their zero-shot counterparts and achieve a 9\% accuracy improvement over a specialized transformer-based baseline. Finally, we demonstrate that incorporating additional contextual cues, including ego motion, vehicle motion, and eye gaze, further improves predictive performance. In particular, the fine-tuned Qwen3-VL-2B model guided by eye gaze and ego motion achieves a 14.5% accuracy improvement over the transformer baseline, establishing a new state of the art for egocentric pedestrian intent decoding.

---


### 257. [CAMF-Det: Closure-Aware Multimodal Fusion for LiDAR-Camera 3D Object Detection on UAV Platforms](https://arxiv.org/abs/2606.09143)

**<font color=#1a73e8>作者：</font>** Yanze Jiang, Yanfeng Gu, Xian Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal 3D object detection based on LiDAR and cameras has demonstrated excellent performance in ground-vehicle scenarios, but has not been explored for Unmanned Aerial Vehicle (UAV) platforms. In UAV top-down scenes, frequent groundobject occlusion dominated by tree canopies causes spatially varying and modality-dependent information degradation. Existing multimodal fusion frameworks neither explicitly model such ground-object occlusion nor embed occlusion awareness into the detection pipeline, limiting their performance in occluded UAV scenes. To address these challenges, we propose CAMF-Det, a closure-aware multimodal fusion framework for LiDAR-camera 3D object detection on UAV platforms, which derives dual-modal occlusion intensity through physics-inspired modeling and embeds them as priors throughout the detection pipeline. First, a dual-modal closure modeling module explicitly constructs occlusion intensity ground truth for both modalities offline via a Beer-Lambert-inspired formulation and building-mask correction. Second, using these ground-truth maps as supervision, a dual-modal prediction network converts the offline modeling results into online occlusion intensity predictions under single-frame inference. Third, both ground-truth and predicted occlusion intensity are injected into data augmentation, feature encoding, multimodal fusion, and detection head, enabling adaptive detection under spatially varying and modality-dependent information degradation. Experiments on two self-built UAV-based multimodal datasets, SI3D-DI and SI3D-DII, demonstrate that CAMF-Det achieves the best performance across all difficulty levels, with hard-level mAP$_{\mathrm{BEV}}$ improvements of 9.43% and 4.88% over the best competing methods, respectively. These results confirm the effectiveness of explicit occlusion prior modeling and exploitation for robust multimodal 3D detection in UAV scenes.

---


### 258. [Explicit Representation Alignment for Multimodal Sentiment Analysis](https://arxiv.org/abs/2606.09148)

**<font color=#1a73e8>作者：</font>** Baode Wang, Ziming Wang, Huacan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal affective analysis aims to understand human sentiment and emotion by jointly modeling heterogeneous modalities such as text and images. However, multimodal models often fail to consistently outperform strong text-only baselines, with performance varying significantly across fusion strategies. In this work, we identify representation misalignment between independently pretrained modality encoders as a key bottleneck for effective multimodal learning, and show through controlled experiments that alignment prior to fusion is often more important than fusion complexity. To address this issue, we propose a unified multimodal affective analysis framework that leverages vision-language models (VLMs) to convert visual content into structured textual descriptions, projecting heterogeneous modalities into a shared linguistic space and enabling interpretable text-centric reasoning. To further improve robustness, we introduce a hybrid learning strategy that combines semantic token selection with a batch-level uniformity regularization objective, encouraging a more dispersed and stable global feature space while mitigating noise introduced by VLM-generated descriptions. Experiments on multiple multimodal sentiment and emotion benchmarks show that our method consistently outperforms strong unimodal and multimodal baselines, achieving state-of-the-art performance. Our analysis further highlights the critical role of representation alignment in multimodal affective learning.

---


### 259. [SEF-CLGC at SemEval-2026 Task 11: Logical Notation Impact on Language Model Performance](https://arxiv.org/abs/2606.09157)

**<font color=#1a73e8>作者：</font>** Hanna Abi Akl, Fabien Gandon, Catherine Faron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper revisits our pipeline called Syllogistic Evaluation Framework-Common Logic Grammar Construction (SEF-CLGC). We combine formal logical notations with Small Language Models (SLMs) to evaluate reasoning performance on the SemEval-2026 Task 11 Subtask 1: Disentangling Content and Formal Reasoning in Large Language Models. Our experiments show that by relying solely on SLMs, trained on a combination of natural and symbolic languages, our best model achieves a content score of 27.80% on the task while significantly lowering the content bias in reasoning.

---


### 260. [Unified Energy for Invariant and Independent Decoding in Diffusion Language Models](https://arxiv.org/abs/2606.09159)

**<font color=#1a73e8>作者：</font>** Yuchen Yan, Minkai Xu, Zaiquan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) enable parallel text generation by iteratively denoising a full sequence, offering attractive flexibility compared to auto-regressive (AR) decoding. However, existing methods fail to fully capture token relationships, leading to a performance gap relative to AR baselines, especially as the degree of parallelism increases. In this paper, we give a systematic analysis of the gap, identifying three key factors: (i) model capacity, (ii) dependency, and (iii) invariance. To address these issues, we first propose an invariant energy (Inv-E) together with an effective sampling-based estimator to handle the invariance issue. By further combining with the independent energy (Ind-E), we obtain a unified energy (Uni-E), that accounts for all these factors. Uni-E enjoys a unique advantage: it can be computed exactly without sampling-based partition estimation. Besides, Uni-E is model agnostic and can therefore be scaled to models of arbitrary size. We further prove that Uni-E can correct the distribution shift caused by dependency and invariance. Extensive experiments across Diffusion Language Models (DLMs) and Diffusion Large Language Models (DLLMs) demonstrate the effectiveness of the proposed Uni-E.

---


### 261. [Vision-Language Guided Hyperspectral Object Tracking via Semantics Fusion and Contextual Template Updating](https://arxiv.org/abs/2606.09167)

**<font color=#1a73e8>作者：</font>** Rui Yao, Yuhong Zhang, Kunyang Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral object tracking (HOT) leverages the rich spectral information provided by hyperspectral videos (HSVs), offering substantial potential for object tracking. However, efficiently extracting and exploiting spectral information from redundant spectral bands remains a fundamental challenge, which severely limits model generalization and tracking performance. Moreover, in dynamic scenes, targets often experience drastic appearance variations due to factors such as occlusion and illumination changes. These variations lead to large deformations between the current frame and the template. Such discrepancies pose major challenges for existing temporal modeling approaches. In this work, we propose VLHTrack, a novel hyperspectral vision-language (VL) joint tracking framework. Specifically, we incorporate language priors to address the fundamental challenge of spectral redundancy by designing a Language-Guided Band Selection Module (LBSM). By leveraging Large Language Model (LLM) descriptions, LBSM establishes a semantic-to-spectral mapping that mitigates redundancy and accentuates discriminative spectral features. A Multi-Modal Vision-Language Fusion Module is then employed to seamlessly integrate visual and linguistic embeddings, harnessing their complementary advantages to learn coherent cross-modal representations. To address target deformation in long-term sequences, we propose a dynamic update template feature strategy implemented via the Dynamic Template Update with Mamba (DTUM) module. By leveraging selective state space modeling, DTUM learns inter-frame dependencies to update template feature, ensuring efficient template feature evolution guided by temporal context. Experiments on HOT2023 and HOT2024 demonstrate that VLHTrack outperforms state-of-the-art (SOTA) methods.

---


### 262. [IMUG-Bench: Benchmarking Unified Multimodal Models on Interleaved Understanding and Generation](https://arxiv.org/abs/2606.09169)

**<font color=#1a73e8>作者：</font>** Lingyi Meng, Zecong Tang, Haoran Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, unified multimodal models (UMMs) have emerged to support both understanding and generation within a single framework. Mastering dynamic, multi-turn interleaved image-text dialogues is a crucial task for UMMs in real-world applications. However, existing benchmarks fail to evaluate this important task, as they are often limited to single-turn or static settings, and typically overlook exposure bias in multi-turn interactions. To bridge this gap, we propose IMUG-Bench, a comprehensive benchmark for multi-turn interleaved image-text dialogue of UMMs that jointly evaluates their understanding and generation capabilities. Our IMUG-Bench comprises three classes: Static Spatial, Temporal Causal, and Hybrid, covering 3,113 samples and 12,034 interaction turns. It also includes dynamic understanding questions, thereby supporting evaluation that better reflects real-world multi-turn interaction scenarios. Large-scale experiments on IMUG-Bench systematically evaluate mainstream open-source and closed-source UMMs, revealing their capability boundaries and failure modes, and uncovering pronounced exposure bias on the generation side in multi-turn interactions. We further explore several test-time scaling strategies, including Chain-of-Thought, Self-Verification, and Best-of-N Sampling, which effectively improve generation accuracy and mitigate exposure bias in generation tasks. These findings provide insights into enhancing the robustness and multi-turn interaction capability of future UMMs.

---


### 263. [Claude Code-Driving Scenario Mining for the Argoverse 2 Challenge](https://arxiv.org/abs/2606.09180)

**<font color=#1a73e8>作者：</font>** Wei Deng, Caoshengzhe Xue, Shuaikun Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present our submission to the CVPR 2026 Argoverse 2 Scenario Mining Challenge. Our system uses a four-stage pipeline: (1) autonomous code generation via a Claude Code agent powered by GLM~5.1, (2) iterative training set screening with Timestamp Balanced Accuracy threshold 0.8 to curate few-shot examples, (3) semantic code review by a separate Claude Code session, and (4) Qwen3-VL scene-level verification to filter false positives. We report results on the Argoverse 2 test set.

---


### 264. [Symbolic and Abstractive Reasoning with Complex Visual Queries](https://arxiv.org/abs/2606.09195)

**<font color=#1a73e8>作者：</font>** Yichi Zhang, Jingdian Lu, Zhuo Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding and reasoning over abstract visual content remains a challenge for current multi-modal large language models (MLLMs). In this paper, we explore a novel abstract data type termed complex visual query (CVQ), designed to probe symbolic and abstractive reasoning, which is a critical yet underexplored dimension of human-like neuro-symbolic reasoning for MLLMs. We present a comprehensive investigation from three perspectives: \textbf{Data $\times$ Paradigm $\times$ Exploration}. Specifically, we propose a scalable pipeline for synthesizing CVQs grounded in large-scale multi-modal knowledge graphs, generating a diverse dataset encompassing 14 distinct query types via systematic combinations of first-order logic operators. We further introduce a two-stage training framework that progressively equips MLLMs with robust visual reasoning capabilities. We conduct extensive experiments to rigorously evaluate MLLMs across multiple dimensions, including reasoning performance on CVQs, as well as cross-task and cross-scenario generalization. We believe our work opens new perspectives and avenues for advancing the reasoning frontiers of MLLMs.

---


### 265. [MASS: Deep Research for Social Sciences with Memory-Augmented Social Simulation](https://arxiv.org/abs/2606.09198)

**<font color=#1a73e8>作者：</font>** Yongrui Liu, Deyi Xiong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Research agents powered by Large Language Models (LLMs) have exhibited extraordinary potential in automated paper writing tasks. However, existing systems rely heavily on literature retrieval and synthesis through internet and local knowledge bases, often resulting research in lacking insight and creativity in social science. To address this issue, we propose "Memory-Augmented Social Simulation (MASS)", an innovative paradigm that leverages highly realistic and research-oriented social simulations to enhance the creativity and empirical founding of LLMs-generated research. Specifically, MASS integrates three core components: dynamic goal-path planning with multi-level social norm restraint to guide the simulation, a multi-disciplinary behavior dataset for agent memory cold-start, and a structured forgetting mechanism inspired by the Ebbinghaus curve. Together, these ensure simulation authenticity and provide a robust empirical foundation for generating innovative scholarly papers. Experimental results demonstrate the effectiveness of our method, showing a 6.81\% improvement in generation overall quality over foundation LLMs and 17.19\% gain in Insight over strong baselines.

---


### 266. [The Injection Paradox: Brand-Level Suppression in Safety-Trained LLM Recommendations via RAG Context Injection](https://arxiv.org/abs/2606.09204)

**<font color=#1a73e8>作者：</font>** Hyunseok Paeng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a reproducible failure mode of safety training in RAG-based LLM recommendation -- the Injection Paradox -- in which prompt injections embedded in retrieved documents backfire against the attacker, suppressing the target brand below the injection-free baseline. In safety-trained Claude models, documents containing prompt injections suffer a sharp drop in recommendation rate, and this suppression propagates beyond the injected document to unmodified documents of the same brand. In Claude Opus 4.6, the target brand drops from a 54% baseline to zero top-2 recommendations across all 50 trials, even though only 1 of 4 brand documents in the corpus contains an injection. The directional pattern is reproduced in counterfactual experiments and across three brands. A contrasting result across the GPT models tested, where the same injection instead increases recommendations, suggests model-family differences in how injection-like context affects recommendation behavior. These findings raise the technical possibility of a reverse-attack scenario in which an adversary embeds injections in a competitor's documents to suppress the competitor's brand via safety-sensitive model behavior.

---


### 267. [Event-driven dynamic trajectories reconstruction and measurement of mechanical parameters for fragments](https://arxiv.org/abs/2606.09208)

**<font color=#1a73e8>作者：</font>** Haoyang Li, Banglei Guan, Muxi Zha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> During warhead detonation, high-density, high-speed, and mutually occluded fragments are generated. Their mechanical parameters (position, velocity, kinetic energy) directly determine the lethality of the warhead fragment field. However, high-intensity flash and smoke in detonation scenarios severely hinder the accurate acquisition of these mechanical parameters. To address this challenge, this paper integrates experimental mechanics approaches and presents an event-driven method for reconstructing the dynamic trajectories of fragments and measuring their mechanical parameters. As a novel brain-inspired visual sensor, event cameras offer microsecond-level temporal resolution and high dynamic range lighting change perception, overcoming the difficulty of accurately measuring high-speed targets under strong flash interference. The method constructs a multi-event-camera vision system, adopting three geometric constraints: time-correlated epipolar constraint to find potential matching event point pairs, and trifocal tensor line constraint plus local homography constraint to eliminate mismatches. A comprehensive probability model is established, with entropy weight method determining the weight of each constraint's probability to quantitatively filter mismatches. 3D trajectory reconstruction is achieved via spatial line-line intersection and nonlinear optimization. Finally, the velocity and kinetic energy of the fragments are calculated based on the reconstructed trajectory. This method provides reliable technical support for the mechanical damage evaluation of warhead fragment fields and the tactical protection design.

---


### 268. [Temporal-Aware Reasoning Optimization for Video Temporal Grounding](https://arxiv.org/abs/2606.09248)

**<font color=#1a73e8>作者：</font>** Minghang Zheng, Zihao Yin, Yi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal Large Language Models (MLLMs) have achieved remarkable progress in video temporal grounding with reinforcement learning for generating reasoning paths. However, existing models often produce superficial reasoning, which offers limited guidance for precise temporal localization. This limitation stems from (1) inefficient random exploration and (2) reward functions that focus solely on the answer correctness while ignoring reasoning quality. To address these issues, we propose TaRO (Temporal-Aware Reasoning Optimization), a framework that explicitly enhances the model's ability of thinking with time. First, we introduce a Constructive Reasoning Exploration that leverages pre-generated dense captions to construct reasoning paths grounded in explicit visual cues and timestamps, enabling efficient exploration of high-quality time-aware reasoning. Second, to evaluate reasoning quality, we design a Temporal-Sensitivity Reward. High-quality reasoning should be anchored to specific events and timestamps. If the event boundary under thinking is disrupted, such reasoning should become invalid, leading to a drop in the logit of the reasoning path. We utilize this drop as a critique of reasoning quality. Finally, TaRO follows a progressive curriculum, which starts by utilizing this reward to select better constructed reasoning paths, and evolves to a free exploration phase where the model autonomously generates effective reasoning. Experiments demonstrate that TaRO achieves state-of-the-art performance on VTG benchmarks. Code is available at this https URL.

---


### 269. [MAGIS: Evidence-Based Multi-Agent Reasoning for Interpretable Strabismus Clinical Decision-Making](https://arxiv.org/abs/2606.09249)

**<font color=#1a73e8>作者：</font>** Xikai Tang, Yifan Wang, Jiafan Zhuang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Strabismus is a common ocular disorder that requires fine-grained subtype diagnosis for individualized treatment planning. However, existing deep learning methods mainly provide diagnostic predictions without transparent reasoning, while recent large vision-language models (LVLMs), although promising for joint image understanding and report generation, remain highly prone to hallucination in this evidence-sensitive and rule-driven medical task. To address these challenges, we propose MAGIS, an evidence-based Multi-AGent reasoning for Interpretable Strabismus diagnosis framework. MAGIS transforms black-box end-to-end generation into a structured diagnostic process consisting of candidate hypothesis generation, dual-evidence constrained context, evidence-based corrective verification, and report generation. Specifically, we introduce a Dual-Evidence Constrained Context (DECC) mechanism that jointly organizes visual evidence from the photograph of the nine cardinal positions of gaze and evidence-based clinical diagnostic rules into a constrained context for reliable diagnostic reasoning. We further develop an Evidence-Based Corrective Verification (EBCV) mechanism that verifies whether the current diagnostic hypothesis is supported by visual evidence, heatmap-based visual cues, and evidence-based clinical diagnostic rules. Hypothesis refinement is triggered when inconsistency is detected. Experiments on a fine-grained strabismus benchmark demonstrate that MAGIS not only significantly outperforms other state-of-the-art diagnostic systems, improving the weighted F1 score from 72.0% to 91.3%, but also substantially improves the clinical reliability (consistency, alignment, and completeness) of generated diagnostic reports. These results demonstrate that MAGIS provides an effective solution for building accurate, evidence-based, and clinically interpretable strabismus diagnosis systems.

---


### 270. [Reason Twice: Segmentation via Candidate Discovery and Comparative Reasoning](https://arxiv.org/abs/2606.09303)

**<font color=#1a73e8>作者：</font>** Xinyan Gao, Haoran Hao, Xiangyu Yue  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid development of pretrained foundation models has enabled more general image segmentation. Multimodal large language models (MLLMs) have been widely explored for image segmentation with complex queries that require high-level reasoning. Despite promising progress, existing methods are often constrained by limited training data and the gap between MLLMs and mask generation modules. To better transfer MLLMs' perception and reasoning ability to complex reasoning-based segmentation tasks, we propose a two-stage framework Rea2Seg for mask generation and selection. Specifically, the framework first identifies potential regions as candidate masks based on the attention maps of a segmentation MLLM. It then employs an MLLM to reason over the question and candidate masks and assign scores to each mask. The final segmentation result is obtained by reranking the candidates and selecting the highest-scoring mask, reformulating image segmentation as candidate discovery followed by discriminative mask selection.
We also notice that a large portion of questions in existing benchmarks focus on commonsense reasoning, and these questions usually do not fully require joint visual observation and reasoning. To address this issue, we introduce a new benchmark called ReasonSeg-SGDR that comprehensively evaluates a model's perception, grounding, and reasoning abilities across multiple dimensions, including discriminative recognition, spatial reasoning, geometric reasoning, and multi-step reasoning, with fine-grained mask generation.
In addition, we collect training data to enhance MLLMs' ability to jointly understand multimodal queries and candidate masks, and to assign scores through reasoning. Experimental results on the proposed benchmark and ReasonSeg demonstrate the effectiveness of the unified mask generation and selection framework.

---


### 271. [FF-JEPA: Long-Horizon Planning in World Models with Latent Planners](https://arxiv.org/abs/2606.09311)

**<font color=#1a73e8>作者：</font>** Sergi Masip, Jonathan Swinnen, Yutong Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Joint Embedding Predictive Architectures (JEPAs) have shown promising world modeling capabilities, enabling planning in latent space by optimizing action trajectories using methods like the Cross-Entropy Method (CEM). These methods are, however, too computationally expensive and ineffective for long-horizon planning. Furthermore, these methods typically require an explicit image of the goal state, which is not always possible in real-world tasks. In this work, we tackle these limitations by proposing Forward-Forward-JEPA (FF-JEPA), a hierarchical approach leveraging two forward dynamics models. Alongside a standard action-conditioned forward model, we introduce an action-free latent planner that predicts the next subgoal given the current state. This approach removes the need for goal images and enables long-horizon planning by decomposing complex trajectories into a sequence of tractable, short-term optimization problems. Preliminary results on PushT demonstrate that FF-JEPA successfully overcomes flat world models' long-horizon collapse, highlighting this approach as a promising direction for goal-free planning.

---


### 272. [Toward Compiler World Models: Learning Latent Dynamics for Efficient Tensor Program Search](https://arxiv.org/abs/2606.09312)

**<font color=#1a73e8>作者：</font>** Haolin Pan, Lianghong Huang, Xvlin Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor program optimization is essential for modern machine learning systems, but its search space is enormous. Existing auto-schedulers reduce measurement cost with learned cost models, yet they usually evaluate each candidate as a static code snapshot, ignoring the schedule trajectory that produced it. This makes them insensitive to action dependencies and vulnerable to superficial code variations. We propose a \emph{world-model-inspired} evaluator that models schedule evaluation as action-conditioned latent dynamics over program states. Starting from the initial program, it rolls out scheduling actions in a continuous latent space with a lightweight transition model, avoiding expensive AST mutation and repeated code encoding. The final dynamic representation is combined with action and hardware features to rank candidates. Implemented in TVM AutoScheduler, our method improves representative-subgraph latency over Ansor by 1.37$\times$ on GPU and 1.54$\times$ on CPU under the same 64-trial budget. It also matches Ansor-10K within 2.2% geometric mean using 10$\times$ fewer measurements, and accelerates full-model inference over PyTorch/PyTorch-opt(cuDNN) by 4.61$\times$/3.67$\times$ geometric mean.

---


### 273. [How Far Can Prompting Go for Minimal-Edit Ukrainian Grammatical Error Correction?](https://arxiv.org/abs/2606.09334)

**<font color=#1a73e8>作者：</font>** Kateryna Karpo, Artem Chernodub  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuned Large Language Models (LLMs) dominate in Ukrainian grammatical error correction (GEC), while API-accessed LLMs remain nearly untested on minimal-edit benchmarks. We evaluate 11 commercial LLMs from four providers and one open-source Ukrainian model on the UNLP 2023 GEC-only benchmark, comparing zero-shot, few-shot, minimal-edits, and LLM-assisted prompt optimization strategies. Our best configuration (Gemini 3.1-Pro) reaches F0.5=69.22, closing over 90% of the gap to fine-tuned SOTA (F0.5=73.14). For zero-shot prompts, only Claude models benefit from Ukrainian instructions. However, the best overall results for all models use Ukrainian minimal-edits prompts, whose language-specific rules require Ukrainian to express precisely. LLM-assisted prompt optimization on top of minimal-edits + few-shot achieves the highest score. Detailed minimal-edits instructions yield the largest gains for punctuation and case errors but cause the model to abandon several low-frequency categories. Delving into error analysis, we identify five recurring overcorrection patterns tied to Ukrainian-specific linguistic phenomena. Code, prompts, and outputs are publicly available.

---


### 274. [Leveraging Structural Constraints for Diffusion-based Neural TSP Solvers](https://arxiv.org/abs/2606.09343)

**<font color=#1a73e8>作者：</font>** Mickaël Basson, Philippe Preux  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural combinatorial optimization has recently achieved strong results on the Euclidean Traveling Salesman Problem (TSP) using generative models such as diffusion and consistency models. State-ofthe-art approaches like FT2T combine fast consistency-based prediction with gradient-based inference time refinement. However, gradient search often incurs significant computational overhead and may not align with the discrete structure of feasible solutions. We introduce Projected Consistency Inference (PCI), a plug-and-play, retraining-free alternative that replaces gradient refinement with structure-aware projections: PCI decodes valid Hamiltonian tours from the consistency model output and applies a lightweight local search (e.g., 2-opt). PCI achieves an average optimality gap (OG) of 0.17% on TSP with 500 cities, and 0.31% on TSP with 1000 cities, outperforming FT2T best settings (OG 0.22% and 0.36%, respectively) while reducing the inference time up to 30 to 40%. PCI also exhibits lower variance and memory usage, and can surpass classical heuristics such as LKH3 in rapid solution generation. Our results demonstrate that structure-aware inference time operations provide a practical and principled path for neural TSP solvers, complementing training time objectives.

---


### 275. [In-Context Learning for the Imputation of Public Opinion Data with Large Language Models](https://arxiv.org/abs/2606.09351)

**<font color=#1a73e8>作者：</font>** Tobias Holtdirk, Georg Ahnert, Joseph W Sakshaug 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have been widely evaluated as simulators of individual survey responses. In practice, however, fully unobserved responses are rare; the dominant problem is partial non-response. Imputation aims to restore the overall structure of a survey dataset by filling in these missing values. It has its own well-defined evaluation criteria and differs fundamentally from prediction. We propose to impute missing survey data through in-context learning (ICL). We systematically evaluate ICL design choices across different missingness mechanisms (MCAR, MAR, MNAR) on 150 opinion variables spanning 15 waves of the American Trends Panel. Compared to well-established statistical methods for data imputation like MICE PMM, our ICL approach consistently reduces absolute error across all missingness mechanisms, with the largest gains under non-random missingness (MNAR). Notably, the best-performing specification (gpt-oss-120b with 100 in-context examples) achieves near-nominal aggregate coverage (approaching the 95% level) with confidence intervals two to five times narrower than MICE PMM. We publish a Python package with an sklearn-like API to enable easy deployment of our method using local and proprietary LLMs.

---


### 276. [Is Text All You Need? Text as a Universal Information Bottleneck for Speech LLMs](https://arxiv.org/abs/2606.09366)

**<font color=#1a73e8>作者：</font>** Ming-Hao Hsu, Yuxuan Hu, Shujie Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) provide a powerful reasoning backbone for speech understanding, but integrating continuous acoustic signals into a frozen LLM remains challenging. Existing speech-to-LLM interfaces typically operate at two extremes: either enforcing near-discrete token alignment, which benefits transcription but loses paralinguistic information, or learning unconstrained continuous representations, which can drift away from the LLM's input space and degrade autoregressive decoding. In this work, we propose Convex Gate (C-Gate), a speech-to-LLM bridge that constrains all speech representations to lie within the LLM's input embedding manifold with an architectural convex-hull constraint. Concretely, each frame is represented as a convex combination of token embeddings, ensuring compatibility with the pretrained LLM while preserving continuous expressivity. Across automatic speech recognition (ASR) and emotion recognition, C-Gate achieves strong joint performance, improving LibriSpeech WER by up to 48.7% relative while matching or exceeding single-task emotion accuracy. Beyond performance, our analysis reveals a key insight: information is not carried by discrete token identities, but by time-resolved trajectories in the embedding space. Causal interventions confirm that both the trajectory structure and alignment to the pretrained embedding manifold are critical for performance. These results suggest that geometry, rather than token discreteness, is the fundamental design factor in speech-to-LLM interfaces, and provide a controlled regime for studying multimodal integration in frozen LLMs. We release the checkpoint, per-sample outputs, mechanism dumps, and intervention suite for replication.

---


### 277. [Capability-Aligned Hierarchical Learning for Tool-Augmented LLMs](https://arxiv.org/abs/2606.09371)

**<font color=#1a73e8>作者：</font>** Haotong Yang, Ting Long, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool learning enables LLMs to invoke external tools to accomplish tasks. Prior studies have demonstrated the effectiveness of a hierarchical structure: a high-level policy handles global planning and decomposes tasks into manageable sub-tasks, and a low-level policy focuses on invoking tools to solve these sub-tasks. However, these works typically optimize the high-level and low-level policies separately, leading to planner-executor misalignment and limiting LLM performance on tool-use tasks. In this paper, we propose a method called Capability-Aligned Hierarchical Learning (CAHL), which leverages RLVR to jointly optimize both policies, enabling better alignment between the high-level planner and the low-level executor. Experiments on constrained tool-use benchmarks (API-Bank and BFCL) and an open-ended environment (Bamboogle) demonstrate the effectiveness of CAHL.

---


### 278. [Precision Is Not Faithfulness: Coverage-Aware Evaluation of Grounded Generation with a Complete Oracle](https://arxiv.org/abs/2606.09376)

**<font color=#1a73e8>作者：</font>** Juan S. Santillana  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reference-free faithfulness metrics verify each atomic claim a model makes against ground truth, and are increasingly used to evaluate grounded generation. We show they share a blind spot: they measure only precision -- are the stated claims supported? -- and therefore reward abstention, since a model can score near-perfect faithfulness by saying almost nothing. We make this measurable using Formula 1 telemetry, a domain where strategic ground truth is derived deterministically and, crucially, completely: for each decision we know the full set of facts that mattered. This completeness -- absent in open-domain faithfulness benchmarks -- lets us measure recall (coverage of the relevant facts) exactly, alongside precision. On a multilingual (EN/ES/PT) benchmark of 7,253 decision instances spanning 150 races, the most precise frontier model covers under half of the relevant facts and ranks last by F1, so requiring coverage reorders the systems; the same effect reappears in a second complete-oracle domain (NOAA weather forecasts). A prompt ablation shows the low coverage is not an under-prompting artifact: explicitly asking models to be thorough does not close the gap. We pair faithfulness with coverage into a single score, validate the metric (controlled perturbation; agreement across a model-free regex extractor and a cross-family LLM extractor, system-level Spearman 1.0), and give a verifier-guided generation method that improves precision and recall without references. We release the benchmark, structured annotations, metric, baselines, and an interactive demo.

---


### 279. [Distilling Safe LLM Systems via Soft Prompts for On Device Settings](https://arxiv.org/abs/2606.09388)

**<font color=#1a73e8>作者：</font>** Motasem Alfarra, Cristina Pinneri, Dana Kianfar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying safe large language models (LLMs) on resource-constrained edge devices presents a critical challenge: while dual-model systems combining LLMs with guard models provide effective safety guarantees, their substantial memory and computational demands make them prohibitively expensive for on-device deployment. This paper presents a comprehensive study of parameter-efficient safety alignment methods for resource-constrained settings. Through systematic evaluation across multiple LLM architectures, training objectives, and parameter-efficient fine-tuning approaches, we identify that soft prompts combined with distillation-based training consistently outperform alternative methods. We introduce distillation frameworks based on total variation and KL divergence that effectively transfer safety behaviors from guard models into learned soft prompts. Our evaluations on various benchmarks demonstrate that this combination achieves superior safety-usefulness trade-offs compared to LoRA adapters, steering vectors, and direct optimization methods, while requiring minimal additional memory and compute at inference time. These findings establish soft prompt distillation as the preferred approach for safety alignment in on-device LLM deployment.

---


### 280. [CapRL++: Unified Reinforcement Learning with Verifiable Rewards for Dense Image and Video Captioning](https://arxiv.org/abs/2606.09393)

**<font color=#1a73e8>作者：</font>** Penghui Yang, Long Xing, Xiaoyi Dong 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image and video captioning are fundamental tasks that bridge the visual and linguistic domains, playing a critical role in pre-training Large Vision-Language Models (LVLMs). Current state-of-the-art captioning models are typically trained with Supervised Fine-Tuning (SFT), a paradigm that relies on expensive, non-scalable annotations and often causes models to memorize specific ground-truth answers, limiting their generality and ability to generate diverse, creative descriptions. To overcome these limitations, we propose applying Reinforcement Learning with Verifiable Rewards (RLVR) to the open-ended task of multimodal captioning. We introduce Captioning Reinforcement Learning++ (CapRL++), a novel reference-free training framework that redefines caption quality through its utility: a high-quality caption should enable a non-visual language model to accurately answer questions about the corresponding visual content. CapRL++ employs a decoupled two-stage pipeline where an LVLM generates a caption, and the objective reward is derived from the accuracy of a separate, vision-free LLM answering Multiple-Choice Questions based solely on that caption. Evaluations on more than 20 image and video benchmarks show that CapRL++ improves dense caption quality and strengthens caption-based pretraining across tasks such as spatial and temporal understanding. Pretraining on scalable image and video caption datasets annotated by CapRL++ yields substantial downstream gains. Furthermore, within the Prism Framework for caption quality evaluation, compact models trained with CapRL++ achieve dense captioning performance comparable to substantially larger models such as Qwen2.5-VL-72B and Qwen3-VL-235B-A22B. These results validate that CapRL++ effectively trains models to produce generalizable, high-fidelity descriptions, establishing a robust foundation beyond the limitations of traditional SFT.

---


### 281. [PriFT: Prior-Support Guided Supervised Fine-Tuning](https://arxiv.org/abs/2606.09396)

**<font color=#1a73e8>作者：</font>** Ke Wang, Shuangqi Li, Mathieu Salzmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is an efficient approach for downstream task adaptation and often serves as the initialization stage for reinforcement learning (RL), but it can show weaker generalization than RL. A key limitation is its off-policy objective: SFT fits fixed demonstrations token by token, including targets poorly aligned with the model's pretrained distribution, which can lead to overfitting. A recent line of work addresses this issue by assigning larger training weights to tokens better aligned with the current model's predictive distribution, with the intuition that fitting these tokens are less distortive to the model's pretrained knowledge and representations. However, computing the token weights from the model that is currently fine-tuned entangles token weights with the optimization trajectory, inducing a self-reinforcing dynamics as the distribution rapidly departs from the pretrained model. To address this, we propose PriFT (Prior-support guided Fine-Tuning), which derives token weights from a frozen pretrained reference to obtain a stable reweighting signal unaffected by fine-tuning. This signal estimates prior support: the extent to which each target token is supported by the pretrained distribution. Across multiple existing token-reweighting rules, replacing the reweighting signal from the online model to pretrained model consistently improves performance. We introduce two instantiations: PriFT-prob uses pretrained token probability, while PriFT-mass selects tokens by cumulative probability mass under the pretrained distribution. Extensive experiments on mathematical reasoning, code generation, and medical question answering show that PriFT achieves state-of-the-art results among SFT baselines and provides a better initialization for subsequent RL training.

---


### 282. [Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models](https://arxiv.org/abs/2606.09401)

**<font color=#1a73e8>作者：</font>** Bartłomiej Marek, Lorenzo Rossi, Vincent Hanke 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has applied differential privacy (DP) to adapt large language models (LLMs) for sensitive applications, offering theoretical guarantees. However, its practical effectiveness remains unclear, partly due to LLM pretraining, where overlaps and interdependencies with adaptation data can undermine privacy despite DP efforts. To analyze this issue in practice, we investigate privacy risks under DP adaptations in LLMs using state-of-the-art attacks such as robust membership inference and canary data extraction. We benchmark these risks by systematically varying the adaptation data distribution, from exact overlaps with pretraining data, through in-distribution (IID) cases, to entirely out-of-distribution (OOD) examples. Additionally, we evaluate how different adaptation methods and different privacy regimes impact the vulnerability. Our results show that distribution shifts strongly influence privacy vulnerability: the closer the adaptation data is to the pretraining distribution, the higher the practical privacy risk at the same theoretical guarantee, even without direct data overlap. We find that parameter-efficient fine-tuning methods, such as LoRA, achieve the highest empirical privacy protection for OOD data. Our benchmark identifies key factors for achieving practical privacy in DP LLM adaptation, providing actionable insights for deploying customized models in sensitive settings. Looking forward, we propose a structured framework for holistic privacy assessment beyond adaptation privacy, to identify and evaluate risks across the full pretrain-adapt pipeline of LLMs.

---


### 283. [What Should a Skill Remember? Quality-Cost Trade-offs in Cost-Aware Skill Rewriting for Language Model Agents](https://arxiv.org/abs/2606.09421)

**<font color=#1a73e8>作者：</font>** Qinghua Xing, Yinda Chen, Yaping Jin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly rely on skills: reusable procedural documents encoding workflows, tool use, implementation patterns, validation checks, and domain rules. Skill rewriting is often treated as prompt compression, but shorter skills can make agents more expensive by removing sparse operational anchors that prevent exploration, debugging, and recovery. We study skill rewriting through this economic lens. Our controlled framework profiles skill structure, rewrites skills using information-preservation strategies, and evaluates the rewrites under fixed task instructions, environments, and verifiers. Experiments on SkillsBench reveal distinct quality--cost trade-offs across strategies: API/code anchoring, workflow guarding, and rule/formula anchoring benefit different task families, with no universally dominant template. In the main held-out evaluation, the learned policy reduces total cost by 7.0\% and downstream agent-token cost by 6.0\%; in frozen cross-model transfer, the corresponding reductions average 14.7\% and 13.7\%, while verifier quality is preserved. These results position skill design as cost-aware operational knowledge engineering rather than prompt compression. Resources: \href{this https URL}{SkillEE}.

---


### 284. [MUDIDI: A Two-Stage Framework for Multilingual Dictionary Digitization with Language Models](https://arxiv.org/abs/2606.09435)

**<font color=#1a73e8>作者：</font>** David Setiawan, Temuulen Khishigsuren, Milind Agarwal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual dictionaries are among the most valuable documentary resources for low-resource and endangered languages, yet many remain available only as scans. For many decades, their digitization and conversion into a machine-readable format was nearly impossible due to language-specific scripts, complex multi-column layouts full of entries with abbreviations and cross-references. Recent vision-language models offer a promising solution, but it is unclear how well they preserve characters, markup, and process lexicographic structure. We introduce MUDIDI, a two-stage framework for multi-lingual dictionary digitization. Stage One evaluates the quality of character recognition and markup preservation; Stage Two focuses on dictionary entry segmentation with subsequent mapping into a machine-readable lexicographic schema, SIL's Multi-Dictionary Formatter. We also release a dataset that consists of human-annotated lexicographic entries collected from 30 public-domain dictionaries featuring diverse writing systems, language families, and formats. We benchmark OCR systems, general-purpose Large Language Models (LLMs), and Vision Language Models (VLMs) on the dataset, demonstrating superior performance of LLMs across most writing systems and languages in both stages, and provide practical guidelines on improving the results for more challenging scenarios. Finally, we show that supplementing additional information, such as dictionary introduction, to the LLMs can improve the quality of the digitized dictionary. Github: this https URL

---


### 285. [SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance](https://arxiv.org/abs/2606.09441)

**<font color=#1a73e8>作者：</font>** Rya Sanovar, Srikant Bharadwaj, Hritvik Taneja 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) injects LLM queries with relevant documents to improve response quality. This injection increases prompt length and slows time to first token (TTFT). Unlike standard queries, RAG queries have a unique property of context reuse where the same documents recur across user queries. Thus, fully recomputing documents for every RAG query does redundant compute and increases TTFT. Prior works precompute KV tensors of RAG documents offline and coarsely recompute some tokens during online prefill. However, such KV reuse is often slower than full recomputation on modern GPUs due to high-latency disk transfers. Further, such a coarse-grained recomputation degrades accuracy.
To address these limitations, this paper proposes SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance. SIFT processes documents offline and extracts fine-grained locations of high attention scores for each document. Next, we identify the following attention invariance insights that enable us to exploit the extracted locations during runtime: (1) Local-Attention Invariance: The location of high attention scores within a document remain invariant to surrounding documents. This helps us predict the location of high scores where the document attends to itself. (2) Cross-Attention Consistency: Keys with high intra-document attention also attract cross-attention from subsequent documents. This helps us predict the location of high scores where the document attends to future documents. Critically, SIFT stores no KV data and only stores locations of high scores in the form of two compact bit vectors. SIFT's storage is up to 24,000x smaller than KV tensors, obviating costly disk transfers. During prefill, SIFT computes the attention only for the marked locations and improves TTFT by 1.71x while holding accuracy within 1% of full recompute.

---


### 286. [Leveraging Morphology for Historical Script Metrological Analysis](https://arxiv.org/abs/2606.09446)

**<font color=#1a73e8>作者：</font>** Malamatenia Vlachou Efstathiou, Raphaël Baena, Dominique Stutzmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in handwritten text recognition have enabled large-scale transcription of historical documents, but still provide limited access to interpretable visual measurements for paleography, the study of historical scripts. In this paper, our main insight is that morphological script analysis, in particular the capacity to learn character prototypes from line-level transcriptions, enables the definition of scalable, meaningful, and stable paleographic measurements. More precisely, we leverage a transformer-based detection architecture together with a prototype-based line reconstruction module to learn prototypical characters and their occurrence, deformation, and positioning.
Our contributions are twofold. First, we introduce a deep architecture and learning methodology that enables efficient character modeling with only line-level transcription supervision, significantly improving over the Learnable Typewriter baseline and enabling accurate character bounding box prediction, unlocking its potential for paleographic measurements. Second, we introduce and demonstrate the paleographical relevance of automatic measurements enabled by our architecture for characters, bi-grams, and spaces between graphical units. For this demonstration, we extend the annotations of the codex Paris, BnF, fr. 2813, commissioned in the late fourteenth century by Charles V and copied by four hands, to 160 pages. We visualize our measurements over these pages, showing how they enable us not only to differentiate graphical profiles, but also to discover and analyze subtle variations. This case study outlines the scalability of our approach and its frugality in terms of required training data, since a single column of text is sufficient to compute our measurements on each of the 160 pages.
Data and code are publicly available at: this https URL.

---


### 287. [AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning](https://arxiv.org/abs/2606.09447)

**<font color=#1a73e8>作者：</font>** Bojie Rong, Zheyu Shen, Qiaoping Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present AliyunConsoleAgent, a web agent framework for automated documentation verification in real-world cloud consoles. Major cloud platforms encompass hundreds of products with rapid feature iteration, causing console UIs to frequently diverge from their corresponding documentation. Verifying that documented procedures accurately reflect the current console and can be executed end-to-end demands an estimated 4 million recurring inspections annually, yet manual coverage remains below 1%. While agent systems built on frontier proprietary models achieve high success rates, their prohibitive cost and data privacy constraints preclude large-scale deployment. We propose a two-stage training paradigm: supervised fine-tuning (SFT) on distilled frontier-model trajectories, followed by reinforcement learning using Group Relative Policy Optimization (GRPO) and a dual-channel outcome reward model in real cloud environments. To support large-scale RL training, we construct a high-determinism rollout system featuring Terraform-based resource pre-provisioning and LLM-driven on-demand provisioning, which effectively isolates environment noise from the training signal. We further introduce a rule-based reward evaluation protocol grounded in backend audit logs, providing objective, reward-hacking-resistant outcome judgment. Our model evolves from mechanical instruction following to autonomous decision-making with cloud console and product-specific understanding. Experiments on a challenging 278-task benchmark where the best frontier model achieves only 65.34% demonstrate that AliyunConsoleAgent-32B achieves a 63.52% mean success rate -- a 20.24 percentage-point improvement over the base model, narrowing the gap to the best frontier proprietary model to 1.82 pp (bootstrap 95% CI [-1.27, 7.39]) -- at 92% lower inference cost.

---


### 288. [TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics](https://arxiv.org/abs/2606.09450)

**<font color=#1a73e8>作者：</font>** QuocViet Pham, Elvir Karimov, Andrey Galichin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs have recently achieved strong results on formal proving benchmarks. However, existing evaluations remain heavily concentrated on competition-style problems and often fail to capture how models behave on longer, more dependency-rich mathematical developments. We introduce TheoremBench, a Lean4 benchmark designed to evaluate theorem provers beyond contest settings. The benchmark is built from nearly one hundred classical theorems and is released in two complementary forms: a plain main version containing one target theorem per instance, and a premised version that expands each theorem into a structured family of related proving tasks consisting of the main theorem together with automatically extracted supporting subtheorems. This design enables evaluation of not only whether the final theorem was proved from scratch, but also of partial progress through the internal proof structure of a theorem. Our experiments show that explicit premises substantially improve performance for Lean4-capable prover models. To provide a comprehensive evaluation, we introduce theorem-level coverage and token-efficiency metrics that expose qualitative differences in proof behavior. The results show that current provers remain strongly biased toward easy subtheorems and often solve theorems through long and inefficient tactic traces rather than compact proof plans. TheoremBench therefore provides a more fine-grained view of formal reasoning ability and highlights the importance of structural benchmark design for evaluating Lean4 theorem provers.

---


### 289. [GD-MIL: Grade-Disentangled Multiple Instance Learning for Multimodal Biochemical Recurrence Prediction in Prostate Cancer](https://arxiv.org/abs/2606.09453)

**<font color=#1a73e8>作者：</font>** Dasari Naga Raju  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biochemical recurrence (BCR) after radical prostatectomy is a critical endpoint in prostate cancer, yet risk stratification relies almost entirely on variables dominated by Gleason grade. Whether H&E whole slide images (WSIs) carry prognostic signal beyond grade, and whether multiple instance learning (MIL) can recover it, remains unsettled. A key obstacle is that many pipelines select model checkpoints on the evaluation fold, artificially inflating concordance. We construct a rigorous benchmark on TCGA-PRAD (487 patients, 101 BCR events) using strict out-of-fold scoring over five-fold cross-validation repeated across five seeds. The choice of MIL aggregator (ABMIL, CLAM, TransMIL, PatchGCN) has little effect (C-index 0.61-0.64 with UNI2-h), while the feature extractor is the dominant factor (ResNet50 0.566 versus pathology foundation models up to 0.639). A clinical Cox model on grade, stage, and age reaches 0.687; no imaging-only model significantly outperforms it (p > 0.10). We introduce Grade-Disentangled MIL (GD-MIL), a gated-attention MIL encoder trained with a gradient-reversal grade adversary that encourages the slide representation to be invariant to Gleason grade before late fusion with clinical variables. GD-MIL achieves C-index 0.704, significantly outperforming both the clinical baseline (delta-c = +0.029, p = 0.0005) and the best imaging-only model (delta-c = +0.062, p = 0.039), suggesting H&E morphology contains prognostic information complementary to grade. A median risk split yields log-rank p < 0.0001 separation in BCR-free survival (~20% vs ~70% at five years).

---


### 290. [Breaking the Tokenizer Barrier: On-Policy Distillation across Model Families](https://arxiv.org/abs/2606.09456)

**<font color=#1a73e8>作者：</font>** Yifan Niu, Han Xiao, Dongyi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-Policy Distillation (OPD) has become a core technique in the post-training of Large Language Models (LLMs) for transferring knowledge from domain experts to student models. However, existing OPD distillation methods require teacher and student models to share the same tokenizer, restricting the applicability of OPD within the model series. Current mainstream practice typically employs Supervised Fine-Tuning (SFT) on teacher-generated responses for cross-tokenizer distillation, which fails to capture the rich knowledge embedded in the teacher's probability distribution. In this work, we enable the standard on-policy distillation method to operate across model families, ensuring that high-fidelity token-level signals can propagate across different tokenizers with a precise token-mapping algorithm. Extensive experiments show that cross-tokenizer OPD is significantly more compute-efficient than baselines on various benchmarks. Our results unlock a broader range of teacher-student pairs for OPD, opening up new avenues for adapting and enhancing interactions between LLMs.

---


### 291. [AbstRAG: Learning to Abstract for Retrieval Problems](https://arxiv.org/abs/2606.09459)

**<font color=#1a73e8>作者：</font>** Lei Xu, Xin Quan, Daniel Pedronette 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation often fails when the query, the document evidence, and the user's intent are expressed at different levels of abstraction. A query may ask about a class, a relation, or an event, while the document only states specific instances, indirect framings, or scoped formulations. We define this mismatch as an abstraction gap: the minimal set of typed assumptions required to align query intent with the available evidence. To close this gap, we introduce AbstRAG, which treats abstraction as an explicit retrieval object. AbstRAG decomposes the query--evidence gap into expression, conceptual, intent--evidence, and event-type components, and scores relevance by combining match quality, a query-independent utility prior, and the cost of the required bridges. Its central mechanism is reflective refinement: a critic diagnoses retrieval failures, localizes the failed abstraction operator, proposes a minimal stage-specific patch, and accepts the patch only under sufficiency and compression controls. Across three within-document retrieval benchmarks against seven baselines, AbstRAG outperforms on nDCG@10 in 18 of 21 paired-bootstrap contrasts and improves generation accuracy by 1.9%, 5.2%, and 4.0% across the three benchmarks; ablations confirm that reflective refinement drives most of the retrieval gain and the compression control alone reduces over-expansion false positives from 73.7% to 0% on a stress slice.

---


### 292. [H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions](https://arxiv.org/abs/2606.09461)

**<font color=#1a73e8>作者：</font>** Shiping Zhu, Yibo Yang, Zhengyang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly deployed in human-human interaction settings, such as meeting assistants and clinical documentation systems, where they must observe conversations and retain information for downstream queries. Unlike traditional human-assistant settings, these environments are inherently multimodal, involve complex discourse phenomena such as anaphora and deixis, and contain asynchronous or conflicting information from multiple participants. However, existing memory benchmarks largely focus on single-user, text-only interactions, failing to capture these challenges. To address this gap, we introduce H2HMem, a Human-to-Human Multimodal Memory Benchmark for evaluating memory capabilities in complex human-human interactions. H2HMem includes both dyadic and multi-party conversations with multimodal information streams, and evaluates agents along three dimensions: memory recall, reasoning, and application. Experiments with advanced agents reveal substantial limitations in constructing, retaining, and utilizing memories across modalities, participants, and sessions, highlighting substantial room for improvement in next-generation LLM agents.

---


### 293. [DECSELFMASK: Leveraging Unlabeled Text via Self-Relevance-Guided Masking for Decoder-Only Classification](https://arxiv.org/abs/2606.09466)

**<font color=#1a73e8>作者：</font>** Pietro Ferrazzi, Matteo Merler, Giovanni Bonetta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Classification tasks require annotated data, which can often be expensive, time-consuming, or even unfeasible to collect. This is the case of the medical domain, where large datasets often have few annotated examples. To address this, we propose DecSelfMask (Decoder Self-learning by Masking), an approach to enhance decoder-only performance on classification tasks. We build on common self-learning approaches by leveraging a model to create training examples from unlabeled data to propose a novel relevance-guided masking strategy. We use relevance attribution methods to determine what portions of unannotated texts are relevant for a task. We then create self-supervised training examples by masking out those portions, training the model to reconstruct them via next-token-prediction. We hypothesize that those examples convey knowledge about the structure and semantics of unannotated data that can be useful for downstream performance. We test our approach on 136 tasks from a collection of 1.9M clinical notes from an Italian hospital. We quantify DecSelfMask's impact on downstream tasks on 5 models of different scales and families, including a probing analysis. Experiments show consistent gains, outperforming standard supervised fine-tuning approaches (+19.9 points in Macro F1), synthetic label generation (+12.5), and continual pretraining (+6.3), as well as common baselines.

---


### 294. [A Finetuned SpeechLLM for Joint Multi-Granular L2 Assessment and Natural-Language Rationales](https://arxiv.org/abs/2606.09470)

**<font color=#1a73e8>作者：</font>** Aditya Kamlesh Parikh, Cristian Tejedor-Garcia, Catia Cucchiarini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated L2 speech assessment can assign proficiency labels, but often lacks interpretability. We propose a rubric-guided SpeechLLM for multi-aspect, multi-granular assessment, trained with a hybrid objective combining supervised fine-tuning and Bounded Direct Preference Optimization. The model jointly predicts ordinal labels at the sentence-level (accuracy, fluency, prosody), word/phoneme-level accuracy, and generates a natural-language rationale in the same response. On SpeechOcean762, our approach matches or outperforms single-granularity models while remaining competitive with prior approaches. We analyze rationale reliability along two axes: self-consistency with model predictions and alignment with ground-truth labels, using sentiment consistency (plausibility) and mention-based agreement (faithfulness). Rationales are plausible at the sentence level, but faithfulness degrades at the word/phoneme level: references are sparse and weakly aligned with token-level labels.

---


### 295. [Emergent alignment and the projectability of ethical personas](https://arxiv.org/abs/2606.09475)

**<font color=#1a73e8>作者：</font>** Guillermo Del Pinal, Youngchan Lee, Cameron McNamara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Work on `emergent misalignment' shows that finetuning LLMs on narrow tasks can induce broadly misaligned behavior. This supports the `persona selection' (PSM) hypothesis: during pre-training, LLMs learn to simulate different characters and perspectives, which can be elicited and refined during post-training. This paper investigates the converse phenomenon, `emergent alignment', and uses it to support and refine the PSM and motivate a novel desideratum for alignment. We finetune a helpful-only model on broad and narrow safety tasks. To create SFT samples, we follow the `Constitutional AI' (CAI) approach and use four constitutions which encode reasonable alignment strategies: deontology, consequentialism, virtue ethics, and aligning AIs as subordinate to human authority. For each of those models, we show that finetuning on two narrow safety sub-categories reliably induces emergent alignment over a representative set of general safety categories, and on safety subcategories that we directly filtered-out of the data sets used for narrow alignment. To test the `PSM' using a more fine-grained evaluation, we used a multidimensional `ethical persona' diagnostic. For each constitutionally finetuned (broad/narrow) model, we evaluate how well their behavior matches their expected signature profile. Our results show that our CAI models acquire their expected ``ethical persona'' -- e.g., the model narrowly fine-tuned on SFT samples created using the consequentialist constitution agrees significantly more with utilitarian than deontological beliefs. Yet our coarse and fine-grained evaluations show that there are significant differences across our (broad/narrow) finetuned CAI models in how well they project. We conclude that alignment strategies should be evaluated, not just on their (in-distribution) general safety performance, but also specifically on their degree of projectability.

---


### 296. [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.09483)

**<font color=#1a73e8>作者：</font>** Tianxiang Fei, Mingyang Song, Mao Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory for an LLM agent is more than retrieving the right passage at the right time. Current memory systems collapse belief revision, causal coupling, and cross-domain abstraction into a single retrieval surface tuned for surface recall, and consequently struggle on implicit personalisation that requires reasoning over how a user has evolved. We propose DCPM, which reorganises agent memory along a cognitive capability hierarchy ascending from raw inputs and atomic facts, through diachronic belief trajectories and identity, to domain schemas, latent intentions and cross-domain patterns. The hierarchy is driven by two processes inheriting the architectural split of dual-process theory: a synchronous daytime writer (System1) that records belief revisions as doubly linked supersedes chains, and an asynchronous nighttime engine (System2) that induces schemas and intentions and sweeps for cross-domain collisions abstracted into higher-level core schemas. On LongMemEval, PersonaMem and PersonaMem-v2, enabling System2 contributes most where the benchmark rewards implicit cross-session inference (up to +5.20 on PersonaMem-v2) and least on span recall, matching the architectural prediction.

---


### 297. [Detecting Differences Is Not Understanding Structure: Large Language Models Fail at Graph Isomorphism](https://arxiv.org/abs/2606.09484)

**<font color=#1a73e8>作者：</font>** Kumar Thushalika, Sukumar Kishanthan, Asela Hevapathige  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown impressive performance on diverse reasoning tasks, yet their capacity for structural reasoning in graphs remains unclear. We investigate whether LLMs can genuinely understand graph isomorphism -a fundamental problem in graph theory. While LLMs achieve near-perfect accuracy on isomorphism detection, we show this performance is illusory. When identical graphs are presented with permuted node labels, LLMs fail to identify their isomorphism. This finding suggests that LLMs exploit patterns rather than reasoning about abstract graph structure. Since permutation invariance is a fundamental requirement for valid structural reasoning, these results indicate that success on graph reasoning benchmarks should not be interpreted as evidence of genuine topological understanding.

---


### 298. [LLM-Orchestrated Conformance Checking in Stroke Care Without Computer-Interpretable Guidelines](https://arxiv.org/abs/2606.09489)

**<font color=#1a73e8>作者：</font>** Giorgio Leonardi, Stefania Montani, Manuel Striani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective: Conformance checking in healthcare seeks to assess whether patient care pathways adhere to clinical guidelines. However, its practical application often depends on the availability of formal, machine-interpretable representations of guidelines, such as Computer-Interpretable Guidelines (CIGs), which are seldom available in real-world clinical settings.
Methods: This work introduces a modular framework based on the orchestration of Large Language Models (LLMs) to support medical conformance checking directly from unstructured clinical and guideline texts, without requiring predefined CIGs. The proposed architecture integrates multiple LLMs and supporting components to extract patient traces from clinical discharge letters, identify normative rules from textual clinical guidelines, translate these rules into executable scripts, and compute a Trace Conformance Indicator to quantify compliance within the event log.
Results: The framework was implemented and evaluated in the stroke care domain at the neurological ward of Alessandria Hospital. Hundreds of patient traces were automatically extracted from hospital data and assessed against 50 rules derived from the reference guideline. The analysis showed that more than 86\% of the available traces were conformant.
Conclusion: The results demonstrate the feasibility of using orchestrated LLMs for practical healthcare conformance analysis. At the same time, the study provides evidence of a high level of adherence to stroke care guidelines at Alessandria Hospital.

---


### 299. [Deterministic Integrity Gates for LLM-Assisted Clinical Manuscript Preparation: An Auditable Biomedical Informatics Architecture](https://arxiv.org/abs/2606.09500)

**<font color=#1a73e8>作者：</font>** Yoojin Nam, Jinhoon Jeong, Namkug Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective. Large language models (LLMs) increasingly draft clinical research manuscripts, but their fluency can hide fabricated citations, numbers that drift from source tables, and unmet reporting-guideline items. Existing tools generate text without verifying it, and self-critique inherits the blind spots that produce confident fabrication. We describe an architecture that pairs generation with verification. Methods. The design rests on three principles: decompose the workflow into self-contained skills, gate every stage transition with halt-on-failure, and resolve each integrity question with the cheapest sufficient mechanism -- a deterministic, re-executable check where one suffices, and a prose-level probe only where interpretation is unavoidable. This determinism-where-possible split, organized as an integrity-gate taxonomy, is the core contribution. It is realized as MedSci Skills, an open-source toolkit of 43 skills coordinated by one orchestrator, whose deterministic tier comprises 21 standard-library detectors. We evaluate it on three reproducible public-dataset pipelines (STARD, PRISMA, STROBE) and a seeded-defect ablation. Results. Across the three pipelines every content-hash manifest verified clean and the gates surfaced real defects. On 27 identical injected defects the deterministic gates detected all 27 with no false positives on the matched clean fixtures, whereas a generic single-prompt LLM reviewer detected 11, its misses concentrated in generated-code, bibliography-internal, and style defects the prose does not expose. Conclusion. Determinism-where-possible verification yields an auditable, re-executable trail that exposes the evidence a human needs to check an LLM-assisted manuscript -- feasibility and reproducibility evidence, not a claim of human-competitive quality, which a separate blinded study addresses. MedSci Skills is MIT-licensed and archived (v3.8.0).

---


### 300. [Prisma-World: Camera-Controllable Multi-Agent Video World Model](https://arxiv.org/abs/2606.09507)

**<font color=#1a73e8>作者：</font>** Huiqiang Sun, Zhan Peng, Size Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models have made rapid progress in generating controllable visual experiences, but most of them still simulate the world from a single observer. Extending such models to multiple agents raises a central challenge: if each agent's future state is generated independently, overlapping views may instantiate different versions of the same scene, leading to inconsistent objects, layouts, and appearances across agents. Conventional camera conditioning controls individual trajectories, but it does not explicitly couple the generation of views that should agree under shared scene geometry. We introduce Prisma-World, a camera-controllable multi-agent world model that formulates multi-agent generation as a joint geometry-aware denoising process for cross-view consistency. Prisma-World processes all agent videos within one full-attention sequence, uses a multi-agent RoPE design to distinguish agent identities while preserving synchronized temporal coordinates, and injects relative camera geometry into attention to bias overlapping viewpoints toward shared scene evidence. To further strengthen multi-view consistency and enhance global spatial perception, we augment our framework with an overlap-decaying curriculum training paradigm alongside minimap-conditioned structural guidance. To facilitate the training and evaluation of multi-agent models, we introduce PrismaDataset, a large-scale UE5 dataset with panoramic acquisition across diverse scenes, composable multi-agent view groups with flexible agent counts and complex camera trajectories, and precise camera/action annotations for consistency training and evaluation. Experiments show that a single Prisma-World model can generate high-fidelity multi-agent videos with flexible agent numbers, camera controllability, improved cross-view consistency, and spatial grounding under minimap guidance.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-331](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

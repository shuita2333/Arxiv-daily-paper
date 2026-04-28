# 🧠 大模型相关研究 | 2026年04月29日

> 本类共 **215** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-215](./part-05.md)

---

### 1. [A learning health system in Neurorehabilitation as a foundation for multimodal patient representation](https://arxiv.org/abs/2604.22763)

**<font color=#1a73e8>作者：</font>** Thomas Weikert, Eljas Roellin, Lukas Heumos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Neurological disorders represent a growing global health burden requiring long-term, interdisciplinary rehabilitation. Computational neurorehabilitation (compNR) - the use of data-driven and model-based approaches to personalize treatment - offers new opportunities for precision rehabilitation. However, its clinical deployment is limited by fragmented data systems, poor interoperability, and low clinician engagement in model development. We embed the learning health system (LHS) framework in Neurorehabilitation through integration of multimodal data collection, model computation, and clinical visualization that enables clinician-ML collaboration in everyday neurorehabilitation practice. The system facilitates structured digital data capture, secure computational processing, and interoperable visualization of patient trajectories. Through a real-world deployment in stroke rehabilitation, we demonstrate how such an infrastructure bridges the gap between research models and clinical use, showcasing one approach to a translational pathway for compNR.

---


### 2. [The Randomness Floor: Measuring Intrinsic Non-Randomness in Language Model Token Distributions](https://arxiv.org/abs/2604.22771)

**<font color=#1a73e8>作者：</font>** Jarosław Hryszko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models cannot be random. This paper introduces Entropic Deviation (ED), the normalised KL divergence between a model's token distribution and the uniform distribution, and measures it systematically across 31,200 generations spanning seven models, two architectures (transformer and state space), nine prompt categories, three temperatures, and five languages. Under semantically neutral prompts (empty strings, random characters, nonsense syllables) transformers still exhibit ED of approximately 0.30, meaning that 88-93% of the non-randomness observed under semantic prompts is intrinsic to the learned weights rather than induced by context. Three transformer families (Gemma, Llama, Qwen) converge on nearly identical ED values despite different training data and vocabularies. A state space model (Mamba2) reveals a qualitatively different regime: twice the ED, three times lower within-sequence variance, and massive sensitivity to temperature (r = -0.78) where transformers are nearly immune (r < 0.05). Cross-lingual experiments with Qwen-32B show a stable gradient across five languages (English, Japanese, Chinese, Polish, Arabic) that does not correlate with token fertility and persists when two languages sharing an identical tokeniser subset are compared. These findings establish a structural lower bound on randomness in pretrained language models, characterise how this bound differs across architectures, and demonstrate that language itself modulates the bound independently of tokenisation.

---


### 3. [Trace Mutation in Human-LLM Dialogue: The Transcript as Forensic and Mitigation Surface](https://arxiv.org/abs/2604.22773)

**<font color=#1a73e8>作者：</font>** William J. Bensen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as partners in knowledge work, where the shared conversational record functions as the decision record that safeguards work continuity. We characterize a class of context failures we term trace mutations, in which distortions enter the shared record while presenting as grounded continuity. We describe two forms: utterance effacement, in which an interlocutor's contribution is re-presented with altered substance, and genitive dissociation, in which a model loses authorship of its own contributions. Using a schematic illustration and two naturalistic anchor cases, we show how these failures differ from confabulation and sycophancy and why they resist ordinary conversational repair. Preliminary cross-model elicitation suggests that at least one such failure is highly camouflaged to contemporary models. We situate the phenomena within grounding and repair theory and discuss implications for tool design.

---


### 4. [Cognitive Alignment Deciphered: A Self-Developed Scenario-Based Prompt Scale Coupled with Representational Similarity Analysis and Social Network Analysis for Unraveling Bias Mechanisms Across Humans and LLMs](https://arxiv.org/abs/2604.22775)

**<font color=#1a73e8>作者：</font>** Chengrui Zhou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional cognitive bias measurement tools are limited by narrow bias coverage, low ecological validity, and reliance on abstract self reports, constraining scenario based and human AI comparisons. We introduce the context based Cognitive Bias Assessment Scale CBAS, a scenario driven prompt template covering 58 cognitive biases across five hot cold dual system dimensions: Calculation, Belief, Information, Social, and Memory. Psychometric testing with 330 participants shows satisfactory reliability Cronbachs alpha 0.714 and good model fit chi squared df 1.83, RMSEA 0.057, CFI 0.908, TLI 0.903. We then combine Representational Similarity Analysis RSA and Social Network Analysis SNA to compare human age groups and three large language models Baidu ERNIE 3.5 8K, DeepSeek V3, DeepSeek R1. Humans show coherent hot cold integration with high inter individual variability, whereas LLMs display fragmented, inflexible response patterns and lower variability. Human cognitive networks exhibit strong inter module connectivity, while LLMs show fixed core biases and isolated information processing components. Prompt interventions integrating role playing and bias mitigation instructions effectively improve LLM response accuracy, reaching 84.86 percent for DeepSeek R1 and 78.24 percent for DeepSeek V3, and partially reshape their internal representations. Our work establishes a replicable assessment and analysis pipeline for cognitive alignment research, bridging empirical psychological evaluation and interpretable artificial intelligence.

---


### 5. [KARL: Mitigating Hallucinations in LLMs via Knowledge-Boundary-Aware Reinforcement Learning](https://arxiv.org/abs/2604.22779)

**<font color=#1a73e8>作者：</font>** Cheng Gao, Cheng Huang, Kangyang Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enabling large language models (LLMs) to appropriately abstain from answering questions beyond their knowledge is crucial for mitigating hallucinations. While existing reinforcement learning methods foster autonomous abstention, they often compromise answer accuracy because their static reward mechanisms, agnostic to models' knowledge boundaries, drive models toward excessive caution. In this work, we propose KARL, a novel framework that continuously aligns an LLM's abstention behavior with its evolving knowledge boundary. KARL introduces two core innovations: a Knowledge-Boundary-Aware Reward that performs online knowledge boundary estimation using within-group response statistics, dynamically rewarding correct answers or guided abstention; and a Two-Stage RL Training Strategy that first explores the knowledge boundary and bypasses the "abstention trap", and subsequently converts incorrect answers beyond the knowledge boundary into abstentions without sacrificing accuracy. Extensive experiments on multiple benchmarks demonstrate that KARL achieves a superior accuracy-hallucination trade-off, effectively suppressing hallucinations while maintaining high accuracy across both in-distribution and out-of-distribution scenarios.

---


### 6. [Parameter Efficiency Is Not Memory Efficiency: Rethinking Fine-Tuning for On-Device LLM Adaptation](https://arxiv.org/abs/2604.22783)

**<font color=#1a73e8>作者：</font>** Irene Tenison, Stella Ahn, Miriam Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-Efficient Fine-Tuning (PEFT) has become the standard for adapting large language models (LLMs). In this work we challenge the wide-spread assumption that parameter efficiency equates memory efficiency and on-device adaptability. We show that this is not true - while methods like LoRA and IA3 significantly reduce trainable parameters, they remain bound by intermediate tensors that scale linearly with sequence length, often triggering out-of-memory errors on-device. In this work, we introduce LARS (Low-memory Activation-Rank Subspace), a novel adaptation framework that decouples memory consumption from sequence length. While prior PEFT methods apply low-rank constraints to model parameters, LARS instead constrains the activation subspace used during training, directly targeting the dominant source of memory consumption and fundamentally flattening the memory growth rate. LARS reduces the memory footprint by an average of 33.54% on GPUs and 51.95% on CPUs in comparison to LoRA across reasoning, understanding and long-context datasets using different models while maintaining competitive accuracy and throughput. Besides GPUs, we deploy on Raspberry Pi and consumer-grade CPUs to demonstrate that LARS provides a scalable path for sophisticated LLM personalization on resource-constrained hardware and edge devices.

---


### 7. [CoFi-PGMA: Counterfactual Policy Gradients under Filtered Feedback for Multi-Agent LLMs](https://arxiv.org/abs/2604.22785)

**<font color=#1a73e8>作者：</font>** Stela Tong, Elai Ben-Gal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) deployments increasingly rely on multi-agent architectures in which multiple models either compete through routing mechanisms or collaborate to produce a final answer. In both settings, the learning signal received by each agent is filtered by the system mechanism. Routing produces selection-gated feedback where only the chosen response is evaluated, while collaboration produces shared rewards that obscure the individual contribution of each agent. As a result, standard RLHF objectives designed for a single deployed policy become misspecified. We introduce CoFi-PGMA (Counterfactual Policy Gradients under Filtered Feedback for Multi-Agent LLMs), a unified framework for learning under filtered feedback in multi-agent LLM systems. Our approach derives a counterfactual per-agent training objective based on marginal contribution, which corrects the learning signal under both routing and collaborative mechanisms. For routing systems, the objective corresponds to off-policy corrections for selection-gated feedback, while for collaborative systems it reduces to leave-one-out difference rewards for credit assignment. We further analyze how softmax routing induces risk-sensitive incentives and provide practical training algorithms that integrate counterfactual estimators, multiturn-aware rewards, and policy optimization methods, and demonstrate the approach on a real-world reasoning dataset.

---


### 8. [Complete Cyclic Subtask Graphs for Tool-Using LLM Agents: Flexibility, Cost, and Bottlenecks in Multi-Agent Workflows](https://arxiv.org/abs/2604.22820)

**<font color=#1a73e8>作者：</font>** Luay Gharzeddine, Samer Saab Jr  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Long-horizon tool-using tasks sometimes benefit from revisiting earlier subtasks for recovery and exploration, but added multi-agent workflow flexibility can also introduce coordination overhead and substantial inference cost. We study complete cyclic subtask graphs, a deliberately maximally flexible multi-agent architecture in which executable subtask nodes are fully connected and a unified state-analysis-and-routing agent selects transitions using natural-language criteria. This makes unrestricted revisitation explicit and directly analyzable at the subtask level. We evaluate task-specific (Spec-Cyc) and benchmark-generic (Gen-Cyc) graphs on TextCraft, ALFWorld, and Finance-Agent, with ablations over planner/executor/router strength, tool exposure (generalist vs specialized), $n$-shot successful trajectory summaries, and fault-injected random subtask perturbations. The benchmarks expose three distinct regimes. ALFWorld highlights a setting where explicit revisitation supports recovery and exploration; TextCraft, a largely prerequisite-chain domain, often favors the efficiency of simpler forward execution; and Finance-Agent remains bottlenecked by retrieval, grounding, and evidence synthesis more than by workflow flexibility alone. Shared-win token comparisons further show that the added flexibility can be substantially more expensive than a single ReAct agent. Overall, we use complete cyclic subtask graphs as a maximally flexible experimental lens for measuring when multi-agent revisitation helps, when it mainly adds coordination cost, and when external task bottlenecks dominate.

---


### 9. [DO-Bench: An Attributable Benchmark for Diagnosing Object Hallucination in Vision-Language Models](https://arxiv.org/abs/2604.22822)

**<font color=#1a73e8>作者：</font>** JiYang Wang, Jiawei Chen, Mengqi Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object level hallucination remains a central reliability challenge for vision language models (VLMs), particularly in binary object existence verification. Existing benchmarks emphasize aggregate accuracy but rarely disentangle whether errors stem from perceptual limitations or from the influence of contextual textual priors, leaving underlying failure mechanisms ambiguous. We introduce DO-Bench, a controlled diagnostic benchmark that isolates these sources through structured multimodal interventions. Rather than evaluating models in unconstrained settings, DO-Bench probes two complementary dimensions: the Prior Override dimension progressively strengthens contextual textual priors while holding visual evidence constant to assess resistance to prior pressure, and the Perception-Limited dimension incrementally enhances visual evidence from full-scene context to localized object crops to measure perceptual grounding strength. This paired design enables attribution of errors to prior suppression, perceptual insufficiency, or their interaction. We further define two diagnostic metrics, PriorRobust and PerceptionAbility, to quantify these behaviors consistently. Evaluations across diverse open- and closed-source VLMs reveal systematic differences in prior sensitivity and perceptual reliability, demonstrating that object hallucination reflects heterogeneous, mechanism dependent failure patterns beyond aggregate accuracy.

---


### 10. [PivotMerge: Bridging Heterogeneous Multimodal Pre-training via Post-Alignment Model Merging](https://arxiv.org/abs/2604.22823)

**<font color=#1a73e8>作者：</font>** Zibo Shao, Baochen Xiong, Xiaoshan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) rely on multimodal pre-training over diverse data sources, where different datasets often induce complementary cross-modal alignment capabilities. Model merging provides a cost-effective mechanism for integrating multiple expert MLLMs with complementary strengths into a unified model. However, existing model merging research mainly focuses on post-finetuning scenarios, leaving the pre-training stage largely unexplored. We argue that the core of MLLM pre-training lies in establishing effective cross-modal alignment, which bridges visual and textual representations into a unified semantic space. Motivated by this insight, we introduce the post-alignment merging task, which aims to integrate cross-modal alignment capabilities learned from heterogeneous multimodal pre-training. This setting introduces two key challenges: cross-domain parameter interference, where parameter updates learned from different data distributions conflict during merging, and layer-wise alignment contribution disparity, where different layers and projectors contribute unevenly to cross-modal alignment. To address them, we propose \textbf{PivotMerge}, a post-alignment merging framework for cross-modal projectors. PivotMerge incorporates two key components: Shared-space Decomposition and Filtering, which disentangles shared alignment patterns from domain-specific variations and suppresses conflicting directions, and Alignment-guided Layer-wise Merging, which assigns layer-specific merging weights based on differing alignment contributions. We construct systematic CC12M-based post-alignment merging scenarios for evaluation. Extensive experiments on multiple multimodal benchmarks show that PivotMerge consistently outperforms existing baselines, demonstrating its effectiveness and generalization ability.

---


### 11. [Shape: A Self-Supervised 3D Geometry Foundation Model for Industrial CAD Analysis](https://arxiv.org/abs/2604.22826)

**<font color=#1a73e8>作者：</font>** Bayangmbe Mounmo, Sam Chien, Mile Mitrovic  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial CAD workflows require robust, generalizable 3D geometric representations supporting accuracy and explainability. We introduce Shape, a self-supervised foundation model converting surface meshes into dense per-token embeddings. Shape combines a structured 3D latent grid, a multi-scale geometry-aware tokenizer (MAGNO) with cross-attention, and a transformer processor using grouped-query attention and RMSNorm. A learned reconstruction prior enables per-region attribution for explainable predictions. Pretraining uses masked-token reconstruction of normalized geometry statistics and multi-resolution contrastive consistency. The 10.9M-parameter backbone is pretrained on 61,052 CAD meshes from Thingi10K, MFCAD, and Fusion360. On a held-out split of 2,983 meshes, Shape achieves reconstruction R2 = 0.729 and 98.1% top-1 retrieval under the Wang-Isola protocol, with near-zero reconstruction train/val gap (contrastive scores use a larger evaluation pool). A 2x2 ablation on loss type and target-space normalization shows per-dimension normalization is critical: without it, performance collapses (R2 < 0.14, top-1 < 88%); with it, both losses succeed (R2 > 0.70, top-1 > 96%). Smooth-L1 offers secondary stability. Code, embeddings, and an interactive demo are released at this https URL.

---


### 12. [Lost in the Vibrations: Vision Language Models Fail the Dynamic Gauges Test](https://arxiv.org/abs/2604.22829)

**<font color=#1a73e8>作者：</font>** Tairan Fu, Francisco Javier Santos-Martín, Javier Conde 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The digital transformation of industrial manufacturing increasingly relies on the ability of autonomous robots to interact with legacy infrastructure, particularly analog gauges. While Vision-Language Models (VLMs) have demonstrated potential in zero-shot instrument recognition, their deployment in measurement systems remains constrained by an inherent inability to accurately analyze high-frequency temporal events and needle vibrations. This paper evaluates state-of-the-art models, including GPT-5 and Gemini 3, against the strict requirements of metrology and uncertainty quantification. To facilitate this evaluation, we introduce a novel dataset comprising video sequences of various gauge types: circular, linear, and Vernier, under diverse motion speed profiles. Our findings indicate that current VLMs exhibit limited ability in interpreting needle trajectories and scale semantics, failing to provide the traceability and reliability needed for safety-critical monitoring. The results demonstrate that these models have not yet achieved the performance necessary to be classified as trustworthy synthetic instruments under existing IEEE and ISO standards.

---


### 13. [2D Pre-Training for 3D Pose Estimation](https://arxiv.org/abs/2604.22830)

**<font color=#1a73e8>作者：</font>** Liyao Jiang, Ruichen Chen, Keith G. Mills  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-training is a general method that is used in a range of deep learning tasks. By first training a model on one task, and then further training on the downstream task used for final evaluation, the model is forced to learn a more general understanding of the input data. While pre-training has been applied to 3D Human Pose Estimation (HPE) previously, the scope of datasets used is typically very limited to some strong benchmarks, like Human3.6M. Therefore, in this project, we expand the scope of an existing 3D HPE scheme to be compatible with additional 2D and 3D HPE datasets, like Occlusion Person. We perform an extensive study on how aspects of 2D pre-training, such as model size, affect downstream performance, and to what extent pre-training can help the model generalize to different datasets. Experimental results show that 2D pre-training consistently outperforms training on 3D data alone, particularly in terms of computational efficiency. Finally, using MPII and Human3.6M, we are able to obtain an MPJPE score of under 64.5mm.

---


### 14. [Intervention-Aware Multiscale Representation Learning from Imaging Phenomics and Perturbation Transcriptomics](https://arxiv.org/abs/2604.22832)

**<font color=#1a73e8>作者：</font>** Jiayuan Chen, Ruoqi Liu, Zishan Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Microscopy-based phenotypic profiling is scalable for drug discovery but lacks the mechanistic depth of transcriptomics, which remains costly and scarce. Existing multimodal approaches either use images to support other modalities or naively align representations by sample identity, ignoring cell-type and dose variations in weakly paired data-limiting generalization to unseen interventions. In this paper, we introduce an intervention-aware distillation framework that leverages perturbational transcriptomics to guide image representation learning. A transcriptome-conditioned teacher integrates gene expression and intervention metadata to produce soft distributions over a chemistry-aware codebook organized by drug similarity. The teacher employs a fine-tuned single-cell foundation model to encode cell-type context and disentangle dose effects. An image-only student learns to predict these distributions from microscopy alone, distilling mechanistic knowledge while operating independently at test time. This design emphasizes intervention semantics rather than identity alignment and explicitly handles dose and cell-type mismatches. We provide theoretical guarantees showing that transcriptomic guidance tightens the risk bound for image-based prediction. On Cell Painting and RxRx datasets paired with L1000, our method significantly improves one-shot transfer to unseen interventions and drug-target gene discovery compared to self-supervised and alignment baselines.

---


### 15. [Neural Network Optimization Reimagined: Decoupled Techniques for Scratch and Fine-Tuning](https://arxiv.org/abs/2604.22838)

**<font color=#1a73e8>作者：</font>** Xin Ning, Qiankun Li, Xiaolong Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the accumulation of resources in the era of big data and the rise of pre-trained models in deep learning, optimizing neural networks for various tasks often involves different strategies for fine-tuning pre-trained models versus training from scratch. However, existing optimizers primarily focus on reducing the loss function by updating model parameters, without fully addressing the unique demands of these two major paradigms. In this paper, we propose DualOpt, a novel approach that decouples optimization techniques specifically tailored for these distinct training scenarios. For training from scratch, we introduce real-time layer-wise weight decay, designed to enhance both convergence and generalization by aligning with the characteristics of weight updates and network architecture. For more importantly fine-tuning, we integrate weight rollback with the optimizer, incorporating a rollback term into each weight update step. This ensures consistency in the weight distribution between upstream and downstream models, effectively mitigating knowledge forgetting and improving fine-tuning performance. Additionally, we extend the layer-wise weight decay to dynamically adjust the rollback levels across layers, adapting to the varying demands of different downstream tasks. Extensive experiments across diverse tasks, including image classification, object detection, semantic segmentation, and instance segmentation, demonstrate the broad applicability and state-of-the-art performance of DualOpt. Code is available at this https URL.

---


### 16. [AeSlides: Incentivizing Aesthetic Layout in LLM-Based Slide Generation via Verifiable Rewards](https://arxiv.org/abs/2604.22840)

**<font color=#1a73e8>作者：</font>** Yiming Pan, Chengwei Hu, Xuancheng Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong potential in agentic tasks, particularly in slide generation. However, slide generation poses a fundamental challenge: the generation process is text-centric, whereas its quality is governed by visual aesthetics. This modality gap leads current models to frequently produce slides with aesthetically suboptimal layouts. Existing solutions typically rely either on heavy visual reflection, which incurs high inference cost yet yields limited gains; or on fine-tuning with large-scale datasets, which still provides weak and indirect aesthetic supervision. In contrast, the explicit use of aesthetic principles as supervision remains unexplored. In this work, we present AeSlides, a reinforcement learning framework with verifiable rewards for Aesthetic layout supervision in Slide generation. We introduce a suite of meticulously designed verifiable metrics to quantify slide layout quality, capturing key layout issues in an accurate, efficient, and low-cost manner. Leveraging these verifiable metrics, we develop a GRPO-based reinforcement learning method that directly optimizes slide generation models for aesthetically coherent layouts. With only 5K training prompts on GLM-4.7-Flash, AeSlides improves aspect ratio compliance from 36% to 85%, while reducing whitespace by 44%, element collisions by 43%, and visual imbalance by 28%. Human evaluation further shows a substantial improvement in overall quality, increasing scores from 3.31 to 3.56 (+7.6%), outperforming both model-based reward optimization and reflection-based agentic approaches, and even edging out Claude-Sonnet-4.5. These results demonstrate that such a verifiable aesthetic paradigm provides an efficient and scalable approach to aligning slide generation with human aesthetic preferences. Our repository is available at this https URL.

---


### 17. [EX-FIQA: Leveraging Intermediate Early eXit Representations from Vision Transformers for Face Image Quality Assessment](https://arxiv.org/abs/2604.22842)

**<font color=#1a73e8>作者：</font>** Guray Ozgur, Tahar Chettaoui, Eduarda Caldeira 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Image Quality Assessment is crucial for reliable face recognition systems, yet existing Vision Transformer-based approaches rely exclusively on final-layer representations, ignoring quality-relevant information captured at intermediate network depths. This paper presents the first comprehensive investigation of how intermediate representations within ViTs contribute to face quality assessment through early exit mechanisms and score fusion strategies. We systematically analyze all twelve transformer blocks of ViT-FIQA architectures, demonstrating that different depths capture distinct and complementary quality-relevant information, as evidenced by varying attention patterns and performance characteristics across network layers. We propose a score fusion framework that combines quality predictions from multiple transformer blocks without architectural modifications or additional training. Our early exit analysis reveals optimal performance-efficiency trade-offs, enabling significant computational savings while maintaining competitive performance. Through extensive evaluation across eight benchmark datasets using four FR models, we demonstrate that our fusion strategy improves upon single-exit approaches. Our proposed quality fusion approach employs depth-weighted averaging that assigns progressively higher importance to deeper transformer blocks, achieving the best quality assessment performance by effectively leveraging the hierarchical nature of feature learning in ViTs. Our work challenges the conventional wisdom that only deep features matter for face analysis, revealing that intermediate representations contain valuable information for quality assessment. The proposed framework offers practical benefits for real-world biometric systems by enabling adaptive computation based on resource constraints while maintaining competitive quality assessment capabilities.

---


### 18. [EgoDyn-Bench: Evaluating Ego-Motion Understanding in Vision-Centric Foundation Models for Autonomous Driving](https://arxiv.org/abs/2604.22851)

**<font color=#1a73e8>作者：</font>** Finn Rasmus Schäfer, Yuan Gao, Dingrui Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Vision-Language Models (VLMs) have advanced highlevel reasoning in autonomous driving, their ability to ground this reasoning in the underlying physics of ego-motion remains poorly understood. We introduce EgoDyn-Bench, a diagnostic benchmark for evaluating the semantic ego-motion understanding of vision-centric foundation models. By mapping continuous vehicle kinematics to discrete motion concepts via a deterministic oracle, we decouple a model's internal physical logic from its visual perception. Our large-scale empirical audit spanning 20 + models, including closed-source MLLMs, open-source VLMs across multiple scales, and specialized VLAs, identifies a significant Perception Bottleneck: while models exhibit logical physical concepts, they consistently fail to accurately align them with visual observations, frequently underperforming classical non-learned geometric baselines. This failure persists across model scales and domain-specific training, indicating a structural deficit in how current architectures couple visual perception with physical reasoning. We demonstrate that providing explicit trajectory encodings substantially restores physical consistency across all evaluated models, revealing a functional disentanglement between vision and language: egomotion logic is derived almost exclusively from the language modality, while visual observations contribute negligible additional signal. This structural finding provides a standardized diagnostic framework and a practical pathway toward physically aligned embodied AI. Keywords: Ego-motion - Physical Reasoning - Foundation Models

---


### 19. [Evaluating Remote Sensing Image Captions Beyond Metric Biases](https://arxiv.org/abs/2604.22855)

**<font color=#1a73e8>作者：</font>** Ziyun Chen, Fan Liu, Liang Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The core objective of image captioning is to achieve lossless semantic compression from visual signals into textual modalities. However, the reliance on manually curated reference texts for evaluation essentially forces models to mimic specific human annotation styles, thereby masking the true descriptive capabilities of advanced foundation models. This systemic misalignment prompts a critical question: Is task-specific fine-tuning truly necessary for Remote Sensing Image Captioning, or is the perceived performance gap merely an artifact of flawed evaluation criteria? To investigate this discrepancy, we propose ReconScore, a novel reference-free evaluation metric. Rather than computing textual similarities, we assess caption quality by its capability to reconstruct the original visual elements solely from the generated text, effectively neutralizing human annotation biases. Applying this metric, we uncover a profound, counterintuitive truth: inherently powerful, unfine-tuned MLLMs surpass their fine-tuned counterparts in authentic zero-shot RSIC tasks. Driven by this structural discovery, we introduce RemoteDescriber, a completely training-free generation methodology. By employing ReconScore as a self-correction mechanism, we iteratively refine the semantic precision of MLLM outputs without any computational fine-tuning overhead. Comprehensive experiments demonstrate that RemoteDescriber achieves state-of-the-art performance on three datasets. Furthermore, we validate ReconScore's reliability and analyze the flaws of traditional metrics. Our code is available at this https URL.

---


### 20. [When Policies Cannot Be Retrained: A Unified Closed-Form View of Post-Training Steering in Offline Reinforcement Learning](https://arxiv.org/abs/2604.22873)

**<font color=#1a73e8>作者：</font>** Elias Hossain, Mohammad Jahid Ibna Basher, Ivan Garibay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) can learn effective policies from fixed datasets, but deployment objectives may change after training, and in many applications the trained actor cannot be retrained because of data, cost, or governance constraints. We study deployment-time adaptation for frozen offline actors using Product-of-Experts (PoE) composition with a goal-conditioned prior. Our main practical finding is graceful degradation rather than universal performance gain: under degraded or random priors, precision-weighted composition remains anchored to the frozen actor, while additive and prior-only adaptation collapse, and a KL-budget selector often recovers a near-oracle operating point. We also make explicit a closed-form identity in the frozen-actor setting: for diagonal-Gaussian actors and priors, PoE with coefficient alpha yields the same deterministic policy as KL-regularized adaptation with beta = alpha / (1 - alpha), with posterior covariances differing only by a global scalar factor. Empirically, across four D4RL environments (3,900 MuJoCo episodes), we observe a 4/5/3 HELP/FROZEN/HURT split. Extending the analysis to six harder cells and two AntMaze diagnostics reveals an actor-competence ceiling: medium-expert remains HURT in all 9 cells at every tested alpha, while AntMaze with a behavior-cloned frozen actor yields zero success for all composition rules. Overall, PoE and KL-regularized adaptation are best viewed as a single actor-anchored safety mechanism for deployment-time steering.

---


### 21. [SketchVLM: Vision language models can annotate images to explain thoughts and guide users](https://arxiv.org/abs/2604.22875)

**<font color=#1a73e8>作者：</font>** Brandon Collins, Logan Bolton, Hung Huy Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When answering questions about images, humans naturally point, label, and draw to explain their reasoning. In contrast, modern vision-language models (VLMs) such as Gemini-3-Pro and GPT-5 only respond with text, which can be difficult for users to verify. We present SketchVLM, a training-free, model-agnostic framework that enables VLMs to produce non-destructive, editable SVG overlays on the input image to visually explain their answers. Across seven benchmarks spanning visual reasoning (maze navigation, ball-drop trajectory prediction, and object counting) and drawing (part labeling, connecting-the-dots, and drawing shapes around objects), SketchVLM improves visual reasoning task accuracy by up to +28.5 percentage points and annotation quality by up to 1.48x relative to image-editing and fine-tuned sketching baselines, while also producing annotations that are more faithful to the model's stated answer. We find that single-turn generation already achieves strong accuracy and annotation quality, and multi-turn generation opens up further opportunities for human-AI collaboration. An interactive demo and code are at this https URL.

---


### 22. [Beyond Single-Agent Alignment: Preventing Context-Fragmented Violations in Multi-Agent Systems](https://arxiv.org/abs/2604.22879)

**<font color=#1a73e8>作者：</font>** Jie Wu, Ming Gong  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We identify and formalize a novel security risk: Context-Fragmented Violations (CFVs) - a class of policy breaches where individual agent actions appear locally safe and reasonable, yet collectively violate organizational policies because critical policy facts are siloed in different departments private contexts. Existing prompt-based alignment mechanisms and monolithic interceptors are poorly matched to violations that span contextual islands. We propose Distributed Sentinel, a distributed zero-trust enforcement architecture that introduces the Semantic Taint Token (STT) Protocol. Through lightweight sidecar proxies, our system propagates security state across organizational boundaries without exposing raw cross-domain data, enabling Counterfactual Graph Simulation for cross-domain policy verification. We construct PhantomEcosystem, a comprehensive benchmark comprising 9 categories of realistic cross-agent violation scenarios with adversarially balanced safe controls. On this benchmark, Distributed Sentinel achieves F1 = 0.95 with 106ms end-to-end latency (16ms verification + 90ms entity extraction on A100), compared to 0.85 F1 for prompt-based filtering and 0.65 for rule-based DLP. To empirically validate the need for external enforcement, we evaluate eight frontier LLMs in execution-oriented multi-agent workflows with per-agent domain world models. All models exhibit substantial violation rates (14-98%), with cross-domain data flows showing systematically higher violation rates than same-domain flows. These results indicate that self-avoidance is unreliable and that multi-agent security benefits from a centralized enforcement layer operating above individual agents.

---


### 23. [Can Multimodal Large Language Models Truly Understand Small Objects?](https://arxiv.org/abs/2604.22884)

**<font color=#1a73e8>作者：</font>** Fujun Han, Junan Chen, Xintong Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have shown promising potential in diverse understanding tasks, e.g., image and video analysis, math and physics olympiads. However, they remain blank and unexplored for Small Object Understanding (SOU) tasks. To fill this gap, we introduce SOUBench, the first and comprehensive benchmark for exploring the small objects understanding capability of existing MLLMs. Specifically, we first design an effective and automatic visual question-answer generation strategy, constructing a new SOU-VQA evaluation dataset, with 18,204 VQA pairs, six relevant sub-tasks, and three dominant scenarios (i.e., Driving, Aerial, and Underwater). Then, we conduct a comprehensive evaluation on 15 state-of-the-art MLLMs and reveal their weak capabilities in small object understanding. Furthermore, we develop SOU-Train, a multimodal training dataset with 11,226 VQA pairs, to improve the SOU capabilities of MLLMs. Through supervising fine-tuning of the latest MLLM, we demonstrate that SOU-Train can effectively enhance the latest MLLM's ability to understand small objects. Comprehensive experimental results demonstrate that, the proposed SOUBench, along with the SOU-VQA and SOU-Train datasets, provides a crucial empirical foundation to the community for further developing models with enhanced small object understanding capabilities. Datasets and Code: this https URL.

---


### 24. [Quantifying and Mitigating Self-Preference Bias of LLM Judges](https://arxiv.org/abs/2604.22891)

**<font color=#1a73e8>作者：</font>** Jinming Yang, Chuxian Qiu, Zhenyu Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge has become a dominant approach in automated evaluation systems, playing critical roles in model alignment, leaderboard construction, quality control, and so on. However, the scalability and trustworthiness of this approach can be substantially distorted by Self-Preference Bias (SPB), which is a directional evaluative deviation in which LLMs systematically favor or disfavor their own generated outputs during evaluation. Existing measurements rely on costly human annotations and conflate generative capability with evaluative stance, and thus are impractical for large-scale deployment in real-world systems. To address this issue, we introduce a fully automated framework to quantifying and mitigating SPB, which constructs equal-quality pairs of responses with negligible quality differences, enabling statistical disentanglement of discriminability from bias propensity without human gold standards. Empirical analysis across 20 mainstream LLMs reveals that advanced capabilities are often uncorrelated, or even negatively correlated, with low SPB. To mitigate this bias, we propose a structured multi-dimensional evaluation strategy grounded in cognitive load decomposition, which reduces SPB by 31.5\% on average.

---


### 25. [Utility-Aware Data Pricing: Token-Level Quality and Empirical Training Gain for LLMs](https://arxiv.org/abs/2604.22893)

**<font color=#1a73e8>作者：</font>** Minghui Xu, Qi Luo, Kun Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional data valuation methods based on ``row-count $\times$ quality coefficient'' paradigms fail to capture the nuanced, nonlinear contributions that data makes to Large Language Model (LLM) capabilities. This paper presents a dynamic data valuation framework that transitions from static accounting to utility-based pricing. Our approach operates on three layers: (1) token-level information density metrics using Shannon entropy and Data Quality Scores; (2) empirical training gain measurement through influence functions, proxy model strategies, and Data Shapley values; and (3) cryptographic verifiability through hash-based commitments, Merkle trees, and a tamper-evident training ledger. We provide comprehensive experimental validation on three real domains (instruction following, mathematical reasoning, and code summarization), demonstrating that proxy-based empirical gain achieves near-perfect ranking alignment with realized utility, substantially outperforming row-count and token-count baselines. This framework enables a fair Data-as-a-Service economy where high-reasoning data is priced according to its actual contribution to model intelligence, while providing the transparency and auditability necessary for trustworthy data markets.

---


### 26. [Text-Guided Multimodal Unified Industrial Anomaly Detection](https://arxiv.org/abs/2604.22899)

**<font color=#1a73e8>作者：</font>** Zewen Li, Shuo Ye, Zitong Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection based on RGB-3D multimodal data has emerged as a mainstream paradigm for intelligent quality inspection. However, existing unsupervised methods suffer from two critical limitations: ambiguous cross-modal alignment caused by the lack of high-level semantic guidance and insufficient geometric modeling for RGB-to-3D feature mapping. To address these issues, we propose a unified multimodal industrial anomaly detection framework guided by text semantics. The framework consists of two core modules: a Geometry-Aware Cross-Modal Mapper to preserve geometric structure during modality conversion, and an Object-Conditioned Textual Feature Adaptor to align multimodal features with semantic priors. Furthermore, we establish a unified learning paradigm for multimodal industrial anomaly detection, which breaks the one-model-one-class constraint and enables accurate anomaly detection across diverse classes using a single model. Extensive experiments on the MVTec 3D-AD and Eyecandies datasets demonstrate that our method achieves state-of-the-art performance in classification and localization under unsupervised settings.

---


### 27. [AutoPyVerifier: Learning Compact Executable Verifiers for Large Language Model Outputs](https://arxiv.org/abs/2604.22937)

**<font color=#1a73e8>作者：</font>** Pouya Pezeshkpour, Estevam Hruschka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verification is becoming central to both reinforcement-learning-based training and inference-time control of large language models (LLMs). Yet current verifiers face a fundamental trade-off: LLM-based verifiers are expressive but hard to control and prone to error, while deterministic executable verifiers are reliable and interpretable but often limited in capability. We study the following question: given a development set of LLM outputs and labels for a target objective, such as correctness, can we automatically induce a minimal set of Python verifiers whose joint satisfaction closely matches that objective? We propose AutoPyVerifier, a framework that uses an LLM to synthesize candidate verifier functions and then refines them through search over a directed acyclic graph (DAG). By navigating the DAG, AutoPyVerifier systematically explores the space of deterministic executable verifiers and selects a compact verifier set whose joint satisfaction best approximates the target objective. Across mathematical reasoning, coding, function calling, and instruction-following benchmarks for several state-of-the-art LLMs, AutoPyVerifier improves target-objective prediction by up to 55.0 F1 points over the initial LLM-generated verifier sets. Additional analyses show that the most useful verification targets vary by benchmark and model, and that the DAG-based search shifts the learned verifier sets toward more structural and semantically grounded checks. We further show that exposing the discovered verifier set to an LLM as an external tool improves downstream accuracy by up to 17.0 points. We release our code

---


### 28. [Self Knowledge Re-expression: A Fully Local Method for Adapting LLMs to Tasks Using Intrinsic Knowledge](https://arxiv.org/abs/2604.22939)

**<font color=#1a73e8>作者：</font>** Mengyu Wang, Xiaoying Zhi, Zhiyi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While the next-token prediction (NTP) paradigm enables large language models (LLMs) to express their intrinsic knowledge, its sequential nature constrains performance on specialized, non-generative tasks. We attribute this performance bottleneck to the LLMs' knowledge expression mechanism, rather than to deficiencies in knowledge acquisition. To address this, we propose Self-Knowledge Re-expression (SKR), a novel, task-agnostic adaptation method. SKR transforms the LLM's output from generic token generation to highly efficient, task-specific expression. SKR is a fully local method that uses only unannotated data, requiring neither human supervision nor model distillation. Experiments on a large financial document dataset demonstrate substantial improvements: over 40% in Recall@1 for information retrieval tasks, over 76% reduction in object detection latency, and over 33% increase in anomaly detection AUPRC. Our results on the MMDocRAG dataset surpass those of leading retrieval models by at least 12.6%.

---


### 29. [Uncertainty Quantification for LLM Function-Calling](https://arxiv.org/abs/2604.22985)

**<font color=#1a73e8>作者：</font>** Zihuiwen Ye, Lukas Aichberger, Michael Kirchhof 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed to autonomously solve real-world tasks. A key ingredient for this is the LLM Function-Calling paradigm, a widely used approach for equipping LLMs with tool-use capabilities. However, an LLM calling functions incorrectly can have severe implications, especially when their effects are irreversible, e.g., transferring money or deleting data. Hence, it is of paramount importance to consider the LLM's confidence that a function call solves the task correctly prior to executing it. Uncertainty Quantification (UQ) methods can be used to quantify this confidence and prevent potentially incorrect function calls. In this work, we present what is, to our knowledge, the first evaluation of UQ methods for LLM Function-Calling (FC). While multi-sample UQ methods, such as Semantic Entropy, show strong performance for natural language Q&A tasks, we find that in the FC setting, it offers no clear advantage over simple single-sample UQ methods. Additionally, we find that the particularities of FC outputs can be leveraged to improve the performance of existing UQ methods in this setting. Specifically, multi-sample UQ methods benefit from clustering FC outputs based on their abstract syntax tree parsing, while single-sample UQ methods can be improved by selecting only semantically meaningful tokens when calculating logit-based uncertainty scores.

---


### 30. [CheXmix: Unified Generative Pretraining for Vision Language Models in Medical Imaging](https://arxiv.org/abs/2604.22989)

**<font color=#1a73e8>作者：</font>** Ashwin Kumar, Robbie Holland, Corey Barrett 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent medical multimodal foundation models are built as multimodal LLMs (MLLMs) by connecting a CLIP-pretrained vision encoder to an LLM using LLaVA-style finetuning. This two-stage, decoupled approach introduces a projection layer that can distort visual features. This is especially concerning in medical imaging where subtle cues are essential for accurate diagnoses. In contrast, early-fusion generative approaches such as Chameleon eliminate the projection bottleneck by processing image and text tokens within a single unified sequence, enabling joint representation learning that leverages the inductive priors of language models. We present CheXmix, a unified early-fusion generative model trained on a large corpus of chest X-rays paired with radiology reports. We expand on Chameleon's autoregressive framework by introducing a two-stage multimodal generative pretraining strategy that combines the representational strengths of masked autoencoders with MLLMs. The resulting models are highly flexible, supporting both discriminative and generative tasks at both coarse and fine-grained scales. Our approach outperforms well-established generative models across all masking ratios by 6.0% and surpasses CheXagent by 8.6% on AUROC at high image masking ratios on the CheXpert classification task. We further inpaint images over 51.0% better than text-only generative models and outperform CheXagent by 45% on the GREEN metric for radiology report generation. These results demonstrate that CheXmix captures fine-grained information across a broad spectrum of chest X-ray tasks. Our code is at: this https URL.

---


### 31. [FormalScience: Scalable Human-in-the-Loop Autoformalisation of Science with Agentic Code Generation in Lean](https://arxiv.org/abs/2604.23002)

**<font color=#1a73e8>作者：</font>** Jordan Meadows, Lan Zhang, Andre Freitas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formalising informal mathematical reasoning into formally verifiable code is a significant challenge for large language models. In scientific fields such as physics, domain-specific machinery (\textit{e.g.} Dirac notation, vector calculus) imposes additional formalisation challenges that modern LLMs and agentic approaches have yet to tackle. To aid autoformalisation in scientific domains, we present FormalScience; a domain-agnostic human-in-the-loop agentic pipeline that enables a single domain expert (without deep formal language experience) to produce \textit{syntactically correct} and \textit{semantically aligned} formal proofs of informal reasoning for low economic cost. Applying FormalScience to physics, we construct FormalPhysics, a dataset of 200 university-level (LaTeX) physics problems and solutions (primarily quantum mechanics and electromagnetism), along with their Lean4 formal representations. Compared to existing formal math benchmarks, FormalPhysics achieves perfect formal validity and exhibits greater statement complexity. We evaluate open-source models and proprietary systems on a statement autoformalisation task on our dataset via zero-shot prompting, self-refinement with error feedback, and a novel multi-stage agentic approach, and explore autoformalisation limitations in modern LLM-based approaches. We provide the first systematic characterisation of semantic drift in physics autoformalisation in terms of concepts such as notational collapse and abstraction elevation which reveals what formal language verifies when full semantic preservation is unattainable. We release the codebase together with an interactive UI-based FormalScience system which facilitates autoformalisation and theorem proving in scientific domains beyond this http URL://github.com/jmeadows17/formal-science

---


### 32. [Chinese-SkillSpan: A Span-Level Dataset for ESCO-Aligned Competency Extraction from Chinese Job Ads](https://arxiv.org/abs/2604.23009)

**<font color=#1a73e8>作者：</font>** Guojing Li, Zichuan Fu, Junyi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Job Skill Named Entity Recognition (JobSkillNER) aims to automatically extract key skill information from large-scale job posting data, which is important for improving talent-market matching efficiency and supporting personalized employment services. To the best of our knowledge, this work presents the first Chinese JobSkillNER dataset for recruitment texts. We propose annotation guidelines tailored to Chinese job postings and an LLM-empowered Macro-Micro collaborative annotation pipeline. The pipeline leverages the contextual understanding ability of large language models (LLMs) for initial annotation and then refines the results through expert sentence-level adjudication. Using this pipeline, we annotate more than 20,000 instances collected from four major recruitment platforms over the period 2014-2025. Based on these efforts, we release Chinese-SkillSpan, the first Chinese JobSkillNER dataset aligned with the ESCO occupational skill standard across four dimensions: knowledge, skill, transversal competence, and language competence (LSKT). Experimental results show that the dataset supports effective model training and evaluation, indicating that Chinese-SkillSpan helps fill a major gap in Chinese JobSkillNER resources and provides a useful benchmark for intelligent recruitment research. Code and data are available at this https URL .

---


### 33. [Understanding Representation Gaps Across Scales in Tropical Tree Species Classification from Drone Imagery](https://arxiv.org/abs/2604.23019)

**<font color=#1a73e8>作者：</font>** Sulagna Saha, Arthur Ouaknine, Etienne Laliberté 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate classification of tropical tree species from unoccupied aerial vehicle (UAV) imagery remains challenging due to high species diversity and strong visual similarity among species at typical image resolutions (centimeters per pixel). In contrast, models trained on close-up citizen science photographs captured with smartphones achieve strong plant species classification performance. Recent advances in UAV data acquisition now enable the collection of close-up images that are spatially registered with top-view aerial imagery and approach the level of visual detail found in smartphone photographs, with the trade-off that such high-resolution photos cannot be acquired for many trees. In this work, we evaluate the performance of existing methods using paired top-view and close-up UAV imagery collected in a species-rich tropical forest. Through fine-tuning experiments, we quantify the performance gap between vision foundation models and in-domain generalist plant recognition models across both image types (high-resolution close-up versus coarser-resolution top-view imagery). We show that classification performance is consistently higher on close-up images than on top-view aerial imagery, and that this performance gap widens for rare species. Finally, we propose that self-supervised representation alignment across these two spatial scales offers a promising approach for integrating fine-grained visual information into canopy-level species classification models based on top-view UAV imagery. Leveraging high-resolution close-up UAV imagery to enhance canopy-level species classification could substantially improve large-scale monitoring of tropical forest biodiversity.

---


### 34. [A Systematic Approach for Large Language Models Debugging](https://arxiv.org/abs/2604.23027)

**<font color=#1a73e8>作者：</font>** Basel Shbita, Anna Lisa Gentile, Bing Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become central to modern AI workflows, powering applications from open-ended text generation to complex agent-based reasoning. However, debugging these models remains a persistent challenge due to their opaque and probabilistic nature and the difficulty of diagnosing errors across diverse tasks and settings. This paper introduces a systematic approach for LLM debugging that treats models as observable systems, providing structured, model-agnostic methods from issue detection to model refinement. By unifying evaluation, interpretability, and error-analysis practices, our approach enables practitioners to iteratively diagnose model weaknesses, refine prompts and model parameters, and adapt data for fine-tuning or assessment, while remaining effective in contexts where standardized benchmarks and evaluation criteria are lacking. We argue that such a structured methodology not only accelerates troubleshooting but also fosters reproducibility, transparency, and scalability in the deployment of LLM-based systems.

---


### 35. [Preserving Long-Tailed Expert Information in Mixture-of-Experts Tuning](https://arxiv.org/abs/2604.23036)

**<font color=#1a73e8>作者：</font>** Haoze He, Xingyuan Ding, Xuan Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite MoE models leading many benchmarks, supervised fine-tuning (SFT) for the MoE architectures remains difficult because its router layers are fragile. Methods such as DenseMixer and ESFT mitigate router collapse with dense mixing or auxiliary load-balancing losses, but these introduce noisy gradients that often degrade performance. In preliminary experiments, we systematically pruned experts and observed that while certain super experts are activated far more frequently, discarding less used experts still leads to notable performance degradation. This suggests that even rarely activated experts encode non-trivial knowledge useful for downstream tasks. Motivated by this, we propose an auxiliary-loss-free MoE SFT framework that combines bias-driven sparsification with always-active gated condenser experts. Rather than enforcing balanced activation across all experts, our method encourages task-relevant experts to remain active while pushing long-tailed experts toward inactivity. The condenser experts provide a persistent, learnable pathway that alleviates gradient starvation and facilitates consolidation of information that would otherwise remain fragmented across sparsely activated experts. Analysis further suggest that this design better preserves long-tailed expert information under sparse routing. Experiments on large-scale MoE models demonstrate that our approach outperforms state-of-the-art SFT baselines such as DenseMixer and ESFT, achieving average gain of 2.5%+ on both mathematical reasoning and commonsenseQA benchmarks.

---


### 36. [A Decoupled Human-in-the-Loop System for Controlled Autonomy in Agentic Workflows](https://arxiv.org/abs/2604.23049)

**<font color=#1a73e8>作者：</font>** Edward Cheng, Jeshua Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly deployed to execute tasks and make decisions within agentic workflows, introducing new requirements for safe and controlled autonomy. Prior work has established the importance of human oversight for ensuring transparency, accountability, and trustworthiness in such systems. However, existing implementations of Human-in-the-Loop (HITL) mechanisms are typically embedded within application logic, limiting reuse, consistency, and scalability across multi-agent environments.
This paper presents a decoupled HITL system architecture that treats human oversight as an independent system component within the agent operating environment. The proposed design separates human interaction management from application workflows through explicit interfaces and a structured execution model. In addition, a design framework is introduced to formalize HITL integration along four dimensions: intervention conditions, role resolution, interaction semantics, and communication channel. This framework enables selective and context-aware human involvement while maintaining system-level consistency.
The approach supports alignment with emerging agent communication protocols, allowing HITL to be implemented as a protocol-level concern. By externalizing HITL and structuring its integration, the system provides a foundation for scalable governance and progressive autonomy in agentic workflows.

---


### 37. [Evaluating Temporal Consistency in Multi-Turn Language Models](https://arxiv.org/abs/2604.23051)

**<font color=#1a73e8>作者：</font>** Yash Kumar Atri, Steven L. Johnson, Tom Hartvigsen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly deployed in interactive settings where users reason about facts over time rather than in isolation. In such scenarios, correct behavior requires models to maintain and update implicit temporal assumptions established earlier in a conversation. We study this challenge through the lens of temporal scope stability: the ability to preserve, override, or transfer time-scoped factual context across dialogue turns. We introduce ChronoScope, a large-scale diagnostic benchmark designed to isolate temporal scope behavior in controlled multi-turn interactions, comprising over one million deterministically generated question chains grounded in Wikidata. ChronoScope evaluates whether models can correctly retain inferred temporal scope when follow-up questions omit explicit time references, spanning implicit carryover, explicit scope switching, cross-entity transfer, and longer temporal trajectories. Through extensive evaluation of state-of-the-art language models, we find that temporal scope stability is frequently violated in controlled multi-turn settings, with models often drifting toward present-day assumptions despite correct underlying knowledge. These failures intensify with interaction length and persist even under oracle context conditions, revealing a gap between single-turn factual accuracy and coherent temporal reasoning under sequential interaction. We make our dataset and evaluation suite publicly available at this https URL

---


### 38. [DeepImagine: Learning Biomedical Reasoning via Successive Counterfactual Imagining](https://arxiv.org/abs/2604.23054)

**<font color=#1a73e8>作者：</font>** Youze Zheng, Jianyou Wang, Yuhan Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Predicting the outcomes of prospective clinical trials remains a major challenge for large language models. Prior work has shown that both traditional correlational predictors, such as random forests and logistic regression, and strong commercial LLMs achieve limited performance on this task. In this paper, we propose DeepImagine, a framework for teaching LLMs biomedical reasoning through successive counterfactual imagining. The central idea is to approximate hidden causal mechanisms of clinical trials by training models to infer how observed trial results would change under controlled perturbations of experimental conditions, such as dosage, outcome measures, study arms, geography, and other trial attributes. To support this objective, we construct both natural and approximate counterfactual pairs from real clinical trials with reported outcomes. For settings where strict counterfactual supervision is available, such as paired outcome measures or dose-ranging study arms within the same trial, we train models with supervised fine-tuning. For broader settings where only approximate counterfactual pairs can be retrieved, we optimize models with reinforcement learning using verifiable rewards based on downstream benchmark correctness. We further augment training with synthetic reasoning traces that provide causally plausible explanations for local counterfactual transitions. Using this pipeline, we train language models under 10B parameters, including Qwen3.5-9B, and evaluate them on clinical trial outcome prediction. We aim to show that DeepImagine consistently improves over untuned language models and traditional correlational baselines. Finally, we aim to show that the learned reasoning trajectories provide interpretable signals about how models represent trial-level mechanisms, suggesting a practical path toward more mechanistic and scientifically useful biomedical language models.

---


### 39. [Don't Make the LLM Read the Graph: Make the Graph Think](https://arxiv.org/abs/2604.23057)

**<font color=#1a73e8>作者：</font>** Yuqi Sun, Tianqin Meng, George Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate whether explicit belief graphs improve LLM performance in cooperative multi-agent reasoning. Through 3,000+ controlled trials across four LLM families in the cooperative card game Hanabi, we establish four findings. First, integration architecture determines whether belief graphs provide value: as prompt context, graphs are decorative for strong models and beneficial only for weak models on 2nd-order Theory of Mind (80% vs 10%, p<0.0001, OR=36.0); when graphs gate action selection through ranked shortlists, they become structurally essential even for strong models (100% vs 20% on 2nd-order ToM, p<0.001). Second, we identify "Planner Defiance," a model-family-specific failure where LLMs override correct planner recommendations at partial competence (90% override, replicated N=20); Gemini models show near-zero defiance while Llama 70B shows 90%, and models distinguish factual context (deferred to) from advisory recommendations (overridden). Third, full-game evidence confirms inter-agent conventions (+128% over baseline, p=0.003) outperform all single-agent interventions, and individual belief-graph components must be combined to produce gains. Fourth, preliminary scaling analysis (N=10/cell, exploratory) suggests graph depth has diminishing returns: shallow graphs provide the best cost-benefit ratio, while deeper ToM graphs appear harmful at larger player counts (-1.5 pts at 5-player, p=0.029).

---


### 40. [Implicit Framing in Obstetric Counseling Notes: A Grounded LLM Pipeline on a VBAC-Eligible Cohort](https://arxiv.org/abs/2604.23059)

**<font color=#1a73e8>作者：</font>** Baris Karacan, Barbara Di Eugenio, Patrick Thornton 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical framing -- the linguistic manner in which clinical information is presented -- can influence patient understanding and decision-making, with important implications for healthcare outcomes. Obstetrics is a high-stakes domain in which physicians counsel patients on delivery mode choices such as vaginal birth after cesarean (VBAC) and repeat cesarean section (RCS), yet counseling language remains underexplored in large-scale clinical text analysis. In this work, we analyze physician counseling language in 2,024 obstetric history and physical narratives for a rigorously defined cohort of patients for whom both VBAC and RCS were clinically viable options. To control for confounding due to medical contraindications, we first construct a VBAC-eligible cohort using structured clinical data supplemented by a large language model (LLM)-based extraction pipeline constrained to grounded, verbatim evidence from free-text narratives. We then apply a zero-shot LLM framework to categorize counseling segments into predefined framing categories capturing how physicians linguistically present delivery options. Our analysis reveals a significant difference in counseling framing distributions between VBAC and RCS notes; risk-focused language accounts for a substantially larger share of counseling segments in RCS documentation than in VBAC, with category-level differences confirmed by statistical testing, highlighting the value of controlled LLM-based framing analysis in obstetric care.

---


### 41. [C-MORAL: Controllable Multi-Objective Molecular Optimization with Reinforcement Alignment for LLMs](https://arxiv.org/abs/2604.23061)

**<font color=#1a73e8>作者：</font>** Rui Gao, Youngseung Jeon, Swastik Roy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show promise for molecular optimization, but aligning them with selective and competing drug-design constraints remains challenging. We propose C-Moral, a reinforcement learning post-training framework for controllable multi-objective molecular optimization. C-Moral combines group-based relative optimization, property score alignment for heterogeneous objectives, and continuous non-linear reward aggregation to improve stability across competing properties. Experiments on the C-MuMOInstruct benchmark show that C-Moral consistently outperforms state-of-the-art models across both in-domain and out-of-domain settings, achieving the best Success Optimized Rate (SOR) of 48.9% on IND tasks and 39.5% on OOD tasks, while largely preserving scaffold similarity. These results suggest that RL post-training is an effective way to align molecular language models with continuous molecular design objectives. Our code and models are publicly available at this https URL.

---


### 42. [ContextWeaver: Selective and Dependency-Structured Memory Construction for LLM Agents](https://arxiv.org/abs/2604.23069)

**<font color=#1a73e8>作者：</font>** Yating Wu, Yuhao Zhang, Sayan Ghosh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents often struggle in long-context interactions. As the agent accumulates more interaction history, context management approaches such as sliding window and prompt compression may omit earlier structured information that later steps rely on. Recent retrieval-based memory systems surface relevant content but still overlook the causal and logical structure needed for multi-step reasoning. We introduce ContextWeaver, a selective and dependency-structured memory framework that organizes an agent's interaction trace into a graph of reasoning steps and selects the relevant context for future actions. Unlike prior context management approaches, ContextWeaver supports: (1) dependency-based construction and traversal that link each step to the earlier steps it relies on; (2) compact dependency summarization that condenses root-to-step reasoning paths into reusable units; and (3) a lightweight validation layer that incorporates execution feedback. On the SWE-Bench Verified and Lite benchmarks, ContextWeaver improves performance over a sliding-window baseline in pass@1, while reducing reasoning steps and token usage. Our observations suggest that modeling logical dependencies provides a stable and scalable memory mechanism for LLM agents that use tools.

---


### 43. [Analytica: Soft Propositional Reasoning for Robust and Scalable LLM-Driven Analysis](https://arxiv.org/abs/2604.23072)

**<font color=#1a73e8>作者：</font>** Junyan Cheng, Kyle Richardson, Peter Chin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly tasked with complex real-world analysis (e.g., in financial forecasting, scientific discovery), yet their reasoning suffers from stochastic instability and lacks a verifiable, compositional structure. To address this, we introduce Analytica, a novel agent architecture built on the principle of Soft Propositional Reasoning (SPR). SPR reframes complex analysis as a structured process of estimating the soft truth values of different outcome propositions, allowing us to formally model and minimize the estimation error in terms of its bias and variance. Analytica operationalizes this through a parallel, divide-and-conquer framework that systematically reduces both sources of error. To reduce bias, problems are first decomposed into a tree of subpropositions, and tool-equipped LLM grounder agents are employed, including a novel Jupyter Notebook agent for data-driven analysis, that help to validate and score facts. To reduce variance, Analytica recursively synthesizes these grounded leaves using robust linear models that average out stochastic noise with superior efficiency, scalability, and enable interactive "what-if" scenario analysis. Our theoretical and empirical results on economic, financial, and political forecasting tasks show that Analytica improves 15.84% accuracy on average over diverse base models, achieving 71.06% accuracy with the lowest variance of 6.02% when working with a Deep Research grounder. Our Jupyter Notebook grounder shows strong cost-effectiveness that achieves a close 70.11% accuracy with 90.35% less cost and 52.85% less time. Analytica also exhibits highly noise-resilient and stable performance growth as the analysis depth increases, with a near-linear time complexity, as well as good adaptivity to open-weight LLMs and scientific domains.

---


### 44. [From Pixels to Explanations: Interpretable Diabetic Retinopathy Grading with CNN-Transformer Ensembles, Visual Explainability and Vision-Language Models](https://arxiv.org/abs/2604.23079)

**<font color=#1a73e8>作者：</font>** Pir Bakhsh Khokhar, Carmine Gravino, Fabio Palomba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The quality of diabetic retinopathy (DR) screening relies on the ability to correctly grade severity; however, many deep-learning (DL) classifiers cannot be easily interpreted in the clinical context. This study presents a methodology that combines strong discriminative models with multimodal explanations, converting retinal pixels into clinically interpretable outputs. Using the APTOS 2019 benchmark, we evaluated six representative CNN- and transformer-based backbones under a controlled protocol with stratified five-fold cross-validation. We then compared ensembling strategies (hard voting, weighted soft voting, stacking) and investigated a hybrid class-level fusion variant to exploit grade-specific advantages. For interpretability, we produced Grad-CAM++ visual attribution maps and short textual rationales using vision-language models (VLMs) conditioned on the fundus image and classifier outputs under conservative prompting constraints. Modern CNN backbones (ResNet-50 and ConvNeXt-Tiny) provided the strongest single-model baselines, with cross-validated QWK up to 0.919 and 0.914, respectively. Ensembling improved ordinal agreement, and weighted soft voting was the most consistent across folds (QWK 0.934 +/- 0.017). Hybrid class-level fusion was competitive but did not yield a statistically reliable improvement over standard fusion in paired fold comparisons (Holm-adjusted p >= 1.000). For explanation quality, Grad-CAM++ offered plausible but coarse localization, and VLM rationales were generally grade-consistent. Quantitatively, VLM variants showed a trade-off between clinical completeness and template-level semantic similarity (coverage 0.700 vs. BERTScore 0.072), while image-text alignment was comparable (CLIPScore approximately 0.34).

---


### 45. [Towards Automated Ontology Generation from Unstructured Text: A Multi-Agent LLM Approach](https://arxiv.org/abs/2604.23090)

**<font color=#1a73e8>作者：</font>** Abid Talukder, Maruf Ahmed Mridul, Oshani Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatically generating formal ontologies from unstructured natural language remains a central challenge in knowledge engineering. While large language models (LLMs) show promise, it remains unclear which architectural design choices drive generation quality and why current approaches fail. We present a controlled experimental study using domain-specific insurance contracts to investigate these questions. We first establish a single-agent LLM baseline, identifying key failure modes such as poor Ontology Design Pattern compliance, structural redundancy, and ineffective iterative repair. We then introduce a multi-agent architecture that decomposes ontology construction into four artifact-driven roles: Domain Expert, Manager, Coder, and Quality Assurer. We evaluate performance across architectural quality (via a panel of heterogeneous LLM judges) and functional usability (via competency question driven SPARQL evaluation with complementary retrieval augmented generation based assessment). Results show that the multi-agent approach significantly improves structural quality and modestly enhances queryability, with gains driven primarily by front-loaded planning. These findings highlight planning-first, artifact-driven generation as a promising and more auditable path toward scalable automated ontology engineering.

---


### 46. [Channel Adaptation for EEG Foundation Models: A Systematic Benchmark Across Architectures, Tasks, and Training Regimes](https://arxiv.org/abs/2604.23091)

**<font color=#1a73e8>作者：</font>** Kuntal Kokate, Bruno Aristimunha, Dung Truong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling EEG foundation models requires pooling data across heterogeneous electrode montages, a prerequisite both for larger pretraining corpora and for downstream deployment. We present the first systematic comparison of four channel adaptation methods (Conv1d projection, spherical spline interpolation (SSI), source-space decomposition, and Riemannian re-centering) across five pretrained EEG foundation models (5M--157M parameters), five downstream tasks, and two training regimes with 10--15 random seeds each. We find that rigid-montage models (BENDR, Neuro-GPT) require external adaptation, while flexible models (EEGPT, CBraMod) match or exceed it natively when fine-tuned but benefit from external methods under frozen-encoder deployment. A probe-SFT asymmetry exists: external adaptation can cause severe negative transfer during fine-tuning of flexible models. The optimal method is architecture-dependent (Conv1d for BENDR, SSI/Riemannian for Neuro-GPT, source-space decomposition for depression detection), and 5M-parameter CBraMod outperforms models up to 31$\times$ larger on 4/5 datasets, consistent with independent findings that compact EEG-specific architectures can match larger models.

---


### 47. [Mixture of Heterogeneous Grouped Experts for Language Modeling](https://arxiv.org/abs/2604.23108)

**<font color=#1a73e8>作者：</font>** Zhicheng Ma, Xiang Liu, Zhaoxiang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) based on Mixture-of-Experts (MoE) are pivotal in industrial applications for their ability to scale performance efficiently. However, standard MoEs enforce uniform expert sizes,creating a rigidity that fails to align computational costs with varying token-level complexity. While heterogeneous expert architectures attempt to address this by diversifying expert sizes, they often suffer from significant system-level challenges, specifically unbalanced GPU utilization and inefficient parameter utilization, which hinder practical deployment. To bridge the gap between theoretical heterogeneity and robust industrial application, we propose Mixture of Heterogeneous Grouped Experts (MoHGE) which introduces a two-level routing mechanism to enable flexible, resource-aware expert combinations. To optimize inference efficiency, we propose a Group-Wise Auxiliary Loss, which dynamically steers tokens to the most parameter-efficient expert groups based on task difficulty. To address the critical deployment challenge of GPU load balancing, we introduce an All-size Group-decoupling Allocation strategy coupled with an Intra-Group Experts Auxiliary Loss. These mechanisms collectively ensure uniform computation distribution across GPUs. Extensive evaluations demonstrate that MoHGE matches the performance of MoE architectures while reducing the total parameters by approximately 20% and maintaining balanced GPU utilization. Our work establishes a scalable paradigm for resource-efficient MoE design, offering a practical solution for optimizing inference costs in real-world scenarios.

---


### 48. [Mechanistic Steering of LLMs Reveals Layer-wise Feature Vulnerabilities in Adversarial Settings](https://arxiv.org/abs/2604.23130)

**<font color=#1a73e8>作者：</font>** Nilanjana Das, Manas Gaur  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can still be jailbroken into producing harmful outputs despite safety alignment. Existing attacks show this vulnerability, but not the internal mechanisms that cause it. This study asks whether jailbreak success is driven by identifiable internal features rather than prompts alone. We propose a three-stage pipeline for Gemma-2-2B using the BeaverTails dataset. First, we extract concept-aligned tokens from adversarial responses via subspace similarity. Second, we apply three feature-grouping strategies (cluster, hierarchical-linkage, and single-token-driven) to identify SAE feature subgroups for the aligned tokens across all 26 model layers. Third, we steer the model by amplifying the top features from each identified subgroup and measure the change in harmfulness score using a standardized LLM-judge scoring protocol. In all three approaches, the features in the layers [16-25] were relatively more vulnerable to steering. All three methods confirmed that mid to later layer feature subgroups are more responsible for unsafe outputs. These results provide evidence that the jailbreak vulnerability in Gemma-2-2B is localized to feature subgroups of mid to later layers, suggesting that targeted feature-level interventions may offer a more principled path to adversarial robustness than current prompt-level defenses.

---


### 49. [UpstreamQA: A Modular Framework for Explicit Reasoning on Video Question Answering Tasks](https://arxiv.org/abs/2604.23145)

**<font color=#1a73e8>作者：</font>** Jason Nguyen, Ameet Rao, Alexander Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Question Answering (VideoQA) demands models that jointly reason over spatial, temporal, and linguistic cues. However, the task's inherent complexity often requires multi-step reasoning that current large multimodal models (LMMs) perform implicitly, leaving their internal decision process opaque. In contrast, large reasoning models (LRMs) explicitly generate intermediate logical steps that enhance interpretability and can improve multi-hop reasoning accuracy. Yet, these models are not designed for native video understanding, as they typically rely on static frame sampling. We propose UpstreamQA, a modular framework that disentangles and evaluates core video reasoning components through explicit upstream reasoning modules. Specifically, we employ multimodal LRMs to perform object identification and scene context generation before passing enriched reasoning traces to downstream LMMs for VideoQA. We evaluate UpstreamQA on the OpenEQA and NExTQA datasets using two LRMs (o4-mini, Gemini 2.5 Pro) and two LMMs (GPT-4o, Gemini 2.5 Flash). Our results demonstrate that introducing explicit reasoning can significantly boost performance and interpretability of downstream VideoQA, but can also lead to performance degradation when baseline performance is sufficiently high. Overall, UpstreamQA offers a principled framework for combining explicit reasoning and multimodal understanding, advancing both performance and diagnostic transparency in VideoQA in several scenarios.

---


### 50. [PhySE: A Psychological Framework for Real-Time AR-LLM Social Engineering Attacks](https://arxiv.org/abs/2604.23148)

**<font color=#1a73e8>作者：</font>** Tianlong Yu, Yang Yang, Ziyi Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emerging threat of AR-LLM-based Social Engineering (AR-LLM-SE) attacks (e.g. SEAR) poses a significant risk to real-world social interactions. In such an attack, a malicious actor uses Augmented Reality (AR) glasses to capture a target visual and vocal data. A Large Language Model (LLM) then analyzes this data to identify the individual and generate a detailed social profile. Subsequently, LLM-powered agents employ social engineering strategies, providing real-time conversation suggestions, to gain the target trust and ultimately execute phishing or other malicious acts. Despite its potential, the practical application of AR-LLM-SE faces two major bottlenecks, (1) Cold-start personalization, Current Retrieval-Augmented Generation (RAG) methods introduce critical delays in the earliest turns, slowing initial profile formation and disrupting real-time interaction, (2) Static Attack Strategies, Existing approaches rely on fixed-stage, handcrafted social engineering tactics that lack foundation in established psychological theory. To address these limitations, we propose PhySE, a novel framework with two core innovations, (1) VLM-Based SocialContext Training, To eliminate profiling delays, we efficiently pre-train a Visual Language Model (VLM) with social-context data, enabling rapid, on-the-fly profile generation, (2) Adaptive Psychological Agent, We introduce a psychological LLM that dynamically deploys distinct classes of psychological strategies based on target response, moving beyond static, handcrafted scripts. We evaluated PhySE through an IRB-approved user study with 60 participants, collecting a novel dataset of 360 annotated conversations across diverse social scenarios.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-215](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

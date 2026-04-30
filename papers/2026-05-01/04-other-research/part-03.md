# 📦 其他研究 | 2026年05月01日

> 本类共 **173** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-173](./part-04.md)

---

### 101. [Layer-wise Lipschitz-Product Control for Deep Kolmogorov--Arnold Network Representations of Compositionally Structured Functions](https://arxiv.org/abs/2604.26444)

**<font color=#1a73e8>作者：</font>** Aleksander Tankman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that any continuous function f from [0,1]^n to R representable by a finite computation tree with N internal nodes and compositional sparsity s = O(1) admits a deep Kolmogorov-Arnold Network (KAN) representation. Each internal node is realised by a primitive KAN block with controlled block depth and Lipschitz product. The layer-wise Lipschitz product satisfies the primary domain-sensitive bound independent of the input dimension n. It simplifies to P(KAN_f) <= max(C*,1)^L_f with L_f <= c_max * N. For the standard operations {+,-,x,sin,cos} with x nodes on [0,1]-bounded inputs we obtain P(KAN) <= 1. Layer widths satisfy n_l <= n + 2 w_max * N. The uniform approximation error is bounded by N * max(C*,1)^d(f) * epsilon_Op (simplifies when C* <=1). For f in C^m we obtain optimal B-spline rates. Range bounds are also derived (B_f <= N+1 for additive trees). This addresses the gap on Lipschitz control in deep KAN stacks noted by Liu et al. (2024). Experiments confirm P(KAN)=1.0 for several compositionally structured functions.

---


### 102. [Near-Optimal Cryptographic Hardness of Learning With Homogeneous Halfspaces Under Gaussian Marginals](https://arxiv.org/abs/2604.26446)

**<font color=#1a73e8>作者：</font>** Jizhou Huang, Brendan Juba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study three problems that involve identifying homogeneous halfspaces under Gaussian distributions: agnostic learning, one-sided reliable learning, and fairness auditing. In each of these problems, we are given labeled examples $(\mathbf{x}, \mathrm{y})$ drawn from an unknown distribution on $\mathbb{R}^d\times\{-1, +1\}$, whose marginal distribution on $\mathbf{x}$ is standard Gaussian and on $\mathrm{y}$ is arbitrary. The goal of each problem is to output a homogeneous halfspace that approaches the best-fitting homogeneous halfspace in terms of its corresponding loss measure. We prove near-optimal computational hardness results for these problems under the widely believed hardness assumption of the Learning With Errors (LWE) problem. Prior hardness results for these problems were mostly established for general halfspaces; our findings extend some of these hardness results to homogeneous halfspaces. Remarkably, our lower bound strictly generalizes over prior works and narrows the gap between the upper and lower bounds for agnostically learning homogeneous halfspaces under Gaussian marginals.

---


### 103. [Last-Layer-Centric Feature Recombination: Unleashing 3D Geometric Knowledge in DINOv3 for Monocular Depth Estimation](https://arxiv.org/abs/2604.26454)

**<font color=#1a73e8>作者：</font>** Gongshu Wang, Zhirui Wang, Kan Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation (MDE) is a fundamental yet inherently ill-posed task. Recent vision foundation models (VFMs), particularly DINO-based transformers, have significantly improved accuracy and generalization for dense prediction. Prior works generally follow a unified paradigm: sampling a fixed set of intermediate transformer layers at uniform intervals to build multi-scale features. This common practice implicitly assumes that geometric information is uniformly distributed across layers, which may underutilize the structural 3D cues encoded in VFMs. In this study, we present a systematic layer-wise analysis of DINOv3, revealing that 3D information is distributed non-uniformly: deeper layers exhibit stronger depth predictability and better capture inter-sample geometric variation. Motivated by this, we introduce a Last-Layer-Centric Feature Recombination (LFR) module to enhance geometric expressiveness. LFR treats the final layer as a geometric anchor and adaptively selects complementary intermediate layers according to a minimal-similarity criterion. Selected features are fused with the last-layer representation via compact linear this http URL experiments show that LFR module consistently improves MDE accuracy and achieves state-of-the-art performance. Our analysis sheds light on how geometric knowledge is organized within VFMs and offers an efficient strategy for unlocking their potential in dense 3D tasks.

---


### 104. [$\text{PKS}^4$:Parallel Kinematic Selective State Space Scanners for Efficient Video Understanding](https://arxiv.org/abs/2604.26461)

**<font color=#1a73e8>作者：</font>** Lingjie Zeng, Hailun Zhang, Xiwen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal modeling remains a fundamental challenge in video understanding, particularly as sequence lengths scale. Traditional video models relying on dense spatiotemporal attention suffer from quadratic computational costs for long videos. To circumvent these costs, recent approaches adapt image models for videos via Parameter-Efficient Fine-Tuning (PEFT) methods such as adapters. However, deeply inserting these modules incurs prohibitive activation memory overhead during back-propagation. While recent efficient State Space Models (SSMs) introduce linear complexity, they disrupt 2D spatial relationships and rely on extensive masked pre-training to recover spatial awareness.
To overcome these limitations, we propose Parallel Kinematic Selective State Space Scanners (PKS$^4$). We retain a standard 2D vision backbone for spatial semantics and insert a single plug-and-play PKS$^4$ module with linear-complexity temporal scanning, avoiding temporal attention and multi-layer adapters. We first extract kinematic priors via a Kinematic Prior Encoder, which captures local displacements and motion boundaries through inter-frame correlations and differences. These priors drive linear-complexity SSMs to track underlying kinematic states, adaptively modulating update speeds and read-write strategies at each time step.
Instead of global scanning, we deploy parallel scanners along the temporal dimension for each spatial location, preserving spatial structures while reducing overhead. Experiments on spatial-heavy and temporal-heavy action recognition benchmarks show that PKS$^4$ achieves state-of-the-art performance. Remarkably, our method converges in merely $20$ epochs, achieving approximately $10\times$ lower training compute than pure video SSMs, establishing a new paradigm for efficient video understanding.

---


### 105. [A Multistage Extraction Pipeline for Long Scanned Financial Documents: An Empirical Study in Industrial KYC Workflows](https://arxiv.org/abs/2604.26462)

**<font color=#1a73e8>作者：</font>** Yuxuan Han, Yuanxing Zhang, Yushuo Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured information extraction from long, multilingual scanned financial documents is a core requirement in industrial KYC and compliance workflows. These documents are typically non machine readable, noisy, and visually heterogeneous. They usually span dozens of pages while containing only sparse task relevant information. Although recent vision-language models achieve strong benchmark performance, directly applying them end to end to full financial reports often leads to unreliable extraction under real world conditions. We present a multistage extraction framework that integrates image preprocessing, multilingual OCR, hybrid page-level retrieval, and compact VLM-based structured extraction. The design separates page localization from multimodal reasoning, enabling more accurate extraction from complex multipage documents. We evaluated the framework on 120 production KYC documents comprising about 3000 multilingual scanned pages. Across multiple OCR-VLM combinations, the proposed pipeline consistently outperforms direct PDF-to-VLM baselines, improving field-level accuracy by up to 31.9 percentage points. The best configuration, PaddleOCR with MiniCPM2.6, achieves 87.27 percent accuracy. Ablation studies show that page-level retrieval is the dominant factor in performance improvements, particularly for complex financial statements and non-English documents.

---


### 106. [Differentially Private Contrastive Learning via Bounding Group-level Contribution](https://arxiv.org/abs/2604.26467)

**<font color=#1a73e8>作者：</font>** Kecen Li, Chen Gong, Zinan Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differentially private (DP) contrastive learning aims to learn general-purpose representations from sensitive data, alleviating the privacy leakage concerns of organizations deploying or sharing embedding models trained on private user content. However, existing approaches suffer from severe utility degradation due to the over-strong inter-sample dependency inherent in standard contrastive objectives, where each sample's gradient depends on all other samples in the batch, amplifying the impact of DP noise. In this work, we argue that effective DP contrastive learning requires explicitly reducing such intrinsic inter-sample reliance. To this end, we propose DP-GCL, a principled DP contrastive learning framework that structurally limits gradient dependency through bounding group-level contribution. DP-GCL partitions each batch into small, disjoint groups and restricts available negative samples to within-group samples, thereby localizing gradient influence and reducing sensitivity. To counteract the resulting loss of negative sample diversity, we further introduce intra-group augmentation, which generates additional negative views without increasing privacy cost. Extensive experiments across eight datasets demonstrate that DP-GCL consistently advances the state of the art in both uni-modal and multi-modal contrastive learning under practical privacy budgets: it improves image classification accuracy by 5.6% and image-text retrieval accuracy by 20.1% over existing DP contrastive methods.

---


### 107. [Hierarchical adaptive control for real-time dynamic inference at the edge](https://arxiv.org/abs/2604.26470)

**<font color=#1a73e8>作者：</font>** Francesco Daghero, Mahyar Tourchi Moghaddam, Mikkel Baun Kjærgaard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial systems increasingly depend on Machine Learning (ML), and operate on heterogeneous nodes that must satisfy tight latency, energy, and memory constraints. Dynamic ML models, which reconfigure their computational footprint at runtime, promise high energy efficiency and lower average latency for modest accuracy tradeoffs; however, their deployment is complex due to the additional hyperparameters they rely on. These hyperparameters, controlling the accuracy versus average latency tradeoff, are often tuned on a calibration dataset that must match the test time distribution, an assumption that rarely holds in real-world scenarios, leading to suboptimal operational conditions, possibly below static models. We propose a two-tier adaptive architecture that co-optimizes model and system decisions. At the global level, a scheduler configures and deploys, for each edge node, a cascade of classifiers composed of lightweight specialized models and a generalist fallback, satisfying latency and memory constraints. At the node level, a local controller tracks data drifts and hardware resources, enabling or disabling specialized predictors (SP) to preserve high energy efficiency and avoid latency-constraint violations under varying conditions. This design allows longer operating times without forcing a global redeployment step, and enables efficient execution in case of an unreachable remote global controller. We evaluate the approach on two datasets under controlled distribution mismatch scenarios, showing average per-inference reductions of latency up to 2.45x and energy up to 2.86x, with less than 4% accuracy drop compared to static baselines. Our contributions are:(1) a budgeted SP-cascade formulation that preserves worst-case latency constraints;(2) a hierarchical controller that maintains efficiency under data and resource changes; and (3) an experimental evaluation on embedded hardware.

---


### 108. [Featurising Pixels from Dynamic 3D Scenes with Linear In-Context Learners](https://arxiv.org/abs/2604.26488)

**<font color=#1a73e8>作者：</font>** Nikita Araslanov, Martin Sundermeyer, Hidenobu Matsuki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One of the most exciting applications of vision models involve pixel-level reasoning. Despite the abundance of vision foundation models, we still lack representations that effectively embed spatio-temporal properties of visual scenes at the pixel level. Existing frameworks either train on image-based pretext tasks, which do not account for dynamic elements, or on video sequences for action-level reasoning, which does not scale to dense pixel-level prediction. We present a framework that learns pixel-accurate feature descriptors from videos, LILA. The core element of our training framework is linear in-context learning. LILA leverages spatio-temporal cue maps -- depth and motion -- estimated with off-the-shelf networks. Despite the noisy nature of those cues, LILA trains effectively on uncurated video datasets, embedding semantic and geometric properties in a temporally consistent manner. We demonstrate compelling empirical benefits of the learned representation across a diverse suite of vision tasks: video object segmentation, surface normal estimation and semantic segmentation.

---


### 109. [Understanding DNNs in Feature Interaction Models: A Dimensional Collapse Perspective](https://arxiv.org/abs/2604.26489)

**<font color=#1a73e8>作者：</font>** Jiancheng Wang, Mingjia Yin, Hao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DNNs have gained widespread adoption in feature interaction recommendation models. However, there has been a longstanding debate on their roles. On one hand, some works claim that DNNs possess the ability to implicitly capture high-order feature interactions. Conversely, recent studies have highlighted the limitations of DNNs in effectively learning dot products, specifically second-order interactions, let alone higher-order interactions. In this paper, we present a novel perspective to understand the effectiveness of DNNs: their impact on the dimensional robustness of the representations. In particular, we conduct extensive experiments involving both parallel DNNs and stacked DNNs. Our evaluation encompasses an overall study of complete DNN on two feature interaction models, alongside a fine-grained ablation analysis of components within DNNs. Experimental results demonstrate that both parallel and stacked DNNs can effectively mitigate the dimensional collapse of embeddings. Furthermore, a gradient-based theoretical analysis, supported by empirical evidence, uncovers the underlying mechanisms of dimensional collapse.

---


### 110. [Culturally Aware GenAI Risks for Youth: Perspectives from Youth, Parents, and Teachers in a Non-Western Context](https://arxiv.org/abs/2604.26494)

**<font color=#1a73e8>作者：</font>** Aljawharah Alzahrani, Tory Park, Tanusree Sharma  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI tools are widely used by youth and have introduced new privacy and safety challenges. While prior research has explored youth's safety in GenAI within western context, it often overlooks the cultural, religious, and social dimensions of technology use that strongly shape youths digital experiences in countries like Saudi Arabia. To address the gap, this study explores children (aged 7 to 17), parents and teachers interactions with GenAI tools and risk perceptions through non-western lens. Through a mixed methods approach, we analyzed 736 Reddit and 1,262 X(Twitter) posts and conducted interviews with 31 Saudi Arabian participants (8 youth, 13 parents, 10 teachers). Our findings highlight context dependent and relational privacy and safety of GenAI from non-western context which often formed by communal structure and prescribed norms. We found significant risks tied to youths disclosure of personal and family information, which conflict with culturally rooted expectations of modesty, privacy, and honor, particularly when youth seek emotional support from GenAI. These risks further compounded by socio economic factors such as cost-saving practices leading to the use of shared GenAI accounts (this http URL) within families or even among strangers. We provide design implication reflecting on parents and teachers expectation of how youth should use GenAI. This work lays groundwork for inclusive, context sensitive parental controls that adhere to cultural norms and values.

---


### 111. [Beyond Code Reasoning: A Specification-Anchored Audit Framework for Expert-Augmented Security Verification](https://arxiv.org/abs/2604.26495)

**<font color=#1a73e8>作者：</font>** Masato Kamba, Hirotake Murakami, Akiyoshi Sannai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security-critical software is routinely audited by tools that reason about vulnerabilities as repository-local code patterns. Yet specification-governed systems -- protocol stacks, consensus implementations, cryptographic libraries -- are constrained by invariants and correctness conditions defined in natural-language specifications. When a vulnerability arises from what the specification requires rather than how code is written, code-level approaches lack the representational vocabulary to detect it, and their false positives resist systematic diagnosis.
We present SPECA, a specification-anchored security audit framework that derives explicit, typed security properties from natural-language specifications and audits implementations through structured proof-attempt reasoning grounded in each property. The framework yields three capabilities absent from code-driven auditing: spec-dependent detections, controlled cross-implementation comparison under a shared property vocabulary, and false positives that decompose into interpretable, pipeline-phase-traceable root causes.
On the Sherlock Ethereum Fusaka Audit Contest (366 submissions, 10 implementations), SPECA recovers all 15 in-scope vulnerabilities and independently discovers 4 bugs confirmed by developer fix commits. On the RepoAudit C/C++ benchmark (15 projects), SPECA matches the best published precision (88.9\%) while surfacing 12 candidate bugs beyond the established ground truth, two confirmed by upstream maintainers. A multi-model analysis reveals that more capable models audit more faithfully within property scope, shifting the detection bottleneck from model reasoning to property generation quality. All false positives trace to three recurring root causes -- trust boundary misunderstanding, code reading errors, and specification misinterpretation -- each yielding actionable improvement targets.

---


### 112. [StarDrinks: An English and Korean Test Set for SLU Evaluation in a Drink Ordering Scenario](https://arxiv.org/abs/2604.26500)

**<font color=#1a73e8>作者：</font>** Marcely Zanon Boito, Caroline Brun, Inyoung Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs and speech assistants are increasingly used for task-oriented interactions, yet their evaluation often relies on controlled scenarios that fail to capture the variability and complexity of real user requests. Drink ordering, for example, involves diverse named entities, drink types, sizes, customizations, and brand-specific terminology, as well as spontaneous speech phenomena such as hesitations and self-corrections. To address this gap, we introduce StarDrinks, a test set in English and Korean containing speech utterances features, transcriptions, and annotated slots. Our dataset supports speech-to-slots SLU, transcription-to-slots NLU, and speech-to-transcription ASR evaluation, providing a realistic benchmark for model robustness and generalization in a linguistically rich, real-world task.

---


### 113. [Tree-of-Text: A Tree-based Prompting Framework for Table-to-Text Generation in the Sports Domain](https://arxiv.org/abs/2604.26501)

**<font color=#1a73e8>作者：</font>** Shang-Hsuan Chiang, Tsan-Tsung Yang, An-Zi Yen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating sports game reports from structured tables is a complex table-to-text task that demands both precise data interpretation and fluent narrative generation. Traditional model-based approaches require large, annotated datasets, while prompt-based methods using large language models (LLMs) often struggle with hallucination due to weak table comprehension. To overcome these challenges, we propose Tree-of-Text, a tree-structured prompting framework that guides LLMs through a three-stage generation process: (1) Content Planning, where relevant operations and arguments are selected from the input tables; (2) Operation Execution, which breaks down large tables into manageable sub-tables; and (3) Content Generation, where short textual outputs are merged and rewritten into a cohesive report. Experiments show that our method outperforms existing methods on ShuttleSet+, leads in RG and CO metrics on RotoWire-FG, and excels in CS and CO on MLB with roughly 40% of the time and cost of Chain-of-Table. These results demonstrate the effectiveness and efficiency of Tree-of-Text and suggest a promising direction for prompt-based table-to-text generation in the sports domain.

---


### 114. [Delta Score Matters! Spatial Adaptive Multi Guidance in Diffusion Models](https://arxiv.org/abs/2604.26503)

**<font color=#1a73e8>作者：</font>** Haosen Li, Wenshuo Chen, Lei Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable success in synthesizing complex static and temporal visuals, a breakthrough largely driven by Classifier-Free Guidance (CFG). However, despite its pivotal role in aligning generated content with textual prompts, standard CFG relies on a globally uniform scalar. This homogeneous amplification traps models in a well-documented "detail-artifact dilemma": low guidance scales fail to inject intricate semantics, while high scales inevitably cause structural degradation, color over-saturation, and temporal inconsistencies in videos. In this paper, we expose the physical root of this flaw through the lens of differential geometry. By analyzing Tweedie's Formula, we reveal that CFG intrinsically performs a tangential linear extrapolation. Because the natural data manifold is highly curved, this uniform linear step introduces a severe orthogonal deviation. To keep the generation trajectory safely bounded, we formulate a theoretical upper bound for spatial and adaptive guidance. Based on these geometric insights, we propose Spatial Adaptive Multi Guidance (SAMG), a training-free and virtually zero-cost sampling algorithm. SAMG dynamically computes point-wise conditional guidance energy, applying a conservative minimum scale to high-energy boundary regions to preserve delicate micro-textures, while deploying an aggressive maximum scale in low-energy regions to maximize semantic injection. Extensive experiments across diverse image (SD 1.5, SDXL, SD3.5 Medium) and video (CogVideoX, ModelScope) architectures demonstrate that SAMG effectively resolves the detail-artifact dilemma, achieving superior semantic alignment, structural integrity, and temporal smoothness without any computational overhead.

---


### 115. [Quantamination: Dynamic Quantization Leaks Your Data Across the Batch](https://arxiv.org/abs/2604.26505)

**<font color=#1a73e8>作者：</font>** Hanna Foerster, Ilia Shumailov, Cheng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dynamic quantization emerged as a practical approach to increase the utilization and efficiency of the machine learning serving flow. Unlike static quantization, which applies quantization offline, dynamic quantization operates on tensors at run-time, adapting its parameters to the actual input data. Today's mainstream machine learning frameworks, including ML compilers and inference engines, frequently recommend dynamic quantization as an initial step for optimizing model serving. This is because dynamic quantization can significantly reduce memory usage and computational load, leading to faster token generation and improved model serving efficiency without substantial loss in model accuracy. In this paper, we reveal a critical vulnerability in dynamic quantization: an adversary can exploit such quantization strategy to steal sensitive user data placed in the same batch as the adversary's input. Our analysis demonstrates that dynamic quantization, when improperly implemented or configured, can create side channels that expose information about other inputs within the same batch. We call this phenomenon Quantamination, describing contamination from quantization. Specifically, we show that at least 4 of the most popular ML frameworks in use today either default to or can use configurations that leak data across the batch boundary. This data leakage, in theory, allows attackers to partially or even fully recover other users' batched input data, representing a serious privacy risk for existing ML serving frameworks.

---


### 116. [Auto-Relational Reasoning](https://arxiv.org/abs/2604.26507)

**<font color=#1a73e8>作者：</font>** Ioannis Konstantoulas, Dimosthenis Tsimas, Pavlos Peppas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background & Objectives: In the last decade, Machine learning research has grown rapidly, but large models are reaching their soft limits demonstrating diminishing returns and still lack solid reasoning abilities. These limits could be surpassed through synergistic combination of Machine Learning scalability and rigid reasoning. Methods: In this work, we propose a theoretical framework for reasoning through object-relations in an automated manner integrated with Artificial Neural Networks. We present a formal analysis of the Reasoning, and we show the theory in practice through a paradigm integrating Reasoning and Machine Learning. Results: This paradigm is a system that solves Intelligence Quotient problems without any prior knowledge of the problem. Our system achieves 98.03% solving rate corresponding to the top 1% percentile or 132-144 iq score. This result is only limited by the small size of the model and the processing capabilities of the machine it run on. Conclusions: With the integration of prior knowledge in the system and the expansion of the dataset, the system can be generalized to solve a large category of problems. The functionality of the system inherently favors the solution of such problems in few-shot or zero-shot attempts.

---


### 117. [Text-Utilization for Encoder-dominated Speech Recognition Models](https://arxiv.org/abs/2604.26514)

**<font color=#1a73e8>作者：</font>** Albert Zeyer, Tim Posielek, Ralf Schlüter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates efficient methods for utilizing text-only data to improve speech recognition, focusing on encoder-dominated models that facilitate faster recognition. We provide a comprehensive comparison of techniques to integrate text-only data, including modality matching and dynamic downsampling to reach text-level representations within the encoder. Our experiments on the LibriSpeech corpus show that a larger encoder with a smaller decoder can equal or surpass the performance of architectures with larger decoders. We demonstrate that simple configurations, such as random duration models, are often more effective than complex alternatives, significantly simplifying the training pipeline. All code and recipes are made publicly available.

---


### 118. [MTCurv: Deep learning for direct microtubule curvature mapping in noisy fluorescence microscopy images](https://arxiv.org/abs/2604.26517)

**<font color=#1a73e8>作者：</font>** Achraf Ait Laydi, Sidi Mohamed Sid'El Moctar, Yousef El Mourabit 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate quantification of the geometry of curvilinear biological structures is essential for understanding cellular mechanics and disease-related morphological alterations. Microtubule curvature is a key descriptor of filament rigidity and mechanical perturbations. However, reliable curvature extraction from fluorescence microscopy images remains challenging due to noise, low contrast, and partial filament visibility. Existing approaches rely on segmentation pipelines with pre or post-processing, which are highly sensitive to segmentation errors and often fail under adverse imaging conditions. In this work, we propose MTCurv, a deep learning framework for direct, segmenta-tion-free regression of microtubule curvature maps from noisy microscopy images. Leveraging a synthetic dataset with pixel-wise curvature annotations, we reformulated curvature estimation as a regression problem and adapted an attention-based residual U-Net. To reduce hallucinations and enforce spatial coherence, we introduced a gradient-aware loss combining Mean Squared Error with a gradient consistency term. Beyond model and loss design, we evaluated commonly used regression and image quality metrics, revealing that many perceptual and blind metrics are poorly suited for curvature estimation. Correlation-based metrics, particularly Spearman correlation, emerged as more reliable indicators of curvature prediction quality. Experiments on two datasets of increasing difficulty demonstrated that MTCurv accurately recovers local microtubule curvatures, even in the presence of background fluorescence. Ablation studies highlighted the contribution of both residual encoding and attention-based decoding. Overall, this work provides a practical tool for filament curvature analysis and methodological insights for geometry-aware regression in biomedical imaging. Datasets and code are made available.

---


### 119. [GIFGuard: Proactive Forensics against Deepfakes in Facial GIFs via Spatiotemporal Watermarking](https://arxiv.org/abs/2604.26519)

**<font color=#1a73e8>作者：</font>** Shupeng Che, Zhiqing Guo, Changtao Miao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of deepfake technology poses an unprecedented threat to the authenticity of Graphics Interchange Format (GIF) imagery, which serves as a representative of short-loop temporal media in social networks. However, existing proactive forensics works are designed for static images, which limits their applicability to animated GIFs. To bridge this gap, we propose GIFGuard, the first spatiotemporal watermarking framework tailored for deepfake proactive forensics in GIFs. In the embedding stage, we propose the Spatiotemporal Adaptive Residual Encoder (STARE) to ensure robustness against high-level semantic tampering. It employs a 3D convolutional backbone with adaptive channel recalibration to capture globally coherent temporal dependencies. In the extraction stage, we design the Deep Integrity Restoration Decoder (DIRD). It utilizes a spatiotemporal hourglass architecture equipped with 3D attention to restore latent features, allowing for the accurate extraction of watermark signals even under severe facial manipulation. Furthermore, we construct GIFfaces, the first large-scale benchmark dataset curated for GIF proactive forensics to facilitate research in this domain. Extensive results show that GIFGuard achieves high-fidelity visual quality and remarkable robustness performance against deepfakes. Related code and dataset will be released.

---


### 120. [3D-LENS: A 3D Lifting-based Elevated Novel-view Synthesis method for Single-View Aerial-Ground Re-Identification](https://arxiv.org/abs/2604.26520)

**<font color=#1a73e8>作者：</font>** William Grolleau, Astrid Sabourin, Guillaume Lapouge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial-Ground Re-Identification (AG-ReID) is constrained by the viewpoint-domain gap, as drastic viewpoint disparities occlude or distort discriminative features, making cross-viewpoint image retrieval challenging. While existing methods rely on paired cross-view annotations, real-world deployments, such as wilderness search-and-rescue (SAR), often lack target-domain data, requiring retrieval from ground-level references alone. To our knowledge, we are the first to address this challenge by formalizing the Single-View AG-ReID (SV AG-ReID) setting, where models trained on a single real viewpoint must generalize to an unseen viewpoint. We propose 3D Lifting-based Elevated Novel-view Synthesis (3D-LENS), a unified framework combining geometrically-consistent novel view synthesis that leverages large-scale 3D mesh reconstruction, with a robust representation learning scheme to mitigate synthetic-to-real bias. Unlike 2D generative baselines that suffer from geometric inconsistencies or prior 3D methods that are restricted to class-specific templates, our approach ensures view-consistent synthesis across diverse categories without predefined templates that fail to capture fine-grained details, such as carried objects. Extensive experiments demonstrate that our method achieves state-of-the-art performance on SV AG-ReID scenarios. Code and data will be released at this https URL.

---


### 121. [Grounding vs. Compositionality: On the Non-Complementarity of Reasoning in Neuro-Symbolic Systems](https://arxiv.org/abs/2604.26521)

**<font color=#1a73e8>作者：</font>** Mahnoor Shahid, Hannes Rothe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compositional generalization remains a foundational weakness of modern neural networks, limiting their robustness and applicability in domains requiring out-of-distribution reasoning. A central, yet unverified, assumption in neuro-symbolic AI is that compositional reasoning will emerge as a byproduct of successful symbol grounding. This work presents the first systematic empirical analysis to challenge this assumption by disentangling the contributions of grounding and reasoning. To operationalize this investigation, we introduce the Iterative Logic Tensor Network ($i$LTN), a fully differentiable architecture designed for multi-step deduction. Using a formal taxonomy of generalization -- probing for novel entities, unseen relations, and complex rule compositions -- we demonstrate that a model trained solely on a grounding objective fails to generalize. In contrast, our full $i$LTN, trained jointly on perceptual grounding and multi-step reasoning, achieves high zero-shot accuracy across all tasks. Our findings provide conclusive evidence that symbol grounding, while necessary, is insufficient for generalization, establishing that reasoning is not an emergent property but a distinct capability that requires an explicit learning objective.

---


### 122. [Persona-Based Process Design for Assistive Human-Robot Workplaces for Persons with Disabilities](https://arxiv.org/abs/2604.26527)

**<font color=#1a73e8>作者：</font>** Nils Mandischer, Daria Eckert and, Lars Mikelsons  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-robot interaction is emerging as an important paradigm for integrating persons with disabilities into the workplace. While these systems can enable individuals to work, their design is mostly personalized, hindering widespread use beyond the individual user. The universal design paradigm is a central pillar of inclusive design, describing usability of systems by all. To incorporate universal design into process design for human-robot workplaces expert knowledge is required that is often not available. To simplify process design of human-robot workplaces, we propose a persona-based design approach. First, typical impairments prevalent in the workforce or particularly relevant for the processes are abstracted into personas with disabilities. The work process is subdivided into sequential actions. For each action and persona, strategies are developed to reach the action goal by a design thinking approach. The resulting actions are ordered by level of robot assistance, i.e. robot involvement, and implemented in a behavior tree. Therefore, the macro-behavior of the workplace may adapt to individual personas online. We demonstrate the method in a collaborative box folding process with a total of seven personas with disabilities. The persona-based process design shows promising results by generating more comprehensive process strategies while enabling adaptive behavior in the sense of universal design.

---


### 123. [Preventing Distinguishability between Multiplication and Squaring Operations](https://arxiv.org/abs/2604.26536)

**<font color=#1a73e8>作者：</font>** Alkistis Aikaterini Sigourou, Zoya Dyka, Peter Langendoerfer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Scalar multiplication kP is a critical operation in Elliptic Curve Cryptosystems (ECC), often targeted by Side-Channel Analysis (SCA). Despite strategies based on atomic patterns to enhance security, the binary kP algorithms remain susceptible to simple SCA due to energy consumption variations in field multipliers during passing two different or two identical operands. This vulnerability arises independent of the multiplication method used. We implemented and analysed two mitigation techniques: one involving data redirection and another focusing on bus reloading.

---


### 124. [Large-scale semi-supervised learning with online spectral graph sparsification](https://arxiv.org/abs/2604.26550)

**<font color=#1a73e8>作者：</font>** Daniele Calandriello, Alessandro Lazaric, Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Sparse-HFS, a scalable algorithm that can compute solutions to SSL problems using only O(n polylog(n)) space and O(m polylog(n)) time.

---


### 125. [Preserving Disagreement: Architectural Heterogeneity and Coherence Validation in Multi-Agent Policy Simulation](https://arxiv.org/abs/2604.26561)

**<font color=#1a73e8>作者：</font>** Ariel Sela  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent deliberation systems using large language models (LLMs) are increasingly proposed for policy simulation, yet they suffer from artificial consensus: evaluator agents converge on the same option regardless of their assigned value perspectives. We present the AI Council, a three-phase deliberation framework, and conduct 120 deliberations across two policy scenarios to test two interventions. First, architectural heterogeneity (assigning a different 7-9B parameter model to each value perspective) significantly reduces first-choice concentration compared to a homogeneous baseline (child welfare: 70.9% to 46.1%, p < 0.001, r = 0.58; housing: 46.0% to 22.9%, p < 0.001, r = 0.50). This contrasts with accuracy-oriented multi-agent debate, where heterogeneity does not reduce convergence, suggesting model diversity operates differently when no objectively correct answer exists. Second, coherence validation (using a frontier model to assess whether each evaluator's reasoning is grounded in its assigned values) reveals a fidelity-diversity tradeoff: on a scenario with a dominant option, it further reduces concentration (46.1% to 40.8%, p = 0.004), but on a scenario with genuinely competitive options, it increases concentration (22.9% to 26.6%, p = 0.96) by amplifying high-coherence evaluators who cluster on one option. This tradeoff may be a general property of multi-agent systems employing quality weighting. We report negative results from three failed Delphi designs, demonstrate that 8B models exhibit binary rather than graded responses to counter-arguments, and propose the trustworthy tension rate as a diagnostic measure of small-model deliberation capabilities.

---


### 126. [AirZoo: A Unified Large-Scale Dataset for Grounding Aerial Geometric 3D Vision](https://arxiv.org/abs/2604.26567)

**<font color=#1a73e8>作者：</font>** Xiaoya Cheng, Rouwan Wu, Xinyi Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid progress in data-driven 3D vision, aerial geometric 3D vision remains a formidable challenge due to the severe scarcity of large-scale, high-fidelity training data. Existing benchmarks, predominantly biased toward ground-level or object-centric views, do not account for complex viewpoint transformations and diverse environmental conditions in UAV-based sensing. To bridge this critical gap, we propose AirZoo, a unified large-scale dataset and benchmark for grounding aerial geometric 3D vision. AirZoo possesses three appealing properties: 1) Scalable Generation Pipeline: Leveraging freely available, world-scale photogrammetric 3D meshes, it renders vast outdoor environments with customizable UAV flight trajectories and configurable weather/illumination. 2) Comprehensive Scene Diversity: It provides the most extensive coverage of region types to date (spanning 378 regions across 22 countries), systematically encompassing both highly structured urban landscapes and complex unstructured natural environments. 3) Rich Geometric Annotations: Each frame provides synchronized, pixel-level metric depth and precise 6-DoF geo-referenced poses, essential for geometry-aware learning. Through three rigorous evaluation tracks -- aerial image retrieval, cross-view matching, and multi-view 3D reconstruction -- we demonstrate that AirZoo serves as a powerful pre-training engine. Extensive experiments on both public and newly collected real-world benchmarks reveal that fine-tuning on AirZoo yields substantial performance gains for SoTA models (e.g., MegaLoc, RoMa, VGGT, and Depth Anything 3), establishing a new performance upper bound for aerial spatial intelligence.

---


### 127. [Star-Fusion: A Multi-modal Transformer Architecture for Discrete Celestial Orientation via Spherical Topology](https://arxiv.org/abs/2604.26582)

**<font color=#1a73e8>作者：</font>** May Hammad, Menatallh Hammad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable celestial attitude determination is a critical requirement for autonomous spacecraft navigation, yet traditional "Lost-in-Space" (LIS) algorithms often suffer from high computational overhead and sensitivity to sensor-induced noise. While deep learning has emerged as a promising alternative, standard regression models are often confounded by the non-Euclidean topology of the celestial sphere and by the periodic boundary conditions of Right Ascension (RA) and Declination (Dec). In this paper, we present Star-Fusion, a multi-modal architecture that reformulates orientation estimation as a discrete topological classification task. Our approach leverages spherical K-Means clustering to partition the celestial sphere into K topologically consistent regions, effectively mitigating coordinate wrapping artifacts. The proposed architecture employs a tripartite fusion strategy: a SwinV2-Tiny transformer backbone for photometric feature extraction, a convolutional heatmap branch for spatial grounding, and a coordinate-based MLP for geometric anchoring. Experimental evaluations on a synthetic Hipparcos-derived dataset demonstrate that Star-Fusion achieves a Top-1 accuracy of 93.4% and a Top-3 accuracy of 97.8%. Furthermore, the model exhibits high computational efficiency, maintaining an inference latency of 18.4 ms on resource-constrained COTS hardware, making it a viable candidate for real-time onboard deployment in next-generation satellite constellations.

---


### 128. [PiGGO: Physics-Guided Learnable Graph Kalman Filters for Virtual Sensing of Nonlinear Dynamic Structures under Uncertainty](https://arxiv.org/abs/2604.26593)

**<font color=#1a73e8>作者：</font>** Marcus Haywood-Alexander, Gregory Duthé, Eleni Chatzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital twins provide a powerful paradigm for diagnostic and prognostic tasks in the monitoring and control of engineered systems; however, their deployment for complex structures remains challenged by model-form uncertainty, arising from unknown nonlinear dynamics, and by sparse sensing. These limitations hinder reliable online state estimation using either purely physics-based or purely data-driven approaches. This work introduces the Physics-Guided Graph Neural ODE (PiGGO) framework, a physics-informed, graph-based Bayesian state estimation approach in which a learned graph neural ordinary differential equation (GNODE) serves as the continuous-time state-transition model within an extended Kalman filter. The graph representation explicitly defines the system state-space, while physics-guided inductive biases encode known structural relationships and constrain the learning of nonlinear dynamics. By integrating graph-native learned dynamics with recursive Bayesian filtering, the proposed PiGGO framework enables online virtual sensing and uncertainty-aware state estimation for nonlinear systems with unknown model form, while maintaining generalisation across topologically similar structures. Numerical case studies demonstrate improved robustness to model uncertainty and measurement noise, outperforming both open-loop graph neural models and conventional filtering approaches in online prediction tasks.

---


### 129. [FunFace: Feature Utility and Norm Estimation for Face Recognition](https://arxiv.org/abs/2604.26598)

**<font color=#1a73e8>作者：</font>** Žiga Babnik, Fadi Boutros, Naser Damer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Recognition (FR) is used in a variety of application domains, from entertainment and banking to security and surveillance. Such applications rely on the FR model to be robust and perform well in a variety of settings. To achieve this, state-of-the-art FR models typically use expressive adaptive margin loss functions, which tie the feature norm to concepts related to sample quality, such as recognizability and perceptual image quality. Recently, through the development of Face Image Quality Assessment (FIQA) techniques, biometric utility has become the preferred measure of face-image quality and has been shown to be a better predictor of the usefulness of samples for face recognition compared to more human-centric aspects, such as resolution, blur, and lighting, tied to general image quality. While image quality expressed through feature norms exhibits a certain level of correlation with biometric utility, it does not fully encapsulate all aspects of utility. To address this point, we propose a new adaptive margin loss, FunFace (Face Recognition Through Utility and Norm Estimation), which incorporates biometric utility, estimated by the Certainty Ratio, into the adaptive margin, taking inspiration from AdaFace. We show that FunFace (when used to train a face recognition model) achieves competitive results to other state-of-the-art FR models on benchmarks containing high-quality samples, while surpassing them on low quality benchmarks.

---


### 130. [SnapPose3D: Diffusion-Based Single-Frame 2D-to-3D Lifting of Human Poses](https://arxiv.org/abs/2604.26620)

**<font color=#1a73e8>作者：</font>** Alessandro Simoni, Riccardo Catalini, Davide Di Nucci 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth ambiguity and joint uncertainty are the two main obstacles in obtaining accurate human pose predictions by 2D-to-3D lifting methods proposed in the literature. In particular, these issues are caused by 2D joint locations that can be mapped to multiple 3D positions, inducing multiple possible final poses. Following these considerations, we propose leveraging diffusion-based models generation capability to predict multiple hypotheses and aggregate them in a final accurate pose. Therefore, we introduce SnapPose3D, a pose-lifting framework trained deterministically to denoise 3D poses conditioned on both visual context and 2D pose features. SnapPose3D adopts a probabilistic approach during inference, generating multiple hypotheses through random sampling from a unit Gaussian distribution. Unlike most previous methods that address pose ambiguity by processing temporal sequences, SnapPose3D uses single frames as input, avoiding tracking and limiting computational cost, data acquisition complexity, and the need for online, real-time applications. We extensively evaluate SnapPose3D on well-known benchmarks for the 3D human pose estimation task showing its ability to generate and aggregate accurate hypotheses that lead to state-of-the-art results.

---


### 131. [OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory](https://arxiv.org/abs/2604.26622)

**<font color=#1a73e8>作者：</font>** Jinze Li, Yang Zhang, Xin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents increasingly operate in long-horizon, interactive settings where success depends on reusing experience accumulated over extended histories. However, existing agent memory systems are fundamentally constrained by text-context budgets: storing or revisiting raw trajectories is prohibitively token-expensive, while summarization and text-only retrieval trade token savings for information loss and fragmented evidence. To address this limitation, we propose Optical Context Retrieval Memory (OCR-Memory), a memory framework that leverages the visual modality as a high-density representation of agent experience, enabling retention of arbitrarily long histories with minimal prompt overhead at retrieval time. Specifically, OCR-Memory renders historical trajectories into images annotated with unique visual identifiers. OCR-Memory retrieves stored experience via a \emph{locate-and-transcribe} paradigm that selects relevant regions through visual anchors and retrieves the corresponding verbatim text, avoiding free-form generation and reducing hallucination. Experiments on long-horizon agent benchmarks show consistent gains under strict context limits, demonstrating that optical encoding increases effective memory capacity while preserving faithful evidence recovery.

---


### 132. [SAGE: A Strategy-Aware Graph-Enhanced Generation Framework For Online Counseling](https://arxiv.org/abs/2604.26630)

**<font color=#1a73e8>作者：</font>** Eliya Naomi Aharon, Meytal Grimland, Avi Segal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective mental health counseling is a complex, theory-driven process requiring the simultaneous integration of psychological frameworks, real-time distress signals, and strategic intervention planning. This level of clinical reasoning is critical for safety and therapeutic effectiveness but is often missing in general-purpose Large Language Models (LLMs). We introduce SAGE (Strategy-Aware Graph-Enhanced), a novel framework designed to bridge the gap between structured clinical knowledge and generative AI. SAGE constructs a heterogeneous graph that unifies conversational dynamics with a psychologically grounded layer, explicitly anchoring interactions in a theory-driven lexicon. Our architecture first employs a Next Strategy Classifier to identify the optimal therapeutic intervention. Subsequently, a Graph-Aware Attention mechanism projects graph-derived structural signals into soft prompts, conditioning the LLM to generate responses that maintain clinical depth. Validated through both automated metrics and expert human evaluation, SAGE outperforms baselines in strategy prediction and recommended response quality. By providing actionable intervention recommendations, SAGE serves as a cutting-edge decision-support tool designed to augment human expertise in high-stakes crisis counseling.

---


### 133. [SynSur: An end-to-end generative pipeline for synthetic industrial surface defect generation and detection](https://arxiv.org/abs/2604.26633)

**<font color=#1a73e8>作者：</font>** Paul Julius Kühn, Mika Pommeranz, Arjan Kuijper 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The bottleneck in learning-based industrial defect detection is often limited not by model capacity, but by the scarcity of labeled defect data: defects are rare, annotations are expensive, and collecting balanced training sets is slow. We present an end-to-end pipeline for synthetic defect generation and annotation, combining Vision-Language-Model-based prompts, LoRA-adapted diffusion, mask-guided inpainting, and sample filtering with automatic label derivation, and demonstrates the potential of real data with realistic synthetic samples to overcome data scarcity. The evaluation is conducted on, a challenging dataset of pitting defects on ball screw drives, and then on a subset of the Mobile phone screen surface defect segmentation dataset (MSD) dataset to test cross-domain transfer. Beyond downstream detector performance, we analyze key stages of the pipeline, including prompt construction, LoRA selection, and sample filtering with DreamSim and CLIPScore, to understand which synthetic samples are both realistic and useful. Experiments with YOLOv26, YOLOX, and LW-DETR show that synthetic-only training does not replace real data. When combined with real data, synthetic defects can preserve performance and yield modest gains in selected BSData training regimes. The MSD transfer study shows that the overall pipeline structure carries over to a second industrial inspection domain, while also highlighting the importance of domain-specific adaptation and annotation-quality control. Overall, the paper provides an end-to-end assessment of diffusion-based industrial defect synthesis and shows that its strongest value lies in strengthening scarce real datasets rather than substituting for them.

---


### 134. [Electricity price forecasting across Norway's five bidding zones in the post-crisis era](https://arxiv.org/abs/2604.26634)

**<font color=#1a73e8>作者：</font>** My Thi Diem Phan, Trung Tuyen Truong, Hoai Phuong Ha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Norway's electricity market is heavily dominated by hydropower, but the 2021--2022 energy crisis and stronger integration with Continental Europe have fundamentally altered price formation, reducing the reliability of forecasting models calibrated on historical data. Despite the critical need for updated models, a unified benchmark evaluating feature contributions across all structurally diverse Norwegian bidding zones remains lacking. Here we present a comprehensive evaluation of electricity price forecasting across all five Norwegian Nord Pool bidding zones. We constructed a multimodal hourly dataset spanning 2019--2025 and evaluated eight forecasting model families including LightGBM, ARX, and advanced deep learning architectures using a strictly causal test set. We implemented robust rolling-origin backtesting, leave-one-group-out feature ablation, and conditional regime analysis to dissect model performance and feature utility. Our results show that LightGBM achieves the best performance in every zone with MAE ranging from 1.64 to 5.74~EUR/MWh, while the ridge ARX model remains a highly competitive linear benchmark in northern zones. Feature ablation reveals that models relying solely on lagged prices and calendar variables achieve high accuracy and often match or exceed full multimodal integration. However, conditional regime analysis demonstrates that external features like reservoir levels and gas prices remain crucial to stratify forecast errors, which consistently increase under stressed market regimes. This highlights the practical value of model interpretability and regime awareness for decision makers facing structural changes in market dynamics.

---


### 135. [When to Vote, When to Rewrite: Disagreement-Guided Strategy Routing for Test-Time Scaling](https://arxiv.org/abs/2604.26644)

**<font color=#1a73e8>作者：</font>** Zhimin Lin, Yixin Ji, Jinpeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve strong performance on mathematical reasoning tasks but remain unreliable on challenging instances. Existing test-time scaling methods, such as repeated sampling, self-correction, and tree search, improve performance at the cost of increased computation, yet often exhibit diminishing returns on hard problems. We observe that output disagreement is strongly correlated with instance difficulty and prediction correctness, providing a useful signal for guiding instance-level strategy selection at test time. Based on this insight, we propose a training-free framework that formulates test-time scaling as an instance-level routing problem, rather than allocating more computation within a single strategy, dynamically selecting among different scaling strategies based on output disagreement. The framework applies lightweight resolution for consistent cases, majority voting for moderate disagreement, and rewriting-based reformulation for highly ambiguous instances. Experiments on seven mathematical benchmarks and three models show that our method improves accuracy by 3% - 7% while reducing sampling cost compared to existing approaches.

---


### 136. [Differentially-Private Text Rewriting reshapes Linguistic Style](https://arxiv.org/abs/2604.26656)

**<font color=#1a73e8>作者：</font>** Stefan Arnold  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Differential Privacy (DP) for text matured from disjointed word-level substitutions to contiguous sentence-level rewriting by leveraging the generative capacity of language models. While this form of text privatization is best suited for balancing formal privacy guarantees with grammatical coherence, its impact on the register identity of text remains largely unexplored. By conducting a multidimensional stylistic profiling of differentially-private rewriting, we demonstrate that the cost of privacy extends far beyond lexical variation. Specifically, we find that rewriting under privacy constraints induces a systematic functional mutation of the text's communicative signature. This shift is characterized by the severe attrition of interactive markers, contextual references, and complex subordination. By comparing autoregressive paraphrasing against bidirectional substitution across a spectrum of privacy budgets, we observe that both architectures force convergence toward a non-involved and non-persuasive register. This register-blind sanitization effectively preserves semantic content but structurally homogenizes the nuanced stylistic markers that define human-authored discourse.

---


### 137. [From Black-Box Confidence to Measurable Trust in Clinical AI: A Framework for Evidence, Supervision, and Staged Autonomy](https://arxiv.org/abs/2604.26671)

**<font color=#1a73e8>作者：</font>** Serhii Zabolotnii, Viktoriia Holinko, Olha Antonenko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Trust in clinical artificial intelligence (AI) cannot be reduced to model accuracy, fluency of generation, or overall positive user impression. In medicine, trust must be engineered as a measurable system property grounded in evidence, supervision, and operational boundaries of AI autonomy. This article proposes a practical framework for trustworthy clinical AI built around three principles: evidence, supervision, and staged autonomy. Rather than replacing deterministic clinical logic wholesale with end-to-end black-box models, the proposed approach combines a deterministic core, a patient-specific AI assistant for contextual validation, a multi-tier model escalation mechanism, and a human supervision layer for verification, escalation, and risk control. We demonstrate that trust also depends on selective verification of clinically critical findings, bounded clinical context, disciplined prompt architecture, and careful evaluation on realistic cases. Classifier-driven modular prompting is examined as an incremental path to scaling clinical depth without sacrificing prompt performance and without waiting for complete rule-based coverage. To operationalize trust, a set of trust metrics is proposed, built on metrological principles -- measurement uncertainty, calibration, traceability -- enabling quantitative rather than subjective assessment of each architectural layer. In this perspective, trustworthy clinical AI emerges not as a property of an individual model, but as an architectural outcome of a system into which evidence trails, human oversight, tiered escalation, and graduated action rights are embedded from the outset.

---


### 138. [Hearing the Room Through the Shape of the Drum: Modal-Guided Sound Recovery from Multi-Point Surface Vibrations](https://arxiv.org/abs/2604.26678)

**<font color=#1a73e8>作者：</font>** Shai Bagon, Matan Kichler, Mark Sheinin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical vibration sensing enables recovering the scene sound directly from the surface vibration of nearby objects, turning everyday objects into ``visual microphones''. However, most prior methods had focused on capturing the vibrations of specific objects with highly favorable vibration responses. These include objects where the surface vibrations are generated by the object itself (e.g., speaker membrane or guitar body) or objects consisting of a thin membrane which is highly reactive to sound (e.g., a chip bag or the leaf of a plant). In this paper, we tackle sound recovery for a more challenging class of solid objects whose vibration responses are poor or highly resonant. We simultaneously capture vibrations for multiple surface points on the object using a speckle-based vibrometry imaging system. Then, we derive a novel physics-guided vibration formation model that relates the scene sound source to the captured multi-point multi-axis vibrations via the object's vibrational modes. The model is then used to reverse the resonant transfer function of the vibrating object, fusing multiple vibration signals to estimate the original sound source in the scene. We evaluate our approach by recovering sound from a variety of everyday objects, demonstrating that it significantly outperforms traditional single-point speckle vibrometry in challenging scenarios and other signal-processing-based methods for multi-signal fusing.

---


### 139. [CurEvo: Curriculum-Guided Self-Evolution for Video Understanding](https://arxiv.org/abs/2604.26707)

**<font color=#1a73e8>作者：</font>** Guiyi Zeng, Junqing Yu, Yi-Ping Phoebe Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in self-evolution video understanding frameworks have demonstrated the potential of autonomous learning without human annotations. However, existing methods often suffer from weakly controlled optimization and uncontrolled difficulty progression, as they lack structured guidance throughout the iterative learning process. To address these limitations, we propose CurEvo, a curriculum-guided self-evolution framework that introduces curriculum learning into self-evolution to achieve more structured and progressive model improvement. CurEvo dynamically regulates task difficulty, refines evaluation criteria, and balances data diversity according to model competence, forming a curriculum-guided feedback loop that aligns learning complexity with model capability. Built upon this principle, we develop a multi-dimensional adaptive QA framework that jointly evolves question generation and answer evaluation across perception, recognition, and understanding dimensions, ensuring coherent and measurable curriculum progression. Through this integration, CurEvo transforms weakly controlled self-evolution into a more structured learning process for autonomous video understanding. Across seven backbones, CurEvo consistently improves both benchmark accuracy and evaluator-based semantic score on four VideoQA benchmarks, validating the effectiveness of curriculum-guided self-evolution for video understanding.

---


### 140. [Swap distance minimization shapes the order of subject, object and verb in languages of the world](https://arxiv.org/abs/2604.26726)

**<font color=#1a73e8>作者：</font>** Jairo Rios-El-Yazidi, Ramon Ferrer-i-Cancho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Languages of the world vary concerning the order of subject, object and verb. The most frequent dominant orders are SOV and SVO, and researchers have tailored models to this fact. However, there are still languages whose dominant order does not conform to these expectations or even lack a dominant order. Here we show that across linguistic families and macroareas, word order variation within languages is shaped by the principle of swap distance minimization even when the dominant order is not SOV/SVO and even when a dominant order is lacking.

---


### 141. [Catching the Fly: Practical Challenges in Making Blockchain FlyClient Real](https://arxiv.org/abs/2604.26736)

**<font color=#1a73e8>作者：</font>** Pericle Perazzo, Dario Capecchi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> FlyClient is a lightweight blockchain verification protocol that enables proof-of-work validation using minimal data, making it ideal for resource-constrained environments like mobile wallets, Internet-of-Things devices or cross-chain bridges implemented with smart contracts. Despite its strong potential for enabling lightweight blockchain verification, FlyClient protocol is still in the experimental stages, with limited real-world deployments and performance evaluations under diverse conditions. In this paper we bridge the gap between theory and deployment, by addressing several technical challenges to advance FlyClient to a production-ready solution. Namely, our contribution is three-fold: (i) we formally introduce an adversary model alternative to the original FlyClient one, that allows us to parametrize a verifier under a concrete economic interpretation, while also saving some proof space; (ii) we provide the first practical FlyClient prover implementation for a production blockchain (Zcash), and we estimate its performance under different configurations; (iii) we introduce and evaluate two optimizations that minimize the size of FlyClient proofs, the first of which does not require any consensus change.

---


### 142. [Learning Sparse BRDF Measurement Samples from Image](https://arxiv.org/abs/2604.26740)

**<font color=#1a73e8>作者：</font>** Wen Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate BRDF acquisition is important for realistic rendering, but dense gonioreflectometer measurements are slow and expensive. We study how to select a small number of BRDF measurements that are most useful for reconstructing material appearance under a learned reflectance prior. Our method combines a set encoder for sparse coordinate-value observations, a pretrained hypernetwork-based BRDF reconstructor, and a differentiable renderer. During sampler training, the reconstructor is kept fixed and gradients from BRDF-space and rendered-image losses are used to optimize measurement locations. This separates sample selection from prior fitting and encourages the sampler to choose directions that are informative under the learned material distribution. Experiments on the MERL dataset show that the proposed sampler improves low-budget reconstruction quality at 8 and 16 measurements compared with neural reconstruction baselines, while PCA-based methods remain strong at larger budgets. We further analyze the effect of image-space supervision, co-optimization, and image-only latent fitting for unseen materials.

---


### 143. [Exploring the Potential of Probabilistic Transformer for Time Series Modeling: A Report on the ST-PT Framework](https://arxiv.org/abs/2604.26762)

**<font color=#1a73e8>作者：</font>** Zhangzhi Xiong, Haoyi Wu, You Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Probabilistic Transformer (PT) establishes that the Transformer's self-attention plus its feed-forward block is mathematically equivalent to Mean-Field Variational Inference (MFVI) on a Conditional Random Field (CRF). Under this equivalence the Transformer ceases to be a black-box neural network and becomes a programmable factor graph: graph topology, factor potentials, and the message-passing schedule are all explicit and inspectable primitives that can be engineered. PT was originally developed for natural language and in this report we investigate its potential for time series. We first lift PT into the Spatial-Temporal Probabilistic Transformer (ST-PT) to repair PT's missing channel axis and weak per-step semantics, and adopt ST-PT as a shared cornerstone backbone. We then identify three distinct properties that PT/ST-PT offers as a factor-graph model and derive three Research Questions, one per property, that probe how each property can be exploited in time series: RQ1. The graph topology and potentials are direct programmable primitives. Can this be used to inject symbolic time-series priors into ST-PT through structural graph modifications, especially under data scarcity and noise? RQ2. The CRF's factor matrices are the operator's potentials. Can an external condition program these factor matrices on a per-sample basis, so that conditional generation becomes structural rather than feature-level modulation of a fixed one? RQ3. Each MFVI iteration is a Bayesian posterior update on the factor graph. Can this turn the latent transition of latent-space AutoRegressive (AR) forecasting from an opaque MLP into a principled posterior update, and can a CRF teacher distill its latents into the AR student to counter cumulative error? We give one empirical study per question. Together, these three studies position ST-PT as a programmable framework for time-series modeling.

---


### 144. [MemOVCD: Training-Free Open-Vocabulary Change Detection via Cross-Temporal Memory Reasoning and Global-Local Adaptive Rectification](https://arxiv.org/abs/2604.26774)

**<font color=#1a73e8>作者：</font>** Zuzheng Kuang, Honghao Chang, Boqiang Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary change detection aims to identify semantic changes in bi-temporal remote sensing images without predefined categories. Recent methods combine foundation models such as SAM, DINO and CLIP, but typically process each timestamp independently or interact only at the final comparison stage. Such paradigms suffer from insufficient temporal coupling during semantic reasoning, which limits their ability to distinguish genuine semantic changes from non-semantic appearance discrepancies. In addition, patch-dominant inference on high-resolution images often weakens global semantic continuity and produces fragmented change regions. To address these issues, we propose MemOVCD, a training-free open-vocabulary change detection framework based on cross-temporal memory reasoning and global-local adaptive rectification. Specifically, we reformulate bi-temporal change detection as a two-frame tracking problem and introduce weighted bidirectional propagation to aggregate semantic evidence from both temporal directions. To stabilize memory propagation across large temporal gaps, we construct histogram-aligned transition frames to smooth abrupt appearance changes. Moreover, a global-local adaptive rectification strategy adaptively fuses local and global-view predictions, improving spatial consistency while preserving fine-grained details. Experiments on five benchmarks demonstrate that MemOVCD achieves favorable performance on two change detection tasks, validating its effectiveness and generalization under diverse open-vocabulary settings.

---


### 145. [Virtual-reality based patient-specific simulation of spine surgical procedures: A fast, highly automated and high-fidelity system for surgical education and planning](https://arxiv.org/abs/2604.26781)

**<font color=#1a73e8>作者：</font>** Raj Kumar Ranabhat, Tayler D Ross, Tony Jiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical training involves didactic teaching, mentor-led learning, surgical skills laboratories, and direct exposure to surgery; however, increasing clinical pressures have limited operating room (OR) exposure. This work leverages virtual reality (VR) to provide a safe and immersive training environment. Existing VR training is often based on standardized scenarios not tailored to individual clinical cases. This study addresses this limitation using artificial intelligence (AI) based computer vision methods to generate patient-specific simulations from computed tomography (CT) and magnetic resonance imaging (MRI). This study focuses on patient-specific spinal decompression simulation for spinal stenosis in a virtual operating room. The objectives were (1) automatic creation of 3D anatomical models and (2) VR simulation of spinal decompression procedures including laminectomy, disc resection, and foraminotomy. Model construction required multimodal fusion (registration) of CT and MRI and segmentation of relevant structures. Segmentation was evaluated using the Dice Similarity Coefficient (DSC), and registration accuracy using Target Registration Error (TRE). Qualitative feedback was obtained from surgeons and trainees. High-fidelity patient-specific 3D models were generated efficiently (approximately 2.5 minutes per case, N = 15). Segmentation accuracy was high, with a DSC of 0.95 (+/- 0.03) for vertebral bone and 0.895 (+/- 0.02) for soft tissue structures. Registration accuracy showed a mean TRE of 1.73 (+/- 0.42) mm. Semi-structured interviews indicated improved spatial understanding, increased procedural confidence, and strong perceived educational value. This platform significantly reduced the time and costs of patient-specific modelling, thereby facilitating pre-operative planning, post-procedural assessments, and comprehensive surgical simulation.

---


### 146. [Hankel and Toeplitz Rank-1 Decomposition of Arbitrary Matrices with Applications to Signal Direction-of-Arrival Estimation](https://arxiv.org/abs/2604.26787)

**<font color=#1a73e8>作者：</font>** Georgios I. Orfanidis, Dimitris A. Pados, George Sklivanitis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problems of computing the optimal rank-$1$ Hankel and Toeplitz-structured approximation of arbitrary matrices under $L_2$ and $L_1$-norm error. Such problems arise naturally in engineered systems, including the basic few-shot signal Direction-of-Arrival (DoA) estimation problem that is of importance to modern autonomous systems applications. We develop accurate and computationally efficient structured matrix decomposition algorithms for both formulations and then derive analytically grounded small-sample-support DoA estimators for practical sensing system deployments. The resulting estimators under the $L_2$ and $L_1$ norms are formally shown to be maximum-likelihood optimal under white Gaussian and Laplace noise, respectively. The estimators are further validated through extensive simulation studies and real-world data experiments in few-shot DoA inference.

---


### 147. [Super-resolution Multi-signal Direction-of-Arrival Estimation by Hankel-structured Sensing and Decomposition](https://arxiv.org/abs/2604.26793)

**<font color=#1a73e8>作者：</font>** Georgios I. Orfanidis, Dimitris A. Pados, George Sklivanitis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by sensing modalities in modern autonomous systems that involve hardware-constrained spatial sampling over large arrays with limited coherence time, we develop a novel framework for rapid super-resolution multi-signal direction-of-arrival (DoA) estimation based on Hankel-structured sensing and data matrix decomposition of arbitrary rank, under both the $L_2$ and $L_1$-norm formulation. The resulting $L_2$-norm estimator is shown to be maximum-likelihood optimal in white Gaussian noise. The $L_1$-norm estimator is shown to be maximum-likelihood optimal in independent, identically distributed (i.i.d.) isotropic Laplace noise, offering broad robustness to impulsive interference and corrupted measurements commonly encountered in practice. Extensive simulations demonstrate that the proposed methods exhibit powerful super-resolution capabilities, requiring significantly lower SNR and achieving substantially higher resolution probability than recent competing approaches.

---


### 148. [ViCrop-Det: Spatial Attention Entropy Guided Cropping for Training-Free Small-Object Detection](https://arxiv.org/abs/2604.26806)

**<font color=#1a73e8>作者：</font>** Hui Wang, Hongze Li, Wei Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based architectures have established a dominant paradigm in global semantic perception; however, they remain fundamentally constrained by the profound spatial heterogeneity inherent in natural images. Specifically, the imposition of a uniform global receptive field across regions of varying information density inevitably leads to local feature degradation, particularly in dense conflict zones populated by microscopic targets. To address this mechanistic limitation, we propose ViCrop-Det, a training-free inference framework that introduces adaptive spatial trust region shrinkage. Inspired by the use of attention entropy in anomaly segmentation, ViCrop-Det leverages the detection decoder's cross-attention distribution as an endogenous probe. By utilizing Spatial Attention Entropy (SAE) to heuristically evaluate local spatial ambiguity, the framework executes dynamic spatial routing, allocating a fixed computational budget exclusively to regions exhibiting both high target saliency and high cognitive uncertainty. By shrinking the spatial trust region and injecting high-frequency localized observations, ViCrop-Det actively resolves spatial ambiguity and recovers fine-grained features without requiring architectural modifications. Extensive evaluations on VisDrone and DOTA-v1.5 demonstrate that ViCrop-Det yields competitive performance enhancements, consistently adding +1-3 mAP@50 to RT-DETR-R50 and Deformable DETR with a marginal 20-23\% latency overhead. On MS COCO, $AP_{S}$ improves while $AP_{M}/AP_{L}$ remains stable, indicating precise fine-scale refinement without compromising the global spatial prior. Under compute-matched settings, our adaptive routing strategy comprehensively surpasses uniform slicing baselines, achieving a highly optimized accuracy-speed trade-off.

---


### 149. [A Multi-Dataset Benchmark of Multiple Instance Learning for 3D Neuroimage Classification](https://arxiv.org/abs/2604.26807)

**<font color=#1a73e8>作者：</font>** Ethan Harvey, Dennis Johan Loevlie, Amir Ali Satani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite being resource-intensive to train, 3D convolutional neural networks (CNNs) have been the standard approach to classify CT and MRI scans. Recent work suggests that deep multiple instance learning (MIL) may be a more efficient alternative for 3D brain scans, especially when the pre-trained image encoder used to embed each 2D slice is frozen and only the pooling operation and classifier are trained. In this paper, we provide a systematic comparison of simple MIL, attention-based MIL, 3D CNNs, and 3D ViTs across three CT and four MRI datasets, including two large datasets of at least 10,000 scans. Our goal is to help resource-constrained practitioners understand which neural networks work well for 3D neuroimages and why. We further compare design choices for attention-based MIL, including different encoders, pooling operations, and architectural orderings. We find that simple mean pooling MIL, without any learnable attention, matches or outperforms recent MIL or 3D CNN alternatives on 4 of 6 moderate-sized tasks. This baseline remains competitive on two large datasets while being 25x faster to train. To explain mean pooling's success, we examine per-slice attention quality and a semi-synthetic dataset where we can derive the best possible classifier via a Bayes estimator. This analysis reveals the limits of existing MIL approaches and suggests routes for future improvements.

---


### 150. [Asynchronous Federated Unlearning with Invariance Calibration for Medical Imaging](https://arxiv.org/abs/2604.26809)

**<font color=#1a73e8>作者：</font>** Zhaoyuan Cai, Xinglin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Unlearning (FU) is an emerging paradigm in Federated Learning (FL) that enables participating clients to fully remove their contributions from a trained global model, driven by data protection regulations that mandate the right to be forgotten. However, existing FU methods mostly rely on synchronous coordination. This requirement forces the entire federation to halt and wait for stragglers to complete erasure, creating significant delays due to device heterogeneity. Furthermore, these methods often face the problem that the influence of erased data is merely suppressed temporarily and resurfaces during subsequent training, rather than being genuinely removed. To overcome these limitations, this paper proposes Asynchronous Federated Unlearning with Invariance Calibration (AFU-IC), a novel framework for medical imaging that decouples the erasure process from the global training workflow. This enables the target client to perform unlearning asynchronously without interrupting global training. Meanwhile, a server-side invariance calibration mechanism prevents the model from relearning the erased data. Extensive experiments on three medical benchmarks demonstrate that AFU-IC achieves unlearning efficacy and model fidelity comparable to gold-standard retraining while significantly reducing wall-clock latency compared to synchronous baselines. AFU-IC ensures efficient, compliant and reliable FL in cross-silo medical environments.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-173](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*

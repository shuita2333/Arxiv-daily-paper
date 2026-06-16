# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

---

### 201. [Parameter-Efficient Adaptation of SAM 3 for Automated ITV Generation from 4DCT Images](https://arxiv.org/abs/2606.15604)

**<font color=#1a73e8>作者：</font>** Changwoo Song  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Four-dimensional computed tomography (4DCT) captures the full respiratory cycle of thoracic anatomy, yet current Internal Target Volume contouring workflows process each phase in isolation, discarding temporal coherence and leaving contours vulnerable to phase-specific artifacts. We present a lightweight framework that applies parameter-efficient fine-tuning to the Segment Anything Model 3 (SAM 3) via low-rank adaptation (LoRA) to align its text-prompted segmentation with the medical domain using only seven annotated 3D CT volumes. Furthermore, the framework incorporates a hard negative mining strategy to improve boundary discrimination in low-contrast thoracic regions. At inference, phase-wise predictions are refined through phase-coherent temporal filtering and spatial connectivity analysis. Since respiratory motion is continuous and periodic, genuine anatomy appears in contiguous blocks of phases, whereas transient artifacts appear sporadically and are thus effectively suppressed. Experiments on pulmonary and cardiac structures yield median Dice scores of 0.968 and 0.910 with 95th-percentile Hausdorff distances of 0.998 mm and 2.931 mm, respectively. The proposed framework effectively eliminates the severe false-positive predictions inherent in the zero-shot inference of the unadapted SAM 3. With only seven annotated volumes, the framework retains over 95% of full-data accuracy, and the entire pipeline is trainable on a single consumer-grade GPU, demonstrating a scalable, data-efficient solution for adaptive radiotherapy.

---


### 202. [Variational Test-time Optimization for Diffusion Synchronization](https://arxiv.org/abs/2606.15614)

**<font color=#1a73e8>作者：</font>** Hyunsoo Lee, Farrin Marouf Sofian, Kushagra Pandey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative generation, which coordinates multiple diffusion trajectories to extend the capabilities of pretrained priors, has emerged as a powerful paradigm for extending the applicability of diffusion models. Among existing approaches, diffusion synchronization provides a scenario-agnostic solution by introducing general guidance mechanisms. However, current synchronization approaches rely heavily on heuristics and still require task-specific tailoring, which limits their generalizability and performance. In this work, we mathematically derive a synchronization framework based on optimal control, providing a principled explanation of diffusion synchronization. During sampling, we optimize control variables to guide multiple trajectories toward coherent solutions while remaining close to the underlying diffusion prior. Our method operates entirely at test-time without additional training, thereby enabling broad applicability across diverse generation scenarios when combined with strong pretrained priors. We demonstrate consistent improvements over baselines on three representative collaborative generation tasks, covering a wide range of modalities and applications. Beyond performance gains, our work establishes a novel foundation for collaborative generation, opening a principled path toward extending pretrained generative models to new collaborative generation settings.

---


### 203. [NeRD: Neuro-Symbolic Rule Distillation for Efficient Ontology-Grounded Chain-of-Thought in Medical Image Diagnosis](https://arxiv.org/abs/2606.15617)

**<font color=#1a73e8>作者：</font>** Hongxi Yang, Yiwen Jiang, Siyuan Yan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpretability is essential for trustworthy medical image diagnosis. However, existing concept-driven interpretable methods have key limitations: Concept Bottleneck Models (CBMs) require scoring all predefined concepts at inference time and for manual intervention, imposing a substantial burden on clinicians, while rationale-based generative approaches often select concepts by class discriminability, which can drift from diagnostic ontologies. To address these issues, we propose Neuro-Symbolic Rule Distillation (NeRD), a framework that produces efficient, ontology-grounded reasoning chains that are sufficient yet non-redundant, without manually crafting diagnostic rules. Experiments on two skin datasets demonstrate strong diagnostic performance and interpretability, and blinded expert evaluation confirms the clinical plausibility of NeRD rationales. Our method further enables a first expert-in-the-loop study for Multimodal Chain-of-Thought-based diagnosis, achieving efficient and effective concept-level intervention.

---


### 204. [Re-feeding Is Not Replaying: Measuring Replay Noise in Counterfactual Token-Credit Estimation](https://arxiv.org/abs/2606.15621)

**<font color=#1a73e8>作者：</font>** Nils Matteson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Per-token counterfactual credit estimation asks which token in a language-model rollout caused the final answer to be right or wrong: cut the transcript at a pivot, substitute an alternative token, replay continuations, and compare outcomes. Published methods re-feed the transcript prefix as a fresh prompt, assuming this reproduces the state the model passed through during generation. We measure what that assumption costs on a stock inference engine, with a three-pass design: continuations resumed from the verified decode-time KV state, an identical second exact pass (a replica noise floor), and a re-feed pass. Across six configurations and three models (including a GRPO-trained checkpoint), at low-margin decision tokens, re-feeding changes the credit estimate at rates 14-28 percentage points above the replica floor (7-21pp under a treatment-independent conditioning; problem-clustered t = 2.9-6.4). Most changes are zero-boundary crossings of the quantized estimator rather than polarity reversals, and the perturbation is consistent with mean-zero, so averaged quantities are largely safe; but selection is not: a critical-token set chosen by thresholding $|\hat{A}_t|$ under re-feed overlaps the exact-resume selection at Jaccard 0.34-0.90, versus a 0.63-0.96 replica ceiling. A causal confirmation closes the loop: under vLLM's batch-invariant kernels all three passes are identical on every measured channel, with both disagreement rates exactly zero. Replica passes themselves disagree on 9-23% of eligible estimates: single-sample credit measurements at decision tokens are unreliable under any replay. Settings were fixed in advance; exact-pass cache hits in the second campaign are instrumented (100% hit rate, 3,434 pivots); total compute was under 10 USD. We recommend that counterfactual credit studies resume decoder state or use batch-invariant kernels, and report a replica floor.

---


### 205. [Surprise-Guided MergeSort: Budget-Efficient Human-in-the-Loop Ranking via Adaptive Comparison Scheduling](https://arxiv.org/abs/2606.15623)

**<font color=#1a73e8>作者：</font>** Yujin Park, Haejun Chung, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pairwise comparison is the gold standard for subjective ranking tasks; however, exhaustive annotation requires a massive number of human comparisons ($O(n^2)$). While sorting-based methods have reduced this burden to $O(n\log n)$, they still require expensive human judgment for every single comparison. To further improve annotation efficiency, we propose leveraging a Vision-Language Model (VLM) not as an annotator replacement, but as a \emph{question prioritizer} to identify which comparisons genuinely require human judgment. The proposed \textbf{Surprise-Guided MergeSort (SGS)} framework achieves this through three integrated components: (1) a bottom-up MergeSort scheduler that structures comparisons and exploits transitivity, (2) a composite Surprise Scorer -- combining position-bias-cancelled VLM confidence, Elo gap, and vote entropy -- to quantify comparison ambiguity, and (3) an adaptive budget allocator that routes high-surprise pairs to humans while automating low-surprise pairs via transitivity inference. Validation was conducted on six diverse benchmarks spanning text similarity (STS-B, BIOSSES, SICKR-STS) and image quality assessment (KonIQ-10k, TID2013, LIVE Challenge). SGS effectively identified and skipped up to 535 non-informative comparisons per session. Consequently, it achieved Kendall's $\tau{\times}100$ improvements of $+6$ to $+12$ over Active Elo under the same total budget. These results demonstrate that combining VLM-guided surprise metrics with algorithmic sorting provides a generally consistent accuracy-efficiency trade-off across diverse domains.

---


### 206. [XPASS-Vis: A Dataset for Cross-Domain Personalized Image Aesthetic Assessment](https://arxiv.org/abs/2606.15629)

**<font color=#1a73e8>作者：</font>** Takato Hayashi, Hiroaki Takahara, Candy Olivia Mawalim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized image aesthetic assessment (PIAA) seeks to model, at the individual level, the subjective nature of aesthetic judgments toward artworks and photographs. Aesthetic preference is known to be both deeply personal and partially consistent across visual domains. Yet existing PIAA datasets and methods are largely confined to a single domain, or provide too few samples per annotator within each domain to enable personalization across domains. Consequently, the cross-domain generalization of personalized aesthetic preferences remains largely unexplored. To address this gap, we introduce XPASS-Vis, the first dataset explicitly designed for cross-domain PIAA. XPASS-Vis comprises 6,526 stimuli from three visual domains -- art, fashion, and landscape -- rated by 129 annotators, yielding 87,836 user-stimulus interactions, each annotated with an overall aesthetic score and nine aesthetic-emotion ratings. Notably, each annotator rated more than 200 stimuli per domain, providing sufficient per-domain coverage to support personalization both within and across domains. Moreover, we establish baseline models for cross-domain PIAA under unsupervised domain adaptation (UDA), where a model trained on a labeled source domain is transferred to an unlabeled target domain. A systematic evaluation of representative UDA approaches shows that the best-performing method recovers approximately 60\% (Spearman's $\rho$ = .28) of the supervised upper bound under a fully unsupervised setting. This provides encouraging evidence that personalized aesthetic preferences are, to a meaningful extent, transferable across visual domains. At the same time, a substantial gap remains, highlighting the need for PIAA-specific adaptation strategies. XPASS-Vis and the accompanying baselines provide a foundation for future research on cross-domain PIAA. All datasets and code will be made publicly available upon acceptance.

---


### 207. [Open-World Video Segmentation](https://arxiv.org/abs/2606.15632)

**<font color=#1a73e8>作者：</font>** Qing Su, Kaiyang Li, Yuan Zhuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While video segmentation has advanced rapidly on short clips and closed-set benchmarks, open-world video segmentation remains largely unexplored. The challenge is twofold: (1) existing methods are not designed to support object discovery and identity maintenance in long videos of dynamic ego-motion, and (2) existing evaluation protocols rely on a rigid 1:1 matching that unfairly penalizes semantically valid predictions with mismatched granularity. To address both gaps, we introduce Savvy, a practical and strong system for zero-shot open-world long-horizon video segmentation. Savvy combines hierarchical mask discovery, deferred admission, and track consolidation to support persistent object discovery, safe track promotion, and stable long-range identity maintenance. We further propose OGA, a granularity-aware evaluation suite for open-world video segmentation. Built on a Granularity-Agnostic (GA) matching protocol, OGA relaxes conventional 1:1 matching to an n:1 mapping, but still enforces temporal rigor by detecting support discontinuities through sever points and scoring each reference object through its dominant coherent fragment. This prevents fragmented or flickering support from being over-rewarded while enabling GA-adapted metrics and structural diagnostics: identity persistence (IP), and identity concentration (IC). On VIPSeg, we show that standard 1:1 evaluation substantially underestimates open-world methods, whereas GA evaluation recovers much of their suppressed performance. On the more realistic long-horizon benchmarks: ScanNet and HM3D, Savvy consistently outperforms strong baselines across both classical and proposed metrics, including STQ, VPQ$_\infty$, IP and IC. Together, these results establish a practical benchmark and a strong baseline for open-world long-horizon video segmentation.

---


### 208. [HAPI-EP: Towards Hybrid, Adaptive, and Predictive Digital Twins of Cardiac Electrophysiology](https://arxiv.org/abs/2606.15637)

**<font color=#1a73e8>作者：</font>** Sumeet Vadhavkar, Xiajun Jiang, Yubo Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A digital twin (DT) of a patient-specific heart offers significant potential in personalized medicine. However, its rapid and dynamic adaptation to an individual's live data and its predictive capability after adaptation remains central challenges. We examine this challenge from its two building blocks: DT formulation where mechanistic and data-driven models show competing merits and limitations, and DT optimization strategies that are largely driven by a reconstruction objective leading to un-identifiable models. We address both bottlenecks via HAPI -- an AI framework for building hybrid, adaptive, and predictive DTs with three key enablers. First, HAPI constructs a physics-integrated gray-box model in which an interpretable mechanistic backbone is augmented by a neural component that models its residual to the observed data. Second, rather than attempting to pre-encode all possible variations in a static hybrid model, HAPI enables rapid on-the-fly adaptation of the hybrid model to few-shot live data, achieved by feedforward meta-learners realizing amortized inference of both mechanistic and neural parameters of the hybrid model trained with predictive objectives. Finally, we show that this adaptivity corresponds to the construction of a conditional generative model (i.e., the hybrid DT) that endows it with theoretical identifiability and thus strong performance in predictive scenarios. We demonstrate the proof-of-concept of HAPI in cardiac electrophysiology using a hybrid monodomain model with mechanistic reaction kinetics and neural graph diffusion. Across synthetic and real-data studies, we show that HAPI's mechanistic-neural hybridization and predictive adaptation are critical for obtaining identifiable DTs with strong predictive and out-of-distribution capabilities.

---


### 209. [Multi-Agent Framework for Audit Risk Assessment with Explicit Uncertainty and Evidence Conflict Modeling](https://arxiv.org/abs/2606.15640)

**<font color=#1a73e8>作者：</font>** Yuhan Wang, Manqing Wang, Yixuan Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Audit risk assessment increasingly benefits from combining heterogeneous evidence sources, yet existing approaches typically produce point predictions without quantifying how well different evidence streams agree. We propose UMAR (Uncertainty-Aware Multi-Agent Risk Assessment), a framework that employs three specialized agents: an MD&A Text Agent, a Financial Ratio Agent, and a CAM Agent, each producing independent risk scores with calibrated uncertainty estimates. An Uncertainty Aggregator based on Dempster-Shafer evidence theory fuses these scores while explicitly measuring inter-agent conflict. We evaluate UMAR on a U.S. dataset of 3,200 firm-year observations from SEC 10-K filings (2019-2023), with financial restatement as the target label. Experimental results show that UMAR achieves an AUROC of 0.782 and a PR-AUC of 0.341, outperforming logistic regression, XGBoost, FinBERT, and single-agent and dual-agent LLM baselines. UMAR attains the lowest expected calibration error (ECE = 0.052) among all methods and identifies evidence-conflict patterns that correlate with actual restatement risk, offering auditors potentially actionable and interpretable risk signals.

---


### 210. [CIWI-CKT: Chaos-Informed Wave Interference Feature Fusion and Cross-City Knowledge Transfer for Traffic Flow Forecasting](https://arxiv.org/abs/2606.15642)

**<font color=#1a73e8>作者：</font>** Abdul Joseph Fofanah, Lian Wen, David Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate traffic flow prediction remains challenging in cross-city, data-scarce scenarios where limited historical data hinders model generalisation. The chaotic nature of traffic dynamics, complex spatio-temporal dependencies, and heterogeneous urban networks complicate few-shot learning across cities. Existing deep learning approaches either treat traffic as purely deterministic or lack mechanisms to model wave-like interference patterns essential for cross-regime traffic dynamics. To address these limitations, this paper proposes CIWI-CKT, a novel Chaos-Informed Wave Interference Feature Fusion framework with Cross-City Knowledge Transfer. Our framework introduces three core innovations: chaos-informed wave generation that extracts measurable chaos invariants and models traffic as adaptive wave components; meta-interference processing that captures wave interactions between support and query regimes while producing a predictability score for confidence estimation; and chaos-aware meta-learning that enables efficient cross-city knowledge transfer while preserving chaotic characteristics. We establish theoretical guarantees including chaos-to-wave stability, wave-induced dimension reduction, and meta-learning generalisation bounds. Extensive experiments on four real-world traffic datasets demonstrate that CIWI-CKT significantly outperforms state-of-the-art spatio-temporal graph learning, transfer learning, prompt-based, and few-shot methods, improving prediction accuracy while substantially reducing required training data.

---


### 211. [Extending Item Response Theory for Efficient and Meaningful Multilingual Evaluation](https://arxiv.org/abs/2606.15643)

**<font color=#1a73e8>作者：</font>** Gili Lior, Tzviel Frostig, Gabriel Stanovsky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual benchmarks are central to evaluating large language models (LLMs) across languages, but they suffer from three issues: exhaustive evaluation scales linearly with the number of languages, automatic translation introduces errors that are easily missed at scale, and some items conflate general and culture-specific knowledge. We address all three with a unified statistical framework, Multilingual-IRT, which extends Item Response Theory with per-language difficulty deviations, split discriminability separating content from language effects, and per-language ability residuals. Fitting Multilingual-IRT on 25 LLMs across 29 languages of MMLU-Pro-X, we show that its fitted parameters support three practical applications: predicting unobserved (item, LLM, language) instances with 11-16% lower binary cross-entropy than the strongest accuracy-based baseline, surfacing candidate translation errors distributed across all 28 non-English languages, whereas accuracy-based baselines concentrate detections in a few languages, and recovering culture-specific items that accuracy-based baselines miss.

---


### 212. [Towards Next-Generation Healthcare: A Survey of Medical Embodied AI for Perception, Decision-Making, and Action](https://arxiv.org/abs/2606.15647)

**<font color=#1a73e8>作者：</font>** Cheng Zhang, Qing Cai, Xingzheng Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models have demonstrated impressive performance in enhancing healthcare efficiency across a wide range of medical applications. Nevertheless, their limited ability to perceive, understand, and interact with the physical world significantly constrains their effectiveness in real-world clinical workflows, where safety-critical decision-making and physical execution are tightly coupled. Recently, embodied artificial intelligence (AI) has emerged as a promising physical-interactive paradigm for intelligent healthcare, enabling agents to operate in complex medical environments. As research in this area rapidly expands, understanding how intelligent agents function as integrated, end-to-end systems in clinical environments becomes increasingly critical. However, existing surveys on medical embodied AI largely emphasize individual aspects or functional components, lacking a unified system-level organization of the field. To support and consolidate recent advances, we systematically survey the core components of medical embodied AI, with a particular emphasis on the coordinated integration of perception, decision-making, and action. We further review representative medical applications and relevant datasets, and we analyze the major challenges encountered in real-world clinical practice. Finally, we discuss key directions for future research in this rapidly evolving field. The associated project can be found at this https URL.

---


### 213. [Fusing Transferred Priors and Physics-based Decomposition for Underwater Image Enhancement](https://arxiv.org/abs/2606.15648)

**<font color=#1a73e8>作者：</font>** Haochen Hu, Yanrui Bin, Zhengyan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The underwater images are captured within diverse water-medium conditions, leading to complex degradation, including color bias, low contrast, and blur effect. Recently, learning-based methods have demonstrated their potential for underwater image enhancement (UIE). However, most of the previous work focus on the training strategy or network design to make the enhanced result aligned well with the labels in datasets, ignoring that the labels are selected from the enhanced results of previous UIE methods and these pseudo-labels are noisy. Consequently, the performance of their models is not satisfactory to a certain extent. However, collecting the true labels of the underwater images is challenging. In this work, we propose a transfer learning-based UIE that does not require underwater images to have paired noisy or true labels for learning. Instead, the UIE task is first divided into global color correction, haze removal, and background noise suppression following the underwater physics. Then multiple types of prior from other vision tasks are leveraged as cross-domain supervision in each step. In this way, a novel UIE is available via transfer learning, and the physics-aligned UIE decomposition provides theoretical soundness. Qualitative and quantitative experiments demonstrate that our proposal based on physics and priors fusion achieves SOTA performance in the UIE task and effectively boosts downstream vision tasks, significantly outperforming benchmark methods. Project repo: this https URL.

---


### 214. [AnonShield: Scalable On-Premise Pseudonymization for CSIRT Vulnerability Data](https://arxiv.org/abs/2606.15650)

**<font color=#1a73e8>作者：</font>** Cristhian Kapelinski, Douglas Lautert, Beatriz Machado 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present AnonShield, a high-throughput, on-premise pseudonymization system that combines GPU-accelerated NER, streaming processing, caching, and schema-aware configuration. Evaluated on datasets up to 550 MB (70,951 records), AnonShield reduces processing time from over 92 hours to under 10 minutes (up to 738x speedup) while achieving up to 94.2% F1-score and 96.7% recall. Our results show that scalable pseudonymization of vulnerability data is feasible without sacrificing analytical utility, enabling compliant data sharing in operational CSIRT environments.

---


### 215. [Advanced Machine Learning and Deep Learning Techniques for Enhanced Cattle Identification and Detection: A Comprehensive Review](https://arxiv.org/abs/2606.15655)

**<font color=#1a73e8>作者：</font>** Fayazunnesa Chowdhury, Syed Md. Galib, Md Nasim Adnan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The need for effective cattle identification technology is now more acutely felt than ever in maintaining biosecurity, food safety, and supply chain efficacy in livestock management. This paper presents a systematic review of recent research in cattle identification using machine learning and deep learning techniques. The present systematic review measures the effectiveness of traditional and modern cattle identification techniques using studies from major academic databases, where articles were subjected to full-text review. Among these techniques, classical Machine Learning Techniques such as K-Nearest Neighbors and Support Vector Machines have demonstrated good results in cattle identification; however, Deep Learning Techniques, such as Convolutional Neural Networks, Residual Networks, and You Only Look Once, are better in cognition, detection, and identification tasks. Feature extraction relies on common techniques like Local Binary Pattern (LBP), Speeded-Up Robust Features (SURF), and Scale-Invariant Feature Transform (SIFT), while key features commonly used in these studies include muzzle prints and coat patterns. The review highlights key hurdles involving cattle identification, such as the limited number of publicly accessible datasets, issues with data quality susceptible to environmental changes and animal mobility, and high demand for real-time processing ability. The paper aims to inform researchers, policymakers, and stakeholders about implementing scalable, humane, and effective cattle identification systems to achieve sustainable livestock management.

---


### 216. [SpatialAvatar-0: High-Quality 4D Head Avatar with Multi-Stage Reconstruction](https://arxiv.org/abs/2606.15659)

**<font color=#1a73e8>作者：</font>** Yiran Wang, Zeyu Zhang, Yuanming Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality 4D head avatars from one or a few source portraits are central to telepresence, AR/VR, and digital-human interaction. 3D Gaussian Splatting (3DGS) has emerged as the dominant representation, with two complementary regimes (generalizable feed-forward predictors and per-subject refiners) maturing in parallel. However, existing feed-forward predictors are trained on a single dataset family with a hard-coded source count, inheriting the corresponding domain bias. Per-subject refiners require 300K--600K iterations and rely on adaptive densification that destroys upstream Gaussian layouts, preventing the two regimes from sharing a representation end-to-end. To bridge both regimes we propose SpatialAvatar-0 on a shared FLAME-mesh-bound Gaussian representation: a feed-forward generator with a parameter-free K-source mean-pool and a monocular-temporal to multi-view-spatial two-phase schedule that anchors against identity-prior collapse onto the smaller multi-view set. We further introduce a 10K-iter layout-preserving per-subject refinement loop that freezes the FLAME-binding and Gaussian count and replaces densification with a three-component anti-spike regularization. On VFHQ/HDTF cross-domain zero-shot we surpass the in-domain leader GAGAvatar by +1.5 dB PSNR despite never training on either test domain, and on the SplattingAvatar monocular benchmark we lead every reported metric, surpassing the 300K-iter GeoAvatar by +1.3 dB PSNR at up to 60x shorter per-subject schedule than common SOTA baselines. Website: this https URL.

---


### 217. [CEVAR: Centerline Embedding Extraction for Endovascular Aneurysm Repair](https://arxiv.org/abs/2606.15667)

**<font color=#1a73e8>作者：</font>** Roman Naeem, Timo Niiniskorpi, Charlotte Sandström 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term mortality rates after endovascular aneurysm repair (EVAR) remain elevated due to post-EVAR rupture caused by loss of seal in stent graft sealing zones. Structured CT review using centerline measurements improves detection, but current workflows require manual centerline editing and expert operators. We propose a transformer framework for automated, protocol-driven sealing zone assessment that combines 3D centerline tracking with embedding-based geometric prediction. Two state-of-the-art image-to-graph models are evaluated for aorto-iliac centerline extraction from follow-up CT and for measurement of stent position, vessel diameters, and seal lengths according to EVAR4C protocol. Across the full test set and a challenging no-contrast subset, the proposed fully automatic method outperforms the commercial semi-automatic workflow.

---


### 218. [Z-Plane Neural Networks: Bounded Geometric Activation Replaces ReLU and LayerNorm](https://arxiv.org/abs/2606.15669)

**<font color=#1a73e8>作者：</font>** Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep neural networks rely on Euclidean scalar activations (e.g., ReLU) and global normalization techniques (e.g., LayerNorm) to prevent gradient instability in deep architectures. However, these mechanisms inherently cause dead neurons, discard critical directional information, and destroy the orthogonality of feature representations. Inspired by the frequency-modulation transmission of biological axons, we propose the Z-Plane Neural Network, which maps hidden states into 2D phasor bundles on a hypersphere. We introduce a novel geometric activation function, Radial Bounding($\mathbf{x} / \max(1, \|\mathbf{x}\|_2)$), which limits the energy magnitude while preserving the phase (direction). We demonstrate mathematically that this isotropic activation maintains 1-Lipschitz continuity and prevents gradient vanishing by preserving tangential gradients. Empirically, a 100-layer Z-Plane Multi-Layer Perceptron (MLP)-entirely devoid of ReLU and LayerNorm-successfully converges on the MNIST dataset with 98.34% accuracy and absolute numerical stability, proving that bounded geometric activation alone is sufficient for stable deep learning.

---


### 219. [Where Did It Go Wrong? Process-Level Evaluation of Web Agents with Semantic State Tracking](https://arxiv.org/abs/2606.15673)

**<font color=#1a73e8>作者：</font>** Jiwan Chung, JiHyuk Byun, Vibhav Vineet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web agents act through long interaction sequences, yet existing benchmarks evaluate only terminal success, discarding all process information and offering little guidance on improvement. In this work, we conduct a process-level analysis of web agents. We introduce WebStep, a benchmark of 1,800 task instances with controlled difficulty and automatic semantic state tracking. Each website exposes a deterministic semantic MDP alongside the GUI: the agent operates on the interface, while the environment records high-level states and transitions in the background, enabling fine-grained analysis without manual annotation. Based on the semantic trajectory, we first show that process metrics reveal differences invisible to outcome evaluation: three agents whose success rates cluster within 31-33% diverge in exploration reach versus execution accuracy. Then, decomposing by skill characterizes the nature of these differences, exposing opposite per-skill rankings hidden within the same website: e.g., on Housing, OpenAI CUA outperforms Qwen3.5 by 23.7% on commit actions yet underperforms it by 15.6% on filtering, pinpointing a concrete skill to improve even within a domain. Bifurcation analysis further localizes the decisive error that loses the task and shows that this error is agent-specific rather than shared. Finally, these differences widen as tasks grow harder: success rate is similar on easy tasks but separates sharply as exploration becomes more demanding. Our process-level analysis opens a new avenue in web agent evaluation, providing fine-grained and actionable insight into where and how each agent should be improved.

---


### 220. [The Reservoir Attention Network: Cross-Pass State in Pretrained Transformers via Content-Addressable Reservoir Injection](https://arxiv.org/abs/2606.15678)

**<font color=#1a73e8>作者：</font>** Emma Leonhart  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A feasibility and dynamics study of the Reservoir Attention Network (RAN), an architecture that injects a fixed, randomly-initialized reservoir into the mid-layer attention of a pretrained transformer to carry state across forward passes. Experiments span GPT-2 (124M, 355M) to Qwen2.5 (0.5B, 1.5B) on a single consumer GPU. The tasks are minimal probes chosen to isolate individual mechanisms; the broader always-alive agent vision is treated throughout as compute-limited future work, not a claim of this paper. The reservoir is left untrained (fixed random) by design: this isolates whether untrained recurrent dynamics alone suffice to carry usable cross-pass state, leaving trained recurrence as a complementary, more expensive direction.

---


### 221. [3D Consistency Optimization for Self-Supervised Monocular Video Depth Estimation](https://arxiv.org/abs/2606.15681)

**<font color=#1a73e8>作者：</font>** Yuanye Liu, Ke Zhang, Junzhe Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable monocular video depth estimation is crucial for downstream 3D reasoning and embodied AI in endoscopic navigation. However, existing self-supervised approaches typically treat video frames independently or rely on weak temporal regularization. These methods, lacking a holistic perception of the underlying 3D scene, inevitably suffer from geometrically inconsistent predictions and severe cross-frame drift. To address these limitations, we introduce a new paradigm that recasts sequential video depth estimation as an unconstrained multi-view 3D reconstruction problem, enabling full exploitation of the powerful geometric priors embedded in recent 3D foundation models. The core of our approach is a 3D consistency optimization framework driven by three constraints: image-level photometric rendering, explicit world-coordinate geometric alignment, and multi-scale temporal gradient consistency. Such unified optimization elegantly anchors isolated frames to a globally coherent 3D structure. Our method has been validated in both the self-supervised training scenarios and challenging zero-shot clinical environments. Results show that the proposed approach achieves state-of-the-art spatial accuracy, outperforming the frame-based, video-based depth estimators and the multi-view 3D reconstruction baselines.

---


### 222. [ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training](https://arxiv.org/abs/2606.15682)

**<font color=#1a73e8>作者：</font>** Janghwan Lee, Sihwa Lee, Jinseok Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve strong problem-solving through long chain-of-thought, but their deployment is constrained by the high cost of full-precision inference and growing KV cache footprints. Microscaled FP4 formats enable efficient FP4 deployment; however, fully quantizing weights, activations, and KV caches (W4A4KV4) causes severe reasoning degradation that existing PTQ and QAT fail to recover. We identify that FP4 failures concentrate on low-entropy tokens--precise symbolic commitments such as digits and operators--where quantization noise inflates sampling errors that cascade through reasoning traces. Based on this insight, we propose ReQAT, a reasoning-centric FP4 training framework with three components: (i) Trace-Aligned QAT (TAQ), which revisits identical reasoning traces to focus updates on critical low-entropy decisions; (ii) Selective Entropy Minimization (SEM), which reinforces confidence at low-entropy positions; and (iii) Q-FIT, a quantization-friendly initialization that jointly calibrates RoPE-consistent KV cache transformations to stabilize QAT. Under the same training budget, ReQAT not only recovers but surpasses BF16 fine-tuning accuracy, while delivering up to 3.9x throughput speedup on NVIDIA DGX Spark and 3.1x on B200.

---


### 223. [Multi-agent Framework for Time-Sensitive Complementary Collaboration in Minecraft](https://arxiv.org/abs/2606.15684)

**<font color=#1a73e8>作者：</font>** Juheon Yi, Jinglu Wang, Xiaoyi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present TickingCollabBench, a Minecraft-based multi-agent benchmark for a novel class of time-sensitive complementary collaboration tasks. Our benchmark reflects four core characteristics of real-world collaboration: agent heterogeneity, mandatory collaboration, dynamic environments, and strict real-time constraints with failure risks. To enable this, we develop the TickingCollab framework, which supports the generation of diverse dynamic environments and abstracts Minecraft's primitive APIs to enable declarative YAML task specifications for composing these events. Building on this, we design a feasibility-aware automated benchmark generation pipeline, where an LLM drafts structurally diverse task configurations and feasibility verifier filters out invalid ones using approximate constraints. Evaluations demonstrate that lang latency and inherent difficulty of coordinating under partial observability and agent heterogeneity cause LLMs to frequently fail under dynamic environments and fall significantly short of a global-knowledge oracle.

---


### 224. [Multi-Fidelity SINDy: Sparse Discovery of Nonlinear Dynamical Systems with Fidelity-Weighted Measurements](https://arxiv.org/abs/2606.15690)

**<font color=#1a73e8>作者：</font>** Filippo Zacchei, Ana Larrañaga, Attilio Frangi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data from simulations and experiments are rarely noise-free and often exhibit heterogeneous levels of fidelity. Measurement uncertainty may vary across repeated observations, sensing devices, or even within a single experiment. This work addresses the problem of discovering nonlinear dynamical systems from such inhomogeneous data. We extend the Sparse Identification of Nonlinear Dynamical Systems (SINDy) framework to account for variable noise levels by combining Ensemble SINDy and Weak SINDy within a weighted regression formulation derived from generalized least squares. A statistical justification for the weighting strategy is also provided. The methodology is validated on several benchmark systems, including ordinary and partial differential equations. In addition, we show the benefit of multi-fidelity integration for forecasting the dynamics of a double pendulum system. The results confirm that the proposed approach mitigates the adverse effects of heteroscedastic noise and that repeated, low-cost, low-quality measurements can improve model recovery, in some cases matching or outperforming reconstructions obtained using only high-fidelity data.

---


### 225. [When Generator Replay Degrades: Projected Rehearsal Orchestration for Heterogeneous Federated Class-Incremental Learning](https://arxiv.org/abs/2606.15695)

**<font color=#1a73e8>作者：</font>** Thinh T. H. Nguyen, Khoa D. Doan, Binh T. Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated class-incremental learning (FCIL) becomes substantially harder when clients observe different label subsets, progress through tasks at different stages, and provide uneven supervision for the same semantic concepts. Existing FCIL methods often preserve old knowledge through input-space synthesis, but they can be fragile under heterogeneous task streams and difficult to transfer across modalities. To alleviate such issues, we propose PRO, a framework that replaces synthetic input replay with projected rehearsal orchestration. To remove external pretraining, we evaluate all methods under the same warmup. After this, PRO maintains compact class-level projected memories on the server and allows clients perform balanced pseudo multi-task training over current examples and old projected memories. To handle stronger representation drift, we further introduce PRO-MAX, which augments PRO with neighborhood-weighted memory alignment while preserving the same server-light principle that the server only aggregates model updates and memory statistics. Across image, text, and graph benchmarks, PRO and PRO-MAX improve retention and final utility under heterogeneous streams while remaining competitive in homogeneous FCIL. Even when baselines are given expanded replay budgets, they degrade under supervision imbalance and stage misalignment, indicating that replay quantity alone does not resolve replay-quality failures. Additional weak-task diagnostics further show that larger replay mismatch is associated with larger downstream degradation, while our method keeps projected memories better aligned with the evolving representation.

---


### 226. [Robust Transformer-Based One-Step Stock Index Forecasting via Shifted Data Augmentation](https://arxiv.org/abs/2606.15701)

**<font color=#1a73e8>作者：</font>** Tien Thanh Thach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have shown remarkable success in sequence modeling, yet their direct application to financial time series remains challenging due to noisy signals, short-memory dynamics, and distributional shifts. This paper proposes a modified Transformer architecture for one-step stock index forecasting, combined with advanced learning-rate scheduling and a novel Shifted Data Augmentation (SDA) technique. We evaluate the proposed framework on two benchmark stock index datasets, VN30 and S&P 500. Experimental results demonstrate that cosine annealing with warmup consistently improves forecasting accuracy over the generalized inverse-power scheduler. Furthermore, SDA substantially reduces forecasting errors and run-to-run variability while improving robustness to hyperparameter selection. The combination of cosine annealing scheduling and SDA achieved the best performance on both datasets, indicating that data augmentation can play a more important role than increasing model complexity in Transformer-based financial forecasting. These findings provide a practical and computationally efficient approach for robust stock index forecasting in noisy financial environments.

---


### 227. [Artificial Intelligence Index Report 2026](https://arxiv.org/abs/2606.15708)

**<font color=#1a73e8>作者：</font>** Sha Sajadieh, Loredana Fattorini, Raymond Perrault 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Welcome to the ninth edition of the AI Index report. As AI continues to advance rapidly, the question becomes whether the systems built around it can keep up. Governance frameworks, evaluation methods, education systems, and the data infrastructure needed to track AI's impact are struggling to match the pace of the technology itself. That gap between what AI can do and how prepared we are to manage it runs through every chapter of this year's report. New in this edition, the report tracks how AI is being tested more ambitiously across reasoning, safety, and real-world task execution, and why those measurements are increasingly difficult to rely on. It also features new estimates of generative AI's economic value alongside emerging evidence of its labor market effects, an analytical framework on AI sovereignty, and a science chapter developed in collaboration with Schmidt Sciences. For the first time, the report features standalone chapters on AI in science and AI in medicine, reflecting AI's growing impact across these two domains.

---


### 228. [Odds Law: The Decomposition Algebra On How Intelligence Organizes Itself to Solve Difficult Problems Reliably](https://arxiv.org/abs/2606.15712)

**<font color=#1a73e8>作者：</font>** Hidayet Aksu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We ask a structural question: given unreliable elementary problem-solvers, what organizations of them solve hard problems reliably, and what are the limits? We develop a $decomposition~algebra$: elementary solvers are morphisms in a stochastic category, and four combinators (sequential composition, parallel ensembling, verification gating, and recursive reduction) generate the space of compound solvers. We equip this algebra with two homomorphisms, a $reliability$ valuation into the ordered monoid $([0,1],\le)$ and a $cost$ valuation into a commutative semiring, and we derive the composition laws that govern how reliability flows through structure. Our central results are (i) a $verification~odds~law$ (the result that names this report), showing that a verification gate multiplies the odds of correctness by the verifier's likelihood ratio $\Lambda$, so that $k$ conditionally independent gates yield geometric amplification; (ii) a $reliability~amplification~theorem$, giving target reliability $1-\delta$ at $O(\log 1/\delta)$ verification depth whenever $\Lambda>1$; and (iii) a $threshold~dichotomy$: above the critical parameters reliability can be driven arbitrarily close to one at logarithmic cost, while at or below them no amplification is possible. We then show that $self-organization$ is the least fixed point of a monotone improvement operator on the complete lattice of strategies, and that this fixed point equalizes marginal log-odds gain per unit cost. Finally, we prove matching limits: an information ceiling bounds per-gate amplification by a divergence quantity; shared error causes create a strictly positive voting floor, so diversity is $necessary$ for unbounded amplification. Reliability, in short, is neither free nor magical: it is bought with independent information, arranged by composition, and bounded by the verifier.

---


### 229. [InstantForget: Update-Free Backdoor Unlearning with Inference-Time Feature Reset](https://arxiv.org/abs/2606.15730)

**<font color=#1a73e8>作者：</font>** Zhenyu Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backdoor unlearning aims to remove a malicious trigger behavior from a deployed model while preserving clean utility. We study the update-free inference-time setting, where model parameters remain frozen. First, we audit a common projection assumption under oracle paired clean and triggered features. Projection succeeds mainly on BadNets and leaves WaNet, Blended, and SIG at 0.683, 0.888, and 0.941 ASR on CIFAR-10 ResNet-18. This failure is not explained by spectral compactness, spatial locality, or subspace misalignment. It is predicted by a logit-triplet gap involving the target margin, target-logit drop, and non-target logit rise. We then introduce InstantForget, a clean-calibrated gated reset that flags anomalous features with a Mahalanobis score and moves only flagged features toward a neutral non-target representation. With one fixed operating point selected on held-out triggered validation, InstantForget reduces average ASR to 0.071 across four non-adaptive CIFAR-10 triggers without triggered samples or parameter updates at deployment. It also reaches 0.981 detection AUROC and transfers to six of eight tested backbones. Reported failures under WaNet, ModelNet10 point blend, two backbone geometries, and adaptive feature-compactness attacks define the method's scope.

---


### 230. [EHRNote-ChatQA: A Benchmark for Evidence-Grounded Multi-Turn Clinical Question Answering over Longitudinal Discharge Summaries](https://arxiv.org/abs/2606.15735)

**<font color=#1a73e8>作者：</font>** Jiyoun Kim, Muhan Yeo, Eunhye Jang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discharge summaries are crucial clinical documents containing the context of a patient's overall hospital stay, and are routinely reviewed by medical experts for patient readmission, ongoing care, and diagnostic decision-making. When reviewing them, medical experts often must iteratively synthesize information across multiple summaries while verifying the evidence supporting each answer. Although large language models (LLMs) are increasingly explored for clinical question answering, existing benchmarks do not sufficiently reflect this setting: they often evaluate exam-style medical knowledge or focus on single-turn question answering with limited evidence-grounding evaluation. We introduce EHRNote-ChatQA, the first benchmark for evidence-grounded multi-turn clinical question answering over patients' multiple discharge summaries. Built from de-identified MIMIC-IV discharge summaries, EHRNote-ChatQA contains 967 patient-level multi-turn samples spanning one to five notes and 16,072 medical-expert-verified QA pairs (8,036 content questions, each paired with an evidence-grounding question) across eight clinical categories. The benchmark is constructed through an expert-informed pipeline combining discharge-summary structuring schema, expert-curated multi-turn QA templates, and LLM-based generation, followed by review and revision of every single QA sample by 11 medical experts. Benchmarking 22 open- and closed-source LLMs reveals several challenges, including that LLMs struggle more with evidence grounding than content answering, multi-turn errors compound across turns, and single-turn clinical QA performance does not reliably transfer to this setting. These findings establish EHRNote-ChatQA as a rigorous and practical benchmark for evaluating clinical QA systems. The dataset will be made publicly available through PhysioNet credentialed access.

---


### 231. [A Self Consistency Based Reranking for Narrative Question Answering](https://arxiv.org/abs/2606.15741)

**<font color=#1a73e8>作者：</font>** Molham Mohamed, Ali Hamdi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Narrative question answering (NQA) is a challenging task in natural language processing that requires models to understand long textual contexts, capture relationships across events, and generate coherent responses. Despite recent advances in pretrained language models, most existing approaches rely on a single decoding output during inference, making them sensitive to generation variability and often resulting in incomplete or inconsistent answers .To address this limitation, we propose a self-ensemble Self-Consistency-Based reranking framework for narrative question answering. The proposed method generates multiple candidate answers for each story-question pair and selects the final answer based on semantic agreement among the generated responses. This allows the model to explore diverse answer formulations while improving robustness through consensus-based selection without requiring modifications to the underlying architecture .The framework combines pretrained and fine-tuned language generation with multi-answer inference and similarity-based reranking. We evaluate the proposed approach on the NarrativeQA dataset using multiple models, including FLAN-T5 (Base and Small) and Pegasus-Large, under both baseline and fine-tuned settings .Experimental results demonstrate that the proposed method consistently improves performance across all models. In particular, FLAN-T5-Base achieves the best overall performance, improving from 82.32% to 86.66% (+4.34%) when combined with self-ensemble inference. Additionally, the largest improvement is observed with Pegasus-Large, which increases from 72.50% to 87.07% (+14.57%), highlighting the effectiveness of the proposed strategy.

---


### 232. [From Correlation to Causation in Lane Change Prediction for Automated Driving: A Causal Explanation Framework](https://arxiv.org/abs/2606.15756)

**<font color=#1a73e8>作者：</font>** Mohamed Manzour, Aditya Kumar, Augusto Luis Ballardini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lane-change prediction is a central task in intelligent vehicles, where early maneuver anticipation can support safer decision-making. However, many existing approaches mainly learn statistical associations between observed driving variables and future maneuvers, while overlooking the causal dependencies among the input variables themselves. This limits interpretability, especially when physically related variables such as longitudinal gap, relative longitudinal velocity, and Time-To-Collision (TTC) are treated as independent flat inputs. This article presents a causal-inference-based framework for lane-change prediction and explanation. The proposed approach combines linguistic feature construction, expert-constrained causal discovery, deep structural causal modeling with Deep End-to-end Causal Inference (DECI), intervention-based effect analysis, refutation testing, and recursive causal-chain explanation. The objective is not only to predict the future maneuver, but also to identify candidate variables that directly contribute to the prediction, the upstream factors influencing them, and the causal chains through which these effects propagate. The framework achieves average F1-scores above 95% during the first three seconds before the lane-marking crossing event. Beyond prediction accuracy, the framework uses intervention-based effect analysis to distinguish influential from weakly influential variables under the learned causal structure. It further distinguishes candidate direct contributors from mediated effects and generates contrastive causal-chain explanations that clarify why the predicted maneuver is favored and why the alternative maneuvers are less supported. The main contribution is therefore a mechanism-aware lane-change prediction pipeline that moves beyond correlation-based classification toward more interpretable causal reasoning for maneuver prediction.

---


### 233. [The Data Manifold under the Microscope](https://arxiv.org/abs/2606.15760)

**<font color=#1a73e8>作者：</font>** Marios Koulakis, Constantin Seibold  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A significant gap exists between theory and practice in deep learning. Generalization and approximation error bounds are often derived for simplified models or are too loose to be informative. Many rely on the manifold hypothesis and on geometric regularity such as intrinsic dimension, curvature, and reach. Progress requires insight into data-manifold geometry and suitable benchmarks, yet existing options are polarized: analytic manifolds with known geometry but limited applicability, or real-world datasets where geometry is only coarsely estimable. We introduce a benchmarking framework for studying data geometry. We repurpose and extend dSprites and COIL-20 with additional transformation dimensions and dense, axis-aligned sampling, and pair them with finite-difference estimators that recover curvature, reach, and volume at near-ground-truth accuracy in a regime where general-purpose estimators are unreliable or difficult to deploy. The framework is intended as a controlled testbed, useful as a calibration environment for geometric estimators and a sandbox for probing theoretical assumptions. To illustrate its use, we present two application studies, namely assessing the scaling behavior of the bounds of Genovese et al. and Fefferman et al., and tracking the layer-wise geometry of a $\beta$-VAE, highlighting the behavior of current bounds and the value of controlled benchmarks for guiding and validating future theory.
A reference implementation is available at this https URL.

---


### 234. [The Circumplex Degeneracy Behind the Rare-Class Limit in Affect Recognition](https://arxiv.org/abs/2606.15763)

**<font color=#1a73e8>作者：</font>** Van Thong Huynh, Hong Hai Nguyen, Soo-Hyung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-the-wild expression recognition persistently fails on a few rare emotions, and the standard explanation is class imbalance. Through a controlled multi-task study on two benchmarks, we show the failure is instead a property of affect geometry: the rare classes are degenerate on Russell's circumplex, and that degeneracy bounds what any loss or cost can achieve. Our instrument is a circumplex-cost optimal-transport term that prices expression confusions by their valence-arousal distance. The term improves the official score and expression macro-F1, but a control most studies omit shows the gain is not geometric: a uniform cost, equivalent to a generic confidence penalty, matches it on Aff-Wild2 (p=0.625) and significantly exceeds it on AffectNet (+0.057 over base, larger than the circumplex). What the geometry reshapes is the structure of the errors, making them affectively nearer the truth on Aff-Wild2 (p=0.031 against the uniform control), an effect that does not survive on AffectNet, where a visual confound at the far corner of the circumplex overwhelms it. The rare-class failure, by contrast, is stable across both datasets we examine: the degenerate pairs (anger-fear on Aff-Wild2, anger-contempt on AffectNet) resist frequency-based interventions, the transport term, and an action-unit-augmented cost built specifically to separate them. We conclude that progress on rare expressions requires representations that distinguish the classes, not supervision that reprices their confusions, and we provide the controls and metrics needed to tell the two apart.

---


### 235. [Visualizing Uncertainty: Spatial Maps of Missing and Conflicting Evidence in Deep Learning](https://arxiv.org/abs/2606.15767)

**<font color=#1a73e8>作者：</font>** Dong Hyun Jeong, Feng Chen, Jin-Hee Cho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding when and why deep neural networks are uncertain is crucial for deploying reliable machine learning systems in safety-critical domains. While existing uncertainty quantification methods provide scalar measures of model confidence, they offer limited insight into which spatial regions of an input contribute to different types of uncertainty. We propose a novel visualization framework, Uncertainty Activation Map (UAM), that combines Evidential Deep Learning (EDL) with Full-Gradient Class Activation Mapping (FullGrad) to generate interpretable spatial uncertainty activation maps. Our approach distinguishes between two fundamental types of uncertainty: vacuity, representing lack of evidence, and dissonance, capturing conflicting evidence between competing hypotheses. By leveraging the complete gradient decomposition property of FullGrad and the principled uncertainty quantification of Subjective Logic, our method produces theoretically grounded visualizations that highlight specific image regions responsible for model uncertainty. With this framework, vacuity and dissonance activation maps are generated by computing belief-weighted attributions, enabling identification of where models lack knowledge versus where they encounter ambiguous evidence. Extensive evaluations across multiple benchmark datasets demonstrate that the proposed framework effectively addresses the critical gap between uncertainty quantification and explainability, providing intuitive visual feedback to assess model reliability in complex visual recognition tasks.

---


### 236. [Ellipse Meets Bit-Planes: A Novel Approach to RNFL based Glaucoma Detection Using Advanced Image Processing and Deep Learning](https://arxiv.org/abs/2606.15772)

**<font color=#1a73e8>作者：</font>** Snigdha Paul, Sambit Mallick, Anindya Sen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work proposes an integrated pipeline for automatic glaucoma detection method from easily available colour fundas images based on an adaptive algorithm for ellipse-based polar transformation, to enhance the analysis of the Retinal Nerve Fiber Layer (RNFL) as the primary biomarker for observing glaucomatous changes, regardless of optic disc and macula position. Utilizing this transformation, we introduce two distinct frameworks tailored to different operational needs. The first framework, a deep learning-inspired feature fusion approach, achieves a 99.3% detection rate, ideal for settings where high precision is essential, despite higher computational demands. The second framework employs a novel image-processing algorithm based on bit-plane slicing, offering 92.31% accuracy and optimized for environments requiring rapid inference with minimal resource consumption. Both frameworks provide scalable and cost-effective solutions for early glaucoma detection. This study highlights the potential of RNFL-based diagnostic tools in addressing the global challenge of glaucoma, particularly in underserved regions.

---


### 237. [Faithful Action-unit Causal Reasoning for Counterfactually Faithful Emotion Explanations](https://arxiv.org/abs/2606.15779)

**<font color=#1a73e8>作者：</font>** Van Thong Huynh, Hong Hai Nguyen, Thuy Pham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal models can name the action units (AUs) behind a facial emotion, but their AU->emotion rationales are typically plausible rather than faithful: nothing forces the AUs a model invokes to be the AUs that actually drive its prediction. We cast AU->emotion reasoning as a counterfactual-consistency problem between the rationale, the label, and a structural AU->emotion causal graph G, and propose FACR, which grounds the reasoner in an independently induced, polarity-aware G and trains a counterfactual-faithfulness objective: a do-intervention on an AU that G marks causal for a class must move the prediction, while one it marks irrelevant must leave it unchanged. Faithfulness is thereby both trainable and measurable through a matching interventional metric, which we evaluate against a known causal structure, the PSPI pain-AU composition, as no existing affective-reasoning benchmark allows. We are explicit that this metric tests fidelity to the supplied structure rather than its rediscovery: it asks whether the trained reasoner invokes the AUs the structure marks causal, on held-out subjects and a second dataset. Under subject-independent evaluation on UNBC-PAIN, the objective raises the agreement between the invoked AUs and the PSPI composition from a no-objective baseline of 0.08 to 0.57, at a small detection cost; an unfaithfulness control attributes the gain to the objective. On a cross-dataset emotion transfer, the objective likewise raises fidelity to G on a seven-class task (0.50 to 0.84). Finally, we attach a language verbalizer and extend the audit to the generated text: biasing each action unit's emission by its latent activation makes the rationale faithful by construction, so that ablating an AU removes it from the explanation, a property that transfers to a second language-model backbone, whereas a freely generated rationale is unfaithful.

---


### 238. [Bayesian Networks with Latent Time Embedding for Stage-Aware Causal Modeling of Alzheimer's Disease Progression](https://arxiv.org/abs/2606.15784)

**<font color=#1a73e8>作者：</font>** Nguyen Linh Dan Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) progression is often described through the amyloid-tau-neurodegeneration, or AT(N), cascade. However, most longitudinal models represent this cascade either as a fixed sequence of biomarkers or as a black-box forecasting task. This makes it difficult to determine when biologically guided biomarker relationships influence future regional pathology. In this study, we introduce Bayesian Networks with Latent Time Embedding (BN-LTE), a Bayesian structural framework for stage-aware modeling of AD progression. BN-LTE estimates disease pseudotime from baseline biomarker profiles and constrains directed dependencies according to biologically plausible AT(N) ordering. Posterior spline-varying structural equations are then used to link initial multimodal measurements with future annualized regional tau-PET change. Across repeated subject-disjoint evaluations using ADNI data, BN-LTE shows strong spatial reconstruction of tau progression compared with the included forecasting baselines. Beyond spatial reconstruction, BN-LTE recovers posterior stage-varying AT(N)-constrained effects and identifies a mid-pseudotime window of amyloid sensitivity. This window is supported by model-implied g-formula contrasts, root-adjusted AIPW, mechanism-sensitive ablations, and robustness analyses across spline and prior specifications. Overall, these findings position BN-LTE as a Bayesian structural framework for forecasting tau progression while examining stage-dependent AT(N)-cascade mechanisms in observational longitudinal neuroimaging data. Our code is available at this https URL.

---


### 239. [Domain-Guided Prompting of the Segment Anything Model for Seismic Interpretation: The Role of Attributes, Visualization, and Hybrid Prompts](https://arxiv.org/abs/2606.15786)

**<font color=#1a73e8>作者：</font>** Aniq Ahmad, Heather Bedle, Ahmad Mustafa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advent of large pretrained foundation models for computer vision has significantly improved the efficiency of visual data interpretation. The Segment Anything Model (SAM), in particular, offers powerful zero shot segmentation capabilities through prompt based interaction, thus making it a promising tool for seismic interpretation. However, most existing applications of SAM rely on fine tuning for specific geological targets, which requires extensive labeled data, incurs high computational cost, and often compromises the model's generalization capability. In this study, we introduce a principled framework for zero shot adaptation of foundation models to seismic data. The framework is built on two key components: (1) aligning seismic attributes and visualization choices (e.g., colormaps) with the geological target of interest, and (2) employing a hybrid prompting strategy that combines sparse user defined point prompts with dense mask prompts derived from SAM's internal feature activations. We systematically evaluate this framework across multiple geological targets, datasets, prompt configurations, and seismic attribute representations. Our results demonstrate that geologic target aware selection of seismic attributes and colormaps, combined with hybrid prompting, enhances the separability of geological features and improves boundary delineation and segmentation accuracy relative to point based prompting alone. Our findings show that, when these components are jointly applied, SAM can achieve competitive segmentation performance in a fully zero shot setting, thereby eliminating the need to retrain SAM for each geologic feature. This work establishes a practical and scalable pathway to leverage foundation models in seismic interpretation, reducing reliance on labeled data while preserving model generality.

---


### 240. [Proximal Policy Optimization for Amortized Discrete Sampling](https://arxiv.org/abs/2606.15793)

**<font color=#1a73e8>作者：</font>** Anna Zykova-Myzina, Timofei Gritsaev, Daniil Tiapkin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper explores policy gradient algorithms for training stochastic policies to sample from structured discrete probability distributions under the Generative Flow Network (GFlowNet) framework. Building on extensive theoretical connections between GFlowNets and entropy-regularized reinforcement learning, we derive equivalents of standard policy gradient algorithms for training GFlowNets, as well as experimentally explore their various methodological aspects, including baseline training and advantage estimation. Most importantly, our work is the first to derive and successfully apply proximal policy optimization to GFlowNets, showing its improved convergence speed and data efficiency compared to standard GFlowNet training objectives on benchmarks ranging from synthetic energies to molecular graph generation.

---


### 241. [DifFRACT: Diffusion Feature Reconstruction and Attribution for Circuit Tracing](https://arxiv.org/abs/2606.15796)

**<font color=#1a73e8>作者：</font>** Artyom Mazur, Nina Konovalova, Aibek Alanov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability seeks to explain neural network behavior by decomposing model computations into interpretable features and circuits. While transcoder-based circuit tracing has recently enabled detailed causal analyses of large language models, multimodal diffusion transformers for image generation remain comparatively opaque. We still lack tools for understanding how semantic information propagates across denoising steps and how text and image representations interact within double-stream MM-DiT architectures. Existing methods provide only partial insight: attention maps expose a limited view of token interactions, while sparse autoencoders can discover interpretable features but do not directly reveal how these features are transformed and composed through nonlinear MLP layers. In this work, we extend transcoder-based circuit tracing to multimodal diffusion transformers. We train timestep-conditioned transcoders that faithfully approximate the input-output behavior of MLP sublayers in FLUX.1[schnell]. By replacing MLPs with transcoders and linearizing the remaining computation, we obtain exact feature-to-feature attribution and recover compact, interpretable circuits. Empirically, our transcoders match or slightly outperform sparse autoencoders on the sparsity-faithfulness tradeoff. The resulting circuits reveal mechanisms underlying attribute binding and cross-stream semantic propagation, and provide causal explanations for systematic generation errors. Moreover, circuit-guided interventions are substantially more precise and effective than standard SAE-based steering. Our results demonstrate that transcoder-based circuit analysis is feasible for state-of-the-art diffusion transformers and provides a powerful framework for understanding and controlling multimodal generative models. The code is available at this https URL

---


### 242. [Unassigned Agents in Compilation-based Multi-agent Path Finding](https://arxiv.org/abs/2606.15797)

**<font color=#1a73e8>作者：</font>** Pavel Surynek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compilation-based techniques represent an important stream of solvers for multi-agent path finding (MAPF) due to their modularity and adaptability for non-standard variants of the problem. While in the standard MAPF the task is to navigate all agents from their initial positions to given individual goal positions without any collision, variants where a different requirement for agents is used are also relevant. Such a variant is MAPF with unassigned agents (UA-MAPF) where some agents have the same setting as in the standard MAPF with initial positions and goals while the remaining agents have the initial position but have no goal - unassigned agents. Despite unassigned agent do not need to reach any goal position they have to be moved out of the way of the standard agents if needed which represent a specific challenge. We show in this paper that UA-MAPF can be expressed in recent compilation-based techniques for MAPF based on formulating the problem as Boolean satisfiability, namely we adapt SMT-CBS and NRF-SAT, the recent solvers based on counterexample guided abstraction refinement and non-refined abstractions.

---


### 243. [CPS4: Class Prompt driven Semi-Supervised Spine Segmentation with Class-specific Consistency Constraint](https://arxiv.org/abs/2606.15802)

**<font color=#1a73e8>作者：</font>** Qingtao Pan, Hongzan Sun, Bing Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Model (VLM) has great potential to enhance the quality of pseudo labels in semi-supervised spine segmentation by leveraging textual class prompts to generate segmentation map, but no one has studied it yet. Although promising, it lacks explicit constraints to ensure consistency between spine class prompts and spine unit region, resulting in unsatisfactory performance in multi-class segmentation map generation. In this paper, we propose CPS4, the first text-guided semi-supervised spine segmentation network using class prompts to enhance the quality of spine pseudo labels. Specifically, CPS4 is implemented through two training stages. (i) Class-specific consistency constrained VLM pretraining stage: we propose token- and pixel-level attention loss to optimize the consistency between class prompts and spine units, forcing the textual class prompt to be closely coupled with the target spine unit in the semantic space. (ii) Class Prompt driven semi-supervised spine segmentation stage: using the pretrained vision-text encoder, we derive each class-specific binary segmentation map for the unlabeled spine image and integrate them into an unified multi-class segmentation map, improving the quality of the spine pseudo label generated by the semi-supervised spine segmentation network. Experimental results show that our CPS4 achieves superior spine segmentation performance with Dice of 80.44%, only using 5% labeled data on the public spine segmentation dataset, surpassing popular semi-supervised learning and VLM methods. Our code will be available.

---


### 244. [Continuous Cross-Domain Traffic State Prediction via Memory-Augmented Graph Liquid Time-Constant Networks](https://arxiv.org/abs/2606.15807)

**<font color=#1a73e8>作者：</font>** Jinrong Xiang, Ming Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic state prediction is a fundamental task in intelligent transportation systems. In practical applications, some regions suffer from limited traffic observations due to insufficient sensing infrastructure, making cross-domain knowledge transfer an important solution for data-scarce traffic prediction. However, existing cross-domain traffic prediction methods still face several limitations, including coarse-grained source-target adaptation, limited capability in handling unseen target-domain patterns, and insufficient modeling of continuous traffic dynamics under irregular or heterogeneous temporal conditions. To address these issues, this paper proposes a continuous cross-domain traffic prediction framework, termed Memory-Augmented Graph Liquid Time-Constant Network (MA-GLTC). Specifically, we first construct spatio-temporal units (STUs) to decompose traffic networks into transferable local units, enabling fine-grained knowledge alignment across domains. Then, a graph liquid time-constant network (GLTC) is developed to model graph-coupled traffic evolution in continuous time. Different from generic graph neural ODE-based models, GLTC introduces graph-coupled recurrent conductance into liquid time-constant dynamics, allowing node states to evolve with leakage, adaptive time constants, and neighborhood-aware feedback. Furthermore, a Memory-based Transfer Storage (MTS) mechanism is designed to preserve source-domain knowledge, retrieve matched traffic patterns, and update reliable target-domain patterns when unseen states emerge. Experiments on five public traffic datasets demonstrate that MA-GLTC consistently outperforms representative innerdomain and cross-domain baselines in both short-term and longterm prediction tasks. Compared with the second-best method, MA-GLTC reduces the average prediction errors by 3.02%, 0.33%, 8.92%, 10.09%, and 2.11%, respectively.

---


### 245. [FuseChain: Runtime Evidence Reconstruction for Software Supply-Chain Attacks](https://arxiv.org/abs/2606.15811)

**<font color=#1a73e8>作者：</font>** Zhuoran Tan, Yutian Tang, Jeremy Singer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software supply-chain (SSC) attacks are increasingly multi-stage, cross-source, and temporally distributed. A single attack campaign may leave weak and fragmented traces across multi-source telemetry that captures different granularities and perspectives of runtime behavior. Existing runtime detection systems often analyze these sources independently, making it difficult to identify low-frequency attack evidence or reconstruct the temporal context in which it appears. We present FUSECHAIN, a runtime detection framework that represents multi-source software supply-chain telemetry as a temporal heterogeneous provenance graph over a unified event-time axis. By aligning package/runtime traces, process events, network telemetry, DNS/HTTP metadata, and security alerts on a unified temporal graph, FuseChain captures cross-source dependencies and sparse attack evidence that may be ambiguous within any individual source. It learns anomaly-centric temporal representations from benign-prefix telemetry and performs deployable attack-stage reconstruction through a lightweight decoder on top of a frozen anomaly backbone. Our experiments show that jointly optimizing anomaly detection and stage prediction is ineffective under sparse and imbalanced runtime supply-chain telemetry. Across seven SSC attack scenarios, FuseChain improves deployable stage reconstruction from 0.369 to 0.881 Stage Recall@500 with a frozen-backbone decoder, while adaptive retrieval further increases observable-stage recall from 0.524 to 0.655 without modifying the detector. These results highlight the deployable value of decoupling runtime SSC anomaly detection from downstream attack-stage interpretation.

---


### 246. [Brownian Kernel Ladders](https://arxiv.org/abs/2606.15812)

**<font color=#1a73e8>作者：</font>** Mahdi Mohammadigohari, Giuseppe Di Fatta, Giuseppe Nicosia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constructing mathematically tractable function spaces that capture hierarchical compositional representations remains a central challenge in statistical learning theory. We introduce Brownian kernel ladders (BKLs), a recursively defined hierarchy of integral reproducing kernel Hilbert spaces generated through Brownian-kernel integral constructions. Starting from linear functionals, each layer is obtained by integrating Brownian kernels over probability measures supported on subsets of the previous layer, yielding a recursive function-space model in which depth is encoded directly through the hierarchy.
Based on this framework, we define canonical BKL spaces together with an associated complexity functional. We establish several analytical and statistical properties of these spaces. In particular, we show that BKL spaces form quasi-Banach spaces, satisfy depth-dependent Hölder regularity estimates, and exhibit strict monotonicity with respect to depth. We further prove existence results for regularized empirical risk minimization and derive Gaussian complexity bounds that remain uniformly controlled with respect to both the ambient dimension and the hierarchy depth.
A key ingredient of the analysis is a combinatorial proof technique based on recursive subset decompositions and Brownian-kernel threshold representations. These estimates yield excess-risk guarantees of near-parametric order for regularized empirical risk minimization over BKL spaces. Our results provide a mathematically tractable hierarchical function-space framework for studying compositional representations in deep learning.

---


### 247. [On Defining Erasure Harms for NLP](https://arxiv.org/abs/2606.15815)

**<font color=#1a73e8>作者：</font>** Yu Lu Liu, Arnav Goel, Jackie Chi Kit Cheung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The deployment of NLP systems has raised concerns about harms they might produce, including representational harms. Recent literature has begun to conceptualize and measure one such harm, the harm of erasure. Nevertheless, the field lacks a clear and cohesive conceptual foundation for identifying and measuring erasure. Existing conceptualizations of erasure are often broad -- making it difficult to identify what is needed to establish and measure erasure -- or else specific to particular settings -- facilitating measurement for those settings but potentially challenging to adapt to other settings. To address this gap, we develop and propose a structured definition of erasure that clarifies what components are necessary for establishing whether erasure has occurred, which practitioners need to explicitly articulate and operationalize in order to measure erasure.

---


### 248. [SACE: Concept Erasure at the Semantic Singularity in Visual Autoregressive Models](https://arxiv.org/abs/2606.15819)

**<font color=#1a73e8>作者：</font>** Siya Yang, Nanxiang Jiang, Zhaoxin Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid progress of visual autoregressive (VAR) models has unlocked a transformative frontier for high-fidelity text-to-image synthesis, while heightening concerns over the safety alignment of generated content. Naive application of existing erasure techniques to VAR models causes catastrophic semantic collapse and visual artifacts, since they are predominantly designed for the homogeneous denoising steps of diffusion models. To address this foundational challenge, we first propose the Semantic Singularity Axiom, which posits that any target semantic concept embedded within a prompt is definitively locked at Scale-0. Then rigorously validate this axiom through our proposed Incremental Semantic Saliency Analysis (ISSA),which also enable the community to transparently inspect the coarse-to-fine semantic injection process. Guided by this insight, we introduce the first scale-aware concept erasure framework (SACE) for VAR models. By strictly confining interventions to the first scale, our approach couples an Entropy-Regularized Erasure Objective to prevent high-entropy sampling degeneration, alongside a restorative preservation loss to safely anchor the integrity of entangled benign priors. Extensive experiments demonstrate that our method achieves surgical concept erasure performance across various domains with minimal training overhead, timely and elegently resolute the critical safety vulnerabilities inherent in emerging VAR architectures. Code is available at: this https URL}{this https URL.

---


### 249. [An Integrated System for Real-Time Student Assessment and Career Guidance Using Neural Networks in Computing Disciplines](https://arxiv.org/abs/2606.15831)

**<font color=#1a73e8>作者：</font>** Sakir Hossain Faruque, Md. Jubair Hossain, Sharun Akter Khushbu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many undergraduate students in Computer Science (CS) and Software Engineering (SWE) struggle to identify suitable career paths, particularly when their academic performance, abilities, and interests do not fully align. To address this issue, this study proposes an AI-driven Student Assessment and Career Prediction System that integrates a Career Guidance Expert (CGE) system with a Web-Based Student Assessment (WBSA) platform. Within the integrated framework, CGE enhances personalized career recommendations using AI while also assisting students after graduation in identifying suitable jobs, research domains, and higher study opportunities aligned with their skills and interests. The WBSA platform further strengthens interaction between students and faculty through assessments, personalized tasks, mentorship activities, and a secure real-time chat application. The CGE system employs a Multilayer Perceptron (MLP) model trained on real-world academic and extracurricular data collected using the snowball sampling method from the students of universities, achieving a validation accuracy of 94.71% in predicting personalized career paths. A pre-survey was conducted across universities to evaluate the proposed model before deployment. The WBSA system was developed as a modern web application using technologies such as this http URL, this http URL, and PostgreSQL to ensure scalability, responsiveness, and secure data management. The overall system is supported by a secure cloud-based infrastructure, the platform provides reliable performance while assisting graduates to select suitable career path in IT sector. In addition, a post-survey involving both students and faculty was conducted to gather feedback and further improve the overall effectiveness and usability of the system.

---


### 250. [SILAGE: Memory-Efficient, Full-Gradient-Free Nonconvex Optimization for Nested Finite Sums](https://arxiv.org/abs/2606.15832)

**<font color=#1a73e8>作者：</font>** Igor Sokolov, Laurent Condat, Peter Richtárik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Empirical risk minimization on massive datasets naturally exhibits a nested double finite-sum structure, where $N=nm$ total samples are logically or physically partitioned into $n$ blocks of size $m$ (e.g., in pooled data silos, out-of-core learning, or deliberate stratification). While variance-reduced methods achieve optimal oracle complexities for nonconvex objectives, they suffer from severe scaling bottlenecks in this centralized regime. Recursive estimators, such as PAGE, require periodic global full-gradient refreshes over all $nm$ samples, which are computationally expensive. Conversely, single-loop methods, such as SILVER, avoid such refreshes but require an impractical $\mathcal{O}(nm)$ memory footprint to store a control variate for every sample. In this paper, we propose SILAGE, a variance-reduced algorithm that addresses this trade-off. By actively exploiting the double-sum structure, SILAGE eliminates periodic global full-gradient refreshes over all $nm$ components (evaluating at most one local group gradient per iteration) while requiring only $\mathcal{O}(n)$ memory. Furthermore, we provide a tight convergence analysis that avoids pessimistic worst-case Lipschitz constants. Instead, SILAGE's complexity natively adapts to the underlying data geometry via nested functional similarities: across-group ($\delta_1$) and within-group ($\delta_2$) heterogeneity. Our results improve existing state-of-the-art bounds in several practically relevant regimes.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
